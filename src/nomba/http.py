from __future__ import annotations

import asyncio
import random
import threading
import time
from typing import Any

import httpx

from .exceptions import NombaAPIError, NombaAuthError

LIVE_BASE_URL = "https://api.nomba.com"
SANDBOX_BASE_URL = "https://sandbox.nomba.com"

# Status codes worth retrying: rate limit + transient server-side errors.
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def _compute_backoff(attempt: int, retry_after: str | None, backoff_factor: float) -> float:
    if retry_after:
        try:
            return float(retry_after)
        except ValueError:
            pass
    # exponential backoff with jitter: backoff_factor * 2^attempt, +/- 20%
    base = backoff_factor * (2 ** attempt)
    jitter = base * random.uniform(-0.2, 0.2)
    return max(0.0, base + jitter)


class NombaClient:
    """
    Low-level HTTP client for the Nomba API.

    Handles OAuth2 client-credentials authentication, token caching/refresh
    (with a lock so concurrent requests don't race to re-fetch a token),
    the `accountId` header that most endpoints require, and automatic
    retry-with-backoff for 429/5xx responses.

    Example:
        client = NombaClient(
            client_id="...",
            client_secret="...",
            account_id="...",
        )
        account = client.get(f"/v1/accounts/virtual/{account_ref}")
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        account_id: str,
        *,
        sandbox: bool = False,
        timeout: float = 30.0,
        max_retries: int = 3,
        backoff_factor: float = 0.5,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_id = account_id
        self.base_url = SANDBOX_BASE_URL if sandbox else LIVE_BASE_URL
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

        self._access_token: str | None = None
        self._token_expires_at: float = 0.0
        self._token_lock = threading.Lock()

        self._http = httpx.Client(base_url=self.base_url, timeout=timeout)

    # -- auth -----------------------------------------------------------

    def _fetch_token_locked(self) -> None:
        try:
            response = self._http.post(
                "/v1/auth/token/issue",
                headers={
                    "Content-Type": "application/json",
                    "accountId": self.account_id,
                },
                json={
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                },
            )
        except httpx.HTTPError as exc:
            raise NombaAuthError(f"Failed to reach Nomba auth endpoint: {exc}") from exc

        if response.status_code >= 400:
            raise NombaAuthError(
                "Failed to obtain access token",
                status_code=response.status_code,
                response_body=_safe_json(response),
            )

        body = _safe_json(response) or {}
        data = body.get("data", body)
        token = data.get("access_token")
        if not token:
            raise NombaAuthError(
                "Nomba auth response did not include an access_token",
                response_body=body,
            )

        expires_in = data.get("expires_in", 3600)
        self._access_token = token
        # refresh a little early to avoid edge-of-expiry failures
        self._token_expires_at = time.monotonic() + max(int(expires_in) - 60, 0)

    def _ensure_token(self) -> str:
        # fast path: token already valid, no lock needed
        if self._access_token is not None and time.monotonic() < self._token_expires_at:
            return self._access_token
        # slow path: only one thread should actually fetch; others wait then
        # re-check (the lock serializes them, avoiding a fetch stampede).
        with self._token_lock:
            if self._access_token is None or time.monotonic() >= self._token_expires_at:
                self._fetch_token_locked()
        assert self._access_token is not None
        return self._access_token

    def _invalidate_token(self) -> None:
        with self._token_lock:
            self._access_token = None

    # -- request helpers --------------------------------------------------

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        extra_headers: dict[str, str] | None = None,
        _attempt: int = 0,
        _retry_on_auth_failure: bool = True,
    ) -> dict[str, Any]:
        token = self._ensure_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "accountId": self.account_id,
            "Content-Type": "application/json",
        }
        if extra_headers:
            headers.update(extra_headers)

        try:
            response = self._http.request(
                method, path, json=json, params=params, headers=headers
            )
        except httpx.HTTPError as exc:
            raise NombaAPIError(f"Request to {path} failed: {exc}") from exc

        if response.status_code == 401 and _retry_on_auth_failure:
            # token may have been invalidated server-side; force refresh once
            self._invalidate_token()
            return self.request(
                method,
                path,
                json=json,
                params=params,
                extra_headers=extra_headers,
                _attempt=_attempt,
                _retry_on_auth_failure=False,
            )

        if response.status_code in RETRYABLE_STATUS_CODES and _attempt < self.max_retries:
            delay = _compute_backoff(
                _attempt, response.headers.get("Retry-After"), self.backoff_factor
            )
            time.sleep(delay)
            return self.request(
                method,
                path,
                json=json,
                params=params,
                extra_headers=extra_headers,
                _attempt=_attempt + 1,
                _retry_on_auth_failure=_retry_on_auth_failure,
            )

        body = _safe_json(response)

        if response.status_code >= 400:
            message = "Nomba API request failed"
            code = None
            if isinstance(body, dict):
                message = body.get("description", message)
                code = body.get("code")
            raise NombaAPIError(
                message,
                status_code=response.status_code,
                code=code,
                response_body=body,
            )

        return body if isinstance(body, dict) else {"data": body}

    def get(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return self.request("DELETE", path, **kwargs)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "NombaClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()


def _safe_json(response: httpx.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        return None


class AsyncNombaClient:
    """
    Async low-level HTTP client for the Nomba API (httpx.AsyncClient based).

    Mirrors NombaClient's behavior: OAuth2 client-credentials auth, token
    caching/refresh guarded by an asyncio.Lock, the `accountId` header, and
    automatic retry-with-backoff for 429/5xx responses.

    Example:
        client = AsyncNombaClient(
            client_id="...",
            client_secret="...",
            account_id="...",
        )
        account = await client.get(f"/v1/accounts/virtual/{account_ref}")
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        account_id: str,
        *,
        sandbox: bool = False,
        timeout: float = 30.0,
        max_retries: int = 3,
        backoff_factor: float = 0.5,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_id = account_id
        self.base_url = SANDBOX_BASE_URL if sandbox else LIVE_BASE_URL
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

        self._access_token: str | None = None
        self._token_expires_at: float = 0.0
        self._token_lock = asyncio.Lock()

        self._http = httpx.AsyncClient(base_url=self.base_url, timeout=timeout)

    # -- auth -----------------------------------------------------------

    async def _fetch_token_locked(self) -> None:
        try:
            response = await self._http.post(
                "/v1/auth/token/issue",
                headers={
                    "Content-Type": "application/json",
                    "accountId": self.account_id,
                },
                json={
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                },
            )
        except httpx.HTTPError as exc:
            raise NombaAuthError(f"Failed to reach Nomba auth endpoint: {exc}") from exc

        if response.status_code >= 400:
            raise NombaAuthError(
                "Failed to obtain access token",
                status_code=response.status_code,
                response_body=_safe_json(response),
            )

        body = _safe_json(response) or {}
        data = body.get("data", body)
        token = data.get("access_token")
        if not token:
            raise NombaAuthError(
                "Nomba auth response did not include an access_token",
                response_body=body,
            )

        expires_in = data.get("expires_in", 3600)
        self._access_token = token
        self._token_expires_at = time.monotonic() + max(int(expires_in) - 60, 0)

    async def _ensure_token(self) -> str:
        if self._access_token is not None and time.monotonic() < self._token_expires_at:
            return self._access_token
        async with self._token_lock:
            if self._access_token is None or time.monotonic() >= self._token_expires_at:
                await self._fetch_token_locked()
        assert self._access_token is not None
        return self._access_token

    async def _invalidate_token(self) -> None:
        async with self._token_lock:
            self._access_token = None

    # -- request helpers --------------------------------------------------

    async def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        extra_headers: dict[str, str] | None = None,
        _attempt: int = 0,
        _retry_on_auth_failure: bool = True,
    ) -> dict[str, Any]:
        token = await self._ensure_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "accountId": self.account_id,
            "Content-Type": "application/json",
        }
        if extra_headers:
            headers.update(extra_headers)

        try:
            response = await self._http.request(
                method, path, json=json, params=params, headers=headers
            )
        except httpx.HTTPError as exc:
            raise NombaAPIError(f"Request to {path} failed: {exc}") from exc

        if response.status_code == 401 and _retry_on_auth_failure:
            await self._invalidate_token()
            return await self.request(
                method,
                path,
                json=json,
                params=params,
                extra_headers=extra_headers,
                _attempt=_attempt,
                _retry_on_auth_failure=False,
            )

        if response.status_code in RETRYABLE_STATUS_CODES and _attempt < self.max_retries:
            delay = _compute_backoff(
                _attempt, response.headers.get("Retry-After"), self.backoff_factor
            )
            await asyncio.sleep(delay)
            return await self.request(
                method,
                path,
                json=json,
                params=params,
                extra_headers=extra_headers,
                _attempt=_attempt + 1,
                _retry_on_auth_failure=_retry_on_auth_failure,
            )

        body = _safe_json(response)

        if response.status_code >= 400:
            message = "Nomba API request failed"
            code = None
            if isinstance(body, dict):
                message = body.get("description", message)
                code = body.get("code")
            raise NombaAPIError(
                message,
                status_code=response.status_code,
                code=code,
                response_body=body,
            )

        return body if isinstance(body, dict) else {"data": body}

    async def get(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return await self.request("POST", path, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return await self.request("PUT", path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return await self.request("DELETE", path, **kwargs)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncNombaClient":
        return self

    async def __aexit__(self, *exc_info: Any) -> None:
        await self.close()

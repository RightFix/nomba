from __future__ import annotations

from typing import Any


class NombaError(Exception):
    """Base exception for all Nomba SDK errors."""


class NombaAPIError(NombaError):
    """Raised when the Nomba API returns a non-success response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        code: str | None = None,
        response_body: Any = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.response_body = response_body

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        parts = [super().__str__()]
        if self.status_code is not None:
            parts.append(f"(status={self.status_code})")
        if self.code is not None:
            parts.append(f"(code={self.code})")
        return " ".join(parts)


class NombaAuthError(NombaAPIError):
    """Raised when authentication with Nomba fails."""


class NombaValidationError(NombaError):
    """
    Raised locally (before any network call) when a request body is missing
    required nested fields per Nomba's own OpenAPI spec. This catches
    mistakes in nested objects (e.g. a missing field inside `order={...}`)
    that the generated method's flat signature can't enforce on its own.
    """

    def __init__(self, message: str, *, missing: list[str] | None = None) -> None:
        super().__init__(message)
        self.missing = missing or []

"""
Webhook signature verification, per Nomba's documented scheme
(https://developer.nomba.com/products/webhooks/signature-verification-new
and .../webhooks/introduction):

Headers sent with every webhook POST:
    nomba-signature            base64-encoded HMAC
    nomba-signature-algorithm  always "HmacSHA256"
    nomba-signature-version    currently "1.0.0"
    nomba-timestamp            RFC-3339 timestamp the payload was sent at

Signing scheme (confirmed from Nomba's own sample code):
    hashing_payload = ":".join([
        event_type,
        requestId,
        data.merchant.userId,
        data.merchant.walletId,
        data.transaction.transactionId,
        data.transaction.type,
        data.transaction.time,
        data.transaction.responseCode,
    ])
    message = f"{hashing_payload}:{timestamp}"
    signature = base64(HMAC-SHA256(key=signature_key, msg=message))
"""
from __future__ import annotations

import base64
import hmac
import json
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any

from .exceptions import NombaValidationError

SIGNATURE_HEADER = "nomba-signature"
ALGORITHM_HEADER = "nomba-signature-algorithm"
VERSION_HEADER = "nomba-signature-version"
TIMESTAMP_HEADER = "nomba-timestamp"


def _get_path(payload: dict[str, Any], *path: str, default: str = "") -> str:
    node: Any = payload
    for key in path:
        if not isinstance(node, dict):
            return default
        node = node.get(key)
    return "" if node is None else str(node)


def _parse_rfc3339(timestamp: str) -> datetime:
    # Python's fromisoformat doesn't accept a trailing "Z" before 3.11;
    # normalize it to an explicit UTC offset for broad compatibility.
    ts = timestamp.strip()
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)


def check_timestamp_freshness(timestamp: str, *, max_age_seconds: float) -> None:
    """
    Raise NombaValidationError if `timestamp` (the nomba-timestamp header,
    RFC-3339) is older than `max_age_seconds` compared to now, or is in the
    future by more than the same window (clock skew allowance). This guards
    against replay attacks: a captured, validly-signed webhook being resent
    later. Nomba's signature alone does not protect against replay -- it
    only proves the payload+timestamp pair was signed with your key.
    """
    try:
        sent_at = _parse_rfc3339(timestamp)
    except ValueError as exc:
        raise NombaValidationError(f"Invalid nomba-timestamp format: {timestamp!r}") from exc

    if sent_at.tzinfo is None:
        sent_at = sent_at.replace(tzinfo=timezone.utc)

    age = (datetime.now(timezone.utc) - sent_at).total_seconds()
    if age > max_age_seconds:
        raise NombaValidationError(
            f"Webhook timestamp is {age:.0f}s old, exceeding max_age_seconds={max_age_seconds} "
            "(possible replay attack, or a webhook retried long after the original send)"
        )
    if age < -max_age_seconds:
        raise NombaValidationError(
            f"Webhook timestamp is {-age:.0f}s in the future, exceeding max_age_seconds="
            f"{max_age_seconds} (check for clock skew, or treat with suspicion)"
        )


def compute_signature(signature_key: str, payload: dict[str, Any], timestamp: str) -> str:
    """
    Compute the base64 HMAC-SHA256 signature Nomba expects for a webhook
    payload + timestamp, per their documented scheme.
    """
    hashing_payload = ":".join(
        [
            _get_path(payload, "event_type"),
            _get_path(payload, "requestId"),
            _get_path(payload, "data", "merchant", "userId"),
            _get_path(payload, "data", "merchant", "walletId"),
            _get_path(payload, "data", "transaction", "transactionId"),
            _get_path(payload, "data", "transaction", "type"),
            _get_path(payload, "data", "transaction", "time"),
            _get_path(payload, "data", "transaction", "responseCode"),
        ]
    )
    message = f"{hashing_payload}:{timestamp}"
    mac = hmac.new(signature_key.encode("utf-8"), message.encode("utf-8"), sha256).digest()
    return base64.b64encode(mac).decode("ascii")


def verify_webhook_signature(
    signature_key: str,
    payload: dict[str, Any],
    *,
    signature: str,
    timestamp: str,
) -> bool:
    """
    Verify a webhook's signature using a constant-time comparison.

    Example (Flask):
        from nomba.webhooks import verify_webhook_signature

        @app.post("/webhooks/nomba")
        def handle_webhook():
            payload = request.get_json()
            ok = verify_webhook_signature(
                signature_key="...",
                payload=payload,
                signature=request.headers["nomba-signature"],
                timestamp=request.headers["nomba-timestamp"],
            )
            if not ok:
                return "invalid signature", 401
            ...
    """
    expected = compute_signature(signature_key, payload, timestamp)
    return hmac.compare_digest(expected, signature)


def verify_webhook_request(
    signature_key: str,
    *,
    body: bytes | str,
    headers: dict[str, str],
    max_age_seconds: float | None = 300.0,
) -> dict[str, Any]:
    """
    Convenience wrapper: parses the raw body as JSON, pulls the
    nomba-signature/nomba-timestamp headers (case-insensitively), verifies
    the signature, checks the timestamp isn't stale (replay protection),
    and returns the parsed payload on success.

    `max_age_seconds` (default 300s / 5 min) rejects webhooks whose
    nomba-timestamp is older than this -- protects against a captured,
    validly-signed webhook being replayed later. Pass None to disable this
    check (signature is still verified).

    Raises NombaValidationError if the signature is missing, invalid, the
    timestamp is stale, or the body isn't valid JSON. Does not raise on a
    valid-but-unsigned request -- if you didn't configure a signature key on
    the Nomba dashboard, no signature header will be sent; check for that
    yourself if relevant.
    """
    lower_headers = {k.lower(): v for k, v in headers.items()}
    signature = lower_headers.get(SIGNATURE_HEADER)
    timestamp = lower_headers.get(TIMESTAMP_HEADER)
    if not signature or not timestamp:
        raise NombaValidationError(
            f"Missing '{SIGNATURE_HEADER}' or '{TIMESTAMP_HEADER}' header on webhook request"
        )

    if max_age_seconds is not None:
        check_timestamp_freshness(timestamp, max_age_seconds=max_age_seconds)

    if isinstance(body, bytes):
        body = body.decode("utf-8")
    try:
        payload = json.loads(body)
    except ValueError as exc:
        raise NombaValidationError(f"Webhook body is not valid JSON: {exc}") from exc

    if not verify_webhook_signature(
        signature_key, payload, signature=signature, timestamp=timestamp
    ):
        raise NombaValidationError("Webhook signature verification failed")

    return payload

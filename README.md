# nomba

Unofficial Python SDK for the [Nomba](https://developer.nomba.com) payments API, built with [`uv`](https://docs.astral.sh/uv/) and [`httpx`](https://www.python-httpx.org/).

Covers **every endpoint** in Nomba's official [OpenAPI spec](https://github.com/kudi-inc/vendor-openapi-spec) — 64 methods across 10 resource groups, generated directly from the spec so field names and required/optional parameters match Nomba's docs exactly.

## Install

```bash
uv add nomba
# or
pip install nomba
```

## Usage

```python
from nomba import Nomba

nomba = Nomba(
    client_id="...",
    client_secret="...",
    account_id="...",
    sandbox=True,  # set False for live
)

account = nomba.virtual_accounts.create_virtual_account(
    account_ref="ref-123",
    account_name="Jane Doe",
)

nomba.close()
```

Or as a context manager:

```python
with Nomba(client_id=..., client_secret=..., account_id=...) as nomba:
    nomba.virtual_accounts.fetch_a_virtual_account("ref-123")
```

## Async

Every resource is also available via `AsyncNomba`, built on `httpx.AsyncClient`:

```python
import asyncio
from nomba import AsyncNomba

async def main():
    async with AsyncNomba(
        client_id="...",
        client_secret="...",
        account_id="...",
        sandbox=True,
    ) as nomba:
        account = await nomba.virtual_accounts.create_virtual_account(
            account_ref="ref-123",
            account_name="Jane Doe",
        )
        transfer = await nomba.transfers.perform_bank_account_transfer_the_parent_account(
            amount="5000.00",
            account_number="0123456789",
            account_name="John Doe",
            bank_code="058",
            merchant_tx_ref="txn-001",
            sender_name="Jane Sender",
        )

asyncio.run(main())
```

## Resource groups

Each group is available on both `Nomba` and `AsyncNomba` (async methods are awaited):

| Group               | Examples |
|---------------------|----------|
| `accounts`           | `list_all_accounts`, `create_a_sub_account`, `fetch_account_balance`, `suspend_an_account` |
| `virtual_accounts`   | `create_virtual_account`, `fetch_a_virtual_account`, `update_a_virtual_account`, `expire_a_virtual_account` |
| `checkout`           | `create_an_online_checkout_order`, `charge_customer_with_tokenized_card_data`, `list_all_tokenized_cards_for_merchant` |
| `charge`             | `submit_customer_card_details`, `submit_customer_payment_otp`, `fetch_checkout_order_details` |
| `transfers`          | `perform_bank_account_lookup`, `perform_bank_account_transfer_the_parent_account`, `perform_wallet_transfer_from_a_sub_account` |
| `terminals`          | `assign_a_terminal_to_the_parent_account`, `un_assign_terminal_from_an_account` |
| `transactions`       | `fetch_transactions_on_the_parent_account`, `filter_account_transactions`, `confirm_a_transaction_s_status_by_session_id` |
| `airtime_data`       | `make_airtime_purchases_via_parent_account`, `vend_data_bundles_via_parent_account`, `fetch_data_plans_available_on_a_telco_network_provider` |
| `cabletv`            | `cabletv_lookup`, `cable_tv_subscription_via_parent_account` |
| `electricity`        | `fetch_electricity_providers`, `electricity_customer_lookup`, `vend_electricity_via_parent_account` |

Every method's docstring lists its required and optional body fields straight from Nomba's schema — check `help(nomba.transfers.perform_bank_account_transfer_the_parent_account)` or your editor's signature hints.

## Reliability (token locking + retry/backoff)

`NombaClient`/`AsyncNombaClient` guard token fetching with a lock, so
concurrent requests never race to re-fetch a token — only one fetch happens,
the rest wait and reuse it. Requests that hit a `429` or transient `5xx` are
automatically retried with exponential backoff (respecting `Retry-After` if
Nomba sends one):

```python
nomba = Nomba(
    client_id="...", client_secret="...", account_id="...",
    max_retries=3,       # default
    backoff_factor=0.5,  # default; delay ~= backoff_factor * 2^attempt
)
```

## Typed responses

Every method's return type is a `TypedDict` generated from Nomba's response
schema (in `nomba.models`), giving editor autocomplete and type-checking on
the actual JSON keys (e.g. `resp["data"]["accountNumber"]`). This costs
nothing at runtime — methods still return plain dicts; the TypedDict is
purely a type hint, which matters on constrained hardware.

## Nested body validation

Flat method signatures (e.g. `order_reference=`, `amount=`) are validated by
Python itself. But some fields are nested objects — like `order={...}` in
checkout order creation — whose *inner* required fields a flat signature
can't enforce. Every write call is checked against Nomba's own OpenAPI spec
(bundled with the package) before any network call, so a typo or missing
nested field fails fast locally instead of round-tripping to Nomba's API:

```python
from nomba import NombaValidationError

try:
    nomba.checkout.create_an_online_checkout_order(order={"orderReference": "x"})
except NombaValidationError as e:
    print(e)  # Missing required field(s) in request body: order.amount, order.currency, ...
```

## Webhook signature verification

Implements Nomba's documented HMAC-SHA256 scheme
(`nomba-signature` / `nomba-timestamp` headers, base64-encoded signature),
including replay protection via the timestamp:

```python
from nomba import verify_webhook_request, NombaValidationError

@app.post("/webhooks/nomba")
def handle_webhook():
    try:
        payload = verify_webhook_request(
            signature_key="...",  # the key you set up on the Nomba dashboard
            body=request.get_data(),
            headers=request.headers,
            max_age_seconds=300,  # default; reject webhooks older than 5 min
        )
    except NombaValidationError:
        return "invalid signature", 401

    if payload["event_type"] == "payment_success":
        ...
    return "", 200
```

A valid signature alone doesn't prove a webhook wasn't captured and resent
later — `max_age_seconds` rejects stale ones. Pass `max_age_seconds=None` to
disable that check if you have your own replay protection.

## Bounded concurrency for fan-out calls

`asyncio.gather` has no built-in limit — firing off many calls at once can
trigger a retry storm if several start failing together, or just trip
Nomba's rate limit by bursting too many requests in one window.
`gather_limited` runs the same calls with a concurrency cap:

```python
from nomba import AsyncNomba, gather_limited

async with AsyncNomba(...) as nomba:
    calls = [
        (lambda ref=ref: nomba.virtual_accounts.fetch_a_virtual_account(ref))
        for ref in account_refs
    ]
    results = await gather_limited(calls, limit=5)
```

Extra/undocumented fields can always be passed as kwargs; they get merged into the JSON body verbatim.

## Pagination

Nomba's list endpoints are cursor-paginated server-side (they return a
`cursor` you feed back in for the next page). `paginate`/`apaginate` just
drive that loop for you — no extra pagination scheme is introduced.

```python
from nomba import Nomba, paginate

nomba = Nomba(...)
for account in paginate(nomba.accounts.list_all_accounts, limit=50):
    print(account["accountRef"])
```

Async:

```python
from nomba import AsyncNomba, apaginate

async with AsyncNomba(...) as nomba:
    async for txn in apaginate(nomba.transactions.fetch_transactions_on_the_parent_account, limit=50):
        print(txn)
```

Confirmed paginated endpoints (per Nomba's spec): `accounts.list_all_accounts`,
`accounts.fetch_terminals_assigned_to_an_account`,
`accounts.fetch_terminals_assigned_to_the_parent_account`,
`virtual_accounts.filter_virtual_accounts`, and all six
`transactions.*` list/filter methods.

## Card payment flow

Card checkout is a multi-step sequence (submit card → maybe OTP → maybe 3D
Secure → confirm). `CardPaymentFlow` wraps it so you don't have to track
`transactionId` by hand or look up what Nomba's `responseCode` values mean:

```python
order = nomba.checkout.create_an_online_checkout_order(
    order={"orderReference": "order-001", "amount": "1000", ...}
)

flow = nomba.card_payment(order_reference="order-001")
step = flow.submit_card(card_details="...", key="")

if step.requires_otp:
    step = flow.submit_otp("123456")
elif step.requires_3ds:
    # redirect the user using step.secure_authentication_data
    ...

if step.completed:
    result = flow.confirm()
```

`nomba.card_payment(...)` returns a `CardPaymentFlow` (or `AsyncCardPaymentFlow`
off `AsyncNomba`). `step` is a `CardPaymentStep` with `.completed`,
`.requires_otp`, `.requires_3ds`, `.transaction_id`, `.message`, etc.

## Error handling

```python
from nomba import NombaAPIError, NombaAuthError

try:
    nomba.virtual_accounts.fetch_a_virtual_account("missing-ref")
except NombaAuthError as e:
    print("auth failed:", e)
except NombaAPIError as e:
    print("api error:", e.status_code, e.code, e.response_body)
```

## Authentication

The SDK handles the OAuth2 client-credentials flow automatically: it fetches an
access token on first request, caches it, and refreshes it transparently when
it expires or is rejected (a 401 triggers exactly one retry with a fresh token).
Get your `client_id` / `client_secret` / `accountId` from your Nomba dashboard
under **Webhook & API Keys**.

## Regenerating from the spec

The resource modules in `src/nomba/resources/` and response models in
`src/nomba/models.py` are generated from `src/nomba/data/nomba_openapi.json`
(a snapshot of Nomba's published OpenAPI spec, also bundled into the package
for runtime nested-body validation). To pick up upstream API changes:

```bash
curl -sL -o src/nomba/data/nomba_openapi.json \
  "https://github.com/kudi-inc/vendor-openapi-spec/raw/refs/heads/main/openapi3_0_v_1_0_0.json"
uv run python scripts/generate_resources.py
```

## Development

```bash
uv sync
uv run python -m pytest   # once tests are added
```

## Status

Generated from Nomba's official OpenAPI spec (v1.0.0) — all 64 documented
endpoints across Accounts, Virtual Accounts, Online Checkout, Charge,
Transfers, Terminals, Transactions, Airtime/Data, CableTV, and Electricity.

Also includes: typed responses, cursor pagination helpers, a guided
card-payment flow, locked/retrying HTTP clients, local nested-body
validation against Nomba's own spec, and webhook signature verification.

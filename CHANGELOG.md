# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0] - 2026-10-06

### Added
- Synced with the live Nomba OpenAPI spec (90 → 100 paths, 94 → 104
  non-auth operations): added the 10 new `/v2/bill/...` vend endpoints as
  `*_v2` methods (sync + async) in `airtime_data` (+4), `betting` (+2),
  `cabletv` (+2), `electricity` (+2).
- Nomba marks the v1 bill-vend endpoints as deprecated in favour of the v2
  twins — both are kept; prefer `*_v2` for new integrations.
- Also picked up additive upstream spec drift in `global_payout`:
  optional `idempotencyKey` on `authorize_transfer`/`authorize_exchange`,
  and optional `destinationCountryIsoCode`/`destinationCurrency` filters on
  `fetch_payment_methods`. All optional, backwards-compatible.

### Fixed
- Hardened `scripts/generate_resources.py` against the recurring upstream
  spec bug where a path declares a `{param}` placeholder but omits it from
  the operation's parameters (still present for
  `POST /v1/terminals/payment-request/{terminalId}`): missing path params
  are now injected so regeneration no longer emits an undefined variable.
- Fixed packaging metadata so `uv run`/`uv build` work: `license`
  `AGPL-3.0` → `AGPL-3.0-only` (deprecated SPDX identifier) and relaxed
  `uv_build` upper bound; `__init__.__version__` `0.2.0` → `0.4.0` to match
  `pyproject.toml`.

### Changed
- Moved `pytest`/`twine` from runtime `dependencies` to the `dev`
  dependency group; runtime now only requires `httpx`.
- `test.py` no longer contains hardcoded credentials — reads from
  environment variables.

## [0.3.0] - 2026-08-15

### Added
- Added the 4 missing Global Payout accounts endpoints to match the official Nomba API spec:
  `fetch_global_payout_accounts`, `fetch_global_payout_account`,
  `fetch_global_payout_accounts_sandbox`, `fetch_global_payout_account_sandbox`
  (sync + async, in `nomba.global_payout`). These were present in the spec but had not been
  generated into the resource modules.
- Added `Nomba.revoke_token()` / `AsyncNomba.revoke_token()` to revoke the active access token
  via `POST /v1/auth/token/revoke` (previously only issue/refresh were handled by the client).
- Regenerated all resource modules and response models from the bundled OpenAPI spec.

### Changed
- Resource method count 86 → 94 across 14 groups; README coverage and the `global_payout`
  feature table updated to reflect the new endpoints.
- Several existing method signatures were updated to match the current Nomba spec (these are
  breaking changes for callers):
  - `airtime_data.vend_data_bundles_via_parent_account` /
    `vend_data_bundles_via_specific_or_sub_account`: `amount` is now an optional keyword and a
    required `product_id` positional was added.
  - `global_payout.authorize_transfer` / `authorize_exchange`: the `auth_code` positional
    argument was removed (no longer part of the request body).
  - `global_payout.convert_money`: `source_country_iso_code` was removed.
  - `virtual_accounts.update_a_virtual_account`: the `callback_url` keyword was removed.

### Fixed
- Worked around two bugs in Nomba's published OpenAPI spec so the generated code is correct:
  - `terminals.send_payment_request_to_terminal`: the spec declares `terminalId` in the path but
    omits it from the operation's parameters, which regenerating would have turned into an
    undefined variable in the request URL. `terminal_id` is now a required argument again.
  - `direct_debits.get_mandate_status`: the spec inlines the query parameter as
    `/v1/direct-debits/status?mandateId={mandateId}`; the generator now strips the malformed
    inline query and sends `mandateId` as a proper query parameter.

## [0.2.1] - 2026-06-29

### Added
- Added warning when sandbox mode is enabled to inform users about disabled SSL verification

### Changed
- Updated token refresh timing (refresh 50 seconds before expiry instead of 60)
- Cleaned up literal strings in resource modules (removed unnecessary f-string prefixes)

## [0.2.0] - 2026-06-26

### Added
- New API groups: Betting, Direct Debits, Global Collections, Global Payout
- 26 new endpoints (60 → 86 total)
- Bug fixes: Fixed hardcoded mandateId in direct_debits, renamed account_id to sub_account_id in accounts

### Changed
- Updated OpenAPI spec source to developer.nomba.com
- Regenerated all resource modules from latest Nomba API spec

## [0.1.1] - 2026-06-23

### Changed
- Renamed PyPI package from `nomba` to `nomba-python`
- Import name remains `nomba` for backwards compatibility
- Updated version to match PyPI release

## [0.1.0] - 2026-06-22

### Added
- Initial release
- 64 endpoints across 10 resource groups
- Sync and async clients
- Typed responses, pagination, card payment flow
- Webhook signature verification
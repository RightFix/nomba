# Changelog

All notable changes to this project will be documented in this file.

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
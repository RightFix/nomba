# Changelog

All notable changes to this project will be documented in this file.

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
# Changelog

## 0.1.4 - 2026-08-02

- Corrects the Python README example to use the canonical `nameOfficial`
  provider field.
- Adds a regression assertion for the documented provider name field.

## 0.1.3 - 2026-08-02

- Aligns package metadata with the `v0.1.3` GitHub release.
- Makes GitHub Release creation tag-only and scopes write permission to the
  publishing job.
- Requires the PyPI publishing workflow to receive a matching version tag.

## Unreleased

- Reserved for the next unreleased change.

## 0.1.1 - 2026-08-01

- Aligns the package metadata version with the `v0.1.1` client release line.

## 0.1.0 - 2026-08-01

- Initial Python client for Turkish IBAN validation and provider-code lookup.
- Consumes `turkiye-iban` v0.2.1 release data with no runtime network access.
- Includes synthetic fixture parity tests.

# Publishing

The GitHub release workflow builds and attaches wheel/sdist artifacts but does
not publish to PyPI automatically. Index publication is a deliberate,
environment-protected action.

## Trusted publishing setup

1. Create a `pypi` environment in this repository and require maintainer approval.
2. In PyPI, add a pending Trusted Publisher for owner `trugurpala`, repository
   `turkiye-iban-python`, workflow `publish-pypi.yml`, environment `pypi`, and
   project `turkiye-iban`.
3. For a rehearsal, repeat the registration on TestPyPI with environment
   `testpypi` and project `turkiye-iban`.
4. Run **Publish Python package** from GitHub Actions, select `testpypi` first,
and enter a tag or commit ref such as `v0.1.2`.
5. Verify the index page, downloaded artifacts, package metadata, and a clean
   virtual-environment install before selecting `pypi`.

The workflow uses OIDC and does not store a PyPI token in GitHub secrets. It
must not be run until the matching Trusted Publisher registration exists.

The package validates Turkish IBAN structure and checksum and looks up the
provider code from the pinned dataset. It does not verify account existence,
account ownership, licensing, or transferability. Examples and tests are
synthetic only.

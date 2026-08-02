import json
import hashlib
from pathlib import Path

from turkiye_iban import identify_bank_from_iban, validate_turkish_iban


FIXTURES = Path(__file__).parent / "fixtures"
README = Path(__file__).parents[1] / "README.md"


def canonical_fixture_sha256(content: bytes) -> str:
    """Hash fixture content as canonical LF text across Git checkout platforms."""
    return hashlib.sha256(content.replace(b"\r\n", b"\n")).hexdigest()


def load(name: str) -> list[dict[str, object]]:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_shared_valid_fixture() -> None:
    for item in load("valid.synthetic.json"):
        assert validate_turkish_iban(str(item["iban"]))


def test_shared_invalid_fixture() -> None:
    for item in load("invalid.synthetic.json"):
        assert not validate_turkish_iban(str(item["iban"]))


def test_shared_lookup_fixture() -> None:
    for item in load("lookup.synthetic.json"):
        result = identify_bank_from_iban(str(item["iban"]))
        assert result["provider_code"] == item["providerCode"]
        if item.get("providerStatus") == "known":
            assert result["provider"] is not None
        else:
            assert result["provider"] is None


def test_conformance_manifest_matches_fixture_bytes() -> None:
    manifest = json.loads((FIXTURES / "conformance.manifest.json").read_text(encoding="utf-8"))
    assert manifest["contractVersion"] == "1.0.0"
    assert manifest["dataVersion"] == "2026-07-31"
    assert manifest["sourceRelease"] == "v0.2.1"
    assert {item["kind"] for item in manifest["fixtures"]} == {"valid", "invalid", "lookup"}
    for item in manifest["fixtures"]:
        digest = canonical_fixture_sha256((FIXTURES / str(item["file"])).read_bytes())
        assert digest == item["sha256"]


def test_conformance_digest_is_stable_for_windows_line_endings() -> None:
    manifest = json.loads((FIXTURES / "conformance.manifest.json").read_text(encoding="utf-8"))
    fixture = manifest["fixtures"][0]
    content = (FIXTURES / str(fixture["file"])).read_bytes().replace(b"\r\n", b"\n")

    assert canonical_fixture_sha256(content.replace(b"\n", b"\r\n")) == fixture["sha256"]


def test_readme_uses_verified_pypi_install_and_central_discussions() -> None:
    readme = README.read_text(encoding="utf-8")

    assert "python -m pip install turkiye-iban==0.1.5" in readme
    assert "PyPI kaydı henüz doğrulanmadığı" not in readme
    assert "https://github.com/trugurpala/turkiye-iban/discussions" in readme

import json
import hashlib
from pathlib import Path

from turkiye_iban import identify_bank_from_iban, validate_turkish_iban


FIXTURES = Path(__file__).parent / "fixtures"


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
        digest = hashlib.sha256((FIXTURES / str(item["file"])).read_bytes()).hexdigest()
        assert digest == item["sha256"]

import json
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

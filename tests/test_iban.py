from turkiye_iban import (
    format_iban,
    identify_bank_from_iban,
    mask_iban,
    parse_iban,
    validate_turkish_iban,
)


def test_known_synthetic_iban() -> None:
    iban = "TR280000109999000000000001"
    assert validate_turkish_iban(iban)
    assert format_iban(iban) == "TR28 0000 1099 9900 0000 0000 01"
    assert mask_iban(iban) == "TR28 **** **** **** **** **00 01"
    result = identify_bank_from_iban(iban)
    assert result["provider_status"] == "known"
    assert result["provider"]["nameOfficial"] == "T.C. MERKEZ BANKASI"


def test_unknown_provider_is_not_invalidated() -> None:
    result = identify_bank_from_iban("TR16999990ABC123DEF456GHIJ")
    assert result["parsed"]["is_valid"]
    assert result["provider_code"] == "99999"
    assert result["provider_status"] == "unknown"
    assert result["provider"] is None


def test_invalid_checksum() -> None:
    result = parse_iban("TR290000109999000000000001")
    assert not result["is_valid"]
    assert "INVALID_CHECK_DIGITS" in result["errors"]

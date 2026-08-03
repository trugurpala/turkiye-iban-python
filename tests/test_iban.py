from turkiye_iban import (
    format_iban,
    get_bank_code_from_iban,
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


def test_short_and_malformed_inputs_report_component_errors() -> None:
    assert mask_iban("TR28") == "****"
    assert "INVALID_COUNTRY_CODE" in parse_iban("DE")["errors"]
    assert "INVALID_CHECK_DIGITS" in parse_iban("TRXX0000109999000000000001")["errors"]
    assert "INVALID_PROVIDER_CODE" in parse_iban("TR28000A109999000000000001")["errors"]
    assert "INVALID_ACCOUNT_NUMBER" in parse_iban("TR28000010999900000000000!")["errors"]


def test_provider_code_extraction_rejects_short_and_non_turkish_inputs() -> None:
    from turkiye_iban import find_bank_by_code

    assert get_bank_code_from_iban("TR28") is None
    assert get_bank_code_from_iban("DE280000109999000000000001") is None
    assert get_bank_code_from_iban("TR28ABC0109999000000000001") is None
    assert find_bank_by_code("") is None
    assert find_bank_by_code("123456") is None


def test_oversized_inputs_are_rejected_without_normalization() -> None:
    at_limit = "A" * 1_024
    iban = "TR" + "0" * 1_023

    assert format_iban(at_limit).replace(" ", "") == at_limit

    parsed = parse_iban(iban)
    assert parsed == {
        "input": iban,
        "normalized": "",
        "formatted": "",
        "country_code": "",
        "check_digits": "",
        "bank_code": "",
        "reserve_digit": "",
        "account_number": "",
        "is_valid": False,
        "errors": ["INVALID_LENGTH"],
    }
    assert not validate_turkish_iban(iban)
    assert get_bank_code_from_iban(iban) is None
    assert format_iban(iban) == ""
    assert mask_iban(iban) == ""

    identified = identify_bank_from_iban(iban)
    assert identified["provider_code"] is None
    assert identified["provider"] is None
    assert identified["provider_status"] == "unknown"

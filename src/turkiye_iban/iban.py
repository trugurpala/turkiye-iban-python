from __future__ import annotations

import re
from typing import Any

from .providers import data_version, find_bank_by_code


def _normalize(iban: str) -> str:
    return re.sub(r"\s", "", iban).upper()


def format_iban(iban: str) -> str:
    normalized = _normalize(iban)
    return " ".join(normalized[index:index + 4] for index in range(0, len(normalized), 4))


def mask_iban(iban: str) -> str:
    normalized = _normalize(iban)
    if len(normalized) <= 8:
        return "*" * len(normalized)
    masked = normalized[:4] + "*" * (len(normalized) - 8) + normalized[-4:]
    return format_iban(masked)


def get_bank_code_from_iban(iban: str) -> str | None:
    normalized = _normalize(iban)
    if not normalized.startswith("TR") or len(normalized) < 9:
        return None
    code = normalized[4:9]
    return code if re.fullmatch(r"\d{5}", code) else None


def _has_mod97_checksum(iban: str) -> bool:
    rearranged = iban[4:] + iban[:4]
    remainder = 0
    for char in rearranged:
        value = char if char.isdigit() else str(ord(char) - 55)
        for digit in value:
            remainder = (remainder * 10 + int(digit)) % 97
    return remainder == 1


def parse_iban(iban: str) -> dict[str, Any]:
    normalized = _normalize(iban)
    errors: list[str] = []
    if not normalized:
        errors.append("EMPTY_INPUT")
    if not re.fullmatch(r"[A-Z0-9]*", normalized):
        errors.append("INVALID_CHARACTERS")
    if len(normalized) != 26:
        errors.append("INVALID_LENGTH")
    country = normalized[:2]
    check_digits = normalized[2:4]
    bank_code = normalized[4:9]
    reserve_digit = normalized[9:10]
    account_number = normalized[10:26]
    if country != "TR":
        errors.append("INVALID_COUNTRY_CODE")
    if not re.fullmatch(r"\d{2}", check_digits):
        errors.append("INVALID_CHECK_DIGITS")
    if not re.fullmatch(r"\d{5}", bank_code):
        errors.append("INVALID_PROVIDER_CODE")
    if reserve_digit != "0":
        errors.append("INVALID_RESERVE_DIGIT")
    if not re.fullmatch(r"[A-Z0-9]{16}", account_number):
        errors.append("INVALID_ACCOUNT_NUMBER")
    if len(normalized) == 26 and re.fullmatch(r"[A-Z0-9]+", normalized) and not _has_mod97_checksum(normalized):
        errors.append("INVALID_CHECK_DIGITS")
    return {
        "input": iban,
        "normalized": normalized,
        "formatted": format_iban(normalized),
        "country_code": country,
        "check_digits": check_digits,
        "bank_code": bank_code,
        "reserve_digit": reserve_digit,
        "account_number": account_number,
        "is_valid": not errors,
        "errors": list(dict.fromkeys(errors)),
    }


def validate_turkish_iban(iban: str) -> bool:
    return bool(parse_iban(iban)["is_valid"])


def identify_bank_from_iban(iban: str) -> dict[str, Any]:
    parsed = parse_iban(iban)
    code = get_bank_code_from_iban(iban)
    provider = find_bank_by_code(code) if code is not None else None
    return {
        "parsed": parsed,
        "provider_code": code,
        "provider": provider,
        "provider_status": "known" if provider is not None else "unknown",
        "data_version": data_version(),
        "bank_code": code,
        "bank": provider,
        "is_known_provider": provider is not None,
    }

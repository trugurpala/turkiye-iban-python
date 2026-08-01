from __future__ import annotations

import json
from importlib.resources import files
from typing import Any, cast


def _data() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(files("turkiye_iban").joinpath("data/tr-banks.json").read_text(encoding="utf-8")))


def providers() -> list[dict[str, Any]]:
    return list(_data().get("providers", []))


def find_bank_by_code(code: str) -> dict[str, Any] | None:
    compact = "".join(code.split())
    if not compact.isdigit() or not 1 <= len(compact) <= 5:
        return None
    normalized = compact.zfill(5)
    return next((provider for provider in providers() if provider.get("code") == normalized), None)


def data_version() -> str:
    return str(_data().get("dataVersion", "unknown"))

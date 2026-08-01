from __future__ import annotations

import hashlib
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "v0.2.1"
BASE = f"https://github.com/trugurpala/turkiye-iban/releases/download/{VERSION}/"


def main() -> None:
    target = ROOT / "src" / "turkiye_iban" / "data"
    target.mkdir(parents=True, exist_ok=True)
    for name in ("tr-banks.json", "SHA256SUMS"):
        urllib.request.urlretrieve(BASE + name, target / name)
    expected = next(line.split()[0] for line in (target / "SHA256SUMS").read_text().splitlines() if line.endswith("tr-banks.json"))
    actual = hashlib.sha256((target / "tr-banks.json").read_bytes()).hexdigest()
    if expected != actual:
        raise SystemExit("checksum mismatch")


if __name__ == "__main__":
    main()

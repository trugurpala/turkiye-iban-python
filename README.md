# turkiye-iban

Python 3.10+ package for Turkish IBAN normalization, validation, formatting, masking, and provider-code lookup.

```bash
pip install turkiye-iban
```

```python
from turkiye_iban import identify_bank_from_iban, format_iban, mask_iban

iban = "TR280000109999000000000001"  # synthetic documentation value
result = identify_bank_from_iban(iban)
print(result["provider_status"])
print(format_iban(iban))
print(mask_iban(iban))
```

The package checks Turkish IBAN structure and MOD 97-10 and maps the five-digit provider code to the pinned dataset. It does not verify that an account exists, identify an account holder, prove licensing, or guarantee transferability. `provider_status="unknown"` means the code is absent from the pinned dataset; it is not a claim that the IBAN checksum is invalid.

Data is embedded from the `turkiye-iban` v0.2.1 release and is not fetched at runtime. All examples and tests are synthetic. This package is not TCMB-approved.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m mypy src
python -m build
python -m twine check dist/*
```

## License

MIT. See [LICENSE](LICENSE) and [SECURITY.md](SECURITY.md).

# Python Test Report

Bu rapor, `turkiye-iban-python` istemcisinin public API'sini ve `v0.1.2`
release assetlerini kaydeder. Testlerde yalnız sentetik IBAN kullanıldı.

## Release kanıtı

- Release: [v0.1.2](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.2)
- Wheel: `turkiye_iban-0.1.1-py3-none-any.whl`
- Wheel SHA-256: `0bdcdebf225cde808012252a7f71f6a1ff8a5811400c4393e32d998b474511ef`
- Source archive SHA-256: `6d341b094f219655374509fcfe16ec01c6a57700c9a7349e2f5137c3709ffc3c`
- Paket verisi: `turkiye-iban` v0.2.1 release assetlerinden sabitlenir.

## Public API

| Fonksiyon | Kontrol |
| --- | --- |
| `parse_iban` | IBAN bölümleri, alanlar ve hata kodları |
| `validate_turkish_iban` | Yapı ve MOD 97-10 checksum |
| `get_bank_code_from_iban` | Beş haneli kuruluş kodu |
| `find_bank_by_code` | Bilinen ve bilinmeyen kod |
| `identify_bank_from_iban` | `known` ve geçerli checksum'lı `unknown` sonucu |
| `format_iban` | Dörderli gruplama |
| `mask_iban` | Güvenli gösterim |

## Sonuç

- pytest: **6 test, başarılı**
- mypy strict: **hata yok**
- `python -m build`: wheel ve source archive üretildi
- `twine check`: **başarılı**
- GitHub Actions: Python 3.10, 3.11, 3.12 ve 3.13 matrisi başarılı

Bu kontroller IBAN biçimini, checksum'ı ve kuruluş kodu eşleşmesini test eder;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini kanıtlamaz.

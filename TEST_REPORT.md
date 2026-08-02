# Python Test Report

Bu rapor, `turkiye-iban-python` istemcisinin public API'sini ve `v0.1.5`
release assetlerini kaydeder. Testlerde yalnız sentetik IBAN kullanıldı.

## Release kanıtı

- Release: [v0.1.5](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.5)
- Wheel: `turkiye_iban-0.1.5-py3-none-any.whl`
- Wheel SHA-256: `65fdf307046629dd97d42d542c8d7c5cdff785d2f380a8518124cf66af4e38c9`
- Source archive: `turkiye_iban-0.1.5.tar.gz`
- Source archive SHA-256: `828a4fd60caa8a1de33849e926d3e643d5cfbcdce618e3a1cbb2ae292a733926`
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

- pytest: **9 test, başarılı**
- mypy strict: **hata yok**
- `python -m build`: wheel ve source archive üretildi
- `twine check`: **başarılı**
- PyPI'dan indirilen `v0.1.5` wheel'ini temiz virtualenv'e kurma smoke testi: **başarılı** (`nameOfficial`, `00001`, maskeleme sonucu doğrulandı)
- GitHub Actions: Python 3.10, 3.11, 3.12 ve 3.13 matrisi başarılı

Bu kontroller IBAN biçimini, checksum'ı ve kuruluş kodu eşleşmesini test eder;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini kanıtlamaz.

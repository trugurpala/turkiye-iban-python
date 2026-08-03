# Python Test Report

Bu rapor, `turkiye-iban-python` istemcisinin public API'sini ve `v0.1.7`
release adayı doğrulamasını kaydeder. Testlerde yalnız sentetik IBAN kullanıldı.

## Release kanıtı

- Release: [v0.1.7](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.7)
- Wheel: `turkiye_iban-0.1.7-py3-none-any.whl`
- Source archive: `turkiye_iban-0.1.7.tar.gz`
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

- pytest: **12 test, başarılı**
- mypy strict: **hata yok**
- `python -m build`: wheel ve source archive üretildi
- `twine check`: **başarılı**
- Yerel `v0.1.7` wheel'ini temiz virtualenv'e kurma smoke testi: **başarılı**
  (`nameOfficial`, `00001`, maskeleme sonucu doğrulandı)
- GitHub Actions: Python 3.10, 3.11, 3.12, 3.13 ve 3.14 matrisi başarılı

Bu kontroller IBAN biçimini, checksum'ı ve kuruluş kodu eşleşmesini test eder;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini kanıtlamaz.

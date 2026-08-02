# Python Test Report

Bu rapor, `turkiye-iban-python` istemcisinin public API'sini ve `v0.1.4`
release assetlerini kaydeder. Testlerde yalnız sentetik IBAN kullanıldı.

## Release kanıtı

- Release: [v0.1.4](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.4)
- Wheel: `turkiye_iban-0.1.4-py3-none-any.whl`
- Wheel SHA-256: `3f104bc158729ee7dfa7587d39441140c624ead27f506d6c9b958f23e7a269d0`
- Source archive: `turkiye_iban-0.1.4.tar.gz`
- Source archive SHA-256: `10ab8c127b1c8e3f3c86556ec2d4fac3b584bd61abc97f5ca789ce33a8d26932`
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
- İndirilen `v0.1.4` wheel'i temiz virtualenv'e kurma smoke testi: **başarılı** (`nameOfficial`, `00001`, maskeleme sonucu doğrulandı)
- GitHub Actions: Python 3.10, 3.11, 3.12 ve 3.13 matrisi başarılı

Bu kontroller IBAN biçimini, checksum'ı ve kuruluş kodu eşleşmesini test eder;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini kanıtlamaz.

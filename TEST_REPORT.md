# Python Test Report

Bu rapor, `turkiye-iban-python` istemcisinin public API'sini ve `v0.1.6`
release/registry kanıtını kaydeder. Testlerde yalnız sentetik IBAN kullanıldı.

## Release kanıtı

- Release: [v0.1.6](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.6)
- PyPI wheel: `turkiye_iban-0.1.6-py3-none-any.whl`
- PyPI wheel SHA-256: `b13ccdb4b98baf2a2ad73091013ea50bae476e0a85adf7271cd9c9a7c614cf75`
- PyPI source archive: `turkiye_iban-0.1.6.tar.gz`
- PyPI source archive SHA-256: `86a43ce1c98335dc1c388ed81a53bb747ba62ca8149a94613d12ced7b7940038`
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

- pytest: **11 test, başarılı**
- mypy strict: **hata yok**
- `python -m build`: wheel ve source archive üretildi
- `twine check`: **başarılı**
- PyPI'dan indirilen `v0.1.6` wheel'ini önbelleksiz temiz virtualenv'e kurma
  smoke testi: **başarılı** (`nameOfficial`, `00001`, maskeleme sonucu doğrulandı)
- GitHub Actions: Python 3.10, 3.11, 3.12 ve 3.13 matrisi başarılı

Bu kontroller IBAN biçimini, checksum'ı ve kuruluş kodu eşleşmesini test eder;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini kanıtlamaz.

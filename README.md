# turkiye-iban-python

[![CI](https://github.com/trugurpala/turkiye-iban-python/actions/workflows/ci.yml/badge.svg)](https://github.com/trugurpala/turkiye-iban-python/actions/workflows/ci.yml)
[![GitHub Release](https://img.shields.io/github/v/release/trugurpala/turkiye-iban-python)](https://github.com/trugurpala/turkiye-iban-python/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Divan ile üretildi](https://img.shields.io/badge/Divan%20ile-%C3%BCretildi-087F8C)](https://github.com/trugurpala/divan)

Python 3.10+ istemcisi: Türkiye IBAN normalleştirme, doğrulama, biçimlendirme,
maskeleme ve kuruluş kodu eşleştirmesi.

> [!IMPORTANT]
> Bu paket IBAN biçimini ve MOD 97-10 kontrolünü doğrular; hesabın varlığını,
> hesap sahibini, lisans durumunu veya transfer yapılabilirliğini doğrulamaz.
> `provider_status: "unknown"`, checksum hatası değil, kodun sabitlenmiş veri
> kümesinde bulunmadığı anlamına gelir. Paket TCMB tarafından onaylanmış değildir.

## Ne yapar?

- Türkiye IBAN yapısını ve kontrol rakamlarını doğrular.
- Beş haneli kuruluş kodunu çıkarır ve sabitlenmiş veriyle eşleştirir.
- Bilinen ve bilinmeyen kuruluşları ayrı sonuçlarla bildirir.
- IBAN'ı dörder karakterlik gruplara ayırır veya maskeleyerek gösterir.
- Veriyi runtime sırasında ağdan indirmez; `turkiye-iban` v0.2.1 release verisini kullanır.

## Kurulum

PyPI kaydı henüz doğrulanmadığı için bugün doğrulanmış GitHub release wheel
assetini kullanın:

```bash
python -m pip install https://github.com/trugurpala/turkiye-iban-python/releases/download/v0.1.2/turkiye_iban-0.1.1-py3-none-any.whl
```

PyPI kaydı doğrulandıktan sonra kısa kurulum yolu şu olacaktır:

```bash
python -m pip install turkiye-iban
```

Güncel durum ve Trusted Publisher adımları için [PUBLISHING.md](PUBLISHING.md)
ve ana projenin [Packagist/PyPI yayın belgesine](https://github.com/trugurpala/turkiye-iban/blob/main/docs/PACKAGE_INDEX_PUBLICATION.md) bakın.

## Hızlı kullanım

```python
from turkiye_iban import identify_bank_from_iban, mask_iban

iban = "TR280000109999000000000001"  # yalnızca sentetik örnek
result = identify_bank_from_iban(iban)

if result["parsed"]["is_valid"] and result["provider_status"] == "known":
    print(result["provider"]["name_official"])

print(mask_iban(iban))
```

## Public API

| Fonksiyon | Görevi |
| --- | --- |
| `parse_iban` | IBAN bölümlerini ve hata kodlarını döndürür |
| `validate_turkish_iban` | Yapı ve MOD 97-10 sonucunu döndürür |
| `get_bank_code_from_iban` | Beş haneli kuruluş kodunu çıkarır |
| `find_bank_by_code` | Kodu veri kümesinde arar |
| `identify_bank_from_iban` | Doğrulama ve kuruluş eşleştirmesini birleştirir |
| `format_iban` | IBAN'ı dörderli gruplara ayırır |
| `mask_iban` | IBAN'ın büyük bölümünü gizler |

Detaylı davranış ve sentetik fixture sözleşmesi için ana repository'deki
[API belgesine](https://github.com/trugurpala/turkiye-iban/blob/main/docs/API.md)
ve [Python test raporuna](TEST_REPORT.md) bakın.

## İlgili projeler

- Ana veri ve TypeScript/NPM paket: [trugurpala/turkiye-iban](https://github.com/trugurpala/turkiye-iban)
- Aynı sözleşmenin PHP istemcisi: [turkiye-iban-php](https://github.com/trugurpala/turkiye-iban-php)
- Ortak veri kaynakları: [DATA_SOURCES.md](https://github.com/trugurpala/turkiye-iban/blob/main/DATA_SOURCES.md)
- Güvenlik bildirimi: [SECURITY.md](SECURITY.md)
- Katkı rehberi: [CONTRIBUTING.md](CONTRIBUTING.md)
- Yayınlama: [PUBLISHING.md](PUBLISHING.md)
- Destek: [SUPPORT.md](SUPPORT.md)
- Davranış kuralları: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Geliştirme ve kalite

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m mypy src
python -m build
python -m twine check dist/*
```

Her public API fonksiyonunun kontrol edildiği [TEST_REPORT.md](TEST_REPORT.md)
belgesinde Python CI, build ve paket metadata kanıtları bulunur. Gerçek IBAN,
müşteri adı veya kişisel finansal veri issue, test veya PR içinde kullanmayın.

## Release

Son doğrulanmış release [v0.1.2](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.2)'dir.
Release assetleri ve test sonucu [TEST_REPORT.md](TEST_REPORT.md) içinde kayıtlıdır.
Release geçmişi [CHANGELOG.md](CHANGELOG.md) dosyasındadır.

## Divan ile üretildi

Bu proje [Divan](https://github.com/trugurpala/divan) ile tasarlandı ve üretildi.
Divan runtime bağımlılığı değildir; paket çalışırken Divan'a veya ağ servisine
ihtiyaç duymaz.

## Lisans

MIT. Ayrıntılar için [LICENSE](LICENSE) ve [NOTICE](NOTICE) dosyalarına bakın.

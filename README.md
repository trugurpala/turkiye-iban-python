# turkiye-iban-python

[![CI](https://github.com/trugurpala/turkiye-iban-python/actions/workflows/ci.yml/badge.svg)](https://github.com/trugurpala/turkiye-iban-python/actions/workflows/ci.yml)
[![GitHub Release](https://img.shields.io/github/v/release/trugurpala/turkiye-iban-python)](https://github.com/trugurpala/turkiye-iban-python/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python 3.10+ istemcisi: Türkiye IBAN normalleştirme, doğrulama, biçimlendirme,
maskeleme ve kuruluş kodu eşleştirmesi.

[Ne yapar?](#ne-yapar) · [Kurulum](#kurulum) · [Hızlı kullanım](#hızlı-kullanım) · [Public API](#public-api) · [Test ve kalite](#geliştirme-ve-kalite) · [Topluluk](#ilgili-projeler)

> **Önemli sınır**
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

## Ne yapmaz?

- Hesabın varlığını, sahibini, bakiyesini veya transfer yapılabilirliğini doğrulamaz.
- TCMB, banka veya ödeme kuruluşu adına resmî onay ya da hesap doğrulama sunmaz.
- Gerçek IBAN, müşteri kaydı veya kişisel finansal veri toplamaz.
- `provider_status: "unknown"` sonucunda otomatik kuruluş seçimi yapmaz.

## Türkiye IBAN yapısı

Türkiye IBAN'ı `TR` ülke kodu, iki kontrol rakamı, beş haneli kuruluş kodu,
bir rezerv rakamı ve 16 karakterlik hesap alanından oluşur. `MOD 97-10`,
IBAN'ın yazım bütünlüğünü matematiksel olarak kontrol eder; bir hesabın
bankada gerçekten var olduğunu kanıtlamaz.

## Kurulum

`turkiye-iban==0.1.5`, PyPI üzerinde doğrulanmış olarak yayımlandı. Normal
kurulum için sürümü sabitleyin:

```bash
python -m pip install turkiye-iban==0.1.5
```

PyPI erişiminin uygun olmadığı, kapalı ağ veya artefact doğrulama senaryoları
için aynı sürümün GitHub Release wheel dosyasını kullanabilirsiniz:

```bash
python -m pip install https://github.com/trugurpala/turkiye-iban-python/releases/download/v0.1.5/turkiye_iban-0.1.5-py3-none-any.whl
```

Güncel durum ve Trusted Publisher adımları için [PUBLISHING.md](PUBLISHING.md)
ve ana projenin [Packagist/PyPI yayın belgesine](https://github.com/trugurpala/turkiye-iban/blob/main/docs/PACKAGE_INDEX_PUBLICATION.md) bakın.

## Hızlı kullanım

```python
from turkiye_iban import identify_bank_from_iban, mask_iban

iban = "TR280000109999000000000001"  # yalnızca sentetik örnek
result = identify_bank_from_iban(iban)

if result["parsed"]["is_valid"] and result["provider_status"] == "known":
    print(result["provider"]["nameOfficial"])

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
ve [conformance belgesine](https://github.com/trugurpala/turkiye-iban/tree/main/conformance)
ve [Python test raporuna](TEST_REPORT.md) bakın.

## Sonuçları nasıl yorumlamalısınız?

| Sonuç | Anlamı | Uygulama davranışı |
| --- | --- | --- |
| `parsed["is_valid"] == False` | IBAN yapısı veya kontrol rakamları hatalıdır | IBAN'ı kabul etmeyin |
| `parsed["is_valid"] == True`, `provider_status == "known"` | Kuruluş kodu veri kümesinde bulunur | Kuruluşu otomatik doldurabilirsiniz |
| `parsed["is_valid"] == True`, `provider_status == "unknown"` | IBAN biçimsel olarak geçerli, kod bu veri sürümünde yoktur | Kuruluşu otomatik seçmeyin; kendi iş kuralınızı uygulayın |

## İlgili projeler

- Ana veri ve TypeScript/NPM paket: [trugurpala/turkiye-iban](https://github.com/trugurpala/turkiye-iban)
- Aynı sözleşmenin PHP istemcisi: [turkiye-iban-php](https://github.com/trugurpala/turkiye-iban-php)
- Genel sorular ve diller arası konular: [ana Discussions](https://github.com/trugurpala/turkiye-iban/discussions)
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
python -m pytest --cov=turkiye_iban --cov-report=term-missing
python -m mypy src
python -m build
python -m twine check dist/*
```

Her public API fonksiyonunun kontrol edildiği [TEST_REPORT.md](TEST_REPORT.md)
belgesinde Python CI, build ve paket metadata kanıtları bulunur. Gerçek IBAN,
müşteri adı veya kişisel finansal veri issue, test veya PR içinde kullanmayın.

## Release

Son doğrulanmış release [v0.1.5](https://github.com/trugurpala/turkiye-iban-python/releases/tag/v0.1.5)'dir.
Release assetleri ve test sonucu [TEST_REPORT.md](TEST_REPORT.md) içinde kayıtlıdır.
Release geçmişi [CHANGELOG.md](CHANGELOG.md) dosyasındadır.
GitHub Release workflow'u yalnızca `v*.*.*` tag'lerinde arşiv üretir; PyPI
yayını ise ayrı, ortam korumalı Trusted Publisher workflow'unda yapılır.

## Lisans

MIT. Ayrıntılar için [LICENSE](LICENSE) ve [NOTICE](NOTICE) dosyalarına bakın.

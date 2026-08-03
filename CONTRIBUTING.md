# Katkı Rehberi

Bu depo yalnızca Python istemcisini ve ana Türkiye IBAN veri sözleşmesinin
Python uygulamasını kapsar. Kanonik kuruluş verisi
[ana depoda](https://github.com/trugurpala/turkiye-iban) tutulur.

## Katkı yolları

- Tekrarlanabilir Python hatası için [bug formunu](https://github.com/trugurpala/turkiye-iban-python/issues/new/choose)
  kullanın.
- Yeni API veya belge fikrini feature formunda açıklayın.
- Ortak veri veya diller arası davranış konusunu
  [ana Discussions](https://github.com/trugurpala/turkiye-iban/discussions)
  bölümünde konuşun.

Güvenlik açığı için issue açmayın; [SECURITY.md](SECURITY.md) içindeki özel
bildirim yolunu kullanın.

## Gizlilik ve kapsam

- Gerçek IBAN, hesap sahibi, müşteri kaydı, üretim logu veya ekran görüntüsü
  paylaşmayın.
- Örnek ve fixture'larda yalnız sentetik değerler kullanın.
- Değişikliği ortak API ve veri sözleşmesiyle uyumlu tutun.
- İlgisiz Türkiye veri kümelerini bu istemciye eklemeyin.

## Geliştirme ortamı

Python 3.10+ gereklidir:

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m pytest --cov=turkiye_iban --cov-report=term-missing
python -m mypy src
python -m build --sdist --wheel
python -m twine check dist/*
```

## Pull request kontrolü

- Sabitlenmiş veri sürümü değişiyorsa kaynak release'i ve checksumı belirtin.
- Sürüm etiketi ile `pyproject.toml` sürümünün eşleştiğini doğrulayın.
- Kurulu Python sürümünü ve çalıştırdığınız komutları yazın.
- README, CHANGELOG, TEST_REPORT ve etkilenen public belgeleri gözden geçirin.
- Güvenlik, geriye uyumluluk ve release etkisini açıklayın.

Odaklı bir dal açın, her committe tek bir konuyu ele alın ve pull request'i
`main` dalına yöneltin.

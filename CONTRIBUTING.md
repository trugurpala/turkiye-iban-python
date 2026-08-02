# Katkı Verme

Bu repository yalnızca Python istemcisini ve ana Türkiye IBAN veri sözleşmesinin
Python uygulamasını kapsar. Kanonik kuruluş verisi ana repository'de tutulur.

## Kurallar

- Gerçek IBAN, hesap sahibi, müşteri kaydı veya üretim logu kullanmayın.
- Örnek ve fixture'larda yalnız sentetik değerler kullanın.
- API sonuçlarını TypeScript ana projesindeki ortak sözleşmeyle uyumlu tutun.
- Kapsam dışı Türkiye veri setleri eklemeyin.

## Pull request öncesi

```bash
python -m pytest
python -m pytest --cov=turkiye_iban --cov-report=term-missing
python -m mypy src
python -m build --sdist --wheel
python -m twine check dist/*
```

Sabitlenmiş veri sürümü değişiyorsa checksum ve release kaynağını PR'a ekleyin.
README, CHANGELOG, TEST_REPORT ve etkilenebilecek public belgeleri kontrol edin.
Sürüm etiketi ile `pyproject.toml` metadata sürümünün eşleştiğini doğrulayın.

Güvenlik bildirimi için [SECURITY.md](SECURITY.md) yolunu kullanın.

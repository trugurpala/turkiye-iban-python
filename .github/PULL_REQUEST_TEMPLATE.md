## Özet

Python istemcisi, test, belge veya release değişikliğini açıklayın.

## Gizlilik

- [ ] Gerçek IBAN, hesap sahibi, müşteri verisi veya üretim logu eklenmedi.
- [ ] Tüm örnekler ve fixture'lar sentetiktir.

## Doğrulama

- [ ] `python -m pytest`
- [ ] `python -m mypy src`
- [ ] `python -m build`
- [ ] `python -m twine check dist/*`
- [ ] README ve ilgili public belgeler gözden geçirildi
- [ ] Release veya paket metadata değiştiyse CHANGELOG ve TEST_REPORT gözden geçirildi
- [ ] Güvenlik, geriye uyumluluk ve release etkisi belirlendi
- [ ] Ana `turkiye-iban` veri sözleşmesiyle uyumluluk korundu

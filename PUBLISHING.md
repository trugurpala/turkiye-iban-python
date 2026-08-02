# Yayınlama

## PyPI verification status

Verification on 2026-08-02 confirms `turkiye-iban` version `0.1.5` is indexed at
`https://pypi.org/project/turkiye-iban/`.
GitHub environments `pypi` and `testpypi` now exist and require approval
from `trugurpala`.

The PyPI Trusted Publisher registration is active with these exact values:

- owner: `trugurpala`
- repository: `turkiye-iban-python`
- workflow: `publish-pypi.yml`
- environment: `pypi` (or `testpypi` for a rehearsal)
- project: `turkiye-iban`

The protected `pypi` workflow published `v0.1.5` through OIDC after the build,
pytest, coverage, mypy, package build, and Twine checks passed. A clean
virtualenv install and synthetic IBAN smoke test also passed.

GitHub release iş akışı wheel ve sdist dosyalarını üretip release'e ekler;
PyPI'ye kendiliğinden yayın yapmaz. Paket indeksine yayın, maintainer onayı ve
korumalı bir GitHub ortamı gerektiren ayrı bir adımdır.

## Yayınlama öncesi koşullar

- GitHub'da `pypi` ve gerekirse `testpypi` ortamları oluşturulmalıdır.
- Her ortam için maintainer onayı ve uygun koruma kuralları tanımlanmalıdır.
- PyPI veya TestPyPI üzerinde Trusted Publisher kaydı yapılmalıdır. PyPI için
  `turkiye-iban` Trusted Publisher kaydı artık aktiftir.
- Yayınlanacak commit, `pyproject.toml` içindeki sürümle aynı `vMAJOR.MINOR.PATCH`
  etiketi taşımalıdır. Örneğin `v0.1.5` etiketi `0.1.5` paket sürümüyle eşleşmelidir.

## Trusted Publisher kurulumu

1. Bu repository'de `pypi` ortamını oluşturun ve maintainer onayı isteyin.
2. PyPI'da owner `trugurpala`, repository `turkiye-iban-python`, workflow
   `publish-pypi.yml`, environment `pypi` ve project `turkiye-iban` bilgileriyle
   Trusted Publisher kaydı açın.
3. Önce TestPyPI üzerinde aynı kurulumu `testpypi` ortamı ve
   `turkiye-iban` projesiyle prova edin.
4. GitHub Actions içindeki **Publish Python package** iş akışını çalıştırın;
   hedefi seçin ve mutlaka `v0.1.5` gibi tam bir sürüm etiketi girin.
5. Önce TestPyPI sayfasını, indirilen dosyaları, paket metadata'sını ve temiz bir
   virtualenv kurulumunu doğrulayın. Sonra aynı adımı `pypi` için tekrarlayın.

İş akışı varsayılan olarak `main` dalını kabul etmez. Bu kasıtlı bir güvenlik
kapısıdır: yayın yalnızca sürüm etiketi ile yapılır ve etiketin paket metadata
sürümüyle eşleştiği iş akışında kontrol edilir.

İş akışı OIDC kullanır; PyPI token'ı GitHub secret olarak saklamaz. Eşleşen
Trusted Publisher kaydı ve korumalı ortam hazırlanmadan yayın iş akışını
çalıştırmayın.

## Yayın sonrası kontrol

- PyPI veya TestPyPI sayfasında sürüm ve metadata'yı açın.
- Wheel ve sdist dosyalarının beklenen sürümle yayımlandığını kontrol edin.
- Temiz bir virtualenv içinde `pip install turkiye-iban==SÜRÜM` çalıştırın.
- `identify_bank_from_iban`, `format_iban` ve `mask_iban` ile sentetik smoke testi
  yapın.
- Sonucu `TEST_REPORT.md` ve ana projenin
  [paket indeks yayın belgesine](https://github.com/trugurpala/turkiye-iban/blob/main/docs/PACKAGE_INDEX_PUBLICATION.md)
  kaydedin.

## Kapsam ve güvenlik sınırı

Paket Türkiye IBAN yapısını ve kontrol basamaklarını doğrular; sabitlenmiş veri
kümesinden kuruluş kodu eşleştirir. Hesabın varlığını, hesap sahibini, lisans
durumunu veya transfer yapılabilirliğini doğrulamaz. Örnek ve testlerde yalnızca
sentetik IBAN kullanılır.

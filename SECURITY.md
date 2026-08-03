# Güvenlik Politikası

## Desteklenen sürümler

Yalnızca PyPI ve GitHub'daki en güncel sürüm güvenlik güncellemesi alır.
Kullandığınız sürümü `python -m pip index versions turkiye-iban` komutuyla
veya [son GitHub sürümünden](https://github.com/trugurpala/turkiye-iban-python/releases/latest)
kontrol edin. Eski sürümlere düzeltme geri taşınması garanti edilmez.

## Güvenlik açığını özel olarak bildirin

Güvenlik açığı veya gerçek finansal veri sızıntısı için public issue,
Discussion ya da pull request açmayın.
[Özel GitHub Security Advisory](https://github.com/trugurpala/turkiye-iban-python/security/advisories/new)
oluşturun.

Raporda yalnız sentetik örneklerle şunları belirtin:

- Etkilenen paket ve Python sürümü.
- Beklenen ve gerçekleşen davranış.
- Tekrarlama adımları.
- IBAN doğrulaması, kuruluş eşlemesi veya veri ifşası üzerindeki olası etki.

Proje yöneticisi ilk alındı bildirimini makul olarak 72 saat içinde vermeyi,
durum güncellemelerini özel kanalda paylaşmayı ve düzeltme yayımlanana kadar
ayrıntıları gizli tutmayı hedefler. Bu süre bir hizmet seviyesi taahhüdü
değildir.

## Gizlilik ve kapsam

Issue, PR, test, fixture, log veya ekran görüntüsünde gerçek IBAN, ad-soyad,
hesap bilgisi, müşteri kaydı ya da üretim verisi paylaşmayın. Bir gizlilik
olayı fark ederseniz veriyi yeniden paylaşmadan özel advisory üzerinden
konumunu bildirin.

Bu istemci yalnızca Türkiye IBAN biçimini ve kontrol basamaklarını doğrular;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini doğrulamaz.
`provider_status: "known"` yalnızca sabitlenmiş veri kümesinde kuruluş kodu
eşleşmesi bulunduğunu ifade eder.

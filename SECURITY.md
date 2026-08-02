# Güvenlik

Issue, PR, test, fixture veya log içine gerçek IBAN, ad-soyad, hesap bilgisi,
müşteri kaydı ya da üretim verisi koymayın. Güvenlik açığını public issue olarak
açmak yerine GitHub private vulnerability reporting üzerinden bildirin.

Bu istemci yalnızca Türkiye IBAN biçimini ve kontrol basamaklarını doğrular;
hesabın varlığını, hesap sahibini veya transfer yapılabilirliğini doğrulamaz.
`providerStatus: "known"` yalnızca sabitlenmiş veri kümesinde kuruluş kodu
eşleşmesi bulunduğunu ifade eder.

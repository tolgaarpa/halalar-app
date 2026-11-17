# LESSONS

## 13.11 Kadrajı dosyada değil uygulamada kontrol et (Taş Fener)
Kartlarda ürünler kesik görünüyordu; ben görsel dosyalarına bakıp "tam" dedim. Asıl sebep kart CSS'iydi: grid içindeki img max-height:100% çözülmüyor, uzun ürünler bilgi panelinin altına taşıyordu. Önlem: görsel işi bitince uygulamayı telefon boyunda açıp gerçek kartta kontrol et (uzun ve geniş ürün örnekleri dahil).

## 13.11 Görsel kontrolü = yön + kadraj + uygulamada kart (Taş Fener)
Buda üçlüsü ters duruyordu, 94lü küçük ızgarada gözden kaçtı. Önlem: görsel değişince tüm kareleri en fazla 6x6 sayfada (kare ~230px) yön ve kadraj için tek tek bak, sonra uygulamada her ürünün her açısını kartta açıp taşma ölç (index.html, oneAl+aciDegis döngüsü).

## 15.11 Hit Pazarı tasarımında canlı sürüm esas (Taş Fener)
Tolga yazılı bir tasarım yönü ve sonra bir referans görsel verdi; iki uygulama da reddedildi, 'bizim versiyona geri gel' dedi. Önlem: Hit sayfasında büyük tasarım değişikliğini canlı dosyanın üzerine değil ayrı bir deneme dosyasında (ör. hit-deneme.html) yap; Tolga onaylayınca asıl dosyaya taşı. Böylece geri dönüş tek adım olur.

## 16.11 Yeni sınıf/kimlik adı vermeden önce ara (Taş Fener)
Bölüm katmanına 'sekme' adını verdim; hesap kartının sekmeleri de 'sekme' idi, canlıda hesap sayfası siyaha döndü. Önlem: yeni bir CSS sınıfı ya da id eklemeden önce `grep -n 'ad' dosya` ile aynı adın kullanılıp kullanılmadığına bak; ortak adlar (sekme, kart, liste, menu) yerine işe özel ad ver.

## 17.11 Site ve uygulama tek proje (Sessiz Örs)
Siteyi 3 dükkânlı yaptım, uygulama eski tek dükkânlı tünel/ana sayfa kopyasıyla kaldı; Tolga 'Pazara gir deyince hâlâ Halalar geliyor' diye defalarca söyledi. Önlem: her değişiklikte halalar-web ve halalar-app'te etkilenen yeri grep'le, ikisini birlikte düzelt ve 390px'te ikisini de dene. Uygulamada tünel/ana sayfa kopyası tutma; sitedekine bağlan.

## 17.11 Tünel yerleşimi: tek değişiklik, önce/sonra (Sessiz Örs)
Tolga 'kalabalık, tekrar sayısıysa azalt' dedi; ben aralık, boyut, orta boşluk, çerçeve ve dinamik kenara açılmayı üç turda birlikte değiştirdim, tünel 'çorbaya döndü', ilk Halalar stratejisine geri dönüldü. Önlem: tünel yerleşiminde Tolga'nın söylediği tek parametreyi değiştir, önce/sonra aynı derinlikte ekran görüntüsüyle göster; ilk strateji (aralık 32, tekrar 12, iç ofset 0.35, çerçeve 1.4x1.35) referanstır.

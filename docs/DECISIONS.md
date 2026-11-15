# DECISIONS
- 2026-10-30: İlk sürüm telefon odaklı web uygulaması (tek HTML). NEDEN: Tolga "telefon odaklı başlayalım"; mağaza uygulaması kararı sonra.
- 2026-11-14: Hit Pazarı sayfası tek kaynaktan: tasarım halalar-web/hit.html'de yapılır, uygulamadaki hit.html `python3 araclar/hit_esitle.py` ile üretilir (yollar img/, vitrin/, ürün bağlantısı index.html#u=ID). NEDEN: Tolga telefon arayüzünün webdekiyle aynı olmasını istedi; iki kopyayı elle tutmak ayrışmaya yol açar.

## 2026-11-15 Panel yalnız Tolga'nın (Taş Fener)
Tolga: 'panel sadece bana ait olsun, Halalar yani Koray burada bir mağaza sadece.' Genel yönetici yalnız tolgaarpa@gmail.com; Koray'ın panel yetkisi kaldırıldı. Müşteri ad/telefonu (talepler) yalnız yönetici okur; müşteriye görünen durum ayrı 'durumlar' koleksiyonunda.

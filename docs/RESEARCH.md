# RESEARCH

## 2026-10-30 — Uygulama içi satış ödeme altyapısı
- iyzico pazaryeri ürünü (iyzibazaar) alt satıcıya para dağıtımı sunuyor: https://www.iyzico.com/en/iyzibazaar . Güncel komisyon herkese açık değil; panelde / satış ekibinden teklif. 3. taraf bloglarda %2,49–3,99 + 0,25 TL arası çelişkili rakamlar (doğrulanmadı).
- PayTR de pazaryeri çözümü sunuyor (alt satıcı dağıtımı, komisyon yönetimi); pazaryeri oranı herkese açık değil.
- Apple 3.1.3(e): uygulama dışında tüketilen fiziksel ürünlerde ödeme Apple IAP DIŞINDA alınmalı (kart/Apple Pay). Yani Apple %15-30 kesmez. Kaynak forum alıntısı; resmi metin doğrulanmadı.

## 2026-10-30 — Teklif/sipariş için arka uç (Supabase vs Firebase)
- Supabase ücretsiz: proje başı 500 MB veritabanı, 50.000 aylık kullanıcı; 1 hafta işlem olmazsa proje DURAKLATILIR, elle açılması gerekir. Pro 25$/ay. (3. taraf kaynaklar: jetadmin.io, automationatlas.io; resmi sayfa doğrulanmadı)
- Firebase Spark ücretsiz: Firestore günde 50K okuma / 20K yazma, 1 GiB veri, 50.000 aylık giriş; kart gerekmez, duraklatma yok. SMS ile giriş ücretli/kotası belirsiz. (firebase.google.com/pricing yerel sürümleri, magora-systems.com, supertokens.com)
- Öneri: Firebase (duraklatma riski yok, Google hesabıyla kurulur).

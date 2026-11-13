## 13.11 Taş Fener — deste kaldığı yer hatası
Tolga ürünleri az gördü. Sebep: telefonda kayıtlı 'sira' yeni 94lük sırada da geçerli kalıyordu, öndeki ürünler atlanıyordu. Düzeltme: index.html ürün listesi imzası (D.liste) değişince sira=0, eski order silinir; beğeni/işlemler kalır. Tarayıcıda denendi: eski kayıt (sira 40, 59luk order) → 1/94; aynı listeyle yenileme → 6/94 korunuyor. Yerel commit, yayın bekliyor.

## 13.11 Taş Fener — ad yayında
Porselen Çan adı app + web canlıda doğrulandı.

## 13.11 Taş Fener — ürün adı
Tolga onayıyla 3489 "Çay Fincanı" -> "Porselen Çan" (app + web). Yerel, yayın bekliyor.

## 13.11 Taş Fener — app + web yayında
Tolga "yayınla" dedi; iki depo push edildi, canlı galeri.js ikisinde de yerel ile aynı.

## 13.11 Taş Fener — yön ve tam kontrol
Tolga: Buda üçlüsü ters, "tek tek yazmak saçma, kontrolü düzgün yap". 94 kapak + 136 galeri karesi 6x6 sayfalarda tek tek yön/kadraj için bakıldı. Düzeltilen: 3464 Buda (ters), 3468 fön (vitrinde ters asılı çekilmiş, düz çevrildi), h/fragile/2 kapak (yan). Galeriden çıkarılan: paravan_v2/1 (kesim artığı). Uygulamada 94 ürünün tüm açıları kartta açılıp ölçüldü: taşan/yüklenmeyen 0. Not: 3489 "Çay Fincanı" aslında asılı porselen çan (kedi figürü düz) — ad Tolga onayı bekliyor.

## 13.11 Taş Fener — kart düzeltmesi yayında
Tolga "yayınla" dedi; push edildi, canlı index.html yeni CSS ile doğrulandı.

## 13.11 Taş Fener — kart kesik hatası
Tolga: astronot ve Philips lamba son foto kesik, "neyi kontrol ediyorsun". Sebep görseller değil kart CSS'i: img max-height:100% grid içinde çözülmüyor, uzun görseller bilgi panelinin altında kalıyordu. Düzeltildi, telefon boyunda astronot ve lamba 4. açı tam görüldü. Ders LESSONS'a yazıldı.

## 13.11 Taş Fener — kenar payı yayında
Tolga "yayınla" dedi; push edildi, canlı aspect.js yerel ile aynı.

## 13.11 Taş Fener — kenar payı
Tolga: hoparlör ve Philips lamba kadrajı kötü, hepsini kontrol et. Fable limite takıldı, iş Opus ile yapıldı: kesik görünümün ortak sebebi sıfır kenar payıydı; 226 görsele %3,5 şeffaf pay eklendi, aspect.js güncellendi (3c875a6). Push sınıflandırıcıya takıldı, "yayınla" bekleniyor. Lamba son foto: kaynak tam ama Vision gövdeyi kesiyor.

## 13.11 Taş Fener — kapak düzeltmesi
Tolga: tam görünen foto önce, detay sonra; fön kesik. Fable yaptı (b3cb653): 12 kapak değişti (hendrix, bakirtablo, bongo, filtablo, fisher, havan, jimbeam, piknik, fragile, fincantakim, 3479, ig_portre), 10 galeri sırası, 4 kapak kaynaktan yeniden kesildi (3468 fön, jant, şövalye, kadeh). Kapak sayfası kontrol edildi, Tolga "yayınla" dedi, push edildi.

## 13.11 Taş Fener — yayın
Tolga "kur kral" dedi; 710b9c0 push edildi. Canlıda kategoriler.js, galeri.js ve Ara düğmesi 200 döndü.

## 2026-11-13 Taş Fener (2)
- Ellili/masalı fotolar dahil 35 yeni ürün + 9 eski ürüne yeni açılar eklendi; arama ve 10 kategori kuruldu.
- Eski kadrajlar kaynaktan yeniden kesildi; kaynak fotoğraflar ürünü kestiği için düzelmedi, eskiler korundu.

## 2026-11-13 Taş Fener
- Dekupelik klasörü (44 ürün) Mac Vision ile dekupe edildi; 171/174 tamam, kusur listesi dekupe/KONTROL.txt.
- El/eldiven otomatik ayrılamıyor (Vision tek nesne görüyor).

# JOURNAL

## 2026-10-30 — başlangıç
Mekanik onaylandı (sağ beğen, sol geç, yukarı teklif, aşağı satın al). 59 ürün + webp görseller halalar-web ten alındı. Kart yığını, teklif/satın al alt pencereleri, Beğeniler ve Teklif&Alım listeleri, localStorage kalıcılığı. Önizleme: artifacts/2026-10-30-ilk-onizleme.jpg

## 2026-10-30 — tünel girişi
Uygulama sitedeki tünelle açılıyor (canvas, telefona ölçekli). Parmakla kaydır = ilerle, dokun = ürünü seç → kaydırma destesi o üründen başlar. "Tünel" tuşuyla geri dönüş, "Kaydırmaya başla" ile direkt geçiş. Testler: .tmp/test.py, .tmp/test2.py geçti. Önizleme: artifacts/2026-10-30-tunel-girisi.jpg

## 2026-10-30 akşam — Firebase
Proje halalar-app-tr (tolgaarpa@gmail.com, Spark ücretsiz). Firestore (nam5/ABD) + kurallar: talepler koleksiyonu, müşteri yalnız oluşturur ve kendi belgesini okur; liste/güncelleme yalnız tolgaarpa@gmail.com. Google girişi açık, tolgaarpa.github.io izinli alan. Uygulama teklif/alımda ad+telefon alıp Firestore a yazıyor; panel.html dükkân paneli (Kabul/Ret/Karşı teklif/Satıldı/Sil). Canlı test: gönderme, eksik bilgi uyarısı, 3 güvenlik engeli geçti. Firebase CLI ajan algılayınca uzaktan giriş istiyor; giriş Tolga Terminal den yaptı.

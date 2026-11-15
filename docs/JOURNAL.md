## 15.11 Taş Fener — vintage deneme 2. tur (Fable'da)
Tolga: 'örnekteki görkemi hissetmedim', 'fon rengi beyaz olsun'. Görkem referanstaki büyük fotoğrafik objelerden geliyor; referanstan yazısız, saydam zeminli kolaj çıkarıldı (halalar-web/kaynak/referans/kolaj-seffaf.webp; gömülü Halalar kartı canlı kartla örtülecek). Fable'a beyaz zemin + referans oranları + Ş okunurluğu + gömülü kartın örtülmesi verildi.

## 15.11 Taş Fener — vintage deneme hazır
Fable hit-deneme.html'i bitirdi (e465dcd): sarı/kırmızı/mavi kolaj girişi, gerçek ürünlerle kolaj (kurt büstü, daktilo, vazo, papağan, polaroid, heykel), Halalar kartı, 4 mavi karo, diğer bölümler aynı içerikle temada, 'Dükkânını sokağa aç - başvuru yakında'. Ben masaüstü girişe baktım: referansa yakın, taşma ve kırık görsel yok. Tolga'ya gösterildi.

## 15.11 Taş Fener — vintage tema Fable'a verildi
Tolga yeni referans (sarı zemin, kırmızı/mavi, kolaj, 'Her şeyin bir hikâyesi var') verdi ve 'Fable'a yaptır' dedi. Referans görsel web projesine taşındı. Fable yardımcısı hit-deneme.html'de çalışıyor; kolaj Halalar'ın gerçek ürün görselleriyle kurulacak. Canlı hit.html'e dokunulmuyor (15.11 dersi).

## 15.11 Taş Fener — canlı tasarıma geri dönüş
Tolga 'hiçbiri değil, bizim versiyona geri gel'. web hit.html 4ee07b6 sürümüne (canlı tasarım + durumlar okuması) döndü, app hit.html eşitlendi ve önceki hâliyle birebir aynı; hit_esitle.py eski hâline döndü. Ders yazıldı (denemeler ayrı dosyada).

## 15.11 Taş Fener — dijital dükkânlar sokağı tasarımı (yerel)
Tolga referans görsel verdi ('eski siteyi buna ayarla, ek sayfalarımızda bu tasarım dili olsun'). Canlıdaki hit.html temel alındı, referans diline çevrildi: Yön seç meydanı + perspektif cam panolar + Vitrin/Üye girişi/Bilmen gerekenler/KVKK/Nasıl çalışır tünelleri. Düzeltilenler: panolar düz görünüyordu (perspektif 520px), 02/03 yazıları taşıyordu, duvar 01'e biniyordu, Google düğmesindeki ok yuvarlak düğme sınıfıyla çakışıyordu, telefonda bilgi panoları 47px'e çöküyordu (flex:none), telefonda başlık duvarın üstüne biniyordu (duvar üste, başlık altına). app eşitlendi (sokak/ eklendi). Yerel, yayın bekliyor.

## 15.11 Taş Fener — yeni mod reddedildi
Tolga: 'bu çok kötü, bekle, neye benzediğini ben vereceğim.' Referans bekleniyor; yerel tasarım yayınlanmayacak.

## 15.11 Taş Fener — Hit Pazarı yeni tasarım modu (yerel)
Tolga kendi yazdığı tasarım anlayışını yapıştırdı ('dijital mekân; tipografi tasarımın kendisi; giriş mekânın parçası; bilgi dev 01/02/03; kart yığını, ikon, standart buton, dekoratif neon yok'). halalar-web/hit.html yeniden kuruldu: kapı (neon Hit) korundu, içerisi siyah + beyaz + tek turuncu nokta. Vitrin dev ad + sayaç, Gişe (dev sıra numarası + füme cam + 'Sıranı al'), sürüklenen kart sahnesi, dev numaralı açılır bilgiler. Telefonda iki çakışma bulundu ve düzeldi (cam numarayı fazla örtüyordu; Geç/Beğen kartın altına kaydı). app hit.html eşitlendi. Yerel, yayın bekliyor.

## 15.11 Taş Fener — güvenlik 1. adım (yerel)
Tolga 'panel sadece bana ait olsun, Koray bir mağaza; sistemi sağlama almaya başla'. firestore.rules: yönetici yalnız Tolga, alan sınırları + telefon deseni + satıcı sabit; talepler okuma yalnız yönetici, müşteri durumu 'durumlar' koleksiyonundan (panel toplu yazım). app index.html yanıt kaçışlı; web hit.html durumlar'dan okuyor, app hit.html eşitlendi. Kural testi yazıldı (14 durum, scratchpad/kural/t.py) ama öykünücü Java 21 istiyor; çalışmadı. Yerel, yayın bekliyor.

## 15.11 Taş Fener — güvenlik eksikleri taraması
Tolga 'güvenliğimizle ilgili eksiklerimizi tespit et'. Yalnız okuma: firestore.rules, panel.html, urun.html, index.html incelendi; canlı Firestore'a girişsiz liste denemesi 403 (kural yayında); iki deponun git geçmişinde yalnız herkese açık Firebase web anahtarı var (gizli değil). Bulgular Tolga'ya önem sırasıyla verildi; hiçbir dosya değişmedi.

## 15.11 Taş Fener — web teklif + menü düzeltmesi yayında
Tolga "yayınla" (web ve telefon): iki depo push edildi; web urun.html (Teklif ver/Satın al), web ve app hit.html (nav.dolu menü zemini) canlıda doğrulandı.

## 15.11 Taş Fener — gerçek teklif panelde
Tolga canlıdan gerçek bir teklif gönderdi, panel.html'de (Google girişi) göründüğünü doğruladı: talep akışı uçtan uca çalışıyor. Web ürün sayfası teklif/satın alma + menü çubuğu düzeltmesi hâlâ yerel, yayın bekliyor.

## 15.11 Taş Fener — web ürün sayfasında teklif/satın alma
Tolga '1 için başla' (eksik listesi 1: web 'Sor / Rezerve et' bir yere gitmiyordu). halalar-web/urun.html: fiyat (ÖRNEK) + Teklif ver / Satın al düğmeleri, satır içi form (tutar + %70/80/90 hızlı seçim; özet; ad, telefon, KVKK açık rıza), uygulamadaki gonder() ile aynı alanlar Firestore 'talepler'e (urun, urunAd, tur, tutar, ad, tel, durum Beklemede, zaman serverTimestamp, satici halalar) -> dükkân paneline düşer; ortak localStorage 'halalar-app-v1' islem'e yazılır -> Hit Pazarı Tekliflerim'de görünür. Test: veritabanı yazımı taklit edildi (canlı panele sahte talep düşmesin): doğrulama sırası doğru, alanlar kurallardaki izinli liste ile aynı, tutar sayı, kayıt ve onay kutusu doğru; 375'te yana taşma bulundu ve düzeldi (main>div min-width:0). Gerçek gönderim canlıda Tolga ile bir kez denenecek. Yerel, yayın bekliyor.

## 15.11 Taş Fener — menü çubuğu binme düzeltmesi
Tolga: Hit Pazarı yazısının üstüne binen yazılar var. Sebep: sabit menü çubuğu şeffaf gradyandı, kayan bölümler (ör. Bilmen gerekenler başlığı) sol üstteki Hit Pazarı/Halalar ve sağdaki bağlantıların altından geçiyordu. Düzeltme: girişin %55'inden sonra nav.dolu (koyu + buzlu zemin, alt çizgi), section scroll-margin-top 96px, alt dev yazı line-height 1.08 (p kuyruğu bağlantılara değiyordu). Gözle 1440: Bilmen gerekenler ve sayfa sonu temiz. App hit.html eşitlendi. Yerel, yayın bekliyor.

## 14.11 Taş Fener — açıklamalar + neon kapı yayında
Tolga "yayınla": iki depo push edildi; app ve web urunler.js (yeni açıklamalar), app kart düzeni (ust1) ve web hit.html (neon Hit tünel kapısı, yeni metin) canlıda doğrulandı.

## 14.11 Taş Fener — 94 ürüne açıklama
Tolga: ürünlere açıklayıcı, uygun açıklamalar (kapsam: 94'ün hepsi). Kapak sayfalarına (.tmp/kapak_yon_0-2) bakılarak her ürüne 2 cümle yazıldı: ne olduğu + görünen detay, sonra kullanım/hava; durum/orijinallik/çalışırlık uydurulmadı, eldeki marka/yıl korundu. Eski hâl .tmp/urunler-aciklama-oncesi.js. Web veri/urunler.js aynı. Uygulama kartı açıklamayı tek satırda kesiyordu: bilgi alanı yeniden düzenlendi (üst satır kategori + fiyat, sonra tam genişlik ad, sonra 4 satıra kadar açıklama; alan en çok +21px uzar, resmin 26px boşluğu içinde). 94 kart ölçüldü: kısalan kategori 0, kesilen açıklama 0, taşma 0. Yerel, yayın bekliyor.

## 14.11 Taş Fener — neon Hit tünel kapısı
Tolga: girişteki 'Tünele giriş' kalksın, metin 'Hit Tünelinde gez; beğen, teklif ver, pazarlık et.', neon Hit'e tıklayınca tünele gitsin. Yapıldı (web + eşitlemeyle app). Tabela bağlantı oldu (üzerine gelince hafif büyür/parlar). Denendi: web 1280'de tıklama -> index.html; app 375'te dokunma -> index.html, tünel açık. Yerel, yayın bekliyor.

## 14.11 Taş Fener — ikon yayında
Tolga "yayınla": iki depo push edildi; 7 canlı sayfanın hepsinde Hit Pazarı ikonu doğrulandı.

## 14.11 Taş Fener — Hit Pazarı ikonu her sayfada
Tolga: alttaki mavi 'hit pazarı' ana sayfadaki kırmızıyla; her sayfada sol üstte Hit Pazarı ikonu. Yapılan: alt yazı #ff5a1f (nav'daki Hit Pazarı rengi) + hafif parıltı. İkon = Hit tabelasının minik hâli (neon çerçeve + kıvrımlar + 'Hit'), koyu plaka üstünde (beyaz urun.html'de krem yazı kayboluyordu, plaka eklendi), tıklayınca hit.html. araclar/hit_ikon.py ile 6 sayfaya eklendi: web index/hit/urun, app index (tünel + kart ekranı + Beğeniler + Teklif), kvkk, panel; app hit.html eşitlemeyle geldi. Aynı işaret sekme simgesi (favicon) oldu. Ölçüm: 7 sayfada ikon sol üstte, üstünde başka katman yok; gözle: app tüneli, web ürün sayfası. Yerel, yayın bekliyor.

## 14.11 Taş Fener — vitrin + çerçeveli notlar + telefon sürümü yayında
Tolga "yayınla": iki depo push edildi; web hit.html (nlevha), app hit.html (#u bağlantıları), app vitrin fotoğrafı ve app index #u desteği canlıda doğrulandı.

## 14.11 Taş Fener — vitrin başlığı, çerçeveli notlar, telefon sürümü eşit
Tolga: 'Açık vitrinler' yerine yalnız 'Halalar' (yandaki başlık oraya), 9 ürün büyüsün; Bilmen gerekenler crazy.studio örneğine yakın; app hit.html de aynı olsun. Yapılan: üst başlık kaydırılan dükkânın adı (Halalar / Sıradaki vitrin), 9 ürün foto boyuna kilitli (contain:size; 1440'ta foto 695 = ızgara), ürünler karede %86. Notlar: başlıktan inen neon hat, düğüm, 4 dala çerçeveli (çift çizgi) levha, isim plakası üstte, fare ışığı (kobalt), bölüm görününce bir kez çizim; notlar varsayılan görünür. Telefon: araclar/hit_esitle.py web sayfasından app hit.html'i üretir + vitrin fotoğrafını kopyalar; app index.html'e #u=ID desteği (ürün kartı en üste, tünel kapanır). Bulunan ve düzelen: 9'lu ızgara fotodan uzundu (1156px), not sınıfı kepenk levhasıyla çakışıyordu (.nlevha). Doğrulama: 34 görsel yolu app'te 200, #u=3490 -> Rüzgâr Çanı üstte ve tünel kapalı, yana taşma yok; gözle 1440 vitrin + not hatları (yakın), 375 notlar. Yerel, yayın bekliyor.

## 14.11 Taş Fener — Hit çerçevesi + düz yazı yayında
Tolga "yayınla": halalar-web push edildi, notlar bölümü canlıda doğrulandı. Not: Tolga'nın duyduğu müzik, incelemek için tarayıcı panelinde açtığım crazy.studio sayfasından geliyordu; panel yerel sayfaya döndürüldü. Öneri bekliyor: crazy.studio'dan fener ışığı, neon kablo, plakalı duvar (Tolga seçecek).

## 14.11 Taş Fener — Hit çerçevesi + düz yazı uyarılar
Tolga: Hit yazısı kutusunun içinde olsun; Bilmen gerekenler kart olmasın, düz yazı. Tabela iç payı artırıldı (.2em .5em .26em, yazı 150-280px): 1440'ta 568x345 çerçeve, 375'te 311x189 ekrana sığıyor, yazı dört yandan paylı. Asma tabelalar kaldırıldı; 4 madde başlık + paragraf, masaüstünde 2 sütun, telefonda tek sütun. Gözle: 1440 kapı ve Bilmen gerekenler. Yerel, yayın bekliyor.

## 14.11 Taş Fener — gece çarşısı yayında
Tolga "yayınla": halalar-web push edildi; hit.html (Hit'len metni), vitrin fotoğrafı ve tünel nav boyutu canlıda doğrulandı. Hareketlerin (kaydırma, sallanma, neon yanma) akıcılığı Tolga'nın ekranında kontrol edilecek.

## 14.11 Taş Fener — Hit Pazarı üçüncü tur: gece çarşısı
Tolga: yeni metin, Hit büyük/Halalar küçük, başlık yalnız 'Hit', açık vitrinlere Halalar vitrini + 9 ürün, sıradaki vitrin okla kaysın, bilgi kartları sallansın ve sönük olsun; dışarıdan araştır. Araştırma: Ilm-Alan/frontend-design (tek yön seç + tek akılda kalan hamle), superdesign (var olan sistem + gerçek referans), ConardLi web-design-engineer (5 boyutlu eleştiri); yerel frontend-design kalıp listesi (büyük harf etiketler, ortası noktalı yazılar, sıra olmayan numaralar, yazı sonu oklar kaldırıldı). Vizyon: gece çarşısı, gerçek Halalar gece vitrini fotoğrafından (hit-pazari/vitrin/halalar.webp -> halalar-web/kaynak/vitrin). Neon çerçeveli 'Hit' tabelası bir kez titreyip yanıyor; vitrinler yatay kayıyor (Halalar foto + 3x3 ürün, ikinci sırada kepenk); uyarılar koyu asma tabela, iplerinden sallanıyor. Hata bulundu ve düzeldi: tünel ürünleri z-index yüzünden yazının üstüne çıkıyordu (önceki yayında da vardı) -> .sahne z-index:0. Ölçüm/göz: 1440 kapı, vitrin, tabelalar; 375 kapı; yana taşma yok, foto ile ürün sütunu eşit 708px, ok kaydırması çalışıyor. Web tünel nav'ında Hit Pazarı 28px, Halalar 17px. App tüneli değişmedi. Yerel, yayın bekliyor.

## 14.11 Taş Fener — web Hit Pazarı yayında
Tolga "yayınla": halalar-web push edildi; hit.html (ikinci tur), tünel bağlantısı ve veri/firebase-ayar.js canlıda doğrulandı. Google girişi web'de de Tolga'nın denemesini bekliyor.

## 14.11 Taş Fener — web Hit Pazarı ikinci tur (sanat yönetmeni)
Eleştiri: kapı jenerik (eşit boy, çember gibi serpilmiş, derinlik yok), askı ipi kesimde kayboluyordu, bölüm numaraları kayıptı. Düzeltme: kapı gerçek tünel ağzı — başlık kaçış noktasında, 24 ürün halkalarda derine uzanıyor, yakındakiler büyük ve kadrajdan taşıyor, uzaktakiler siste; kamera yavaş içeri süzülüyor, kaydırınca dalıyor; yazının önünden geçen ürün soluyor. Askı ipi sarmalayıcıya alındı, numaralar büyüdü. Ölçüm: 1440'ta kare başına yazıya binen 0-2 (çoğu opak düğmenin arkası), 375'te 0-1, yatay taşma yok. Gözle: kapı (1440) ve etiketler bakıldı; telefon kapısı yalnız ölçüldü. Yerel, yayın bekliyor.

## 14.11 Taş Fener — web Hit Pazarı sayfası
Tolga: web arayüzü, yaratıcı ama mevcut site diline uygun. halalar-web/hit.html: koyu zemin, Fraunces + Space Grotesk, kobalt vurgu; derinlikte süzülen ürün kapısı (fare/kaydırmayla, tünel yankısı), ürün adları bandı, vitrin camı Halalar kartı, krem giriş bileti (Google girişi + Hesabım), dört yön kartı, krem askı etiketleri (uyarılar), sonda dev kobalt 'hit pazarı'. Web tüneli bağlantısı artık web hit.html'e. Ölçüm: kapı ürünleri yazıların üstüne binmiyor (1024, 1440, 375 genişlik), yatay kaydırma yok, panel sahte kullanıcıyla 2 beğeni gösterdi. Gözle bakılan: kapı, vitrin, bilet; nasıl çalışır/etiketler/alt kısım yalnız ölçüldü (ekran görüntüsü sınırı). Yerel, yayın bekliyor.

## 14.11 Taş Fener — Hit Pazarı yayında
Tolga "yayınla": app (hit.html, tünel bağlantısı, kvkk) + web (nav bağlantısı, tünele giriş) push edildi; dördü canlıda doğrulandı. Gerçek Google girişi Tolga'nın denemesini bekliyor.

## 14.11 Taş Fener — Hit Pazarı giriş sayfası + üye paneli
Tolga: hesap girişi + kullanıcı paneli, tünelde Halalar üstüne Hit Pazarı, 'deliğe' yerine tünel. Yapılan: hit.html (tanıtım, Tünele giriş, Google ile üye girişi, Hesabım: Beğenilerim/Tekliflerim/Bilgilerim, Nasıl çalışır, 4 uyarı, KVKK + Dükkân girişi bağlantısı). App tünelinde Halalar üstünde turuncu 'Hit Pazarı ↗' (tünel pointerdown'u a etiketini de bıraktı, yoksa dokunma yutuluyordu). Web: nav'da aynı bağlantı (app hit.html'e), urun.html '← deliğe dön' → '← tünele giriş'. kvkk.html'e üye girişi verisi eklendi. Tarayıcıda: bağlantı açılıyor, sahte kullanıcıyla panel 3 beğeni/2 teklif, Bilgilerim kaydı uygulamanın kaydına yazıyor; test verisi geri alındı. Sınır: beğeni/teklif hâlâ cihazda, hesaba bulut eşitleme yok (firestore.rules değişikliği + deploy ister). Google girişi yalnız yetkili alan adlarında çalışır (github.io panelde çalışıyor). Uyarı metinleri taslak, Tolga kendi metnini verebilir. Yerel, yayın bekliyor.

## 13.11 Taş Fener — kategori
Tolga: Rüzgâr Çanı (3490) Heykel → Müzik, Fisher Müzik Seti (h/fisher) Elektronik → Müzik. App + web veri/kategoriler.js aynı; tarayıcıda Müzik 14 ürün. Yerel, yayın bekliyor.

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

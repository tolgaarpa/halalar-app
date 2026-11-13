# LESSONS

## 13.11 Kadrajı dosyada değil uygulamada kontrol et (Taş Fener)
Kartlarda ürünler kesik görünüyordu; ben görsel dosyalarına bakıp "tam" dedim. Asıl sebep kart CSS'iydi: grid içindeki img max-height:100% çözülmüyor, uzun ürünler bilgi panelinin altına taşıyordu. Önlem: görsel işi bitince uygulamayı telefon boyunda açıp gerçek kartta kontrol et (uzun ve geniş ürün örnekleri dahil).

## 13.11 Görsel kontrolü = yön + kadraj + uygulamada kart (Taş Fener)
Buda üçlüsü ters duruyordu, 94lü küçük ızgarada gözden kaçtı. Önlem: görsel değişince tüm kareleri en fazla 6x6 sayfada (kare ~230px) yön ve kadraj için tek tek bak, sonra uygulamada her ürünün her açısını kartta açıp taşma ölç (index.html, oneAl+aciDegis döngüsü).

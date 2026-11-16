/* İkinci dükkân: yurt içi tedarikçilerden (Hepsibayi, BEZOS) stoksuz satış.
   urunler listesi araclar/xml_cevir.py ile tedarikçi XML'inden üretilir; elle düzenleme.
   Ad şimdilik yer tutucu: Tolga dükkânın adını verince yalnız 'ad' değişir. */
const DUKKAN2={
  id:'dukkan2',
  ad:'Yeni Dükkân',
  slogan:'Giyim, hediyelik ve ev dekorasyonu; stoktan, kapına.',
  kategoriler:['Giyim','Hediyelik','Ev dekorasyon'],
  teslim:'Kargo ile 1-3 iş günü',
  urunler:[] // {id, ad, aciklama, kategori, fiyat, gorsel, tedarikci, stok}
};

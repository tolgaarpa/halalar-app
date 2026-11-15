#!/usr/bin/env python3
"""Tedarikçi XML'ini (Hepsibayi, BEZOS) ikinci dükkânın ürün listesine çevirir.
Kullanım:
  python3 araclar/xml_cevir.py <xml dosyası ya da bağlantı> --tedarikci BEZOS --kar 35 [--kategori-esle esle.json] [--en-cok 500]
Çıktı: ~/Desktop/halalar-web/veri/dukkan2.js içindeki 'urunler' listesi (ad, slogan vb. korunur).
Tedarikçilerin XML alan adları farklıdır; yaygın adlar otomatik tanınır (ad/name/title, fiyat/price, resim/image, stok/stock, kategori/category, kod/sku/barcode).
Kar: tedarikçi fiyatına eklenecek yüzde; sonuç 9 ile biten fiyata yuvarlanır."""
import argparse, json, os, re, sys, urllib.request, xml.etree.ElementTree as ET
WEB=os.path.expanduser('~/Desktop/halalar-web'); HEDEF=os.path.join(WEB,'veri','dukkan2.js')
ALAN={'id':['stokkodu','stok_kodu','kod','sku','productcode','product_code','urunkodu','barcode','barkod','id'],
      'ad':['urunadi','urun_adi','ad','name','title','baslik','productname','product_name'],
      'aciklama':['aciklama','description','detay','details'],
      'fiyat':['satisfiyati','satis_fiyati','bayifiyati','bayi_fiyati','fiyat','price','price1','listprice'],
      'gorsel':['resim1','resim','image1','image','picture1','picture','gorsel','img','imageurl','image_url'],
      'stok':['stok','stock','miktar','quantity','qty','stokadedi'],
      'kategori':['kategori','category','categoryname','category_name','anakategori','kategori1']}
def norm(t): return re.sub(r'[^a-z0-9_]','',t.lower().replace('ı','i').replace('ş','s').replace('ğ','g').replace('ü','u').replace('ö','o').replace('ç','c'))
def deger(el,alan):
    cocuk={norm(c.tag.split('}')[-1]):(c.text or '').strip() for c in el}
    cocuk.update({norm(k):v for k,v in el.attrib.items()})
    for a in ALAN[alan]:
        if cocuk.get(a): return cocuk[a]
    return ''
def sayi(t):
    t=re.sub(r'[^0-9,.]','',t or '')
    if t.count(',') and t.count('.'): t=t.replace('.','').replace(',','.') if t.rfind(',')>t.rfind('.') else t.replace(',','')
    else: t=t.replace(',','.')
    try: return float(t)
    except: return 0.0
def main():
    p=argparse.ArgumentParser(); p.add_argument('kaynak'); p.add_argument('--tedarikci',required=True); p.add_argument('--kar',type=float,default=35)
    p.add_argument('--kategori-esle'); p.add_argument('--en-cok',type=int,default=500); a=p.parse_args()
    veri=urllib.request.urlopen(a.kaynak,timeout=60).read() if a.kaynak.startswith('http') else open(a.kaynak,'rb').read()
    kok=ET.fromstring(veri)
    # ürün düğümü: içinde ad ve fiyat alanı olan en sık etiket
    adaylar=[el for el in kok.iter() if len(el) and deger(el,'ad') and deger(el,'fiyat')]
    if not adaylar: sys.exit('XML içinde ürün bulunamadı (ad/fiyat alanları tanınmadı). Alan adlarını ALAN listesine ekle.')
    esle=json.load(open(a.kategori_esle)) if a.kategori_esle else {}
    urunler=[];gor=set()
    for el in adaylar:
        uid=deger(el,'id') or deger(el,'ad'); uid=re.sub(r'[^A-Za-z0-9_-]','',uid)[:60]
        if not uid or uid in gor: continue
        fiyat=sayi(deger(el,'fiyat')); stok=int(sayi(deger(el,'stok'))) if deger(el,'stok') else None
        if fiyat<=0 or stok==0: continue
        kat=deger(el,'kategori'); kat=esle.get(kat,kat)
        if esle and kat not in esle.values(): continue   # eşleme verildiyse yalnız seçili kategoriler
        satis=int(round(fiyat*(1+a.kar/100)/10)*10-1)
        urunler.append({'id':a.tedarikci[:3].lower()+'-'+uid,'ad':deger(el,'ad')[:120],'aciklama':re.sub(r'<[^>]+>',' ',deger(el,'aciklama'))[:600].strip(),
                        'kategori':kat,'fiyat':satis,'gorsel':deger(el,'gorsel'),'tedarikci':a.tedarikci,'stok':stok})
        gor.add(uid)
        if len(urunler)>=a.en_cok: break
    s=open(HEDEF,encoding='utf-8').read()
    eski=[u for u in json.loads(re.search(r'urunler:(\[.*?\])\s*(//[^\n]*)?\n',s,re.S).group(1) or '[]') if u.get('tedarikci')!=a.tedarikci] if 'urunler:[' in s and 'urunler:[]' not in s else []
    hepsi=eski+urunler
    s=re.sub(r'urunler:\[.*?\]\s*(//[^\n]*)?\n','urunler:'+json.dumps(hepsi,ensure_ascii=False)+' // araclar/xml_cevir.py\n',s,count=1,flags=re.S)
    open(HEDEF,'w',encoding='utf-8').write(s)
    print(f'{a.tedarikci}: {len(urunler)} ürün eklendi; dükkânda toplam {len(hepsi)} ürün.')
if __name__=='__main__': main()

#!/usr/bin/env python3
"""Hit Pazarı sayfasını webden telefon uygulamasına eşitler.
Kaynak: ~/Desktop/halalar-web/hit.html (tasarım burada yapılır).
Hedef:  halalar-app/hit.html (elle düzenleme; her eşitlemede üzerine yazılır).
Kullanım: python3 araclar/hit_esitle.py"""
import os, shutil, sys
WEB = os.path.expanduser('~/Desktop/halalar-web')
APP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(WEB, 'hit.html'), encoding='utf-8').read()
DEGIS = [
    ('href="urun.html?id=${encodeURIComponent(\'d2:\'+u.id)}"', 'href="https://tolgaarpa.github.io/halalar-web/urun.html?id=${encodeURIComponent(\'d2:\'+u.id)}"'),  # ikinci dükkân ürünleri web'de
    ('href="dukkan.html"', 'href="https://tolgaarpa.github.io/halalar-web/dukkan.html"'),
    ('href="kategori.html"', 'href="https://tolgaarpa.github.io/halalar-web/kategori.html"'),  # kategori tüneli web'de
    ('src="veri/', 'src="'),                                   # veri dosyaları app kökünde
    ('kaynak/web/', 'img/'),                                   # ürün görselleri
    ('kaynak/vitrin/', 'vitrin/'),                             # dükkân vitrin fotoğrafları
    ('kaynak/referans/', 'referans/'),                         # giriş kolajı
    ('href="urun.html?id=${encodeURIComponent(id)}"', 'href="index.html#u=${encodeURIComponent(id)}"'),  # ürün: uygulamada kart olarak açılır
    ('<a href="https://tolgaarpa.github.io/halalar-app/">Telefon uygulaması</a>', '<a href="https://tolgaarpa.github.io/halalar-web/">Web sitesi</a>'),
]
for a, b in DEGIS:
    if a not in s:
        sys.exit(f'Bulunamadı, eşitleme durdu: {a}')
    s = s.replace(a, b)
s = s.replace('<!doctype html>', '<!doctype html>\n<!-- Bu dosya araclar/hit_esitle.py ile halalar-web/hit.html dosyasından üretilir; elle düzenleme. -->', 1)
open(os.path.join(APP, 'hit.html'), 'w', encoding='utf-8').write(s)
os.makedirs(os.path.join(APP, 'vitrin'), exist_ok=True)
for f in os.listdir(os.path.join(WEB, 'kaynak', 'vitrin')):
    shutil.copy2(os.path.join(WEB, 'kaynak', 'vitrin', f), os.path.join(APP, 'vitrin', f))
# giriş kolajı: yalnız sayfanın kullandığı webp'ler (büyük kaynak PNG taşınmaz)
os.makedirs(os.path.join(APP, 'referans'), exist_ok=True)
for f in os.listdir(os.path.join(WEB, 'kaynak', 'referans')):
    if f.endswith('.webp'):
        shutil.copy2(os.path.join(WEB, 'kaynak', 'referans', f), os.path.join(APP, 'referans', f))
shutil.copy2(os.path.join(WEB, 'veri', 'dukkan2.js'), os.path.join(APP, 'dukkan2.js'))
print('hit.html eşitlendi;', len(os.listdir(os.path.join(APP, 'vitrin'))), 'vitrin fotoğrafı')

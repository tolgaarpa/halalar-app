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
    ('src="veri/', 'src="'),                                   # veri dosyaları app kökünde
    ('kaynak/web/', 'img/'),                                   # ürün görselleri
    ('kaynak/vitrin/', 'vitrin/'),                             # dükkân vitrin fotoğrafları
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
print('hit.html eşitlendi;', len(os.listdir(os.path.join(APP, 'vitrin'))), 'vitrin fotoğrafı')

#!/usr/bin/env python3
"""Hit Pazarı ikonunu (minik neon tabela) sayfaların sol üstüne ve sekme simgesine ekler.
Bir kez çalıştırılır; zaten ekli sayfaya dokunmaz. Yeni sayfa eklenirse SAYFALAR listesine yaz."""
import os, sys
APP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.expanduser('~/Desktop/halalar-web')
CSS = """
/* Hit Pazarı ikonu: minik neon tabela (her sayfanın sol üstünde) */
.hpi-sol{display:flex;align-items:center;gap:12px}
.hpi{position:relative;display:inline-grid;place-items:center;width:48px;height:34px;flex:none;text-decoration:none;pointer-events:auto;background:#0b0b0d;border-radius:9px}
.hpi svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible;filter:drop-shadow(0 0 2px #ff2d55) drop-shadow(0 0 6px #ff2d5588)}
.hpi svg rect,.hpi svg path{fill:none;stroke:#ff6b85;stroke-width:1.6;stroke-linecap:round}
.hpi b{position:relative;font:300 18px/1 Fraunces,Georgia,serif;letter-spacing:-.03em;color:#fff1ea;text-shadow:0 0 1px #fff,0 0 5px #ff5a1f,0 0 12px #ff5a1f}
"""
FAV = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2714%27 fill=%27%230b0b0d%27/%3E%3Crect x=%277%27 y=%2714%27 width=%2750%27 height=%2736%27 rx=%279%27 fill=%27none%27 stroke=%27%23ff6b85%27 stroke-width=%273%27/%3E%3Ctext x=%2732%27 y=%2741%27 font-family=%27Georgia,serif%27 font-size=%2722%27 text-anchor=%27middle%27 fill=%27%23fff1ea%27%3EHit%3C/text%3E%3C/svg%3E">'
def ikon(href):
    return (f'<a class="hpi" href="{href}" aria-label="Hit Pazarı"><svg viewBox="0 0 48 34" aria-hidden="true">'
            '<rect x="1.5" y="1.5" width="45" height="31" rx="7"/>'
            '<path d="M6 7.5c-1.6 0-2.2 1.6-1.4 2.4.7.6 1.8.2 1.5-.7"/><path d="M42 7.5c1.6 0 2.2 1.6 1.4 2.4-.7.6-1.8.2-1.5-.7"/>'
            '<path d="M6 26.5c-1.6 0-2.2-1.6-1.4-2.4.7-.6 1.8-.2 1.5.7"/><path d="M42 26.5c1.6 0 2.2-1.6 1.4-2.4-.7-.6-1.8-.2-1.5.7"/>'
            '</svg><b>Hit</b></a>')
I = ikon('hit.html')
SAYFALAR = {
  os.path.join(WEB, 'index.html'): [('<nav><span class="marka">', '<nav><span class="hpi-sol">'+I+'<span class="marka">'),
                                    ('<span class="sag">', '</span><span class="sag">')],
  os.path.join(WEB, 'hit.html'):   [('<nav><span class="marka">', '<nav><span class="hpi-sol">'+ikon('#')+'<span class="marka">'),
                                    ('</span>\n  <span class="sag">', '</span></span>\n  <span class="sag">')],
  os.path.join(WEB, 'urun.html'):  [('<nav><a class="logo" href="index.html#ic">Halalar</a>', '<nav><span class="hpi-sol">'+I+'<a class="logo" href="index.html#ic">Halalar</a></span>')],
  os.path.join(APP, 'index.html'): [('<header><div class="logo">Halalar</div>', '<header><div class="hpi-sol">'+I+'<div class="logo">Halalar</div></div>'),
                                    ('<header><div class="logo">Beğeniler</div>', '<header><div class="hpi-sol">'+I+'<div class="logo">Beğeniler</div></div>'),
                                    ('<header><div class="logo">Teklif & Alım</div>', '<header><div class="hpi-sol">'+I+'<div class="logo">Teklif & Alım</div></div>'),
                                    ('<div class="tust"><div class="marka">', '<div class="tust"><div class="hpi-sol">'+I+'<div class="marka">'),
                                    ('<div class="logo">Halalar</div></div><div class="derin"', '<div class="logo">Halalar</div></div></div><div class="derin"')],
  os.path.join(APP, 'kvkk.html'):  [('<body><main>', '<body><div class="hpi-sol" style="padding:18px 18px 0;max-width:760px;margin:0 auto">'+I+'</div><main>')],
  os.path.join(APP, 'panel.html'): [('<header><h1>Halalar <small>Dükkân paneli</small></h1>', '<header><div class="hpi-sol">'+I+'<h1>Halalar <small>Dükkân paneli</small></h1></div>')],
}
for yol, degis in SAYFALAR.items():
    s = open(yol, encoding='utf-8').read()
    if 'class="hpi"' in s:
        print('zaten var:', os.path.basename(yol)); continue
    for a, b in degis:
        if s.count(a) != 1: sys.exit(f'{yol}: bulunamadı/tekil değil: {a[:50]}')
        s = s.replace(a, b)
    s = s.replace('</style>', CSS + '</style>', 1)
    if 'rel="icon"' not in s: s = s.replace('</head>', FAV + '\n</head>', 1)
    open(yol, 'w', encoding='utf-8').write(s)
    print('eklendi:', yol.replace(os.path.expanduser('~'), '~'))

"""Gibt je Ebene (g[data-ebene]) einer SVG-Grafik den umschließenden Rahmen aus: x0 y0 x1 y1 in SVG-Einheiten.
Hilft beim Festlegen der zoom-Angaben der Scroll-Schritte.

Aufruf: rahmen.py <datei.svg>
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from _basis import browser

svg = Path(sys.argv[1]).read_text(encoding="utf-8")
with sync_playwright() as p:
    b = browser(p)
    pg = b.new_page()
    pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
    r = pg.evaluate("""() => [...document.querySelectorAll('g[data-ebene]')].map(g => {
        const k = g.getBBox();
        return g.dataset.ebene + ': ' + [k.x, k.y, k.x + k.width, k.y + k.height].map(Math.round).join(' ')})""")
    print("\n".join(r))
    b.close()

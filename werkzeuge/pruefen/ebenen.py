"""Rendert ausgewählte Ebenen (g[data-ebene]) einer SVG-Grafik wie im Browser, mit Schriften.

Aufruf: ebenen.py <ausgabe.png> <datei.svg> [ebene,ebene,…]   (ohne Liste: alle Ebenen)
Ergänzt werkzeuge/ebenen_export.py (rsvg, ohne Browser).
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from _basis import browser

aus, svg = sys.argv[1], Path(sys.argv[2]).read_text(encoding="utf-8")
zeige = sys.argv[3].split(",") if len(sys.argv) > 3 else None
with sync_playwright() as p:
    b = browser(p)
    pg = b.new_page(device_scale_factor=1.5)
    pg.set_content(f"<html><body style='margin:0;background:#fff'>{svg}</body></html>")
    if zeige:
        pg.evaluate("""z => document.querySelectorAll('g[data-ebene]').forEach(
            g => g.style.display = z.includes(g.dataset.ebene) ? '' : 'none')""", zeige)
    pg.locator("svg").first.screenshot(path=aus)
    b.close()
print(aus)

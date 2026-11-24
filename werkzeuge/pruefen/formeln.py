"""Listet abgesetzte Formeln, die auf die Spaltenbreite verkleinert werden (normal und im Beamer-Modus, 1920 × 1080).

Aufruf: formeln.py <seite> …   z. B. formeln.py vorlesung/04-schnittgroessen.html
"""
import sys
import time

from playwright.sync_api import sync_playwright

from _basis import browser, url

with sync_playwright() as p:
    b = browser(p)
    for seite in sys.argv[1:]:
        for beamer in (False, True):
            pg = b.new_page(viewport={"width": 1920, "height": 1080})
            pg.goto(url(seite))
            time.sleep(3)
            if beamer:
                pg.keyboard.press("b")
                time.sleep(1.5)
            r = pg.evaluate("""() => [...document.querySelectorAll('mjx-container[display="true"]')]
                .filter(m => m.style.fontSize && parseFloat(m.style.fontSize) < 100)
                .map(m => m.style.fontSize + ' | ' +
                     (m.closest('.schritt, section')?.querySelector('h3, h2')?.textContent || '').trim().slice(0, 50))""")
            print(f"== {seite} {'Beamer' if beamer else 'normal'}: {len(r)} verkleinert")
            for x in r:
                print("  ", x)
            pg.close()
    b.close()

"""Screenshots einzelner Scroll-Schritte bei 1920 × 1080 (Schritt mittig) und Zählung der MathJax-Fehler.

Aufruf: schritte.py <ausgabeordner> <seite> "<Teil der Schritt-Überschrift>" …
Beispiel: schritte.py /tmp/s vorlesung/04-schnittgroessen.html "Ein Stück herausschneiden" "Fahrplan"
"""
import os
import sys
import time

from playwright.sync_api import sync_playwright

from _basis import browser, url

aus, seite, titel = sys.argv[1], sys.argv[2], sys.argv[3:]
os.makedirs(aus, exist_ok=True)
with sync_playwright() as p:
    b = browser(p)
    pg = b.new_page(viewport={"width": 1920, "height": 1080})
    fehler = []
    pg.on("pageerror", lambda e: fehler.append(str(e)))
    pg.goto(url(seite))
    time.sleep(3)
    print("MathJax-Fehler (mjx-merror):", pg.locator("mjx-merror").count())
    for i, t in enumerate(titel):
        h = pg.locator(".schritt h3", has_text=t).first
        if h.count() == 0:
            print(f"  nicht gefunden: {t}")
            continue
        pg.evaluate("e => e.closest('.schritt').scrollIntoView({block: 'center'})", h.element_handle())
        time.sleep(1.8)
        datei = os.path.join(aus, f"schritt-{i + 1}.png")
        pg.screenshot(path=datei)
        print(f"  {datei}: {t}")
    if fehler:
        print("JavaScript-Fehler:", *fehler, sep="\n  ")
    b.close()

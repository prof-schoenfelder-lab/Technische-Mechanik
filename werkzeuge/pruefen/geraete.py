"""Prüft eine Seite auf Phone (390 × 844, Touch), Tablet (820 × 1180, Touch) und Desktop (1920 × 1080):
Seitenbreite (kein waagrechtes Scrollen), Sichtbarkeit von Inhaltsknopf und Randleiste, Öffnen der Liste und
Sprung über den ersten Abschnittseintrag. Screenshots landen im Ausgabeordner.

Aufruf: geraete.py <seite> [ausgabeordner]   z. B. geraete.py vorlesung/04-schnittgroessen.html /tmp/g
"""
import os
import sys
import time

from playwright.sync_api import sync_playwright

from _basis import browser, url

seite = sys.argv[1]
aus = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(aus, exist_ok=True)
GERAETE = (
    ("phone", dict(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)),
    ("tablet", dict(viewport={"width": 820, "height": 1180}, device_scale_factor=2, is_mobile=True, has_touch=True)),
    ("desktop", dict(viewport={"width": 1920, "height": 1080})),
)
ANZEIGE = """() => { const d = s => { const e = document.querySelector(s); return e ? getComputedStyle(e).display : '–' };
    return {knopf: d('.inhalt-knopf'), rand: d('.inhalt-rand'), liste: d('.inhalt-liste'),
            breite: document.documentElement.scrollWidth, fenster: innerWidth} }"""
with sync_playwright() as p:
    b = browser(p)
    for name, kw in GERAETE:
        c = b.new_context(**kw)
        pg = c.new_page()
        fehler = []
        pg.on("pageerror", lambda e: fehler.append(str(e)))
        pg.goto(url(seite))
        time.sleep(2.5)
        z = pg.evaluate(ANZEIGE)
        breit = " ZU BREIT" if z["breite"] > z["fenster"] else ""
        print(f"{name}: Seite {z['breite']}/{z['fenster']} px{breit}, Knopf {z['knopf']}, Rand {z['rand']}")
        pg.screenshot(path=os.path.join(aus, f"{name}.png"))
        if z["knopf"] != "none" and z["knopf"] != "–":
            pg.tap(".inhalt-knopf") if kw.get("has_touch") else pg.click(".inhalt-knopf")
            time.sleep(0.8)
            print(f"  Liste nach Tipp: {pg.evaluate(ANZEIGE)['liste']}")
            pg.screenshot(path=os.path.join(aus, f"{name}-offen.png"))
            eintrag = pg.locator(".inhalt-liste a.ab").nth(1)
            if eintrag.count():
                text = eintrag.inner_text().strip()
                eintrag.tap() if kw.get("has_touch") else eintrag.click()
                time.sleep(2)
                offen = pg.evaluate("() => document.querySelector('.inhalt-rand').classList.contains('mobil-offen')")
                print(f"  Sprung zu „{text[:40]}“: {pg.evaluate('location.hash')}, Liste noch offen: {offen}")
                pg.screenshot(path=os.path.join(aus, f"{name}-sprung.png"))
        if fehler:
            print("  JavaScript-Fehler:", *fehler, sep="\n    ")
        c.close()
    b.close()

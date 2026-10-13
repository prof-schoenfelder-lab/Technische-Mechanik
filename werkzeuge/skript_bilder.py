"""Standbilder der Scrollytelling-Grafiken für das PDF-Skript der Vorlesungen.

Die Schritte eines Scrollys werden zu Gruppen zusammengefasst: Solange ein Schritt alle Ebenen
des vorigen behält und nur neue hinzufügt, bleibt es ein Bild. Für jede Gruppe entsteht eine SVG
mit genau diesen Ebenen und einem Bildausschnitt um ihren Inhalt:

    grafiken/_skript/<sha1(svg|ebenen)[:12]>.svg

Der Lua-Filter (assets/scrolly.lua) bildet Gruppen und Dateinamen nach derselben Regel.
Die Begrenzungsrahmen der Ebenen liefert Inkscape (--query-all); sie werden nach SVG-Inhalt in
grafiken/_skript/_boxen.json zwischengespeichert, damit das Rendern ohne Inkscape (GitHub) klappt.
"""
import hashlib
import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
ZIEL = PROJEKT / "grafiken" / "_skript"
CACHE = ZIEL / "_boxen.json"
RAND = 10

NS = {"svg": "http://www.w3.org/2000/svg", "inkscape": "http://www.inkscape.org/namespaces/inkscape",
      "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd", "xlink": "http://www.w3.org/1999/xlink"}
for k, v in NS.items():
    ET.register_namespace("" if k == "svg" else k, v)

RE_SCROLLY = re.compile(r'^:{4,}\s*\{\.scrolly\s+svg="([^"]+)"', re.M)
RE_SCHRITT = re.compile(r'^:::\s*\{\.schritt([^}]*)\}', re.M)
RE_ENDE = re.compile(r'^:{4,}\s*$', re.M)


def attr(text, name):
    m = re.search(name + r'="([^"]*)"', text)
    return m.group(1).split() if m else []


def gruppen(schritte):
    """schritte: Liste von Ebenen-Mengen → Liste der Gruppen-Ebenenmengen (Vereinigung je Gruppe)."""
    out, akt = [], None
    for s in schritte:
        if akt is not None and s >= akt:
            akt = s
        else:
            if akt is not None:
                out.append(akt)
            akt = s
    if akt is not None:
        out.append(akt)
    return out


def schluessel(svg_rel, ebenen):
    return hashlib.sha1((svg_rel + "|" + " ".join(sorted(ebenen))).encode()).hexdigest()[:12]


def scrollys(qmd):
    """(svg-Pfad relativ zur qmd, [Ebenenmengen der Schritte]) für jedes Scrolly."""
    text = qmd.read_text(encoding="utf-8")
    for m in RE_SCROLLY.finditer(text):
        ende = RE_ENDE.search(text, m.end())
        block = text[m.end():ende.start() if ende else len(text)]
        schritte = [set(attr(a, "zeige")) | set(attr(a, "dimmen")) for a in RE_SCHRITT.findall(block)]
        yield m.group(1), schritte


def inkscape_boxen(pfad):
    erg = subprocess.run(["inkscape", "--query-all", str(pfad)], capture_output=True, text=True, timeout=180)
    boxen = {}
    for zeile in erg.stdout.splitlines():
        teile = zeile.split(",")
        if len(teile) == 5:
            try:
                boxen[teile[0]] = [float(t) for t in teile[1:]]
            except ValueError:
                pass
    return boxen


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    auftraege = {}                                  # Ziel-Datei → (svg-Pfad, Ebenen)
    for qmd in sorted((PROJEKT / "vorlesung").glob("*.qmd")):
        for svg_rel, schritte in scrollys(qmd):
            svg = (qmd.parent / svg_rel).resolve()
            rel = svg.relative_to(PROJEKT).as_posix()
            for ebenen in gruppen(schritte):
                auftraege[ZIEL / f"{schluessel(rel, ebenen)}.svg"] = (svg, ebenen)

    # Begrenzungsrahmen je SVG (nach Inhalt zwischengespeichert)
    hashes = {svg: hashlib.sha1(svg.read_bytes()).hexdigest() for svg, _ in auftraege.values()}
    fehlend = [svg for svg, h in hashes.items() if h not in cache]
    if fehlend and shutil.which("inkscape"):
        with ThreadPoolExecutor(6) as pool:
            for svg, boxen in zip(fehlend, pool.map(inkscape_boxen, fehlend)):
                cache[hashes[svg]] = boxen
    gueltig = set(hashes.values())
    cache = {h: b for h, b in cache.items() if h in gueltig}
    CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))

    for datei, (svg, ebenen) in auftraege.items():
        baum = ET.parse(svg)
        wurzel = baum.getroot()
        boxen = cache.get(hashes[svg], {})
        x0 = y0 = float("inf")
        x1 = y1 = float("-inf")
        for g in list(wurzel):
            if g.get(f"{{{NS['inkscape']}}}groupmode") != "layer":
                continue
            if g.get("id") not in ebenen:
                wurzel.remove(g)
                continue
            g.attrib.pop("style", None)
            b = boxen.get(g.get("id"))
            if b:
                x0, y0 = min(x0, b[0]), min(y0, b[1])
                x1, y1 = max(x1, b[0] + b[2]), max(y1, b[1] + b[3])
        if x0 < x1:
            vb = [x0 - RAND, y0 - RAND, x1 - x0 + 2 * RAND, y1 - y0 + 2 * RAND]
        else:                                       # ohne Inkscape-Daten: ganze Zeichenfläche
            vb = [float(v) for v in wurzel.get("viewBox").split()]
        wurzel.set("viewBox", " ".join(f"{v:.1f}" for v in vb))
        wurzel.set("width", f"{vb[2]:.1f}")
        wurzel.set("height", f"{vb[3]:.1f}")
        neu = ET.tostring(wurzel, encoding="unicode")
        if not datei.exists() or datei.read_text(encoding="utf-8") != neu:
            datei.write_text(neu, encoding="utf-8")

    for alt in ZIEL.glob("*.svg"):
        if alt not in auftraege:
            alt.unlink()


if __name__ == "__main__":
    main()

"""Grafiken zu Woche 3 (Übung Gleichgewicht): Gelenkträger (Götz 1.3.12), Fahrradrahmen als Fachwerk,
Balken mit Streckenlast q(x) = q0 (x/L − (x/L)^6).

Aufruf:  python werkzeuge/grafiken_gleichgewicht.py
Ergebnis: grafiken/gleichgewicht/*.svg (Inkscape-Ebenen = Scroll-Schritte)

Koordinaten wie in Woche 1 und 2: x nach rechts, y nach oben; Momente gegen den Uhrzeigersinn positiv.
"""

import math
from pathlib import Path

from grafiken_grundlagen import GRUEN, ROT, koord_xy, punkt
from tmzeichnen import (FARBE, STRICH, Abbildung, balken, festlager, gelenk, gelenk_offen, kraft, kreis, linie,
                        loslager, mass, nummer, pfeil, polylinie, schnitt, schnittlinie, streckenlast, text, winkelbogen)

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "gleichgewicht"
SCHWARZ = "#000000"
GRAU_HELL = "#9a9a9a"
BLAU = "#0050b4"                                # negativ (Druck), wie bei den Schnittgrößenverläufen
T = 3.5                                         # halbe Balkendicke (balken dicke=7)


# =====================================================================
# 1  Fahrradrahmen als Fachwerk
# =====================================================================
P = 50                                          # px je a (a = 0,1 m)
KN = {"I": (130, 330), "II": (330, 330), "III": (330, 180), "IV": (530, 180)}
STAEBE = {1: ("I", "II"), 2: ("I", "III"), 3: ("II", "III"), 4: ("II", "IV"), 5: ("III", "IV")}
# Stabkräfte in N (Zug positiv), siehe Vorlesung
S = {1: 650, 2: -687.5, 3: -187.5, 4: 812.5, 5: -550}
BETA = math.degrees(math.atan2(3, 4))           # 36,87°


def _richtung(von, nach):
    (x1, y1), (x2, y2) = KN[von], KN[nach]
    return math.degrees(math.atan2(-(y2 - y1), x2 - x1))


def _stab_mitte(nr):
    a, b = STAEBE[nr]
    return (KN[a][0] + KN[b][0]) / 2, (KN[a][1] + KN[b][1]) / 2


def _zahl(v):
    s = f"{abs(v):.1f}".rstrip("0").rstrip(".").replace(".", ",")
    return ("−" if v < 0 else "") + s


def schnittkreis(x, y, r=42, wellen=9, amplitude=3.5):
    """Gedanklicher Schnitt rund um einen Knoten: geschlossene grüne Schlangenlinie."""
    pts = [(x + (r + amplitude * math.sin(wellen * w)) * math.cos(w), y + (r + amplitude * math.sin(wellen * w)) * math.sin(w))
           for w in (2 * math.pi * i / 180 for i in range(181))]
    return polylinie(pts, FARBE["mass"], 1.6)


def _knotenbild(e, cx, cy, name, staebe, lasten, name_pos=(-14, -14)):
    """Freigeschnittener Knoten: kurze Stabstümpfe, Stabkräfte als Zug (vom Knoten weg), äußere Kräfte."""
    for winkel, nr, _ in staebe:
        ux, uy = math.cos(math.radians(winkel)), -math.sin(math.radians(winkel))
        e.append(linie(cx, cy, cx + ux * 34, cy + uy * 34, GRAU_HELL, 5, kappe="round"))
    for winkel, nr, seite in staebe:
        e.append(kraft(cx, cy, winkel, f"S_{nr}", laenge=62, ziehend=True, label_seite=seite, label_pos=0.85))
    for args in lasten:
        e.append(kraft(cx, cy, *args[:2], **args[2]))
    e.append(punkt(cx, cy, 4))
    e.append(text(cx + name_pos[0], cy + name_pos[1], f"[{name}]", SCHWARZ, 16, anker="end" if name_pos[0] < 0 else "start", italic=False))


def fahrrad():
    abb = Abbildung(900, 700, "Fahrradrahmen als Fachwerk")
    (xI, yI), (xII, yII), (xIII, yIII), (xIV, yIV) = (KN[k] for k in ("I", "II", "III", "IV"))

    # Ansicht: Fahrrad schematisch
    e = abb.ebene("ansicht", "Fahrrad")
    xV, rr = xIV + 80, 120
    yb = yI + rr
    e.append(linie(20, yb, 780, yb, SCHWARZ, STRICH["normal"]))
    for x in (xI, xV):
        e.append(kreis(x, yI, rr, "#555555", "none", 2.2))
        e.append(kreis(x, yI, 5, "#555555", "#555555", 1))
    for a, b in STAEBE.values():
        e.append(linie(*KN[a], *KN[b], "#3c6e9e", 6, kappe="round"))
    e.append(linie(xIV, yIV, xV, yI, "#3c6e9e", 5, kappe="round"))           # Gabel
    e.append(linie(xIV, yIV, xIV - 12, yIV - 45, "#555555", 4, kappe="round"))  # Vorbau
    e.append(linie(xIV - 30, yIV - 48, xIV + 6, yIV - 42, "#555555", 5, kappe="round"))
    e.append(linie(xIII, yIII, xIII - 8, yIII - 40, "#555555", 4, kappe="round"))  # Sattelstütze
    e.append(polylinie([(xIII - 40, yIII - 46), (xIII + 22, yIII - 44), (xIII + 22, yIII - 38), (xIII - 38, yIII - 38)],
                       "#333333", 1.2, "#333333", schliessen=True))
    e.append(kreis(xII, yII, 22, "#555555", "none", 2))
    e.append(linie(xII, yII, xII + 30, yII + 34, "#555555", 4, kappe="round"))

    # Modell: Stäbe, Knoten, Nummern
    e = abb.ebene("fachwerk", "Fachwerk")
    for nr, (a, b) in STAEBE.items():
        e.append(balken(*KN[a], *KN[b], dicke=6))
    for k, (x, y) in KN.items():
        e.append(kreis(x, y, 4.5))
    for k, (dx, dy) in {"I": (-18, -14), "II": (-18, 26), "III": (-16, -16), "IV": (48, -8)}.items():
        x, y = KN[k]
        e.append(text(x + dx, y + dy, f"[{k}]", SCHWARZ, 16, italic=False))

    e = abb.ebene("lager", "Lager")
    e.append(festlager(xI, yI, label="B", label_pos=(-26, 18)))
    e.append(loslager(xIV, yIV, label="A", label_pos=(30, 26)))

    e = abb.ebene("lasten", "Lasten")
    e.append(kraft(xIII, yIII - 5, -90, "F_S", laenge=62, label_seite=-1, label_pos=0.6))
    e.append(kraft(xII, yII + 5, -90, "F_P", laenge=60, ziehend=True, label_seite=-1, label_pos=0.6))
    e.append(kraft(xIV - 3, yIV - 3, -45, "F_L", laenge=70, label_seite=1, label_pos=0.8))

    e = abb.ebene("mass", "Bemaßung")
    e.append(linie(xIV, yIV, xIV + 60, yIV, GRUEN, STRICH["duenn"], strich="3 2"))
    e.append(winkelbogen(xIV, yIV, 30, 0, 135, "135°"))
    e.append(mass(xI, yI, xII, yII, "4a", abstand=-62))
    e.append(mass(xII, yII, xIV, yII, "4a", abstand=-62))
    e.append(mass(xIV, yII, xIV, yIV, "3a", abstand=-90, hilfslaenge=10))
    e.append(winkelbogen(xI, yI, 52, 0, BETA, "β"))
    e.append(koord_xy(40, 140, 30, 30))

    e = abb.ebene("schnitt-lager", "Schnitt an den Lagern")
    e.append(schnitt(xI - 22, yI + 9, xI + 22, yI + 9))
    e.append(schnitt(xIV - 6, yIV + 11, xIV + 18, yIV + 11))

    for k, (x, y) in KN.items():
        abb.ebene(f"schnitt-{k}", f"Schnitt um Knoten {k}").append(schnittkreis(x, y))

    e = abb.ebene("reaktionen", "Lagerreaktionen")
    e.append(kraft(xIV, yIV + 5, 90, "F_A", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(kraft(xI - 5, yI, 0, "F_{BH}", laenge=56, label_seite=1, label_pos=0.7))
    e.append(kraft(xI, yI + 5, 90, "F_{BV}", laenge=60, label_seite=1, label_pos=0.6))

    # Freigeschnittene Knoten (untere Reihe)
    y0 = 560
    lasten = {
        "IV": [(-45, "F_L", {"laenge": 58, "label_seite": -1, "label_pos": 0.8}),
               (90, "F_A", {"laenge": 55, "label_seite": 1, "label_pos": 0.6})],
        "III": [(-90, "F_S", {"laenge": 55, "label_seite": -1, "label_pos": 0.6})],
        "II": [(-90, "F_P", {"laenge": 55, "ziehend": True, "label_seite": -1, "label_pos": 0.6})],
        "I": [(0, "F_{BH}", {"laenge": 50, "label_seite": 1, "label_pos": 0.75}),
              (90, "F_{BV}", {"laenge": 55, "label_seite": 1, "label_pos": 0.6})],
    }
    staebe = {"IV": [(180, 5, 1), (180 + BETA, 4, -1)], "III": [(0, 5, -1), (270, 3, -1), (180 + BETA, 2, -1)],
              "II": [(BETA, 4, -1), (90, 3, -1), (180, 1, 1)], "I": [(0, 1, 1), (BETA, 2, -1)]}
    for i, k in enumerate(("IV", "III", "II", "I")):
        e = abb.ebene(f"knoten-{k}", f"Knoten {k}")
        _knotenbild(e, 120 + i * 215, y0, k, staebe[k], lasten[k], (14, -12) if k == "IV" else (-14, -14))

    # Ergebnis: Zug rot, Druck blau
    e = abb.ebene("ergebnis", "Stabkräfte")
    for nr, (a, b) in STAEBE.items():
        e.append(linie(*KN[a], *KN[b], ROT if S[nr] > 0 else BLAU, 6, kappe="round"))
    pos = {1: (0, 26, "middle"), 2: (-20, -12, "end"), 3: (12, 6, "start"), 4: (22, 14, "start"), 5: (0, -14, "middle")}
    for nr in STAEBE:
        mx, my = _stab_mitte(nr)
        dx, dy, anker = pos[nr]
        e.append(text(mx + dx, my + dy, f"[{_zahl(S[nr])} N]", ROT if S[nr] > 0 else BLAU, 16, anker=anker, italic=False))
    e.append(text(620, 300, "[Zug]", ROT, 17, anker="start", italic=False))
    e.append(text(620, 324, "[Druck]", BLAU, 17, anker="start", italic=False))
    e = abb.ebene("nummern", "Stabnummern")
    for nr in STAEBE:
        mx, my = _stab_mitte(nr)
        dx, dy = {1: (0, -16), 2: (12, -16), 3: (-16, 0), 4: (-14, 14), 5: (0, 16)}[nr]
        e.append(nummer(mx + dx, my + dy, nr))
    return abb.speichern(ZIEL / "fahrrad.svg")


# =====================================================================
# 2  Gelenkträger (nach Götz 1.3.12)
# =====================================================================
def gelenktraeger():
    abb = Abbildung(860, 470, "Gelenkträger")
    l = 60                                      # px je l
    x0, y = 110, 140
    def X(k):
        return x0 + k * l
    e = abb.ebene("system", "System")
    e.append(balken(X(0), y, X(4), y))
    e.append(balken(X(4), y, X(6), y))
    e.append(gelenk(X(4), y, r=5))
    e.append(text(X(4), y + 26, "G", SCHWARZ, 17))
    e.append(festlager(X(0), y + T, label="A", label_pos=(-22, 12)))
    e.append(loslager(X(3), y + T, label="B", label_pos=(-22, 12)))
    e.append(loslager(X(6), y + T, label="C", label_pos=(22, 12)))
    e.append(streckenlast(X(0), X(6), y - T, 32, label="q", n=24))
    e.append(kraft(X(2), y - T, -90, "F", laenge=72, label_seite=-1, label_pos=0.85))
    for a, b, lab in ((0, 2, "2l"), (2, 3, "l"), (3, 4, "l"), (4, 6, "2l")):
        e.append(mass(X(a), y, X(b), y, lab, abstand=-58))
    e.append(koord_xy(30, 60, 28, 28))

    e = abb.ebene("schnitt", "Schnitte: Gelenk und Lager")
    e.append(schnittlinie(X(4), y, hoehe=44))
    for k in (0, 3, 6):                         # durch die Lager, knapp unter dem Gelenkpunkt
        e.append(schnitt(X(k) - 14, y + T + 8, X(k) + 14, y + T + 8))

    # Ganzer Träger freigeschnitten (Kontrolle): Lager ersetzt, Gelenk geschlossen
    e = abb.ebene("gesamt", "Ganzer Träger")
    e.append(balken(X(0), y, X(4), y))
    e.append(balken(X(4), y, X(6), y))
    e.append(gelenk(X(4), y, r=5))
    e.append(text(X(4), y + 26, "G", SCHWARZ, 17))
    e.append(streckenlast(X(0), X(6), y - T, 32, label="q", n=24))
    e.append(kraft(X(2), y - T, -90, "F", laenge=72, label_seite=-1, label_pos=0.85))
    e.append(kraft(X(0), y + T, 90, "F_{AV}", laenge=50, label_seite=1, label_pos=0.6))
    e.append(kraft(X(0) - 4, y, 0, "F_{AH}", laenge=44, label_seite=-1))
    e.append(kraft(X(3), y + T, 90, "F_B", laenge=50, label_seite=-1, label_pos=0.6))
    e.append(kraft(X(6), y + T, 90, "F_C", laenge=50, label_seite=-1, label_pos=0.6))
    e.append(punkt(X(0), y, 3))
    for a, b, lab in ((0, 2, "2l"), (2, 3, "l"), (3, 6, "3l")):
        e.append(mass(X(a), y, X(b), y, lab, abstand=-80))

    y2 = 360
    d = 90
    e = abb.ebene("freischnitt", "Freikörperbilder")
    e.append(balken(X(0), y2, X(4), y2))
    e.append(balken(X(4) + d, y2, X(6) + d, y2))
    e.append(gelenk_offen(X(4), y2, 180))
    e.append(gelenk_offen(X(4) + d, y2, 0))
    e.append(streckenlast(X(0), X(4), y2 - T, 28, label="q", n=16))
    e.append(streckenlast(X(4) + d, X(6) + d, y2 - T, 28, label="q", n=8))
    e.append(kraft(X(2), y2 - T, -90, "F", laenge=62, label_seite=-1, label_pos=0.85))
    e.append(kraft(X(0), y2 + T, 90, "F_{AV}", laenge=48, label_seite=1, label_pos=0.6))
    e.append(kraft(X(0) - 4, y2, 0, "F_{AH}", laenge=44, label_seite=-1))
    e.append(kraft(X(3), y2 + T, 90, "F_B", laenge=48, label_seite=-1, label_pos=0.6))
    e.append(kraft(X(6) + d, y2 + T, 90, "F_C", laenge=48, label_seite=-1, label_pos=0.6))
    # Gelenkkräfte: an I nach unten/rechts, an II nach oben/links (actio = reactio)
    e.append(kraft(X(4), y2 + T, -90, "G_V", laenge=46, ziehend=True, label_seite=1, label_pos=0.7))
    e.append(kraft(X(4), y2, 0, "G_H", laenge=30, ziehend=True, label_seite=1))
    e.append(kraft(X(4) + d, y2 + T, 90, "G_V", laenge=46, label_seite=1, label_pos=0.7))
    e.append(kraft(X(4) + d, y2, 180, "G_H", laenge=30, ziehend=True, label_seite=-1))
    e.append(text(X(2), y2 + 74, "[I]", "#555555", 16, italic=False))
    e.append(text(X(5) + d, y2 + 74, "[II]", "#555555", 16, italic=False))
    return abb.speichern(ZIEL / "gelenktraeger.svg")


# =====================================================================
# 3  Balken mit Streckenlast q(x) = q0 (x/L − (x/L)^6)
# =====================================================================
def _q(xi):
    return xi - xi ** 6


def balken_qx():
    abb = Abbildung(700, 470, "Balken mit veränderlicher Streckenlast")
    L, x0, y = 480, 100, 170
    hmax = 90 / _q(6 ** -0.2)                  # Skala: Lastspitze 90 px hoch

    e = abb.ebene("balken", "Balken")
    e.append(balken(x0, y, x0 + L, y))
    e.append(festlager(x0, y + T, label="A", label_pos=(-22, 12)))
    e.append(loslager(x0 + L, y + T, label="B", label_pos=(22, 12)))
    e.append(mass(x0, y, x0 + L, y, "L", abstand=-56))
    e.append(koord_xy(30, 60, 30, 30))

    e = abb.ebene("last", "Streckenlast")
    yo = y - T
    pts = [(x0 + L * i / 120, yo - hmax * _q(i / 120)) for i in range(121)]
    e.append(polylinie(pts, ROT, STRICH["normal"]))
    for i in range(1, 16):
        xi = i / 16
        h = hmax * _q(xi)
        if h > 6:
            e.append(pfeil(x0 + L * xi, yo - h, x0 + L * xi, yo, ROT, STRICH["normal"], (8, 5.5)))
    e.append(text(x0 + L * 0.7 + 20, yo - hmax * _q(0.7) - 14, "q(x)", ROT, anker="start"))

    xR = x0 + L * 7 / 12
    e = abb.ebene("ersatz", "Resultierende")
    e.append(kraft(xR, yo, -90, "F_R", laenge=80, label_seite=-1, label_pos=0.7))
    e.append(mass(x0, y, xR, y, "x_R", abstand=-92, hilfslaenge=12))

    yf = 400
    e = abb.ebene("freikoerper", "Freikörperbild")
    e.append(balken(x0, yf, x0 + L, yf))
    e.append(kraft(xR, yf - T, -90, "F_R", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(kraft(x0, yf + T, 90, "F_{AV}", laenge=50, label_seite=1, label_pos=0.6))
    e.append(kraft(x0 - 4, yf, 0, "F_{AH}", laenge=46, label_seite=-1))
    e.append(kraft(x0 + L, yf + T, 90, "F_B", laenge=50, label_seite=-1, label_pos=0.6))
    e.append(punkt(x0, yf, 3))
    e.append(text(x0 + 8, yf - 16, "A", SCHWARZ, 16, anker="start"))
    return abb.speichern(ZIEL / "balken-qx.svg")


if __name__ == "__main__":
    for fn in (fahrrad, gelenktraeger, balken_qx):
        print(fn())

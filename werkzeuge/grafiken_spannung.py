"""Grafiken zur Vorlesung 5: Spannung, Dehnung, Stoffgesetz.

Feder als Modell, Spannung (viele kleine Federn im Querschnitt), Normal- und Schubspannung, abgesetzter Stab,
Kerbe, Dehnung am Gummiband, Zugversuch, Querkontraktion/Schub/Wärmedehnung, Beispiel Kupferkabel,
Zusammenfassung.
Aufruf:  python werkzeuge/grafiken_spannung.py
Ergebnis: grafiken/spannung/*.svg (Inkscape-Ebenen = Scroll-Schritte)
"""

import math
from pathlib import Path

from grafiken_grundlagen import GRAU, GRUEN, ROT, hinweis, koord_xy, platte, punkt
from grafiken_mathematik import _decke, feder
from tmzeichnen import (STRICH, Abbildung, _spitze, balken, einspannung, festlager, gruppe, kraft, kreis, linie,
                        loslager, mass, pfeil, polylinie, schnitt, schnittlinie, text, verlauf, winkelbogen)

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "spannung"
SCHWARZ = "#000000"
BLAU = "#0050b4"
HELL = "#e6e6e6"
DUNKELROT = "#9b0000"


# ---------------------------------------------------------------- Hilfen
def feder_h(x1, x2, y, breite=16, windungen=6, farbe=SCHWARZ, vor=8, dicke=1.3):
    """Schraubenfeder (Zickzack) waagerecht von x1 nach x2."""
    pts = [(x1, y), (x1 + vor, y)]
    n = 2 * windungen
    h = (x2 - x1 - 2 * vor) / n
    for i in range(n):
        pts.append((x1 + vor + (i + 0.5) * h, y + (breite / 2 if i % 2 == 0 else -breite / 2)))
    pts += [(x2 - vor, y), (x2, y)]
    return polylinie(pts, farbe, dicke)


def rechteck(x0, y0, x1, y1, fuellung=HELL, farbe=SCHWARZ, breite=STRICH["normal"], strich=None):
    return polylinie([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], farbe, breite, fuellung, strich=strich,
                     schliessen=True)


def stab(x0, x1, y, dicke):
    """Waagerechter Stab als Rechteck mit Achse y."""
    return rechteck(x0, y - dicke / 2, x1, y + dicke / 2)


def endplatte(x, y, hoehe):
    return rechteck(x, y - hoehe / 2, x + 7, y + hoehe / 2, "#cfcfcf")


def gestrichelt(x1, y1, x2, y2):
    return linie(x1, y1, x2, y2, GRAU, STRICH["duenn"], strich="4 3")


def zahl(x, y, s, farbe=SCHWARZ, groesse=14, anker="middle"):
    """Zahl oder Einheit aufrecht (Latin Modern)."""
    return text(x, y, f"[{s}]", farbe, groesse, anker=anker, italic=False)


# =====================================================================
# Einordnung: von der Stereostatik zur Elastostatik (nach der Grafik aus Vorlesung 1)
# =====================================================================
def einordnung():
    from grafiken_grundlagen import kasten
    abb = Abbildung(660, 430, "Einordnung: Elastostatik")
    knoten = {"mech": (320, 45), "dyn": (112, 182), "stat": (440, 182), "stereo": (330, 322), "elasto": (540, 322)}
    groesse = {"mech": 340, "dyn": 210, "stat": 220, "stereo": 196, "elasto": 196}
    e = abb.ebene("baum", "Gliederung der Mechanik")
    for a, b in (("mech", "dyn"), ("mech", "stat"), ("stat", "stereo"), ("stat", "elasto")):
        (x1, y1), (x2, y2) = knoten[a], knoten[b]
        e.append(linie(x1, y1 + 38, x2, y2 - 38, "#444444", STRICH["normal"]))
    for k, zeilen in (("mech", ["Technische Mechanik", "Kräfte und ihre Wirkungen"]),
                      ("dyn", ["Dynamik", "Körper in Bewegung"]), ("stat", ["Statik", "Körper in Ruhe"]),
                      ("stereo", ["Stereostatik", "starre Körper"]), ("elasto", ["Elastostatik", "verformbare Körper"])):
        e.append(kasten(*knoten[k], groesse[k], 76, zeilen, gr1=28, gr2=19))
    e = abb.ebene("bisher", "Bisher: Stereostatik")
    x, y = knoten["stereo"]
    e.append(rechteck(x - 102, y - 44, x + 102, y + 44, "none", GRAU, 1.8, strich="7 4"))
    e.append(text(x, y + 66, "[Vorlesungen 0–4]", GRAU, 18, italic=False))
    e = abb.ebene("jetzt", "Jetzt: Elastostatik")
    x, y = knoten["elasto"]
    e.append(rechteck(x - 102, y - 44, x + 102, y + 44, "none", ROT, 2.6))
    e.append(text(x, y + 66, "[ab Vorlesung 5]", ROT, 18, italic=False))
    return abb.speichern(ZIEL / "einordnung.svg")


# =====================================================================
# Beanspruchungsarten: fünf Kacheln
# =====================================================================
def beanspruchungsarten():
    from grafiken_mathematik import doppelpfeil
    from tmzeichnen import moment
    W, H, rand = 280, 200, 14
    abb = Abbildung(2 * W + 3 * rand, 2 * H + 3 * rand, "Beanspruchungsarten")

    def kachel(e, i, titel):
        x, y = rand + (i % 2) * (W + rand), rand + (i // 2) * (H + rand)
        e.append(polylinie([(x, y), (x + W, y), (x + W, y + H), (x, y + H)], "#c8c8c8", 1.2, "#fafafa",
                           schliessen=True))
        e.append(text(x + W / 2, y + H - 18, f"[{titel}]", SCHWARZ, 18, italic=False))
        return x + (W - 200) / 2, y      # Inhalt ist für 200 px breite Kacheln gezeichnet

    e = abb.ebene("zug", "Zug und Druck")
    x, y = kachel(e, 0, "Zug / Druck")
    for yy, zug in ((y + 55, True), (y + 115, False)):
        e.append(stab(x + 55, x + 145, yy, 16))
        if zug:
            e.append(kraft(x + 55, yy, 180, "", laenge=36, ziehend=True))
            e.append(kraft(x + 145, yy, 0, "", laenge=36, ziehend=True))
        else:
            e.append(kraft(x + 55, yy, 0, "", laenge=36))
            e.append(kraft(x + 145, yy, 180, "", laenge=36))

    e = abb.ebene("biegung", "Biegung")
    x, y = kachel(e, 1, "Biegung")
    yy = y + 80
    pts = [(x + 40 + 120 * i / 30, yy + 14 * math.sin(math.pi * i / 30)) for i in range(31)]
    e.append(stab(x + 40, x + 160, yy, 12).replace('fill="#e6e6e6"', 'fill="none"').replace('stroke="#000000"', 'stroke="#9a9a9a" stroke-dasharray="4 3"'))
    from grafiken_mathematik import biegebalken
    e.append(biegebalken(pts, dicke=12))
    e.append(moment(x + 38, yy, "", gegen_uhrzeiger=False, r=18, start=150, bogen=220))
    e.append(moment(x + 162, yy, "", gegen_uhrzeiger=True, r=18, start=30, bogen=220))

    e = abb.ebene("torsion", "Torsion")
    x, y = kachel(e, 2, "Torsion")
    yy = y + 80
    e.append(stab(x + 50, x + 150, yy, 22))
    e.append(doppelpfeil(x + 50, yy, x + 12, yy))
    e.append(doppelpfeil(x + 150, yy, x + 188, yy))
    for k in range(4):
        xx = x + 62 + 26 * k
        e.append(linie(xx, yy - 11, xx + 12, yy + 11, GRAU, STRICH["duenn"]))

    e = abb.ebene("schub", "Schub")
    x, y = kachel(e, 3, "Schub / Scherung")
    yy = y + 80
    e.append(rechteck(x + 30, yy - 22, x + 120, yy - 2))
    e.append(rechteck(x + 80, yy + 2, x + 170, yy + 22))
    e.append(rechteck(x + 92, yy - 30, x + 108, yy + 30, "#cfcfcf"))
    e.append(kraft(x + 30, yy - 12, 180, "", laenge=26, ziehend=True))
    e.append(kraft(x + 170, yy + 12, 0, "", laenge=26, ziehend=True))
    e.append(linie(x + 86, yy, x + 114, yy, ROT, 1.8))

    return abb.speichern(ZIEL / "beanspruchungsarten.svg")


# =====================================================================
# Die Feder als Modell: Feder, Stab, doppelte Fläche, doppelte Länge
# =====================================================================
def feder_modell():
    abb = Abbildung(900, 510, "Die Feder als Modell für den Stab")
    xw, L0, u = 60, 110, 30                     # Wand, Federlänge unbelastet, Verschiebung
    xs, ls, us = 500, 150, 22                   # Stab: Wand, Länge, Verlängerung (überhöht)
    r1, r2, r3 = 95, 250, 425                   # Zeilen

    # --- eine Feder
    e = abb.ebene("feder", "Feder")
    e.append(hinweis(xw - 10, r1 - 72, "eine Feder"))
    e.append(einspannung(xw, r1, 54, "links"))
    xe = xw + L0 + u
    e.append(feder_h(xw, xe, r1, windungen=6))
    e.append(endplatte(xe, r1, 34))
    e.append(kraft(xe + 7, r1, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(gestrichelt(xw + L0, r1 - 30, xw + L0, r1 + 26))
    e.append(mass(xw + L0, r1 + 17, xe, r1 + 17, "u", abstand=-18, hilfslinien=False))
    e.append(text(xe + 70, r1 - 30, "F = c u", SCHWARZ, 18, anker="start"))

    # --- Stab
    e = abb.ebene("stab", "Stab")
    e.append(hinweis(xs - 10, r1 - 72, "ein Stab: eine sehr steife Feder"))
    e.append(einspannung(xs, r1, 54, "links"))
    e.append(stab(xs, xs + ls + us, r1, 16))
    e.append(kraft(xs + ls + us, r1, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(gestrichelt(xs + ls, r1 - 26, xs + ls, r1 + 26))
    e.append(mass(xs + ls, r1 + 8, xs + ls + us, r1 + 8, "u", abstand=-24, hilfslinien=False))
    e.append(mass(xs, r1 - 8, xs + ls, r1 - 8, "l", abstand=26))
    e.append(text(xs + 60, r1, "E, A", GRUEN, 15))
    e.append(text(xs + ls + us + 66, r1 - 30, "c = EA / l", SCHWARZ, 18, anker="start"))

    # --- doppelte Fläche: zwei Federn nebeneinander
    e = abb.ebene("parallel", "Doppelte Fläche")
    e.append(hinweis(xw - 10, r2 - 62, "zwei Federn nebeneinander"))
    e.append(einspannung(xw, r2, 74, "links"))
    for dy in (-18, 18):
        e.append(feder_h(xw, xe, r2 + dy, breite=13, windungen=6))
    e.append(endplatte(xe, r2, 58))
    e.append(kraft(xe + 7, r2, 0, "2F", laenge=50, ziehend=True, label_seite=1))
    e.append(gestrichelt(xw + L0, r2 - 40, xw + L0, r2 + 38))
    e.append(mass(xw + L0, r2 + 29, xe, r2 + 29, "u", abstand=-18, hilfslinien=False))
    e.append(hinweis(xs - 10, r2 - 62, "Stab mit doppelter Fläche"))
    e.append(einspannung(xs, r2, 64, "links"))
    e.append(stab(xs, xs + ls + us, r2, 32))
    e.append(kraft(xs + ls + us, r2, 0, "2F", laenge=50, ziehend=True, label_seite=1))
    e.append(gestrichelt(xs + ls, r2 - 32, xs + ls, r2 + 32))
    e.append(mass(xs + ls, r2 + 16, xs + ls + us, r2 + 16, "u", abstand=-24, hilfslinien=False))
    e.append(text(xs + 60, r2, "E, 2A", GRUEN, 15))

    # --- doppelte Länge: zwei Federn hintereinander
    e = abb.ebene("reihe", "Doppelte Länge")
    e.append(hinweis(xw - 10, r3 - 72, "zwei Federn hintereinander"))
    e.append(einspannung(xw, r3, 54, "links"))
    xm = xw + L0 + u
    e.append(feder_h(xw, xm, r3, windungen=6))
    e.append(rechteck(xm, r3 - 12, xm + 6, r3 + 12, "#cfcfcf"))
    xe2 = xm + 6 + L0 + u
    e.append(feder_h(xm + 6, xe2, r3, windungen=6))
    e.append(endplatte(xe2, r3, 34))
    e.append(kraft(xe2 + 7, r3, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(gestrichelt(xw + 2 * L0 + 6, r3 - 30, xw + 2 * L0 + 6, r3 + 26))
    e.append(mass(xw + 2 * L0 + 6, r3 + 17, xe2, r3 + 17, "2u", abstand=-18, hilfslinien=False))
    e.append(hinweis(xs - 10, r3 - 72, "Stab mit doppelter Länge"))
    e.append(einspannung(xs, r3, 54, "links"))
    e.append(stab(xs, xs + 2 * ls * 0.8 + 2 * us, r3, 16))
    e.append(kraft(xs + 2 * ls * 0.8 + 2 * us, r3, 0, "F", laenge=44, ziehend=True, label_seite=1))
    e.append(gestrichelt(xs + 2 * ls * 0.8, r3 - 26, xs + 2 * ls * 0.8, r3 + 26))
    e.append(mass(xs + 2 * ls * 0.8, r3 + 8, xs + 2 * ls * 0.8 + 2 * us, r3 + 8, "2u", abstand=-24,
                  hilfslinien=False))
    e.append(mass(xs, r3 - 8, xs + 2 * ls * 0.8, r3 - 8, "2l", abstand=26))
    e.append(text(xs + 60, r3, "E, A", GRUEN, 15))
    return abb.speichern(ZIEL / "feder-modell.svg")


# =====================================================================
# Spannung: Schnitt, Normalkraft, viele kleine Federn, Kraft je Fläche
# =====================================================================
def spannung():
    abb = Abbildung(940, 450, "Spannung: Kraft je Fläche")
    x0, x1, xs, d = 110, 530, 320, 46
    r1, r2, r3, r4 = 60, 160, 270, 380
    lagen = [-18, -9, 0, 9, 18]

    e = abb.ebene("system", "Stab unter Zug")
    e.append(stab(x0, x1, r1, d))
    e.append(kraft(x0, r1, 180, "F", laenge=50, ziehend=True, label_seite=-1))
    e.append(kraft(x1, r1, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(text(x0 + 60, r1, "A", GRUEN, 16))

    e = abb.ebene("schnitt", "Schnitt")
    e.append(schnittlinie(xs, r1, hoehe=70))

    e = abb.ebene("normalkraft", "Normalkraft im Schnitt")
    e.append(stab(x0, xs, r2, d))
    e.append(kraft(x0, r2, 180, "F", laenge=50, ziehend=True, label_seite=-1))
    e.append(kraft(xs, r2, 0, "N", laenge=50, ziehend=True, label_seite=1))

    e = abb.ebene("federn", "Viele kleine Federn im Querschnitt")
    xl, xr = xs - 30, xs + 30
    e.append(stab(x0, xl, r3, d))
    e.append(stab(xr, x1, r3, d))
    for dy in lagen:
        e.append(feder_h(xl, xr, r3 + dy, breite=6, windungen=4, vor=5, dicke=1.0))
    e.append(kraft(x0, r3, 180, "F", laenge=50, ziehend=True, label_seite=-1))
    e.append(kraft(x1, r3, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(hinweis(xs, r3 - 40, "viele kleine Federn", anker="middle"))

    e = abb.ebene("spannung", "Spannung am Schnittufer")
    e.append(stab(x0, xs, r4, d))
    e.append(kraft(x0, r4, 180, "F", laenge=50, ziehend=True, label_seite=-1))
    for dy in lagen:
        e.append(pfeil(xs, r4 + dy, xs + 34, r4 + dy, ROT, STRICH["normal"], (8, 5)))
    e.append(linie(xs + 34, r4 - 22, xs + 34, r4 + 22, ROT, STRICH["duenn"]))
    e.append(text(xs + 48, r4, "σ", ROT, 20, anker="start"))
    e.append(text(xs + 120, r4, "σ = N / A", SCHWARZ, 19, anker="start"))

    # Querschnitt von vorn: A und 2A mit „Federn“ als Punkten
    e = abb.ebene("querschnitt", "Querschnitt A und 2A")
    qx, qy, a = 640, 160, 84
    e.append(hinweis(qx, qy - 26, "Querschnitt von vorn"))
    e.append(rechteck(qx, qy, qx + a, qy + a))
    for i in range(4):
        for j in range(4):
            e.append(punkt(qx + a * (i + 0.5) / 4, qy + a * (j + 0.5) / 4, 2.6, ROT))
    e.append(text(qx + a + 14, qy + a / 2, "A", GRUEN, 18, anker="start"))
    e.append(text(qx + a + 14, qy + a / 2 + 26, "F", ROT, 18, anker="start"))
    e.append(text(qx + a + 50, qy + a / 2 + 13, "→  σ", ROT, 18, anker="start"))
    qy2 = qy + a + 40
    e.append(rechteck(qx, qy2, qx + 2 * a, qy2 + a))
    for i in range(8):
        for j in range(4):
            e.append(punkt(qx + 2 * a * (i + 0.5) / 8, qy2 + a * (j + 0.5) / 4, 2.6, ROT))
    e.append(text(qx + 2 * a + 14, qy2 + a / 2, "2A", GRUEN, 18, anker="start"))
    e.append(text(qx + 2 * a + 14, qy2 + a / 2 + 26, "F", ROT, 18, anker="start"))
    e.append(text(qx + 2 * a + 50, qy2 + a / 2 + 13, "→  σ / [2]", ROT, 18, anker="start"))
    return abb.speichern(ZIEL / "spannung.svg")


# =====================================================================
# Normal- und Schubspannung an einer schrägen Schnittfläche
# =====================================================================
def normal_schub():
    abb = Abbildung(860, 290, "Normal- und Schubspannung")
    y, h = 145, 110                             # Achse, Stabhöhe
    x0, xo, xu = 90, 380, 450                   # linkes Ende, Schnitt oben/unten
    yo, yu = y - h / 2, y + h / 2

    e = abb.ebene("schraeg", "Schräger Schnitt")
    e.append(polylinie([(x0, yo), (xo, yo), (xu, yu), (x0, yu)], SCHWARZ, STRICH["normal"], HELL, schliessen=True))
    e.append(kraft(x0, y, 180, "F", laenge=55, ziehend=True, label_seite=-1))
    e.append(linie(xo, yo, xu, yu, GRUEN, 1.6))

    e = abb.ebene("spannung-schraeg", "Spannung in Stabrichtung")
    for k in range(5):
        t = (k + 0.5) / 5
        px, py = xo + t * (xu - xo), yo + t * (yu - yo)
        e.append(pfeil(px, py, px + 40, py, ROT, STRICH["normal"], (8, 5)))

    e = abb.ebene("zerlegung", "Zerlegung in σ und τ")
    dx, dy = xu - xo, yu - yo
    L = math.hypot(dx, dy)
    tx, ty = dx / L, dy / L                     # längs der Fläche (nach unten rechts)
    nx, ny = ty, -tx                            # Normale nach außen (rechts oben)
    P = (640, 150)                              # Ausschnitt der Schnittfläche, rechts daneben
    s = 130                                     # Länge des Spannungsvektors (in +x)
    sn, st = s * nx, s * tx
    Pn = (P[0] + sn * nx, P[1] + sn * ny)
    Pt = (P[0] + st * tx, P[1] + st * ty)
    E = (P[0] + s, P[1])
    e.append(linie(P[0] - 85 * tx, P[1] - 85 * ty, P[0] + 160 * tx, P[1] + 160 * ty, GRUEN, 1.6))
    e.append(gestrichelt(*Pn, *E))
    e.append(gestrichelt(*Pt, *E))
    e.append(pfeil(*P, *E, ROT, STRICH["normal"], (9, 6)))
    e.append(pfeil(*P, *Pn, ROT, STRICH["dick"]))
    e.append(pfeil(*P, *Pt, ROT, STRICH["dick"]))
    e.append(text(Pn[0] + 8, Pn[1] - 6, "σ", ROT, 21, anker="start"))
    e.append(text(Pt[0] - 10, Pt[1] + 4, "τ", ROT, 21, anker="end"))
    e.append(punkt(*P, 3, SCHWARZ))
    e.append(hinweis(P[0] - 90, 275, "Ausschnitt der Schnittfläche", groesse=13))
    return abb.speichern(ZIEL / "normal-schub.svg")


# =====================================================================
# Abgesetzter Stab: N konstant, σ springt
# =====================================================================
def abgesetzter_stab():
    abb = Abbildung(820, 400, "Abgesetzter Stab")
    x0, xm, x1, y = 120, 380, 640, 70
    e = abb.ebene("system", "Abgesetzter Stab")
    e.append(stab(x0, xm, y, 20))
    e.append(stab(xm, x1, y, 40))
    e.append(kraft(x0, y, 180, "F", laenge=50, ziehend=True, label_seite=-1))
    e.append(kraft(x1, y, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(text((x0 + xm) / 2, y - 26, "A", GRUEN, 17))
    e.append(text((xm + x1) / 2, y - 36, "2A", GRUEN, 17))

    e = abb.ebene("verlauf-N", "Normalkraftverlauf")
    e.append(verlauf(x0, [(0, 1), (x1 - x0, 1)], 46, 200, x1 - x0, "N(x)",
                     werte=[((x1 - x0) / 2, 1, "F", "middle")]))

    e = abb.ebene("verlauf-sigma", "Spannungsverlauf")
    m = xm - x0
    e.append(verlauf(x0, [(0, 2), (m, 2), (m, 1), (x1 - x0, 1)], 36, 350, x1 - x0, "σ(x)",
                     werte=[(m / 2, 2, "F / A", "middle"), (m + (x1 - xm) / 2, 1, "F / 2A", "middle")]))
    return abb.speichern(ZIEL / "abgesetzter-stab.svg")


# =====================================================================
# Bohrung in einer breiten Platte: Spannungsspitze am Lochrand (Kirsch)
# =====================================================================
def kerbe():
    abb = Abbildung(760, 360, "Spannungsspitze an einer Bohrung")
    x0, x1, y0, y1 = 120, 640, 50, 310
    xc, yc, r = (x0 + x1) / 2, (y0 + y1) / 2, 30
    e = abb.ebene("platte", "Platte mit Bohrung")
    e.append(rechteck(x0, y0, x1, y1))
    e.append(kreis(xc, yc, r, SCHWARZ, "#ffffff"))
    for k in range(7):
        yy = y0 + (y1 - y0) * (k + 0.5) / 7
        e.append(pfeil(x1, yy, x1 + 36, yy, ROT, STRICH["normal"], (8, 5)))
        e.append(pfeil(x0, yy, x0 - 36, yy, ROT, STRICH["normal"], (8, 5)))
    e.append(text(x1 + 48, y0 + 14, "σ_0", ROT, 18, anker="start"))
    e.append(text(x0 - 48, y0 + 14, "σ_0", ROT, 18, anker="end"))

    e = abb.ebene("verteilung", "Spannungsverteilung im Lochquerschnitt")
    s0 = 34                                     # px je σ_0
    e.append(linie(xc, y0, xc, y1, GRUEN, STRICH["duenn"], strich="6 4"))
    for vz in (-1, 1):
        pts = []
        n = 60
        for k in range(n + 1):
            yy = r + (yc - y0 - r) * k / n
            q = r / yy
            sig = 1 + 0.5 * q ** 2 + 1.5 * q ** 4
            pts.append((xc + s0 * sig, yc + vz * yy))
        flaeche = [(xc, yc + vz * r)] + pts + [(xc, yc + vz * (yc - y0))]
        e.append(polylinie(flaeche, None, fuellung="#f4bcbc", schliessen=True))
        e.append(polylinie(pts, ROT, STRICH["dick"]))
        e.append(linie(xc + s0, yc + vz * r, xc + s0, yc + vz * (yc - y0), ROT, STRICH["duenn"], strich="4 3"))
    e.append(text(xc + 3 * s0 + 8, yc - r - 4, "σ_{max} ≈ [3] σ_0", ROT, 17, anker="start"))
    e.append(text(xc + s0 + 6, y0 + 16, "σ_0", ROT, 15, anker="start"))
    return abb.speichern(ZIEL / "kerbe.svg")


# =====================================================================
# Dehnung: Gummiband am Lineal
# =====================================================================
S_CM = 50                                       # px je cm
X_LINEAL = 70


def _lineal(e, y, bis=16):
    x0 = X_LINEAL
    e.append(rechteck(x0 - 14, y, x0 + bis * S_CM + 14, y + 34, "#f4f4f4", "#7a7a7a"))
    for k in range(2 * bis + 1):
        x = x0 + k * S_CM / 2
        lang = k % 2 == 0
        e.append(linie(x, y, x, y + (12 if lang else 7), SCHWARZ, STRICH["duenn"]))
        if lang:
            e.append(zahl(x, y + 23, k // 2, SCHWARZ, 12))
    e.append(zahl(x0 + bis * S_CM + 30, y + 23, "cm", SCHWARZ, 12, anker="start"))


def _band(e, y, stuecke, striche, beschriftung=None):
    """Gummiband aus Stücken [(von_cm, bis_cm, dicke_px)], Striche bei cm-Werten; Nagel am Anfang."""
    for a, b, d in stuecke:
        e.append(rechteck(X_LINEAL + a * S_CM, y - d / 2, X_LINEAL + b * S_CM, y + d / 2, "#e9dcc6", "#6b5a40",
                          STRICH["duenn"]))
    for k in range(1, len(stuecke)):
        xk = X_LINEAL + stuecke[k][0] * S_CM
        e.append(kreis(xk, y, 5, "#6b5a40", "#d8c5a3", STRICH["duenn"]))     # Knoten
    for xc in striche:
        e.append(linie(X_LINEAL + xc * S_CM, y - 11, X_LINEAL + xc * S_CM, y + 11, SCHWARZ, 1.6))
    e.append(kreis(X_LINEAL, y, 4.5, SCHWARZ, "#555555", 1.0))                # Nagel
    if beschriftung:
        e.append(hinweis(X_LINEAL - 14, y - 26, beschriftung))


def _wege(e, y_alt, y_neu, alt, neu, beschriften=()):
    """Jeder Strich wandert: schräge Verbindungslinie von der alten zur neuen Lage; für ausgewählte Striche
    die Verschiebung u als Pfeil (gestaffelt über dem gedehnten Band)."""
    for xa, xn in zip(alt, neu):
        e.append(gestrichelt(X_LINEAL + xa * S_CM, y_alt + 12, X_LINEAL + xn * S_CM, y_neu - 12))
    k = 0
    for xa, xn in zip(alt, neu):
        if any(abs(xa - b) < 1e-6 for b in beschriften):
            yy = y_neu - 20 - 16 * k
            e.append(linie(X_LINEAL + xa * S_CM, yy - 5, X_LINEAL + xa * S_CM, yy + 5, GRUEN, STRICH["duenn"]))
            e.append(pfeil(X_LINEAL + xa * S_CM, yy, X_LINEAL + xn * S_CM, yy, GRUEN, STRICH["normal"], (8, 5)))
            u = f"{xn - xa:g}".replace(".", ",")
            e.append(text(X_LINEAL + xn * S_CM + 6, yy, f"u = [{u} cm]", GRUEN, 13, anker="start"))
            k += 1


def _u_diagramm(e, y0, punkte, skala_u, bis=16, ticks=()):
    """u(x) über x (cm), Werteachse nach oben."""
    x0 = X_LINEAL
    e.append(pfeil(x0, y0, x0 + bis * S_CM + 20, y0, SCHWARZ, STRICH["normal"], (9, 6)))
    e.append(text(x0 + bis * S_CM + 26, y0, "x", SCHWARZ, 16, anker="start"))
    hoehe = max(u for _, u in punkte) * skala_u + 28
    e.append(pfeil(x0, y0, x0, y0 - hoehe, SCHWARZ, STRICH["normal"], (9, 6)))
    e.append(text(x0 - 10, y0 - hoehe + 6, "u(x)", SCHWARZ, 16, anker="end"))
    for u in ticks:
        yy = y0 - u * skala_u
        e.append(linie(x0 - 4, yy, x0 + 4, yy, SCHWARZ, STRICH["duenn"]))
        e.append(zahl(x0 - 8, yy, f"{u:g}".replace(".", ",") + " cm", SCHWARZ, 11, anker="end"))
    e.append(polylinie([(x0 + x * S_CM, y0 - u * skala_u) for x, u in punkte], BLAU, STRICH["dick"]))


def _steigung(e, y0, xa, xb, ua, ub, skala_u, label):
    pa = (X_LINEAL + xa * S_CM, y0 - ua * skala_u)
    pb = (X_LINEAL + xb * S_CM, y0 - ub * skala_u)
    e.append(polylinie([pa, (pb[0], pa[1]), pb], GRUEN, STRICH["normal"]))
    e.append(text(pb[0] + 8, (pa[1] + pb[1]) / 2, label, GRUEN, 15, anker="start"))


def gummiband():
    abb = Abbildung(950, 470, "Dehnung am Gummiband")
    y0, y1, yl, yd = 70, 170, 205, 430
    alt = [0, 2, 4, 6, 8, 10]
    neu = [1.5 * x for x in alt]

    e = abb.ebene("lineal", "Lineal")
    _lineal(e, yl)
    e = abb.ebene("band0", "Gummiband unbelastet")
    _band(e, y0, [(0, 10, 9)], alt, "unbelastet")
    e = abb.ebene("band1", "Gummiband gedehnt")
    _band(e, y1, [(0, 15, 7)], neu, "gedehnt")
    e.append(kraft(X_LINEAL + 15 * S_CM, y1, 0, "F", laenge=45, ziehend=True, label_seite=1))
    e = abb.ebene("wege", "Verschiebungen der Striche")
    _wege(e, y0, y1, alt, neu, beschriften=(4, 10))

    e = abb.ebene("stuecke", "Gleiche Dehnung jedes Stücks")
    for (a, b), farbe in (((4, 6), BLAU), ((8, 10), BLAU)):
        e.append(rechteck(X_LINEAL + a * S_CM, y0 - 7, X_LINEAL + b * S_CM, y0 + 7, "none", farbe, 2.4))
        e.append(rechteck(X_LINEAL + 1.5 * a * S_CM, y1 - 6, X_LINEAL + 1.5 * b * S_CM, y1 + 6, "none", farbe, 2.4))
        e.append(zahl(X_LINEAL + (a + b) / 2 * S_CM, y0 + 22, "2 cm", farbe, 13))
        e.append(zahl(X_LINEAL + 1.5 * (a + b) / 2 * S_CM, y1 + 22, "3 cm", farbe, 13))

    e = abb.ebene("u-gerade", "Verschiebung u(x)")
    sk = 26
    _u_diagramm(e, yd, [(0, 0), (10, 5)], sk, ticks=(5,))
    _steigung(e, yd, 4, 8, 2, 4, sk, "ε = [0,5]")
    return abb.speichern(ZIEL / "gummiband.svg")


def gummiband_knoten():
    abb = Abbildung(950, 470, "Dünnes und dickes Gummiband verknotet")
    y0, y1, yl, yd = 70, 170, 205, 430
    alt = list(range(11))
    neu = [1.4 * x if x <= 5 else 7 + 1.2 * (x - 5) for x in alt]

    e = abb.ebene("lineal", "Lineal")
    _lineal(e, yl)
    e = abb.ebene("band0", "Unbelastet")
    _band(e, y0, [(0, 5, 5), (5, 10, 12)], alt, "dünn und dick, unbelastet")
    e = abb.ebene("band1", "Gedehnt")
    _band(e, y1, [(0, 7, 4), (7, 13, 11)], neu, "gedehnt")
    e.append(kraft(X_LINEAL + 13 * S_CM, y1, 0, "F", laenge=45, ziehend=True, label_seite=1))
    e = abb.ebene("wege", "Verschiebungen")
    _wege(e, y0, y1, alt, neu, beschriften=(5, 10))

    e = abb.ebene("u-knick", "Verschiebung u(x) mit Knick")
    sk = 40
    _u_diagramm(e, yd, [(0, 0), (5, 2), (10, 3)], sk, ticks=(2, 3))
    _steigung(e, yd, 1, 4, 0.4, 1.6, sk, "ε = [0,4]")
    _steigung(e, yd, 6, 9, 2.2, 2.8, sk, "ε = [0,2]")
    return abb.speichern(ZIEL / "gummiband-knoten.svg")


# =====================================================================
# Stoffgesetz: von der Feder zum σ-ε-Diagramm, Werkstoffe, nichtlinearer Bereich
# =====================================================================
def stoffgesetz():
    from grafiken_grundlagen import koord_xy
    abb = Abbildung(900, 470, "Stoffgesetz")
    D = (330, 420)

    def P(eps, sig):
        return D[0] + eps, D[1] - sig

    # links: Feder
    xf, y0 = 130, 50
    e = abb.ebene("feder", "Feder")
    e.append(_decke(xf, y0, 70))
    e.append(feder(xf, y0, 250, breite=22, windungen=8))
    e.append(rechteck(xf - 26, 250, xf + 26, 262, "#cfcfcf"))
    e.append(kraft(xf, 262, -90, "F", laenge=55, ziehend=True, label_seite=-1))
    e.append(gestrichelt(xf - 40, 210, xf + 50, 210))
    e.append(mass(xf + 40, 210, xf + 40, 250, "u", abstand=-12, hilfslinien=False))
    e.append(text(xf - 26, 140, "c", GRUEN, 18, anker="end"))

    # links: Zugprobe
    xp, kopf, schaft = 130, 34, 15
    e = abb.ebene("probe", "Zugprobe")
    umriss = [(xp - kopf, 40), (xp + kopf, 40), (xp + kopf, 95), (xp + schaft, 125), (xp + schaft, 335),
              (xp + kopf, 365), (xp + kopf, 420), (xp - kopf, 420), (xp - kopf, 365), (xp - schaft, 335),
              (xp - schaft, 125), (xp - kopf, 95)]
    e.append(polylinie(umriss, SCHWARZ, STRICH["normal"], HELL, schliessen=True))
    for ym in (160, 300):
        e.append(linie(xp - schaft - 5, ym, xp + schaft + 5, ym, SCHWARZ, 1.6))
    e.append(mass(xp - schaft, 160, xp - schaft, 300, "l_0", abstand=-26))
    e.append(text(xp + schaft + 10, 230, "A_0", GRUEN, 16, anker="start"))
    e.append(kraft(xp, 40, 90, "F", laenge=30, ziehend=True, label_seite=-1))
    e.append(kraft(xp, 420, -90, "F", laenge=30, ziehend=True, label_seite=-1))

    # F-u-Diagramm
    e = abb.ebene("achsen-fu", "Achsen F, u")
    e.append(koord_xy(*D, 540, 360, xlabel="u", ylabel="F"))
    e = abb.ebene("linie-fu", "Federkennlinie")
    e.append(linie(*D, *P(260, 300), ROT, 2.6))
    e.append(polylinie([P(110, 127), P(190, 127), P(190, 219)], GRUEN, STRICH["normal"]))
    e.append(text(D[0] + 198, D[1] - 172, "c", GRUEN, 18, anker="start"))
    e.append(text(D[0] + 280, D[1] - 300, "F = c u", ROT, 20, anker="start"))

    # σ-ε-Diagramm
    e = abb.ebene("achsen-se", "Achsen σ, ε")
    e.append(koord_xy(*D, 540, 360, xlabel="ε", ylabel="σ"))
    e = abb.ebene("linie-se", "Hookesche Gerade")
    e.append(linie(*D, *P(260, 300), ROT, 2.6))
    e.append(polylinie([P(110, 127), P(190, 127), P(190, 219)], GRUEN, STRICH["normal"]))
    e.append(text(D[0] + 198, D[1] - 172, "E", GRUEN, 18, anker="start"))
    e.append(text(D[0] + 280, D[1] - 300, "σ = E ε", ROT, 20, anker="start"))

    # Werkstoffe: nur der lineare Bereich (schematisch)
    lin = {"Stahl": (46, 230), "Aluminium": (83, 150), "Kunststoff": (111, 50)}
    e = abb.ebene("materialien", "Lineare Bereiche verschiedener Werkstoffe")
    for name, (ee, ss) in lin.items():
        e.append(linie(*D, *P(ee, ss), ROT, 2.6))
        e.append(punkt(*P(ee, ss), 3.2, ROT))
    e.append(text(D[0] + 36, D[1] - 246, "[Stahl]", SCHWARZ, 15, anker="end", italic=False))
    e.append(text(D[0] + 90, D[1] - 140, "[Aluminium]", SCHWARZ, 15, anker="start", italic=False))
    e.append(text(D[0] + 118, D[1] - 50, "[Kunststoff]", SCHWARZ, 15, anker="start", italic=False))
    e.append(hinweis(D[0] + 540, D[1] - 360, "schematisch, nicht maßstäblich", anker="end", groesse=13))

    # nichtlineare Bereiche
    e = abb.ebene("nichtlinear", "Nichtlineare Bereiche")
    st = [P(46, 230), P(52, 216), P(60, 226), P(68, 218), P(76, 224), P(120, 222)]
    st += [P(120 + 210 * t, 222 + 108 * math.sin(math.pi / 2 * t) ** 0.8) for t in [i / 25 for i in range(1, 26)]]
    st += [P(330 + 90 * t, 330 - 40 * t ** 1.8) for t in [i / 15 for i in range(1, 16)]]
    al = [P(83 + (370 - 83) * t, 150 + 105 * (1 - math.exp(-4 * t)) - 12 * t ** 4) for t in [i / 40 for i in range(41)]]
    ku = [P(111 + 140 * t, 50 + 24 * math.sin(math.pi / 2 * t)) for t in [i / 20 for i in range(21)]]
    ku += [P(251 + 270 * t, 74 - 10 * t) for t in [i / 10 for i in range(1, 11)]]
    for kurve in (st, al, ku):
        e.append(polylinie(kurve, SCHWARZ, 1.8))
        xe, ye = kurve[-1]
        e.append(linie(xe - 5, ye - 5, xe + 5, ye + 5, SCHWARZ, 1.4))
        e.append(linie(xe - 5, ye + 5, xe + 5, ye - 5, SCHWARZ, 1.4))
    e.append(text(D[0] + 300, D[1] - 345, "R_m", SCHWARZ, 16))
    e.append(hinweis(D[0] + 70, D[1] - 246, "Fließen", groesse=13))
    return abb.speichern(ZIEL / "stoffgesetz.svg")


# =====================================================================
# Weitere Kennwerte: Querkontraktion, Schub, Wärmedehnung
# =====================================================================
def weitere_kennwerte():
    abb = Abbildung(640, 300, "Querkontraktion und Schub")

    e = abb.ebene("quer", "Querkontraktion")
    x0, y, l0, b0 = 50, 150, 190, 70
    l, b = 225, 52
    e.append(hinweis(x0, 40, "Querkontraktion"))
    e.append(rechteck(x0, y - b0 / 2, x0 + l0, y + b0 / 2, "none", GRAU, STRICH["duenn"], strich="5 4"))
    e.append(rechteck(x0, y - b / 2, x0 + l, y + b / 2))
    e.append(kraft(x0, y, 180, "F", laenge=36, ziehend=True, label_seite=-1, label_pos=1.2))
    e.append(kraft(x0 + l, y, 0, "F", laenge=36, ziehend=True, label_seite=1, label_pos=1.2))
    e.append(mass(x0, y + b0 / 2, x0 + l0, y + b0 / 2, "l_0", abstand=-26))
    e.append(mass(x0, y + b / 2, x0 + l, y + b / 2, "l", abstand=-62, hilfslinien=False))
    e.append(text(x0 + l0 - 12, y - b0 / 2 - 14, "b_0", GRAU, 15))
    e.append(text(x0 + l / 2 - 30, y, "b", GRUEN, 16))

    e = abb.ebene("schub", "Schubverformung")
    xs, ys, a, v = 410, 230, 120, 30
    e.append(hinweis(xs - 20, 40, "Schub"))
    e.append(linie(xs - 20, ys, xs + a + 50, ys, SCHWARZ, STRICH["normal"]))
    xx = xs - 18
    while xx < xs + a + 50:
        e.append(linie(xx, ys, xx - 7, ys + 7, SCHWARZ, STRICH["duenn"]))
        xx += 6
    e.append(rechteck(xs, ys - a, xs + a, ys, "none", GRAU, STRICH["duenn"], strich="5 4"))
    e.append(polylinie([(xs, ys), (xs + a, ys), (xs + a + v, ys - a), (xs + v, ys - a)], SCHWARZ,
                       STRICH["normal"], HELL, schliessen=True))
    e.append(pfeil(xs + v + 10, ys - a - 14, xs + v + a - 10, ys - a - 14, ROT, STRICH["dick"]))
    e.append(text(xs + v + a / 2, ys - a - 32, "τ", ROT, 19))
    gam = math.degrees(math.atan2(v, a))
    e.append(winkelbogen(xs, ys, 70, 90 - gam, 90, "γ"))
    e.append(linie(xs, ys, xs, ys - a, GRAU, STRICH["duenn"], strich="5 4"))

    return abb.speichern(ZIEL / "weitere-kennwerte.svg")


# =====================================================================
# Wärmedehnung: Stab wird ohne Kraft länger bzw. kürzer
# =====================================================================
def waermedehnung():
    abb = Abbildung(560, 330, "Wärmedehnung")
    xw, lw, dl = 80, 300, 42
    e = abb.ebene("stab", "Stab bei Ausgangstemperatur")
    for y in (90, 230):
        e.append(einspannung(xw, y, 50, "links"))
    e.append(rechteck(xw, 78, xw + lw, 102))
    e.append(text(xw + lw / 2, 90, "T_0", SCHWARZ, 17))
    e.append(mass(xw, 102, xw + lw, 102, "l", abstand=-26))
    e = abb.ebene("warm", "Erwärmt")
    e.append(rechteck(xw, 218, xw + lw, 242, "none", GRAU, STRICH["duenn"], strich="5 4"))
    e.append(rechteck(xw, 218, xw + lw + dl, 242, "#f6d9c8"))
    e.append(text(xw + lw / 2, 230, "[Δ]T > [0]", SCHWARZ, 17))
    e.append(mass(xw + lw, 218, xw + lw + dl, 218, "[Δ]l_T", abstand=18, aussen=True))
    e.append(hinweis(xw, 290, "länger, aber ohne Kraft: spannungsfrei", groesse=14))
    e = abb.ebene("kalt", "Abgekühlt")
    e.append(rechteck(xw, 218, xw + lw - dl, 242, "#d6e2f3"))
    e.append(rechteck(xw, 218, xw + lw, 242, "none", GRAU, STRICH["duenn"], strich="5 4"))
    e.append(text(xw + (lw - dl) / 2, 230, "[Δ]T < [0]", SCHWARZ, 17))
    e.append(mass(xw + lw - dl, 218, xw + lw, 218, "[Δ]l_T", abstand=18, aussen=True))
    e.append(hinweis(xw, 290, "kürzer, ebenfalls spannungsfrei", groesse=14))
    return abb.speichern(ZIEL / "waermedehnung.svg")


# =====================================================================
# Beispiel Kupferkabel (nach Götz 2.2.1)
# =====================================================================
def kupferkabel():
    abb = Abbildung(800, 450, "Beispiel Kupferkabel")
    xk, yd, yk = 150, 50, 290
    e = abb.ebene("system", "Kabel mit Masse")
    e.append(_decke(xk, yd, 60))
    e.append(linie(xk, yd, xk, yk, "#b06a2c", 3.2))
    e.append(rechteck(xk - 32, yk, xk + 32, yk + 52, "#cfcfcf"))
    e.append(text(xk, yk + 26, "m", SCHWARZ, 19))
    e.append(mass(xk, yd, xk, yk, "l", abstand=36))
    e.append(text(xk - 10, (yd + yk) / 2, "E, A, α_T", GRUEN, 15, anker="end"))
    e.append(kraft(xk + 70, yk - 30, -90, "g", laenge=46, ziehend=True, label_seite=-1))

    e = abb.ebene("fkb", "Freikörperbild")
    xf = 310
    e.append(linie(xf, yk - 50, xf, yk, "#b06a2c", 3.2))
    e.append(schnitt(xf - 13, yk - 50, xf + 13, yk - 50))
    e.append(rechteck(xf - 32, yk, xf + 32, yk + 52, "#cfcfcf"))
    e.append(kraft(xf, yk - 58, 90, "N", laenge=50, ziehend=True, label_seite=1))
    e.append(kraft(xf, yk + 52, -90, "F_G", laenge=50, ziehend=True, label_seite=1))

    # Lage der Masse, stark vergrößert (1 mm = 300 px)
    xs, ys, sk = 520, 60, 300
    def Y(mm):
        return ys + mm * sk
    e = abb.ebene("skala", "Absenkung unter Last")
    e.append(hinweis(xs - 40, ys - 30, "Absenkung der Masse (vergrößert)"))
    e.append(pfeil(xs, ys, xs, Y(1.05), SCHWARZ, STRICH["normal"], (9, 6)))
    for k in range(11):
        e.append(linie(xs - 5, Y(k / 10), xs + 5, Y(k / 10), SCHWARZ, STRICH["duenn"]))
        if k % 2 == 0:
            e.append(zahl(xs - 10, Y(k / 10), f"{k / 10:.1f}".replace(".", ","), SCHWARZ, 12, anker="end"))
    e.append(zahl(xs - 10, Y(1.05) + 14, "mm", SCHWARZ, 12, anker="end"))

    def marke(e, mm, farbe, beschriftung):
        e.append(punkt(xs, Y(mm), 4.5, farbe))
        e.append(linie(xs, Y(mm), xs + 30, Y(mm), farbe, STRICH["normal"]))
        e.append(zahl(xs + 36, Y(mm), beschriftung, farbe, 13, anker="start"))

    marke(e, 0, SCHWARZ, "0   ohne Last")
    marke(e, 0.481, ROT, "0,481 mm   mit Last, 20 °C")
    e = abb.ebene("skala-warm", "Erwärmt auf 65 °C")
    marke(e, 0.863, ROT, "0,863 mm   65 °C")
    e = abb.ebene("skala-kalt", "Abgekühlt auf −10 °C")
    marke(e, 0.226, BLAU, "0,226 mm   −10 °C")
    return abb.speichern(ZIEL / "kupferkabel.svg")


# =====================================================================
# Zusammenfassung: sechs Kacheln
# =====================================================================
def zusammenfassung():
    W, H, rand = 300, 220, 15
    abb = Abbildung(3 * W + 4 * rand, 2 * H + 3 * rand, "Zusammenfassung: Spannung, Dehnung, Stoffgesetz")

    def kachel(e, spalte, zeile, titel, formel):
        x, y = rand + spalte * (W + rand), rand + zeile * (H + rand)
        e.append(polylinie([(x, y), (x + W, y), (x + W, y + H), (x, y + H)], "#c8c8c8", 1.2, "#fafafa",
                           schliessen=True))
        e.append(text(x + 14, y + 22, f"[{titel}]", SCHWARZ, 17, anker="start", italic=False))
        zeilen = formel if isinstance(formel, (list, tuple)) else [formel]
        for k, z in enumerate(reversed(zeilen)):
            e.append(text(x + W / 2, y + H - 20 - 24 * k, z, ROT, 17))
        return x, y

    e = abb.ebene("k-feder", "Feder")
    x, y = kachel(e, 0, 0, "Stab = Feder", "F = c u,   c = EA / l")
    yy = y + 90
    e.append(einspannung(x + 40, yy, 40, "links"))
    e.append(feder_h(x + 40, x + 170, yy, breite=14, windungen=5))
    e.append(endplatte(x + 170, yy, 28))
    e.append(kraft(x + 177, yy, 0, "F", laenge=40, ziehend=True, label_seite=1))

    e = abb.ebene("k-spannung", "Spannung")
    x, y = kachel(e, 1, 0, "Spannung", "σ = N / A")
    yy = y + 90
    e.append(stab(x + 60, x + 150, yy, 40))
    e.append(kraft(x + 60, yy, 180, "", laenge=34, ziehend=True))
    for dy in (-15, -7.5, 0, 7.5, 15):
        e.append(pfeil(x + 150, yy + dy, x + 180, yy + dy, ROT, STRICH["normal"], (7, 5)))
    e.append(text(x + 196, yy, "σ", ROT, 19, anker="start"))

    e = abb.ebene("k-dehnung", "Dehnung")
    x, y = kachel(e, 2, 0, "Dehnung", ["ε = [Δ]l / l", "[allgemein]  ε = [d]u / [d]x"])
    for (yy, laenge, n) in ((y + 60, 150, 5), (y + 100, 225, 5)):
        e.append(rechteck(x + 30, yy - 4, x + 30 + laenge, yy + 4, "#e9dcc6", "#6b5a40", STRICH["duenn"]))
        for k in range(n + 1):
            xk = x + 30 + laenge * k / n
            e.append(linie(xk, yy - 9, xk, yy + 9, SCHWARZ, 1.4))

    e = abb.ebene("k-hooke", "Hooke")
    x, y = kachel(e, 0, 1, "Stoffgesetz (Hooke)", "σ = E ε")
    D = (x + 60, y + 160)
    e.append(koord_xy(*D, 190, 120, xlabel="ε", ylabel="σ"))
    e.append(linie(*D, D[0] + 120, D[1] - 100, ROT, 2.2))
    e.append(polylinie([(D[0] + 50, D[1] - 41.7), (D[0] + 90, D[1] - 41.7), (D[0] + 90, D[1] - 75)], GRUEN,
                       STRICH["normal"]))
    e.append(text(D[0] + 98, D[1] - 58, "E", GRUEN, 16, anker="start"))

    e = abb.ebene("k-weitere", "Weitere Kennwerte")
    x, y = kachel(e, 1, 1, "Weitere Kennwerte", ["ε_q = −ν ε,   τ = G γ", "ε_T = α_T [Δ]T"])
    e.append(rechteck(x + 50, y + 55, x + 230, y + 105, "none", GRAU, STRICH["duenn"], strich="5 4"))
    e.append(rechteck(x + 50, y + 62, x + 250, y + 98))

    e = abb.ebene("k-laenge", "Längenänderung")
    x, y = kachel(e, 2, 1, "Längenänderung", ["[Δ]l = N l / (E A) + α_T [Δ]T l"])
    e.append(einspannung(x + 40, y + 85, 40, "links"))
    e.append(rechteck(x + 40, y + 75, x + 200, y + 95, "none", GRAU, STRICH["duenn"], strich="5 4"))
    e.append(rechteck(x + 40, y + 75, x + 225, y + 95))
    e.append(kraft(x + 225, y + 85, 0, "", laenge=34, ziehend=True))
    e.append(mass(x + 200, y + 95, x + 225, y + 95, "[Δ]l", abstand=-24, aussen=True))
    return abb.speichern(ZIEL / "zusammenfassung.svg")


# =====================================================================
# Seminaraufgaben
# =====================================================================
def _aufgabe(name, breite, hoehe):
    abb = Abbildung(breite, hoehe, name)
    return abb, abb.ebene("system", "System")


def stab_gelenkig(x1, y1, x2, y2, dicke=5):
    """Pendelstab bzw. Seil: schmaler Stab mit Gelenken an beiden Enden."""
    return gruppe([balken(x1, y1, x2, y2, dicke=dicke), kreis(x1, y1, 3.6), kreis(x2, y2, 3.6)])


# 5.1  Zugversuch: Probe mit Messlänge und Durchmesser (Götz 2.1.1)
def aufgabe_5_1():
    abb, e = _aufgabe("Aufgabe 5.1", 600, 180)
    x0, x1, y, d = 90, 510, 85, 40
    e.append(stab(x0, x1, y, d))
    for xm in (150, 450):
        e.append(linie(xm, y - d / 2 - 5, xm, y + d / 2 + 5, SCHWARZ, 1.6))
    e.append(kraft(x0, y, 180, "F", laenge=50, ziehend=True, label_seite=-1))
    e.append(kraft(x1, y, 0, "F", laenge=50, ziehend=True, label_seite=1))
    e.append(mass(150, y - d / 2, 450, y - d / 2, "l_0", abstand=24))
    e.append(mass(300, y - d / 2, 300, y + d / 2, "d_0", abstand=-44, hilfslinien=False))
    return abb.speichern(ZIEL / "aufgabe-5-1.svg")


# 5.2  Körper an zwei schrägen Stäben (Götz 2.2.2)
def aufgabe_5_2():
    from grafiken_grundlagen import deckenlager
    abb, e = _aufgabe("Aufgabe 5.2", 520, 375)
    yd, a = 60, 180
    w = a / math.tan(math.radians(60))
    xm = 260
    K = (xm, yd + a)
    for sx in (-1, 1):
        e.append(stab_gelenkig(xm + sx * w, yd, *K))
        e.append(deckenlager(xm + sx * w, yd))
    e.append(linie(xm - w - 50, yd, xm + w + 50, yd, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(winkelbogen(xm - w, yd, 34, -60, 0, "α"))
    e.append(winkelbogen(xm + w, yd, 34, 180, 240, "α"))
    e.append(rechteck(K[0] - 26, K[1] + 14, K[0] + 26, K[1] + 54, "#cfcfcf"))
    e.append(linie(K[0], K[1], K[0], K[1] + 14, SCHWARZ, 1.4))
    e.append(kraft(K[0], K[1] + 54, -90, "F_G", laenge=46, ziehend=True, label_seite=-1))
    e.append(mass(xm + w, yd, xm + w, K[1], "a", abstand=50))
    e.append(text(xm - w / 2 - 18, yd + a / 2, "d", GRUEN, 17, anker="end"))
    return abb.speichern(ZIEL / "aufgabe-5-2.svg")


# 5.3  Abgesetzte Welle mit zwei Zugkräften
def aufgabe_5_3():
    abb, e = _aufgabe("Aufgabe 5.3", 640, 230)
    x0, xm, x1, y = 70, 340, 520, 95
    h1, h2 = 60, 36
    e.append(einspannung(x0, y, 90, "links"))
    e.append(stab(x0, xm, y, h1))
    e.append(stab(xm, x1, y, h2))
    for sy in (-1, 1):
        e.append(pfeil(xm + 2, y + sy * (h2 / 2 + 6), xm + 48, y + sy * (h2 / 2 + 6), ROT, STRICH["dick"]))
    e.append(text(xm + 54, y - h2 / 2 - 14, "F_1", ROT, anker="start"))
    e.append(kraft(x1, y, 0, "F_2", laenge=50, ziehend=True, label_seite=1))
    e.append(mass(x0, y + h1 / 2, xm, y + h1 / 2, "l_1", abstand=-34))
    e.append(mass(xm, y + h1 / 2, x1, y + h1 / 2, "l_2", abstand=-34))
    e.append(text((x0 + xm) / 2, y, "d_1", GRUEN, 17))
    e.append(text((xm + x1) / 2 + 30, y, "d_2", GRUEN, 17))
    return abb.speichern(ZIEL / "aufgabe-5-3.svg")


# 5.4  Starrer Balken am Festlager, von einer Pendelstütze waagerecht gehalten
def aufgabe_5_4():
    abb, e = _aufgabe("Aufgabe 5.4", 560, 460)
    xA, xF, xB, y, yb = 80, 380, 480, 140, 380
    e.append(balken(xA, y, xB, y, dicke=10))
    e.append(festlager(xA, y + 5, label="A", label_pos=(-22, 8)))
    e.append(stab_gelenkig(xB, y + 5, xB, yb))
    e.append(festlager(xB, yb, label="C", label_pos=(24, 8)))
    e.append(text(xB - 4, y - 22, "B", GRUEN, anker="middle"))
    e.append(kraft(xF, y - 5, -90, "F", laenge=50, label_seite=1))
    e.append(mass(xA, y, xF, y, "a", abstand=58))
    e.append(mass(xA, y, xB, y, "l", abstand=86))
    e.append(mass(xB, y + 5, xB, yb, "h", abstand=-40))
    e.append(text(xB - 14, (y + yb) / 2, "d", GRUEN, 17, anker="end"))
    e.append(hinweis(xA + 60, y + 30, "starr"))
    return abb.speichern(ZIEL / "aufgabe-5-4.svg")


# 5.5  Starrer Balken an zwei unterschiedlich langen Seilen, ohne Führung
def aufgabe_5_5():
    abb, e = _aufgabe("Aufgabe 5.5", 560, 450)
    x1, x2, y1d, y2d, yb = 130, 430, 45, 195, 345
    e.append(_decke(x1, y1d, 80))
    e.append(_decke(x2, y2d, 80))
    e.append(stab_gelenkig(x1, y1d, x1, yb - 6, dicke=3))
    e.append(stab_gelenkig(x2, y2d, x2, yb - 6, dicke=3))
    e.append(rechteck(x1 - 20, yb - 6, x2 + 20, yb + 14, HELL))
    e.append(kraft((x1 + x2) / 2, yb - 6, -90, "F", laenge=50, label_seite=1))
    e.append(mass(x1, y1d, x1, yb - 6, "L_1", abstand=-40))
    e.append(mass(x2, y2d, x2, yb - 6, "L_2", abstand=40))
    e.append(text(x1 + 12, (y1d + yb) / 2 - 40, "[Seil 1]", SCHWARZ, 15, anker="start", italic=False))
    e.append(text(x1 + 12, (y1d + yb) / 2 - 14, "A_1", GRUEN, 16, anker="start"))
    e.append(text(x2 - 12, (y2d + yb) / 2 - 14, "[Seil 2]", SCHWARZ, 15, anker="end", italic=False))
    e.append(text(x2 - 12, (y2d + yb) / 2 + 12, "A_2", GRUEN, 16, anker="end"))
    e.append(mass(x1, yb + 14, (x1 + x2) / 2, yb + 14, "b/2", abstand=-30))
    e.append(mass((x1 + x2) / 2, yb + 14, x2, yb + 14, "b/2", abstand=-30))
    e.append(hinweis((x1 + x2) / 2 + 30, yb + 4, "starr", groesse=13))
    return abb.speichern(ZIEL / "aufgabe-5-5.svg")


if __name__ == "__main__":
    for fn in (einordnung, beanspruchungsarten, feder_modell, spannung, normal_schub, abgesetzter_stab, kerbe, gummiband, gummiband_knoten,
               stoffgesetz, weitere_kennwerte, waermedehnung, kupferkabel, zusammenfassung,
               aufgabe_5_1, aufgabe_5_2, aufgabe_5_3, aufgabe_5_4, aufgabe_5_5):
        print(fn())

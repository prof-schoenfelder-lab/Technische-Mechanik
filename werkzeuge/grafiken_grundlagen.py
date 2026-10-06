"""Grafiken zum Kapitel Grundlagen (Woche 1): Kraft, Moment, Axiome, Kraftsysteme, Gleichgewicht.

Aufruf:  python werkzeuge/grafiken_grundlagen.py
Ergebnis: grafiken/grundlagen/*.svg (Inkscape-Ebenen = Scroll-Schritte)

In diesem Kapitel gilt wie in der Vorlesung 2013 und bei Götz: x nach rechts, y nach oben.
Hilfsfunktion P(...) rechnet Modellkoordinaten in SVG-Pixel um.
"""

import math
from pathlib import Path

from tmzeichnen import (FARBE, STRICH, Abbildung, _spitze, balken, festlager, gruppe, kraft, kreis, linie,
                        mass, moment, pfeil, polylinie, text, winkelbogen)

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "grundlagen"
ROT, GRUEN, GRAU = FARBE["last"], FARBE["mass"], FARBE["hinweis"]
HELL = "#e6e6e6"


# ---------------------------------------------------------------- Hilfen
def abbild(ox, oy, s):
    """Modellkoordinaten (x nach rechts, y nach oben) → SVG-Pixel."""
    return lambda x, y: (ox + s * x, oy - s * y)


def koord_xy(x, y, lx=60, ly=60, xlabel="x", ylabel="y", farbe=None, negativ=0, negativ_y=None):
    """Koordinatensystem x nach rechts, y nach oben; negativ: Achsen auch in die Gegenrichtung (px)."""
    farbe = farbe or FARBE["koord"]
    negativ_y = negativ if negativ_y is None else negativ_y
    return gruppe([pfeil(x - negativ, y, x + lx, y, farbe, STRICH["normal"], (8, 5)),
                   text(x + lx + 4, y + 11, xlabel, farbe, anker="start"),
                   pfeil(x, y + negativ_y, x, y - ly, farbe, STRICH["normal"], (8, 5)),
                   text(x + 8, y - ly - 2, ylabel, farbe, anker="start")])


def vektor(x1, y1, x2, y2, label="", farbe=ROT, breite=STRICH["dick"], gestrichelt=False,
           lx=0, ly=0, anker="middle", groesse=None):
    """Pfeil von (x1,y1) nach (x2,y2), optional gestrichelt (Komponenten), Label an der Pfeilmitte + (lx, ly)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    hl, hw = (10, 7) if gestrichelt else (12, 8)
    teile = [linie(x1, y1, x2 - ux * hl * 0.8, y2 - uy * hl * 0.8, farbe, breite,
                   strich="6 4" if gestrichelt else None),
             _spitze(x2, y2, ux, uy, farbe, hl, hw)]
    if label:
        kw = {"groesse": groesse} if groesse else {}
        teile.append(text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, farbe, anker=anker, **kw))
    return gruppe(teile)


def strichpunkt(x1, y1, x2, y2, farbe=GRAU, breite=0.9):
    """Wirkungslinie (Strich-Punkt)."""
    return linie(x1, y1, x2, y2, farbe, breite, strich="14 4 2 4")


def platte(punkte, fuellung=HELL):
    return polylinie(punkte, FARBE["linie"], STRICH["normal"], fuellung, schliessen=True)


def kasten(x, y, b, h, zeilen, fuellung="#f2f2f2", farbe="#000000", fett=False):
    teile = [polylinie([(x - b / 2, y - h / 2), (x + b / 2, y - h / 2), (x + b / 2, y + h / 2), (x - b / 2, y + h / 2)],
                       "#444444", STRICH["normal"], fuellung, schliessen=True)]
    n = len(zeilen)
    for i, z in enumerate(zeilen):
        gr = 17 if i == 0 else 13
        teile.append(text(x, y + (i - (n - 1) / 2) * 19, f"[{z}]", farbe if i == 0 else "#444444", gr,
                          italic=False, halo=False))
    return gruppe(teile)


def rechter_winkel(x, y, ux, uy, vx, vy, a=9, farbe=GRAU):
    """Kennzeichnung eines rechten Winkels im Punkt (x,y) zwischen den Richtungen u und v (Einheitsvektoren, SVG)."""
    return polylinie([(x + ux * a, y + uy * a), (x + (ux + vx) * a, y + (uy + vy) * a), (x + vx * a, y + vy * a)],
                     farbe, STRICH["duenn"])


def punkt(x, y, r=3.2, farbe="#000000"):
    return kreis(x, y, r, farbe, farbe, 0.8)


def hinweis(x, y, s, anker="start", groesse=14):
    return text(x, y, f"[{s}]", "#444444", groesse, anker=anker, italic=False)


# =====================================================================
# Einordnung: Mechanik → Dynamik / Statik → Stereostatik / Elastostatik
# =====================================================================
def einordnung():
    abb = Abbildung(770, 330, "Einordnung der Technischen Mechanik")
    e = abb.ebene("baum", "Gliederung der Mechanik")
    knoten = {"mech": (360, 45), "dyn": (150, 145), "stat": (520, 145), "stereo": (400, 255), "elasto": (650, 255)}
    for a, b in (("mech", "dyn"), ("mech", "stat"), ("stat", "stereo"), ("stat", "elasto")):
        (x1, y1), (x2, y2) = knoten[a], knoten[b]
        e.append(linie(x1, y1 + 24, x2, y2 - 24, "#444444", STRICH["normal"]))
    e.append(kasten(*knoten["mech"], 200, 46, ["Technische Mechanik", "Kräfte und ihre Wirkungen"]))
    e.append(kasten(*knoten["dyn"], 200, 46, ["Dynamik", "Körper in Bewegung"]))
    e.append(kasten(*knoten["stat"], 220, 46, ["Statik", "Körper in Ruhe"]))
    e.append(kasten(*knoten["stereo"], 180, 46, ["Stereostatik", "starre Körper"]))
    e.append(kasten(*knoten["elasto"], 170, 46, ["Elastostatik", "verformbare Körper"]))

    e = abb.ebene("inhalt", "Inhalt dieser Lehrveranstaltung")
    e.append(polylinie([(300, 110), (755, 110), (755, 318), (300, 318)], ROT, 1.4, schliessen=True, strich="7 4"))
    e.append(text(750, 98, "[Inhalt dieser Lehrveranstaltung]", ROT, 14, anker="end", italic=False))
    e.append(text(400, 296, "[Wochen 1–4]", ROT, 13, italic=False))
    e.append(text(650, 296, "[Wochen 5–14 (Festigkeitslehre)]", ROT, 13, italic=False))
    return abb.speichern(ZIEL / "einordnung.svg")


# =====================================================================
# Kraft als Vektor: Angriffspunkt, Wirkungslinie, Richtungssinn, Komponenten
# =====================================================================
def kraft_vektor():
    abb = Abbildung(560, 360, "Die Kraft als gebundener Vektor")
    O = (110, 290)
    P = abbild(*O, 1)
    a = math.radians(35)
    L = 230
    E = P(L * math.cos(a), L * math.sin(a))

    e = abb.ebene("koordinaten", "Koordinatensystem")
    e.append(koord_xy(*O, 300, 230, negativ=30, negativ_y=60))

    e = abb.ebene("kraft", "Kraft mit Wirkungslinie")
    e.append(strichpunkt(*P(-60 * math.cos(a), -60 * math.sin(a)), *P((L + 90) * math.cos(a), (L + 90) * math.sin(a))))
    e.append(vektor(*O, *E))
    e.append(text(E[0] - 50, E[1] - 14, "F", ROT, 22))
    e.append(punkt(*O, 3.6, ROT))
    e.append(hinweis(O[0] - 12, O[1] + 26, "Angriffspunkt", anker="end"))
    wl = P((L + 70) * math.cos(a), (L + 70) * math.sin(a))
    e.append(hinweis(wl[0] - 10, wl[1] - 14, "Wirkungslinie", anker="end"))
    e.append(hinweis(E[0] + 14, E[1] + 12, "Richtungssinn"))
    e.append(hinweis(E[0] + 14, E[1] + 28, "(Pfeilspitze)"))

    e = abb.ebene("komponenten", "Komponenten und Winkel")
    Fx, Fy = P(L * math.cos(a), 0), P(0, L * math.sin(a))
    e.append(linie(*E, *Fx, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(*E, *Fy, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(vektor(*O, *Fx, "F_x", gestrichelt=True, breite=1.5, ly=18))
    e.append(vektor(*O, *Fy, "F_y", gestrichelt=True, breite=1.5, lx=-22))
    e.append(winkelbogen(*O, 62, 0, 35, "α"))

    e = abb.ebene("einheitsvektoren", "Einheitsvektoren")
    e.append(pfeil(O[0], O[1], O[0] + 42, O[1], GRUEN, 2.2, (9, 6)))
    e.append(pfeil(O[0], O[1], O[0], O[1] - 42, GRUEN, 2.2, (9, 6)))
    e.append(text(O[0] + 24, O[1] - 14, "e_x", GRUEN, 16))
    e.append(text(O[0] + 16, O[1] - 34, "e_y", GRUEN, 16, anker="start"))
    return abb.speichern(ZIEL / "kraft-vektor.svg")


# =====================================================================
# Axiome der Statik: vier Felder, der Zoom wandert von Feld zu Feld
# =====================================================================
def axiome():
    abb = Abbildung(800, 560, "Axiome der Statik")
    W, H = 400, 280

    # 1. Linienflüchtigkeit (Feld oben links)
    e = abb.ebene("linienfluechtig", "1. Axiom: Linienflüchtigkeit")
    e.append(text(20, 26, "[1  Linienflüchtigkeit]", "#000000", 17, anker="start", italic=False))
    e.append(platte([(90, 120), (300, 95), (330, 190), (250, 235), (110, 215)]))
    y = 160
    e.append(strichpunkt(20, y, 390, y))
    e.append(kraft(98, y, 0, "F", laenge=60, label_seite=1))
    e.append(punkt(98, y))
    e.append('<g opacity="0.45">' + kraft(318, y, 0, "F", laenge=60, ziehend=True, label_seite=1) + "</g>")
    e.append(punkt(318, y))
    e.append(hinweis(200, 262, "gleiche Wirkung am starren Körper", anker="middle"))

    # 2. Kräfteparallelogramm (oben rechts)
    e = abb.ebene("parallelogramm", "2. Axiom: Kräfteparallelogramm")
    e.append(text(W + 20, 26, "[2  Kräfteparallelogramm]", "#000000", 17, anker="start", italic=False))
    A = (W + 90, 225)
    f1 = (170 * math.cos(math.radians(12)), -170 * math.sin(math.radians(12)))
    f2 = (120 * math.cos(math.radians(70)), -120 * math.sin(math.radians(70)))
    p1 = (A[0] + f1[0], A[1] + f1[1])
    p2 = (A[0] + f2[0], A[1] + f2[1])
    pr = (A[0] + f1[0] + f2[0], A[1] + f1[1] + f2[1])
    e.append(linie(*p1, *pr, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(*p2, *pr, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(vektor(*A, *p1, "F_1", ly=18))
    e.append(vektor(*A, *p2, "F_2", lx=-20))
    e.append(vektor(*A, *pr, "F_R", lx=-16, ly=-12))
    e.append(punkt(*A))

    # 3. Gleichgewicht zweier Kräfte (unten links)
    e = abb.ebene("gleichgewicht", "3. Axiom: Gleichgewicht")
    e.append(text(20, H + 26, "[3  Gleichgewicht zweier Kräfte]", "#000000", 17, anker="start", italic=False))
    e.append(platte([(110, H + 110), (290, H + 95), (310, H + 200), (130, H + 220)]))
    yw = H + 155
    e.append(strichpunkt(20, yw - 30, 390, yw + 30))
    m = (30 / 185)
    xa, xb = 118, 300
    e.append(kraft(xa, yw - 30 + m * (xa - 20) * 1.0, 180 + math.degrees(math.atan(m)), "F", laenge=70,
                   ziehend=True, label_seite=-1))
    e.append(kraft(xb, yw - 30 + m * (xb - 20) * 1.0, -math.degrees(math.atan(m)), "F", laenge=70,
                   ziehend=True, label_seite=1))
    e.append(hinweis(200, H + 258, "gleich groß · gleiche Wirkungslinie · entgegengesetzt", anker="middle"))

    # 4. Wechselwirkung und Schnittprinzip (unten rechts)
    e = abb.ebene("wechselwirkung", "4. Axiom: Wechselwirkung, Schnittprinzip")
    e.append(text(W + 20, H + 26, "[4  Wechselwirkung (actio = reactio)]", "#000000", 17, anker="start", italic=False))
    y1, y2 = H + 95, H + 190
    x0, x1, xs = W + 90, W + 310, W + 200
    e.append(balken(x0, y1, x1, y1, dicke=12))
    e.append(kraft(x0, y1, 180, "F", laenge=55, ziehend=True, label_seite=1))
    e.append(kraft(x1, y1, 0, "F", laenge=55, ziehend=True, label_seite=1))
    e.append(linie(xs, y1 - 22, xs, y1 + 22, "#000000", STRICH["normal"], strich="5 3"))
    d = 62
    e.append(balken(x0, y2, xs - d, y2, dicke=12))
    e.append(balken(xs + d, y2, x1, y2, dicke=12))
    e.append(kraft(x0, y2, 180, "F", laenge=55, ziehend=True, label_seite=1))
    e.append(kraft(x1, y2, 0, "F", laenge=55, ziehend=True, label_seite=1))
    e.append(kraft(xs - d, y2, 0, "F_i", laenge=44, ziehend=True, label_seite=-1, label_abstand=12))
    e.append(kraft(xs + d, y2, 180, "F_i", laenge=44, ziehend=True, label_seite=1, label_abstand=12))
    e.append(hinweis(W + 200, H + 248, "Schnitt: Kräfte paarweise entgegengesetzt", anker="middle"))
    return abb.speichern(ZIEL / "axiome.svg")


# =====================================================================
# Beispiel B01-1: Resultierende zweier Kräfte (VL 2013 Teil 1 S. 15)
#   F1 = 20 N unter 30°, F2 = 30 N unter 135°
# =====================================================================
def resultierende_zwei_kraefte():
    abb = Abbildung(720, 400, "Resultierende zweier Kräfte")
    s = 6.0                                  # px je N
    O = (250, 320)
    P = abbild(*O, s)
    F1 = (20 * math.cos(math.radians(30)), 20 * math.sin(math.radians(30)))
    F2 = (30 * math.cos(math.radians(135)), 30 * math.sin(math.radians(135)))
    FR = (F1[0] + F2[0], F1[1] + F2[1])

    e = abb.ebene("system", "Kräfte im Koordinatensystem")
    e.append(koord_xy(*O, 200, 250, negativ=200))
    e.append(vektor(*O, *P(*F1), "F_1", lx=-8, ly=-18))
    e.append(vektor(*O, *P(*F2), "F_2", lx=-18, ly=-16))
    e.append(winkelbogen(*O, 70, 0, 30, "30°"))
    e.append(linie(O[0] - 190, O[1], O[0], O[1], GRAU, 0.6))
    e.append(winkelbogen(*O, 60, 135, 180, "45°"))
    e.append(punkt(*O))

    e = abb.ebene("komponenten", "Komponenten")
    for (fx, fy), name in ((F1, "1"), (F2, "2")):
        E = P(fx, fy)
        e.append(linie(*E, *P(0, fy), GRAU, STRICH["duenn"], strich="4 3"))
        e.append(vektor(*O, *P(fx, 0), f"F_{{{name}x}}", gestrichelt=True, breite=1.4, ly=18, groesse=16))
    e.append(vektor(*P(F1[0], 0), *P(*F1), "F_{1y}", gestrichelt=True, breite=1.4, lx=26, groesse=16))
    e.append(vektor(*P(F2[0], 0), *P(*F2), "F_{2y}", gestrichelt=True, breite=1.4, lx=-28, groesse=16))

    e = abb.ebene("krafteck", "Krafteck")
    K0 = (560, 330)
    Q = abbild(*K0, s)
    e.append(hinweis(K0[0] - 30, K0[1] + 40, "Krafteck", anker="middle"))
    e.append(vektor(*K0, *Q(*F1), "F_1", ly=18))
    e.append(vektor(*Q(*F1), *Q(*FR), "F_2", lx=18, ly=-4))
    e.append(punkt(*K0))

    e = abb.ebene("resultierende", "Resultierende")
    e.append(vektor(*K0, *Q(*FR), "F_R", farbe=ROT, lx=-22, breite=2.6))
    e.append(vektor(*O, *P(*FR), "F_R", farbe=ROT, lx=20, ly=-40, breite=2.6))
    e.append(winkelbogen(*O, 34, 0, math.degrees(math.atan2(FR[1], FR[0])), ""))
    e.append(text(O[0] + 12, O[1] - 46, "α_R", GRUEN, 16, anker="start"))
    return abb.speichern(ZIEL / "resultierende-zwei-kraefte.svg")


# =====================================================================
# Beispiel B01-2: Masse am Seil, horizontal ausgelenkt (Gleichgewicht, zentral)
#   m = 20 kg, α = 30°  →  F = m g tan α, F_S = m g / cos α
# =====================================================================
def seil_masse():
    abb = Abbildung(860, 420, "Auslenkung einer Masse am Seil")
    alpha = math.radians(30)
    L = 190
    H = (130, 50)
    K = (H[0] + L * math.sin(alpha), H[1] + L * math.cos(alpha))
    yk = K[1] + 70                         # Oberkante Masse

    def masse(x, y, b=64, h=52):
        return gruppe([platte([(x - b / 2, y), (x + b / 2, y), (x + b / 2, y + h), (x - b / 2, y + h)], "#cfcfcf"),
                       text(x - 16, y + 16, "m", "#000000", 20)])

    e = abb.ebene("system", "System")
    # Aufhängung an der Decke (Festlager um 180° gedreht)
    e.append(festlager(H[0], H[1], drehung=180))
    e.append(linie(*H, *K, "#000000", 1.6))
    e.append(linie(K[0], K[1], K[0], yk, "#000000", 1.6))
    e.append(masse(K[0], yk))
    e.append(punkt(*K, 2.6))
    e.append(linie(H[0], H[1], H[0], H[1] + 230, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(winkelbogen(*H, 120, -90, -60, "α"))
    e.append(kraft(*K, 0, "F", laenge=85, ziehend=True, label_seite=1))
    e.append(text(H[0] - 30, 380, "g", GRUEN, 18))
    e.append(pfeil(H[0] - 14, 345, H[0] - 14, 400, GRUEN, STRICH["normal"], (8, 5)))

    # Freikörperbild: rechts daneben
    dx = 290
    Kf = (K[0] + dx, K[1])
    e = abb.ebene("freischnitt", "Freikörperbild")
    e.append(linie(Kf[0], Kf[1], Kf[0], yk, "#000000", 1.6))
    e.append(linie(*Kf, Kf[0] - 40 * math.sin(alpha), Kf[1] - 40 * math.cos(alpha), "#000000", 1.6))
    e.append(masse(Kf[0], yk))
    e.append(punkt(*Kf, 2.6))
    # Schnittmarke am Seil
    cx, cy = Kf[0] - 40 * math.sin(alpha), Kf[1] - 40 * math.cos(alpha)
    e.append(linie(cx - 16 * math.cos(alpha), cy + 16 * math.sin(alpha), cx + 16 * math.cos(alpha),
                   cy - 16 * math.sin(alpha), "#000000", STRICH["normal"]))
    e.append(kraft(cx, cy, 120, "F_S", laenge=80, ziehend=True, label_seite=-1))
    e.append(kraft(*Kf, 0, "F", laenge=85, ziehend=True, label_seite=1))
    e.append(kraft(Kf[0], yk + 26, -90, "m g", laenge=70, ziehend=True, label_seite=-1, label_pos=0.75))
    e.append(koord_xy(Kf[0] + 110, yk + 70, 42, 42))
    e.append(hinweis(Kf[0] - 120, 32, "Freikörperbild"))

    # Krafteck (geschlossen)
    s = 0.62                               # px je N
    mg = 20 * 9.81
    F = mg * math.tan(alpha)
    S0 = (750, 70)
    S1 = (S0[0], S0[1] + mg * s)
    S2 = (S1[0] + F * s, S1[1])
    e = abb.ebene("krafteck", "Geschlossenes Krafteck")
    e.append(hinweis(S0[0] - 10, 32, "Krafteck", anker="middle"))
    e.append(vektor(*S0, *S1, "m g", lx=-28))
    e.append(vektor(*S1, *S2, "F", ly=20))
    e.append(vektor(*S2, *S0, "F_S", lx=28, ly=-4))
    e.append(winkelbogen(*S0, 40, -90, -60, "α"))
    e.append(punkt(*S0))
    return abb.speichern(ZIEL / "seil-masse.svg")


# =====================================================================
# Moment: Kräftepaar, Moment einer Kraft um einen Punkt, Versatzmoment
# =====================================================================
def moment_grafik():
    abb = Abbildung(1020, 330, "Das Moment")

    # Feld 1: Kräftepaar
    e = abb.ebene("kraeftepaar", "Kräftepaar")
    e.append(text(20, 26, "[Kräftepaar]", "#000000", 17, anker="start", italic=False))
    e.append(platte([(60, 110), (250, 100), (260, 240), (70, 250)]))
    xl, xr = 100, 220
    e.append(strichpunkt(xl, 60, xl, 300))
    e.append(strichpunkt(xr, 60, xr, 300))
    e.append(kraft(xl, 175, 90, "F", laenge=70, ziehend=True, label_seite=1))
    e.append(kraft(xr, 175, -90, "F", laenge=70, ziehend=True, label_seite=1))
    e.append(mass(xl, 175, xr, 175, "b", abstand=-115))
    e.append(text(290, 175, "[=]", "#000000", 26, italic=False))
    e.append(platte([(320, 110), (480, 100), (490, 240), (330, 250)]))
    e.append(moment(405, 175, "", gegen_uhrzeiger=False, r=26, start=150, bogen=280))
    e.append(text(405, 120, "M = F b", ROT, 19))

    # Feld 2: Moment einer Kraft bezüglich eines Punktes
    e = abb.ebene("hebelarm", "Moment um einen Punkt, Hebelarm")
    x0 = 530
    e.append(text(x0, 26, "[Moment um einen Punkt]", "#000000", 17, anker="start", italic=False))
    O = (x0 + 50, 250)
    A = (x0 + 200, 150)
    w = math.radians(60)
    u = (math.cos(w), -math.sin(w))
    e.append(strichpunkt(A[0] - u[0] * 110, A[1] - u[1] * 110, A[0] + u[0] * 120, A[1] + u[1] * 120))
    e.append(kraft(*A, 60, "F", laenge=85, ziehend=True, label_seite=-1))
    e.append(vektor(*O, *A, "r", farbe=GRUEN, breite=1.5, lx=-4, ly=-14))
    # Lotfußpunkt
    t = (O[0] - A[0]) * u[0] + (O[1] - A[1]) * u[1]
    Fp = (A[0] + t * u[0], A[1] + t * u[1])
    e.append(linie(*O, *Fp, GRUEN, STRICH["normal"]))
    lx, ly = (Fp[0] - O[0]), (Fp[1] - O[1])
    ll = math.hypot(lx, ly)
    e.append(rechter_winkel(*Fp, -lx / ll, -ly / ll, u[0], u[1]))
    e.append(text((O[0] + Fp[0]) / 2 - 4, (O[1] + Fp[1]) / 2 + 18, "b", GRUEN, 19))
    e.append(punkt(*O, 3.6))
    e.append(text(O[0] - 14, O[1] + 14, "0", "#000000", 18))
    e.append(punkt(*A, 2.8))
    e.append(text(A[0] + 14, A[1] + 12, "A", "#000000", 17))
    e.append(hinweis(x0 + 20, 305, "Hebelarm b: Abstand von 0 zur Wirkungslinie"))

    # Feld 3 (eigene Ebene, gleiche Position wie Feld 1): Versatzmoment
    e = abb.ebene("versatz", "Parallelverschiebung, Versatzmoment")
    e.append(text(20, 26, "[Kraft parallel verschieben]", "#000000", 17, anker="start", italic=False))
    e.append(platte([(60, 110), (250, 100), (260, 240), (70, 250)]))
    e.append(strichpunkt(150, 60, 150, 300))
    e.append(kraft(150, 160, -90, "F", laenge=60, label_seite=1))
    e.append(punkt(150, 160))
    e.append(text(290, 175, "[=]", "#000000", 26, italic=False))
    e.append(platte([(320, 110), (480, 100), (490, 240), (330, 250)]))
    e.append(strichpunkt(370, 60, 370, 300))
    e.append(strichpunkt(450, 60, 450, 300, "#bbbbbb"))
    e.append(kraft(370, 160, -90, "F", laenge=60, label_seite=-1))
    e.append(punkt(370, 160))
    e.append(moment(425, 175, "", gegen_uhrzeiger=False, r=20, start=150, bogen=280))
    e.append(text(425, 218, "M = F a", ROT, 18))
    e.append(mass(370, 280, 450, 280, "a", abstand=-14))
    return abb.speichern(ZIEL / "moment.svg")


# =====================================================================
# Beispiel B01-3: Scheibe mit vier Kräften (VL 2013 Teil 1 S. 26–27)
#   F1 = F4 = F, F2 = 2F, F3 = 3F; F_R = 5F, M_R0 = −5cF, WL y = −3/4 x + 5/4 c
# =====================================================================
def scheibe_vier_kraefte():
    abb = Abbildung(720, 420, "Scheibe mit vier Kräften")
    c = 52
    O = (150, 260)
    P = abbild(*O, c)
    k = 30                                    # px je F

    e = abb.ebene("system", "Scheibe mit Kräften")
    e.append(platte([P(0, -1), P(6, -1), P(6, 0), P(4.4, 2), P(0, 2)]))
    e.append(koord_xy(*O, 7.2 * c, 1.5 * c, negativ=1.6 * c))
    for xv in (1, 3, 6):
        x, y = P(xv, 0)
        e.append(linie(x, y - 4, x, y + 4, GRUEN, STRICH["normal"]))
    e.append(text(P(6, 0)[0] + 10, P(6, 0)[1] + 14, "6c", GRUEN, 15, anker="start"))
    e.append(text(P(3, 0)[0], P(3, 0)[1] + 15, "3c", GRUEN, 15))
    e.append(text(P(1, 0)[0], P(1, 0)[1] + 15, "c", GRUEN, 15))
    for yv, lab in ((2, "2c"), (1, "c"), (-1, "−c")):
        x, y = P(0, yv)
        e.append(linie(x - 4, y, x + 4, y, GRUEN, STRICH["normal"]))
        e.append(text(x - 10, y + (14 if yv == 2 else 0), lab, GRUEN, 15, anker="end"))
    e.append(kraft(*P(0, 2), 0, "F_1 = F", laenge=1.4 * k, label_seite=-1, label_abstand=12))
    e.append(kraft(*P(0, 2), -90, "F_2 = 2F", laenge=2 * k, label_seite=-1))
    e.append(kraft(*P(6, -1), 0, "F_3 = 3F", laenge=3 * k, ziehend=True, label_seite=1, label_pos=0.55))
    e.append(kraft(*P(6, 0), -90, "F_4 = F", laenge=1.4 * k, label_seite=-1))
    for p in (P(0, 2), P(6, -1), P(6, 0)):
        e.append(punkt(*p, 2.6))
    e.append(text(O[0] - 12, O[1] + 14, "0", "#000000", 16))

    e = abb.ebene("ersatz-0", "Resultierende und Moment im Ursprung")
    e.append(kraft(*O, -36.87, "F_R = 5F", laenge=5 * k * 0.75, ziehend=True, label_seite=-1, farbe=ROT))
    e.append(moment(*O, "", gegen_uhrzeiger=False, r=24, start=200, bogen=250))
    e.append(text(O[0] - 34, O[1] - 34, "M_R", ROT, 18, anker="end"))

    e = abb.ebene("wirkungslinie", "Wirkungslinie der Resultierenden")
    xa, xb = -0.4, 7.0
    e.append(linie(*P(xa, -0.75 * xa + 1.25), *P(xb, -0.75 * xb + 1.25), ROT, 1.2, strich="10 5"))
    x0 = 5 / 3
    e.append(kraft(*P(x0, 0), -36.87, "F_R", laenge=5 * k * 0.75, ziehend=True, label_seite=-1, farbe=ROT))
    e.append(punkt(*P(x0, 0), 3, ROT))
    e.append(punkt(*P(0, 1.25), 3, ROT))
    e.append(text(P(0, 1.25)[0] + 12, P(0, 1.25)[1] - 12, "5c/4", ROT, 15, anker="start"))
    e.append(text(P(x0, 0)[0] + 6, P(x0, 0)[1] - 16, "5c/3", ROT, 15, anker="start"))
    return abb.speichern(ZIEL / "scheibe-vier-kraefte.svg")


# =====================================================================
# Seminaraufgaben (nach Götz, Abschn. 1.1 und 1.2) und Hausaufgaben
# =====================================================================
def _aufgabe(name, breite, hoehe):
    abb = Abbildung(breite, hoehe, name)
    return abb, abb.ebene("system", "System")


def aufgabe_1_1_3():
    abb, e = _aufgabe("Containerschiff mit zwei Schleppern", 560, 260)
    y, xb = 130, 330
    e.append(platte([(60, y - 32), (240, y - 32), (300, y - 22), (xb, y), (300, y + 22), (240, y + 32), (60, y + 32),
                     (52, y)], "#d9d9d9"))
    e.append(linie(240, y - 32, 240, y + 32, "#000000", STRICH["normal"]))
    e.append(strichpunkt(20, y, 540, y))
    p1, p2 = math.radians(21), math.radians(35)
    for phi, s, name in ((p1, 1, "F_1"), (p2, -1, "F_2")):
        e.append(kraft(xb, y, s * math.degrees(phi), name, laenge=120, ziehend=True,
                       label_seite=-s, label_pos=0.6, label_abstand=14))
        ex, ey = xb + 175 * math.cos(phi), y - s * 175 * math.sin(phi)
        e.append(linie(xb + 122 * math.cos(phi), y - s * 122 * math.sin(phi), ex, ey, "#000000", STRICH["duenn"]))
        e.append(f'<ellipse cx="{ex + 14 * math.cos(phi):.1f}" cy="{ey - s * 14 * math.sin(phi):.1f}" rx="17" ry="8" '
                  f'transform="rotate({-s * math.degrees(phi):.1f} {ex + 14 * math.cos(phi):.1f} '
                  f'{ey - s * 14 * math.sin(phi):.1f})" fill="#7a7a7a" stroke="#000" stroke-width="1"/>')
    e.append(winkelbogen(xb, y, 70, 0, 21, "φ_1"))
    e.append(winkelbogen(xb, y, 70, -35, 0, "φ_2"))
    return abb.speichern(ZIEL / "aufgabe-1-1-3.svg")


def aufgabe_1_1_4():
    abb, e = _aufgabe("Stahlträger am Kran", 480, 280)
    yb, xm, l, h = 200, 230, 180, 110
    xa, xc = xm - l / 2, xm + l / 2
    e.append(balken(xm - 170, yb, xm + 170, yb, dicke=14))
    ring = (xm, yb - 7 - h)
    e.append(linie(xa, yb - 7, ring[0] - 6, ring[1] + 6, "#000000", 1.8))
    e.append(linie(xc, yb - 7, ring[0] + 6, ring[1] + 6, "#000000", 1.8))
    e.append(kreis(*ring, 9, "#000000", "#ffffff", 3))
    e.append(linie(ring[0], ring[1] - 9, ring[0], ring[1] - 70, "#000000", 2))
    e.append(text(xm, yb - 45, "[Seil]", "#000000", 14, italic=False))
    e.append(mass(xa, yb + 7, xc, yb + 7, "l", abstand=-30))
    e.append(mass(xm - 150, yb - 7, xm - 150, ring[1], "h", abstand=-18))
    e.append(linie(xm - 160, ring[1], ring[0] - 12, ring[1], GRUEN, STRICH["duenn"]))
    e.append(text(xm + 150, yb - 30, "m", "#000000", 20))
    e.append(pfeil(430, 60, 430, 110, GRUEN, STRICH["normal"], (8, 5)))
    e.append(text(444, 76, "g", GRUEN, 18, anker="start"))
    return abb.speichern(ZIEL / "aufgabe-1-1-4.svg")


def aufgabe_1_1_5():
    abb, e = _aufgabe("Kiste an Stricken", 460, 340)
    H = (150, 50)
    l = 170
    th = math.radians(35)
    K = (H[0] + l * math.sin(th), H[1] + l * math.cos(th))
    e.append(festlager(*H, drehung=180))
    e.append(linie(*H, *K, "#000000", 1.6))
    e.append(linie(K[0], K[1], K[0], K[1] + 40, "#000000", 1.6))
    e.append(platte([(K[0] - 28, K[1] + 40), (K[0] + 28, K[1] + 40), (K[0] + 28, K[1] + 84), (K[0] - 28, K[1] + 84)],
                    "#cfcfcf"))
    e.append(text(K[0], K[1] + 62, "m", "#000000", 20))
    e.append(punkt(*K, 2.6))
    e.append(kraft(*K, 0, "F", laenge=90, ziehend=True, label_seite=1))
    e.append(text((H[0] + K[0]) / 2 + 14, (H[1] + K[1]) / 2 - 6, "[(a)]", "#000000", 15, anker="start", italic=False))
    e.append(text(K[0] + 30, K[1] - 14, "[(b)]", "#000000", 15, italic=False))
    e.append(text(K[0] + 14, K[1] + 22, "[(c)]", "#000000", 15, anker="start", italic=False))
    # Ausgangslage gestrichelt
    y0 = H[1] + l
    e.append(linie(H[0], H[1], H[0], y0 + 40, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(polylinie([(H[0] - 28, y0 + 40), (H[0] + 28, y0 + 40), (H[0] + 28, y0 + 84), (H[0] - 28, y0 + 84)],
                       GRAU, STRICH["duenn"], strich="4 3", schliessen=True))
    e.append(mass(H[0], H[1], H[0], y0, "l", abstand=-70))
    e.append(mass(H[0] - 40, y0, H[0] - 40, K[1], "h", abstand=-18))
    e.append(linie(H[0] - 64, K[1], K[0], K[1], GRUEN, STRICH["duenn"], strich="2 3"))
    return abb.speichern(ZIEL / "aufgabe-1-1-5.svg")


def aufgabe_1_2_1():
    abb, e = _aufgabe("Scheibe mit drei Kräften", 520, 330)
    m = 52
    O = (215, 165)
    P = abbild(*O, m)
    e.append(platte([P(-3.6, 1.7), P(-2.6, 2.8), P(4.1, 2.8), P(5.0, 1.7), P(5.0, -1.9), P(4.1, -2.9), P(-2.6, -2.9),
                     P(-3.6, -1.9)], "#ececec"))
    e.append(koord_xy(*O, 4.6 * m, 2.6 * m, negativ=3.3 * m, negativ_y=2.6 * m))
    for xv in (-3, -2, -1, 1, 2, 3, 4):
        x, y = P(xv, 0)
        e.append(linie(x, y - 4, x, y + 4, "#000000", STRICH["duenn"]))
        e.append(text(x + (6 if xv < 0 else 0), y + 15, str(xv).replace("-", "−"), "#000000", 13, italic=False))
    for yv in (-2, -1, 1, 2):
        x, y = P(0, yv)
        e.append(linie(x - 4, y, x + 4, y, "#000000", STRICH["duenn"]))
        e.append(text(x - 8, y, str(yv).replace("-", "−"), "#000000", 13, anker="end", italic=False))
    e.append(kraft(*P(-2, 0), 60, "F_1", laenge=95, ziehend=True, label_seite=1, label_pos=0.85))
    e.append(winkelbogen(*P(-2, 0), 26, 0, 60, "α_1"))
    e.append(kraft(*P(0, -2), 0, "F_2", laenge=80, ziehend=True, label_seite=1))
    e.append(kraft(*P(4, 1), -45, "F_3", laenge=95, label_seite=-1, label_pos=0.85))
    e.append(linie(*P(4, 1), *P(0, 1), GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(*P(4, 1), *P(4.9, 1), GRAU, STRICH["duenn"]))
    e.append(winkelbogen(*P(4, 1), 34, 135, 180, "α_3"))
    for p in (P(-2, 0), P(0, -2), P(4, 1)):
        e.append(punkt(*p, 2.6))
    return abb.speichern(ZIEL / "aufgabe-1-2-1.svg")


def aufgabe_1_2_4():
    abb, e = _aufgabe("Fahrradantrieb", 620, 300)
    yb = 270
    rH, rZ, rR = 115, 38, 15
    H = (450, yb - rH)
    Z = (170, H[1] + 20)
    e.append(linie(20, yb, 600, yb, "#000000", STRICH["normal"]))
    e.append(kreis(*H, rH, "#000000", "none", 4))
    for i in range(10):
        w = math.radians(i * 36 + 10)
        e.append(linie(H[0], H[1], H[0] + (rH - 3) * math.cos(w), H[1] - (rH - 3) * math.sin(w), "#555555", 0.7))
    e.append(kreis(*H, rR, "#000000", "#cfcfcf", 1.2))
    e.append(linie(Z[0], Z[1] - rZ, H[0], H[1] - rR, "#000000", 1.0))
    e.append(linie(Z[0], Z[1] + rZ, H[0], H[1] + rR, "#000000", 1.0))
    e.append(kreis(*Z, rZ, "#000000", "#cfcfcf", 1.2))
    a = math.radians(40)
    lK = 80
    Pd = (Z[0] - lK * math.cos(a), Z[1] - lK * math.sin(a))
    e.append(balken(*Z, *Pd, dicke=8))
    e.append(punkt(*Z, 3))
    e.append(platte([(Pd[0] - 14, Pd[1] - 5), (Pd[0] + 14, Pd[1] - 5), (Pd[0] + 14, Pd[1] + 5), (Pd[0] - 14, Pd[1] + 5)],
                    "#7a7a7a"))
    e.append(kraft(Pd[0], Pd[1] - 6, -90, "F", laenge=60, label_seite=-1))
    e.append(linie(Pd[0] - 60, Pd[1], Pd[0] + 4, Pd[1], GRAU, STRICH["duenn"], strich="3 2"))
    e.append(linie(Z[0], Z[1], Z[0] - 140, Z[1], GRAU, STRICH["duenn"], strich="3 2"))
    e.append(winkelbogen(*Z, 40, 140, 180, "α"))
    e.append(mass(*Z, *Pd, "l_K", abstand=-18))
    e.append(mass(Z[0] - rZ, Z[1], Z[0] + rZ, Z[1], "d_Z", abstand=-rZ - 30))
    e.append(mass(H[0] - rH, H[1], H[0] + rH, H[1], "d_H", abstand=rH + 22))
    e.append(mass(H[0] - rR, H[1], H[0] + rR, H[1], "d_R", abstand=-rR - 26))
    return abb.speichern(ZIEL / "aufgabe-1-2-4.svg")


def hausaufgabe_bolzen():
    """B01-4: Bolzen mit vier Kräften in der x-y-Ebene (Draufsicht)."""
    abb, e = _aufgabe("Bolzen mit vier Kräften (Draufsicht)", 520, 330)
    O = (270, 130)
    e.append(koord_xy(*O, 190, 110, negativ=200, negativ_y=150))
    e.append(kreis(*O, 16, "#000000", "#d9d9d9", 1.2))
    L = 130
    for w, name, seite in ((-30, "F_1", -1), (-90, "F_2", 1), (240, "F_3", 1), (180, "F_4", 1)):
        e.append(kraft(*O, w, name, laenge=L if name != "F_2" else 110, ziehend=True, label_seite=seite,
                       label_pos=0.9, label_abstand=12))
    e.append(winkelbogen(*O, 80, -30, 0, "30°"))
    e.append(winkelbogen(*O, 70, 180, 240, "60°"))
    e.append(hinweis(20, 310, "Draufsicht auf die Platte, Kräfte am Bolzenkopf"))
    return abb.speichern(ZIEL / "hausaufgabe-bolzen.svg")


def hausaufgabe_wirkungslinien():
    """B01-5: drei Kräfte durch zwei Kräfte auf gegebenen Wirkungslinien ins Gleichgewicht bringen."""
    abb, e = _aufgabe("Gleichgewicht mit zwei Wirkungslinien", 420, 300)
    O = (210, 170)
    e.append(koord_xy(*O, 180, 130, negativ=180))
    for w, name in ((60, "Wl_4"), (120, "Wl_5")):
        u = (math.cos(math.radians(w)), -math.sin(math.radians(w)))
        e.append(strichpunkt(O[0] - u[0] * 150, O[1] - u[1] * 150, O[0] + u[0] * 150, O[1] + u[1] * 150, "#000000"))
        e.append(text(O[0] + u[0] * 168, O[1] + u[1] * 168, name, "#000000", 17))
    e.append(winkelbogen(*O, 50, 0, 60, "α_4"))
    e.append(winkelbogen(*O, 92, 0, 120, ""))
    e.append(text(O[0] + 8, O[1] - 104, "α_5", GRUEN, 15, anker="start"))
    e.append(punkt(*O))
    return abb.speichern(ZIEL / "hausaufgabe-wirkungslinien.svg")


if __name__ == "__main__":
    for fn in (einordnung, kraft_vektor, axiome, resultierende_zwei_kraefte, seil_masse, moment_grafik,
               scheibe_vier_kraefte, aufgabe_1_1_3, aufgabe_1_1_4, aufgabe_1_1_5, aufgabe_1_2_1, aufgabe_1_2_4,
               hausaufgabe_bolzen, hausaufgabe_wirkungslinien):
        print(fn())

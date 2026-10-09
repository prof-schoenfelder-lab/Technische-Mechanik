"""Grafiken zur Veranstaltung 0: Mathematische Werkzeuge.

Einheitskreis, Vektoraddition, Skalarprodukt und Arbeit, Kreuzprodukt und Moment, Feder.
Aufruf:  python werkzeuge/grafiken_mathematik.py
Ergebnis: grafiken/mathematik/*.svg (Inkscape-Ebenen = Scroll-Schritte)
"""

import math
from pathlib import Path

from grafiken_grundlagen import (GRAU, GRUEN, ROT, abbild, hinweis, koord_xy, platte, punkt,
                                 rechter_winkel, vektor)
from tmzeichnen import STRICH, Abbildung, _spitze, gruppe, kraft, kreis, linie, mass, moment, polylinie, text, \
    winkelbogen

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "mathematik"
BLAU = "#0050b4"
SCHWARZ = "#000000"


def weg(x1, y1, x2, y2, label="", lx=0, ly=0):
    """Verschiebungs-/Wegvektor (schwarz)."""
    return vektor(x1, y1, x2, y2, label, farbe=SCHWARZ, breite=1.6, lx=lx, ly=ly)


def doppelpfeil(x1, y1, x2, y2, farbe=ROT, breite=STRICH["dick"]):
    """Momentenvektor als Doppelpfeil."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    return gruppe([linie(x1, y1, x2 - ux * 18, y2 - uy * 18, farbe, breite),
                   _spitze(x2, y2, ux, uy, farbe, 12, 9),
                   _spitze(x2 - ux * 11, y2 - uy * 11, ux, uy, farbe, 12, 9)])


def feder(x, y1, y2, breite=18, windungen=7, farbe=SCHWARZ):
    """Schraubenfeder (Zickzack) senkrecht von y1 nach y2."""
    vor = 10
    pts = [(x, y1), (x, y1 + vor)]
    n = 2 * windungen
    h = (y2 - y1 - 2 * vor) / n
    for i in range(n):
        pts.append((x + (breite / 2 if i % 2 == 0 else -breite / 2), y1 + vor + (i + 0.5) * h))
    pts += [(x, y2 - vor), (x, y2)]
    return polylinie(pts, farbe, 1.3)


# =====================================================================
# Einheitskreis: Sinus und Kosinus
# =====================================================================
def einheitskreis():
    abb = Abbildung(820, 420, "Sinus und Kosinus am Einheitskreis")
    R = 150
    O = (230, 215)
    a = math.radians(40)
    P = (O[0] + R * math.cos(a), O[1] - R * math.sin(a))

    e = abb.ebene("kreis", "Einheitskreis")
    e.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="{R}" fill="none" stroke="#999999" stroke-width="1.2"/>')
    e.append(koord_xy(*O, R + 40, R + 40, negativ=R + 30))
    for sx, sy, lab in ((R, 0, "1"), (-R, 0, "−1"), (0, -R, "1"), (0, R, "−1")):
        e.append(punkt(O[0] + sx, O[1] + sy, 2.2))
        e.append(text(O[0] + sx + (10 if sx > 0 else -12 if sx < 0 else 10), O[1] + sy + (16 if sy == 0 else 0),
                      f"[{lab}]", SCHWARZ, 14, anker="start" if sx >= 0 else "end", italic=False))

    e = abb.ebene("punkt", "Punkt auf dem Kreis")
    e.append(linie(*O, *P, SCHWARZ, 1.6))
    e.append(punkt(*P, 3.6))
    e.append(winkelbogen(*O, 40, 0, 40, "α"))
    e.append(text(P[0] + 10, P[1] - 14, "P", SCHWARZ, 18, anker="start"))
    e.append(text(O[0] + 0.45 * R * math.cos(a) - 8, O[1] - 0.45 * R * math.sin(a) - 12, "[1]", SCHWARZ, 15,
                  italic=False))

    e = abb.ebene("projektion", "cos und sin als Koordinaten")
    e.append(linie(P[0], P[1], P[0], O[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(P[0], P[1], O[0], P[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(O[0], O[1], P[0], O[1], BLAU, 4))
    e.append(linie(O[0], O[1], O[0], P[1], ROT, 4))
    e.append(text((O[0] + P[0]) / 2, O[1] + 18, "cos α", BLAU, 17))
    e.append(text(O[0] + 8, P[1] + 16, "sin α", ROT, 17, anker="start"))

    e = abb.ebene("quadranten", "Vorzeichen in den Quadranten")
    b = math.radians(140)
    Q = (O[0] + R * math.cos(b), O[1] - R * math.sin(b))
    e.append(linie(*O, *Q, SCHWARZ, 1.6))
    e.append(punkt(*Q, 3.6))
    e.append(linie(Q[0], Q[1], Q[0], O[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(O[0], O[1], Q[0], O[1], BLAU, 4))
    e.append(winkelbogen(*O, 26, 0, 140, ""))
    e.append(text(O[0] - 44, O[1] - 12, "140°", GRUEN, 14))
    e.append(text(Q[0] - 8, Q[1] - 14, "Q", SCHWARZ, 18, anker="end"))
    for qx, qy, s in ((1, -1, "I: cos > 0, sin > 0"), (-1, -1, "II: cos < 0, sin > 0"),
                      (-1, 1, "III: cos < 0, sin < 0"), (1, 1, "IV: cos > 0, sin < 0")):
        e.append(text(O[0] + qx * 112, O[1] + qy * 172, f"[{s}]", "#555555", 12, italic=False))

    # rechtwinkliges Dreieck mit Hypotenuse F
    e = abb.ebene("dreieck", "Rechtwinkliges Dreieck: Kraftkomponenten")
    D = (480, 330)
    L = 230
    E = (D[0] + L * math.cos(a), D[1] - L * math.sin(a))
    e.append(platte([D, (E[0], D[1]), E], "#f6f6f6"))
    e.append(vektor(*D, *E, "", farbe=ROT))
    e.append(text((D[0] + E[0]) / 2 - 16, (D[1] + E[1]) / 2 - 16, "F", ROT, 20))
    e.append(rechter_winkel(E[0], D[1], -1, 0, 0, -1, 12))
    e.append(winkelbogen(*D, 46, 0, 40, "α"))
    e.append(text((D[0] + E[0]) / 2, D[1] + 20, "F_x = F cos α", BLAU, 17))
    e.append(text(E[0] + 10, (D[1] + E[1]) / 2, "F_y = F sin α", ROT, 17, anker="start"))
    e.append(text((D[0] + E[0]) / 2, D[1] + 42, "[Ankathete]", "#555555", 13, italic=False))
    e.append(text(E[0] + 10, (D[1] + E[1]) / 2 + 22, "[Gegenkathete]", "#555555", 13, anker="start", italic=False))
    e.append(text((D[0] + E[0]) / 2 - 40, (D[1] + E[1]) / 2 - 2, "[Hypotenuse]", "#555555", 13, anker="end",
                  italic=False))
    return abb.speichern(ZIEL / "einheitskreis.svg")


# =====================================================================
# Vektoraddition
# =====================================================================
def vektoraddition():
    abb = Abbildung(560, 360, "Addition von Kräften")
    O = (90, 300)
    s = 1.0
    F1, F2 = (230, 70), (-80, 160)
    P = abbild(*O, s)
    FR = (F1[0] + F2[0], F1[1] + F2[1])

    e = abb.ebene("vektoren", "Zwei Kräfte")
    e.append(koord_xy(*O, 330, 270, negativ=30, negativ_y=30))
    e.append(vektor(*O, *P(*F1), "F_1", ly=20))
    e.append(vektor(*O, *P(*F2), "F_2", lx=-20))
    e.append(punkt(*O))

    e = abb.ebene("kette", "Spitze an Fuß")
    e.append('<g opacity="0.55">' + vektor(*P(*F1), *P(*FR), "F_2", lx=22) + "</g>")

    e = abb.ebene("summe", "Resultierende")
    e.append(vektor(*O, *P(*FR), "F_R", farbe=ROT, breite=2.6, lx=-18, ly=-8))

    e = abb.ebene("komponenten", "Komponentenweise addieren")
    e.append(linie(*P(*FR), *P(FR[0], 0), GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(*P(*FR), *P(0, FR[1]), GRAU, STRICH["duenn"], strich="4 3"))
    e.append(text(P(FR[0], 0)[0], O[1] + 20, "F_{1x} + F_{2x}", BLAU, 15))
    e.append(text(O[0] - 8, P(0, FR[1])[1], "F_{1y} + F_{2y}", BLAU, 15, anker="end"))
    return abb.speichern(ZIEL / "vektoraddition.svg")


# =====================================================================
# Skalarprodukt: Projektion
# =====================================================================
def skalarprodukt():
    abb = Abbildung(520, 300, "Skalarprodukt als Projektion")
    O = (70, 240)
    wa, wb = math.radians(12), math.radians(58)
    La, Lb = 360, 210
    A = (O[0] + La * math.cos(wa), O[1] - La * math.sin(wa))
    B = (O[0] + Lb * math.cos(wb), O[1] - Lb * math.sin(wb))
    proj = Lb * math.cos(wb - wa)
    Bp = (O[0] + proj * math.cos(wa), O[1] - proj * math.sin(wa))

    e = abb.ebene("vektoren", "Zwei Vektoren")
    e.append(weg(*O, *A, "a", ly=18))
    e.append(weg(*O, *B, "b", lx=-16))
    e.append(winkelbogen(*O, 60, 12, 58, "φ"))
    e.append(punkt(*O))

    e = abb.ebene("projektion", "Projektion von b auf a")
    e.append(linie(*B, *Bp, GRAU, STRICH["normal"], strich="4 3"))
    e.append(rechter_winkel(*Bp, -math.cos(wa), math.sin(wa), (B[0] - Bp[0]) / math.hypot(B[0] - Bp[0], B[1] - Bp[1]),
                            (B[1] - Bp[1]) / math.hypot(B[0] - Bp[0], B[1] - Bp[1])))
    e.append(linie(O[0], O[1] + 1, Bp[0], Bp[1] + 1, GRUEN, 4.5))
    e.append(text((O[0] + Bp[0]) / 2, (O[1] + Bp[1]) / 2 + 22, "b_a = b cos φ", GRUEN, 16))
    return abb.speichern(ZIEL / "skalarprodukt.svg")


# =====================================================================
# Arbeit: gerader Weg, Höhe, gekrümmter Weg
# =====================================================================
def arbeit():
    abb = Abbildung(960, 330, "Arbeit einer Kraft")

    # Feld 1: gerader Weg, Kraft schräg
    e = abb.ebene("gerade", "Gerader Weg")
    O = (40, 250)
    e.append(weg(O[0], O[1], O[0] + 260, O[1] - 60, "s", lx=10, ly=18))
    ws = math.atan2(60, 260)
    wf = ws + math.radians(50)
    F = (O[0] + 150 * math.cos(wf), O[1] - 150 * math.sin(wf))
    e.append(vektor(*O, *F, "F", lx=-12, ly=-6))
    fs = 150 * math.cos(wf - ws)
    Fs = (O[0] + fs * math.cos(ws), O[1] - fs * math.sin(ws))
    e.append(linie(*F, *Fs, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(vektor(O[0], O[1] + 1, Fs[0], Fs[1] + 1, "F_s", farbe=ROT, gestrichelt=True, breite=1.6, ly=20))
    e.append(winkelbogen(*O, 50, math.degrees(ws), math.degrees(wf), "φ"))
    e.append(punkt(*O))
    e.append(text(30, 30, "W = F_s · s", "#444444", 17, anker="start"))

    # Feld 2: Kraft senkrecht, Komponente des Weges in Kraftrichtung = Höhe
    e = abb.ebene("hoehe", "Weg in Kraftrichtung: Höhe")
    O2 = (360, 260)
    S = (O2[0] + 230, O2[1] - 130)
    e.append(weg(*O2, *S, "s", lx=14, ly=10))
    e.append(vektor(O2[0], O2[1], O2[0], O2[1] - 110, "F", lx=16, ly=-30))
    e.append(linie(S[0], S[1], O2[0] - 10, S[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(O2[0] - 12, O2[1], O2[0] - 12, S[1], GRUEN, 4))
    e.append(text(O2[0] - 20, (O2[1] + S[1]) / 2, "s_F = h", GRUEN, 16, anker="end"))
    e.append(winkelbogen(*O2, 40, math.degrees(math.atan2(130, 230)), 90, "φ"))
    e.append(punkt(*O2))
    e.append(koord_xy(O2[0] + 150, O2[1] + 50, 34, 34))
    e.append(text(350, 30, "W = F · s_F", "#444444", 17, anker="start"))

    # Feld 3: gekrümmter Weg, Vorzeichen von dW
    e = abb.ebene("kurve", "Gekrümmter Weg")
    pts = []
    for i in range(61):
        t = i / 60
        x = 650 + 290 * t
        y = 205 + 60 * math.cos(math.pi * 1.6 * t) - 35 * t
        pts.append((x, y))
    e.append(polylinie(pts, SCHWARZ, 1.4))
    e.append(_spitze(*pts[-1], 1, 0, SCHWARZ, 10, 7))
    e.append(text(pts[-1][0] - 6, pts[-1][1] + 18, "s", SCHWARZ, 17))
    k_max = min(range(30, 60), key=lambda i: pts[i][1])          # höchster Punkt: Tangente waagerecht
    for k, (lab, farbe) in ((8, ("dW < 0", ROT)), (22, ("dW > 0", GRUEN)), (k_max, ("dW = 0", "#555555"))):
        x, y = pts[k]
        (xa, ya), (x2, y2) = pts[k - 1], pts[k + 1]
        x2, y2 = x + (x2 - xa) / 2, y + (y2 - ya) / 2
        ux, uy = (x2 - x) / math.hypot(x2 - x, y2 - y), (y2 - y) / math.hypot(x2 - x, y2 - y)
        e.append(linie(x - ux * 14, y - uy * 14, x + ux * 14, y + uy * 14, BLAU, 3))
        e.append(kraft(x, y, 90, "F", laenge=60, ziehend=True, label_seite=1, label_pos=1.0))
        w = math.degrees(math.atan2(-uy, ux))
        e.append(winkelbogen(x, y, 24, w, 90, ""))
        e.append(text(x, y + 30, f"[{lab}]", farbe, 14, italic=False))
        e.append(text(x + 18, y + 6, "ds", BLAU, 14, anker="start"))
    e.append(text(650, 30, "W = ∫ F_s ds", "#444444", 17, anker="start"))
    return abb.speichern(ZIEL / "arbeit.svg")


# =====================================================================
# Kreuzprodukt und Moment
# =====================================================================
def kreuzprodukt():
    abb = Abbildung(700, 360, "Kreuzprodukt und Moment")
    O = (60, 240)
    wr, wf = math.radians(20), math.radians(75)
    Lr, Lf = 200, 140
    A = (O[0] + Lr * math.cos(wr), O[1] - Lr * math.sin(wr))
    Fe = (A[0] + Lf * math.cos(wf), A[1] - Lf * math.sin(wf))
    Fo = (O[0] + Lf * math.cos(wf), O[1] - Lf * math.sin(wf))

    e = abb.ebene("ebene", "r und F")
    e.append(vektor(*O, *A, "r", farbe=GRUEN, breite=1.8, ly=18))
    e.append(vektor(*A, *Fe, "F", lx=16))
    e.append(punkt(*O, 3.6))
    e.append(text(O[0] - 12, O[1] + 12, "0", SCHWARZ, 17))
    e.append(linie(A[0], A[1], A[0] + 60 * math.cos(wr), A[1] - 60 * math.sin(wr), GRAU, STRICH["duenn"], strich="4 3"))
    e.append(winkelbogen(*A, 34, 20, 75, "φ"))

    e = abb.ebene("flaeche", "Parallelogramm und Hebelarm")
    e.append(polylinie([O, A, Fe, Fo], None, fuellung="#fbe3e3", schliessen=True))
    e.append(linie(*O, *Fo, ROT, 1, strich="5 4"))
    e.append(linie(*Fo, *Fe, GRUEN, 1, strich="5 4"))
    # Hebelarm: Lot von 0 auf die Wirkungslinie von F
    u = (math.cos(wf), -math.sin(wf))
    t = (O[0] - A[0]) * u[0] + (O[1] - A[1]) * u[1]
    Fp = (A[0] + t * u[0], A[1] + t * u[1])
    e.append(linie(Fp[0] + u[0] * 30, Fp[1] + u[1] * 30, *A, GRAU, STRICH["duenn"], strich="10 4 2 4"))
    e.append(rechter_winkel(*Fp, (O[0] - Fp[0]) / math.hypot(O[0] - Fp[0], O[1] - Fp[1]),
                            (O[1] - Fp[1]) / math.hypot(O[0] - Fp[0], O[1] - Fp[1]), -u[0], -u[1]))
    e.append(linie(*O, *Fp, BLAU, 2))
    e.append(text((O[0] + Fp[0]) / 2 + 2, (O[1] + Fp[1]) / 2 + 18, "b = r sin φ", BLAU, 15, anker="start"))
    e.append(text(O[0] + 120, O[1] - 90, "[Fläche = |M|]", ROT, 14, italic=False))

    # räumliche Darstellung (schräg): x nach rechts, y nach hinten-rechts, z nach oben
    e = abb.ebene("raum", "Momentenvektor senkrecht zur Ebene")
    K = (470, 260)

    def R3(x, y, z):
        return (K[0] + x + 0.55 * y, K[1] - z - 0.35 * y)
    e.append(polylinie([R3(-40, -40, 0), R3(190, -40, 0), R3(190, 160, 0), R3(-40, 160, 0)], "#bbbbbb", 0.8,
                       "#f4f4f4", schliessen=True))
    for (x, y, z), lab in (((200, 0, 0), "x"), ((0, 180, 0), "y"), ((0, 0, 170), "z")):
        e.append(pfeil_gruen(*R3(0, 0, 0), *R3(x, y, z)))
        px, py = R3(x, y, z)
        e.append(text(px + 8, py, lab, GRUEN, 17, anker="start"))
    A3 = R3(130, 30, 0)
    e.append(vektor(*R3(0, 0, 0), *A3, "r", farbe=GRUEN, breite=1.8, ly=16))
    e.append(vektor(*A3, *R3(150, 130, 0), "F", lx=16))
    e.append(doppelpfeil(*R3(0, 0, 0), *R3(0, 0, 120)))
    e.append(text(R3(0, 0, 120)[0] - 12, R3(0, 0, 100)[1], "M = r × F", ROT, 17, anker="end"))
    e.append(moment(*R3(0, 0, 60), "", gegen_uhrzeiger=True, r=20, start=200, bogen=250))
    return abb.speichern(ZIEL / "kreuzprodukt.svg")


def pfeil_gruen(x1, y1, x2, y2):
    from tmzeichnen import pfeil
    return pfeil(x1, y1, x2, y2, GRUEN, STRICH["normal"], (8, 5))


# =====================================================================
# Feder: Verschiebung u, Kennlinie, Federarbeit, Schaltungen
# =====================================================================
def feder_grafik():
    abb = Abbildung(940, 390, "Feder und Elastizität")
    y0, l0, u = 50, 170, 60

    e = abb.ebene("feder", "Feder unbelastet und belastet")
    for x, laenge, belastet in ((90, l0, False), (230, l0 + u, True)):
        e.append(_decke(x, y0))
        e.append(feder(x, y0, y0 + laenge, windungen=7))
        e.append(platte([(x - 22, y0 + laenge), (x + 22, y0 + laenge), (x + 22, y0 + laenge + 10),
                         (x - 22, y0 + laenge + 10)], "#cfcfcf"))
        if belastet:
            e.append(kraft(x, y0 + laenge + 10, -90, "F", laenge=55, ziehend=True, label_seite=-1))
    e.append(linie(60, y0 + l0 + 10, 270, y0 + l0 + 10, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(mass(275, y0 + l0 + 10, 275, y0 + l0 + u + 10, "u", abstand=-18))
    e.append(mass(55, y0, 55, y0 + l0 + 10, "l_0", abstand=-14))
    e.append(text(90, 370, "[unbelastet]", "#555555", 13, italic=False))
    e.append(text(230, 370, "[belastet]", "#555555", 13, italic=False))

    # Kennlinie
    D = (370, 300)
    e = abb.ebene("kennlinie", "Kennlinie F = c u")
    e.append(koord_xy(*D, 220, 230, xlabel="u", ylabel="F"))
    uu, FF = 160, 190
    e.append(linie(*D, D[0] + 200, D[1] - 200 * FF / uu, ROT, 2.2))
    e.append(punkt(D[0] + uu, D[1] - FF, 3.4))
    e.append(linie(D[0] + uu, D[1] - FF, D[0] + uu, D[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(D[0] + uu, D[1] - FF, D[0], D[1] - FF, GRAU, STRICH["duenn"], strich="4 3"))
    # Steigungsdreieck
    x1, x2 = D[0] + 40, D[0] + 90
    e.append(polylinie([(x1, D[1] - 40 * FF / uu), (x2, D[1] - 40 * FF / uu), (x2, D[1] - 90 * FF / uu)],
                       GRUEN, STRICH["normal"]))
    e.append(text(x2 + 8, D[1] - 65 * FF / uu, "c", GRUEN, 17, anker="start"))
    e.append(text(D[0] + 95, D[1] - 205, "F = c u", ROT, 18, anker="end"))

    e = abb.ebene("federarbeit", "Federarbeit als Fläche")
    e.append(polylinie([D, (D[0] + uu, D[1] - FF), (D[0] + uu, D[1])], None, fuellung="#fbe3e3", schliessen=True))
    e.append(text(D[0] + 0.66 * uu, D[1] - 0.22 * FF, "W = ½ c u²", ROT, 16))

    # Parallel- und Reihenschaltung
    e = abb.ebene("schaltungen", "Parallel- und Reihenschaltung")
    xp = 700
    e.append(_decke(xp, y0, 90))
    for dx, lab in ((-25, "c_1"), (25, "c_2")):
        e.append(feder(xp + dx, y0, y0 + 160, breite=14, windungen=6))
        e.append(text(xp + dx + (-14 if dx < 0 else 14), y0 + 80, lab, SCHWARZ, 15, anker="end" if dx < 0 else "start"))
    e.append(platte([(xp - 40, y0 + 160), (xp + 40, y0 + 160), (xp + 40, y0 + 170), (xp - 40, y0 + 170)], "#cfcfcf"))
    e.append(kraft(xp, y0 + 170, -90, "F", laenge=45, ziehend=True, label_seite=-1))
    e.append(text(xp, 370, "[parallel]", "#555555", 13, italic=False))
    xr = 860
    e.append(_decke(xr, y0))
    e.append(feder(xr, y0, y0 + 90, windungen=4))
    e.append(platte([(xr - 8, y0 + 90), (xr + 8, y0 + 90), (xr + 8, y0 + 96), (xr - 8, y0 + 96)], "#cfcfcf"))
    e.append(feder(xr, y0 + 96, y0 + 186, windungen=4))
    e.append(text(xr + 16, y0 + 45, "c_1", SCHWARZ, 15, anker="start"))
    e.append(text(xr + 16, y0 + 141, "c_2", SCHWARZ, 15, anker="start"))
    e.append(platte([(xr - 22, y0 + 186), (xr + 22, y0 + 186), (xr + 22, y0 + 196), (xr - 22, y0 + 196)], "#cfcfcf"))
    e.append(kraft(xr, y0 + 196, -90, "F", laenge=45, ziehend=True, label_seite=-1))
    e.append(text(xr, 370, "[in Reihe]", "#555555", 13, italic=False))
    return abb.speichern(ZIEL / "feder.svg")


def _decke(x, y, breite=50):
    teile = [linie(x - breite / 2, y, x + breite / 2, y, SCHWARZ, STRICH["normal"])]
    xx = x - breite / 2 + 2
    while xx <= x + breite / 2:
        teile.append(linie(xx, y, xx + 7, y - 7, SCHWARZ, STRICH["duenn"]))
        xx += 6
    return gruppe(teile)


if __name__ == "__main__":
    for fn in (einheitskreis, vektoraddition, skalarprodukt, arbeit, kreuzprodukt, feder_grafik):
        print(fn())

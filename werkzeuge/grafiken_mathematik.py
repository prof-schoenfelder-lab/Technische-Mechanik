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
def vlabel(x, y, name, farbe=SCHWARZ, groesse=19, anker="middle", index=""):
    """Formelzeichen mit Vektorpfeil darüber, z. B. vlabel(..., "F") → F mit Pfeil; index wird tiefgestellt."""
    b = 0.55 * groesse                                   # ungefähre Breite des Buchstabens
    x0 = x - b / 2 if anker == "middle" else (x if anker == "start" else x - b - (0.45 * groesse if index else 0))
    yp = y - 0.62 * groesse
    teile = [text(x0, y, name + (f"_{{{index}}}" if index else ""), farbe, groesse, anker="start"),
             linie(x0 + 0.5, yp, x0 + b + 1, yp, farbe, 1.1),
             _spitze(x0 + b + 3, yp, 1, 0, farbe, 5, 4)]
    return gruppe(teile)


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
    e.append(weg(*O, *A))
    e.append(vlabel(A[0] - 30, A[1] + 26, "a"))
    e.append(weg(*O, *B))
    e.append(vlabel((O[0] + B[0]) / 2 - 22, (O[1] + B[1]) / 2, "b"))
    e.append(winkelbogen(*O, 60, 12, 58, "φ"))
    e.append(punkt(*O))

    e = abb.ebene("projektion", "Projektion von b auf a")
    e.append(linie(*B, *Bp, GRAU, STRICH["normal"], strich="4 3"))
    n = math.hypot(B[0] - Bp[0], B[1] - Bp[1])
    e.append(rechter_winkel(*Bp, -math.cos(wa), math.sin(wa), (B[0] - Bp[0]) / n, (B[1] - Bp[1]) / n))
    e.append(linie(O[0], O[1] + 1, Bp[0], Bp[1] + 1, GRUEN, 4.5))
    e.append(text((O[0] + Bp[0]) / 2, (O[1] + Bp[1]) / 2 + 24, "b cos φ", GRUEN, 17))
    return abb.speichern(ZIEL / "skalarprodukt.svg")


# =====================================================================
# Arbeit: gerader Weg, Höhe, gekrümmter Weg
# =====================================================================
def arbeit():
    abb = Abbildung(980, 345, "Arbeit einer Kraft")

    # Feld 1: gerader Weg, Kraft schräg
    e = abb.ebene("gerade", "Gerader Weg")
    O = (40, 250)
    S = (O[0] + 260, O[1] - 60)
    e.append(weg(*O, *S))
    e.append(vlabel(S[0] - 40, S[1] + 34, "s"))
    ws = math.atan2(60, 260)
    wf = ws + math.radians(50)
    F = (O[0] + 150 * math.cos(wf), O[1] - 150 * math.sin(wf))
    e.append(vektor(*O, *F))
    e.append(vlabel(F[0] - 34, F[1] + 10, "F", ROT))
    fs = 150 * math.cos(wf - ws)
    Fs = (O[0] + fs * math.cos(ws), O[1] - fs * math.sin(ws))
    e.append(linie(*F, *Fs, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(vektor(O[0], O[1] + 1, Fs[0], Fs[1] + 1, "F_s", farbe=ROT, gestrichelt=True, breite=1.6, ly=22))
    e.append(winkelbogen(*O, 50, math.degrees(ws), math.degrees(wf), "φ"))
    e.append(punkt(*O))
    e.append(text(30, 30, "W = F_s s", "#444444", 17, anker="start"))

    # Feld 2: Kraft senkrecht, Komponente des Weges in Kraftrichtung = Höhe
    e = abb.ebene("hoehe", "Weg in Kraftrichtung: Höhe")
    O2 = (370, 260)
    S2 = (O2[0] + 230, O2[1] - 130)
    e.append(weg(*O2, *S2))
    e.append(vlabel(S2[0] - 40, S2[1] + 44, "s"))
    e.append(vektor(O2[0], O2[1], O2[0], O2[1] - 110))
    e.append(vlabel(O2[0] + 20, O2[1] - 80, "F", ROT, anker="start"))
    e.append(linie(S2[0], S2[1], O2[0] - 20, S2[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(O2[0] - 12, O2[1], O2[0] - 12, S2[1], GRUEN, 4))
    e.append(text(O2[0] - 20, (O2[1] + S2[1]) / 2, "s_F = h", GRUEN, 16, anker="end"))
    e.append(winkelbogen(*O2, 40, math.degrees(math.atan2(130, 230)), 90, "φ"))
    e.append(punkt(*O2))
    e.append(koord_xy(O2[0] + 150, O2[1] + 50, 34, 34))
    e.append(text(360, 30, "W = F s_F", "#444444", 17, anker="start"))

    # Feld 3: gekrümmter Weg: erst fallend, dann steigend, dann waagerecht
    e = abb.ebene("kurve", "Gekrümmter Weg")
    x0, breite = 650, 300

    def kurve(t):                       # t in [0, 1.3]; ab t = 1 waagerecht
        tt = min(t, 1.0)
        return x0 + breite * t / 1.3, 175 + 60 * math.sin(1.5 * math.pi * tt)

    def tangente(t):
        tt = min(t, 1.0)
        dx = breite / 1.3
        dy = 60 * 1.5 * math.pi * math.cos(1.5 * math.pi * tt) if t < 1.0 else 0.0
        n = math.hypot(dx, dy)
        return dx / n, dy / n

    pts = [kurve(1.3 * i / 80) for i in range(81)]
    e.append(polylinie(pts, SCHWARZ, 1.4))
    e.append(_spitze(*pts[-1], 1, 0, SCHWARZ, 10, 7))
    e.append(text(pts[-1][0] + 4, pts[-1][1] + 20, "s", SCHWARZ, 17))
    for t, lab, farbe in ((0.12, "dW < 0", ROT), (0.55, "dW > 0", GRUEN), (1.15, "dW = 0", "#555555")):
        x, y = kurve(t)
        ux, uy = tangente(t)
        e.append(vektor(x, y, x + 46 * ux, y + 46 * uy, "", farbe=BLAU, breite=2))       # ds
        e.append(vektor(x, y, x, y - 62))                                                   # F
        e.append(vlabel(x - 6, y - 70, "F", ROT, 17, anker="end"))
        e.append(vlabel(x + 46 * ux + 4, y + 46 * uy + 14, "ds", BLAU, 15, anker="start"))
        w = math.degrees(math.atan2(-uy, ux))
        e.append(winkelbogen(x, y, 22, w, 90, ""))
        e.append(text(x - 4, y + 32, f"[{lab}]", farbe, 14, italic=False))
        e.append(punkt(x, y, 2.6))
    e.append(text(650, 30, "W = ∫ F_s ds", "#444444", 17, anker="start"))
    return abb.speichern(ZIEL / "arbeit.svg")


# =====================================================================
# Moment in der Ebene
# =====================================================================
def moment_ebene():
    abb = Abbildung(470, 340, "Moment einer Kraft in der Ebene")
    O = (70, 250)
    wr, wf = math.radians(20), math.radians(75)
    Lr, Lf = 210, 140
    A = (O[0] + Lr * math.cos(wr), O[1] - Lr * math.sin(wr))
    Fe = (A[0] + Lf * math.cos(wf), A[1] - Lf * math.sin(wf))
    Fo = (O[0] + Lf * math.cos(wf), O[1] - Lf * math.sin(wf))

    e = abb.ebene("ebene", "r und F")
    e.append(vektor(*O, *A, farbe=GRUEN, breite=1.8))
    e.append(vlabel((O[0] + A[0]) / 2 + 6, (O[1] + A[1]) / 2 + 24, "r", GRUEN))
    e.append(vektor(*A, *Fe))
    e.append(vlabel(Fe[0] + 10, Fe[1] + 30, "F", ROT, anker="start"))
    e.append(punkt(*O, 3.6))
    e.append(text(O[0] - 12, O[1] + 12, "0", SCHWARZ, 17))
    e.append(text(A[0] + 12, A[1] + 14, "A", SCHWARZ, 16, anker="start"))
    e.append(linie(A[0], A[1], A[0] + 60 * math.cos(wr), A[1] - 60 * math.sin(wr), GRAU, STRICH["duenn"], strich="4 3"))
    e.append(winkelbogen(*A, 34, 20, 75, "φ"))

    e = abb.ebene("flaeche", "Parallelogramm und Hebelarm")
    e.append(polylinie([O, A, Fe, Fo], None, fuellung="#fbe3e3", schliessen=True))
    e.append(linie(*O, *Fo, ROT, 1, strich="5 4"))
    e.append(linie(*Fo, *Fe, GRUEN, 1, strich="5 4"))
    u = (math.cos(wf), -math.sin(wf))
    t = (O[0] - A[0]) * u[0] + (O[1] - A[1]) * u[1]
    Fp = (A[0] + t * u[0], A[1] + t * u[1])
    e.append(linie(Fp[0] + u[0] * 30, Fp[1] + u[1] * 30, *A, GRAU, STRICH["duenn"], strich="10 4 2 4"))
    n = math.hypot(O[0] - Fp[0], O[1] - Fp[1])
    e.append(rechter_winkel(*Fp, (O[0] - Fp[0]) / n, (O[1] - Fp[1]) / n, -u[0], -u[1]))
    e.append(linie(*O, *Fp, BLAU, 2))
    e.append(text((O[0] + Fp[0]) / 2 + 2, (O[1] + Fp[1]) / 2 + 18, "b = r sin φ", BLAU, 15, anker="start"))
    e.append(text(O[0] + 120, O[1] - 95, "[Fläche = |M|]", ROT, 14, italic=False))

    e = abb.ebene("komponenten", "Komponenten und ihre Hebelarme")
    e.append(koord_xy(*O, 300, 230, negativ=20, negativ_y=20))
    e.append(vektor(*A, A[0] + Lf * math.cos(wf), A[1], "F_x", gestrichelt=True, breite=1.5, ly=18))
    e.append(vektor(*A, A[0], A[1] - Lf * math.sin(wf), "F_y", gestrichelt=True, breite=1.5, lx=-20))
    e.append(linie(A[0], A[1], A[0], O[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(A[0], A[1], O[0], A[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(mass(O[0], O[1], A[0], O[1], "x", abstand=-26))
    e.append(mass(O[0], O[1], O[0], A[1], "y", abstand=-26))
    return abb.speichern(ZIEL / "moment.svg")


# =====================================================================
# Feder: Verschiebung u, Kennlinie, Federarbeit
# =====================================================================
def feder_grafik():
    abb = Abbildung(640, 390, "Feder und Elastizität")
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

    D = (370, 300)
    e = abb.ebene("kennlinie", "Kennlinie F = c u")
    e.append(koord_xy(*D, 220, 230, xlabel="u", ylabel="F"))
    uu, FF = 160, 190
    e.append(linie(*D, D[0] + 200, D[1] - 200 * FF / uu, ROT, 2.2))
    e.append(punkt(D[0] + uu, D[1] - FF, 3.4))
    e.append(linie(D[0] + uu, D[1] - FF, D[0] + uu, D[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(D[0] + uu, D[1] - FF, D[0], D[1] - FF, GRAU, STRICH["duenn"], strich="4 3"))
    x1, x2 = D[0] + 40, D[0] + 90
    e.append(polylinie([(x1, D[1] - 40 * FF / uu), (x2, D[1] - 40 * FF / uu), (x2, D[1] - 90 * FF / uu)],
                       GRUEN, STRICH["normal"]))
    e.append(text(x2 + 8, D[1] - 65 * FF / uu, "c", GRUEN, 17, anker="start"))
    e.append(text(D[0] + 95, D[1] - 205, "F = c u", ROT, 18, anker="end"))

    e = abb.ebene("federarbeit", "Federarbeit als Fläche")
    e.append(polylinie([D, (D[0] + uu, D[1] - FF), (D[0] + uu, D[1])], None, fuellung="#fbe3e3", schliessen=True))
    e.append(text(D[0] + 0.66 * uu, D[1] - 0.22 * FF, "W = ½ c u²", ROT, 16))
    return abb.speichern(ZIEL / "feder.svg")


def _decke(x, y, breite=50):
    teile = [linie(x - breite / 2, y, x + breite / 2, y, SCHWARZ, STRICH["normal"])]
    xx = x - breite / 2 + 2
    while xx <= x + breite / 2:
        teile.append(linie(xx, y, xx + 7, y - 7, SCHWARZ, STRICH["duenn"]))
        xx += 6
    return gruppe(teile)


# =====================================================================
# Von der Feder zum elastischen Körper: Stab, starrer und elastischer Balken
# =====================================================================
def elastischer_koerper():
    abb = Abbildung(800, 440, "Von der Feder zum elastischen Körper")
    from tmzeichnen import balken, festlager, loslager

    # Stab unter Zug: wie eine Feder
    e = abb.ebene("stab", "Zugstab")
    y0, L, u = 50, 190, 32
    for x, laenge, belastet in ((80, L, False), (190, L + u, True)):
        e.append(_decke(x, y0, 44))
        e.append(balken(x, y0, x, y0 + laenge, dicke=12))
        if belastet:
            e.append(kraft(x, y0 + laenge, -90, "F", laenge=55, ziehend=True, label_seite=-1))
    e.append(linie(60, y0 + L, 215, y0 + L, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(mass(222, y0 + L, 222, y0 + L + u, "u", abstand=-16))
    e.append(mass(52, y0, 52, y0 + L, "l", abstand=-12))
    e.append(text(80, y0 + L + 30, "E, A", GRUEN, 16))
    e.append(text(135, 400, "c = EA/l", SCHWARZ, 18))

    xa, Lb, a = 350, 380, 0.375
    xf = xa + a * Lb
    # starrer Balken
    e = abb.ebene("starr", "Starrer Balken")
    yb = 110
    e.append(balken(xa, yb, xa + Lb, yb))
    e.append(festlager(xa, yb + 3.5, label="A", label_pos=(-22, 10)))
    e.append(loslager(xa + Lb, yb + 3.5, label="B", label_pos=(22, 10)))
    e.append(kraft(xf, yb - 3.5, -90, "F", laenge=55, label_seite=-1))
    e.append(text(xa + Lb + 30, yb - 40, "[starr]", "#555555", 14, anker="end", italic=False))

    e = abb.ebene("reaktionen-starr", "Lagerkräfte am starren Balken")
    e.append(kraft(xa, yb + 26, 90, "F_A", laenge=0.625 * 80, label_seite=1, farbe=ROT))
    e.append(kraft(xa + Lb, yb + 26, 90, "F_B", laenge=0.375 * 80, label_seite=-1, farbe=ROT))

    # elastischer Balken (Durchbiegung stark überhöht)
    e = abb.ebene("elastisch", "Elastischer Balken")
    yb2 = 290
    b = 1 - a
    def w(xi):                                   # Biegelinie Einfeldträger mit Einzellast, normiert
        if xi <= a:
            return b * xi * (1 - b * b - xi * xi)
        return a * (1 - xi) * (1 - a * a - (1 - xi) ** 2)
    wmax = max(w(i / 200) for i in range(201))
    pts = [(xa + Lb * i / 120, yb2 + 30 * w(i / 120) / wmax) for i in range(121)]
    e.append(linie(xa, yb2, xa + Lb, yb2, GRAU, STRICH["duenn"], strich="6 4"))
    e.append(polylinie(pts, SCHWARZ, 9))
    e.append(polylinie(pts, "#e6e6e6", 6.5))
    e.append(festlager(xa, yb2 + 3.5, label="A", label_pos=(-22, 10)))
    e.append(loslager(xa + Lb, yb2 + 3.5, label="B", label_pos=(22, 10)))
    yF = yb2 + 30 * w(a) / wmax
    e.append(kraft(xf, yF - 3.5, -90, "F", laenge=55, label_seite=-1))
    e.append(mass(xf + 40, yb2, xf + 40, yF, "w", abstand=-12))
    e.append(text(xa + Lb + 30, yb2 - 40, "[elastisch (Durchbiegung überhöht)]", "#555555", 14, anker="end",
                  italic=False))

    e = abb.ebene("reaktionen-elastisch", "Lagerkräfte am elastischen Balken")
    e.append(kraft(xa, yb2 + 26, 90, "F_A", laenge=0.625 * 80, label_seite=1, farbe=ROT))
    e.append(kraft(xa + Lb, yb2 + 26, 90, "F_B", laenge=0.375 * 80, label_seite=-1, farbe=ROT))
    e.append(mass(xa, yb2 + 110, xf, yb2 + 110, "a", abstand=12))
    e.append(mass(xa, yb2 + 110, xa + Lb, yb2 + 110, "L", abstand=-14))
    return abb.speichern(ZIEL / "elastischer-koerper.svg")


if __name__ == "__main__":
    for fn in (einheitskreis, vektoraddition, skalarprodukt, arbeit, moment_ebene, feder_grafik,
               elastischer_koerper):
        print(fn())

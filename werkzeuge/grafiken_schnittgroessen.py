"""Grafiken zum Kapitel Schnittgrößen.

Aufruf:  python werkzeuge/grafiken_schnittgroessen.py
Ergebnis: grafiken/schnittgroessen/*.svg (Inkscape-Ebenen = Scroll-Schritte)
"""

import math
from pathlib import Path

from tmzeichnen import (FARBE, Abbildung, balken, einspannung, festlager, gelenk, koordinaten, kraft,
                        linie, loslager, mass, moment, nummer, pfeil, polylinie, schnittlinie, schnittufer,
                        streckenlast, text, verlauf, winkelbogen)

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "schnittgroessen"
R, B_ = FARBE["reaktion"], FARBE["last"]


# =====================================================================
# Vorzeichenkonvention: positives / negatives Schnittufer
# =====================================================================
def vorzeichen():
    abb = Abbildung(620, 330, "Vorzeichenkonvention der Schnittgrößen")
    y, t = 90, 3.5
    x0, xs, x1 = 70, 300, 540

    e = abb.ebene("ganz", "Balken mit Schnitt")
    e.append(balken(x0, y, x1, y))
    e.append(koordinaten(x0, y, 40, "x", "z"))
    e.append(schnittlinie(xs, y, 46))
    e.append(text(xs + 10, y - 30, "S", "#000000", 15))

    yt = 230
    d = 170
    e = abb.ebene("getrennt", "Teilsysteme")
    e.append(balken(x0, yt, xs - d / 2, yt))
    e.append(balken(xs + d / 2, yt, x1, yt))
    e.append(text((x0 + xs) / 2 - 30, yt + 34, "[linkes Teilsystem]", "#444444", 14, italic=False))
    e.append(text((xs + x1) / 2 + 30, yt + 34, "[rechtes Teilsystem]", "#444444", 14, italic=False))

    e = abb.ebene("ufer-pos", "positives Schnittufer")
    e.append(schnittufer(xs - d / 2, yt, positiv=True, N="N(x)", Q="Q(x)", M="M(x)"))
    e.append(pfeil(xs - d / 2 - 70, yt - 72, xs - d / 2 - 4, yt - 8, "#444444", 0.9, (7, 5)))
    e.append(text(xs - d / 2 - 74, yt - 82, "[positives Schnittufer]", "#444444", 14, anker="end", italic=False))

    e = abb.ebene("ufer-neg", "negatives Schnittufer")
    e.append(schnittufer(xs + d / 2, yt, positiv=False, N="N(x)", Q="Q(x)", M="M(x)"))
    e.append(pfeil(xs + d / 2 + 70, yt - 72, xs + d / 2 + 4, yt - 8, "#444444", 0.9, (7, 5)))
    e.append(text(xs + d / 2 + 74, yt - 82, "[negatives Schnittufer]", "#444444", 14, anker="start", italic=False))

    return abb.speichern(ZIEL / "vorzeichen.svg")


# =====================================================================
# Beispiel 1 (Vorlesung 2013): Träger mit Kragarm, Einzelkräfte F1, F2
#   a = 1 m, F1 = 2000 N unter α = 30°, F2 = 500 N
# =====================================================================
def beispiel_einzelkraefte():
    a = 110                      # px je a
    xA, y = 110, 120             # Lager A, Balkenachse
    xF1, xB, xE = xA + a, xA + 3 * a, xA + 4 * a
    t = 3.5                      # halbe Balkendicke
    alpha = 30

    F1, F2 = 2000.0, 500.0
    FAH = F1 * math.cos(math.radians(alpha))
    FB = (F1 * math.sin(math.radians(alpha)) + 4 * F2) / 3
    FAV = F1 * math.sin(math.radians(alpha)) + F2 - FB

    abb = Abbildung(790, 610, "Träger mit Kragarm – Schnittgrößen")

    # --- System
    e = abb.ebene("traeger", "Träger und Bemaßung")
    e.append(balken(xA, y, xE, y))
    e.append(mass(xA, y, xF1, y, "a", abstand=-62))
    e.append(mass(xF1, y, xB, y, "2a", abstand=-62))
    e.append(mass(xB, y, xE, y, "a", abstand=-62))

    e = abb.ebene("lasten", "Lasten")
    e.append(kraft(xF1, y - t, 180 + alpha, "F_1", laenge=62, label_seite=1))
    e.append(winkelbogen(xF1, y - t, 30, 0, alpha, "α"))
    e.append(linie(xF1, y - t, xF1 + 44, y - t, FARBE["hinweis"], 0.6, strich="3 2"))
    e.append(kraft(xE, y - t, -90, "F_2", laenge=55, label_seite=-1))

    e = abb.ebene("lager", "Lager")
    e.append(festlager(xA, y + t, label="A", label_pos=(-26, 22)))
    e.append(loslager(xB, y + t, label="B", label_pos=(26, 22)))

    # --- Freikörperbild: Lager durch Reaktionen ersetzt
    e = abb.ebene("reaktionen", "Lagerreaktionen")
    e.append(kraft(xA - 4, y, 0, "F_{AH}", farbe=R, laenge=48, label_seite=1))
    e.append(kraft(xA, y + t, 90, "F_{AV}", farbe=R, laenge=48, label_seite=1))
    e.append(kraft(xB, y + t, 90, "F_B", farbe=R, laenge=48, label_seite=-1))

    # --- Bereiche und lokale Koordinaten
    e = abb.ebene("bereiche", "Bereiche")
    for xs in (xF1, xB):
        e.append(linie(xs, y - 75, xs, y + 30, FARBE["hinweis"], 0.8, strich="4 3"))
    for i, (x0, x1) in enumerate(((xA, xF1), (xF1, xB), (xB, xE)), 1):
        e.append(nummer((x0 + x1) / 2 + (12 if i == 1 else 0), y - 62, ["I", "II", "III"][i - 1]))
        e.append(koordinaten(x0, y, 30, f"x_{i}", nur_x=True))

    # --- Schnitte (Teilsysteme unterhalb)
    yt = 300

    def links(xs, mit_F1, i, deckkraft=1.0):
        g = [balken(xA, yt, xs, yt),
             kraft(xA - 4, yt, 0, "F_{AH}", farbe=R, laenge=40),
             kraft(xA, yt + t, 90, "F_{AV}", farbe=R, laenge=40)]
        if mit_F1:
            g.append(kraft(xF1, yt - t, 180 + alpha, "F_1", laenge=55, label_seite=1))
        if xs > xB:
            g.append(kraft(xB, yt + t, 90, "F_B", farbe=R, laenge=40, label_seite=-1))
        g.append(schnittufer(xs, yt, positiv=True, N=f"N(x_{i})", Q=f"Q(x_{i})", M=f"M(x_{i})"))
        return f'<g opacity="{deckkraft}">' + "".join(g) + "</g>"

    def rechts(xs, i, deckkraft=1.0):
        d = 200  # Versatz des rechten Teils
        g = [balken(xs + d, yt, xE + d, yt),
             kraft(xE + d, yt - t, -90, "F_2", laenge=45, label_seite=-1)]
        if xs < xB:
            g.append(kraft(xB + d, yt + t, 90, "F_B", farbe=R, laenge=40, label_seite=-1))
        if xs < xF1:
            g.append(kraft(xF1 + d, yt - t, 180 + alpha, "F_1", laenge=55, label_seite=1))
        g.append(schnittufer(xs + d, yt, positiv=False, N=f"N(x_{i})", Q=f"Q(x_{i})", M=f"M(x_{i})"))
        return f'<g opacity="{deckkraft}">' + "".join(g) + "</g>"

    for i, (xs, l_aktiv) in enumerate(((xA + 0.55 * a, True), (xF1 + 1.0 * a, True), (xB + 0.5 * a, False)), 1):
        e = abb.ebene(f"schnitt-{i}", f"Schnitt Bereich {['I', 'II', 'III'][i - 1]}")
        e.append(schnittlinie(xs, y, 40))
        e.append(text(xs + 2, y - 30, "S", "#000000", 15))
        e.append(links(xs, xs > xF1, i, 1.0 if l_aktiv else 0.35))
        e.append(rechts(xs, i, 0.35 if l_aktiv else 1.0))
        e.append(text(xA - 50, yt - 58, "[linkes Teilsystem]" if l_aktiv else "[rechtes Teilsystem]",
                      "#444444", 14, anker="start", italic=False))

    # --- Verläufe (positive Werte oberhalb der Achse, wie Vorlesung 2013)
    def P(xi_list):
        return [(xi - xA, v) for xi, v in xi_list]

    yN, yQ, yM = 280, 400, 520
    sN, sQ, sM = 36 / 1732, 34 / 500, 40 / 500

    e = abb.ebene("verlauf-N", "Normalkraftverlauf")
    e.append(verlauf(xA, P([(xA, -FAH), (xF1, -FAH), (xF1, 0), (xE, 0)]), sN, yN, 4 * a, "N(x)",
                     werte=[(a / 2, -FAH, "−1732 N", "middle")]))
    e = abb.ebene("verlauf-Q", "Querkraftverlauf")
    e.append(verlauf(xA, P([(xA, FAV), (xF1, FAV), (xF1, FAV - 1000), (xB, FAV - 1000), (xB, F2), (xE, F2), (xE, 0)]),
                     sQ, yQ, 4 * a, "Q(x)",
                     werte=[(a / 2, FAV, "500 N", "middle"), (2 * a, -500, "−500 N", "middle"),
                            (3.5 * a, F2, "500 N", "middle")]))
    e = abb.ebene("verlauf-M", "Momentenverlauf")
    e.append(verlauf(xA, P([(xA, 0), (xF1, FAV * 1), (xB, FAV * 3 - 1000 * 2), (xE, 0)]), sM, yM, 4 * a, "M(x)",
                     werte=[(a, 500, "500 Nm", "middle"), (3 * a, -500, "−500 Nm", "middle")]))

    e = abb.ebene("bezug", "Bezug Last – Verlauf")
    for xs, txt in ((xF1, "F_1 sin α"), (xB, "F_B"), (xE, "F_2")):
        e.append(linie(xs, y + 30, xs, yM + 50, FARBE["hinweis"], 0.8, strich="4 3"))
    e.append(text(xF1 + 8, yQ - 14, "[Sprung = ]F_1[ sin ]α", FARBE["last"], 14, anker="start"))
    e.append(text(xB - 8, yQ + 14, "[Sprung = ]F_B", R, 14, anker="end"))
    e.append(text(xF1 - 30, yM - 54, "[Knick]", FARBE["last"], 14, anker="end"))
    e.append(text(xB + 8, yM + 30, "[Knick]", FARBE["last"], 14, anker="start"))
    e.append(text(xF1 + 8, yN - 14, "[Sprung = ]F_1[ cos ]α", FARBE["last"], 14, anker="start"))

    return abb.speichern(ZIEL / "traeger-einzelkraefte.svg")


# =====================================================================
# Beispiel 2 (Vorlesung 2013): Einfeldträger mit Dreieckslast q(x)=q0 x/L
# =====================================================================
def beispiel_dreieckslast():
    L = 440
    xA, y, xB = 120, 150, 560
    t = 3.5
    abb = Abbildung(680, 640, "Einfeldträger mit Dreieckslast – Differentialbeziehungen")

    e = abb.ebene("system", "System")
    e.append(balken(xA, y, xB, y))
    e.append(festlager(xA, y + t, label="A", label_pos=(-22, 6)))
    e.append(loslager(xB, y + t, label="B", label_pos=(22, 6)))
    e.append(mass(xA, y, xB, y, "L", abstand=-55))
    e.append(koordinaten(xA, y, 34, "x", "z"))

    e = abb.ebene("last", "Streckenlast")
    e.append(streckenlast(xA, xB, y - t, 0, 70, "q_0", n=22))
    e.append(text(xA + 0.55 * L, y - t - 52, "q(x)", FARBE["last"], 16))

    # Element dx
    e = abb.ebene("element", "Element dx")
    xe = xA + 0.42 * L
    xel = xe + 11 - 90           # Element vergrößert, mittig unter dem Streifen dx
    ye = 330
    w = 180
    e.append(linie(xe, y - 40, xe, y + 40, "#000", 1, strich="4 3"))
    e.append(linie(xe + 22, y - 40, xe + 22, y + 40, "#000", 1, strich="4 3"))
    e.append(text(xe + 11, y + 22, "[d]x", "#000", 15))
    e.append(balken(xel, ye, xel + w, ye, dicke=24))
    e.append(streckenlast(xel + 34, xel + w - 34, ye - 12, 30, 34, "q", n=6))
    e.append(mass(xel, ye, xel + w, ye, "[d]x", abstand=-48))
    e.append(schnittufer(xel + w, ye, positiv=True, N="", Q="Q(x) + [d]Q", M="M(x) + [d]M", zeige=("Q", "M"), laenge=56))
    e.append(schnittufer(xel, ye, positiv=False, N="", Q="Q(x)", M="M(x)", zeige=("Q", "M"), laenge=56))

    # Verläufe
    n = 60
    xs = [i / n for i in range(n + 1)]
    Q = [(xi * L, 1 / 6 - xi ** 2 / 2) for xi in xs]
    M = [(xi * L, xi / 6 - xi ** 3 / 6) for xi in xs]
    yQ, yM = 330, 500
    e = abb.ebene("verlauf-Q", "Querkraftverlauf")
    e.append(verlauf(xA, Q, 150, yQ, L, "Q(x)",
                     werte=[(0, 1 / 6, "q_0L/6", "start"), (L, -1 / 3, "−q_0L/3", "end")]))
    e = abb.ebene("verlauf-M", "Momentenverlauf")
    x0 = 1 / math.sqrt(3)
    e.append(verlauf(xA, M, 1000, yM, L, "M(x)",
                     werte=[(x0 * L, x0 / 6 - x0 ** 3 / 6, "M_{max} = q_0L^2/(9√3)", "middle")]))

    e = abb.ebene("extremum", "Q = 0 ⇒ M extremal")
    xp = xA + x0 * L
    e.append(linie(xp, yQ - 40, xp, yM - 80, FARBE["hinweis"], 0.9, strich="4 3"))
    e.append(text(xp + 6, yQ + 18, "Q[ = 0]", FARBE["verlauf"], 14, anker="start"))
    e.append(text(xp + 6, yQ + 36, "x_0[ = ]L/√[3]", FARBE["verlauf"], 14, anker="start"))
    # waagerechte Tangente am Maximum
    ym = yM - (x0 / 6 - x0 ** 3 / 6) * 1000
    e.append(linie(xp - 70, ym, xp + 70, ym, FARBE["last"], 1.4))
    # Tangente bei x = 0 (Steigung Q(0) = q0L/6)
    steigung = (1 / 6) * 1000 / L      # dM/dx = Q(0) = q0L/6, umgerechnet in px/px
    e.append(linie(xA, yM, xA + 90, yM - 90 * steigung, FARBE["last"], 1.4))

    return abb.speichern(ZIEL / "einfeldtraeger-dreieckslast.svg")


# =====================================================================
# Seminaraufgaben (nach Götz, Aufgaben zur TM, Abschn. 1.5), im eigenen Stil
# =====================================================================
def _aufgabe(name, breite, hoehe):
    abb = Abbildung(breite, hoehe, name)
    return abb, abb.ebene("system", "System")


def aufgabe_1_5_1():
    abb, e = _aufgabe("Aufgabe 1.5.1", 500, 170)
    l, xA, y, t = 110, 70, 60, 3.5
    xF, xB = xA + 2 * l, xA + 3 * l
    e.append(balken(xA, y, xB, y))
    e.append(mass(xA, y, xF, y, "2l", abstand=-62))
    e.append(mass(xF, y, xB, y, "l", abstand=-62))
    e.append(festlager(xA, y + t, label="A", label_pos=(-20, 6)))
    e.append(loslager(xB, y + t, label="B", label_pos=(20, 6)))
    e.append(kraft(xF, y - t, -90, "F", laenge=45, label_seite=1))
    e.append(kraft(xF + 2, y, 180, "F", laenge=50, label_seite=1, label_abstand=16))
    return abb.speichern(ZIEL / "aufgabe-1-5-1.svg")


def aufgabe_1_5_3():
    abb, e = _aufgabe("Aufgabe 1.5.3", 500, 240)
    l, xA, y, t = 100, 80, 70, 3.5
    xC, xE = xA + 2 * l, xA + 3 * l
    e.append(balken(xA, y, xE, y))
    e.append(balken(xC, y, xC, y + 95, dicke=6))
    e.append(mass(xA, y, xC, y, "2l", abstand=-50))
    e.append(mass(xC, y, xE, y, "l", abstand=-50))
    e.append(festlager(xA - 3.2, y, drehung=90, label="A", label_pos=(-10, -24)))
    e.append(gelenk(xC, y))
    e.append(festlager(xC, y + 95, label="B", label_pos=(22, 8)))
    e.append(text(xC - 14, y - 14, "C"))
    e.append(kraft(xE, y - t, 240, "F", laenge=55, label_seite=-1))
    e.append(linie(xE, y - t, xE + 45, y - t, FARBE["hinweis"], 0.6, strich="3 2"))
    e.append(winkelbogen(xE, y - t, 26, 0, 60, "α"))
    return abb.speichern(ZIEL / "aufgabe-1-5-3.svg")


def aufgabe_1_5_5():
    abb, e = _aufgabe("Aufgabe 1.5.5", 520, 170)
    l, xA, y, t = 90, 60, 70, 3.5
    xM, xG, xF, xC = xA + l, xA + 2 * l, xA + 3 * l, xA + 4 * l
    e.append(balken(xA, y, xG, y))
    e.append(balken(xG, y, xC, y))
    e.append(einspannung(xA, y, label="A"))
    e.append(gelenk(xG, y))
    e.append(text(xG, y - 18, "G"))
    e.append(moment(xM, y, "", gegen_uhrzeiger=False, r=17, start=200, bogen=250))
    e.append(text(xM - 4, y - 32, "M_B", FARBE["last"]))
    e.append(kraft(xF, y - t, 210, "F", laenge=58, label_seite=-1))
    e.append(linie(xF, y - t, xF + 45, y - t, FARBE["hinweis"], 0.6, strich="3 2"))
    e.append(winkelbogen(xF, y - t, 30, 0, 30, "α"))
    e.append(loslager(xC, y + t, label="C", label_pos=(20, 6)))
    for i in range(4):
        e.append(mass(xA + i * l, y, xA + (i + 1) * l, y, "l", abstand=-60))
    return abb.speichern(ZIEL / "aufgabe-1-5-5.svg")


def aufgabe_1_5_6():
    abb, e = _aufgabe("Aufgabe 1.5.6", 460, 190)
    a, xA, y, t = 100, 60, 80, 3.5
    xF, xE = xA + 2 * a, xA + 3 * a
    e.append(balken(xA, y, xE, y))
    e.append(mass(xA, y, xF, y, "2a", abstand=-62))
    e.append(mass(xF, y, xE, y, "a", abstand=-62))
    e.append(einspannung(xA, y, label="A"))
    e.append(streckenlast(xA, xE, y - t, 32, label="q", n=16))
    e.append(kraft(xF, y + t, 90, "F", laenge=45, label_seite=-1))
    return abb.speichern(ZIEL / "aufgabe-1-5-6.svg")


def aufgabe_1_5_8():
    abb, e = _aufgabe("Aufgabe 1.5.8", 420, 160)
    a, xE, y = 300, 60, 80
    xA = xE + a
    e.append(balken(xE, y, xA, y))
    e.append(mass(xE, y, xA, y, "a", abstand=-40))
    e.append(einspannung(xA, y, seite="rechts", label="A"))
    e.append(streckenlast(xE, xA, y - 3.5, 0, 50, "q_0", n=15))
    return abb.speichern(ZIEL / "aufgabe-1-5-8.svg")


if __name__ == "__main__":
    for fn in (vorzeichen, beispiel_einzelkraefte, beispiel_dreieckslast, aufgabe_1_5_1, aufgabe_1_5_3,
               aufgabe_1_5_5, aufgabe_1_5_6, aufgabe_1_5_8):
        print(fn())

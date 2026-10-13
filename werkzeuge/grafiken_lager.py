"""Grafiken zu Woche 2: Arten der Kräfte, Lager, statische Bestimmtheit, Lagerreaktionen,
Streckenlasten, Systeme mit Gelenk, Aufgaben.

Aufruf:  python werkzeuge/grafiken_lager.py
Ergebnis: grafiken/lager/*.svg (Inkscape-Ebenen = Scroll-Schritte)

Koordinaten wie in Woche 1: x nach rechts, y nach oben; Momente gegen den Uhrzeigersinn positiv.
"""

import math
from pathlib import Path

from grafiken_grundlagen import GRAU, GRUEN, ROT, hinweis, kasten, koord_xy, platte, punkt, strichpunkt, vektor
from tmzeichnen import (FARBE, STRICH, Abbildung, balken, einspannung, festlager, gelenk, gruppe, kraft, kreis,
                        linie, loslager, mass, moment, pfeil, polylinie, schnitt, streckenlast, text)

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "lager"
SCHWARZ = "#000000"
T = 3.5                                         # halbe Balkendicke (balken dicke=7)


def titel(e, ox, oy, s, groesse=19):
    e.append(text(ox + 20, oy + 26, f"[{s}]", SCHWARZ, groesse, anker="start", italic=False))


def rahmen(e, ox, oy, b, h):
    e.append(polylinie([(ox + 4, oy + 4), (ox + b - 4, oy + 4), (ox + b - 4, oy + h - 4), (ox + 4, oy + h - 4)],
                       "#c8c8c8", 1.0, "none", schliessen=True))


def boden(e, x0, x1, y):
    e.append(linie(x0, y, x1, y, SCHWARZ, STRICH["normal"]))
    xx = x0 + 2
    while xx < x1:
        e.append(linie(xx, y, xx - 7, y + 7, SCHWARZ, STRICH["duenn"]))
        xx += 7


def pendelstab(x1, y1, x2, y2):
    return gruppe([balken(x1, y1, x2, y2, dicke=6), gelenk(x1, y1), gelenk(x2, y2)])


def gleich(e, x, y, s="⇒"):
    e.append(text(x, y, f"[{s}]", SCHWARZ, 28, italic=False))


# =====================================================================
# 1  Arten der Kräfte
# =====================================================================
def _kraftart(e, nr, ox, oy):
    W = 420
    if nr == 1:
        titel(e, ox, oy, "Einzelkraft F in N")
        y = oy + 160
        e.append(balken(ox + 60, y, ox + 360, y))
        e.append(festlager(ox + 60, y + T))
        e.append(loslager(ox + 360, y + T))
        e.append(platte([(ox + 190, y - T - 120), (ox + 230, y - T - 120), (ox + 230, y - T - 66), (ox + 190, y - T - 66)],
                        "#d9d9d9"))
        e.append(kraft(ox + 210, y - T, -90, "F", laenge=60, label_seite=-1, label_pos=0.5))
        e.append(hinweis(ox + W / 2, oy + 235, "z. B. Stütze auf Träger: Last in einem Punkt", anker="middle", groesse=15))
    elif nr == 2:
        titel(e, ox, oy, "Linienlast (Streckenlast) q in N/m")
        y = oy + 160
        e.append(balken(ox + 60, y, ox + 360, y))
        e.append(festlager(ox + 60, y + T))
        e.append(loslager(ox + 360, y + T))
        e.append(streckenlast(ox + 60, ox + 360, y - T, 40, label="q", n=15))
        e.append(hinweis(ox + W / 2, oy + 235, "z. B. Wand auf Decke, Eigengewicht des Trägers", anker="middle", groesse=15))
    elif nr == 3:
        titel(e, ox, oy, "Flächenlast p in N/m²")
        def P(x, y):                               # schräge Ansicht einer Platte
            return (ox + 70 + x + 0.55 * y, oy + 190 - 0.38 * y)
        e.append(polylinie([P(0, 0), P(240, 0), P(240, 160), P(0, 160)], SCHWARZ, STRICH["normal"], "#e6e6e6",
                           schliessen=True))
        e.append(polylinie([P(0, 0), P(240, 0), (P(240, 0)[0], P(240, 0)[1] + 12), (P(0, 0)[0], P(0, 0)[1] + 12)],
                           SCHWARZ, STRICH["normal"], "#d0d0d0", schliessen=True))
        for i in range(5):
            for k in range(4):
                x, yy = P(20 + 50 * i, 20 + 40 * k)
                e.append(pfeil(x, yy - 30, x, yy, ROT, 1.2, (7, 5)))
        e.append(text(P(240, 160)[0] + 8, P(240, 160)[1] - 22, "p", ROT, anker="start"))
        e.append(hinweis(ox + W / 2, oy + 235, "z. B. Schnee, Wind, Wasserdruck", anker="middle", groesse=15))
    else:
        titel(e, ox, oy, "Volumenkraft ρ g in N/m³")
        x0, y0, b, h = ox + 90, oy + 70, 170, 130
        e.append(platte([(x0, y0), (x0 + b, y0), (x0 + b, y0 + h), (x0, y0 + h)], "#e6e6e6"))
        for i in range(5):
            for k in range(4):
                x, yy = x0 + 20 + 32 * i, y0 + 18 + 30 * k
                e.append(pfeil(x, yy, x, yy + 16, "#e08080", 1.0, (5, 4)))
        S = (x0 + b / 2, y0 + h / 2)
        e.append(punkt(*S, 3.4))
        e.append(kraft(*S, -90, "G", laenge=95, ziehend=True, label_seite=-1, label_pos=0.85))
        e.append(text(x0 + b + 14, y0 + 20, "[im Schwerpunkt]", "#555555", 14, anker="start", italic=False))
        e.append(hinweis(ox + W / 2, oy + 235, "z. B. Gewicht: verteilt über das ganze Volumen", anker="middle", groesse=15))


def kraftarten():
    abb = Abbildung(840, 840, "Arten der Kräfte")
    for nr in (1, 2, 3, 4):
        _kraftart(abb.ebene(f"art-{nr}", f"Kraftart {nr}"), nr, 0, 0)
    e = abb.ebene("uebersicht", "Übersicht")
    for nr, (ox, oy) in zip((1, 2, 3, 4), ((0, 300), (420, 300), (0, 560), (420, 560))):
        rahmen(e, ox, oy, 420, 260)
        _kraftart(e, nr, ox, oy)
    return abb.speichern(ZIEL / "kraftarten.svg")


# =====================================================================
# 2  Lager und Lagerreaktionen
# =====================================================================
def _lager(e, art, ox, oy):
    W = 420
    y = oy + 130
    if art == "freiheitsgrade":
        titel(e, ox, oy, "Freiheitsgrade in der Ebene")
        e.append(platte([(ox + 130, oy + 80), (ox + 290, oy + 70), (ox + 300, oy + 180), (ox + 140, oy + 190)]))
        M = (ox + 215, oy + 130)
        e.append(pfeil(M[0], M[1], M[0] + 90, M[1], GRUEN, 2.2, (11, 8)))
        e.append(pfeil(M[0], M[1], M[0], M[1] - 85, GRUEN, 2.2, (11, 8)))
        e.append(moment(M[0], M[1], "", gegen_uhrzeiger=True, r=26, start=200, bogen=230, farbe=GRUEN))
        e.append(text(M[0] + 96, M[1] + 16, "u_x", GRUEN, 18, anker="start"))
        e.append(text(M[0] + 10, M[1] - 92, "u_y", GRUEN, 18, anker="start"))
        e.append(text(M[0] - 34, M[1] + 30, "φ", GRUEN, 18))
        e.append(hinweis(ox + W / 2, oy + 225, "2 Verschiebungen und 1 Drehung", anker="middle", groesse=15))
        return
    namen = {"los": "Loslager (einwertig)", "fest": "Festlager (zweiwertig)", "einsp": "Einspannung (dreiwertig)",
             "gelenk": "Gelenk (zweiwertig)", "pendel": "Pendelstütze (einwertig)"}
    titel(e, ox, oy, namen[art])
    xs, xf = ox + 120, ox + 330               # Lager links, Freikörperbild rechts
    gleich(e, ox + 215, y)
    if art == "los":
        e.append(balken(xs - 70, y, xs, y))
        e.append(loslager(xs, y + T))
        e.append(balken(xf - 70, y, xf, y))
        e.append(kraft(xf, y + T, 90, "F_A", laenge=55, label_seite=-1))
        txt = "verhindert: Verschiebung senkrecht zur Bahn"
    elif art == "fest":
        e.append(balken(xs - 70, y, xs, y))
        e.append(festlager(xs, y + T))
        e.append(balken(xf - 70, y, xf, y))
        e.append(kraft(xf, y + T, 90, "F_{AV}", laenge=55, label_seite=-1))
        e.append(kraft(xf + 4, y, 180, "F_{AH}", laenge=55, label_seite=-1))
        txt = "verhindert: beide Verschiebungen"
    elif art == "einsp":
        e.append(balken(xs - 70, y, xs + 10, y))
        e.append(einspannung(xs - 70, y, hoehe=50))
        e.append(balken(xf - 60, y, xf + 20, y))
        e.append(kraft(xf - 60, y + T, 90, "F_{AV}", laenge=50, label_seite=1))
        e.append(kraft(xf - 64, y, 0, "F_{AH}", laenge=50, label_seite=1))
        e.append(moment(xf - 60, y, "", gegen_uhrzeiger=True, r=22, start=-60, bogen=200))
        e.append(text(xf - 34, y - 32, "M_A", ROT, anker="start"))
        txt = "verhindert: Verschiebungen und Drehung"
    elif art == "gelenk":
        e.append(balken(xs - 90, y, xs, y))
        e.append(balken(xs, y, xs + 60, y + 20))
        e.append(gelenk(xs, y, r=5))
        e.append(text(xs, y - 18, "G", SCHWARZ, 17))
        xa, xb = xf - 60, xf + 30
        e.append(balken(xa - 40, y, xa, y))
        e.append(balken(xb, y, xb + 45, y + 14))
        e.append(kraft(xa, y, 0, "G_H", laenge=32, ziehend=True, label_seite=1))
        e.append(kraft(xa, y, 90, "G_V", laenge=40, ziehend=True, label_seite=-1))
        e.append(kraft(xb, y, 180, "G_H", laenge=32, ziehend=True, label_seite=-1))
        e.append(kraft(xb, y, -90, "G_V", laenge=40, ziehend=True, label_seite=-1))
        txt = "überträgt Kräfte, aber kein Moment"
    else:
        e.append(balken(xs - 80, y, xs, y))
        e.append(pendelstab(xs, y, xs - 40, y + 70))
        e.append(festlager(xs - 40, y + 70))
        e.append(balken(xf - 70, y, xf, y))
        w = math.degrees(math.atan2(70, -40))
        e.append(strichpunkt(xf + 40 * 0.5, y - 70 * 0.5, xf - 40 * 1.3, y + 70 * 1.3, GRAU))
        e.append(kraft(xf, y, w - 180, "S", laenge=70, label_seite=1, label_pos=0.6))
        txt = "überträgt nur eine Kraft in Stabrichtung"
    e.append(hinweis(ox + W / 2, oy + 225, txt, anker="middle", groesse=15))


def lager():
    arten = ("freiheitsgrade", "los", "fest", "einsp", "gelenk", "pendel")
    abb = Abbildung(1260, 780, "Lager und Lagerreaktionen")
    for a in arten:
        _lager(abb.ebene(f"l-{a}", a), a, 0, 0)
    e = abb.ebene("uebersicht", "Übersicht")
    for k, a in enumerate(arten):
        ox, oy = 420 * (k % 3), 280 + 250 * (k // 3)
        rahmen(e, ox, oy, 420, 250)
        _lager(e, a, ox, oy)
    return abb.speichern(ZIEL / "lager.svg")


# =====================================================================
# 3  Statische Bestimmtheit
# =====================================================================
def _bestimmt(e, art, ox, oy):
    W = 440
    y = oy + 120
    x0, x1 = ox + 80, ox + 360
    texte = {"bestimmt": ("statisch bestimmt", "3 · 1 = 3 + 0", GRUEN),
             "unbestimmt": ("statisch unbestimmt", "3 · 1 < 4 + 0", ROT),
             "beweglich": ("beweglich (kinematisch)", "3 · 1 > 2 + 0", ROT),
             "ausnahme": ("Achtung: trotz 3 = 3 beweglich", "drei parallele Lagerkräfte", ROT),
             "zwang": ("Vorteil: zwängungsfrei", "Temperaturdehnung frei möglich", GRUEN)}
    t1, t2, farbe = texte[art]
    titel(e, ox, oy, t1)
    if art in ("bestimmt", "zwang"):
        e.append(balken(x0, y, x1, y))
        e.append(festlager(x0, y + T))
        if art == "zwang":
            e.append(polylinie([(x0, y - T), (x1 + 30, y - T), (x1 + 30, y + T), (x0, y + T)], GRAU, 1.0, "none",
                               strich="4 3", schliessen=True))
            e.append(loslager(x1 + 30, y + T))
            e.append(pfeil(x1, y - 22, x1 + 30, y - 22, GRUEN, 1.6, (8, 6)))
            e.append(text(x1 + 15, y - 36, "Δl", GRUEN, 16))
        else:
            e.append(loslager(x1, y + T))
    elif art == "unbestimmt":
        e.append(balken(x0, y, x1, y))
        e.append(festlager(x0, y + T))
        e.append(festlager(x1, y + T))
    elif art == "beweglich":
        e.append(balken(x0, y, x1, y))
        e.append(loslager(x0, y + T))
        e.append(loslager(x1, y + T))
        e.append(pfeil(ox + 190, y - 26, ox + 260, y - 26, ROT, 2.2, (11, 8)))
    else:
        e.append(balken(x0, y, x1, y))
        for x in (x0, (x0 + x1) / 2, x1):
            e.append(loslager(x, y + T))
        e.append(pfeil(ox + 190, y - 26, ox + 260, y - 26, ROT, 2.2, (11, 8)))
    e.append(text(ox + W / 2, oy + 195, f"[{t2}]", farbe, 19, italic=False))


def bestimmtheit():
    arten = ("bestimmt", "unbestimmt", "beweglich", "ausnahme", "zwang")
    abb = Abbildung(440, 230, "Statische Bestimmtheit")
    for a in arten:
        _bestimmt(abb.ebene(f"b-{a}", a), a, 0, 0)
    return abb.speichern(ZIEL / "bestimmtheit.svg")


# =====================================================================
# 4  Lagerreaktionen: B02-1 Einfeldträger mit Kragarm, B02-2 Kragträger
#    B02-1: F1 = F bei L/2, F2 = 2F bei L + L/10  ->  F_AH = 0, F_B = 2,7 F, F_AV = 0,3 F
#    B02-2: F1 = F bei L/2, F2 = 2F bei L, eingespannt  ->  F_AV = 3F, M_A = 2,5 F L
# =====================================================================
def einfeldtraeger():
    abb = Abbildung(640, 420, "Einfeldträger mit Kragarm")
    s = 400
    xA, y = 90, 120
    xF1, xB, xF2 = xA + s / 2, xA + s, xA + 1.1 * s
    e = abb.ebene("system", "System")
    e.append(balken(xA, y, xF2, y))
    e.append(festlager(xA, y + T, label="A", label_pos=(-22, 12)))
    e.append(loslager(xB, y + T, label="B", label_pos=(22, 12)))
    e.append(kraft(xF1, y - T, -90, "F_1 = F", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(kraft(xF2, y - T, -90, "F_2 = 2F", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(mass(xA, y, xF1, y, "L/2", abstand=-48))
    e.append(mass(xA, y, xB, y, "L", abstand=-78))
    e.append(mass(xB, y, xF2, y, "L/10", abstand=-48))

    yf = 310
    e = abb.ebene("freikoerper", "Freikörperbild")
    e.append(balken(xA, yf, xF2, yf))
    e.append(kraft(xF1, yf - T, -90, "F", laenge=55, label_seite=-1, label_pos=0.6))
    e.append(kraft(xF2, yf - T, -90, "2F", laenge=55, label_seite=-1, label_pos=0.6))
    e.append(kraft(xA, yf + T, 90, "F_{AV}", laenge=55, label_seite=1, label_pos=0.6))
    e.append(kraft(xA - 4, yf, 0, "F_{AH}", laenge=50, label_seite=-1))
    e.append(kraft(xB, yf + T, 90, "F_B", laenge=55, label_seite=-1, label_pos=0.6))
    e.append(punkt(xA, yf, 3))
    e.append(text(xA + 8, yf - 16, "A", SCHWARZ, 16, anker="start"))
    e.append(koord_xy(560, 400, 34, 34))
    return abb.speichern(ZIEL / "einfeldtraeger.svg")


def kragtraeger():
    abb = Abbildung(600, 400, "Eingespannter Balken")
    s = 400
    xA, y = 90, 120
    xF1, xF2 = xA + s / 2, xA + s
    e = abb.ebene("system", "System")
    e.append(balken(xA, y, xF2, y))
    e.append(einspannung(xA, y, hoehe=54, label="A"))
    e.append(kraft(xF1, y - T, -90, "F_1 = F", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(kraft(xF2, y - T, -90, "F_2 = 2F", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(mass(xA, y, xF1, y, "L/2", abstand=-40))
    e.append(mass(xA, y, xF2, y, "L", abstand=-70))

    yf = 300
    e = abb.ebene("freikoerper", "Freikörperbild")
    e.append(balken(xA, yf, xF2, yf))
    e.append(kraft(xF1, yf - T, -90, "F", laenge=55, label_seite=-1, label_pos=0.6))
    e.append(kraft(xF2, yf - T, -90, "2F", laenge=55, label_seite=-1, label_pos=0.6))
    e.append(kraft(xA, yf + T, 90, "F_{AV}", laenge=55, label_seite=-1, label_pos=0.6))
    e.append(kraft(xA - 2, yf, 0, "F_{AH}", laenge=50, label_seite=1, label_pos=0.8))
    e.append(moment(xA, yf, "", gegen_uhrzeiger=True, r=30, start=100, bogen=150))
    e.append(text(xA - 30, yf - 42, "M_A", ROT, anker="end"))
    e.append(punkt(xA, yf, 3))
    e.append(koord_xy(520, 385, 34, 34))
    return abb.speichern(ZIEL / "kragtraeger.svg")


# =====================================================================
# 5  Streckenlasten
# =====================================================================
def streckenlasten():
    abb = Abbildung(560, 300, "Streckenlasten")
    x0, x1, y = 70, 470, 190
    L = x1 - x0

    e = abb.ebene("allgemein", "Allgemeine Streckenlast")
    titel(e, 0, 0, "Streckenlast q(x)")
    e.append(balken(x0, y, x1, y))
    def q(x):
        t = (x - x0) / L
        return 40 + 50 * math.sin(math.pi * t) + 20 * t
    pts = [(x0 + L * i / 60, y - T - q(x0 + L * i / 60)) for i in range(61)]
    for i in range(0, 61, 4):
        x = x0 + L * i / 60
        e.append(pfeil(x, y - T - q(x), x, y - T, ROT, STRICH["normal"], (8, 5.5)))
    e.append(polylinie(pts, ROT, STRICH["normal"]))
    e.append(text(x1 + 6, y - T - q(x1) - 4, "q(x)", ROT, anker="start"))
    xs = x0 + 0.62 * L
    e.append(polylinie([(xs, y - T), (xs, y - T - q(xs)), (xs + 14, y - T - q(xs + 14)), (xs + 14, y - T)], None,
                       fuellung="#f5b5b5", schliessen=True))
    e.append(text(xs + 7, y - T - q(xs) - 18, "dF = q dx", ROT, 15))
    e.append(koord_xy(x0, y + 50, 40, 0.1, xlabel="x", ylabel=""))
    e.append(mass(xs, y + T, xs + 14, y + T, "dx", abstand=-26, hilfslinien=False))

    e = abb.ebene("ersatz", "Resultierende")
    titel(e, 0, 0, "Ersatz durch eine Einzelkraft")
    e.append(balken(x0, y, x1, y))
    xr = x0 + 0.53 * L
    e.append(kraft(xr, y - T, -90, "F_R", laenge=110, label_seite=-1, label_pos=0.5))
    e.append(mass(x0, y, xr, y, "x_R", abstand=-38))

    e = abb.ebene("rechteck", "Rechtecklast")
    titel(e, 0, 0, "Rechtecklast")
    e.append(balken(x0, y, x1, y))
    e.append(streckenlast(x0, x1, y - T, 60, label="q", n=16))
    xm = (x0 + x1) / 2
    e.append(kraft(xm, y - T, -90, "F_R = q L", laenge=130, label_seite=-1, label_pos=0.85, farbe="#9b0000"))
    e.append(mass(x0, y, xm, y, "L/2", abstand=-36))
    e.append(mass(x0, y, x1, y, "L", abstand=-66))

    e = abb.ebene("dreieck", "Dreieckslast")
    titel(e, 0, 0, "Dreieckslast")
    e.append(balken(x0, y, x1, y))
    e.append(streckenlast(x0, x1, y - T, 0, 90, label="q_0", n=16))
    x23 = x0 + 2 / 3 * L
    e.append(kraft(x23, y - T, -90, "F_R = ½ q_0 L", laenge=130, label_seite=1, label_pos=0.85, farbe="#9b0000"))
    e.append(mass(x0, y, x23, y, "2L/3", abstand=-36))
    e.append(mass(x0, y, x1, y, "L", abstand=-66))
    return abb.speichern(ZIEL / "streckenlasten.svg")


# =====================================================================
# 6  Systeme mit Gelenk: Pkw mit Anhänger (B02-3), Lkw mit Deichselanhänger
#    L_K = 4 m: A bei 0,8 m (Loslager), F_K bei 1,6 m, B bei 3,2 m (Festlager, Handbremse), G bei 4,0 m
#    Anhänger L_A = 2 m, q_0 = 1250 N/m über die ganze Länge, Achse C 1,2 m hinter G
# =====================================================================
def kfz_anhaenger():
    abb = Abbildung(900, 580, "Pkw mit Anhänger")
    m = 85                                      # px je m
    yb, xg0 = 150, 60
    def X(x):
        return xg0 + m * x

    # Ansicht (vereinfacht)
    e = abb.ebene("ansicht", "Pkw mit Anhänger")
    boden(e, 30, 840, yb + 28)
    e.append(platte([(X(0.1), yb + 6), (X(0.15), yb - 30), (X(1.2), yb - 40), (X(1.8), yb - 78), (X(3.1), yb - 78),
                     (X(3.7), yb - 40), (X(4.0), yb - 34), (X(4.0), yb + 6)], "#dfe7f0"))
    for x in (0.8, 3.2):
        e.append(kreis(X(x), yb + 12, 16, SCHWARZ, "#555555", 1.2))
    e.append(linie(X(4.0), yb - 6, X(4.25), yb - 6, SCHWARZ, 2.4))
    e.append(platte([(X(4.25), yb - 60), (X(6.25), yb - 60), (X(6.25), yb + 2), (X(4.25), yb + 2)], "#ececec"))
    e.append(kreis(X(5.45), yb + 12, 16, SCHWARZ, "#555555", 1.2))
    e.append(kreis(X(4.25), yb - 6, 4, SCHWARZ, "#ffffff", 1.4))

    # Modell
    y = 330
    e = abb.ebene("modell", "Modell")
    e.append(balken(X(0), y, X(4.0), y))
    e.append(balken(X(4.0), y, X(6.0), y))
    e.append(gelenk(X(4.0), y, r=5))
    e.append(text(X(4.0), y - 20, "G", SCHWARZ, 17))
    e.append(loslager(X(0.8), y + T, label="A", label_pos=(-22, 12)))
    e.append(festlager(X(3.2), y + T, label="B", label_pos=(22, 12)))
    e.append(loslager(X(5.2), y + T, label="C", label_pos=(22, 12)))
    e.append(kraft(X(1.6), y - T, -90, "F_K", laenge=60, label_seite=-1, label_pos=0.6))
    e.append(streckenlast(X(4.0), X(6.0), y - T, 40, label="q_0", n=12))
    for x1, x2, lab, ab in ((0, 0.8, "0,8", -36), (0.8, 1.6, "0,8", -36), (1.6, 3.2, "1,6", -36),
                             (3.2, 4.0, "0,8", -36), (4.0, 5.2, "1,2", -36), (5.2, 6.0, "0,8", -36)):
        e.append(mass(X(x1), y, X(x2), y, lab, abstand=ab))
    e.append(text(X(6.0) + 10, y + 52, "[m]", GRUEN, 15, anker="start", italic=False))

    # Freikörperbilder (am Gelenk getrennt)
    y2 = 480
    e = abb.ebene("freischnitt", "Freikörperbilder")
    d = 80
    e.append(balken(X(0), y2, X(4.0), y2))
    e.append(balken(X(4.0) + d, y2, X(6.0) + d, y2))
    e.append(schnitt(X(4.0), y2 - 18, X(4.0), y2 + 18))
    e.append(schnitt(X(4.0) + d, y2 - 18, X(4.0) + d, y2 + 18))
    e.append(kraft(X(1.6), y2 - T, -90, "F_K", laenge=50, label_seite=-1, label_pos=0.6))
    e.append(kraft(X(0.8), y2 + T, 90, "F_A", laenge=45, label_seite=1, label_pos=0.6))
    e.append(kraft(X(3.2), y2 + T, 90, "F_{BV}", laenge=45, label_seite=1, label_pos=0.6))
    e.append(kraft(X(3.2) - 4, y2, 0, "F_{BH}", laenge=40, label_seite=-1))
    # Gelenkkräfte: am Pkw G_V nach unten (Stützlast), am Anhänger nach oben
    e.append(kraft(X(4.0), y2 - T, -90, "G_V", laenge=45, label_seite=1, label_pos=0.7))
    e.append(kraft(X(4.0), y2, 0, "G_H", laenge=30, ziehend=True, label_seite=1))
    e.append(kraft(X(4.0) + d, y2 + T, 90, "G_V", laenge=45, label_seite=1, label_pos=0.7))
    e.append(kraft(X(4.0) + d, y2, 180, "G_H", laenge=30, ziehend=True, label_seite=-1))
    e.append(streckenlast(X(4.0) + d, X(6.0) + d, y2 - T, 34, label="q_0", n=10))
    e.append(kraft(X(5.2) + d, y2 + T, 90, "F_C", laenge=45, label_seite=-1, label_pos=0.6))
    e.append(text(X(2.0), y2 + 66, "[I: Pkw]", "#555555", 15, italic=False))
    e.append(text(X(5.0) + d, y2 + 66, "[II: Anhänger]", "#555555", 15, italic=False))
    return abb.speichern(ZIEL / "kfz-anhaenger.svg")


def lkw_deichsel():
    abb = Abbildung(860, 420, "Lkw mit Deichselanhänger")
    yb = 170
    e = abb.ebene("ansicht", "Lkw mit Deichselanhänger")
    boden(e, 20, 840, yb + 28)
    e.append(platte([(40, yb + 6), (40, yb - 90), (120, yb - 90), (135, yb - 50), (135, yb - 70), (360, yb - 70),
                     (360, yb + 6)], "#dfe7f0"))
    for x in (85, 290, 330):
        e.append(kreis(x, yb + 12, 16, SCHWARZ, "#555555", 1.2))
    e.append(platte([(480, yb - 70), (800, yb - 70), (800, yb + 2), (480, yb + 2)], "#ececec"))
    for x in (530, 750):
        e.append(kreis(x, yb + 12, 16, SCHWARZ, "#555555", 1.2))
    e.append(pendelstab(360, yb - 6, 480, yb - 6))
    e.append(text(420, yb - 26, "[Deichsel]", SCHWARZ, 15, italic=False))

    y = 330
    e = abb.ebene("deichsel", "Deichsel als Pendelstütze")
    e.append(balken(80, y, 360, y))
    e.append(balken(480, y, 800, y))
    e.append(pendelstab(360, y, 480, y))
    e.append(loslager(110, y + T, label="A", label_pos=(-20, 12)))
    e.append(festlager(310, y + T, label="B", label_pos=(-20, 12)))
    e.append(kraft(200, y - T, -90, "F_K", laenge=55, label_seite=-1, label_pos=0.6))
    for x, lab in ((530, "C"), (750, "D")):
        e.append(loslager(x, y + T, label=lab, label_pos=(20, 12)))
    e.append(streckenlast(480, 800, y - T, 34, label="q_0", n=14))
    e.append(text(420, y + 62, "[Deichsel: nur Kraft in Stabrichtung]", ROT, 15, italic=False))
    e.append(pfeil(395, y - 22, 445, y - 22, ROT, 2.2, (11, 8)))
    e.append(text(420, y - 40, "S", ROT))
    return abb.speichern(ZIEL / "lkw-deichsel.svg")


# =====================================================================
# 7  Zusammenfassung
# =====================================================================
def zusammenfassung():
    W, H, rand = 300, 220, 15
    abb = Abbildung(3 * W + 4 * rand, 2 * H + 3 * rand, "Zusammenfassung: Lager und Lagerreaktionen")

    def kachel(e, spalte, zeile, t, formel):
        x, y = rand + spalte * (W + rand), rand + zeile * (H + rand)
        e.append(polylinie([(x, y), (x + W, y), (x + W, y + H), (x, y + H)], "#c8c8c8", 1.2, "#fafafa",
                           schliessen=True))
        e.append(text(x + 14, y + 22, f"[{t}]", SCHWARZ, 17, anker="start", italic=False))
        zeilen = formel if isinstance(formel, (list, tuple)) else [formel]
        for k, z in enumerate(reversed(zeilen)):
            e.append(text(x + W / 2, y + H - 20 - 24 * k, z, ROT, 17))
        return x, y

    e = abb.ebene("k-arten", "Arten der Kräfte")
    x, y = kachel(e, 0, 0, "Arten der Kräfte", ["F: N,   q: N/m,   p: N/m²,   ρg: N/m³"])
    e.append(balken(x + 30, y + 120, x + 270, y + 120))
    e.append(kraft(x + 80, y + 116, -90, "F", laenge=50, label_seite=-1))
    e.append(streckenlast(x + 140, x + 260, y + 116, 32, label="q", n=6))

    e = abb.ebene("k-lager", "Lager")
    x, y = kachel(e, 1, 0, "Lager: Wertigkeit 1, 2, 3", ["Lager → Reaktionen ersetzen"])
    for k, (xx, art) in enumerate(((x + 60, "los"), (x + 150, "fest"), (x + 240, "einsp"))):
        yy = y + 110
        if art == "einsp":
            e.append(balken(xx - 20, yy, xx + 30, yy))
            e.append(einspannung(xx - 20, yy, hoehe=40))
        else:
            e.append(balken(xx - 30, yy, xx + 30, yy))
            e.append(loslager(xx, yy + T) if art == "los" else festlager(xx, yy + T))
        e.append(text(xx, yy + 50, f"[{k + 1}]", GRUEN, 19, italic=False))

    e = abb.ebene("k-bestimmt", "Bestimmtheit")
    x, y = kachel(e, 2, 0, "Statisch bestimmt?", ["3 n = a + z"])
    e.append(balken(x + 50, y + 100, x + 250, y + 100))
    e.append(festlager(x + 50, y + 100 + T))
    e.append(loslager(x + 250, y + 100 + T))
    e.append(hinweis(x + W / 2, y + 160, "notwendig, nicht hinreichend", anker="middle", groesse=13))

    e = abb.ebene("k-rechnen", "Lagerreaktionen")
    x, y = kachel(e, 0, 1, "Lagerreaktionen berechnen", ["Σ F_x = 0,  Σ F_y = 0,  Σ M^{(A)} = 0"])
    yy = y + 100
    e.append(balken(x + 50, yy, x + 250, yy))
    e.append(kraft(x + 150, yy - T, -90, "F", laenge=40, label_seite=-1))
    e.append(kraft(x + 50, yy + T, 90, "F_{AV}", laenge=40, label_seite=1))
    e.append(kraft(x + 46, yy, 0, "F_{AH}", laenge=34, label_seite=-1))
    e.append(kraft(x + 250, yy + T, 90, "F_B", laenge=40, label_seite=-1))

    e = abb.ebene("k-strecke", "Streckenlast")
    x, y = kachel(e, 1, 1, "Streckenlast ersetzen", ["F_R = ∫ q dx,   x_R = ∫ q x dx / F_R"])
    yy = y + 120
    e.append(balken(x + 40, yy, x + 260, yy))
    e.append(streckenlast(x + 40, x + 260, yy - T, 0, 50, label="q_0", n=10))
    e.append(kraft(x + 40 + 2 / 3 * 220, yy - T, -90, "", laenge=80, farbe="#9b0000"))

    e = abb.ebene("k-gelenk", "Gelenk")
    x, y = kachel(e, 2, 1, "Systeme mit Gelenk", ["am Gelenk trennen: actio = reactio"])
    yy = y + 105
    e.append(balken(x + 40, yy, x + 140, yy))
    e.append(balken(x + 170, yy, x + 260, yy))
    e.append(schnitt(x + 140, yy - 14, x + 140, yy + 14))
    e.append(schnitt(x + 170, yy - 14, x + 170, yy + 14))
    e.append(kraft(x + 140, yy, 90, "G_V", laenge=36, ziehend=True, label_seite=1))
    e.append(kraft(x + 170, yy, -90, "G_V", laenge=36, ziehend=True, label_seite=1))
    return abb.speichern(ZIEL / "zusammenfassung-lager.svg")


# =====================================================================
# Aufgaben (nach Götz 1.3.x, im Kursstil neu gezeichnet)
# =====================================================================
def _aufg(name, b, h):
    abb = Abbildung(b, h, name)
    return abb, abb.ebene("system", "System")


def aufgabe_1_3_1():
    abb, e = _aufg("Träger mit Kragarm", 500, 200)
    a, xA, y = 120, 60, 90
    e.append(balken(xA, y, xA + 3 * a, y))
    e.append(festlager(xA, y + T, label="A", label_pos=(-20, 12)))
    e.append(loslager(xA + 2 * a, y + T, label="B", label_pos=(22, 12)))
    e.append(kraft(xA + a, y - T, 240, "F_1", laenge=60, label_seite=1))
    e.append(linie(xA + a, y - T, xA + a + 46, y - T, GRAU, 0.6, strich="3 2"))
    from tmzeichnen import winkelbogen
    e.append(winkelbogen(xA + a, y - T, 26, 0, 60, "α"))
    e.append(kraft(xA + 3 * a, y - T, -90, "F_2", laenge=50, label_seite=-1))
    for i in range(3):
        e.append(mass(xA + i * a, y, xA + (i + 1) * a, y, "a", abstand=-56))
    e.append(koord_xy(30, 30, 30, 30))
    return abb.speichern(ZIEL / "aufgabe-1-3-1.svg")


def aufgabe_1_3_2():
    abb, e = _aufg("Eingespannter Winkelträger", 520, 280)
    l = 110
    B = (90, 60)
    E = (B[0], B[1] + l)                         # Ecke unten
    R = (E[0] + 2 * l, E[1])                     # rechtes Ende
    Ro = (R[0], R[1] - l / 4)
    e.append(balken(*B, *E, dicke=8))
    e.append(balken(*E, *R, dicke=8))
    e.append(balken(*R, *Ro, dicke=8))
    from tmzeichnen import einspannung as eins
    e.append(linie(B[0] - 24, B[1], B[0] + 24, B[1], SCHWARZ, STRICH["dick"]))
    xx = B[0] - 22
    while xx < B[0] + 24:
        e.append(linie(xx, B[1], xx + 7, B[1] - 7, SCHWARZ, STRICH["duenn"]))
        xx += 6
    e.append(text(B[0] + 10, B[1] - 18, "B", GRUEN, anker="start"))
    e.append(kraft(E[0] + l, E[1] - 4, -90, "F_1", laenge=70, label_seite=-1))
    e.append(kraft(Ro[0] - 4, Ro[1], 180, "F_2", laenge=55, ziehend=True, label_seite=1))
    e.append(kraft(Ro[0], Ro[1] - 4, 90, "F_3", laenge=50, ziehend=True, label_seite=1))
    e.append(mass(*E, E[0] + l, E[1], "l", abstand=-36))
    e.append(mass(E[0] + l, E[1], *R, "l", abstand=-36))
    e.append(mass(*E, *B, "l", abstand=-34))
    e.append(mass(*R, *Ro, "l/4", abstand=-30))
    e.append(koord_xy(400, 60, 30, 30))
    return abb.speichern(ZIEL / "aufgabe-1-3-2.svg")


def aufgabe_1_3_4():
    abb, e = _aufg("Hebebühne", 520, 330)
    m = 170
    B = (150, 120)
    def P(x, y):
        return (B[0] + m * x, B[1] - m * y)
    d, a, b, h = 0.25, 0.8, 1.0, 0.6
    e.append(balken(*P(-0.05, 0), *P(a + b, 0), dicke=14))
    U = P(-d, -h)
    C = P(a, 0)
    e.append(pendelstab(*U, *C))
    e.append(festlager(*P(0, 0), groesse=12))
    e.append(festlager(*U, groesse=12))
    e.append(text(P(0, 0)[0] - 8, P(0, 0)[1] - 18, "B", SCHWARZ, 17, anker="end"))
    e.append(text(C[0] + 8, C[1] + 22, "C", SCHWARZ, 17, anker="start"))
    e.append(kraft(*P(a, 0.04), -90, "F_G", laenge=60, label_seite=-1))
    e.append(kraft(*P(a + b, -0.04), -90, "F_L", laenge=60, ziehend=True, label_seite=-1))
    e.append(mass(*U, P(0, -h)[0], U[1], "d", abstand=-34))
    e.append(mass(P(0, -h)[0], U[1], P(a, -h)[0], U[1], "a", abstand=-34))
    e.append(mass(P(a, -h)[0], U[1], P(a + b, -h)[0], U[1], "b", abstand=-34))
    e.append(mass(U[0], U[1], U[0], P(0, 0)[1], "h", abstand=40))
    e.append(koord_xy(40, 300, 30, 30))
    e.append(text(*((U[0] + C[0]) / 2 + 14, (U[1] + C[1]) / 2 + 10), "[Hydraulikzylinder]", "#555555", 13, anker="start",
                  italic=False))
    return abb.speichern(ZIEL / "aufgabe-1-3-4.svg")


def aufgabe_1_3_8():
    abb, e = _aufg("Träger mit Streckenlast und drei Kräften", 560, 190)
    l = 80
    x0, y = 50, 90
    e.append(balken(x0, y, x0 + 6 * l, y))
    e.append(streckenlast(x0, x0 + 3 * l, y - T, 34, label="q", n=12))
    e.append(kraft(x0, y - T - 34, -90, "F", laenge=30, label_seite=1))
    e.append(kraft(x0 + 4 * l, y - T, -90, "F", laenge=50, label_seite=-1))
    e.append(kraft(x0 + 6 * l, y - T, -90, "F", laenge=50, label_seite=-1))
    e.append(festlager(x0 + 2 * l, y + T, label="A", label_pos=(-20, 12)))
    e.append(loslager(x0 + 5 * l, y + T, label="B", label_pos=(-20, 12)))
    for x1, x2, lab in ((0, 2, "2l"), (2, 3, "l"), (3, 4, "l"), (4, 5, "l"), (5, 6, "l")):
        e.append(mass(x0 + x1 * l, y, x0 + x2 * l, y, lab, abstand=-50))
    return abb.speichern(ZIEL / "aufgabe-1-3-8.svg")


def aufgabe_1_3_9():
    abb, e = _aufg("Träger mit Dreieckslasten", 520, 200)
    l = 130
    x0, y = 60, 110
    e.append(balken(x0, y, x0 + 3 * l, y))
    e.append(streckenlast(x0, x0 + l, y - T, 0, 70, n=6))
    e.append(streckenlast(x0 + l, x0 + 3 * l, y - T, 70, 0, n=12))
    e.append(text(x0 + l, y - T - 84, "q_0", ROT))
    e.append(festlager(x0 + l, y + T, label="A", label_pos=(-20, 12)))
    e.append(loslager(x0 + 3 * l, y + T, label="B", label_pos=(-20, 12)))
    e.append(mass(x0, y, x0 + l, y, "l", abstand=-50))
    e.append(mass(x0 + l, y, x0 + 3 * l, y, "2l", abstand=-50))
    return abb.speichern(ZIEL / "aufgabe-1-3-9.svg")


def aufgabe_1_3_11():
    abb, e = _aufg("Gelenkträger mit Winkel", 600, 270)
    l = 100
    x0, y = 70, 90
    xB, xG, xA = x0 + l, x0 + 2 * l, x0 + 4 * l
    e.append(balken(x0, y + l, x0, y, dicke=8))
    e.append(balken(x0, y, xG, y, dicke=8))
    e.append(balken(xG, y, xA, y, dicke=8))
    e.append(gelenk(xG, y, r=5))
    e.append(text(xG, y + 22, "G", SCHWARZ, 17))
    e.append(einspannung(xA, y, hoehe=44, seite="rechts", label="A"))
    e.append(loslager(xB, y + 4, label="B", label_pos=(-22, 12)))
    e.append(streckenlast(xG, xA, y - 4, 36, label="q", label_rechts=False, n=12))
    e.append(kraft(x0, y - 4, -90, "F", laenge=50, label_seite=1))
    e.append(kraft(x0 - 4, y + l, 0, "F", laenge=50, label_seite=1))
    e.append(mass(x0, y + l, x0, y, "l", abstand=-26))
    e.append(mass(x0, y, xB, y, "l", abstand=-l - 30))
    e.append(mass(xB, y, xG, y, "l", abstand=-l - 30))
    e.append(mass(xG, y, xA, y, "2l", abstand=-l - 30))
    return abb.speichern(ZIEL / "aufgabe-1-3-11.svg")


if __name__ == "__main__":
    for fn in (kraftarten, lager, bestimmtheit, einfeldtraeger, kragtraeger, streckenlasten, kfz_anhaenger,
               lkw_deichsel, zusammenfassung, aufgabe_1_3_1, aufgabe_1_3_2, aufgabe_1_3_4, aufgabe_1_3_8,
               aufgabe_1_3_9, aufgabe_1_3_11):
        print(fn())

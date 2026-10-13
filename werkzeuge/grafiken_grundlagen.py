"""Grafiken zum Kapitel Grundlagen (Woche 1): Kraft, Moment, Axiome, Kraftsysteme, Gleichgewicht.

Aufruf:  python werkzeuge/grafiken_grundlagen.py
Ergebnis: grafiken/grundlagen/*.svg (Inkscape-Ebenen = Scroll-Schritte)

In diesem Kapitel gilt wie in der Vorlesung 2013 und bei Götz: x nach rechts, y nach oben.
Hilfsfunktion P(...) rechnet Modellkoordinaten in SVG-Pixel um.
"""

import math
from pathlib import Path

from tmzeichnen import (FARBE, STRICH, Abbildung, _spitze, balken, festlager, gruppe, kraft, kreis, linie,
                        mass, moment, pfeil, polylinie, schnitt, text, winkelbogen)

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


def vlabel(x, y, name, farbe="#000000", groesse=19, anker="middle", index=""):
    """Formelzeichen mit Vektorpfeil darüber, z. B. vlabel(..., "F") → F mit Pfeil; index wird tiefgestellt."""
    b = 0.55 * groesse                                   # ungefähre Breite des Buchstabens
    x0 = x - b / 2 if anker == "middle" else (x if anker == "start" else x - b - (0.45 * groesse if index else 0))
    yp = y - 0.62 * groesse
    teile = [text(x0, y, name + (f"_{{{index}}}" if index else ""), farbe, groesse, anker="start"),
             linie(x0 + 0.5, yp, x0 + b + 1, yp, farbe, 1.1),
             _spitze(x0 + b + 3, yp, 1, 0, farbe, 5, 4)]
    return gruppe(teile)


def strichpunkt(x1, y1, x2, y2, farbe=GRAU, breite=0.9):
    """Wirkungslinie (Strich-Punkt)."""
    return linie(x1, y1, x2, y2, farbe, breite, strich="14 4 2 4")


def platte(punkte, fuellung=HELL):
    return polylinie(punkte, FARBE["linie"], STRICH["normal"], fuellung, schliessen=True)


def kasten(x, y, b, h, zeilen, fuellung="#f2f2f2", farbe="#000000", fett=False, gr1=17, gr2=13):
    teile = [polylinie([(x - b / 2, y - h / 2), (x + b / 2, y - h / 2), (x + b / 2, y + h / 2), (x - b / 2, y + h / 2)],
                       "#444444", STRICH["normal"], fuellung, schliessen=True)]
    n = len(zeilen)
    for i, z in enumerate(zeilen):
        gr = gr1 if i == 0 else gr2
        teile.append(text(x, y + (i - (n - 1) / 2) * (gr1 + 4), f"[{z}]", farbe if i == 0 else "#444444", gr,
                          italic=False, halo=False))
    return gruppe(teile)


def rechter_winkel(x, y, ux, uy, vx, vy, a=9, farbe=GRAU):
    """Kennzeichnung eines rechten Winkels im Punkt (x,y) zwischen den Richtungen u und v (Einheitsvektoren, SVG)."""
    return polylinie([(x + ux * a, y + uy * a), (x + (ux + vx) * a, y + (uy + vy) * a), (x + vx * a, y + vy * a)],
                     farbe, STRICH["duenn"])


def deckenlager(x, y, label=""):
    """Festes Gelenklager an der Decke (zweiwertig): Gelenkpunkt bei (x, y), Lagerkörper darüber."""
    return gruppe([festlager(x, y, groesse=16, drehung=180),
                   text(x + 26, y - 6, label, GRUEN, anker="start") if label else ""])


def punkt(x, y, r=3.2, farbe="#000000"):
    return kreis(x, y, r, farbe, farbe, 0.8)


def hinweis(x, y, s, anker="start", groesse=14):
    return text(x, y, f"[{s}]", "#444444", groesse, anker=anker, italic=False)


# =====================================================================
# Einordnung: Mechanik → Dynamik / Statik → Stereostatik / Elastostatik
# =====================================================================
def einordnung():
    abb = Abbildung(645, 430, "Einordnung der Technischen Mechanik")
    e = abb.ebene("baum", "Gliederung der Mechanik")
    knoten = {"mech": (320, 45), "dyn": (112, 182), "stat": (440, 182), "stereo": (330, 322), "elasto": (540, 322)}
    groesse = {"mech": 340, "dyn": 210, "stat": 220, "stereo": 196, "elasto": 196}
    for a, b in (("mech", "dyn"), ("mech", "stat"), ("stat", "stereo"), ("stat", "elasto")):
        (x1, y1), (x2, y2) = knoten[a], knoten[b]
        e.append(linie(x1, y1 + 38, x2, y2 - 38, "#444444", STRICH["normal"]))
    for k, zeilen in (("mech", ["Technische Mechanik", "Kräfte und ihre Wirkungen"]),
                      ("dyn", ["Dynamik", "Körper in Bewegung"]), ("stat", ["Statik", "Körper in Ruhe"]),
                      ("stereo", ["Stereostatik", "starre Körper"]), ("elasto", ["Elastostatik", "verformbare Körper"])):
        e.append(kasten(*knoten[k], groesse[k], 76, zeilen, gr1=28, gr2=19))

    e = abb.ebene("inhalt", "Inhalt dieser Lehrveranstaltung")
    e.append(polylinie([(222, 136), (642, 136), (642, 425), (222, 425)], ROT, 1.8, schliessen=True, strich="9 5"))
    e.append(text(640, 118, "[Inhalt dieser Lehrveranstaltung]", ROT, 21, anker="end", italic=False))
    e.append(text(330, 395, "[Wochen 1–4]", ROT, 20, italic=False))
    e.append(text(540, 395, "[Wochen 5–14]", ROT, 20, italic=False))
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
def _axiom(e, nr, ox, oy):
    """Zeichnet Axiom nr in ein Feld 400 x 280 mit linker oberer Ecke (ox, oy)."""
    titel = {1: "1  Linienflüchtigkeit", 2: "2  Kräfteparallelogramm", 3: "3  Gleichgewicht zweier Kräfte",
             4: "4  Wechselwirkung (actio = reactio)"}[nr]
    e.append(text(ox + 20, oy + 26, f"[{titel}]", "#000000", 19, anker="start", italic=False))
    if nr == 1:
        e.append(platte([(ox + 90, oy + 120), (ox + 300, oy + 95), (ox + 330, oy + 190), (ox + 250, oy + 235),
                         (ox + 110, oy + 215)]))
        y = oy + 160
        e.append(strichpunkt(ox + 20, y, ox + 390, y))
        e.append(kraft(ox + 98, y, 0, "F", laenge=60, label_seite=1))
        e.append(punkt(ox + 98, y))
        e.append('<g opacity="0.45">' + kraft(ox + 318, y, 0, "F", laenge=60, ziehend=True, label_seite=1) + "</g>")
        e.append(punkt(ox + 318, y))
        e.append(hinweis(ox + 200, oy + 262, "gleiche Wirkung am starren Körper", anker="middle", groesse=15))
    elif nr == 2:
        A = (ox + 90, oy + 225)
        f1 = (170 * math.cos(math.radians(12)), -170 * math.sin(math.radians(12)))
        f2 = (120 * math.cos(math.radians(70)), -120 * math.sin(math.radians(70)))
        p1, p2 = (A[0] + f1[0], A[1] + f1[1]), (A[0] + f2[0], A[1] + f2[1])
        pr = (A[0] + f1[0] + f2[0], A[1] + f1[1] + f2[1])
        e.append(linie(*p1, *pr, GRAU, STRICH["normal"], strich="5 4"))
        e.append(linie(*p2, *pr, GRAU, STRICH["normal"], strich="5 4"))
        # ohne Koordinatensystem: Kräfte als Vektoren bezeichnen
        e.append(vektor(*A, *p1))
        e.append(vlabel((A[0] + p1[0]) / 2, (A[1] + p1[1]) / 2 + 22, "F", ROT, index="1"))
        e.append(vektor(*A, *p2))
        e.append(vlabel((A[0] + p2[0]) / 2 - 18, (A[1] + p2[1]) / 2, "F", ROT, anker="end", index="2"))
        e.append(vektor(*A, *pr))
        e.append(vlabel((A[0] + pr[0]) / 2 - 14, (A[1] + pr[1]) / 2 - 12, "F", ROT, anker="end", index="R"))
        e.append(punkt(*A))
        e.append(hinweis(ox + 200, oy + 262, "zwei Kräfte = eine Resultierende", anker="middle", groesse=15))
    elif nr == 3:
        e.append(platte([(ox + 110, oy + 110), (ox + 290, oy + 95), (ox + 310, oy + 200), (ox + 130, oy + 220)]))
        m = 30 / 185
        y0 = oy + 125
        e.append(strichpunkt(ox + 20, y0, ox + 390, y0 + 60))
        for xa, w, seite in ((ox + 118, 180 - math.degrees(math.atan(m)), -1), (ox + 300, -math.degrees(math.atan(m)), 1)):
            e.append(kraft(xa, y0 + m * (xa - ox - 20), w, "F", laenge=70, ziehend=True, label_seite=seite))
        e.append(hinweis(ox + 200, oy + 262, "gleich groß · gleiche Wirkungslinie · entgegengesetzt", anker="middle",
                         groesse=15))
    else:
        y1, y2 = oy + 95, oy + 190
        x0, x1, xs = ox + 90, ox + 310, ox + 200
        e.append(balken(x0, y1, x1, y1, dicke=12))
        e.append(kraft(x0, y1, 180, "F", laenge=55, ziehend=True, label_seite=1))
        e.append(kraft(x1, y1, 0, "F", laenge=55, ziehend=True, label_seite=1))
        e.append(schnitt(xs, y1 - 24, xs, y1 + 24))
        d = 62
        e.append(balken(x0, y2, xs - d, y2, dicke=12))
        e.append(balken(xs + d, y2, x1, y2, dicke=12))
        e.append(schnitt(xs - d, y2 - 16, xs - d, y2 + 16))
        e.append(schnitt(xs + d, y2 - 16, xs + d, y2 + 16))
        e.append(kraft(x0, y2, 180, "F", laenge=55, ziehend=True, label_seite=1))
        e.append(kraft(x1, y2, 0, "F", laenge=55, ziehend=True, label_seite=1))
        e.append(kraft(xs - d, y2, 0, "F_i", laenge=44, ziehend=True, label_seite=-1, label_abstand=12))
        e.append(kraft(xs + d, y2, 180, "F_i", laenge=44, ziehend=True, label_seite=1, label_abstand=12))
        e.append(hinweis(ox + 200, oy + 262, "Schnitt: Kräfte paarweise entgegengesetzt", anker="middle", groesse=15))


def axiome():
    """Jedes Axiom einzeln (Ebenen ax-1 … ax-4 an derselben Stelle), zum Schluss alle vier als Übersicht."""
    abb = Abbildung(800, 900, "Axiome der Statik")
    for nr in (1, 2, 3, 4):
        _axiom(abb.ebene(f"ax-{nr}", f"Axiom {nr}"), nr, 0, 0)
    e = abb.ebene("uebersicht", "Die vier Axiome im Überblick")
    for nr, (ox, oy) in zip((1, 2, 3, 4), ((0, 320), (400, 320), (0, 600), (400, 600))):
        e.append(polylinie([(ox + 4, oy + 4), (ox + 396, oy + 4), (ox + 396, oy + 276), (ox + 4, oy + 276)],
                           "#c8c8c8", 1.0, "none", schliessen=True))
        _axiom(e, nr, ox, oy)
    return abb.speichern(ZIEL / "axiome.svg")


# =====================================================================
# Beispiel B01-1: Resultierende zweier Kräfte (VL 2013 Teil 1 S. 15)
#   F1 = 20 N unter 30°, F2 = 30 N unter 135°
# =====================================================================
def resultierende_zwei_kraefte():
    abb = Abbildung(680, 400, "Resultierende zweier Kräfte")
    s = 6.0                                  # px je N
    O = (250, 320)
    P = abbild(*O, s)
    F1 = (20 * math.cos(math.radians(30)), 20 * math.sin(math.radians(30)))
    F2 = (30 * math.cos(math.radians(135)), 30 * math.sin(math.radians(135)))
    FR = (F1[0] + F2[0], F1[1] + F2[1])

    e = abb.ebene("system", "Kräfte im Koordinatensystem")
    e.append(koord_xy(*O, 200, 250, negativ=200, negativ_y=50))
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

    e = abb.ebene("winkel135", "Richtungswinkel 135°")
    e.append(winkelbogen(*O, 100, 0, 135, ""))
    e.append(text(O[0] + 22, O[1] - 104, "135°", GRUEN, 17, anker="start"))

    e = abb.ebene("krafteck", "Krafteck")
    K0 = (520, 330)
    Q = abbild(*K0, s)
    e.append(hinweis(K0[0] - 30, K0[1] + 40, "Krafteck", anker="middle"))
    e.append(vektor(*K0, *Q(*F1), "F_1", ly=18))
    e.append(vektor(*Q(*F1), *Q(*FR), "F_2", lx=18, ly=-4))
    e.append(vektor(*K0, *Q(*FR), "F_R", farbe=ROT, lx=-22, breite=2.6))
    e.append(punkt(*K0))

    e = abb.ebene("resultierende", "Resultierende")
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
    e.append(deckenlager(H[0], H[1]))
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
    e.append(schnitt(cx - 20 * math.cos(alpha), cy + 20 * math.sin(alpha), cx + 20 * math.cos(alpha),
                     cy - 20 * math.sin(alpha)))
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
    """Woche 1: Kräftepaar und freie Verschiebbarkeit des Moments."""
    abb = Abbildung(620, 540, "Kräftepaar")

    def koerper(x0):
        return platte([(x0 + 20, 100), (x0 + 250, 100), (x0 + 250, 250), (x0 + 20, 250)])

    e = abb.ebene("kraeftepaar", "Kräftepaar")
    e.append(koerper(0))
    xl, xr = 70, 200
    e.append(strichpunkt(xl, 60, xl, 300))
    e.append(strichpunkt(xr, 60, xr, 300))
    e.append(kraft(xl, 175, 90, "F", laenge=70, ziehend=True, label_seite=1))
    e.append(kraft(xr, 175, -90, "F", laenge=70, ziehend=True, label_seite=1))
    e.append(mass(xl, 175, xr, 175, "b", abstand=-118))
    e.append(text(310, 175, "[=]", "#000000", 30, italic=False))
    e.append(koerper(350))
    e.append(moment(485, 175, "", gegen_uhrzeiger=False, r=28, start=150, bogen=280))
    e.append(text(485, 120, "M = F b", ROT, 21))

    e = abb.ebene("verschieblich", "Moment frei verschieblich")
    dy = 230                                     # zweite Zeile, unter dem Moment-Körper
    e.append(text(310, 175 + dy, "[=]", "#000000", 30, italic=False))
    e.append(platte([(370, 100 + dy), (600, 100 + dy), (600, 250 + dy), (370, 250 + dy)]))
    for (x, y) in ((420, 145 + dy), (550, 150 + dy), (480, 215 + dy)):
        e.append(moment(x, y, "", gegen_uhrzeiger=False, r=20, start=150, bogen=280))
        e.append(text(x + 26, y - 22, "M", ROT, 19, anker="start"))
    e.append(hinweis(485, 280 + dy, "überall dieselbe Wirkung", anker="middle", groesse=16))
    return abb.speichern(ZIEL / "moment.svg")


def versatz_grafik():
    """Parallelverschiebung einer Kraft: F im Inneren = F an der Ecke + Versatzmoment."""
    abb = Abbildung(620, 610, "Parallelverschiebung einer Kraft")

    def koerper(x0):
        return platte([(x0 + 20, 100), (x0 + 250, 100), (x0 + 250, 250), (x0 + 20, 250)])

    e = abb.ebene("innen", "Kraft im Inneren")
    e.append(koerper(0))
    xA = 130
    e.append(strichpunkt(xA, 50, xA, 300))
    e.append(kraft(xA, 175, -90, "F", laenge=65, label_seite=1))
    e.append(punkt(xA, 175))
    e.append(text(xA - 10, 192, "A", "#000000", 17, anker="end"))
    e.append(punkt(250, 100, 3.2))
    e.append(text(258, 92, "B", "#000000", 17, anker="start"))

    e = abb.ebene("nullsystem", "Nullsystem in B ergänzen")
    e.append(text(300, 175, "[=]", "#000000", 30, italic=False))
    e.append(koerper(330))
    xA2, xB2 = xA + 330, 580
    e.append(strichpunkt(xA2, 50, xA2, 300))
    e.append(strichpunkt(xB2, 50, xB2, 300))
    e.append(kraft(xA2, 175, -90, "F", laenge=65, label_seite=1))
    e.append(punkt(xA2, 175))
    e.append(kraft(xB2, 100, -90, "F", laenge=65, label_seite=-1))
    e.append(kraft(xB2, 100, 90, "F", laenge=65, label_seite=1))           # von unten an B (Gegenkraft)
    e.append(punkt(xB2, 100))
    e.append(text(xB2 + 10, 92, "B", "#000000", 17, anker="start"))
    e.append(text(455, 300, "[F in A und Gegenkraft in B: Kräftepaar]", GRUEN, 14, italic=False))
    e.append(mass(xA2, 250, xB2, 250, "a", abstand=-16))

    e = abb.ebene("ecke", "Kraft an der Ecke mit Versatzmoment")
    dy = 300                                     # zweite Zeile, unter dem Nullsystem
    e.append(text(300, 175 + dy, "[=]", "#000000", 30, italic=False))
    e.append(platte([(350, 100 + dy), (580, 100 + dy), (580, 250 + dy), (350, 250 + dy)]))
    xB3 = 580
    e.append(strichpunkt(xB3, 25 + dy, xB3, 300 + dy))
    e.append(kraft(xB3, 100 + dy, -90, "F", laenge=65, label_seite=-1))
    e.append(punkt(xB3, 100 + dy))
    e.append(text(xB3 + 10, 92 + dy, "B", "#000000", 17, anker="start"))
    e.append(moment(460, 180 + dy, "", gegen_uhrzeiger=True, r=26, start=30, bogen=280))
    e.append(text(460, 230 + dy, "M = F a", ROT, 20))
    return abb.speichern(ZIEL / "versatz.svg")


# =====================================================================
# Träger an zwei Seilen: Schnittprinzip und Gleichgewicht im allgemeinen ebenen Kraftsystem
#   Seil 1 am linken Ende, Seil 2 bei 3/4 L, Gewicht G in der Mitte  ->  S1 = G/3, S2 = 2G/3
# =====================================================================
def traeger_seile():
    abb = Abbildung(1080, 440, "Träger an zwei Seilen")
    yd, yb, L = 50, 230, 360
    t = 6                                          # halbe Balkendicke

    def decke(e, dx):
        e.append(linie(80 + dx, yd, 540 + dx, yd, "#000000", STRICH["normal"]))
        xx = 82 + dx
        while xx < 540 + dx:
            e.append(linie(xx, yd, xx + 7, yd - 7, "#000000", STRICH["duenn"]))
            xx += 7

    x1, x2 = 120, 120 + 0.75 * L
    e = abb.ebene("system", "Träger an zwei Seilen")
    decke(e, 0)
    for x in (x1, x2):
        e.append(linie(x, yd, x, yb - t, "#000000", 1.8))
    e.append(balken(x1, yb, x1 + L, yb, dicke=2 * t))
    e.append(kraft(x1 + L / 2, yb, -90, "G", laenge=70, ziehend=True, label_seite=-1))
    e.append(text(x1 - 10, 120, "[Seil 1]", "#000000", 16, anker="end", italic=False))
    e.append(text(x2 + 10, 120, "[Seil 2]", "#000000", 16, anker="start", italic=False))

    e = abb.ebene("schnitte", "Schnitte durch die Seile")
    for x in (x1, x2):
        e.append(schnitt(x - 26, 150, x + 26, 150))

    dx = 520
    e = abb.ebene("freikoerper", "Freikörperbilder")
    f1, f2 = x1 + dx, x2 + dx
    yb2 = yb + 40
    decke(e, dx)
    for x, n in ((f1, "1"), (f2, "2")):
        e.append(linie(x, yd, x, yd + 45, "#000000", 1.8))
        e.append(schnitt(x - 20, yd + 45, x + 20, yd + 45))
        e.append(kraft(x, yd + 45, -90, f"S_{n}", laenge=48, ziehend=True, label_seite=1))
    e.append(balken(f1, yb2, f1 + L, yb2, dicke=2 * t))
    for x, n in ((f1, "1"), (f2, "2")):
        e.append(linie(x, yb2 - t, x, yb2 - 55, "#000000", 1.8))
        e.append(schnitt(x - 20, yb2 - 55, x + 20, yb2 - 55))
        e.append(kraft(x, yb2 - 55, 90, f"S_{n}", laenge=48, ziehend=True, label_seite=1))
    e.append(kraft(f1 + L / 2, yb2, -90, "G", laenge=70, ziehend=True, label_seite=-1))

    e = abb.ebene("mass", "Bemaßung")
    e.append(mass(f1, yb2 + t, f1 + L / 2, yb2 + t, "L/2", abstand=-92))
    e.append(mass(f1, yb2 + t, f2, yb2 + t, "3L/4", abstand=-122))
    e.append(koord_xy(dx + 60, 425, 36, 36))
    e.append(punkt(f1, yb2, 3))
    e.append(text(f1 - 10, yb2 + 22, "1", "#000000", 16, anker="end"))
    return abb.speichern(ZIEL / "traeger-seile.svg")


# =====================================================================
# Beispiel B01-3: Scheibe mit vier Kräften (VL 2013 Teil 1 S. 26–27)
#   F1 = F4 = F, F2 = 2F, F3 = 3F; F_R = 5F, M_R0 = −5cF, WL y = −3/4 x + 5/4 c
# =====================================================================
def scheibe_vier_kraefte():
    abb = Abbildung(720, 460, "Scheibe mit vier Kräften")
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
    xa, xb = -0.4, 6.6
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
    abb, e = _aufgabe("Stahlträger am Kran", 480, 290)
    yb, xm, l, h = 215, 230, 180, 120
    xa, xc = xm - l / 2, xm + l / 2
    t = 7
    e.append(balken(xm - 170, yb, xm + 170, yb, dicke=2 * t))
    A = (xm, yb - t - h)
    # Seile laufen um den Träger: je zwei senkrechte Striche über die Trägerhöhe
    for x in (xa, xc):
        e.append(linie(x - 3, yb - t, x - 3, yb + t, "#000000", 1.6))
        e.append(linie(x + 3, yb - t, x + 3, yb + t, "#000000", 1.6))
        e.append(linie(x, yb - t, *A, "#000000", 1.8))
    e.append(festlager(*A, groesse=15, drehung=180))
    e.append(text(A[0] + 26, A[1] - 6, "A", GRUEN, anker="start"))
    e.append(text((xa + A[0]) / 2 - 14, (yb - t + A[1]) / 2, "[Seil 1]", "#000000", 14, anker="end", italic=False))
    e.append(text((xc + A[0]) / 2 + 14, (yb - t + A[1]) / 2, "[Seil 2]", "#000000", 14, anker="start", italic=False))
    e.append(mass(xa, yb + t, xc, yb + t, "l", abstand=-30))
    e.append(mass(xm - 150, yb - t, xm - 150, A[1], "h", abstand=-18))
    e.append(linie(xm - 160, A[1], A[0] - 14, A[1], GRUEN, STRICH["duenn"]))
    e.append(text(xm + 150, yb - 30, "m", "#000000", 20))
    e.append(pfeil(430, 60, 430, 110, GRUEN, STRICH["normal"], (8, 5)))
    e.append(text(444, 76, "g", GRUEN, 18, anker="start"))
    return abb.speichern(ZIEL / "aufgabe-1-1-4.svg")


def aufgabe_1_1_5():
    abb, e = _aufgabe("Kiste an Seilen", 460, 350)
    H = (150, 60)
    l = 170
    th = math.radians(35)
    K = (H[0] + l * math.sin(th), H[1] + l * math.cos(th))
    e.append(deckenlager(*H, "A"))
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


def aufgabe_1_2_1(abb_zurueck=False):
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
    if abb_zurueck:
        return abb, P
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


def aufgabe_b01_4():
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
    return abb.speichern(ZIEL / "aufgabe-b01-4.svg")


def aufgabe_b01_5():
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
    return abb.speichern(ZIEL / "aufgabe-b01-5.svg")


def aufgabe_b01_4_raeumlich():
    """B01-4: Bolzen mit vier Kräften, räumliche Darstellung wie in der Vorlage (zum Abstrahieren)."""
    abb, e = _aufgabe("Bolzen mit vier Kräften (räumlich)", 520, 340)
    O = (250, 120)                           # Mitte Bolzenkopf
    hoehe = 90

    def R3(x, y, z=0.0):                    # schräge Parallelprojektion: y nach hinten rechts
        return (O[0] + x + 0.5 * y, O[1] - z - 0.42 * y)

    zb = -hoehe                              # Plattenoberkante
    platte_pts = [R3(-120, -90, zb), R3(130, -90, zb), R3(130, 90, zb), R3(-120, 90, zb)]
    e.append(polylinie(platte_pts, "#000000", STRICH["normal"], "#ececec", schliessen=True))
    unten = [(px, py + 14) for px, py in platte_pts]
    e.append(polylinie([platte_pts[0], unten[0], unten[1], platte_pts[1]], "#000000", STRICH["normal"], "#d9d9d9",
                       schliessen=True))
    e.append(polylinie([platte_pts[1], unten[1], unten[2], platte_pts[2]], "#000000", STRICH["normal"], "#cfcfcf",
                       schliessen=True))
    # Bolzen (Zylinder)
    r = 16
    oben, fuss = R3(0, 0, 0), R3(0, 0, zb)
    e.append(polylinie([(oben[0] - r, oben[1]), (fuss[0] - r, fuss[1]), (fuss[0] + r, fuss[1]), (oben[0] + r, oben[1])],
                       "#000000", STRICH["normal"], "#d9d9d9"))
    e.append(f'<ellipse cx="{fuss[0]:.1f}" cy="{fuss[1]:.1f}" rx="{r}" ry="6" fill="#d9d9d9" stroke="#000" '
             f'stroke-width="1.25"/>')
    e.append(polylinie([(oben[0] - r, oben[1]), (fuss[0] - r, fuss[1]), (fuss[0] + r, fuss[1]), (oben[0] + r, oben[1])],
                       None, fuellung="#d9d9d9"))
    e.append(linie(oben[0] - r, oben[1], fuss[0] - r, fuss[1], "#000000", STRICH["normal"]))
    e.append(linie(oben[0] + r, oben[1], fuss[0] + r, fuss[1], "#000000", STRICH["normal"]))
    e.append(f'<ellipse cx="{oben[0]:.1f}" cy="{oben[1]:.1f}" rx="{r}" ry="6" fill="#ececec" stroke="#000" '
             f'stroke-width="1.25"/>')
    # Achsen in der Kraftebene
    for (x, y), lab in (((200, 0), "x"), ((0, 170), "y")):
        e.append(strichpunkt(*R3(-x * 0.9, -y * 0.55), *R3(x, y), GRAU))
        e.append(pfeil(*R3(x * 0.85, y * 0.85), *R3(x, y), GRUEN, STRICH["normal"], (8, 5)))
        px, py = R3(x, y)
        e.append(text(px + 8, py, lab, GRUEN, 17, anker="start"))
    # Kräfte in der x-y-Ebene am Bolzenkopf
    L = 130
    for w, name, lx, ly in ((-30, "F_1", 12, 8), (-90, "F_2", -16, 4), (240, "F_3", -18, 2), (180, "F_4", 0, -16)):
        ex, ey = L * math.cos(math.radians(w)), L * math.sin(math.radians(w))
        E = R3(ex, ey)
        e.append(vektor(*O, *E))
        e.append(text(E[0] + lx, E[1] + ly, name, ROT, anker="middle"))
    # Winkel in der Ebene (projizierte Kreisbögen)
    for von, bis, rad, lab in ((-30, 0, 85, "30°"), (180, 240, 75, "60°")):
        pts = [R3(rad * math.cos(math.radians(von + (bis - von) * k / 20)),
                  rad * math.sin(math.radians(von + (bis - von) * k / 20))) for k in range(21)]
        e.append(polylinie(pts, GRUEN, STRICH["duenn"]))
        mx, my = R3((rad + 16) * math.cos(math.radians((von + bis) / 2)), (rad + 16) * math.sin(math.radians((von + bis) / 2)))
        e.append(text(mx, my, lab, GRUEN, 15))
    return abb.speichern(ZIEL / "aufgabe-b01-4-raeumlich.svg")


def aufgabe_b01_6():
    """B01-6: Autokran mit Gegengewicht (Kippen)."""
    abb, e = _aufgabe("Autokran", 640, 380)
    m = 52                                   # px je m
    yb = 300                                 # Boden (Radaufstand)
    xA = 50
    xD, xC = xA + 4 * m, xA + 5.5 * m
    xE = xD + 3.0 * m                        # DE beliebig gezeichnet (gesucht)
    xB = xE + 2 * m
    # Boden
    e.append(linie(20, yb, 620, yb, "#000000", STRICH["normal"]))
    xx = 22
    while xx < 620:
        e.append(linie(xx, yb, xx - 7, yb + 7, "#000000", STRICH["duenn"]))
        xx += 8
    # Fahrzeug
    rad = 20
    e.append(platte([(xD - 40, yb - 2 * rad - 18), (xD - 22, yb - 2 * rad - 70), (xD + 40, yb - 2 * rad - 70),
                     (xD + 46, yb - 2 * rad - 36), (xB + 30, yb - 2 * rad - 36), (xB + 30, yb - 2 * rad + 4),
                     (xD - 40, yb - 2 * rad + 4)], "#e6e6e6"))
    for x in (xD, xE):
        e.append(kreis(x, yb - rad, rad, "#000000", "#cfcfcf", 1.4))
        e.append(kreis(x, yb - rad, 5, "#000000", "#ffffff", 1))
    # Ausleger (Fachwerk vereinfacht) vom Drehpunkt bis über die Last
    P = (xE - 10, yb - 2 * rad - 60)
    S = (xA, yb - 230)
    e.append(linie(*P, *S, "#000000", 2))
    e.append(linie(P[0] + 22, P[1] - 30, S[0] + 30, S[1] - 34, "#000000", 2))
    n = 7
    for k in range(n + 1):
        t = k / n
        a1 = (P[0] + (S[0] - P[0]) * t, P[1] + (S[1] - P[1]) * t)
        a2 = (P[0] + 22 + (S[0] + 30 - P[0] - 22) * t, P[1] - 30 + (S[1] - 34 - P[1] + 30) * t)
        e.append(linie(*a1, *a2, "#000000", 1))
        if k < n:
            t2 = (k + 1) / n
            b2 = (P[0] + 22 + (S[0] + 30 - P[0] - 22) * t2, P[1] - 30 + (S[1] - 34 - P[1] + 30) * t2)
            e.append(linie(*a1, *b2, "#000000", 0.8))
    e.append(kreis(*P, 5, "#000000", "#ffffff", 1.2))
    e.append(linie(S[0] + 15, S[1] - 17, xB - 30, P[1] - 30, "#000000", 1))
    # Gegengewicht B
    e.append(platte([(xB - 30, yb - 2 * rad - 140), (xB + 30, yb - 2 * rad - 140), (xB + 30, yb - 2 * rad - 36),
                     (xB - 30, yb - 2 * rad - 36)], "#bdbdbd"))
    e.append(text(xB, yb - 2 * rad - 118, "B", "#000000", 18))
    # Last A
    e.append(linie(xA, S[1], xA, yb - 130, "#000000", 1.2))
    e.append(platte([(xA - 18, yb - 130), (xA + 18, yb - 130), (xA + 18, yb - 92), (xA - 18, yb - 92)], "#bdbdbd"))
    e.append(text(xA, yb - 111, "A", "#000000", 18))
    # Kräfte
    e.append(kraft(xA, yb - 92, -90, "F_3", laenge=55, ziehend=True, label_seite=1))
    e.append(punkt(xC, yb - 2 * rad - 30, 2.6))
    e.append(text(xC + 10, yb - 2 * rad - 42, "C", "#000000", 16, anker="start"))
    e.append(kraft(xC, yb - 2 * rad - 30, -90, "F_1", laenge=60, ziehend=True, label_seite=-1))
    e.append(kraft(xB, yb - 2 * rad - 90, -90, "F_2", laenge=70, ziehend=True, label_seite=1))
    # Punkte D, E und Bemaßung
    for x, lab in ((xD, "D"), (xE, "E")):
        e.append(punkt(x, yb, 2.6))
        e.append(text(x, yb + 16, lab, "#000000", 16))
    e.append(mass(xA, yb, xD, yb, "a", abstand=-48))
    e.append(mass(xD, yb, xC, yb, "b", abstand=-48))
    e.append(mass(xE, yb, xB, yb, "c", abstand=-48))
    return abb.speichern(ZIEL / "aufgabe-b01-6.svg")


def aufgabe_b01_7():
    """B01-7: Mast mit drei Seilkräften."""
    abb, e = _aufgabe("Mast mit drei Seilen", 440, 330)
    T = (220, 60)
    yb = 300
    e.append(balken(T[0], T[1], T[0], yb, dicke=8))
    e.append(linie(80, yb, 360, yb, "#000000", STRICH["normal"]))
    xx = 82
    while xx < 360:
        e.append(linie(xx, yb, xx - 8, yb + 8, "#000000", STRICH["duenn"]))
        xx += 8
    for w, name, laenge, seite in ((-150, "F_1", 150, 1), (-60, "F_2", 110, -1), (-39, "F_3", 125, -1)):
        e.append(kraft(*T, w, name, laenge=laenge, ziehend=True, label_seite=seite, label_pos=0.95))
    e.append(linie(T[0], T[1], T[0], T[1] + 120, GRAU, STRICH["duenn"], strich="4 3"))
    e.append(winkelbogen(*T, 55, -150, -90, "60°"))
    e.append(winkelbogen(*T, 82, -90, -60, "30°"))
    e.append(winkelbogen(*T, 40, -90, -39, "α"))
    e.append(punkt(*T, 2.6))
    return abb.speichern(ZIEL / "aufgabe-b01-7.svg")


# =====================================================================
# Gleichgewicht im zentralen Kraftsystem: Mast mit drei Seilen (Aufgabe 1.7)
#   F1 = 5 kN (60° links der Senkrechten), F2 = 4 kN (30° rechts), F3 = 3 kN unter α;
#   α so, dass die Resultierende der Seilkräfte in Mastrichtung zeigt (sin α = 0,777 → α = 51°)
# =====================================================================
def mast_gleichgewicht():
    abb = Abbildung(1180, 380, "Mast mit drei Seilen: Gleichgewicht")
    s = 21                                         # px je kN
    al = math.degrees(math.asin((5 * math.sin(math.radians(60)) - 4 * math.sin(math.radians(30))) / 3))
    seile = ((-150, "F_1", 5, 1), (-60, "F_2", 4, -1), (-90 + al, "F_3", 3, -1))
    FR = sum(F * math.cos(math.radians(w + 90)) for w, _, F, _ in seile)

    def boden(e, x0, x1, y):
        e.append(linie(x0, y, x1, y, "#000000", STRICH["normal"]))
        xx = x0 + 2
        while xx < x1:
            e.append(linie(xx, y, xx - 8, y + 8, "#000000", STRICH["duenn"]))
            xx += 8

    def seilkraefte(e, T, winkel=True):
        for w, name, F, seite in seile:
            e.append(kraft(*T, w, name, laenge=F * s, ziehend=True, label_seite=seite, label_pos=0.95))
        if winkel:
            e.append(linie(T[0], T[1], T[0], T[1] + 90, GRAU, STRICH["duenn"], strich="4 3"))
            e.append(winkelbogen(*T, 46, -150, -90, "60°"))
            e.append(winkelbogen(*T, 70, -90, -60, "30°"))
            e.append(winkelbogen(*T, 30, -90, -90 + al, "α"))

    def krafteck(e, x0, y0, schluss):
        P = (x0, y0)
        for w, name, F, seite in seile:
            Q = (P[0] + F * s * math.cos(math.radians(w)), P[1] - F * s * math.sin(math.radians(w)))
            lx = -16 if name == "F_1" else 16
            e.append(vektor(*P, *Q, name, lx=lx, ly=-6))
            P = Q
        if schluss:
            e.append(vektor(*P, x0, y0, "F_B", lx=18))
            e.append(text(x0 - 10, y0 + FR * s + 34, "F_R = 0", ROT, 17))
        else:
            e.append(vektor(x0, y0, *P, "F_R", lx=-20, farbe="#9b0000"))
        e.append(text(x0 - 10, y0 + FR * s + 14, "[Krafteck]", "#555555", 14, italic=False))

    T, yb = (200, 70), 320
    e = abb.ebene("system", "Mast mit drei Seilen")
    boden(e, 70, 330, yb)
    e.append(balken(T[0], T[1], T[0], yb, dicke=8))
    seilkraefte(e, T)
    e.append(punkt(*T, 2.6))

    e = abb.ebene("resultierende", "Resultierende der Seilkräfte")
    # Resultierende greift im zentralen Punkt (Mastspitze) an und zeigt längs der Mastachse nach unten
    e.append(kraft(*T, -90, "F_R", laenge=FR * s, ziehend=True, label_seite=1, label_pos=0.75, label_abstand=10,
                   farbe="#9b0000"))
    krafteck(e, 470, 60, False)

    T2, yfuss, yb2 = (740, 70), 225, 345
    e = abb.ebene("freischnitt", "Schnitt am Boden")
    e.append(balken(T2[0], T2[1], T2[0], yfuss, dicke=8))
    seilkraefte(e, T2, winkel=False)
    e.append(punkt(*T2, 2.6))
    e.append(schnitt(T2[0] - 22, yfuss + 4, T2[0] + 22, yfuss + 4))
    e.append(kraft(T2[0], yfuss + 4, 90, "F_B", laenge=40, label_seite=-1, label_pos=0.5))
    boden(e, T2[0] - 110, T2[0] + 110, yb2)
    e.append(schnitt(T2[0] - 22, yb2 - 4, T2[0] + 22, yb2 - 4))
    e.append(kraft(T2[0], yb2 - 4, -90, "F_B", laenge=40, label_seite=1, label_pos=0.5))
    e.append(text(T2[0] - 70, 160, "[Mast]", "#000000", 16, anker="end", italic=False))
    e.append(text(T2[0] + 120, yb2 + 22, "[Boden]", "#000000", 16, anker="start", italic=False))

    e = abb.ebene("krafteck-zu", "Geschlossenes Krafteck")
    krafteck(e, 1010, 60, True)
    return abb.speichern(ZIEL / "mast-gleichgewicht.svg")


# =====================================================================
# Einstieg Moment: Spielplatz-Wippe
#   G1 = 400 N bei a1 = 1,2 m links, G2 = 300 N bei a2 = 1,6 m rechts → G1 a1 = G2 a2 = 480 Nm
# =====================================================================
def wippe():
    abb = Abbildung(760, 370, "Spielplatz-Wippe")
    D = (380, 200)
    x1, x2 = D[0] - 180, D[0] + 240                 # 150 px je m

    e = abb.ebene("wippe", "Wippe mit zwei Kindern")
    e.append(polylinie([(D[0], D[1] + 5), (D[0] - 26, 250), (D[0] + 26, 250)], "#444444", STRICH["normal"],
                       "#e6e6e6", schliessen=True))
    e.append(linie(320, 250, 440, 250, "#000000", STRICH["normal"]))
    xx = 322
    while xx < 440:
        e.append(linie(xx, 250, xx - 7, 257, "#000000", STRICH["duenn"]))
        xx += 7
    e.append(balken(120, D[1], 645, D[1], dicke=10))
    for x, b, h, r, name in ((x1, 32, 46, 12, "Kind 1"), (x2, 26, 38, 10, "Kind 2")):
        e.append(polylinie([(x - b / 2, D[1] - 5), (x - b / 2, D[1] - 5 - h), (x + b / 2, D[1] - 5 - h),
                            (x + b / 2, D[1] - 5)], "#444444", STRICH["normal"], "#d9d9d9", schliessen=True))
        e.append(kreis(x, D[1] - 5 - h - r - 1, r, "#444444", "#d9d9d9"))
        e.append(text(x, D[1] - 5 - h - 2 * r - 16, f"[{name}]", "#000000", 16, italic=False))
    e.append(punkt(*D, 3))
    e.append(text(D[0] + 14, D[1] + 22, "D", "#000000", 17, anker="start"))

    e = abb.ebene("kraefte", "Gewichtskräfte und Hebelarme")
    e.append(kraft(x1, D[1] + 5, -90, "G_1", laenge=80, ziehend=True, label_seite=-1))
    e.append(kraft(x2, D[1] + 5, -90, "G_2", laenge=60, ziehend=True, label_seite=1))
    e.append(mass(x1, 75, D[0], 75, "a_1", abstand=0, hilfslinien=False))
    e.append(mass(D[0], 75, x2, 75, "a_2", abstand=0, hilfslinien=False))
    for x, y_bis in ((x1, 92), (x2, 102)):
        e.append(linie(x, 65, x, y_bis, FARBE["mass"], STRICH["duenn"]))
    e.append(linie(D[0], 65, D[0], D[1] - 8, FARBE["mass"], STRICH["duenn"], strich="4 3"))

    e = abb.ebene("momente", "Drehwirkungen um D")
    e.append(moment(*D, "", gegen_uhrzeiger=True, r=262, start=164, bogen=30))
    e.append(text(115, 305, "M_1 = G_1 a_1", ROT, 17, anker="middle"))
    e.append(moment(*D, "", gegen_uhrzeiger=False, r=290, start=16, bogen=30))
    e.append(text(655, 320, "M_2 = G_2 a_2", ROT, 17, anker="middle"))

    e = abb.ebene("gleichgewicht", "Gleichgewicht der Momente")
    e.append(text(D[0], 300, "G_1 a_1 = G_2 a_2", "#000000", 19))
    e.append(text(D[0], 330, "400 N · 1,2 m = 300 N · 1,6 m", "#444444", 16, italic=False))
    return abb.speichern(ZIEL / "wippe.svg")


# =====================================================================
# Zusammenfassung Woche 1: sechs Kacheln
# =====================================================================
def zusammenfassung():
    W, H, rand = 300, 220, 15
    abb = Abbildung(3 * W + 4 * rand, 2 * H + 3 * rand, "Zusammenfassung: Kräfte, Momente, Gleichgewicht")

    def kachel(e, spalte, zeile, titel, formel):
        x, y = rand + spalte * (W + rand), rand + zeile * (H + rand)
        e.append(polylinie([(x, y), (x + W, y), (x + W, y + H), (x, y + H)], "#c8c8c8", 1.2, "#fafafa",
                           schliessen=True))
        e.append(text(x + 14, y + 22, f"[{titel}]", "#000000", 17, anker="start", italic=False))
        zeilen = formel if isinstance(formel, (list, tuple)) else [formel]
        for k, z in enumerate(reversed(zeilen)):
            e.append(text(x + W / 2, y + H - 20 - 24 * k, z, ROT, 17))
        return x, y

    e = abb.ebene("k-kraft", "Kraft")
    x, y = kachel(e, 0, 0, "Kraft als Vektor", ["F_x = F cos α,  F_y = F sin α", "F = √(F_x² + F_y²)"])
    O = (x + 70, y + 142)
    e.append(koord_xy(*O, 170, 100))
    E = (O[0] + 140, O[1] - 80)
    e.append(linie(*E, E[0], O[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(linie(*E, O[0], E[1], GRAU, STRICH["duenn"], strich="4 3"))
    e.append(vektor(*O, *E, "F", lx=-14, ly=-8))
    e.append(winkelbogen(*O, 40, 0, math.degrees(math.atan2(80, 140)), "α"))

    e = abb.ebene("k-axiome", "Axiome und Schnittprinzip")
    x, y = kachel(e, 1, 0, "Axiome, Schnittprinzip", ["actio = reactio"])
    yy, x0, x1, xs, d = y + 95, x + 40, x + 260, x + 150, 34
    e.append(balken(x0, yy, xs - d, yy, dicke=10))
    e.append(balken(xs + d, yy, x1, yy, dicke=10))
    e.append(schnitt(xs - d, yy - 14, xs - d, yy + 14))
    e.append(schnitt(xs + d, yy - 14, xs + d, yy + 14))
    e.append(kraft(xs - d, yy, 0, "F_i", laenge=30, ziehend=True, label_seite=-1))
    e.append(kraft(xs + d, yy, 180, "F_i", laenge=30, ziehend=True, label_seite=1))
    e.append(kraft(x0, yy, 180, "", laenge=30, ziehend=True))
    e.append(kraft(x1, yy, 0, "", laenge=30, ziehend=True))
    e.append(hinweis(x + W / 2, y + 150, "Freikörperbild: alle Kräfte antragen", anker="middle", groesse=13))

    e = abb.ebene("k-zentral", "Zentrales Kraftsystem")
    x, y = kachel(e, 2, 0, "Zentrales Kraftsystem", ["Σ F_x = 0,   Σ F_y = 0"])
    P0 = (x + 110, y + 50)
    P1 = (P0[0], P0[1] + 100)
    P2 = (P1[0] + 70, P1[1])
    e.append(vektor(*P0, *P1, "m g", lx=-24))
    e.append(vektor(*P1, *P2, "F", ly=16))
    e.append(vektor(*P2, *P0, "F_S", lx=24))
    e.append(hinweis(x + 200, y + 100, "geschlossenes", groesse=13))
    e.append(hinweis(x + 200, y + 118, "Krafteck", groesse=13))

    e = abb.ebene("k-moment", "Moment")
    x, y = kachel(e, 0, 1, "Moment, Kräftepaar", ["M = F b = x F_y − y F_x"])
    e.append(platte([(x + 30, y + 55), (x + 150, y + 55), (x + 150, y + 150), (x + 30, y + 150)]))
    e.append(kraft(x + 55, y + 102, 90, "F", laenge=40, ziehend=True, label_seite=1))
    e.append(kraft(x + 125, y + 102, -90, "F", laenge=40, ziehend=True, label_seite=1))
    e.append(text(x + 175, y + 102, "[=]", "#000000", 24, italic=False))
    e.append(platte([(x + 195, y + 55), (x + 285, y + 55), (x + 285, y + 150), (x + 195, y + 150)]))
    e.append(moment(x + 240, y + 102, "", gegen_uhrzeiger=False, r=20, start=150, bogen=280))

    e = abb.ebene("k-versatz", "Versatzmoment")
    x, y = kachel(e, 1, 1, "Kraft parallel verschieben", ["+ Versatzmoment  M = F a"])
    e.append(platte([(x + 30, y + 60), (x + 130, y + 60), (x + 130, y + 155), (x + 30, y + 155)]))
    e.append(kraft(x + 70, y + 112, -90, "F", laenge=40, label_seite=1))
    e.append(text(x + 150, y + 108, "[=]", "#000000", 24, italic=False))
    e.append(platte([(x + 170, y + 60), (x + 270, y + 60), (x + 270, y + 155), (x + 170, y + 155)]))
    e.append(kraft(x + 270, y + 60, -90, "F", laenge=40, label_seite=-1))
    e.append(moment(x + 215, y + 112, "", gegen_uhrzeiger=True, r=18, start=30, bogen=280))

    e = abb.ebene("k-gleichgewicht", "Gleichgewicht allgemein")
    x, y = kachel(e, 2, 1, "Gleichgewicht in der Ebene", ["Σ F_x = 0,  Σ F_y = 0,  Σ M = 0"])
    yb = y + 120
    e.append(balken(x + 40, yb, x + 260, yb, dicke=10))
    for xs, lab, seite in ((x + 40, "S_1", 1), (x + 205, "S_2", -1)):
        e.append(kraft(xs, yb - 5, 90, lab, laenge=45, ziehend=True, label_seite=seite))
    e.append(kraft(x + 150, yb + 5, -90, "G", laenge=40, ziehend=True, label_seite=-1))
    return abb.speichern(ZIEL / "zusammenfassung-grundlagen.svg")


if __name__ == "__main__":
    for fn in (einordnung, kraft_vektor, axiome, resultierende_zwei_kraefte, seil_masse, moment_grafik, versatz_grafik,
               traeger_seile, mast_gleichgewicht, wippe, zusammenfassung,
               scheibe_vier_kraefte, aufgabe_1_1_3, aufgabe_1_1_4, aufgabe_1_1_5, aufgabe_1_2_1, aufgabe_1_2_4,
               aufgabe_b01_4, aufgabe_b01_5, aufgabe_b01_4_raeumlich, aufgabe_b01_6, aufgabe_b01_7):
        print(fn())

"""Grafiken zum Kapitel Schnittgrößen.

Aufruf:  python werkzeuge/grafiken_schnittgroessen.py
Ergebnis: grafiken/schnittgroessen/*.svg (Inkscape-Ebenen = Scroll-Schritte)
"""

import math
from pathlib import Path

from tmzeichnen import (FARBE, STRICH, Abbildung, balken, einspannung, festlager, gelenk, koordinaten, kraft, kreis,
                        linie, loslager, mass, moment, nummer, pfeil, polylinie, schnittlinie, schnittufer,
                        streckenlast, text, verlauf, winkelbogen)

ZIEL = Path(__file__).resolve().parent.parent / "grafiken" / "schnittgroessen"
R, B_ = FARBE["reaktion"], FARBE["last"]


# =====================================================================
# Vorzeichenkonvention: positives / negatives Schnittufer
# =====================================================================
def vorzeichen():
    """Einfeldträger (Festlager A, Loslager B, Kraft F) mit einem Schnitt S in der Mitte;
    darunter beide Teilsysteme so weit auseinander, dass sich die Schnittgrößen nicht überdecken."""
    abb = Abbildung(860, 440, "Vorzeichenkonvention der Schnittgrößen")
    t = 3.5
    x0, x1 = 190, 670
    xs = (x0 + x1) / 2
    xF = x0 + (x1 - x0) / 4
    y = 120

    e = abb.ebene("system", "Träger mit Lagern")
    e.append(balken(x0, y, x1, y))
    e.append(kraft(xF, y - t, -90, "F", laenge=55, label_seite=-1))
    e.append(festlager(x0, y + t, label="A", label_pos=(-24, 14)))
    e.append(loslager(x1, y + t, label="B", label_pos=(24, 14)))
    e.append(koordinaten(30, 40, 34, "x", "z"))

    e = abb.ebene("schnitt", "Schnitt in der Mitte")
    e.append(schnittlinie(xs, y, 48))
    e.append(text(xs + 12, y - 28, "S", FARBE["mass"], 15))

    # Teilsysteme: Lager durch Reaktionen ersetzt; die Teile behalten ihre Länge und werden um d
    # nach links bzw. rechts geschoben, damit sich N, Q, M der beiden Ufer nicht überdecken
    yt, d = 320, 110
    xl, xr = xs - d, xs + d
    e = abb.ebene("getrennt", "Teilsysteme")
    e.append(balken(x0 - d, yt, xl, yt))
    e.append(balken(xr, yt, x1 + d, yt))
    e.append(kraft(xF - d, yt - t, -90, "F", laenge=55, label_seite=-1))
    e.append(kraft(x0 - d - 4, yt, 0, "F_{AH}", farbe=R, laenge=46, label_seite=1))
    e.append(kraft(x0 - d, yt + t, 90, "F_{AV}", farbe=R, laenge=48, label_seite=1))
    e.append(kraft(x1 + d, yt + t, 90, "F_B", farbe=R, laenge=48, label_seite=-1))
    e.append(koordinaten(30, yt - 95, 34, "x", "z"))
    e.append(text(xl, yt - 92, "[linkes Teilsystem]", "#444444", 14, anker="end", italic=False))
    e.append(text(xr, yt - 92, "[rechtes Teilsystem]", "#444444", 14, anker="start", italic=False))

    e = abb.ebene("ufer-pos", "positives Schnittufer")
    e.append(schnittufer(xl, yt, positiv=True, N="N(x)", Q="Q(x)", M="M(x)"))
    e.append(linie(xl, yt + 26, xl, yt + 58, "#444444", 0.9))
    e.append(text(xl, yt + 72, "[positives Schnittufer]", "#444444", 14, italic=False))

    e = abb.ebene("ufer-neg", "negatives Schnittufer")
    e.append(schnittufer(xr, yt, positiv=False, N="N(x)", Q="Q(x)", M="M(x)"))
    e.append(linie(xr, yt + 26, xr, yt + 58, "#444444", 0.9))
    e.append(text(xr, yt + 72, "[negatives Schnittufer]", "#444444", 14, italic=False))

    return abb.speichern(ZIEL / "vorzeichen.svg")


# =====================================================================
# Einstieg: reine Biegung – Träger auf zwei Stützen mit gleich großen, entgegengesetzten Momenten M0
#   F_A = F_B = 0, N = Q = 0, M(x) = M0 konstant, Biegelinie ein Kreisbogen
# =====================================================================
def reine_biegung():
    """Träger auf zwei Stützen, an A ein Moment gegen den Uhrzeigersinn, an B gleich groß im
    Uhrzeigersinn: Der Träger biegt sich nach OBEN (für die Demonstration mit dem Zeigestab).
    F_A = F_B = 0, N = Q = 0, M(x) = -M0 konstant (oben gezogen), Biegelinie ein Kreisbogen."""
    from tmzeichnen import stabzug, schnitt
    abb = Abbildung(760, 560, "Reine Biegung")
    x0, x1, y, t = 130, 630, 150, 3.5
    xm, c = (x0 + x1) / 2, x1 - x0
    f = 42                                        # Durchbiegung nach oben (stark überhöht)
    Rk = (c * c / 4 + f * f) / (2 * f)
    yc = y - f + Rk                               # Kreismittelpunkt (unterhalb)
    def yb(xp):
        return yc - math.sqrt(Rk ** 2 - (xp - xm) ** 2)
    def bogen(xa, xb, n=60):
        return [(xa + (xb - xa) * i / n, yb(xa + (xb - xa) * i / n)) for i in range(n + 1)]
    hl = "#b0b6bd"

    def lagermomente(e):
        e.append(moment(x0, y, "", gegen_uhrzeiger=True, r=22, start=-20, bogen=250))
        e.append(text(x0 - 26, y - 30, "M_0", FARBE["last"], anker="end"))
        e.append(moment(x1, y, "", gegen_uhrzeiger=False, r=22, start=200, bogen=250))
        e.append(text(x1 + 26, y - 30, "M_0", FARBE["last"], anker="start"))

    e = abb.ebene("system", "Träger mit zwei Momenten")
    e.append(balken(x0, y, x1, y))
    e.append(festlager(x0, y + t, label="A", label_pos=(-24, 14)))
    e.append(loslager(x1, y + t, label="B", label_pos=(24, 14)))
    e.append(mass(x0, y, x1, y, "L", abstand=-62))
    e.append(koordinaten(30, 40, 30, "x", "z"))

    e = abb.ebene("momente", "Momente an den Lagern")
    lagermomente(e)

    # verformter Träger: Kreisbogen nach oben, unverformte Lage gestrichelt
    e = abb.ebene("verformt", "Biegelinie")
    e.append(linie(x0, y, x1, y, hl, 1.2, strich="6 4"))
    e.append(stabzug(bogen(x0, x1), dicke=7))
    e.append(festlager(x0, y + t, label="A", label_pos=(-24, 14)))
    e.append(loslager(x1, y + t, label="B", label_pos=(24, 14)))
    lagermomente(e)
    e.append(text(xm, y - f - 38, "[oben gezogen, unten gedrückt]", "#444444", 14, italic=False))
    e.append(text(xm - 160, y - 7, "[Kreisbogen]", "#444444", 14, italic=False))
    e.append(koordinaten(30, 40, 30, "x", "z"))

    # Mittelstück herausschneiden
    ds = 46
    xa, xb = xm - ds, xm + ds
    def radial(xp):
        yp = yb(xp)
        ux, uy = (xp - xm) / Rk, (yp - yc) / Rk
        return (xp - 22 * ux, yp - 22 * uy), (xp + 22 * ux, yp + 22 * uy)
    e = abb.ebene("ausschnitt", "Mittelstück")
    for xp in (xa, xb):
        p1, p2 = radial(xp)
        e.append(schnitt(*p1, *p2))
    yv = 330
    wv = 240
    e.append(linie(xa, yb(xa) + 24, xm - wv / 2, yv - 40, hl, 0.9, strich="4 3"))
    e.append(linie(xb, yb(xb) + 24, xm + wv / 2, yv - 40, hl, 0.9, strich="4 3"))
    # vergrößertes Stück: nach oben gekrümmt (Krümmung überhöht), Momente an beiden Ufern
    fv = 16
    Rv = (wv * wv / 4 + fv * fv) / (2 * fv)
    ycv = yv - fv + Rv
    stueck = [(xm - wv / 2 + wv * i / 40,
               ycv - math.sqrt(Rv ** 2 - (wv * i / 40 - wv / 2) ** 2)) for i in range(41)]
    e.append(stabzug(stueck, dicke=14))
    S_ = FARBE["schnitt"]
    xl, yl = stueck[0]
    xr, yr = stueck[-1]
    e.append(moment(xl, yl, "", gegen_uhrzeiger=True, r=26, start=-50, bogen=230, farbe=S_))
    e.append(text(xl - 34, yl - 30, "M_0", S_, anker="end"))
    e.append(moment(xr, yr, "", gegen_uhrzeiger=False, r=26, start=230, bogen=230, farbe=S_))
    e.append(text(xr + 34, yr - 30, "M_0", S_, anker="start"))
    e.append(text(xm, yv + 52, "[gleich große, entgegengesetzte Momente halten das Stück gebogen]",
                  "#444444", 14, italic=False))

    # konstanter Momentenverlauf (negativ: oben gezogen), positive Werte oberhalb der Achse
    e = abb.ebene("verlauf-M", "Momentenverlauf")
    e.append(verlauf(x0, [(0, -1), (c, -1)], 34, 240, c, "M(x)", werte=[(c / 2, -1, "−M_0", "middle")]))
    return abb.speichern(ZIEL / "reine-biegung.svg")


# =====================================================================
# Bereiche und Rechenschema: Musterträger mit allen Arten von Bereichsgrenzen
#   A (Festlager) bei 0, F = 2qa bei a, M0 = 2qa² (gegen Uhrzeiger) bei 2a,
#   q von 3a bis 5a, B (Loslager) bei 4a  ->  F_AV = 2qa, F_B = 2qa
# =====================================================================
def bereiche_muster():
    a = 100
    x0, y, t = 110, 140, 3.5
    X = lambda k: x0 + k * a
    abb = Abbildung(720, 600, "Bereiche und Rechenschema")
    hinweis = FARBE["hinweis"]

    e = abb.ebene("traeger", "Musterträger")
    e.append(balken(X(0), y, X(5), y))
    e.append(festlager(X(0), y + t, label="A", label_pos=(-24, 14)))
    e.append(loslager(X(4), y + t, label="B", label_pos=(-24, 14)))
    e.append(kraft(X(1), y - t, -90, "F", laenge=55, label_seite=-1))
    e.append(moment(X(2), y, "", gegen_uhrzeiger=True, r=20, start=-40, bogen=260))
    e.append(text(X(2) + 24, y - 30, "M_0", FARBE["last"], anker="start"))
    e.append(streckenlast(X(3), X(5), y - t, 30, label="q", n=10))
    for k, lab in ((1, "a"), (2, "a"), (3, "a"), (4, "a"), (5, "a")):
        e.append(mass(X(k - 1), y, X(k), y, lab, abstand=-76))
    e.append(koordinaten(26, 40, 30, "x", "z"))

    e = abb.ebene("grenzen", "Bereichsgrenzen")
    gruende = {0: "[Anfang]", 1: "[Einzelkraft]", 2: "[Einzelmoment]", 3: "[Beginn q]", 4: "[Lager]",
               5: "[Ende]"}
    for k, g in gruende.items():
        e.append(linie(X(k), y - 70, X(k), y + 36, hinweis, 0.9, strich="4 3"))
        e.append(text(X(k), y - 80, g, "#444444", 13, italic=False))

    e = abb.ebene("bereiche", "Bereiche und Koordinaten")
    for k, n in enumerate(["I", "II", "III", "IV", "V"]):
        e.append(nummer(X(k) + a / 2, y + 48, n, r=11.5))
        e.append(koordinaten(X(k), y, 30, f"x_{k + 1}", nur_x=True))

    # Schnitt in Bereich II, linkes Teilsystem
    xs = X(1) + 0.5 * a
    yt = 355
    e = abb.ebene("schnitt", "Schnitt im Bereich II")
    e.append(schnittlinie(xs, y, 44))
    e.append(text(xs + 10, y - 26, "S", FARBE["mass"], 15))
    e.append(balken(X(0), yt, xs, yt))
    e.append(kraft(X(0) - 4, yt, 0, "F_{AH}", farbe=R, laenge=40, label_seite=-1))
    e.append(kraft(X(0), yt + t, 90, "F_{AV}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(X(1), yt - t, -90, "F", laenge=50, label_seite=-1))
    e.append(schnittufer(xs, yt, positiv=True, N="N(x_2)", Q="Q(x_2)", M="M(x_2)"))
    e.append(mass(X(0), yt, X(1), yt, "a", abstand=-64))
    e.append(mass(X(1), yt, xs, yt, "x_2", abstand=-64))
    e.append(koordinaten(26, yt - 70, 30, "x", "z"))
    e.append(text(X(0), yt - 90, "[linkes Teilsystem]", "#444444", 14, anker="start", italic=False))

    # Verläufe (positive Werte oberhalb der Achse), Einheiten qa bzw. qa²
    yQ, yM = 330, 470
    sQ, sM = 22, 26
    QP = [(0, 2), (1, 2), (1, 0), (3, 0), (4, -1), (4, 1), (5, 0)]
    MP = [(0, 0), (1, 2), (2, 2), (2, 0), (3, 0)] + [(3 + i / 10, -(i / 10) ** 2 / 2) for i in range(1, 11)] \
        + [(4 + i / 10, -(1 - i / 10) ** 2 / 2) for i in range(1, 11)]
    e = abb.ebene("verlauf-Q", "Querkraftverlauf")
    e.append(verlauf(X(0), [(k * a, v) for k, v in QP], sQ, yQ, 5 * a, "Q(x)",
                     werte=[(0.5 * a, 2, "[2]qa", "middle"), (4 * a - 8, -1, "[−]qa", "end"),
                            (4 * a + 8, 1, "qa", "start")]))
    e = abb.ebene("verlauf-M", "Momentenverlauf")
    e.append(verlauf(X(0), [(k * a, v) for k, v in MP], sM, yM, 5 * a, "M(x)",
                     werte=[(1.5 * a, 2, "[2]qa²", "middle"), (4 * a, -0.5, "[−]qa²/2", "middle")]))
    e = abb.ebene("grenzen-unten", "Bereichsgrenzen in den Verläufen")
    for k in range(6):
        e.append(linie(X(k), y + 40, X(k), yM + 50, hinweis, 0.6, strich="4 3"))
    return abb.speichern(ZIEL / "bereiche.svg")


# =====================================================================
# Kontrollregeln: Tafel Belastung -> Q -> M, eine Zeile je Regel (Ebene zeile-1 ... zeile-6)
# =====================================================================
def kontrollregeln():
    """Tafel Belastung -> Q -> M an vollständigen Einfeldträgern (A Festlager, B Loslager, L = 1).

    Zeilen 1–4: Einzelkraft, Einzelmoment, q konstant, q linear; abgesetzt Zeile 5: Beginn einer
    Streckenlast (Übergang zwischen Bereichen). Werte normiert (F = M0 = q = q0 = L = 1)."""
    abb = Abbildung(720, 590, "Kontrollregeln für die Verläufe")
    w, h = 170, 88                       # Feldbreite, Zeilenhöhe
    cL, cQ, cM = 40, 280, 510            # linke Kanten der Spalten
    grau = "#444444"
    n = 40
    xs = [i / n for i in range(n + 1)]
    links = [x / 2 for x in xs]          # 0 .. 0,5
    rechts = [0.5 + x / 2 for x in xs]   # 0,5 .. 1

    e = abb.ebene("kopf", "Spaltenköpfe")
    for c, txt, it in ((cL, "[Belastung]", False), (cQ, "[Querkraft ]Q(x)", True), (cM, "[Moment ]M(x)", True)):
        e.append(text(c + w / 2, 30, txt, "#222222", 15, italic=it))
    e.append(linie(20, 44, 700, 44, FARBE["hinweis"], 0.8))
    e.append(pfeil(cL + w + 18, 30, cQ - 18, 30, FARBE["hinweis"], 1.0, (8, 5)))
    e.append(pfeil(cQ + w + 18, 30, cM - 18, 30, FARBE["hinweis"], 1.0, (8, 5)))

    zeilen = [
        ("F", [(0, 0.5), (0.5, 0.5), (0.5, -0.5), (1, -0.5), (1, 0)], [(0, 0), (0.5, 0.25), (1, 0)],
         "[Sprung um ]F", "[Knick]"),
        ("M0", [(0, -1), (1, -1), (1, 0)], [(0, 0), (0.5, -0.5), (0.5, 0.5), (1, 0)],
         "[konstant, kein Sprung]", "[Sprung um ]M_0"),
        ("q", [(x, 0.5 - x) for x in xs], [(x, (x - x * x) / 2) for x in xs], "[linear]", "[Parabel]"),
        ("qlin", [(x, 1 / 6 - x * x / 2) for x in xs], [(x, x / 6 - x ** 3 / 6) for x in xs],
         "[quadratisch]", "[kubisch]"),
        ("qbeginn", [(x, 0.125) for x in links] + [(x, 0.125 - (x - 0.5)) for x in rechts[1:]],
         [(x, 0.125 * x) for x in links] + [(x, 0.125 * x - (x - 0.5) ** 2 / 2) for x in rechts[1:]],
         "[Knick]", "[glatt, kein Knick]"),
    ]
    ymitte = {1: 92, 2: 180, 3: 268, 4: 356, 5: 500}
    skalen = {}
    for k, (last, QP, MP, tQ, tM) in enumerate(zeilen, 1):
        yc = ymitte[k]
        if k == 5:
            e = abb.ebene("trenner", "Übergänge zwischen Bereichen")
            e.append(linie(20, 424, 700, 424, FARBE["hinweis"], 0.8))
            e.append(text(20, 444, "[Übergänge zwischen Bereichen]", "#222222", 15, anker="start", italic=False))
        e = abb.ebene(f"zeile-{k}", f"Regel {k}")
        yb = yc + 8                      # Balkenachse im Lastfeld
        e.append(balken(cL, yb, cL + w, yb, dicke=6))
        e.append(festlager(cL, yb + 3, groesse=10))
        e.append(loslager(cL + w, yb + 3, groesse=10))
        if last == "F":
            e.append(kraft(cL + w / 2, yb - 3, -90, "F", laenge=36, label_seite=-1))
        elif last == "M0":
            e.append(moment(cL + w / 2, yb, "", gegen_uhrzeiger=False, r=15, start=200, bogen=250))
            e.append(text(cL + w / 2 + 22, yb - 20, "M_0", FARBE["last"], anker="start"))
        elif last == "q":
            e.append(streckenlast(cL, cL + w, yb - 3, 24, label="q", n=8))
        elif last == "qlin":
            e.append(streckenlast(cL, cL + w, yb - 3, 2, 30, label="q_0", n=8))
        elif last == "qbeginn":
            e.append(streckenlast(cL + w / 2, cL + w, yb - 3, 24, label="q", n=4))
        sQ = 24 / max(abs(v) for _, v in QP)
        sM = 28 / max(abs(v) for _, v in MP)
        skalen[k] = (sQ, sM)
        e.append(verlauf(cQ, [(x * w, v) for x, v in QP], sQ, yc + 6, w, "", schraffur=6, achse_label=False,
                         vorzeichen=False))
        e.append(verlauf(cM, [(x * w, v) for x, v in MP], sM, yc + 10, w, "", schraffur=6, achse_label=False,
                         vorzeichen=False))
        e.append(text(cQ + w + 16, yc + 40, tQ, grau, 13, anker="end", italic=not tQ.endswith("]")))
        e.append(text(cM + w + 16, yc + 40, tM, grau, 13, anker="end", italic=not tM.endswith("]")))
        if last in ("F", "M0", "qbeginn"):
            for c in (cL, cQ, cM):
                e.append(linie(c + w / 2, yc - 30, c + w / 2, yc + 34, FARBE["hinweis"], 0.6, strich="3 2"))
        if k < 4:
            e.append(linie(20, yc + h / 2 + 4, 700, yc + h / 2 + 4, "#e3e6ea", 0.8))

    # Steigung: in Zeile 3 (q konstant) Q = 0 <-> Maximum von M
    yc = ymitte[3]
    sQ, sM = skalen[3]
    ymax = yc + 10 - 0.125 * sM
    e = abb.ebene("steigung", "Q = 0: M extremal")
    e.append(linie(cQ + w / 2, yc + 6, cM + w / 2, ymax, FARBE["mass"], 1.0, strich="4 3"))
    e.append(kreis(cQ + w / 2, yc + 6, 3.5, FARBE["mass"], FARBE["mass"]))
    e.append(kreis(cM + w / 2, ymax, 3.5, FARBE["mass"], FARBE["mass"]))
    e.append(linie(cM + w / 2 - 34, ymax, cM + w / 2 + 34, ymax, FARBE["mass"], 1.4))
    e.append(text(cQ + w / 2 - 6, yc + 24, "Q[ = 0]", FARBE["mass"], 14, anker="end"))
    e.append(text(cM + w / 2, ymax - 12, "M[ extremal]", FARBE["mass"], 14))
    return abb.speichern(ZIEL / "kontrollregeln.svg")


# =====================================================================
# B04-3 (Vorlesung 2013, Teil 3 S. 17–23): Dreigelenkrahmen
#   A (0,0) und B (12a,4a) Festlager, Gelenk G (4a,12a), Ecken C (0,12a), D (12a,12a)
#   F = 2 q0 a waagerecht in C, q0 auf G–D
#   F_AH = 0,5 q0a, F_AV = 1,5 q0a, F_BH = -2,5 q0a, F_BV = 6,5 q0a, G_H = -2,5 q0a, G_V = -1,5 q0a
#   lokale Koordinaten im Ursprung jedes Bereichs, z_i nach innen; x1 in I aufwärts, x2/x3 nach rechts,
#   x4 in IV abwärts; Verläufe positiv auf der Seite von -z_i (außen, wie Gross/Dankert)
# =====================================================================
def _rahmen_flaeche(P0, P1, werte, skala, aussen, schraffur=7):
    """Verlauf längs eines Stabes P0->P1. werte: [(s, v)] mit s in [0, 1];
    aussen: Einheitsnormale zur Seite, auf der positive Werte aufgetragen werden."""
    from tmzeichnen import _vorzeichen_abschnitte, _interp
    L = math.hypot(P1[0] - P0[0], P1[1] - P0[1])
    ux, uy = (P1[0] - P0[0]) / L, (P1[1] - P0[1]) / L
    nx, ny = aussen
    stil = {1: (FARBE["verlauf"], FARBE["verlauf_flaeche"]), -1: (FARBE["verlauf_neg"], FARBE["verlauf_neg_flaeche"])}
    pkt = [(s * L, v) for s, v in werte]
    P = lambda d, v: (P0[0] + ux * d + nx * v * skala, P0[1] + uy * d + ny * v * skala)
    flaechen, konturen = [], []
    for vz, ab in _vorzeichen_abschnitte(pkt):
        kontur, flaeche = stil[vz]
        kurve = [P(d, v) for d, v in ab]
        flaechen.append(polylinie([P(ab[0][0], 0)] + kurve + [P(ab[-1][0], 0)], None, fuellung=flaeche,
                                  schliessen=True))
        d = ab[0][0] + schraffur / 2
        while d < ab[-1][0]:
            v = _interp(ab, d)
            if abs(v * skala) > 1.5:
                flaechen.append(linie(*P(d, 0), *P(d, v), kontur, 0.6))
            d += schraffur
        konturen.append(polylinie(kurve, kontur, 1.9))
    return "".join(flaechen), "".join(konturen)


def dreigelenkrahmen():
    from tmzeichnen import gelenk_offen, stabzug, schnitt
    a = 26
    A = (190, 470)
    C = (A[0], A[1] - 12 * a)
    G = (A[0] + 4 * a, C[1])
    D = (A[0] + 12 * a, C[1])
    B = (D[0], A[1] - 4 * a)
    t = 3.5
    abb = Abbildung(760, 560, "Dreigelenkrahmen")
    blass = FARBE["hinweis"]

    e = abb.ebene("system", "Rahmen")
    e.append(stabzug([A, C, G], dicke=7))
    e.append(stabzug([G, D, B], dicke=7))
    e.append(gelenk(*G, r=5))
    e.append(festlager(A[0], A[1] + t, label="A", label_pos=(-24, 12)))
    e.append(festlager(B[0], B[1] + t, label="B", label_pos=(24, 12)))
    e.append(text(G[0] - 16, G[1] + 24, "G", "#000000", 17))
    e.append(text(C[0] - 16, C[1] - 12, "C", "#000000", 17))
    e.append(text(D[0] + 16, D[1] - 12, "D", "#000000", 17))

    e = abb.ebene("lasten", "Lasten")
    e.append(kraft(C[0] - t, C[1], 0, "F", laenge=55, label_seite=-1))
    e.append(streckenlast(G[0], D[0], C[1] - t, 30, label="q_0", n=16))

    e = abb.ebene("mass", "Bemaßung")
    e.append(mass(C[0], C[1], G[0], G[1], "4a", abstand=78))
    e.append(mass(G[0], G[1], D[0], D[1], "8a", abstand=78))
    e.append(mass(A[0], A[1], C[0], C[1], "12a", abstand=70))
    e.append(mass(D[0], D[1], B[0], B[1], "8a", abstand=70))
    e.append(koordinaten(40, 40, 30, "x", "z"))

    # --- Teilsysteme mit Lager- und Gelenkkräften (positiv angenommen)
    dl, dr = -40, 62
    L = lambda p: (p[0] + dl, p[1])
    Rr = lambda p: (p[0] + dr, p[1])
    e = abb.ebene("teilsysteme", "Teilsysteme")
    e.append(stabzug([L(A), L(C), L(G)], dicke=7))
    e.append(stabzug([Rr(G), Rr(D), Rr(B)], dicke=7))
    e.append(gelenk_offen(*L(G), 180))
    e.append(gelenk_offen(*Rr(G), 0))
    e.append(kraft(L(C)[0] - t, C[1], 0, "F", laenge=50, label_seite=-1))
    e.append(streckenlast(Rr(G)[0], Rr(D)[0], C[1] - t, 28, label="q_0", n=14))
    e.append(kraft(L(A)[0] - 4, A[1], 0, "F_{AH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(L(A)[0], A[1] + t, 90, "F_{AV}", farbe=R, laenge=46, label_seite=1))
    e.append(kraft(Rr(B)[0] - 4, B[1], 0, "F_{BH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(Rr(B)[0], B[1] + t, 90, "F_{BV}", farbe=R, laenge=46, label_seite=1))
    e.append(kraft(L(G)[0] + 6, G[1], 0, "G_H", farbe=R, laenge=34, ziehend=True, label_seite=1))
    e.append(kraft(L(G)[0], G[1] - t, 90, "G_V", farbe=R, laenge=40, ziehend=True, label_seite=-1, label_pos=0.8))
    e.append(kraft(Rr(G)[0] - 6, G[1], 180, "G_H", farbe=R, laenge=34, ziehend=True, label_seite=-1))
    e.append(kraft(Rr(G)[0], G[1] + t, -90, "G_V", farbe=R, laenge=40, ziehend=True, label_seite=-1, label_pos=0.8))
    e.append(text(L(A)[0] + 50, A[1] - 120, "[I]", "#555555", 16, italic=False))
    e.append(text(Rr(D)[0] - 60, D[1] + 120, "[II]", "#555555", 16, italic=False))

    # --- Bereiche und lokale Koordinaten, jeweils im Ursprung des Bereichs (z_i zeigt nach innen)
    e = abb.ebene("koordinaten", "Bereiche und lokale Koordinaten")
    k = FARBE["koord"]
    def achsen(P, u, z, nr, lx, lz):
        g = [pfeil(P[0], P[1], P[0] + 36 * u[0], P[1] + 36 * u[1], k, 1.6, (9, 6)),
             pfeil(P[0], P[1], P[0] + 28 * z[0], P[1] + 28 * z[1], k, 1.6, (9, 6)),
             text(P[0] + 36 * u[0] + lx[0], P[1] + 36 * u[1] + lx[1], f"x_{nr}", k, 16),
             text(P[0] + 28 * z[0] + lz[0], P[1] + 28 * z[1] + lz[1], f"z_{nr}", k, 16)]
        return "".join(g)
    e.append(achsen(A, (0, -1), (1, 0), 1, (-14, 2), (6, 12)))
    e.append(achsen(C, (1, 0), (0, 1), 2, (0, -12), (14, 4)))
    e.append(achsen(G, (1, 0), (0, 1), 3, (0, -12), (14, 4)))
    e.append(achsen(D, (0, 1), (-1, 0), 4, (16, 0), (0, 16)))
    e.append(nummer(A[0] - 42, A[1] - 6 * a, "I", r=11.5))
    e.append(nummer((C[0] + G[0]) / 2, C[1] + 34, "II", r=11.5))
    e.append(nummer((G[0] + D[0]) / 2, C[1] + 34, "III", r=11.5))
    e.append(nummer(D[0] + 42, (D[1] + B[1]) / 2 + 40, "IV", r=11.5))

    # --- Schnitte in den vier Bereichen (das behaltene Teil kräftig, mit positiven Schnittgrößen)
    S_ = FARBE["schnitt"]
    def N_Q_M(S, n, z, Mccw, Ml, Nl, Ql, Mlp, Nlp, Qlp, Mstart):
        g = [pfeil(S[0] + 9 * n[0], S[1] + 9 * n[1], S[0] + 45 * n[0], S[1] + 45 * n[1], S_),
             text(S[0] + 45 * n[0] + Nlp[0], S[1] + 45 * n[1] + Nlp[1], Nl, S_),
             pfeil(S[0] - 18 * z[0] + 4 * n[0], S[1] - 18 * z[1] + 4 * n[1], S[0] + 18 * z[0] + 4 * n[0],
                   S[1] + 18 * z[1] + 4 * n[1], S_),
             text(S[0] + 18 * z[0] + Qlp[0], S[1] + 18 * z[1] + Qlp[1], Ql, S_),
             moment(S[0], S[1], "", gegen_uhrzeiger=Mccw, r=21, start=Mstart, bogen=200, farbe=S_),
             text(S[0] + Mlp[0], S[1] + Mlp[1], Ml, S_)]
        return "".join(g)

    # I: Schnitt im Stiel A–C bei x1 = 6a, unteres Teil, positives Ufer (Normale nach oben)
    S1 = (A[0], A[1] - 6 * a)
    e = abb.ebene("schnitt-I", "Schnitt Bereich I")
    e.append(balken(A[0], A[1], S1[0], S1[1] + 3))
    e.append(linie(S1[0], S1[1] + 2, S1[0], S1[1] - 6, "#ffffff", 14))
    e.append(kraft(A[0] - 4, A[1], 0, "F_{AH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(A[0], A[1] + t, 90, "F_{AV}", farbe=R, laenge=46, label_seite=1))
    e.append(N_Q_M(S1, (0, -1), (1, 0), True, "M(x_1)", "N(x_1)", "Q(x_1)", (-40, -22), (12, 2), (8, 14), -20))
    e.append(mass(A[0], A[1], S1[0], S1[1], "x_1", abstand=-58))

    # II: Schnitt im Riegel C–G bei x2 = 2a, linkes Teil
    S2 = (C[0] + 2 * a, C[1])
    e = abb.ebene("schnitt-II", "Schnitt Bereich II")
    e.append(stabzug([A, C, (S2[0] - 3, S2[1])], dicke=7))
    e.append(linie(S2[0] - 2, S2[1], S2[0] + 6, S2[1], "#ffffff", 14))
    e.append(kraft(C[0] - t, C[1], 0, "F", laenge=55, label_seite=-1))
    e.append(kraft(A[0] - 4, A[1], 0, "F_{AH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(A[0], A[1] + t, 90, "F_{AV}", farbe=R, laenge=46, label_seite=1))
    e.append(schnittufer(S2[0], S2[1], positiv=True, N="N(x_2)", Q="Q(x_2)", M="M(x_2)"))
    e.append(mass(C[0], C[1], S2[0], S2[1], "x_2", abstand=40))

    # III: Schnitt im Riegel G–D bei x3 = 4a, linkes Teil
    S3 = (G[0] + 4 * a, G[1])
    e = abb.ebene("schnitt-III", "Schnitt Bereich III")
    e.append(stabzug([A, C, G], dicke=7))
    e.append(balken(G[0], G[1], S3[0] - 3, S3[1]))
    e.append(gelenk(*G, r=5))
    e.append(linie(S3[0] - 2, S3[1], S3[0] + 6, S3[1], "#ffffff", 14))
    e.append(kraft(C[0] - t, C[1], 0, "F", laenge=55, label_seite=-1))
    e.append(streckenlast(G[0], S3[0] - 3, C[1] - t, 30, label="q_0", n=8, label_rechts=False))
    e.append(kraft(A[0] - 4, A[1], 0, "F_{AH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(A[0], A[1] + t, 90, "F_{AV}", farbe=R, laenge=46, label_seite=1))
    e.append(schnittufer(S3[0], S3[1], positiv=True, N="N(x_3)", Q="Q(x_3)", M="M(x_3)"))
    e.append(mass(G[0], G[1], S3[0], S3[1], "x_3", abstand=58))

    # IV: Schnitt im Stiel D–B bei x4 = 4a, unteres Teil, negatives Ufer (Normale -x4 = nach oben)
    S4 = (D[0], D[1] + 4 * a)
    e = abb.ebene("schnitt-IV", "Schnitt Bereich IV")
    e.append(balken(S4[0], S4[1] + 3, B[0], B[1]))
    e.append(linie(S4[0], S4[1] - 2, S4[0], S4[1] + 6, "#ffffff", 14))
    e.append(kraft(B[0] - 4, B[1], 0, "F_{BH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(B[0], B[1] + t, 90, "F_{BV}", farbe=R, laenge=46, label_seite=1))
    # negatives Ufer: N nach oben (Zug), Q in -z4 = nach rechts, M im Uhrzeigersinn
    e.append(N_Q_M(S4, (0, -1), (1, 0), False, "M(x_4)", "N(x_4)", "Q(x_4)", (-40, -22), (12, 2), (8, 14), 200))
    e.append(mass(D[0], D[1], S4[0], S4[1], "x_4", abstand=58))

    # --- Verläufe am Rahmen (positiv auf der Seite von -z_i = außen)
    aussen = {"I": (-1, 0), "II": (0, -1), "III": (0, -1), "IV": (1, 0)}
    staebe = {"I": (A, C), "II": (C, G), "III": (G, D), "IV": (D, B)}
    def rahmen_bild(e):
        e.append(polylinie([A, C, G, D, B], "#000000", 2.2))
        e.append(kreis(*G, 4, "#000000", "#ffffff", 1.2))
    xs = [i / 40 for i in range(41)]
    verl = {
        "N": ({"I": [(0, -1.5), (1, -1.5)], "II": [(0, -2.5), (1, -2.5)], "III": [(0, -2.5), (1, -2.5)],
               "IV": [(0, -6.5), (1, -6.5)]}, 7.0,
              [((A[0] + 22, A[1] - 6 * a), "−1,5", "start"), ((C[0] + 2 * a, C[1] + 34), "−2,5", "middle"),
               ((G[0] + 4 * a, C[1] + 34), "−2,5", "middle"), ((D[0] - 52, D[1] + 4 * a), "−6,5", "end")]),
        "Q": ({"I": [(0, -0.5), (1, -0.5)], "II": [(0, 1.5), (1, 1.5)], "III": [(s, 1.5 - 8 * s) for s in xs],
               "IV": [(0, 2.5), (1, 2.5)]}, 7.0,
              [((A[0] + 14, A[1] - 6 * a), "−0,5", "start"), ((C[0] + 2 * a, C[1] - 20), "1,5", "middle"),
               ((D[0] - 14, D[1] + 58), "−6,5", "end"), ((D[0] + 26, D[1] + 4 * a), "2,5", "start")]),
        "M": ({"I": [(s, -6 * s) for s in xs], "II": [(s, -6 + 6 * s) for s in xs],
               "III": [(s, 1.5 * 8 * s - (8 * s) ** 2 / 2) for s in xs], "IV": [(s, -20 + 20 * s) for s in xs]}, 3.0,
              [((C[0] + 24, C[1] + 30), "−6", "start"), ((G[0] + 1.5 * a, C[1] - 16), "9/8", "middle"),
               ((D[0] - 66, D[1] + 66), "−20", "end")]),
    }
    einheit = {"N": "q_0a", "Q": "q_0a", "M": "q_0a^2"}
    for gr, (werte, skala, labels) in verl.items():
        e = abb.ebene(f"verlauf-{gr}", f"{gr}-Verlauf")
        teile = [_rahmen_flaeche(P0, P1, werte[st], skala, aussen[st]) for st, (P0, P1) in staebe.items()]
        for f_, _ in teile:
            e.append(f_)
        for _, k_ in teile:
            e.append(k_)
        rahmen_bild(e)
        for (x, y), txt, anker in labels:
            farbe = FARBE["verlauf_neg"] if txt.startswith("−") else FARBE["verlauf"]
            e.append(text(x, y, f"[{txt}]", farbe, 15, anker=anker, italic=False))
        e.append(text(640, 60, f"{gr}[ in ]{einheit[gr]}", "#222222", 17, anker="start"))
    return abb.speichern(ZIEL / "dreigelenkrahmen.svg")


# =====================================================================
# Zusammenfassung: Fahrplan in fünf Schritten
# =====================================================================
def fahrplan():
    """Fahrplan als Scrollytelling: oben die fünf Schritte als Leiste, darunter ein Beispiel,
    an dem jeder Schritt gezeigt wird. Träger: A (fest) bei 0, F = 2,5 qa bei a, B (los) bei 3a,
    q auf dem Kragarm 3a..4a  ->  F_AV = 1,5 qa, F_B = 2 qa."""
    abb = Abbildung(760, 600, "Fahrplan Schnittgrößen")
    blau, grau_hell = "#0050b4", "#c9d3df"
    a, x0, y, t = 120, 130, 170, 3.5
    X = lambda k: x0 + k * a

    # --- Leiste mit den fünf Schritten
    titel = ["[Lagerreaktionen]", "[Bereiche]", "[Schneiden]", "[Verläufe]", "[Kontrolle]"]
    w, gap, yl = 141, 6, 22
    def chip(i, aktiv):
        xc = 16 + i * (w + gap)
        f, rand, tf = ("#e8f0fa", blau, "#0b2e59") if aktiv else ("#f6f7f9", grau_hell, "#8a8f96")
        g = [polylinie([(xc, yl), (xc + w, yl), (xc + w, yl + 36), (xc, yl + 36)], rand, 2 if aktiv else 1,
                       fuellung=f, schliessen=True),
             kreis(xc + 18, yl + 18, 11, rand if aktiv else "#b0b6bd", rand if aktiv else "#b0b6bd"),
             text(xc + 18, yl + 18, f"[{i + 1}]", "#ffffff", 14, italic=False, halo=False),
             text(xc + 35, yl + 19, titel[i], tf, 14, anker="start", italic=False)]
        return "".join(g)
    e = abb.ebene("leiste", "Fünf Schritte")
    for i in range(5):
        e.append(chip(i, False))
    for i in range(5):
        e = abb.ebene(f"leiste-{i + 1}", f"Schritt {i + 1} hervorgehoben")
        e.append(chip(i, True))

    # --- Beispielträger
    e = abb.ebene("traeger", "Träger mit Lasten")
    e.append(balken(X(0), y, X(4), y))
    e.append(kraft(X(1), y - t, -90, "F", laenge=50, label_seite=-1))
    e.append(streckenlast(X(3), X(4), y - t, 28, label="q", n=6))
    for k0, k1, lab in ((0, 1, "a"), (1, 3, "2a"), (3, 4, "a")):
        e.append(mass(X(k0), y, X(k1), y, lab, abstand=-70))
    e.append(koordinaten(30, 90, 30, "x", "z"))
    e = abb.ebene("lager", "Lager")
    e.append(festlager(X(0), y + t, label="A", label_pos=(-24, 14)))
    e.append(loslager(X(3), y + t, label="B", label_pos=(-24, 14)))
    e = abb.ebene("reaktionen", "Lagerreaktionen")
    e.append(kraft(X(0) - 4, y, 0, "F_{AH}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(X(0), y + t, 90, "F_{AV}", farbe=R, laenge=46, label_seite=1))
    e.append(kraft(X(3), y + t, 90, "F_B", farbe=R, laenge=46, label_seite=-1))

    # --- Bereiche mit Koordinaten im Ursprung
    e = abb.ebene("bereiche", "Bereiche")
    for k in (1, 3):
        e.append(linie(X(k), y - 64, X(k), y + 40, FARBE["hinweis"], 0.9, strich="4 3"))
    for k0, k1, n, nr in ((0, 1, "I", 1), (1, 3, "II", 2), (3, 4, "III", 3)):
        e.append(nummer((X(k0) + X(k1)) / 2, y + 44, n, r=11.5))
        e.append(koordinaten(X(k0), y, 30, f"x_{nr}", nur_x=True))

    # --- Schnitt im Bereich II (linkes Teil)
    xs = X(2)
    yt = 380
    e = abb.ebene("schnitt", "Schnitt im Bereich II")
    e.append(schnittlinie(xs, y, 44))
    e.append(text(xs + 10, y - 26, "S", FARBE["mass"], 15))
    e.append(balken(X(0), yt, xs, yt))
    e.append(kraft(X(0) - 4, yt, 0, "F_{AH}", farbe=R, laenge=40, label_seite=-1))
    e.append(kraft(X(0), yt + t, 90, "F_{AV}", farbe=R, laenge=44, label_seite=-1))
    e.append(kraft(X(1), yt - t, -90, "F", laenge=46, label_seite=-1))
    e.append(schnittufer(xs, yt, positiv=True, N="N(x_2)", Q="Q(x_2)", M="M(x_2)"))
    e.append(koordinaten(30, yt - 70, 30, "x", "z"))
    e.append(text(X(0), yt - 82, "[linkes Teil, Momente um ]S", "#444444", 14, anker="start", italic=False))

    # --- Verläufe (Einheiten qa bzw. qa²), positive Werte oberhalb der Achse
    yQ, yM = 340, 480
    QP = [(0, 1.5), (1, 1.5), (1, -1), (3, -1), (3, 1)] + [(3 + i / 10, 1 - i / 10) for i in range(1, 11)]
    MP = [(0, 0), (1, 1.5), (3, -0.5)] + [(3 + i / 10, -(1 - i / 10) ** 2 / 2) for i in range(1, 11)]
    e = abb.ebene("verlauf-Q", "Querkraftverlauf")
    e.append(verlauf(X(0), [(k * a, v) for k, v in QP], 24, yQ, 4 * a, "Q(x)"))
    e = abb.ebene("verlauf-M", "Momentenverlauf")
    e.append(verlauf(X(0), [(k * a, v) for k, v in MP], 30, yM, 4 * a, "M(x)"))

    # --- Kontrolle: Merkmale an den Verläufen
    gruen = FARBE["mass"]
    e = abb.ebene("kontrolle", "Kontrollen")
    for k in (1, 3):
        e.append(linie(X(k), y + 40, X(k), yM + 60, FARBE["hinweis"], 0.6, strich="4 3"))
    e.append(text(X(1) + 8, yQ + 44, "[Sprung um ]F", gruen, 14, anker="start"))
    e.append(text(X(3) - 8, yQ - 40, "[Sprung um ]F_B", gruen, 14, anker="end"))
    e.append(text(X(4) + 6, yQ - 16, "Q[ → 0]", gruen, 14, anker="start"))
    e.append(text(X(1), yM - 62, "[Knick]", gruen, 14))
    e.append(text(X(3) + 8, yM + 34, "[Knick]", gruen, 14, anker="start"))
    e.append(text(X(3.5), yM - 22, "[Parabel]", gruen, 14))
    e.append(text(X(0) - 6, yM + 22, "M[ = 0]", gruen, 14, anker="end"))
    e.append(text(X(4) + 6, yM + 22, "M[ = 0]", gruen, 14, anker="start"))
    return abb.speichern(ZIEL / "fahrplan.svg")


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
             kraft(xA - 4, yt, 0, "F_{AH}", farbe=R, laenge=40, label_seite=-1),
             kraft(xA, yt + t, 90, "F_{AV}", farbe=R, laenge=40, label_seite=-1)]
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
        e.append(text(xs + 2, y - 30, "S", FARBE["mass"], 15))
        e.append(links(xs, xs > xF1, i, 1.0 if l_aktiv else 0.35))
        e.append(rechts(xs, i, 0.35 if l_aktiv else 1.0))
        e.append(text(xA - 50, yt - 58, "[linkes Teilsystem]" if l_aktiv else "[rechtes Teilsystem]",
                      "#444444", 14, anker="start", italic=False))
        e.append(koordinaten(16, yt - 44, 28, "x", "z"))

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
    # Streckenlast auf dem Element blass, ihre Resultierende q(x) dx als Einzelkraft in der Mitte
    e.append(streckenlast(xel + 4, xel + w - 4, ye - 12, 30, 34, "", farbe="#f6c4c4", n=8))
    e.append(kraft(xel + w / 2, ye - 12, -90, "q(x)[ d]x", laenge=62, label_seite=-1, label_pos=0.75))
    e.append(mass(xel, ye, xel + w, ye, "[d]x", abstand=-48))
    e.append(mass(xel + w / 2, ye, xel + w, ye, "[d]x/2", abstand=-80, hilfslinien=False))
    for xx in (xel + w / 2, xel + w):
        e.append(linie(xx, ye + 72, xx, ye + 88, FARBE["mass"], STRICH["duenn"]))
    e.append(schnittufer(xel + w, ye, positiv=True, N="", Q="Q(x) + [d]Q", M="M(x) + [d]M", zeige=("Q", "M"), laenge=56))
    e.append(schnittufer(xel, ye, positiv=False, N="", Q="Q(x)", M="M(x)", zeige=("Q", "M"), laenge=56))
    # Bezugspunkt der Momentenbilanz: rechter Rand des Ausschnitts
    e.append(kreis(xel + w, ye, 4, FARBE["mass"], FARBE["mass"]))
    e.append(text(xel + w + 22, ye + 6, "R", FARBE["mass"], 17, anker="start"))

    # Verläufe
    n = 60
    xs = [i / n for i in range(n + 1)]
    Q = [(xi * L, 1 / 6 - xi ** 2 / 2) for xi in xs]
    M = [(xi * L, xi / 6 - xi ** 3 / 6) for xi in xs]
    yQ, yM = 330, 500
    e = abb.ebene("verlauf-Q", "Querkraftverlauf")
    e.append(verlauf(xA, Q, 150, yQ, L, "Q(x)",
                     werte=[(10, 1 / 6, "q_0L/6", "start"), (L, -1 / 3, "−q_0L/3", "end")]))
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
    e.append(linie(xC, y, xC, y + 95, "#000000", 3))     # Pendelstütze: schmaler Stab
    e.append(mass(xA, y, xC, y, "2l", abstand=-50))
    e.append(mass(xC, y, xE, y, "l", abstand=-50))
    e.append(festlager(xA - 3.2, y, drehung=90, label="A", label_pos=(-10, -24)))
    e.append(gelenk(xC, y, r=5))
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
    e.append(gelenk(xG, y, r=5))
    e.append(text(xG, y - 18, "G"))
    e.append(moment(xM, y, "", gegen_uhrzeiger=False, r=17, start=200, bogen=250))
    e.append(text(xM - 4, y - 32, "M_B", FARBE["last"]))
    e.append(kraft(xF, y - t, 210, "F", laenge=58, label_seite=1))
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


def lastkurve(x0, x1, y, h, n=14, label="", label_pos=None, farbe=None):
    """Streckenlast mit beliebiger Form: h(t) in px für t in [0, 1], Pfeile zum Balken (Oberkante y)."""
    farbe = farbe or FARBE["last"]
    teile = []
    for i in range(n + 1):
        tt = i / n
        hh = h(tt)
        xx = x0 + (x1 - x0) * tt
        if hh > 4:
            teile.append(pfeil(xx, y - hh, xx, y, farbe, 1.25, (8, 5.5)))
    teile.append(polylinie([(x0 + (x1 - x0) * i / 60, y - h(i / 60)) for i in range(61)], farbe, 1.25))
    if label:
        lx, ly = label_pos or (x1 + 6, y - h(1) - 4)
        teile.append(text(lx, ly, label, farbe, anker="start"))
    return "".join(teile)


def aufgabe_4_6():
    """Abgewinkelter Kragträger (Scan B04-1): Einspannung A, waagerecht 2a bis C, senkrecht a nach unten bis D."""
    from tmzeichnen import stabzug
    abb, e = _aufgabe("Aufgabe 4.6", 460, 250)
    a, xA, y = 110, 70, 70
    C, D = (xA + 2 * a, y), (xA + 2 * a, y + a)
    e.append(stabzug([(xA, y), C, D], dicke=7))
    e.append(einspannung(xA, y, seite="links", label="A"))
    e.append(kraft(C[0], y - 3.5, -90, "F_1", laenge=48, label_seite=-1))
    e.append(kraft(D[0] - 3.5, D[1] - 6, 0, "F_2", laenge=50, label_seite=-1))
    e.append(text(C[0] + 14, y - 12, "C"))
    e.append(text(D[0] + 14, D[1] + 4, "D"))
    e.append(mass(xA, y, C[0], y, "2a", abstand=-(a + 40)))
    e.append(mass(C[0], C[1], D[0], D[1], "a", abstand=46))
    return abb.speichern(ZIEL / "aufgabe-4-6.svg")


def aufgabe_4_7():
    """Kragträger mit Streckenlast, drei Lastfälle (Scan B04-02 a–c)."""
    abb, e = _aufgabe("Aufgabe 4.7", 520, 470)
    L, xA = 320, 110
    for k, (tit, l0, l1) in enumerate((("a)", 0, 1), ("b)", 0, 0.5), ("c)", 0.5, 1))):
        y = 90 + k * 140
        e.append(text(30, y - 36, f"[{tit}]", "#222222", 17, anker="start", italic=False))
        e.append(balken(xA, y, xA + L, y))
        e.append(einspannung(xA, y, seite="links", label="A" if k == 0 else ""))
        e.append(streckenlast(xA + l0 * L, xA + l1 * L, y - 3.5, 30, label="q_0", n=max(4, int(16 * (l1 - l0)))))
        if (l0, l1) == (0, 1):
            e.append(mass(xA, y, xA + L, y, "l", abstand=-34))
        else:
            e.append(mass(xA, y, xA + L / 2, y, "l/2", abstand=-34))
            e.append(mass(xA + L / 2, y, xA + L, y, "l/2", abstand=-34))
    return abb.speichern(ZIEL / "aufgabe-4-7.svg")


def aufgabe_4_8():
    """Parabelförmige Streckenlasten (Scan B04-3): a) Kragträger, b) Einfeldträger."""
    abb, e = _aufgabe("Aufgabe 4.8", 760, 230)
    L, y = 260, 120
    # a) Kragträger: Maximum q0 an der Einspannung (waagerechte Tangente), null am freien Ende
    xA = 80
    e.append(text(20, 40, "[a)]", "#222222", 17, anker="start", italic=False))
    e.append(balken(xA, y, xA + L, y))
    e.append(einspannung(xA, y, seite="links", label="A"))
    e.append(lastkurve(xA, xA + L, y - 3.5, lambda s: 60 * (1 - s * s), n=12, label="q_0", label_pos=(xA + 6, y - 82)))
    e.append(mass(xA, y, xA + L, y, "l", abstand=-38))
    # b) Einfeldträger: Maximum q0 in der Mitte, null an beiden Lagern
    xB = 450
    e.append(text(390, 40, "[b)]", "#222222", 17, anker="start", italic=False))
    e.append(balken(xB, y, xB + L, y))
    e.append(festlager(xB, y + 3.5, label="A", label_pos=(-22, 12)))
    e.append(loslager(xB + L, y + 3.5, label="B", label_pos=(22, 12)))
    e.append(lastkurve(xB, xB + L, y - 3.5, lambda s: 60 * 4 * s * (1 - s), n=12, label="q_0",
                       label_pos=(xB + L / 2 + 8, y - 80)))
    e.append(mass(xB, y, xB + L, y, "l", abstand=-50))
    return abb.speichern(ZIEL / "aufgabe-4-8.svg")


if __name__ == "__main__":
    for fn in (reine_biegung, vorzeichen, bereiche_muster, kontrollregeln, dreigelenkrahmen, fahrplan, beispiel_einzelkraefte, beispiel_dreieckslast, aufgabe_1_5_1, aufgabe_1_5_3,
               aufgabe_1_5_5, aufgabe_1_5_6, aufgabe_1_5_8, aufgabe_4_6, aufgabe_4_7, aufgabe_4_8):
        print(fn())

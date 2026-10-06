import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Kräfte und Gleichgewicht interaktiv")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    ROT, BLAU, GRUEN, GRAU = "#d40000", "#0050b4", "#006414", "#c8c8c8"
    plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "stix", "font.size": 11})
    return BLAU, GRAU, GRUEN, ROT, mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Kräfte und Gleichgewicht interaktiv

    ## 1 · Resultierende und Krafteck

    Drei Kräfte greifen in einem Punkt an (zentrales Kraftsystem). Die Winkel zählen von der
    positiven $x$-Achse gegen den Uhrzeigersinn.

    > Überlegen Sie **vor** jeder Änderung: Wohin dreht sich die Resultierende, wird sie größer oder kleiner?
    > Stellen Sie die Kräfte so ein, dass sich das **Krafteck schließt** ($F_R = 0$).
    """)
    return


@app.cell
def _(mo):
    regler = mo.ui.array([
        mo.ui.slider(0, 40, step=1, value=20, label=r"$F_1$ in N", show_value=True),
        mo.ui.slider(-180, 180, step=5, value=30, label=r"$\alpha_1$ in °", show_value=True),
        mo.ui.slider(0, 40, step=1, value=30, label=r"$F_2$ in N", show_value=True),
        mo.ui.slider(-180, 180, step=5, value=135, label=r"$\alpha_2$ in °", show_value=True),
        mo.ui.slider(0, 40, step=1, value=0, label=r"$F_3$ in N", show_value=True),
        mo.ui.slider(-180, 180, step=5, value=-90, label=r"$\alpha_3$ in °", show_value=True),
    ])
    mo.hstack([mo.vstack(regler.elements[0:2]), mo.vstack(regler.elements[2:4]), mo.vstack(regler.elements[4:6])],
              justify="start", gap=2)
    return (regler,)


@app.cell
def _(BLAU, GRAU, GRUEN, ROT, np, plt, regler):
    _w = regler.value
    kraefte = [(_w[0], _w[1]), (_w[2], _w[3]), (_w[4], _w[5])]
    komp = np.array([(F * np.cos(np.radians(a)), F * np.sin(np.radians(a))) for F, a in kraefte])
    FR = komp.sum(axis=0)

    _fig, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(9, 4.2))
    _lim = max(10.0, np.abs(np.cumsum(komp, axis=0)).max(), np.abs(komp).max()) * 1.2

    def _pfeil(ax, p, q, farbe, txt, lw=2):
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=farbe, lw=lw, mutation_scale=15))
        if txt:
            ax.text((p[0] + q[0]) / 2, (p[1] + q[1]) / 2, txt, color=farbe, fontsize=13,
                    ha="center", va="center", bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))

    for _ax, _titel in ((_ax1, "Kräfte am Punkt"), (_ax2, "Krafteck")):
        _ax.axhline(0, color=GRUEN, lw=0.8)
        _ax.axvline(0, color=GRUEN, lw=0.8)
        _ax.set_xlim(-_lim, _lim)
        _ax.set_ylim(-_lim, _lim)
        _ax.set_aspect("equal")
        _ax.set_title(_titel, fontsize=12)
        _ax.set_xlabel("$x$ in N")
        _ax.grid(color=GRAU, lw=0.4)
    _start = np.zeros(2)
    for _i, (_fx, _fy) in enumerate(komp, 1):
        if np.hypot(_fx, _fy) > 1e-9:
            _pfeil(_ax1, (0, 0), (_fx, _fy), ROT, f"$F_{_i}$")
            _pfeil(_ax2, tuple(_start), tuple(_start + (_fx, _fy)), ROT, f"$F_{_i}$")
        _start = _start + (_fx, _fy)
    if np.hypot(*FR) > 1e-6:
        _pfeil(_ax1, (0, 0), tuple(FR), BLAU, "$F_R$", 2.6)
        _pfeil(_ax2, (0, 0), tuple(FR), BLAU, "$F_R$", 2.6)
    else:
        _ax2.text(0, -0.85 * _lim, "Krafteck geschlossen: Gleichgewicht", ha="center", color=GRUEN, fontsize=12)
    _fig.tight_layout()
    _fig
    return (FR,)


@app.cell
def _(FR, mo, np):
    _FR = float(np.hypot(*FR))
    _roh = np.degrees(np.arctan(FR[1] / FR[0])) if abs(FR[0]) > 1e-9 else float("nan")
    _alpha = float(np.degrees(np.arctan2(FR[1], FR[0])))
    if _FR < 1e-6:
        _hinweis = "Die Resultierende verschwindet: Die Kräfte sind im **Gleichgewicht**."
    elif FR[0] < 0:
        _hinweis = (f"$F_{{Rx}} < 0$: Der Taschenrechner liefert $\\arctan(F_{{Ry}}/F_{{Rx}}) = {_roh:.1f}°$, "
                    f"richtig ist $\\alpha_R = {_roh:.1f}° + 180° = {(_roh + 180):.1f}°$ "
                    f"(gleichwertig ${_alpha:.1f}°$).")
    else:
        _hinweis = f"$F_{{Rx}} > 0$: Der Arkustangens liefert den Winkel direkt."
    mo.md(rf"""
    | $F_{{Rx}}$ | $F_{{Ry}}$ | $F_R$ | $\alpha_R$ |
    |--:|--:|--:|--:|
    | {FR[0]:.2f} N | {FR[1]:.2f} N | {_FR:.2f} N | {_alpha:.1f}° |

    {_hinweis}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2 · Kiste an Stricken (Aufgabe 1.7)

    Die waagerechte Kraft $F$ lenkt den Strick (a) aus, die Kiste steigt um $h$.
    Am Knoten herrscht Gleichgewicht eines **zentralen Kraftsystems**:

    $$
    \tan\varphi = \frac{F}{m g}, \qquad S_a = \sqrt{F^2 + (m g)^2}, \qquad h = l\,(1 - \cos\varphi)
    $$

    > Wie hängt $h$ von $F$ ab? Warum wird es immer schwerer, die Kiste weiter anzuheben?
    """)
    return


@app.cell
def _(mo):
    F_regler = mo.ui.slider(0, 1500, step=10, value=300, label=r"$F$ in N", show_value=True)
    m_regler = mo.ui.slider(10, 100, step=5, value=50, label=r"$m$ in kg", show_value=True)
    S_regler = mo.ui.slider(500, 2000, step=50, value=1200, label=r"$S_\mathrm{max}$ in N", show_value=True)
    mo.hstack([F_regler, m_regler, S_regler], justify="start", gap=2)
    return F_regler, S_regler, m_regler


@app.cell
def _(BLAU, F_regler, GRAU, GRUEN, ROT, S_regler, m_regler, np, plt):
    l, g = 0.8, 9.81
    G = m_regler.value * g
    Smax = S_regler.value
    F = F_regler.value
    phi = np.arctan2(F, G)
    Sa = np.hypot(F, G)
    h = l * (1 - np.cos(phi))
    reisst = Sa > Smax
    Fmax = np.sqrt(max(Smax ** 2 - G ** 2, 0.0))
    hmax = l * (1 - G / Smax) if Smax > G else 0.0

    _fig, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(9, 4.2), gridspec_kw={"width_ratios": [1, 1.4]})
    # Geometrie
    _K = (l * np.sin(phi), -l * np.cos(phi))
    _ax1.plot([-0.12, 0.12], [0, 0], color="k", lw=2)
    _ax1.plot([0, _K[0]], [0, _K[1]], color=ROT if reisst else "k", lw=2, ls="--" if reisst else "-")
    _ax1.plot([_K[0], _K[0]], [_K[1], _K[1] - 0.15], color="k", lw=1.6)
    _ax1.add_patch(plt.Rectangle((_K[0] - 0.08, _K[1] - 0.27), 0.16, 0.12, fc=GRAU, ec="k"))
    _ax1.plot([0, 0], [0, -l - 0.3], color=GRAU, lw=0.8, ls=":")
    _ax1.add_patch(plt.Rectangle((-0.08, -l - 0.27), 0.16, 0.12, fc="none", ec=GRAU, ls="--"))
    if F > 0:
        _ax1.annotate("", xy=(_K[0] + 0.25, _K[1]), xytext=_K,
                      arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2, mutation_scale=14))
        _ax1.text(_K[0] + 0.27, _K[1] + 0.03, "$F$", color=ROT, fontsize=13)
    _ax1.annotate("", xy=(-0.2, _K[1]), xytext=(-0.2, -l), arrowprops=dict(arrowstyle="<->", color=GRUEN))
    _ax1.text(-0.23, (_K[1] - l) / 2, "$h$", color=GRUEN, ha="right", va="center", fontsize=13)
    _ax1.set_xlim(-0.35, 1.15)
    _ax1.set_ylim(-1.15, 0.1)
    _ax1.set_aspect("equal")
    _ax1.axis("off")
    _ax1.set_title("Strick (a) reißt!" if reisst else "Lage im Gleichgewicht", color=ROT if reisst else "k")
    # Kennlinien
    _Fs = np.linspace(0, 1500, 400)
    _ax2.plot(_Fs, l * (1 - np.cos(np.arctan2(_Fs, G))) * 1000, color=BLAU, lw=2, label="$h$ in mm")
    _ax2.plot(_Fs, np.hypot(_Fs, G), color=ROT, lw=2, label="$S_a$ in N")
    _ax2.axhline(Smax, color=ROT, lw=1, ls="--")
    _ax2.text(20, Smax + 25, r"$S_\mathrm{max}$", color=ROT)
    _ax2.plot([F], [h * 1000], "o", color=BLAU)
    _ax2.plot([F], [Sa], "o", color=ROT)
    _ax2.set_xlabel("$F$ in N")
    _ax2.set_xlim(0, 1500)
    _ax2.set_ylim(0, 2100)
    _ax2.grid(color=GRAU, lw=0.4)
    _ax2.legend(loc="upper left", frameon=False)
    _fig.tight_layout()
    _fig
    return Fmax, G, Sa, h, hmax, phi


@app.cell
def _(Fmax, G, Sa, h, hmax, mo, np, phi):
    mo.md(rf"""
    | $m g$ | $\varphi$ | $S_a$ | $h$ | $F_\mathrm{{max}}$ | $h_\mathrm{{max}}$ |
    |--:|--:|--:|--:|--:|--:|
    | {G:.1f} N | {np.degrees(phi):.1f}° | {Sa:.0f} N | {h * 1000:.0f} mm | {Fmax:.0f} N | {hmax * 1000:.0f} mm |

    Die Kurve $h(F)$ wird immer flacher: Für jeden weiteren Millimeter braucht man mehr Kraft,
    und die Seilkraft $S_a$ wächst schneller als die Hubhöhe.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3 · Ergebnis prüfen

    Wählen Sie eine Aufgabe und tragen Sie **Ihre auf Papier ermittelten Werte** ein
    (Komma oder Punkt als Dezimaltrennzeichen). Winkel in Grad, von der positiven $x$-Achse gegen
    den Uhrzeigersinn; Momente gegen den Uhrzeigersinn positiv.
    """)
    return


@app.cell
def _(mo):
    AUFGABEN = {
        "1.1 Containerschiff": [("\\varphi_1", "°", 21.01), ("F_R", "MN", 1.156)],
        "1.2 Stahlträger am Kran": [("F_S", "N", 2873.2)],
        "1.3 Scheibe mit drei Kräften": [
            ("F_R", "N", 3927.0), ("\\alpha_R", "°", 4.64), ("M_R^{(0)}", "Nm", -7535.2),
            ("\\text{Steigung der Wirkungslinie}", "–", 0.0812), ("\\text{Achsabschnitt } y_R(0)", "m", 1.925)],
        "1.4 Fahrradantrieb": [
            ("M_T", "Nm", 68.94), ("F_K", "N", 919.3), ("M_R", "Nm", 33.09), ("F_V", "N", 90.67)],
        "1.5 Bolzen (Hausaufgabe)": [
            ("F_{Rx}", "N", -684.0), ("F_{Ry}", "N", -2299.0), ("F_R", "N", 2398.6), ("\\alpha_R", "°", 253.4)],
        "1.6 Zwei Wirkungslinien (Hausaufgabe)": [("F_4", "N", -22.68), ("F_5", "N", 57.32)],
        "1.7 Kiste an Stricken": [("h_1", "m", 0.1175), ("h_{max}", "m", 0.473), ("F_{max}", "N", 1095.2)],
    }
    wahl = mo.ui.dropdown(options=list(AUFGABEN), value="1.1 Containerschiff", label="Aufgabe")
    wahl
    return AUFGABEN, wahl


@app.cell
def _(AUFGABEN, mo, wahl):
    eingaben = mo.ui.array(
        [mo.ui.text(placeholder="Ihr Wert", label=rf"${tex}$ in {einheit}") for tex, einheit, _ in AUFGABEN[wahl.value]])
    eingaben.vstack()
    return (eingaben,)


@app.cell
def _(AUFGABEN, eingaben, mo, wahl):
    def zahl(t):
        try:
            return float(t.replace(",", ".").replace("−", "-").strip())
        except ValueError:
            return None

    def gleich(a, b):
        return abs(a - b) <= max(0.01 * abs(b), 1e-3)

    zeilen = []
    for (tex, _e, soll), feld in zip(AUFGABEN[wahl.value], eingaben.value):
        w = zahl(feld)
        if w is None:
            urteil = "–"
        elif gleich(w, soll) or (_e == "°" and (gleich(w + 360, soll) or gleich(w - 360, soll))):
            urteil = "✅ richtig"
        elif gleich(abs(w), abs(soll)):
            urteil = "⚠️ Betrag stimmt – Vorzeichen prüfen"
        elif _e == "°" and (gleich(w + 180, soll) or gleich(w - 180, soll)):
            urteil = "⚠️ um 180° daneben – Quadrant prüfen"
        else:
            urteil = "❌ noch nicht"
        zeilen.append(f"| ${tex}$ | {feld or ''} | {urteil} |")
    mo.md("| Größe | Ihr Wert | Bewertung |\n|:--|--:|:--|\n" + "\n".join(zeilen))
    return


if __name__ == "__main__":
    app.run()

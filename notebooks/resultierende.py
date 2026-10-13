import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Resultierende und Krafteck")


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
    # Resultierende und Krafteck

    Bis zu drei Kräfte greifen in einem Punkt an (zentrales Kraftsystem). Die **Richtungswinkel** zählen von
    der positiven $x$-Achse gegen den Uhrzeigersinn, so wie in der Vorlesung: $F_2$ unter $135^\circ$ statt
    „$45^\circ$ zur negativen $x$-Achse“. Dann stimmen die Vorzeichen der Komponenten automatisch.

    Voreingestellt ist das Beispiel aus der Vorlesung: $F_1 = 20$ N unter $30^\circ$, $F_2 = 30$ N unter $135^\circ$.

    > Überlegen Sie **vor** jeder Änderung: Wohin dreht sich die Resultierende, wird sie größer oder kleiner?
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
    return FR, kraefte


@app.cell
def _(FR, kraefte, mo, np):
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
    _zeilen = "\n".join(
        rf"| $F_{_i}$ | {F:.0f} N | {a:.0f}° | ${F:.0f}\cdot\cos {a:.0f}^\circ = {F*np.cos(np.radians(a)):.2f}$ N | ${F:.0f}\cdot\sin {a:.0f}^\circ = {F*np.sin(np.radians(a)):.2f}$ N |"
        for _i, (F, a) in enumerate(kraefte, 1) if F > 0)
    mo.md(rf"""
    | Kraft | Betrag | Winkel | $F_{{ix}} = F_i\cos\alpha_i$ | $F_{{iy}} = F_i\sin\alpha_i$ |
    |:--|--:|--:|--:|--:|
    {_zeilen}

    | $F_{{Rx}}$ | $F_{{Ry}}$ | $F_R$ | $\alpha_R$ |
    |--:|--:|--:|--:|
    | {FR[0]:.2f} N | {FR[1]:.2f} N | {_FR:.2f} N | {_alpha:.1f}° |

    {_hinweis}
    """)
    return


if __name__ == "__main__":
    app.run()

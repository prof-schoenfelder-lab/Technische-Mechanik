import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Gummiband am Lineal")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    ROT, BLAU, GRUEN, GRAU = "#d40000", "#0050b4", "#006414", "#c8c8c8"
    BAND, RAND = "#e9dcc6", "#6b5a40"
    plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "stix", "font.size": 11})
    return BAND, BLAU, GRAU, GRUEN, RAND, ROT, mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Gummiband am Lineal: Dehnung

    Ein Gummiband ist 10 cm lang und links bei 0 festgehalten. Im Abstand von 1 cm sind Striche aufgemalt.
    Sie ziehen das rechte Ende auf die Länge $L$. Auf Wunsch besteht das Band aus einem **dünnen** (links,
    0 bis 5 cm) und einem **dicken** Teil (rechts, 5 bis 10 cm), die verknotet sind. Beide Teile tragen dieselbe
    Kraft; der dicke Teil hat die $k$-fache Querschnittsfläche.

    > Wie weit wandert jeder Strich? Ist die Dehnung jedes 1-cm-Stücks gleich?
    > Was ändert sich, wenn ein Teil dicker ist? Welcher Teil dehnt sich stärker, und warum?
    > Woran erkennen Sie die Dehnung im Diagramm $u(x)$?
    """)
    return


@app.cell
def _(mo):
    L = mo.ui.slider(10, 20, step=0.5, value=15, label=r"Länge $L$ in cm", show_value=True)
    zwei = mo.ui.checkbox(value=False, label="dünnes und dickes Band verknotet")
    k = mo.ui.slider(1, 4, step=0.5, value=2, label=r"Flächenverhältnis $k = A_\mathrm{dick}/A_\mathrm{dünn}$",
                     show_value=True)
    mo.hstack([L, zwei, k], justify="start", gap=2)
    return L, k, zwei


@app.cell
def _(BAND, BLAU, GRAU, GRUEN, L, RAND, ROT, k, mo, np, plt, zwei):
    _L0, _xk = 10.0, 5.0
    _dL = L.value - _L0
    if zwei.value:
        # gleiche Kraft, Spannung und Dehnung umgekehrt proportional zur Fläche: eps_duenn = k * eps_dick
        _e2 = _dL / (_xk * (k.value + 1))
        _e1 = k.value * _e2
    else:
        _e1 = _e2 = _dL / _L0

    def _z(v):                                   # Zahl mit Dezimalkomma (Text)
        return f"{v:.2f}".replace(".", ",")

    def _m(v):                                   # Zahl mit Dezimalkomma (Formel, ohne Abstand)
        return f"{v:.2f}".replace(".", "{,}")

    def _u(x):
        x = np.asarray(x, dtype=float)
        return np.where(x <= _xk, _e1 * x, _e1 * _xk + _e2 * (x - _xk))

    _x = np.arange(0, 11)
    _xn = _x + _u(_x)
    _fig, (_ax, _ax2) = plt.subplots(2, 1, figsize=(9, 6.2), gridspec_kw={"height_ratios": [1.15, 1]})

    def _band(y, a, b, d1, d2):
        for (x0, x1, d) in ((a, b[0], d1), (b[0], b[1], d2)):
            _ax.add_patch(plt.Rectangle((x0, y - d / 2), x1 - x0, d, fc=BAND, ec=RAND, lw=0.8))

    _d1, _d2 = (0.12, 0.12 * np.sqrt(k.value)) if zwei.value else (0.2, 0.2)
    # unbelastet (oben) und gedehnt (unten); die gedehnten Teile werden dünner gezeichnet
    _band(2.0, 0, (_xk, _L0), _d1, _d2)
    _band(1.0, 0, (_xk + _u(_xk), L.value), _d1 * 0.85, _d2 * 0.9)
    for _a, _n in zip(_x, _xn):
        _ax.plot([_a, _a], [1.85, 2.15], color="k", lw=1.4)
        _ax.plot([_n, _n], [0.85, 1.15], color="k", lw=1.4)
        _ax.plot([_a, _n], [1.82, 1.18], color=GRAU, lw=0.8, ls="--")
    _ax.plot([0], [2.0], "o", color="#555555"); _ax.plot([0], [1.0], "o", color="#555555")
    _ax.annotate("", xy=(L.value + 1.2, 1.0), xytext=(L.value, 1.0), arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2))
    _ax.text(L.value + 1.3, 1.0, "$F$", color=ROT, va="center", fontsize=13)
    # Lineal
    _ax.add_patch(plt.Rectangle((-0.3, 0.15), 21.6, 0.45, fc="#f4f4f4", ec="#7a7a7a", lw=0.8))
    for _c in np.arange(0, 21.01, 0.5):
        _ax.plot([_c, _c], [0.6, 0.6 - (0.17 if _c % 1 == 0 else 0.09)], color="k", lw=0.6)
        if _c % 1 == 0:
            _ax.text(_c, 0.27, f"{_c:.0f}", ha="center", fontsize=8)
    _ax.text(-0.4, 2.35, "unbelastet", fontsize=10); _ax.text(-0.4, 1.35, "gedehnt", fontsize=10)
    _ax.set_xlim(-0.6, 21.6); _ax.set_ylim(0.1, 2.6); _ax.axis("off")
    # Verschiebung u(x)
    _xx = np.linspace(0, _L0, 201)
    _ax2.plot(_xx, _u(_xx), color=BLAU, lw=2.2)
    _ax2.plot(_x, _u(_x), "o", color=BLAU, ms=4)
    _ax2.set_xlim(0, 10.5); _ax2.set_ylim(0, max(10.5 * max(_e1, _e2), 0.5))
    _ax2.set_xlabel("ursprüngliche Lage $x$ des Strichs in cm"); _ax2.set_ylabel("Verschiebung $u$ in cm")
    _ax2.grid(color=GRAU, lw=0.3)
    if zwei.value:
        _ax2.axvline(_xk, color=GRAU, lw=0.8, ls=":")
        _ax2.text(2.5, _u(2.5) + 0.06 * _ax2.get_ylim()[1], rf"$\varepsilon = {_m(_e1)}$", color=GRUEN, ha="center")
        _ax2.text(7.5, _u(7.5) + 0.06 * _ax2.get_ylim()[1], rf"$\varepsilon = {_m(_e2)}$", color=GRUEN, ha="center")
    else:
        _ax2.text(5, _u(5) + 0.06 * _ax2.get_ylim()[1], rf"$\varepsilon = {_m(_e1)}$", color=GRUEN, ha="center")
    _fig.tight_layout()

    if zwei.value:
        _txt = (rf"Dünner Teil: 5 cm $\to$ {_z(5 + 5 * _e1)} cm, $\varepsilon = {_m(_e1)}$ · "
                rf"dicker Teil: 5 cm $\to$ {_z(5 + 5 * _e2)} cm, $\varepsilon = {_m(_e2)}$. "
                rf"Der dünne Teil dehnt sich $k = {_m(k.value)}$-mal so stark: gleiche Kraft, aber kleinere Fläche, "
                "also größere Spannung.")
    else:
        _txt = (rf"Jedes 1-cm-Stück wird {_z(1 + _e1)} cm lang: $\varepsilon = \Delta l / l = {_m(_e1)}$ "
                rf"($= {100 * _e1:.0f}\,\%$), überall gleich. Die Verschiebung wächst linear, $u = \varepsilon\,x$; "
                "die Steigung der Geraden ist die Dehnung.")
    mo.vstack([_fig, mo.md(_txt)])
    return


if __name__ == "__main__":
    app.run()

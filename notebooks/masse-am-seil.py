import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Masse am Seil")


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
    # Masse am Seil

    Eine Masse $m$ hängt an einem Seil und wird von der waagerechten Kraft $F$ um den Winkel $\alpha$
    ausgelenkt. Am Knoten bilden $m g$, $F$ und die Seilkraft $F_S$ ein **zentrales Kraftsystem**.
    Gleichgewicht heißt: Das Krafteck ist **geschlossen**.

    $$
    F = m g \tan\alpha, \qquad F_S = \frac{m g}{\cos\alpha}
    $$

    > Was passiert mit $F$ und $F_S$, wenn $\alpha$ gegen $90^\circ$ geht?
    """)
    return


@app.cell
def _(mo):
    alpha = mo.ui.slider(0, 85, step=1, value=30, label=r"$\alpha$ in °", show_value=True)
    masse = mo.ui.slider(5, 50, step=1, value=20, label=r"$m$ in kg", show_value=True)
    mo.hstack([alpha, masse], justify="start", gap=3)
    return alpha, masse


@app.cell
def _(BLAU, GRAU, GRUEN, ROT, alpha, masse, mo, np, plt):
    _a = np.radians(alpha.value)
    _mg = masse.value * 9.81
    _F = _mg * np.tan(_a)
    _FS = _mg / np.cos(_a)
    _fig, (_ax1, _ax2, _ax3) = plt.subplots(1, 3, figsize=(10, 3.8), gridspec_kw={"width_ratios": [1, 1, 1.3]})
    # System
    _l = 1.0
    _K = (_l * np.sin(_a), -_l * np.cos(_a))
    _ax1.plot([-0.1, 0.1], [0, 0], color="k", lw=2)
    _ax1.plot([0, _K[0]], [0, _K[1]], color="k", lw=1.6)
    _ax1.plot([_K[0], _K[0]], [_K[1], _K[1] - 0.25], color="k", lw=1.4)
    _ax1.add_patch(plt.Rectangle((_K[0] - 0.08, _K[1] - 0.4), 0.16, 0.15, fc=GRAU, ec="k"))
    _ax1.annotate("", xy=(_K[0] + 0.35, _K[1]), xytext=_K, arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2))
    _ax1.text(_K[0] + 0.37, _K[1] + 0.04, "$F$", color=ROT, fontsize=13)
    _ax1.plot([0, 0], [0, -1.3], color=GRAU, lw=0.8, ls=":")
    _ax1.set_xlim(-0.3, 1.6); _ax1.set_ylim(-1.5, 0.1); _ax1.set_aspect("equal"); _ax1.axis("off")
    _ax1.set_title("System", fontsize=12)
    # Krafteck (geschlossen)
    _s = 1 / max(_FS, 1)
    _P0 = np.array([0.0, 0.0]); _P1 = _P0 + [0, -_mg * _s]; _P2 = _P1 + [_F * _s, 0]
    for _p, _q, _t in ((_P0, _P1, "$mg$"), (_P1, _P2, "$F$"), (_P2, _P0, "$F_S$")):
        _ax2.annotate("", xy=_q, xytext=_p, arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2))
        _ax2.text(*((_p + _q) / 2 + [0.05, 0.02]), _t, color=ROT, fontsize=12)
    _ax2.set_xlim(-0.2, 1.1); _ax2.set_ylim(-1.1, 0.15); _ax2.set_aspect("equal"); _ax2.axis("off")
    _ax2.set_title("Krafteck: geschlossen", fontsize=12, color=GRUEN)
    # Verlauf über alpha
    _al = np.linspace(0, 85, 200)
    _ax3.plot(_al, _mg * np.tan(np.radians(_al)), color=ROT, lw=2, label="$F$")
    _ax3.plot(_al, _mg / np.cos(np.radians(_al)), color=BLAU, lw=2, label="$F_S$")
    _ax3.plot([alpha.value], [_F], "o", color=ROT); _ax3.plot([alpha.value], [_FS], "o", color=BLAU)
    _ax3.set_xlabel(r"$\alpha$ in °"); _ax3.set_ylabel("Kraft in N"); _ax3.set_ylim(0, 8 * _mg)
    _ax3.grid(color=GRAU, lw=0.4); _ax3.legend(frameon=False)
    _fig.tight_layout()
    mo.vstack([_fig, mo.md(rf"""
    | $m g$ | $\alpha$ | $F = mg\tan\alpha$ | $F_S = mg/\cos\alpha$ |
    |--:|--:|--:|--:|
    | {_mg:.1f} N | {alpha.value}° | {_F:.1f} N | {_FS:.1f} N |
    """)])
    return


if __name__ == "__main__":
    app.run()

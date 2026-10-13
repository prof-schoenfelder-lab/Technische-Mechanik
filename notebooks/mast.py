import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Mast mit drei Seilen")


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
    # Mast mit drei Seilen: Gleichgewicht

    An der Spitze eines Mastes ziehen drei Seile: $F_1 = 5$ kN (60° links der Senkrechten),
    $F_2 = 4$ kN (30° rechts der Senkrechten) und $F_3$ unter dem Winkel $\alpha$ zur Senkrechten. Von unten
    drückt der Boden mit $F_B$ gegen den Mast. Alle vier Wirkungslinien gehen durch die Mastspitze.

    > Stellen Sie $F_3$, $\alpha$ und $F_B$ so ein, dass sich das **Krafteck schließt** ($F_R = 0$).
    > Finden Sie mit $F_3 = 3$ kN **beide** Winkel aus der Vorlesung? Was passiert ohne Boden, also mit $F_B = 0$?
    > Wie klein darf $F_3$ werden, damit es überhaupt noch eine Lösung gibt?
    """)
    return


@app.cell
def _(mo):
    F3 = mo.ui.slider(0, 8, step=0.1, value=3.0, label=r"$F_3$ in kN", show_value=True)
    alpha_m = mo.ui.slider(0, 180, step=0.5, value=30, label=r"$\alpha$ in °", show_value=True)
    FB = mo.ui.slider(0, 15, step=0.1, value=5.0, label=r"$F_B$ in kN", show_value=True)
    mo.hstack([F3, alpha_m, FB], justify="start", gap=2)
    return F3, FB, alpha_m


@app.cell
def _(F3, FB, GRAU, GRUEN, ROT, alpha_m, mo, np, plt):
    # Richtungswinkel (mathematisch): F1 bei -150°, F2 bei -60°, F3 bei -90° + alpha, F_B bei +90°
    _kr = [("$F_1$", 5.0, -150.0), ("$F_2$", 4.0, -60.0), ("$F_3$", F3.value, -90.0 + alpha_m.value),
           ("$F_B$", FB.value, 90.0)]
    _v = [(n, F * np.cos(np.radians(w)), F * np.sin(np.radians(w))) for n, F, w in _kr]
    _Rx = sum(c[1] for c in _v)
    _Ry = sum(c[2] for c in _v)
    _zu = abs(_Rx) < 0.08 and abs(_Ry) < 0.08
    _fig, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(9, 4.2))
    # System: Mast, Boden, Kräfte an der Spitze
    _ax1.plot([0, 0], [-10, 0], color="k", lw=5, solid_capstyle="butt", zorder=1)
    _ax1.plot([-6, 6], [-10, -10], color="k", lw=1.5)
    for _x in np.arange(-6, 6, 0.6):
        _ax1.plot([_x, _x - 0.4], [-10, -10.4], color="k", lw=0.6)
    for _n, _fx, _fy in _v[:3]:
        if abs(_fx) + abs(_fy) > 1e-6:
            _ax1.annotate("", xy=(_fx, _fy), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2))
            _ax1.text(_fx * 1.12, _fy * 1.12, _n, color=ROT, fontsize=13, ha="center", va="center")
    if FB.value > 0:
        # Bodenkraft am Mastfuß (drückend, neben die Mastachse gezeichnet)
        _ax1.annotate("", xy=(0.8, -10), xytext=(0.8, -10 - FB.value * 0.3),
                      arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2))
        _ax1.text(1.2, -10 - FB.value * 0.15, "$F_B$", color=ROT, fontsize=13, va="center")
    _ax1.set_xlim(-8, 8); _ax1.set_ylim(-15, 2); _ax1.set_aspect("equal"); _ax1.axis("off")
    _ax1.set_title("Mast mit drei Seilen", fontsize=12)
    # Krafteck
    _P = np.array([0.0, 0.0]); _pts = [_P.copy()]
    for _n, _fx, _fy in _v:
        _Q = _P + [_fx, _fy]
        if np.hypot(_fx, _fy) > 1e-6:
            _ax2.annotate("", xy=_Q, xytext=_P, arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2))
            _m = (_P + _Q) / 2
            _nv = np.array([_fy, -_fx]) / np.hypot(_fx, _fy)      # rechts der Pfeilrichtung
            _ax2.text(*(_m + 0.6 * _nv), _n, color=ROT, fontsize=12, ha="center", va="center")
        _P = _Q; _pts.append(_P.copy())
    if not _zu:
        _ax2.annotate("", xy=_P, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=GRAU, lw=1.5, ls="--"))
        _ax2.text(_P[0] / 2 - 0.5, _P[1] / 2, "$F_R$", color=GRAU, fontsize=12, ha="right")
    _pts = np.array(_pts)
    _ax2.set_xlim(min(_pts[:, 0].min(), 0) - 1.5, max(_pts[:, 0].max(), 0) + 1.5)
    _ax2.set_ylim(min(_pts[:, 1].min(), 0) - 1.5, max(_pts[:, 1].max(), 0) + 1.5)
    _ax2.set_aspect("equal"); _ax2.grid(color=GRAU, lw=0.3)
    _ax2.set_title("Krafteck: " + ("geschlossen" if _zu else "offen"), fontsize=12, color=GRUEN if _zu else ROT)
    _fig.tight_layout()
    if _zu:
        _txt = "**Gleichgewicht:** Das Krafteck ist geschlossen, $F_R = 0$. Der Mast steht."
    else:
        _txt = (rf"$F_{{Rx}} = {_Rx:.2f}$ kN, $F_{{Ry}} = {_Ry:.2f}$ kN: Das Krafteck ist offen, "
                "der Mast wäre nicht in Ruhe.")
    mo.vstack([_fig, mo.md(_txt)])
    return


if __name__ == "__main__":
    app.run()

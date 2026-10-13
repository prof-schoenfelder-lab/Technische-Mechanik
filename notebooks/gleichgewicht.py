import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Gleichgewicht")


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
    # Gleichgewicht

    ## 1 · Von der Resultierenden zum Gleichgewicht

    An der Spitze eines Mastes ziehen drei Seile: $F_1 = 6$ kN (60° links der Senkrechten),
    $F_2 = 3$ kN (30° rechts der Senkrechten) und $F_3$ unter dem Winkel $\alpha$. Von unten drückt der
    Boden mit $F_B$ gegen den Mast. Alle vier Wirkungslinien gehen durch die Mastspitze.

    > Stellen Sie $F_3$, $\alpha$ und $F_B$ so ein, dass sich das **Krafteck schließt**.
    > Wie viele Winkel $\alpha$ gibt es dafür? Was passiert ohne Boden, also mit $F_B = 0$?

    *(Die Werte sind andere als in Aufgabe 1.7.)*
    """)
    return


@app.cell
def _(mo):
    F3 = mo.ui.slider(0, 8, step=0.1, value=4.0, label=r"$F_3$ in kN", show_value=True)
    alpha_m = mo.ui.slider(0, 180, step=0.5, value=30, label=r"$\alpha$ in °", show_value=True)
    FB = mo.ui.slider(0, 15, step=0.1, value=5.0, label=r"$F_B$ in kN", show_value=True)
    mo.hstack([F3, alpha_m, FB], justify="start", gap=2)
    return F3, FB, alpha_m


@app.cell
def _(F3, FB, GRAU, GRUEN, ROT, alpha_m, mo, np, plt):
    # Richtungswinkel (mathematisch): F1 bei -150°, F2 bei -60°, F3 bei -90° + alpha, F_B bei +90°
    _kr = [("$F_1$", 6.0, -150.0), ("$F_2$", 3.0, -60.0), ("$F_3$", F3.value, -90.0 + alpha_m.value),
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
            _ax2.text(_m[0] + 0.3, _m[1] + 0.3, _n, color=ROT, fontsize=12)
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


@app.cell
def _(mo):
    mo.md(r"""
    ## 2 · Masse am Seil

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


@app.cell
def _(mo):
    mo.md(r"""
    ## 3 · Kiste am Seil (Aufgabe 1.3)

    Die waagerechte Kraft $F$ lenkt Seil (a) aus, die Kiste steigt um $h$.
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
    # festes Gelenklager an der Decke
    _ax1.fill([0, -0.06, 0.06], [0, 0.09, 0.09], color="#d9d9d9", ec="k", lw=1)
    _ax1.plot([-0.1, 0.1], [0.09, 0.09], color="k", lw=1.2)
    for _xs in np.linspace(-0.09, 0.09, 7):
        _ax1.plot([_xs, _xs + 0.03], [0.09, 0.13], color="k", lw=0.6)
    _ax1.plot([0], [0], "o", ms=5, mfc="white", mec="k", zorder=5)
    _ax1.text(0.09, 0.03, "$A$", color=GRUEN, fontsize=13)
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
    _ax1.set_ylim(-1.15, 0.16)
    _ax1.set_aspect("equal")
    _ax1.axis("off")
    _ax1.set_title("Seil (a) reißt!" if reisst else "Lage im Gleichgewicht", color=ROT if reisst else "k")
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


if __name__ == "__main__":
    app.run()

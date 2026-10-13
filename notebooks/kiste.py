import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Kiste am Seil")


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
    # Kiste am Seil (Aufgabe 1.3)

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

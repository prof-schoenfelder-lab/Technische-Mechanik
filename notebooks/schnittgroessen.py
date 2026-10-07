import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="Schnittgrößen interaktiv")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    ROT, BLAU, GRUEN, GRAU = "#d40000", "#0050b4", "#006414", "#c8c8c8"
    plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "stix", "font.size": 11})
    return BLAU, GRAU, GRUEN, Polygon, ROT, mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Schnittgrößen interaktiv

    **Träger mit Kragarm** aus der Vorlesung: Festlager $A$ bei $x=0$, Loslager $B$ bei $x=3a$,
    freies Ende bei $x=4a$ mit $a = 1\,\text{m}$.

    > Überlegen Sie **vor** jeder Änderung: Wie verändern sich $Q$ und $M$? Prüfen Sie dann mit dem Regler.
    """)
    return


@app.cell
def _(mo):
    F1 = mo.ui.slider(0, 3000, step=100, value=2000, label=r"$F_1$ in N", show_value=True)
    alpha = mo.ui.slider(0, 90, step=5, value=30, label=r"$\alpha$ in °", show_value=True)
    s = mo.ui.slider(0.0, 3.0, step=0.1, value=1.0, label=r"Angriffspunkt von $F_1$ in m", show_value=True)
    F2 = mo.ui.slider(-1000, 1000, step=50, value=500, label=r"$F_2$ in N (positiv nach unten)", show_value=True)
    mo.hstack([mo.vstack([F1, alpha]), mo.vstack([s, F2])], justify="start", gap=3)
    return F1, F2, alpha, s


@app.cell
def _(F1, F2, alpha, np, s):
    a = 1.0
    xB, xE = 3 * a, 4 * a
    F1v = F1.value * np.sin(np.radians(alpha.value))
    F1h = F1.value * np.cos(np.radians(alpha.value))
    xF = s.value

    FAH = F1h
    FB = (F1v * xF + F2.value * xE) / xB
    FAV = F1v + F2.value - FB

    x = np.linspace(0, xE, 2001)
    stufe = lambda x0: (x > x0).astype(float)
    N = -FAH * (1 - stufe(xF))
    Q = FAV - F1v * stufe(xF) + FB * stufe(xB)
    M = FAV * x - F1v * np.clip(x - xF, 0, None) + FB * np.clip(x - xB, 0, None)
    return FAH, FAV, FB, F1h, F1v, M, N, Q, a, x, xB, xE, xF


@app.cell
def _(BLAU, F1v, F1h, F2, GRAU, GRUEN, M, N, Polygon, Q, ROT, np, plt, x, xB, xE, xF):
    fig, axs = plt.subplots(4, 1, figsize=(7.5, 7.2), sharex=True,
                            gridspec_kw={"height_ratios": [1.1, 1, 1, 1.2]})

    # --- System
    ax = axs[0]
    ax.add_patch(plt.Rectangle((0, -0.04), xE, 0.08, fc=GRAU, ec="k", lw=1))
    for xl, los in ((0, False), (xB, True)):
        ax.add_patch(Polygon([[xl, -0.04], [xl - 0.1, -0.3], [xl + 0.1, -0.3]], fc="#919191", ec="k"))
        if los:
            ax.plot([xl - 0.14, xl + 0.14], [-0.36, -0.36], "k", lw=1)
    def kraftpfeil(x0, y0, dx, dy, farbe, txt):
        ax.annotate("", xy=(x0, y0), xytext=(x0 - dx, y0 - dy),
                    arrowprops=dict(arrowstyle="-|>", color=farbe, lw=2, mutation_scale=14))
        ax.text(x0 - dx * 1.08, y0 - dy * 1.08, txt, color=farbe, ha="center", va="center", fontsize=13)
    lang = 0.75
    Fges = np.hypot(F1v, F1h)
    if Fges > 0:
        kraftpfeil(xF, 0.05, -F1h / Fges * lang * 0.5, -F1v / Fges * lang, ROT, r"$F_1$")
    if F2.value != 0:
        sg = np.sign(F2.value)
        kraftpfeil(xE, 0.05 if sg > 0 else -0.05, 0, -sg * lang, ROT, r"$F_2$")
    ax.text(-0.12, -0.2, "$A$", ha="right"); ax.text(xB + 0.15, -0.2, "$B$")
    ax.set_ylim(-0.55, 0.95); ax.axis("off")

    # --- Verläufe (positive Werte oberhalb der Achse)
    for ax, y, name, _einheit in ((axs[1], N, "N", "N"), (axs[2], Q, "Q", "N"), (axs[3], M, "M", "Nm")):
        # positive Bereiche rot, negative blau
        ax.fill_between(x, y, where=y >= 0, color="#fbe3e3", interpolate=True)
        ax.fill_between(x, y, where=y <= 0, color="#dde7f5", interpolate=True)
        ax.vlines(x[::40], 0, y[::40], color=np.where(y[::40] >= 0, ROT, BLAU), lw=0.5)
        ax.plot(x, np.where(y >= 0, y, np.nan), color=ROT, lw=2)
        ax.plot(x, np.where(y <= 0, y, np.nan), color=BLAU, lw=2)
        ax.axhline(0, color="k", lw=1)
        ax.set_ylabel(f"${name}$ in {_einheit}")
        ax.spines[["top", "right"]].set_visible(False)
        _i = np.argmax(np.abs(y))
        if abs(y[_i]) > 1e-6:
            ax.annotate(f"{y[_i]:.0f}", (x[_i], y[_i]), textcoords="offset points",
                        xytext=(0, 8 if y[_i] > 0 else -14), ha="center", color=ROT if y[_i] > 0 else BLAU)
        lim = max(1.0, np.max(np.abs(y))) * 1.3
        ax.set_ylim(-lim, lim)
        for xs in (xF, xB):
            ax.axvline(xs, color="#999", lw=0.8, ls="--")
    axs[3].set_xlabel("$x$ in m")
    fig.tight_layout()
    fig
    return


@app.cell
def _(FAH, FAV, FB, M, mo, np, x):
    _i = np.argmax(np.abs(M))
    mo.md(rf"""
    | Lagerreaktion | Wert |
    |:--|--:|
    | $F_{{AH}}$ | {FAH:.0f} N |
    | $F_{{AV}}$ | {FAV:.0f} N |
    | $F_B$ | {FB:.0f} N |
    | $\max\lvert M\rvert$ | {abs(M[_i]):.0f} Nm bei $x = {x[_i]:.2f}$ m |
    """)
    return


if __name__ == "__main__":
    app.run()

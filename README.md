# Technische Mechanik – Kursmaterial

Quarto-Website mit Scrollytelling-Vorlesung, druckbaren Seminarblättern (PDF) und
marimo-Notebooks zur Selbstkontrolle.

## Struktur

| Ordner / Datei | Inhalt |
|:--|:--|
| `vorlesung/*.qmd` | Vorlesungsseiten (Scrollytelling) |
| `seminar/*.qmd` | Seminarblätter → HTML **und** PDF (Typst) |
| `notebooks/*.py` | marimo-Notebooks → WebAssembly-Seiten in `_site/notebooks/<name>/` |
| `grafiken/<kapitel>/*.svg` | Grafiken (Inkscape-Ebenen = Scroll-Schritte) |
| `werkzeuge/tmzeichnen.py` | Zeichenbaukasten (Stil, Lager, Lasten, Bemaßung, Schnittgrößen, Verläufe) |
| `werkzeuge/grafiken_<kapitel>.py` | erzeugt die Grafiken eines Kapitels |
| `werkzeuge/ebenen_export.py` | einzelne Ebenen als PNG/PDF/SVG exportieren (z. B. für Folien, Klausur) |
| `assets/` | Scrollytelling (Lua-Filter, JavaScript, CSS) |
| `quellen-transkript/` | Transkripte der handschriftlichen Vorlesung 2013 |

## Bauen und Ansehen

```bash
quarto render          # Grafiken erzeugen, Seiten + PDFs rendern, Notebooks exportieren
python3 -m http.server 8765 --directory _site
```

Dann <http://localhost:8765> öffnen. Die Notebooks brauchen einen HTTP-Server,
direkt per Doppelklick (`file://`) laufen sie nicht.

Einmalig für die Notebooks: `python3 -m venv .venv && .venv/bin/pip install marimo numpy matplotlib uv`

Notebook bearbeiten: `.venv/bin/marimo edit notebooks/schnittgroessen.py`

## Scrollytelling schreiben

```markdown
:::: {.scrolly svg="../grafiken/schnittgroessen/beispiel.svg"}

::: {.schritt zeige="traeger lasten" zoom="30 40 680 175"}
### Überschrift
Text zum Schritt …
:::

::: {.schritt zeige="traeger lasten reaktionen" dimmen="lager" zoom="30 40 680 330"}
…
:::

::::
```

- `zeige`: sichtbare Ebenen (IDs der Inkscape-Ebenen)
- `dimmen`: blass angezeigte Ebenen (Kontext)
- `zoom`: Bildausschnitt `x y breite höhe` (wird animiert, wirkt wie „Morphen“)

Bedienung: Scrollen, oder **Bild↓/Bild↑** bzw. **→/←** (Presenter funktioniert),
Taste **B** = Beamer-Modus (größere Schrift).

## Grafiken in Inkscape bearbeiten

Die SVGs lassen sich direkt in Inkscape öffnen; jede Ebene ist ein Scroll-Schritt.

- **Eine in Inkscape gespeicherte Datei wird beim Rendern nicht mehr überschrieben.**
  Soll sie wieder aus Python erzeugt werden: Datei löschen und `quarto render` aufrufen.
- Neue Ebene in Inkscape: Ebenen-ID über *Objekt → Objekteigenschaften* (oder XML-Editor)
  sinnvoll benennen, z. B. `verlauf-M`, und diese ID in `zeige="…"` verwenden.
- Farben: Lasten rot `#ff0000`, Reaktionen/Schnittgrößen blau `#0050b4`,
  Bemaßung grün `#006414`, Bauteile grau `#c8c8c8`, Lager `#919191`
  (zentral in `werkzeuge/tmzeichnen.py`, Dict `FARBE`).

## Konventionen (wie Vorlesung 2013)

- $x$ längs der Stabachse, $z$ nach unten
- $N$ positiv als Zug; $Q$ am positiven Schnittufer in $+z$; $M$ positiv, wenn die untere Faser gezogen wird
- Verläufe: positive Werte **oberhalb** der Achse (`verlauf(..., positiv_unten=False)`)
- Bezeichnungen: $F_{AH}$, $F_{AV}$, $F_B$, $N$, $Q$, $M$

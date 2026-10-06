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
./bauen.sh vorschau
```

Das Skript spiegelt das Projekt nach `~/Library/Caches/tm-kurs-build`, rendert dort
(auf dem Netzlaufwerk ist Quarto sehr langsam bzw. bleibt hängen), kopiert `_site/` zurück
und startet mit `vorschau` einen Server auf <http://localhost:8765>.
Die Notebooks brauchen einen HTTP-Server, per Doppelklick (`file://`) laufen sie nicht.

Notebook bearbeiten: `~/Library/Caches/tm-kurs-venv/bin/marimo edit notebooks/schnittgroessen.py`

## Planung

`planung/semesterplan.md` ist die zentrale Vorgabe für alle 14 Wochen. Eigene Beispiele
(Skizze/Scan) unter `planung/beispiele/` mit Beispiel-ID ablegen (`B05-2-name.jpg`) und
die ID im Semesterplan eintragen.

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
- Farben (wie Gross): Lasten, Reaktionen und Schnittgrößen rot `#ff0000`, Verläufe rot gefüllt,
  Bemaßung/Lagerbezeichnungen/Winkel grün `#006414`, Bauteile grau `#e6e6e6`, Lager `#d9d9d9`
  (zentral in `werkzeuge/tmzeichnen.py`, Dict `FARBE`).

## Konventionen (wie Vorlesung 2013)

- $x$ längs der Stabachse, $z$ nach unten
- $N$ positiv als Zug; $Q$ am positiven Schnittufer in $+z$; $M$ positiv, wenn die untere Faser gezogen wird
- Verläufe: positive Werte **oberhalb** der Achse (`verlauf(..., positiv_unten=False)`)
- Bezeichnungen: $F_{AH}$, $F_{AV}$, $F_B$, $N$, $Q$, $M$

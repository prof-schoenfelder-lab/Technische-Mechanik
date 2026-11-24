# Prüfskripte

Browser-Prüfungen der gebauten Seite mit Playwright (nutzt das installierte Google Chrome). Sie ersetzen kein
Hinsehen, machen aber Screenshots und Messwerte schnell reproduzierbar.

## Einrichten (einmal je Rechner)

```
python3 -m venv ~/Library/Caches/tm-pruefen-venv
~/Library/Caches/tm-pruefen-venv/bin/pip install playwright pypdf
```

## Benutzen

1. `./bauen.sh` (baut nach `~/Library/Caches/tm-kurs-build/_site`).
2. Vorschau starten (im Hintergrund):
   `python3 -m http.server 8765 --directory ~/Library/Caches/tm-kurs-build/_site`
   (andere Adresse über die Umgebungsvariable `TM_VORSCHAU`).
3. Aus `kurs/` aufrufen: `~/Library/Caches/tm-pruefen-venv/bin/python werkzeuge/pruefen/<skript>.py …`

| Skript | Zweck |
|:--|:--|
| `schritte.py <ausgabeordner> <seite> "<Schritt>" …` | Screenshots einzelner Scroll-Schritte bei 1920 × 1080, meldet MathJax-Fehler |
| `formeln.py <seite> …` | abgesetzte Formeln, die auf die Spaltenbreite verkleinert werden (normal und Beamer) |
| `ebenen.py <ausgabe.png> <datei.svg> [ebene,ebene]` | ausgewählte Ebenen einer Grafik rendern (wie im Browser) |
| `rahmen.py <datei.svg>` | umschließender Rahmen je Ebene (für `zoom`-Angaben) |
| `geraete.py <seite> [ausgabeordner]` | Phone, Tablet, Desktop: Seitenbreite, Inhaltsknopf, Randleiste, Sprung |

`<seite>` ist der Pfad unter `_site`, z. B. `vorlesung/04-schnittgroessen.html`.
Screenshots nicht in den Kursordner schreiben (z. B. nach `/tmp/…`).

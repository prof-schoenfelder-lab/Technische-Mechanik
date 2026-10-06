#!/bin/bash
# Baut die Kursseite lokal (das Netzlaufwerk ist für Quarto zu langsam/unzuverlässig)
# und kopiert das Ergebnis nach _site/ zurück.
#   ./bauen.sh            alles bauen
#   ./bauen.sh vorschau   bauen und lokalen Server auf http://localhost:8765 starten
set -euo pipefail
QUELLE="$(cd "$(dirname "$0")" && pwd)"
LOKAL="${HOME}/Library/Caches/tm-kurs-build"
mkdir -p "$LOKAL"
rsync -a --delete --exclude _site --exclude .quarto --exclude .git --exclude .venv \
      --exclude __pycache__ "$QUELLE/" "$LOKAL/"
# Python-Umgebung für marimo lokal (schnell); einmalig anlegen
if [ ! -x "$LOKAL/../tm-kurs-venv/bin/marimo" ]; then
  python3 -m venv "$LOKAL/../tm-kurs-venv"
  "$LOKAL/../tm-kurs-venv/bin/pip" install -q marimo numpy matplotlib uv
fi
ln -sfn "$LOKAL/../tm-kurs-venv" "$LOKAL/.venv"
cd "$LOKAL"
quarto render
# Ergebnis zurück (inkl. in Inkscape unveränderter, neu erzeugter Grafiken)
rsync -a --delete "$LOKAL/_site/" "$QUELLE/_site/"
rsync -a "$LOKAL/grafiken/" "$QUELLE/grafiken/"
echo "Fertig: $QUELLE/_site"
if [ "${1:-}" = "vorschau" ]; then
  python3 -m http.server 8765 --directory "$LOKAL/_site"
fi

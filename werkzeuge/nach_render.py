"""Wird von Quarto nach dem Rendern ausgeführt: exportiert die marimo-Notebooks
als WebAssembly-Seiten nach _site/notebooks/<name>/ (laufen ohne Server-Python im Browser).

Export zuerst in ein lokales Temp-Verzeichnis und dann per rsync kopieren –
direktes Schreiben auf das Netzlaufwerk ist unzuverlässig."""
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

projekt = Path(__file__).resolve().parent.parent
venv_bin = projekt / ".venv" / "bin"
marimo = venv_bin / "marimo" if (venv_bin / "marimo").exists() else shutil.which("marimo")
env = dict(os.environ, PATH=f"{venv_bin}:{os.environ.get('PATH', '')}")

# Musterlösungen gehören (vorerst) nicht auf die öffentliche Seite: aus _site nach loesungen/ verschieben
for pdf in sorted((projekt / "_site" / "seminar").glob("*-loesungen.pdf")):
    (projekt / "loesungen").mkdir(exist_ok=True)
    shutil.move(str(pdf), projekt / "loesungen" / pdf.name)
    print(f"Musterlösung (nicht veröffentlicht): loesungen/{pdf.name}")

for nb in sorted((projekt / "notebooks").glob("*.py")):
    ziel = projekt / "_site" / "notebooks" / nb.stem
    if not os.environ.get("QUARTO_PROJECT_RENDER_ALL") and (ziel / "index.html").exists():
        continue
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([str(marimo), "export", "html-wasm", str(nb), "-o", tmp,
                        "--mode", "run", "--no-show-code", "-f"], check=True, env=env,
                       stdout=subprocess.DEVNULL)
        ziel.mkdir(parents=True, exist_ok=True)
        subprocess.run(["rsync", "-a", "--delete", f"{tmp}/", f"{ziel}/"], check=True)
    print(f"marimo-Notebook exportiert: {ziel.relative_to(projekt)}")

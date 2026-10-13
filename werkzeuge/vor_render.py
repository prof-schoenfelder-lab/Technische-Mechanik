"""Wird von Quarto vor dem Rendern ausgeführt: erzeugt alle Grafiken neu."""
import subprocess
import sys
from pathlib import Path

hier = Path(__file__).resolve().parent
for skript in sorted(hier.glob("grafiken_*.py")):
    subprocess.run([sys.executable, str(skript)], check=True, cwd=hier, stdout=subprocess.DEVNULL)

# Standbilder für die PDF-Skripte der Vorlesungen
subprocess.run([sys.executable, str(hier / "skript_bilder.py")], check=True, cwd=hier)

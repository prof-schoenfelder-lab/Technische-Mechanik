"""Nur für die Veröffentlichung (GitHub Actions, vor `quarto render`):
entfernt die in entwuerfe.txt genannten Seiten samt Menüeinträgen und ersetzt Links darauf in
index.qmd durch „folgt“. Lokal wird das Skript nicht ausgeführt, dort bleiben die Entwürfe sichtbar."""
import re
from pathlib import Path

projekt = Path(__file__).resolve().parent.parent
liste = projekt / "entwuerfe.txt"
entwuerfe = [z.strip() for z in liste.read_text(encoding="utf-8").splitlines()
             if z.strip() and not z.startswith("#")] if liste.exists() else []

for pfad in entwuerfe:
    (projekt / pfad).unlink(missing_ok=True)
    print("Entwurf ausgeblendet:", pfad)

    # Menüeintrag (href-Zeile und folgende text-Zeile) aus _quarto.yml entfernen
    q = projekt / "_quarto.yml"
    t = q.read_text(encoding="utf-8")
    t = re.sub(r"\n[ \t]*- href: " + re.escape(pfad) + r"\n[ \t]*text:[^\n]*", "", t)
    q.write_text(t, encoding="utf-8")

    # Links in der Übersicht durch „folgt“ ersetzen
    i = projekt / "index.qmd"
    t = i.read_text(encoding="utf-8")
    t = re.sub(r"\[[^\]]*\]\(" + re.escape(pfad) + r"\)", "*folgt*", t)
    i.write_text(t, encoding="utf-8")

"""Gemeinsame Einstellungen der Prüfskripte (lokale Vorschau auf Port 8765, installiertes Google Chrome)."""
import os

ADRESSE = os.environ.get("TM_VORSCHAU", "http://localhost:8765/")


def url(seite):
    return seite if seite.startswith("http") else ADRESSE + seite.lstrip("/")


def browser(p):
    return p.chromium.launch(channel="chrome")

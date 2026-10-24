"""Offline-Fassung der Kursseite (Progressive Web App), aufgerufen von nach_render.py.

Erzeugt in _site/
  - sw.js                 Service Worker: speichert die freigegebenen Seiten samt Schriften, Logos, Skripten
                          und MathJax im Browser, damit sie ohne Internet laufen
  - manifest.webmanifest  damit sich die Seite als App installieren lässt („Zum Home-Bildschirm“)
und ergänzt im <head> jeder HTML-Seite den Verweis auf Manifest und App-Symbol.

Die Versionskennung im Service Worker ist ein Hash über alle gespeicherten Dateien. Ändert sich etwas,
ändert sich sw.js, der Browser lädt beim nächsten Online-Besuch die neue Fassung, und die Seite zeigt
„Neue Fassung – neu laden“ (assets/scrolly.html).

Notebooks (marimo/WebAssembly, über 100 MB) werden nicht gespeichert; offline erscheint dort ein Hinweis."""
import hashlib
import json
from pathlib import Path

# Offline verfügbar: Startseite und alle Vorlesungen und Seminare (samt PDF), die in _site stehen.
# Entwürfe (entwuerfe.txt) fehlen beim Veröffentlichen in _site und sind damit automatisch ausgenommen.
SEITEN_MUSTER = ["index.html", "vorlesung/*.html", "seminar/*.html"]
DATEI_MUSTER = ["seminar/*.pdf"]
# Ordner, die vollständig gespeichert werden (Skripte, Stile, Schriften, Logos, App-Symbol)
ORDNER = ["site_libs", "assets"]
EINZELN = ["search.json", "manifest.webmanifest"]

MANIFEST = {
    "name": "Technische Mechanik (M279)",
    "short_name": "Techn. Mechanik",
    "description": "Vorlesung Technische Mechanik – Statik und Festigkeitslehre, HTWK Leipzig",
    "lang": "de",
    "start_url": "./index.html",
    "scope": "./",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#0050b4",
    "icons": [
        {"src": "assets/app/symbol-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "assets/app/symbol-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "assets/app/symbol-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}

# MathJax 4 lädt seine Schrift aus einem eigenen Paket (@mathjax/mathjax-newcm-font@<Version>), je nach Formeln
# einer Seite unterschiedliche Teile. Damit auch Seiten, die nie online geöffnet wurden, offline ihre Formeln zeigen,
# speichert der Service Worker das ganze Paket (ca. 2,2 MB), sobald er die Version an einer geladenen Datei erkennt.
# Dateinamen aus dem Paket 4.1.3 (data.jsdelivr.com); fehlt eine Datei in einer späteren Version, wird sie übersprungen.
SCHRIFT_WOFF2 = [
    "ab", "abi", "ai", "ar", "arl", "b-a", "b", "bi", "br", "brd", "brk", "c", "cb", "ch", "chb", "chbi",
    "chi", "cy", "cyb", "cybi", "cyi", "cyss", "cyssb", "cyssbi", "cyssi", "ds", "dv", "em", "f", "fb", "gk",
    "gkb", "gkbi", "gki", "gkss", "gkssb", "gkssbi", "gkssi", "he", "heb", "hebi", "hei", "i", "lb", "li",
    "lib", "lo", "lr", "lt", "m", "mar", "mi", "ml", "mm", "msh", "mx", "n", "ob", "os", "ph", "phb", "phbi",
    "phi", "phss", "phssb", "phssbi", "phssi", "pu", "pub", "pubi", "pui", "rb", "s", "s3", "s4", "s5", "s6",
    "s7", "sb", "sh", "shb", "shbi", "shi", "so", "ss", "ssb", "ssbi", "ssbix", "ssbx", "ssi", "ssix", "sslb",
    "ssli", "sslib", "sslr", "ssx", "sy", "syb", "sybi", "syi", "u-a", "u", "v", "vx", "zero"
]
SCHRIFT_DYNAMIC = [
    "PUA", "accents-b-i", "accents", "arabic", "arrows", "braille-d", "braille", "calligraphic", "cherokee",
    "cyrillic-ss", "cyrillic", "devanagari", "double-struck", "fraktur", "greek-ss", "greek", "hebrew",
    "latin-b", "latin-bi", "latin-i", "latin", "marrows", "math", "monospace-ex", "monospace-l", "monospace",
    "mshapes", "phonetics-ss", "phonetics", "sans-serif-b", "sans-serif-bi", "sans-serif-ex", "sans-serif-i",
    "sans-serif-r", "sans-serif", "script", "shapes", "symbols-b-i", "symbols", "variants"
]
SCHRIFT_DATEIEN = ([f"chtml/woff2/mjx-ncm-{n}.woff2" for n in SCHRIFT_WOFF2]
                   + [f"chtml/dynamic/{n}.js" for n in SCHRIFT_DYNAMIC])

KOPF = ('<link rel="manifest" href="{o}manifest.webmanifest">'
        '<meta name="theme-color" content="#0050b4">'
        '<link rel="apple-touch-icon" href="{o}assets/app/symbol-180.png">'
        '<meta name="apple-mobile-web-app-title" content="Techn. Mechanik">')

SW = r"""// Service Worker der Kursseite – erzeugt von werkzeuge/offline.py, nicht von Hand ändern.
const VERSION = "__VERSION__";
const CACHE = "tm-" + VERSION;          // Seiten und Dateien dieser Fassung
const CDN_CACHE = "tm-cdn";             // MathJax (bleibt über Fassungen hinweg erhalten)
const DATEIEN = __DATEIEN__;
const SEITEN = new Set(__SEITEN__.map(p => new URL(p, self.registration.scope).href));
const MATHJAX = "https://cdn.jsdelivr.net/npm/mathjax@4/";
const MJ_PAKETE = "https://cdn.jsdelivr.net/npm/@mathjax/";   // Schrift von MathJax 4 (eigenes Paket)
const SCHRIFT = __SCHRIFT__;
const istMathJax = u => u.startsWith(MATHJAX) || u.startsWith(MJ_PAKETE);

// Ganzes Schriftpaket speichern, sobald die Version bekannt ist (an einer geladenen Datei erkennbar)
// je Paketversion nur einmal
const schriftLaeuft = new Map();
function schriftSpeichern(urls) {
  const m = urls.map(u => u.match(/^(https:\/\/cdn\.jsdelivr\.net\/npm\/@mathjax\/mathjax-newcm-font@[^/]+\/)/)).find(Boolean);
  if (!m) return Promise.resolve();
  if (!schriftLaeuft.has(m[1])) schriftLaeuft.set(m[1], caches.open(CDN_CACHE).then(c => Promise.all(SCHRIFT.map(f =>
    c.match(m[1] + f).then(da => da || c.add(m[1] + f).catch(() => {}))))));
  return schriftLaeuft.get(m[1]);
}
// Dateien, die MathJax auf jeder Seite mit Formeln lädt (Satz und Sprachausgabe)
const MJ_GRUND = ["tex-chtml.js", "sre/speech-worker.js", "sre/mathmaps/base.json", "sre/mathmaps/en.json",
                  "sre/mathmaps/nemeth.json"];

const html = (titel, text) => new Response(
  `<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
   <title>${titel}</title><body style="font-family:'Source Sans Pro',system-ui,sans-serif;margin:2rem;color:#333;line-height:1.5">
   <h2 style="color:#0050b4">${titel}</h2><p>${text}</p></body></html>`,
  { headers: { "Content-Type": "text/html; charset=utf-8" } });

self.addEventListener("install", e => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(DATEIEN);
    // MathJax gleich mitspeichern, auch wenn die erste Seite (Startseite) keine Formeln hat: Die Version der
    // Schrift ist die von MathJax (package.json), damit lässt sich das Schriftpaket sofort holen
    try {
      const cdn = await caches.open(CDN_CACHE);
      await Promise.all(MJ_GRUND.map(f => cdn.match(MATHJAX + f).then(da => da || cdn.add(MATHJAX + f).catch(() => {}))));
      const paket = await (await fetch(MATHJAX + "package.json")).json();
      await schriftSpeichern([MJ_PAKETE + "mathjax-newcm-font@" + paket.version + "/"]);
    } catch (_) {}
  })());
});

self.addEventListener("activate", e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith("tm-") && k !== CACHE && k !== CDN_CACHE) await caches.delete(k);
    await self.clients.claim();
  })());
});

self.addEventListener("message", e => {
  if (e.data === "aktualisieren") self.skipWaiting();
  // Beim ersten Besuch lädt MathJax, bevor der Service Worker die Seite übernimmt: nachträglich speichern
  if (e.data && e.data.typ === "nachladen") {
    const urls = e.data.urls.filter(istMathJax);
    e.waitUntil(caches.open(CDN_CACHE).then(c => Promise.all(
      urls.map(u => c.match(u).then(m => m || c.add(u).catch(() => {})))
    )).then(() => schriftSpeichern(urls)));
  }
});

// Seiten: zuerst aus dem Netz (immer die aktuelle Fassung), ohne Netz aus dem Speicher
async function seite(req) {
  const c = await caches.open(CACHE);
  const url = new URL(req.url); url.hash = ""; url.search = "";
  if (url.pathname.endsWith("/")) url.pathname += "index.html";
  try {
    const antwort = await fetch(req);
    if (antwort.ok && SEITEN.has(url.href)) c.put(url.href, antwort.clone());
    return antwort;
  } catch (_) {
    return (await c.match(url.href)) || html("Offline nicht verfügbar",
      'Diese Seite ist ohne Internet noch nicht verfügbar. <a href="' + self.registration.scope + 'index.html">Zur Übersicht</a>');
  }
}

// Übrige Dateien: sofort aus dem Speicher, im Hintergrund auffrischen
async function datei(req, cacheName) {
  const c = await caches.open(cacheName);
  const gespeichert = await c.match(req, { ignoreSearch: true });
  const netz = fetch(req).then(a => { if (a.ok) c.put(req, a.clone()); return a; });
  if (gespeichert) { netz.catch(() => {}); return gespeichert; }
  return netz;
}

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (istMathJax(url.href)) { e.respondWith(datei(req, CDN_CACHE)); return; }
  if (url.origin !== location.origin) {
    // übrige externe Skripte (z. B. Polyfill) offline still auslassen
    if (req.destination === "script") e.respondWith(fetch(req).catch(() => new Response("", { headers: { "Content-Type": "text/javascript" } })));
    return;
  }
  if (!url.href.startsWith(self.registration.scope)) return;
  if (url.pathname.includes("/notebooks/")) {
    e.respondWith(fetch(req).catch(() => req.mode === "navigate"
      ? html("Nur mit Internet", "Die Notebooks rechnen mit Python im Browser und sind nur online verfügbar.")
      : Response.error()));
    return;
  }
  if (req.mode === "navigate") { e.respondWith(seite(req)); return; }
  e.respondWith(datei(req, CACHE));
});
"""


def erzeugen(site: Path):
    (site / "manifest.webmanifest").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2), encoding="utf-8")

    # Kopf jeder HTML-Seite ergänzen (nicht in den Notebooks); Pfad relativ zur Seite
    for h in site.rglob("*.html"):
        rel = h.relative_to(site)
        if rel.parts[0] == "notebooks":
            continue
        text = h.read_text(encoding="utf-8")
        if 'rel="manifest"' in text or "</head>" not in text:
            continue
        o = "../" * (len(rel.parts) - 1)
        h.write_text(text.replace("</head>", KOPF.format(o=o) + "</head>", 1), encoding="utf-8")

    def suche(muster):
        return [str(p.relative_to(site)) for m in muster for p in sorted(site.glob(m)) if "-loesungen" not in p.name]

    seiten = suche(SEITEN_MUSTER)
    dateien = seiten + suche(DATEI_MUSTER) + [e for e in EINZELN if (site / e).exists()]
    for d in ORDNER:
        dateien += sorted(str(p.relative_to(site)) for p in (site / d).rglob("*")
                          if p.is_file() and p.name != ".DS_Store")

    h = hashlib.sha256(SW.encode())
    for d in dateien:
        h.update(d.encode())
        h.update((site / d).read_bytes())
    version = h.hexdigest()[:12]

    sw = (SW.replace("__VERSION__", version)
            .replace("__DATEIEN__", json.dumps(dateien, ensure_ascii=False))
            .replace("__SEITEN__", json.dumps(seiten, ensure_ascii=False))
            .replace("__SCHRIFT__", json.dumps(SCHRIFT_DATEIEN)))
    (site / "sw.js").write_text(sw, encoding="utf-8")
    groesse = sum((site / d).stat().st_size for d in dateien) / 1e6
    print(f"Offline-Fassung: {len(seiten)} Seiten, {len(dateien)} Dateien, {groesse:.1f} MB, Version {version}")


if __name__ == "__main__":
    erzeugen(Path(__file__).resolve().parent.parent / "_site")

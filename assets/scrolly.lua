--[[
Scrollytelling für Quarto (nur HTML).

Syntax in .qmd:

  :::: {.scrolly svg="../grafiken/schnittgroessen/beispiel.svg"}
  ::: {.schritt zeige="traeger lasten" dimmen="bereiche" zoom="30 30 620 200"}
  Text zum Schritt …
  :::
  ::::

- svg:    Grafik mit Inkscape-Ebenen (id der Ebene = Name in zeige/dimmen)
- zeige:  sichtbare Ebenen
- dimmen: blass dargestellte Ebenen (Kontext)
- zoom:   Bildausschnitt als viewBox "x y breite höhe" (wird animiert)

In anderen Formaten (PDF) wird die Grafik mit allen Ebenen statisch eingefügt.
]]

local function lies(pfad)
  local f = io.open(pfad, "r")
  if not f then return nil end
  local inhalt = f:read("*a")
  f:close()
  return inhalt
end

-- ::: {.vertiefung titel="…"} … :::  →  aufklappbarer Erklärtext (HTML),
-- in PDF als normaler Absatz mit Überschrift
local function vertiefung(el)
  local titel = el.attributes["titel"] or "Ausführlicher"
  if quarto.doc.is_format("html") then
    local out = { pandoc.RawBlock("html", '<details class="vertiefung"><summary>' .. titel .. '</summary>') }
    for _, b in ipairs(el.content) do table.insert(out, b) end
    table.insert(out, pandoc.RawBlock("html", "</details>"))
    return out
  end
  local out = { pandoc.Para({ pandoc.Strong({ pandoc.Str(titel) }) }) }
  for _, b in ipairs(el.content) do table.insert(out, b) end
  return out
end

-- ::: {.notebook titel="…" src="…"} Text :::  →  aufklappbares, eingebettetes marimo-Notebook
-- (iframe erst beim Aufklappen geladen) mit Link zum Öffnen im eigenen Tab; in PDF nur Text + Hinweis
local function notebook(el)
  local titel = el.attributes["titel"] or "Interaktives Notebook"
  local src = el.attributes["src"]
  if quarto.doc.is_format("html") then
    local out = { pandoc.RawBlock("html", '<details class="notebook"><summary>' .. titel .. '</summary>') }
    for _, b in ipairs(el.content) do table.insert(out, b) end
    table.insert(out, pandoc.RawBlock("html",
      '<p class="small"><a href="' .. src .. '" target="_blank">Im eigenen Tab öffnen</a> ' ..
      '(der erste Start dauert einige Sekunden)</p>' ..
      '<iframe class="notebook-rahmen" loading="lazy" src="' .. src .. '" title="' .. titel .. '"></iframe></details>'))
    return out
  end
  local url = "https://prof-schoenfelder-lab.github.io/Technische-Mechanik/" .. src:gsub("^%.%./", ""):gsub("index%.html$", "")
  local out = { pandoc.Para({ pandoc.Strong({ pandoc.Str(titel) }) }) }
  for _, b in ipairs(el.content) do table.insert(out, b) end
  table.insert(out, pandoc.Para({ pandoc.Link("→ Notebook im Browser öffnen", url) }))
  return out
end

-- PDF: Schritte zu Gruppen zusammenfassen (solange ein Schritt nur Ebenen hinzufügt) und je Gruppe
-- ein Standbild aus grafiken/_skript/ einsetzen (erzeugt von werkzeuge/skript_bilder.py, gleiche Regel)
local function ebenen_von(div)
  local menge, liste = {}, {}
  for _, name in ipairs({ "zeige", "dimmen" }) do
    for w in (div.attributes[name] or ""):gmatch("%S+") do
      if not menge[w] then menge[w] = true; table.insert(liste, w) end
    end
  end
  return menge, liste
end

local function obermenge(a, b)
  for k in pairs(b) do if not a[k] then return false end end
  return true
end

local function bild(svg_rel, liste, basis)
  table.sort(liste)
  local name = pandoc.utils.sha1(svg_rel .. "|" .. table.concat(liste, " ")):sub(1, 12)
  local rel = "../grafiken/_skript/" .. name .. ".svg"
  local inhalt = lies(pandoc.path.join({ basis, rel }))
  if not inhalt then
    quarto.log.warning("scrolly: Standbild fehlt für " .. svg_rel .. " [" .. table.concat(liste, " ") .. "]")
    return pandoc.Para({ pandoc.Image({}, "../" .. svg_rel) })
  end
  local b = tonumber(inhalt:match('<svg[^>]-width="([%d.]+)"')) or 600
  local h = tonumber(inhalt:match('<svg[^>]-height="([%d.]+)"')) or 400
  local cm = math.min(b * 0.021, 16, 10 * b / h)
  return pandoc.Para({ pandoc.Image({}, rel, "", pandoc.Attr("", {}, { { "width", string.format("%.1fcm", cm) } })) })
end

function standbilder(el, src, basis)
  local svg_rel = src:gsub("^%.%./", "")
  local out, akt, akt_liste, puffer = {}, nil, nil, {}
  local function abschliessen()
    if akt then
      table.insert(out, bild(svg_rel, akt_liste, basis))
      for _, b in ipairs(puffer) do table.insert(out, b) end
    end
    puffer = {}
  end
  for _, b in ipairs(el.content) do
    if b.t == "Div" and b.classes:includes("schritt") then
      local menge, liste = ebenen_von(b)
      if not (akt and obermenge(menge, akt)) then abschliessen() end
      akt, akt_liste = menge, liste
      for _, x in ipairs(b.content) do table.insert(puffer, x) end
    else
      table.insert(puffer, b)
    end
  end
  abschliessen()
  return out
end

function Div(el)
  if el.classes:includes("vertiefung") then return vertiefung(el) end
  if el.classes:includes("notebook") then return notebook(el) end
  if not el.classes:includes("scrolly") then return nil end
  local src = el.attributes["svg"]
  local basis = pandoc.path.directory(quarto.doc.input_file)
  local pfad = pandoc.path.join({ basis, src })

  if not quarto.doc.is_format("html") then
    return standbilder(el, src, basis)
  end

  local svg = lies(pfad)
  if not svg then
    quarto.log.error("scrolly: Grafik nicht gefunden: " .. pfad)
    return nil
  end
  svg = svg:gsub("^%s*<%?xml.-%?>%s*", "")

  local id = el.identifier ~= "" and (' id="' .. el.identifier .. '"') or ""
  local out = {
    pandoc.RawBlock("html",
      '<div class="scrolly"' .. id .. '><div class="scrolly-grafik"><div class="scrolly-sticky">'
      .. svg .. '<div class="scrolly-zaehler"></div></div></div><div class="scrolly-schritte">')
  }
  for _, b in ipairs(el.content) do table.insert(out, b) end
  table.insert(out, pandoc.RawBlock("html", "</div></div>"))
  return out
end

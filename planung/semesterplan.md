# Semesterplan Technische Mechanik (M279) – Planungsdatei

Diese Datei ist die **zentrale Vorgabe** für Vorlesung, Seminar und Grafiken.
Bitte frei bearbeiten: ändern, streichen, umsortieren, ergänzen. Alles unter
„Wünsche/Notizen“ wird bei der Umsetzung berücksichtigt.

**Vorbefüllt aus:** Plan WS 24/25 (L. Merker), Modulbeschreibung M279, handschriftliche
Vorlesung 2013 (Transkripte in `../quellen-transkript/`), Aufgabensammlung Götz (`G 1.5.1` = Aufgabe 1.5.1),
Gross TM 1 / Dankert.

## So stellen Sie den Bezug zu eigenen Beispielen her

1. Skizze, Scan oder Foto in `planung/beispiele/` ablegen, Dateiname beginnt mit der **Beispiel-ID**:
   `B05-2-abgesetzter-stab.jpg` (= Woche 5, Beispiel 2). Mehrere Seiten: `B05-2-a.jpg`, `B05-2-b.jpg`.
   Auch PDF oder Inkscape-SVG sind möglich.
2. In der Woche unten unter **Beispiele Vorlesung** bzw. **Seminar** eine Zeile mit derselben ID eintragen
   und kurz sagen, **was gezeigt werden soll** (Schritte, Schwerpunkt, Zahlenwerte, ob mit Lösung).
3. Ich zeichne daraus die Grafik im Kursstil (Inkscape-Ebenen = Scroll-Schritte), baue die Seite
   und trage den Status hier ein.

Beispielzeile:

```
- B05-2 · Abgesetzter Stab Stahl/Alu (Datei: beispiele/B05-2-abgesetzter-stab.jpg)
  Schritte: System → Freischnitt → N(x) → σ(x) → Verlängerung; Zahlen wie VL 2013 S. 19
```

Status-Kürzel: ⬜ offen · 🟨 in Arbeit · ✅ fertig · 🔁 Überarbeitung gewünscht

---

## Woche 1 · Einführung, Kräfte und Momente, Gleichgewicht ⬜

- **Lernziele:** Kraft als gebundener Vektor; Moment und Kräftepaar; Axiome und Schnittprinzip; Gleichgewicht im zentralen und allgemeinen ebenen Kraftsystem
- **Inhalte Vorlesung:**
  1. Einordnung: Statik, Festigkeitslehre, Dynamik; Modelle und Annahmen (starrer Körper)
  2. Vektorrechnung kompakt (Komponenten, Betrag, Winkel, Kreuzprodukt)
  3. Kraft, Wirkungslinie, Axiome der Statik, Schnittprinzip / Freikörperbild
  4. Zentrales Kraftsystem: Resultierende, Krafteck, Gleichgewicht
  5. Moment, Kräftepaar, Versatzmoment; allgemeines Kraftsystem, 3 GGB in der Ebene
- **Beispiele Vorlesung:**
  - B01-1 · Zwei Kräfte, Resultierende ($F_R \approx 31{,}4$ N) – VL 2013 Teil 1
  - B01-2 · Masse an zwei Seilen (277,7 / 298,1 N) – VL 2013 Teil 1
  - B01-3 · Scheibe mit 4 Kräften, Wirkungslinie der Resultierenden – VL 2013 Teil 1 (Achtung: $\alpha_R$ im Original falsch, richtig −36,9°)
- **Seminar:** G 1.1.1, G 1.1.4, G 1.2.x (auswählen)
- **Hausaufgaben:**
- **Notebook-Idee:** Kräfte per Regler, Krafteck und Resultierende live
- **Quellen:** Transkript 1; Gross Kap. 1–3; Dankert Kap. 1–3
- **Wünsche/Notizen:**

## Woche 2 · Lager- und Gelenkreaktionen, Streckenlasten, Haftung ⬜

- **Lernziele:** Lagerarten und Wertigkeit; statische Bestimmtheit; Lagerreaktionen ein- und mehrteiliger Systeme; Streckenlasten ersetzen; Haftbedingung
- **Inhalte Vorlesung:**
  1. Lagerarten (Los-/Festlager, Einspannung, Gelenk, Pendelstütze), Abzählkriterium $3n = a + z$
  2. Lagerreaktionen: Rechenschema
  3. Streckenlasten: Resultierende und Lage (Rechteck, Dreieck)
  4. Systeme mit Gelenk
  5. Haftung (Coulomb), Haftungskegel, Fallunterscheidung
- **Beispiele Vorlesung:**
  - B02-1 · Einfeldträger mit Kragarm ($2{,}7F$ / $0{,}3F$) – VL 2013 Teil 1
  - B02-2 · Eingespannter Balken ($-3F$, $-2{,}5FL$) – VL 2013 Teil 1
  - B02-3 · Kfz mit Anhänger – VL 2013 Teil 1
  - B02-4 · Leiter an der Wand (Haftung) – VL 2013 Teil 4
- **Seminar:** G 1.3.x, G 1.7.x (auswählen)
- **Hausaufgaben:**
- **Offene Frage:** Fachwerke (VL 2013 Teil 2: Knotenschnitt, Ritterschnitt) – eigene Einheit, hier integrieren oder weglassen?
- **Quellen:** Transkripte 1, 2, 4; Gross Kap. 5, 6, 9; Dankert Kap. 5, 6, 9
- **Wünsche/Notizen:**

## Woche 3 · Schnittgrößen ✅ (Prototyp)

- **Lernziele:** Schnittgrößen definieren, Vorzeichenkonvention anwenden; Bereiche einteilen; $N(x)$, $Q(x)$, $M(x)$ berechnen und zeichnen; Differentialbeziehungen nutzen
- **Inhalte Vorlesung:** siehe Seite `vorlesung/03-schnittgroessen.qmd`
- **Beispiele Vorlesung:**
  - B03-1 · Träger mit Kragarm, $F_1$ schräg, $F_2$ am Ende – VL 2013 Teil 3 S. 5–8 ✅
  - B03-2 · Einfeldträger mit Dreieckslast, Integration – VL 2013 Teil 3 S. 11–14 ✅
  - B03-3 · Dreigelenkrahmen – VL 2013 Teil 3 S. 17–23 ⬜ (**Entscheidung nötig:** Auftragsseite von $M$ beim Rahmen, siehe unten)
- **Seminar:** G 1.5.1, G 1.5.6, G 1.5.3 ✅
- **Hausaufgaben:** G 1.5.8, G 1.5.5 ✅
- **Notebook:** `notebooks/schnittgroessen.py` ✅
- **Quellen:** Transkript 3; `planung/abgleich-literatur-schnittgroessen.md`; Gross Kap. 7; Dankert Kap. 7
- **Wünsche/Notizen:**

## Woche 4 · Wiederholung Statik ⬜

- **Inhalte:** Beispiele vorrechnen, typische Fehler, Probeaufgaben
- **Beispiele Vorlesung:**
- **Seminar:**
- **Wünsche/Notizen:**

## Woche 5 · Einführung Festigkeitslehre: Spannung und Verformung ⬜

- **Lernziele:** Annahmen der Elastostatik; Beanspruchungsarten; Spannung (Normal-/Schub-), Dehnung, Gleitung; Kerbwirkung qualitativ
- **Inhalte Vorlesung:**
  1. Festigkeit und Steifigkeit, Annahmen (A)–(D) – VL 2013 Teil 6 §1
  2. Fünf Beanspruchungsarten
  3. Spannung im Stab $\sigma = N/A$, St.-Venant
  4. Kerbspannungen ($k_t$)
  5. Dehnung $\varepsilon = \mathrm{d}u/\mathrm{d}x$
  6. Ebener Spannungszustand, Hauptspannungen (Plan WS 24/25; in VL 2013 nicht enthalten)
- **Beispiele Vorlesung:**
  - B05-1 · Hängender Stab / veränderlicher Querschnitt (qualitativ) – VL 2013 Teil 6 S. 7
  - B05-2 · Bohrung in Platte, $k_t \approx 3$ – VL 2013 Teil 6 S. 10
- **Seminar:** G 2.1.x
- **Quellen:** Transkript 6; Gross TM 2 (fehlt im Ordner); Dankert Kap. 12
- **Wünsche/Notizen:**

## Woche 6 · Stoffgesetz, Zugversuch ⬜

- **Inhalte:** Zugversuch, Hooke, E-Modul, $G$, Querkontraktion $\nu$, Temperaturdehnung
- **Beispiele Vorlesung:**
  - B06-1 · Zugversuch S235 ($\varepsilon \approx 0{,}11\,\%$) – VL 2013 Teil 6 S. 14
- **Seminar:**
- **Quellen:** Transkript 6; Dankert Kap. 12–14
- **Wünsche/Notizen:**

## Woche 7 · Zug und Druck, statisch unbestimmte Stabsysteme ⬜

- **Inhalte:** Spannungs- und Verformungsgleichung, Randbedingungen; statisch unbestimmt: Statik → Kinematik → Stoffgesetz; Temperaturspannungen
- **Beispiele Vorlesung:**
  - B07-1 · Abgesetzter Stab Stahl/Alu – VL 2013 Teil 6 S. 19–21
  - B07-2 · Stab zwischen zwei Wänden, Wärmespannung (−252 N/mm²) – VL 2013 Teil 7 S. 1–5
  - B07-3 · Starrer Balken an zwei Stäben – VL 2013 Teil 7 S. 5–9 (Achtung: $F_{AV} = -0{,}082F$, nicht −0,084F)
- **Seminar:** G 2.2.x
- **Quellen:** Transkripte 6, 7; Dankert Kap. 14
- **Wünsche/Notizen:**

## Woche 8 · Torsion ⬜

- **Inhalte:** Kreis- und Kreisringquerschnitt, Spannungs- und Verformungsgleichung, polares Flächenmoment, dünnwandige geschlossene Profile
- **Beispiele Vorlesung:** (keine Unterlagen aus 2013 – **bitte Beispiele/Skizzen beisteuern**)
- **Seminar:** G 2.3.x
- **Quellen:** Dankert Kap. 21
- **Wünsche/Notizen:**

## Woche 9 · Flächenmomente, gerade Biegung ⬜

- **Inhalte:** Schwerpunkt, Flächenträgheitsmomente, Steiner; Bernoulli-Hypothese, $\sigma = M_y z / I_{yy}$, Widerstandsmoment, Bemessung
- **Beispiele Vorlesung:**
  - B09-1 · L-Profil: $I_{xx}$, $I_{yy}$, $I_{xy}$ – VL 2013 Teil 5
  - B09-2 · Kragträger Kreis/Ring/Rechteck im Vergleich – VL 2013 Teil 8 S. 12–15
  - B09-3 · 3-Punkt-Biegung – VL 2013 Teil 8 S. 19–22
- **Seminar:** G 1.8.x, G 1.9.x, G 2.4.x
- **Quellen:** Transkripte 5, 8; Dankert Kap. 16
- **Offene Frage:** Flächenmomente als eigene Woche oder hier integriert?
- **Wünsche/Notizen:**

## Woche 10 · Schiefe Biegung, Biegung mit Längskraft ⬜

- **Inhalte:** Hauptachsen, Superposition $N/A + M z/I$, Nulllinie
- **Beispiele Vorlesung:**
  - B10-1 · Exzentrischer Zug, Nulllinie bei $h/6$ – VL 2013 Teil 9 S. 2–3
  - B10-2 · Schräge Endlast, Nulllinie diagonal – VL 2013 Teil 9 S. 8–10
  - B10-3 · Welle (Ü 13 4.5) – VL 2013 Teil 9 S. 11–17 (Achtung: $\sigma_{max} \approx 13{,}8$ statt 18,0 N/mm²)
- **Seminar:** G 2.4.x
- **Quellen:** Transkript 9; Dankert Kap. 19
- **Wünsche/Notizen:**

## Woche 11 · Zusammengesetzte Beanspruchung, Festigkeitshypothesen ⬜

- **Inhalte:** mehrachsiger Spannungszustand, Vergleichsspannung (Normalspannungs-, Schubspannungs-, Gestaltänderungsenergiehypothese), Auslegen und Nachweisen
- **Beispiele Vorlesung:** (keine Unterlagen aus 2013 – **bitte beisteuern**)
- **Seminar:** G 2.5.x, G 2.6.x
- **Quellen:** Dankert Kap. 22
- **Wünsche/Notizen:**

## Woche 12 · Knickung ⬜

- **Inhalte:** Euler-Fälle, Theorie 2. Ordnung an Beispielen
- **Beispiele Vorlesung:** (bitte beisteuern)
- **Seminar:** G 2.7.x
- **Wünsche/Notizen:**

## Woche 13 · Energiemethoden ⬜

- **Inhalte:** Prinzip der virtuellen Arbeit, Castigliano, Menabrea
- **Beispiele Vorlesung:** (bitte beisteuern)
- **Seminar:**
- **Wünsche/Notizen:**

## Woche 14 · Wiederholung und Prüfungsvorbereitung ⬜

- **Inhalte:** gemeinsames Lösen einer Probeklausur
- **Wünsche/Notizen:**

---

## Offene Entscheidungen

1. **Rahmen:** Auf welcher Seite wird $M$ aufgetragen? Gross/Dankert: positiv auf der der Bezugsfaser
   abgewandten Seite (wie beim Balken „positiv oben“). VL 2013 beim Rahmen: auf der Zugseite.
   Vorschlag: wie Gross/Dankert, mit Hinweis auf die Zugseiten-Darstellung in der Tragwerksplanung.
2. **Fachwerke:** eigene Einheit, in Woche 2 integrieren oder weglassen?
3. **Flächenmomente:** eigene Woche oder in Woche 9 integriert?
4. **Gross TM 2 (Elastostatik):** Falls vorhanden, bitte ebenfalls in `Literatur/` ablegen.

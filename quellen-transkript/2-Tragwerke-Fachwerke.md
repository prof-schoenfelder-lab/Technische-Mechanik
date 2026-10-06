# Technische Mechanik – Statik: 3. Tragwerke und Fachwerke (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen (Prof. Schönfelder)
Quelle: `Quellen/Vorlesung-2013/2-Tragwerke-Fachwerke.pdf` (17 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten/Ergebnisse, Grün = Bemaßungen, Kommentare, Korrekturen.
- Text sinngemäß-wörtlich; durchgestrichene Passagen nur, wenn inhaltlich relevant (als ~~…~~).
- Unsichere Lesungen sind mit [?] markiert; Anmerkungen zur Nachrechnung mit [Prüfung: …].

---

## Seite 1

### 3. Tragwerke

- Tragwerke sind die Teile einer Konstruktion, die Kräfte aufnehmen und ableiten
  - ↳ verschiedene Kategorien:
    - **Stab (Seil)** (rot eingerahmt)
    - Balken – später in Vorlesung
    - Scheibe
    - Platte
    - Schale

  Stab und Balken → **Linientragwerke**; Scheibe, Platte, Schale → Höhere Mechanik / ~~Flächige Strukturen~~ **Flächentragwerke**

> Skizze: Stab mit Kräften in Längsrichtung an beiden Enden (Zug, rote Doppelpfeile).

#### 3.1 Ebene Fachwerke

##### 3.1.1 Überblick

- **Stab** als Grundelement
  - → gerade Struktur
  - → Kräfte nur in Richtung der Längsachse
  - → Kräfte können nur in Gelenken übertragen werden

> Skizze: Stab mit Gelenken (grün beschriftet „Gelenk") an beiden Enden; Kräfte $F$ in Stabrichtung nach außen (links ←, rechts →).

- ein **Fachwerk** ist ein Tragwerk, welches nur aus geraden Stäben besteht, die nur in ihren Gelenken, sog. **Knoten**, miteinander verbunden sind
  - → äußere Kräfte greifen nur an Knoten an!
  - → Knoten bilden reibungsfreie Gelenke
  - → Stäbe nehmen nur Zug- und Druckkräfte auf

---

## Seite 2

**Bsp.:**

> Skizze: Ebenes Dachfachwerk (Dreiecksbinder) mit 7 Knoten I–VII und 11 Stäben 1–11. Untergurt: Knoten I (links, Festlager) – Stab 1 – III – Stab 4 – V – Stab 10 – VII (rechts, Loslager). Obergurt: I – Stab 2 – II – Stab 6 – IV (First) – Stab 8 – VI – Stab 11 – VII. Füllstäbe: 3 (II–III), 5 (III–IV), 7 (IV–V), 9 (V–VI). Lasten (rot): $F_1$ senkrecht nach unten auf Knoten IV, $F_2$ horizontal nach rechts an Knoten VI, $F_3$ senkrecht nach unten an Knoten V (Knoten V mit $F_3$ grün umrandet). Grüner Kommentar mit Pfeil auf Knoten II: „jeder Knoten ist ein Gelenk".

**Hinweis:** In der Praxis sind Knoten keine Gelenke, sondern Niet-, Schraub- oder Schweißverbindungen!

> Skizze: Links „idealisiert Gelenk": zwei Stäbe über einen Gelenkbolzen verbunden. Mitte „Nietverbindung": zwei Stäbe über ein Knotenblech mit mehreren Nieten verbunden ⇒ Momentenwirkung da wie Einspannung (Skizze eines eingespannten Stabes).

- → durch die Konstruktion des Fachwerks und der Kraftverteilung entstehen real aber kaum Momente

> Skizze: Eingespannter Stab mit Querkraft $F_1$ (≈ 0, rot „→ 0") und Längskraft $F_2$ am Ende; daneben durchgestrichene Einspannung. Darunter: Stab mit $F_2$ in Längsrichtung, am Lager „$M = 0$!".

---

## Seite 3

### Tragwerke

- **Linientragwerke** (lange, schlanke Strukturen)

**Stab**
- Kräfte nur in Richtung der Längsachse
- Kraftübertragung nur in Gelenken

> Skizze: Schräger Stab mit Gelenken an den Enden und Kräften $F$ in Stabachse; horizontaler Stab mit „Gelenk"-Beschriftung (grün) an beiden Enden und $F$ nach außen.

**Sonderfall: Seil**
- kann nur Kräfte in Zugrichtung übertragen: $F_S \geq 0$

> Skizze: Seil über eine Rolle (Kreis mit „+") mit Seilkräften $F_S$ an beiden Enden (schräg nach unten, Zug).

**Balken**
- Kräfte in Längs- und Querrichtung
- Momente werden übertragen
- gerade Struktur

> Skizze: Räumlicher Balken mit Rechteckquerschnitt; daneben Balken mit Streckenlast (rot) und an beiden Enden Normalkraft, Querkraft und Moment (rote Pfeile/Drehpfeile).

**Bogenträger**
- wie Balken mit gekrümmter Struktur

> Skizze: Gekrümmter Träger (räumlich), daneben Bogen mit Kräften und Momenten an den Enden.

---

## Seite 4

- **Flächentragwerke** (dünne flächige Strukturen)

**Scheibe**
- ebene Struktur
- Belastung nur in der Scheibenebene
- Deformation in der Ebene

> Skizze: Unregelmäßig geformte flache Scheibe; rote Flächenlast und Einzelkräfte, alle in der Scheibenebene.

**Platte**
- ebene Struktur
- beliebige Belastung
- Deformationen in der Ebene und Biegung

> Skizze: Platte mit Kraft senkrecht zur Ebene, lokaler Flächenlast und Kräften in der Ebene.

**Schale**
- gekrümmte Ebene
- beliebige Belastung
- Deformationen in Ebene und Biegung

> Skizze: Gekrümmtes Schalenstück mit Kräften senkrecht und tangential zur Fläche.

---

## Seite 5

##### 3.1.2 Statische Bestimmtheit

- Freischnitt um jeden Knoten = Knotenschnittverfahren: (aus Bsp. Knoten V)

> Skizze: Knoten V freigeschnitten: Stabkräfte $F_{S4}$ (nach links), $F_{S10}$ (nach rechts), $F_{S7}$ (nach links oben), $F_{S9}$ (nach rechts oben), äußere Last $F_3$ (nach unten). Winkel: $\alpha$ zwischen Stab 9 und der Horizontalen (rechts), $\beta$ zwischen den Stäben 7 und 9 [?], weiterer Winkel zwischen Stab 7 und Horizontaler (links). Randnotiz: „(Zugkräfte an Schnittufern!)" – alle Stabkräfte werden als Zug (vom Knoten weg) angetragen.

- ↳ zentrales, ebenes Kräftesystem
- ↳ 2 Gleichgewichtsbedingungen für jeden Knoten

Abzählkriterium: ~~$3\cdot n = a + z$~~ → $2$ (Knoten) $\cdot\,k = a + s$; $a$: Lagerreaktionen, Zwischenreaktionen (1× je Stab) → Anzahl der Stäbe

$$\boxed{2k = a + s}\quad\text{statisch bestimmt}$$

$k$ = Anzahl Knoten, $s$ = Anzahl Stäbe, $a$ = Auflagerreaktionen

↳ Im Beispiel: $k = 7$, $a = 3$, $s = 11$:
$$2\cdot 7 = 3 + 11,\qquad 14 = 14\ \checkmark$$

> Skizze: Dreieckfachwerk mit innerem Knoten (Außendreieck mit Spitze oben, Festlager links unten, Loslager rechts unten; innerer Knoten mit allen drei Ecken verbunden). Zunächst „statisch unbestimmt: $8 \neq 9$" ($k = 4$, $s = 6$, $a = 3$). Nach Streichen des unteren Gurtstabs (grünes ×): $8 = 3 + 5 = 8\ \checkmark$ statisch bestimmt.

[Prüfung: ✓. Hinweis: Das Abzählkriterium ist (wie in Teil 1, S. 34) nur notwendig; nach Entfernen des Untergurts ist das Fachwerk nur dank des Festlagers (2 Reaktionen) und Loslagers unverschieblich.]

---

## Seite 6

##### 3.1.3 Berechnungsmethoden

- **KNOTENSCHNITTVERFAHREN**
  - → Freischnitt um jeden Knoten
    - ↳ ebenes zentrales Kräftesystem
    - ⇒ Aufstellen der Gleichgewichtsbedingungen

  s. Schnitt unter 3.1.2 (Knoten V):
$$\sum F_x = 0 \;\leadsto\; -F_{S4} + F_{S10} + F_{S9}\cos\alpha - F_{S7}\cos\beta = 0$$
$$\sum F_y = 0 \;\leadsto\; -F_3 + F_{S9}\sin\alpha + F_{S7}\sin\beta = 0$$

[Prüfung: Die Gleichungen sind nur richtig, wenn $\beta$ der Winkel zwischen Stab 7 und der (linken) Horizontalen ist; in der Skizze S. 5 ist $\beta$ eher zwischen den Stäben 7 und 9 eingetragen [?].]

  ↳ es können sehr aufwendige Gleichungssysteme entstehen (→ für Computer kein Problem)

- **Nullstäbe**
  - sog. „Blindstäbe", die keine Stabkräfte aufnehmen: $F_S = 0$
    - → Vereinfachung des Rechenaufwandes mit dem Knotenschnittverfahren
  - ⇒ **SUCHEN Sie Nullstäbe!**

---

## Seite 7

- es kann Stäben die Kraft $F_S = 0$ zugeordnet werden, wenn folgende Kriterien erfüllt sind:

**① Unbelastete Ecke**
$$F_{S1} = F_{S2} = 0\ \checkmark$$
> Skizze: Knoten mit zwei nicht kollinearen Stäben (einer schräg, einer senkrecht), keine äußere Last; Stabkräfte $F_{S1}$, $F_{S2}$; beide Stäbe als „Nullstäbe" beschriftet.

(Prüfe über Gleichgewichtsbedingung)

**② Belastete Ecke, mit einem Stab in Richtung der angreifenden Last**
> Skizze: Knoten mit zwei Stäben; Last $F$ wirkt in Richtung von Stab 2 (schräg); Stab 1 (horizontal) = Nullstab.

$$F_{S1} = 0,\qquad F_{S2} = F\qquad(\text{Prüfe über Gleichgewichtsbedingung})$$

**③ Knoten mit 3 Stäben ohne äußere Last und zwei Stäben in gleicher Richtung**
> Skizze: Knoten mit zwei kollinearen Stäben ($F_{S1}$ nach rechts oben, $F_{S2}$ nach links unten) und einem dritten Stab ($F_{S3}$, horizontal) = Nullstab.

$$F_{S1} = F_{S2},\qquad F_{S3} = 0\qquad(\text{Prüfe über Gleichgewichtsbedingung})$$

**WICHTIG:** OBWOHL NULLSTÄBE KEINE KRÄFTE AUFNEHMEN, DÜRFEN SIE NICHT AUS DER KONSTRUKTION ENTFERNT WERDEN!
→ Aufgaben in Stabilität und statischer Bestimmtheit

---

## Seite 8

**Beispiel: Pultdach** [?] (Lesung des Wortes unsicher, evtl. „Rampendach")

> Skizze: Fachwerk-Kragdach an einer Wand. Knoten V (oben links, Wandlager: Festlager), Knoten IV (unten links, Wandlager: Loslager mit horizontaler Reaktion), Knoten III (Obergurt, Mitte), Knoten II (Untergurt, Mitte), Knoten I (rechte Spitze). Stäbe: 1 (I–II), 2 (I–III), 3 (II–III, senkrecht), 4 (II–IV), 5 (III–IV, schräg), 6 (III–V), 7 (IV–V, senkrecht). Winkel $\alpha$ (grün): zwischen Stab 1 und 2 bei I, zwischen Stab 6 und Horizontaler sowie Stab 5 und Horizontaler bei III, zwischen Stab 4 und 5 bei IV. Lasten (rot): $F$ auf V, $2F$ auf III, $F$ auf I (alle senkrecht nach unten).

geg.: Dach- und Schneelast verteilt → Resultierende auf Knoten
ges.: Stabkräfte, Lagerreaktionen

**Lös.:**

> Skizze: Fachwerk mit grün umkreisten Knotenschnitten I–V; Lagerreaktionen $F_{AH}$ (→) und $F_{AV}$ (↑) an V, $F_B$ (→) an IV.

Nullstäbe? **S3!** $F_{S3} = 0$ (Fall ③ an Knoten II)

**Knoten I:**

> Skizze: Knoten I mit $F$ (↓), $F_{S1}$ (← entlang Stab 1), $F_{S2}$ (nach links oben entlang Stab 2), Winkel $\alpha$.

$$\to:\quad -F_{S1} - F_{S2}\cos\alpha = 0\quad (1)$$
$$\uparrow:\quad -F + F_{S2}\sin\alpha = 0\quad (2)\;\to\; \underline{F_{S2} = \frac{F}{\sin\alpha}}$$
in (1):
$$\underline{F_{S1} = -F\,\frac{\cos\alpha}{\sin\alpha}}$$

---

## Seite 9

**Knoten II:**

> Skizze: Knoten II mit $F_{S4}$ (←), $F_{S1}$ (→), $F_{S3}$ (↑, „→ 0").

$$\to:\quad -F_{S4} + F_{S1} = 0 \;\to\; F_{S1} = F_{S4},\qquad \underline{F_{S4} = -F\,\frac{\cos\alpha}{\sin\alpha}}$$
$$(\uparrow:\quad F_{S3} = 0\ \checkmark)$$

**Knoten III:**

> Skizze: Knoten III mit $2F$ (↓), $F_{S6}$ (nach links oben), $F_{S2}$ (nach rechts unten), $F_{S5}$ (nach links unten), $F_{S3}$ (↓, durchgestrichen, „0"); Winkel $\alpha$ an Stab 6 und Stab 5.

$$\to:\quad -F_{S6}\cos\alpha - F_{S5}\cos\alpha + F_{S2}\cos\alpha = 0\quad (3)$$
$$\uparrow:\quad F_{S6}\sin\alpha \mp F_{S5}\sin\alpha - 2F - F_{S2}\sin\alpha = 0\quad (4)$$

(Bei $F_{S5}$ ist das Vorzeichen im Original überschrieben; gerechnet wird mit $-F_{S5}\sin\alpha$, was zur Geometrie passt.)

(3) mit $F_{S2} = F/\sin\alpha$, durch $\cos\alpha$ gekürzt:
$$-F_{S6} - F_{S5} + \frac{F}{\sin\alpha} = 0 \;\Rightarrow\; F_{S6} = -F_{S5} + \frac{F}{\sin\alpha}$$
↳ in (4):
$$\left(-F_{S5} + \frac{F}{\sin\alpha}\right)\sin\alpha - F_{S5}\sin\alpha - 2F - F = 0$$
$$-2F_{S5}\sin\alpha + F - 2F - F = 0 \;\Rightarrow\; \underline{F_{S5} = -\frac{F}{\sin\alpha}}$$
↳
$$\underline{F_{S6} = \frac{2F}{\sin\alpha}}$$

---

## Seite 10

**Knoten IV:**

> Skizze: Knoten IV mit $F_{S7}$ (↑), $F_{S5}$ (nach rechts oben, Winkel $\alpha$), $F_{S4}$ (→), Lagerkraft $F_B$ (→).

$$\to:\quad F_B + F_{S4} + F_{S5}\cos\alpha = 0\quad (5)$$
$$\uparrow:\quad F_{S7} + F_{S5}\sin\alpha = 0\quad (6)$$

aus (5):
$$F_B + \left(-F\frac{\cos\alpha}{\sin\alpha}\right) + \left(-F\frac{\cos\alpha}{\sin\alpha}\right) = 0 \;\Rightarrow\; \underline{F_B = 2F\,\frac{\cos\alpha}{\sin\alpha}}$$

aus (6):
$$F_{S7} + \left(-\frac{F}{\sin\alpha}\sin\alpha\right) = 0 \;\Rightarrow\; \underline{F_{S7} = F}$$

**Knoten V:**

> Skizze: Knoten V mit $F$ (↓), $F_{AH}$ (→), $F_{AV}$ (↑), $F_{S7}$ (↓, Richtung Knoten IV), $F_{S6}$ (nach rechts unten, Winkel $\alpha$).

$$\to:\quad F_{AH} + F_{S6}\cos\alpha = 0\quad (7)$$
$$\uparrow:\quad -F + F_{AV} - F_{S7} - F_{S6}\sin\alpha = 0\quad (8)$$

aus (7):
$$\underline{F_{AH} = -F_{S6}\cos\alpha = -2F\,\frac{\cos\alpha}{\sin\alpha}}$$

---

## Seite 11

aus (8):
$$F_{AV} - F - F - 2F\,\frac{\sin\alpha}{\sin\alpha} = 0 \;\Rightarrow\; \underline{F_{AV} = 4F}$$

**Alternative für Lagerkräfte:**
- ohne Stabkräfte, direkt über Gleichgewichtsbedingungen

> Skizze: Gesamtfachwerk freigeschnitten; $A$ (oben links) mit $F$ (↓), $F_{AH}$ (→), $F_{AV}$ (↑); $B$ (unten links) mit $F_B$ (→); $2F$ in der Mitte, $F$ an der Spitze. Bemaßung: Höhe $A$–$B$ = $2\tan\alpha\cdot L$, horizontal $L$ + $L$ (grün).

$$\sum F_x = 0 \;\leadsto\; F_{AH} + F_B = 0\quad (1)$$
$$\sum F_y = 0 \;\leadsto\; -F + F_{AV} - 2F - F = 0\quad (2)$$
$$\sum M\big|_A = 0 \;\leadsto\; -F_B\cdot 2L\tan\alpha + 2F\cdot L + F\cdot 2L = 0\quad (3)$$

aus (3):
$$\underline{F_B = \frac{1}{2\tan\alpha}(2F + 2F) = \frac{4F}{2\tan\alpha} = 2F\,\frac{\cos\alpha}{\sin\alpha}}\ \checkmark$$
aus (2): $\underline{F_{AV} = 4F}\ \checkmark$
aus (1): $\underline{F_{AH} = -F_B = -2F\,\frac{\cos\alpha}{\sin\alpha}}\ \checkmark$

[Prüfung (numerisch mit $\alpha = 30°$, Gleichungssystem aller Knoten): $F_{S1} = F_{S4} = -1{,}732F$, $F_{S2} = 2F$, $F_{S3} = 0$, $F_{S5} = -2F$, $F_{S6} = 4F$, $F_{S7} = F$, $F_{AH} = -3{,}464F$, $F_{AV} = 4F$, $F_B = 3{,}464F$ – stimmt mit allen allgemeinen Ergebnissen überein ✓. Druckstäbe: 1, 4, 5; Zugstäbe: 2, 6, 7.]

---

## Seite 12

- **Rittersches Schnittverfahren** (nach A. Ritter, 1826–1908)
  - → Berechnung weniger Stabkräfte eines größeren Fachwerks
  - → wenn ein Fachwerk durch einen Schnitt, der genau 3 Stäbe schneidet, in zwei Teilsysteme teilbar ist, können die Stabkräfte der geschnittenen Stäbe berechnet werden
  - Bedingungen:
    - 3 geschnittene Stäbe nicht alle parallel und Wirkungslinien treffen sich nicht in einem Punkt/Knoten
    - für mindestens eines der Teilsysteme müssen alle äußeren Kräfte bekannt sein

⇒ Nutzung der 3 Gleichgewichtsbedingungen des ebenen Kräftesystems ($F_x$, $F_y$, $M$)

---

## Seite 13

**Bsp.: Pultdach [?] (again)** – Rittersches Schnittverfahren

> Skizze: Fachwerk von S. 8 (Knoten I–V, Stäbe 1–7, Lasten $F$, $2F$, $F$, Wandlager links an V und IV). Grüner Ritterschnitt durch die Stäbe 6, 5 und 4; er umschließt den rechten Teil (Knoten III, II, I mit den Stäben 1, 2, 3). Winkel $\alpha$ an III (Stab 6 und Stab 5 zur Horizontalen), an IV (Stab 5) und an I.

> Skizze: Teilsystem I (links): Knoten V mit $F$ (↓), $F_{AH}$ (→), $F_{AV}$ (↑), Stabkraft $F_{S6}$ (nach rechts unten); Knoten IV mit $F_B$ (→), $F_{S5}$ (nach rechts oben), $F_{S4}$ (→).
> Teilsystem II (rechts): Knoten III mit $2F$ (↓), $F_{S6}$ (nach links oben), $F_{S5}$ (nach links unten); Knoten II mit $F_{S4}$ (←); Knoten I mit $F$ (↓). Bemaßung $L$ (II–I). Hilfsdreieck: Hebelarm $b$ von I auf die Wirkungslinie von Stab 5, Winkel $\beta$ bei III, Hypotenuse $a$.

Teilsystem II:
$$\to:\quad -F_{S6}\cos\alpha - F_{S5}\cos\alpha - F_{S4} = 0\quad (1)$$
$$\uparrow:\quad F_{S6}\sin\alpha - 2F - F_{S5}\sin\alpha - F = 0\quad (2)$$
$$\curvearrowleft_{III}:\quad -F\cdot L - F_{S4}\cdot L\tan\alpha = 0\quad (3)$$

aus (3): $\checkmark\ \underline{F_{S4} = -\dfrac{F}{\tan\alpha} = -F\dfrac{\cos\alpha}{\sin\alpha}}$

weiter mit (1) und (2) …

**alternativ** (nur Momentengleichungen):
- $\curvearrowleft_{III}$: $F_{S4} = -F\dfrac{\cos\alpha}{\sin\alpha}$
- $\curvearrowleft_{I}$: $2F\cdot L + F_{S5}\cdot 2L\sin\alpha = 0 \;\Rightarrow\; \underline{F_{S5} = -\dfrac{F}{\sin\alpha}}\ \checkmark$

Nebenrechnung (grün): $\beta = 180° - (180° - 2\alpha) = 2\alpha$; $\sin\beta = b/a$, $b = \sin\beta\cdot a = 2\sin\alpha\cos\alpha\cdot\dfrac{L}{\cos\alpha} = 2L\sin\alpha$.

---

## Seite 14

$$\curvearrowleft_{IV}:\quad -2F\cdot L - F\cdot 2L + F_{S6}\cdot 2L\sin\alpha = 0$$

> Skizze: Geometrie zum Hebelarm: Knoten IV mit Winkel $\alpha$, Strecke $c$ entlang Stab 5 bis III, senkrechter Abstand $d$ von IV auf die Wirkungslinie von Stab 6; Winkel $2\alpha$ bei III; horizontale Länge $L$.

$$c = \frac{L}{\cos\alpha},\qquad d = c\sin 2\alpha = \frac{L}{\cos\alpha}\,2\sin\alpha\cos\alpha,\qquad d = 2L\sin\alpha$$

$$F_{S6}\cdot 2L\sin\alpha = 4F \cdot L\;\Rightarrow\; \underline{F_{S6} = \frac{2F}{\sin\alpha}}\ \checkmark$$

(Im Original „$F_{S6}\,2L\sin\alpha = 4F$" – $L$ beidseitig gekürzt.)

↳ Nutzung von 3 Momentenbilanzen anstatt 2× Kräftebilanz + 1× Momentenbilanz: **direkter!**

[Prüfung: Alle drei Ritter-Ergebnisse stimmen mit dem Knotenschnittverfahren (S. 9–11) überein ✓.]

---

## Seite 15

**Beispiel: Fahrrad**

> Skizze: Fahrrad; Rahmen als Fachwerk idealisiert.
> Fachwerkmodell: Knoten IV (vorne oben, Steuerrohr; Lager $A$ = Loslager, vertikal), Knoten II (oben Mitte, Sattel), Knoten III (unten Mitte, Tretlager; im Original ebenfalls mit „II" beschriftet [?]), Knoten I (hinten, Hinterachse; Lager $B$ = Festlager). Stäbe: 5 (IV–II, Oberrohr), 4 (IV–III, Unterrohr), 3 (II–III, Sattelrohr), 1 (II–I, Sitzstrebe), 2 (III–I, Kettenstrebe). Lasten: $F$ (↓) an II, $F/10$ an IV schräg unter $45°$ (nach links unten, Lenkerkraft).

ges.: Lagerkräfte, Stabkräfte

**Lös.:**

> Skizze: Knotenschnitte (grün umrandet) um IV (mit $F/10$, $F_A$ ↑), II (mit $F$), III, I (mit $F_{BV}$ ← horizontal und $F_{BH}$ ↑ vertikal).

$$2k = a + s:\quad \sout{2\cdot 5 = 3 + 6,\ 10 \neq 9}\;\to\; 2\cdot 4 = 3 + 5,\quad 8 = 8$$

[Prüfung: Bezeichnung im Original vertauscht: $F_{BV}$ ist als **horizontale**, $F_{BH}$ als **vertikale** Lagerkraft eingezeichnet und so auch in den Gleichungen verwendet.]

> Skizze (grün, Geometrie): Winkel $\beta$ an IV (zwischen Stab 5 und 4), Winkel $\alpha$ an I (zwischen Stab 2 und 1); horizontale Abstände $a$ (IV bis III) und $b$ (III bis I), Höhe $c$.

**Knoten I:**

> Skizze: $F_{S1}$ (nach links oben, Winkel $\alpha$), $F_{S2}$ (←), $F_{BV}$ (←), $F_{BH}$ (↑).

$$\to:\quad -F_{S2} - F_{BV} - F_{S1}\cos\alpha = 0\quad (1)$$
$$\uparrow:\quad F_{BH} + F_{S1}\sin\alpha = 0\quad (2)$$

**Knoten IV:**

> Skizze: $F/10$ (nach links unten, $45°$), $F_A$ (↑), $F_{S5}$ (→), $F_{S4}$ (nach rechts unten, Winkel $\beta$).

$$\to:\quad -\frac{F}{10}\cos 45° + F_{S5} + F_{S4}\cos\beta = 0$$
$$\uparrow:\quad F_A - \frac{F}{10}\sin 45° - F_{S4}\sin\beta = 0$$

---

## Seite 16

**o. Lagerbedingungen** (Gleichgewicht am Gesamtsystem)

$$\to:\quad -\frac{F}{10}\cos 45° - F_{BV} = 0 \;\Rightarrow\; \underline{F_{BV} = -\frac{F}{10}\,\frac12\sqrt2}$$
$$\uparrow:\quad F_A - \frac{F}{10}\sin 45° - F + F_{BH} = 0$$
$$\curvearrowleft_B:\quad F_A(a+b) - F\cdot b - \frac{F}{10}(a+b)\sin 45° = 0$$
$$\underline{F_A = \frac{F\cdot b}{a+b} + \frac{F}{10}\,\frac12\sqrt2}$$
$$F_{BH} = F\left(1 + \frac1{10}\,\frac12\sqrt2\right) - \frac{F\cdot b}{a+b} - \frac{F}{10}\,\frac12\sqrt2,\qquad \underline{F_{BH} = F\left(1 - \frac{b}{a+b}\right)}$$

[Prüfung: **Fehler im Original** – in der Momentengleichung um $B$ fehlt das Moment der Horizontalkomponente $\frac{F}{10}\cos 45°$, die an IV in der Höhe $c$ über $B$ angreift. Mit $F/10$ nach links unten lautet sie korrekt $F_A(a+b) - F b - \frac{F}{10}\frac{\sqrt2}{2}(a+b) - \frac{F}{10}\frac{\sqrt2}{2}c = 0$, also $F_A = \frac{Fb}{a+b} + \frac{F}{10}\frac{\sqrt2}{2}\left(1 + \frac{c}{a+b}\right)$ und $F_{BH} = F\frac{a}{a+b} - \frac{F}{10}\frac{\sqrt2}{2}\,\frac{c}{a+b}$. Die Ergebnisse des Originals gelten nur für $c = 0$. Stabkräfte werden im Original nicht mehr ausgerechnet.]

---

## Seite 17

**Beispiel** (rot: „Übung 6") – Rittersches Schnittverfahren

> Skizze: Fachwerk mit Knoten I–V. KOS gedacht mit Ursprung in IV: IV $(0,0)$, II $(2a,\,3a)$, I $(8a,\,3a)$, III $(4a,\,0)$, V $(0,\,-8a)$. Stäbe: 1 (II–I, horizontal, $6a$), 2 (III–I), 3 (II–III), 4 (IV–II), 5 (IV–III, horizontal), 6 (III–V), 7 (IV–V, senkrecht). Lager: $A$ links an der Wand, über einen horizontalen Stab mit IV verbunden (horizontale Reaktion); $B$ unter V. Last $F$ (↓) an I. Bemaßung (grün): $2a$, $6a$ (horizontal oben), $3a$ (Höhe I über III), $4a$ (IV–III), $8a$ (Höhe IV über V). Grüner Ritterschnitt durch die Stäbe 4, 5, 6, umschließt Knoten I, II, III.

geg.: $F = 20\,\mathrm{kN}$, $a = 50\,\mathrm{cm}$
ges.: $F_{S4}$, $F_{S5}$, $F_{S6}$

**Lös.:**

> Skizze: Abgeschnittenes Teilsystem (Knoten II, I, III mit Stäben 1, 2, 3); Stabkräfte $F_{S4}$ (an II, Richtung IV), $F_{S5}$ (an III, ←), $F_{S6}$ (an III, Richtung V), Last $F$ an I.

Nebenrechnung: $\tan\alpha = \dfrac{3a}{2a} = \dfrac32$; Hebelarm von $F_{S4}$ um III: $x = \sin\alpha\cdot 4a$.

$$\curvearrowleft_{III}:\quad F\cdot 4a - F_{S4}\sin\left(\arctan\tfrac32\right)\cdot 4a = 0 \;\Rightarrow\; F_{S4} = \frac{F}{\sin(\arctan\frac32)},\qquad \underline{F_{S4} = 24{,}04\,\mathrm{kN}}$$

Nebenrechnung: Dreieck mit Katheten $4a$, $8a$: $\beta = \arctan\left(\dfrac{4a}{8a}\right)$, Hebelarm $x = \sin\beta\cdot 8a$.

$$\curvearrowleft_{IV}:\quad F\cdot 8a + F_{S6}\cdot 8a\,\sin\left(\arctan\tfrac12\right) = 0 \;\Rightarrow\; F_{S6} = -\frac{F}{\sin(\arctan\frac12)} = \underline{-44{,}7\,\mathrm{kN}}$$

$$\to:\quad -F_{S4}\cos\alpha - F_{S6}\sin\beta - F_{S5} = 0$$
$$F_{S5} = -\left(F_{S4}\cos(\arctan\tfrac32) + F_{S6}\sin(\arctan\tfrac12)\right) = \underline{6{,}65\,\mathrm{kN}}$$

[Prüfung (lineares Gleichungssystem mit obigen Koordinaten): $F_{S4} = 24{,}04\,\mathrm{kN}$ (Zug) ✓, $F_{S6} = -44{,}72\,\mathrm{kN}$ (Druck) ✓, $F_{S5} = 6{,}67\,\mathrm{kN}$ (Zug) – im Original $6{,}65\,\mathrm{kN}$, Rundungsabweichung durch gerundete Zwischenwerte. $a = 50\,\mathrm{cm}$ wird für die Kräfte nicht benötigt.]

---

## Didaktische Gliederung

**Reihenfolge der Themen**
1. Tragwerke: Definition und Kategorien (Stab/Seil, Balken → Linientragwerke; Scheibe, Platte, Schale → Flächentragwerke) (S. 1, 3–4)
2. Ebene Fachwerke – Überblick: Stab als Grundelement, Definition Fachwerk/Knoten, Idealisierungen (Lasten nur in Knoten, reibungsfreie Gelenke, nur Zug/Druck); Praxis: Niet-/Schraub-/Schweißknoten erzeugen kaum Momente (S. 1–2)
3. Statische Bestimmtheit von Fachwerken: Knotenfreischnitt, Abzählkriterium $2k = a + s$ (S. 5)
4. Berechnungsmethoden: Knotenschnittverfahren (S. 6), Nullstäbe (3 Regeln) (S. 6–7)
5. Beispiel Pultdach mit Knotenschnittverfahren und Kontrolle über Gesamtgleichgewicht (S. 8–11)
6. Rittersches Schnittverfahren: Voraussetzungen, Pultdach erneut (Kräfte- bzw. reine Momentenbilanzen) (S. 12–14)
7. Anwendungsbeispiele: Fahrradrahmen (S. 15–16), Übung 6 (Ritterschnitt) (S. 17)

**Definitionen**
- Tragwerk: Teile einer Konstruktion, die Kräfte aufnehmen und ableiten (S. 1)
- Stab: gerade, Kräfte nur in Längsachse, Kraftübertragung nur in Gelenken; Seil: nur Zug, $F_S \ge 0$ (S. 1, 3)
- Balken: Längs-, Querkräfte und Momente; Bogenträger: gekrümmter Balken (S. 3)
- Scheibe (Last in Ebene), Platte (beliebige Last, Biegung), Schale (gekrümmt) (S. 4)
- Fachwerk: nur gerade Stäbe, nur in Knoten (reibungsfreie Gelenke) verbunden, äußere Lasten nur an Knoten (S. 1)
- Nullstab (Blindstab): $F_S = 0$, darf trotzdem nicht entfernt werden (Stabilität, statische Bestimmtheit) (S. 6–7)

**Rechenschemata**
- Abzählkriterium Fachwerk: $2k = a + s$ (notwendig, nicht hinreichend) (S. 5)
- Knotenschnittverfahren: Nullstäbe suchen → Stabkräfte als Zug (vom Knoten weg) antragen → an Knoten mit ≤ 2 Unbekannten beginnen → $\sum F_x = 0$, $\sum F_y = 0$ je Knoten → negatives Ergebnis = Druckstab; Lagerkräfte zur Kontrolle am Gesamtsystem (S. 6, 8–11)
- Nullstabregeln: ① unbelasteter Knoten mit 2 nicht kollinearen Stäben → beide 0; ② belasteter Zweistabknoten, Last in Richtung eines Stabes → anderer Stab 0; ③ unbelasteter Dreistabknoten mit 2 kollinearen Stäben → dritter Stab 0 (S. 7)
- Ritterschnitt: Schnitt durch genau 3 Stäbe (nicht alle parallel, nicht durch einen Punkt), Teilsystem mit bekannten äußeren Lasten wählen, Momentenbilanzen um die Schnittpunkte je zweier geschnittener Stäbe (Ritterpunkte) → jede Gleichung liefert direkt eine Stabkraft (S. 12–14, 17)

---

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| 1 | Dachbinder (7 Knoten, 11 Stäbe) – Abzählkriterium | $k = 7$, $a = 3$, $s = 11$ | $14 = 14$, statisch bestimmt | 2, 5 |
| 2 | Dreieckfachwerk mit Innenknoten | $k = 4$, $s = 6$ bzw. 5, $a = 3$ | $8 \ne 9$ (unbestimmt) → nach Entfernen eines Stabs $8 = 8$ | 5 |
| 3 | Pultdach, Knotenschnittverfahren | Lasten $F$, $2F$, $F$; Winkel $\alpha$; Länge $L$ | $F_{S1} = F_{S4} = -F\cot\alpha$, $F_{S2} = F/\sin\alpha$, $F_{S3} = 0$, $F_{S5} = -F/\sin\alpha$, $F_{S6} = 2F/\sin\alpha$, $F_{S7} = F$, $F_B = 2F\cot\alpha$, $F_{AH} = -2F\cot\alpha$, $F_{AV} = 4F$ | 8–11 |
| 4 | Pultdach, Ritterschnitt durch 4, 5, 6 | wie Nr. 3 | $F_{S4} = -F\cot\alpha$, $F_{S5} = -F/\sin\alpha$, $F_{S6} = 2F/\sin\alpha$ (Hebelarm $2L\sin\alpha$) | 13–14 |
| 5 | Fahrradrahmen (4 Knoten, 5 Stäbe) | $F$ (Sattel), $F/10$ unter $45°$ (Lenker), Abstände $a$, $b$, $c$ | $F_{BV}$ (horiz.) $= -\frac{\sqrt2}{20}F$; $F_A = \frac{Fb}{a+b} + \frac{\sqrt2}{20}F$, $F_{BH}$ (vert.) $= F\frac{a}{a+b}$ – Momententerm mit $c$ fehlt im Original; Stabkräfte nur angesetzt | 15–16 |
| 6 | Übung 6, Ritterschnitt | $F = 20\,\mathrm{kN}$, $a = 50\,\mathrm{cm}$, Geometrie in $a$ | $F_{S4} = 24{,}04\,\mathrm{kN}$, $F_{S5} = 6{,}65\,\mathrm{kN}$ (exakt 6,67), $F_{S6} = -44{,}7\,\mathrm{kN}$ | 17 |

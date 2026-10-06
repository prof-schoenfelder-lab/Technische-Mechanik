# Technische Mechanik – II. Elastostatik (Festigkeitslehre) (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen
Quelle: `Quellen/Vorlesung-2013/6-Festigkeitslehre.pdf` (21 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten/Spannungen, Grün = Bemaßungen, Hervorhebungen, Kommentare.
- Durchgestrichene Passagen werden nur erwähnt, wenn sie inhaltlich relevant sind.
- Unsichere Lesungen sind mit [?] markiert, Anmerkungen der Transkription mit [Prüfung: ...].

---

## Seite 1

# II. Elastostatik (Festigkeitslehre)

bisher: – starrer Körper (Stereostatik)

> Skizze: Einfeldträger auf zwei Lagern (links Festlager, rechts Loslager), in Feldmitte Einzellast $F$ (rot, ↓). Pfeil → zur Momentenlinie: dreieckförmige $M$-Fläche (rot schraffiert, Vorzeichen $\oplus$), Spitze unter der Last mit Beschriftung $M_{max}$; rot umkreist „M".

- Schnittgröße zum Auffinden maximaler Belastungen (materialunabhängig!)
- $\Rightarrow$ Auswirkungen der Belastung im Körper?
  - grüner Randvermerk: „Festigkeit, Verformung?"
  - $\Rightarrow$ Aufgabe der Annahme des starren Körpers! (rot unterstrichen)

## 1. Grundlagen der Elastostatik

### 1.1 Einleitung

Die Elastostatik untersucht die inneren Kräfte im Bauteil und die daraus resultierenden Beanspruchungen und Verformungen.

$\Rightarrow$ Dimensionierung von Bauteilen
- bezüglich Festigkeit

$$\boxed{\text{Bauteilbeanspruchung} \le \text{zulässige Beanspruchung}}$$
(zulässige Beanspruchung: Materialkennwerte)

---

## Seite 2

- bezüglich Steifigkeit: Verformung des Bauteils innerhalb bestimmter Grenzwerte? (grün)

> **Zielstellung** (grün umrahmt): Entwicklung von Konstruktionen mit minimalem Materialaufwand unter Gewährleistung der erforderlichen Sicherheit.

### 1.2 Voraussetzungen / Annahmen

(A) Vorstellung des starren Körpers wird aufgegeben.

> Skizze: Einfeldträger (Fest- und Loslager) mit Einzellast $F$ in der Mitte, einmal unverformt (starr), $\Rightarrow$ einmal mit nach unten durchgebogener Achse.

(B) Verformungen am Bauteil sind klein gegenüber seinen Abmessungen.

> Skizze: Links ein Balken (blau) mit leicht verformter Kontur (grün), rot abgehakt ✓. Rechts ein Balken mit sehr großer, halbkreisförmiger Durchbiegung (grün), rot durchgestrichen ✗.

(C) Die Gleichgewichtsbedingungen werden in der Regel am unverformten Bauteil aufgestellt.
- grün: „Gleichgewichtsbedingungen gelten auch hier, genauso wie in der Stereostatik!"

---

## Seite 3

(D) Das Material (der Werkstoff) sei **isotrop** (gleiche physikalische Eigenschaften in jeder Richtung)
- z. B. Gummi – isotrop; Holz – anisotrop (Faserrichtung)

und **homogen** (gleiche physikalische Eigenschaften an jedem Ort)
- z. B. Ast in Holz ist inhomogen

> Skizze: Holzstück mit Faserlinien und einem Ast (Punkt), um den die Fasern herumlaufen.

### 1.3 Beanspruchungsarten

1. Zug- / Druckbeanspruchungen
   > Skizze: Stab mit zwei nach außen zeigenden Kräften $F$ (Zug); Stab mit zwei nach innen zeigenden Kräften $F$ (Druck).
2. Biegebeanspruchungen
   > Skizze: Stab mit Endmomenten $M$ (Drehpfeile an beiden Enden), grün die durchgebogene Form.
3. Torsionsbeanspruchung
   > Skizze: Stab mit Momentenvektoren $M$ (Doppelpfeile in Stabachse) an beiden Enden, entgegengesetzt gerichtet.

---

## Seite 4

4. Scher- bzw. Schubbeanspruchung
   > Skizze: Bolzen-/Nietverbindung: Mittellasche mit Kraft $F$ nach rechts, zwei Außenlaschen mit je $F/2$ nach links (schraffiert). Bolzen senkrecht durch alle drei Bleche; Scherfugen rot markiert. Grün herausvergrößert: Bolzenelement (Rechteck) mit gegengerichteten Schubkräften oben (←) und unten (→).
5. Knickung
   > Skizze: Druckstab mit $F$ an beiden Enden (nach innen), gestrichelt die seitlich ausgeknickte Form.

### 1.4 Wichtige Größen der Elastostatik

Begriffe:
- **Spannungen** $\sigma$ [sigma] $\to$ auf Flächenelemente bezogene innere Kräfte (Kräfte, Momente)
- **Verzerrungen** $\varepsilon$ [epsilon] $\to$ relative Längen- und Winkeländerungen (Verformungen)

$\to$ Spannungen können als Funktion der Verzerrungen angegeben werden und umgekehrt:
$$\sigma = f(\varepsilon), \qquad \varepsilon = f(\sigma)$$

---

## Seite 5

Dieser Zusammenhang wird als **Materialgesetz** bezeichnet.

$\to$ In dieser Lehrveranstaltung werden die Abhängigkeiten zwischen Spannung und Verzerrungen linear angenommen!

> Skizze: Zwei Diagramme: $\sigma$ über $\varepsilon$ (Gerade durch Ursprung) und $\varepsilon$ über $\sigma$ (Gerade durch Ursprung).

## 2. Zug und Druck in Stäben

### 2.1 Spannungen im Stab

Stab:
- eine Abmessung (Länge) ist viel größer als die anderen beiden (Querschnitt)
- Belastung nur in Stabrichtung $\to$ **Normalkraft**
- Verbindungslinie der Schwerpunkte seiner Querschnittsflächen heißt **Stabachse**

> Skizze: Räumlicher Stab mit Querschnitt, Schwerpunkt $S$ eingezeichnet; grün gestrichelt die Stabachse durch die Schwerpunkte (Pfeil auf „Stabachse").

---

## Seite 6

- Betrachtung eines geraden Stabes unter Zugbelastung

> Skizze: Stab mit Zugkräften $F$ an beiden Enden (← links, → rechts). Grün gestrichelt ein Schnitt quer durch den Stab, beschriftet „Schnitt"; linker Teil grün hervorgehoben.

Allgemein: Die äußere Belastung verursacht innere Kräfte (Schnittprinzip!)

> Skizze: Beide Teilstäbe freigeschnitten: links $F$ (←) und am Schnittufer $N$ (→); rechts $N$ (←) am Schnittufer und $F$ (→).

genaue Betrachtung: $N$ wird über den kompletten Querschnitt $A$ übertragen $\Rightarrow$ $N$ „verteilt sich" über $A$.

> Skizze: Dieselben Teilstäbe, am Schnittufer jeweils mehrere parallele rote Pfeile (gleichmäßig verteilte Spannung $\sigma$).

$$\sigma = \frac{N}{A} \quad \hat{=}\ \frac{\text{Kraft}}{\text{Fläche}}$$

mit $N = F$ kann man schreiben:
$$\boxed{\sigma = \frac{F}{A}}$$

$\to$ bei veränderlicher Querschnittsfläche $A = A(x)$ und/oder veränderlicher Normalkraft gilt:
$$\boxed{\sigma(x) = \frac{N(x)}{A(x)}}$$

---

## Seite 7

**Bsp. ①**

> Skizze: Stab mit veränderlichem Querschnitt $A(x)$ (in der Mitte taillenförmig eingeschnürt), Zugkräfte $F$ an beiden Enden (← links, → rechts). Zwei markierte Stellen: $x_1$ am dicken linken Ende mit $A(x_1)$, $x_2$ an der engsten Stelle mit $A(x_2)$.

$A(x_1) > A(x_2)$, $\quad N = F = \text{const.}$ (Statik)

$$\sigma(x) = \frac{F}{A(x)} \quad\Rightarrow\quad \boxed{\sigma(x_1) < \sigma(x_2)}$$

**Bsp. ②** hängender Stab unter Eigengewicht

> Skizze: Senkrechter Stab, oben gelenkig aufgehängt („hängend"), oben Kraft $F_1$ (↑), unten Kraft $F_2$ (↓). Erdbeschleunigung $\vec g$ (↓, rot). Koordinate $x$ (grün) vom oberen Ende nach unten. Im Stab mehrere kleine rote Pfeile ↓ (Eigengewicht), Normalkraft $N(x)$ markiert; grün: $A = \text{const}$.

$$\sigma(x) = \frac{N(x)}{A}$$

$N(x_1) > N(x_2)$, wenn Stab steht [?] (gemeint: hängt; Pfeil von $N(x_2)$ zu „wenn Stab steht" [?])
$\Rightarrow\ \sigma(x_1) > \sigma(x_2)$

- [Prüfung: Im Original war zunächst „$<$" geschrieben und durchgestrichen, rot zu „$>$" korrigiert. Die Korrektur ist richtig: Bei $x$ von oben nach unten und $x_1 < x_2$ trägt der obere Querschnitt zusätzlich das Gewicht des Stababschnitts zwischen $x_1$ und $x_2$, also $N(x_1) = N(x_2) + \rho g A (x_2 - x_1) > N(x_2)$.]

---

- **Zerlegung der allgemeinen Spannung**

> Skizze: Stab, links Kraft $F$ (←), rechtes Ende schräg abgeschnitten (Schnittfläche unter Winkel $\alpha$), an der Schnittfläche horizontale rote Pfeile $\sigma$.

- Schnittfläche unter Winkel $\alpha$

> Skizze (↓): Vergrößerung der schrägen Schnittfläche mit Spannungspfeilen $\sigma$; Element mit Zerlegung; rotes Kräftedreieck: Hypotenuse $\sigma$, Komponente $\sigma^*$ senkrecht zur Fläche, Komponente $\tau$ parallel zur Fläche.

Aufteilung von $\sigma$ in
- $\sigma^*$ – normal zur Fläche
- $\tau$ – parallel zur Fläche

---

## Seite 8

$\sigma^*$ … **Normalspannung**

> Skizze: Rechteckelement, links eingespannt (Schraffur), am rechten Rand Pfeil $\sigma^*$ senkrecht zur Fläche (→).

$\tau$ … **Schubspannung** (Scherspannung)

> Skizze: Rechteckelement, links eingespannt, am rechten Rand Pfeil $\tau$ (↓) parallel zur Fläche; gestrichelt das schubverzerrte (abgeschrägte) Element.

---

- **Prinzip von St. Venant** (1797–1886)

$\to$ Annahme der gleichmäßigen Spannungsverteilung im Körper bei genügend großem Abstand von Lasteinleitung

> Skizze: Stab, links über ein Gelenk/einen Bolzen Kraft $F$ (←) eingeleitet; nahe der Lasteinleitung ungleichmäßige Spannungslinien (rot, „gestörtes Spannungsfeld an Lasteinleitung!"); am rechten Ende gleichmäßig verteilte Spannung $\sigma$ = const.

---

## Seite 9

### 2.4 Kerbspannungen

(grüne Randnotiz: „$\Rightarrow$ bei Spannungen mit Prinzip von St. Venant!")

- ähnlich zu dem Problem an Lasteinleitungen besitzt die Formel $\sigma_x(x) = \dfrac{N(x)}{A(x)}$ **keine Gültigkeit** in der Nähe großer Querschnittsänderungen (Kerben, Löcher, Absätze!)
  - grün: $\to$ Spannungen sind dann ungleichmäßig über den Querschnitt verteilt

[Prüfung: Nummerierung im Original springt von 2.1 auf „2.4" (grün eingekreist); 2.2 und 2.3 folgen erst auf den Seiten 10ff.]

> Skizze: Flachstab, links Kraft $F$ (←), rechts $F$ (→). Von links nach rechts:
> – „Lasteinleitung": am linken Rand ungleichmäßige Spannungsverteilung $\sigma$ (Spitze in der Mitte);
> – „Kerbe": zwei halbkreisförmige Außenkerben (oben/unten), Restquerschnitt $A_K$ (grün bemaßt), Spannungsverteilung mit Spitzen am Kerbgrund;
> – „Bohrung": Loch in der Mitte, Restquerschnitt $A_K$ ober- und unterhalb (grün), Spannungsspitzen am Lochrand;
> – „Absatz": Übergang auf breiteren Querschnitt, Spannungsverteilung mit Spitzen an den Rändern.

Berechnung der Spannungen im Kerbbereich (Außenkerben, Bohrungen):

Nennspannung:
$$\sigma_{x,\text{mittel}} = \frac{F}{A_K}, \qquad \sigma_{x,\max} = k_t\, \sigma_{x,\text{mittel}}$$
$$\boxed{\sigma_{x,\max} = k_t \frac{F}{A_K}}$$

$k_t$ … Formzahl für Kerbgeometrie (tabelliert in Tabellenbüchern)

---

## Seite 10

> Skizze (rot): Ausschnitt eines Flachstabs mit Bohrung (Kreis); Spannungsverteilung ober- und unterhalb der Bohrung: am Lochrand Spitze $\sigma_{max}$, weiter außen abfallend; gestrichelt/schraffiert der Mittelwert $\sigma_{mittel}$.

Beispiel Bohrung: $k_t = 3$

$\Rightarrow\ \sigma_{max} = 3 \cdot \sigma_{x,\text{mittel}}$

$\Rightarrow$ An der Bohrung ist die Spannung um das 3-fache erhöht!

[Prüfung: $k_t \approx 3$ ist der klassische Wert für ein kleines Kreisloch in einer breiten Scheibe unter einachsigem Zug (Kirsch), bezogen auf die Spannung im ungeschwächten Querschnitt. Bei Bezug auf den Nettoquerschnitt $A_K$ (wie auf S. 9 definiert) und endlicher Breite ist $k_t$ kleiner als 3 – die Aussage gilt nur näherungsweise.]

(Rest der Seite leer.)

---

## Seite 11

### 2.2 Dehnungen

- Betrachtung eines Stabes mit konstantem Querschnitt

> Skizze: unbelastet: Stab der Länge $L$ (grün bemaßt), daneben $\Delta L$ markiert. belastet: gleicher Stab mit $F$ (← links, → rechts), um $\Delta L$ verlängert (schraffierter Zuwachs am rechten Ende), Gesamtlänge $L_{neu}$ (grün).

Verlängerung $\Delta L$ als Maß für die Größe der Verformung.

$\to$ relative Längenänderung:
$$\boxed{\varepsilon = \frac{\Delta L}{L}} = \frac{L_{neu} - L_{alt}}{L}$$

$\Rightarrow$ $\varepsilon$ … **Dehnung**, dimensionslos $[-]$, sehr klein ($\approx 10^{-3}$)

- $\varepsilon = \dfrac{\Delta L}{L}$ gilt nur, wenn $\varepsilon$ an jeder Stelle im Stab gleich groß ist
  $\to$ kein veränderlicher Querschnitt $A$, keine Volumenkräfte

- Herleitung für $\varepsilon$ im allgemeinen Fall:

> Skizze: unbelastet/undeformiert: Stab, Koordinate $x$ bis zum Stabelement $dx$ (schraffiert), „Stabelement $dx$, sehr klein". belastet/deformiert: derselbe Stab, linkes Ende des Elements um $u$, rechtes um $u + du$ verschoben; Länge des verformten Elements $dx + (u + du) - u$. Grün: $(u(x))$.

---

## Seite 12

$u(x)$ … Verschiebung der Querschnittsfläche an der Stelle $x$

$\to$ relative Längenänderung $\varepsilon$ am Ort $x$ für das Stabelement der Länge $dx$:
$$\varepsilon(x) = \frac{\text{neue Länge} - \text{alte Länge}}{\text{alte Länge}} = \frac{[dx + (u + du) - u] - dx}{dx} = \frac{du}{dx}$$

$$\varepsilon(x) = \frac{du(x)}{dx} \quad\Longleftrightarrow\quad u(x) = \int \varepsilon(\bar x)\, d\bar x$$

### 2.3 Zusammenhang zwischen Spannung und Dehnung – Materialgesetz

- Spannungen: Kraftgrößen – Maß für Beanspruchung des Körpers
- Dehnungen: kinematische Größen – Maß für Verformung des Körpers
- Materialgesetz: Zusammenhang zwischen Spannungen und Dehnungen

$\Rightarrow$ Experiment zur Ermittlung dieses Zusammenhangs: **Zugversuch**

---

## Seite 13

> Skizze links: Zugprobe (senkrechter Stab), oben $F$ (↑), unten $F$ (↓), grüne Schnittlinie. Daneben freigeschnittener oberer Teil: oben $F$ (↑), Koordinate $x$ (↓, grün), am Schnitt verteilte Spannung $\sigma$ (rote Pfeile ↓) und Dehnung $\varepsilon(x)$ (grün).

> Skizze rechts: Spannungs-Dehnungs-Diagramm $\sigma$ über $\varepsilon$ mit qualitativen Kurven für verschiedene Werkstoffe (von oben nach unten): hochfester Stahl, Baustahl (mit Streckgrenzen-„Zacken" und abfallendem Ast am Ende), Gusseisen, Kupfer, Leder.

- im Detail für Baustahl

> Skizze: $\sigma$-$\varepsilon$-Diagramm für Baustahl. Linearer Anstieg mit Steigungswinkel $E$ (grün) bis $\sigma_P$, darüber $\sigma_E$, dann Fließbereich mit Zacken bei $\sigma_F$, Verfestigung bis Maximum $R_m$ (roter Punkt), danach abfallend. Rote gestrichelte Linien markieren auf der $\sigma$-Achse (von unten) $\sigma_P$, $\sigma_E$, $\sigma_F$, $R_m$. Grün unter der $\varepsilon$-Achse: „elast. Bereich" (linker Abschnitt) und „plastischer Bereich" (rechter Abschnitt).

- $\sigma_P$ … Proportionalitätsgrenze
- $\sigma_E$ … Elastizitätsgrenze
- $\sigma_F$ … Streckgrenze (techn. Fließspannung)
- $R_m$ … Zugfestigkeit
- $(\sigma_E \approx \sigma_P)$

(Beschränkung in Vorlesung auf diesen Bereich [= elastischer Bereich])

Zusammenhang zwischen Dehnung und Spannung bis zur Proportionalitätsgrenze **linear**:
$$\sigma \sim \varepsilon$$

Einführung eines Proportionalitätsfaktors:
$$\frac{\sigma}{\varepsilon} = E \quad \text{… Elastizitätsmodul (E-Modul)}$$

$\Rightarrow$ ist Maß für die Steifigkeit des Materials

---

## Seite 14

$$\boxed{\sigma = E \cdot \varepsilon} \qquad [E] = \frac{\text{N}}{\text{mm}^2} = \text{MPa}$$

**Hookesches Gesetz** (Robert Hooke 1635–1703, Physiker)

bzw.
$$\varepsilon = \frac{\sigma}{E} = \frac{F}{AE}$$

| Werkstoff | E-Modul $[\text{N/mm}^2]$ |
|---|---|
| Stahl | 210.000 |
| Aluminium | 70.000 |
| Kupfer | 120.000 |
| PVC | 3.500 |
| Glas | 76.000 |
| Kohlefaser (C-Faser) | 300.000 |

**Beispiel:** Berechnung der Dehnung an der Elastizitätsgrenze (technische Elastizitätsgrenze $R_{p0,1}$)

Baustahl S235JR: $\quad R_{p0,1} = 235\ \frac{\text{N}}{\text{mm}^2} = \sigma_{F0}$ [?], $\quad E = 210.000\ \frac{\text{N}}{\text{mm}^2}$

$$\varepsilon = \frac{\sigma}{E} = \frac{\sigma_{F0}}{E} = \frac{235\ \text{N/mm}^2}{210.000\ \text{N/mm}^2} = 0{,}0011 \approx 0{,}1\,\%$$

[Prüfung: $235/210\,000 = 0{,}001119$, also $\varepsilon \approx 0{,}11\,\%$; „$0{,}1\,\%$" ist gerundet. Fachlich: Die 235 N/mm² bei S235JR sind die (obere) Streckgrenze $R_{eH}$; als technische Elastizitätsgrenze gilt üblicherweise $R_{p0,01}$, als Ersatzstreckgrenze $R_{p0,2}$. Die Bezeichnung „$R_{p0,1}$" ist daher unüblich, für die Größenordnung der Dehnung aber unerheblich.]

---

## Seite 15

> Skizze: $\sigma$-$\varepsilon$-Diagramm „Normalspannung": Gerade durch den Ursprung, Steigungswinkel $E$. Gebogener Pfeil zur Frage: „$\Rightarrow$ für Schubspannungen?"

> Skizze: Rechteckelement, links eingespannt (Schraffur), rechts Schubspannung $\tau$ (rot, ↓); oben eingezeichnet der Schubwinkel $\gamma$ zwischen ursprünglicher und verformter (gestrichelter) Kante; gestrichelt das verformte Element (Parallelogramm).

> Skizze: Diagramm $\tau$ über $\gamma$: Gerade durch den Ursprung, „Linear!", Steigungswinkel $G$ … Schubmodul.

$$\boxed{\tau = G\,\gamma} \qquad [G] = \frac{\text{N}}{\text{mm}^2}$$

$\Rightarrow$ Schubmodul ist die Steifigkeit des Materials gegen Schubverformung.

---

## Seite 16

### Temperatureinfluss

- Dehnungen im Stab können auch durch Temperaturänderungen entstehen (thermische Ausdehnung).

$$\varepsilon_{th} \sim \Delta T \quad\to\quad \frac{\varepsilon_{th}}{\Delta T} = \alpha_t \qquad \alpha_t \text{ … thermischer Ausdehnungskoeffizient}$$

$$\boxed{\varepsilon_{th} = \alpha_t\, \Delta T}$$

| Werkstoff | $\alpha_t$ in $10^{-5}\ 1/\text{K}$ |
|---|---|
| Stahl | 1,2 |
| Aluminium | 2,3 |
| Kupfer | 1,6 |
| Beton | 1,0 |
| Holz | 2,2 … 3,3 |
| Gusseisen | 0,9 |

[Prüfung: Für Holz gilt der Bereich 2,2…3,3 (bzw. bis ca. 6) $\cdot 10^{-5}$/K nur **quer** zur Faser; **parallel** zur Faser ist $\alpha_t$ deutlich kleiner (ca. $0{,}3 \ldots 0{,}9 \cdot 10^{-5}$/K). Gusseisen liegt meist bei ca. $0{,}9 \ldots 1{,}1 \cdot 10^{-5}$/K. Übrige Werte plausibel.]

- Gesamtdehnung durch Superposition ermittelbar:
$$\varepsilon = \underbrace{\varepsilon_{el}}_{\text{elastischer}} + \underbrace{\varepsilon_{th}}_{\text{thermischer Anteil}}$$
$$\boxed{\varepsilon = \frac{\sigma}{E} + \alpha_t\, \Delta T}$$

---

## Seite 17

### Querkontraktion

> Skizze: Stab, links eingespannt (Schraffur), rechts Zugkraft $F$ (→). Koordinatensystem am linken Ende: $x$ nach rechts, $y$ (aus der Ebene, Punkt), $z$ nach unten. Unverformter Stab: Länge $L_0$, Breite $b_{z0}$ (grün bemaßt). Verformter Stab (dünner gezeichnet): Länge $L$ (länger), Breite $b_z$ (kleiner).

Dehnungen in $z$-Richtung:
$$\varepsilon_z = \underbrace{\frac{b_z - b_{z0}}{b_{z0}}}_{\text{negativ}} \sim \varepsilon_x \quad (\text{Ursache ist } \varepsilon_x)$$

$$\Rightarrow\ -\frac{\varepsilon_z}{\varepsilon_x} = \nu \qquad \nu \text{ … Querkontraktionszahl (Poisson, 1781–1840 [?])}$$

$$\boxed{\varepsilon_z = -\nu\, \varepsilon_x, \qquad \varepsilon_y = -\nu\, \varepsilon_x} \qquad \boxed{\nu = 0 \ldots 0{,}5}$$

| Werkstoff | $\nu\ [-]$ |
|---|---|
| Metalle | 0,3 |
| PVC | 0,4 |
| Beton | 0,16 |
| Gummi | $\approx 0{,}5$ (inkompressibel) |

---

## Seite 18

- Querkontraktion ist wie E-Modul und thermischer Ausdehnungskoeffizient ein weiterer Materialparameter zur Beschreibung des elastischen Materialverhaltens.

**Grundgleichungen des Zug-/Druckstabs** (grün umrahmt):
$$\varepsilon(x) = \frac{du}{dx}, \qquad \varepsilon(x) = \frac{\sigma}{E} + \alpha\,\Delta T, \qquad \sigma(x) = \frac{N(x)}{A(x)}$$

- Für isotrope Materialien sind zwei der Materialparameter $\nu$, $G$ oder $E$ ausreichend zur Beschreibung
  $\to$ Umrechnung möglich:
$$\boxed{G = \frac{E}{2(1+\nu)}}$$

z. B. Stahl: $E = 210.000\ \frac{\text{N}}{\text{mm}^2}$, $\nu = 0{,}3$
$$G = \frac{210.000\ \text{N/mm}^2}{2(1+0{,}3)} = 80.770\ \frac{\text{N}}{\text{mm}^2}$$

[Prüfung: $210\,000/2{,}6 = 80\,769{,}2$ N/mm² – korrekt (gerundet).]

---

## Seite 19

**Beispiele: ① Axialer Stab** (abgesetzter Stab)

> Skizze: Senkrechter, abgesetzter Stab, unten eingespannt (Schraffur). Oberer, schlanker Teil: Länge $L_1$, $E_1, A_1$; unterer, dickerer Teil: Länge $L_2$, $E_2, A_2$ (grün bemaßt). Am oberen Ende Kraft $F_1$ (↓, rot); am Absatz (Übergang) Kraft $F_2$ (↓, rot). Rechts Verschiebungen $w_1$ (↓, am oberen Ende) und $w_2$ (↓, am Absatz).

geg.: $F_1 = 12$ kN, $F_2 = 9$ kN, $L_1 = 30$ cm, $L_2 = 40$ cm, $A_1 = 80$ mm², $E = 210.000\ \frac{\text{N}}{\text{mm}^2} = E_1 = E_2$

ges.:
- a) $\sigma$ im Stab 1
- b) $A_2$, so dass $\sigma_1 = \sigma_2$ ($\sigma_{Stab\,1} = \sigma_{Stab\,2}$)
- c) $\Delta L_1$, $\Delta L_2$ $\to$ Absenkung $w_1$, $w_2$

**Lös.:**

① Statik

> Skizze: Schnitt im oberen Stabteil (grüne Schnittlinie): oben $F_1$ (↓), am Schnitt $F_{N1}$ (↓, positiv als Zug angenommen). Daneben Schnitt im unteren Stabteil: $F_1$ (↓) oben, $F_2$ (↓) am Absatz, am Schnitt $F_{N2}$ (↓).

$$\downarrow:\ F_{N1} = -F_1 \qquad\qquad \downarrow:\ F_{N2} = -F_1 - F_2$$

a)
$$\sigma_1 = \frac{F_{N1}}{A_1} = -\frac{F_1}{A_1} = -\frac{12.000\ \text{N}}{80\ \text{mm}^2} = -150\ \frac{\text{N}}{\text{mm}^2}$$

b) $\sigma_1 = \sigma_2$, $\quad \sigma_2 = \dfrac{F_{N2}}{A_2} = -\dfrac{F_1 + F_2}{A_2}$
$$-\frac{F_1}{A_1} = -\frac{F_1 + F_2}{A_2}$$
$$A_2 = \frac{F_1 + F_2}{F_1} A_1 = \frac{(12 + 9)\ \text{kN}}{12\ \text{kN}} \cdot 80\ \text{mm}^2 = 140\ \text{mm}^2$$

[Prüfung: $\sigma_1 = -150$ N/mm² ✓; $A_2 = 1{,}75 \cdot 80 = 140$ mm² ✓.]

---

## Seite 20

c)

> Skizze: Abgesetzter Stab (blau, unverformt) und daneben verkürzter Stab (grün, verformt), beide unten eingespannt. Am Absatz Verschiebung $\Delta L_2$ (↓), am oberen Ende $\Delta L_1 + \Delta L_2$ (↓); links $w_1$ (↓) und $w_2$ (↓).

(Hinweis eingekreist: $\left(\varepsilon = \dfrac{\sigma}{E}\right)$!)

$$\Delta L_1 = \varepsilon_1 L_1 = \frac{\sigma_1}{E_1} L_1, \qquad \Delta L_1 = -\frac{F_1}{A_1 E_1} L_1 = -\frac{12.000\ \text{N}\ \text{mm}^2}{80\ \text{mm}^2 \cdot 210.000\ \text{N}} \cdot L_1$$
$$\Delta L_1 = -0{,}214\ \text{mm} \quad \Rightarrow \text{negativ} \to \text{Verkürzung}$$

$$\Delta L_2 = \varepsilon_2 L_2 = \frac{\sigma_2}{E_2} L_2$$
$$\Delta L_2 = -\frac{F_1 + F_2}{A_2 E_2} L_2 = \frac{(12 + 9)\ \text{kN}\ \text{mm}^2}{140\ \text{mm}^2 \cdot 210.000\ \text{N}} \cdot 400\ \text{mm} = -0{,}286\ \text{mm} \quad (\text{Verkürzung})$$

$$w_1 = \Delta L_1 + \Delta L_2 = -0{,}5\ \text{mm}, \qquad w_2 = \Delta L_2 = -0{,}286\ \text{mm}$$

[Prüfung: $\Delta L_1 = -12\,000 \cdot 300/(80 \cdot 210\,000) = -0{,}2143$ mm ✓; $\Delta L_2 = -21\,000 \cdot 400/(140 \cdot 210\,000) = -0{,}2857$ mm ✓; $w_1 = -0{,}500$ mm ✓. Formale Kleinigkeiten: Im Zahlenbruch für $\Delta L_2$ fehlt das Minuszeichen (Ergebnis trägt es wieder), und „kN" muss als $21\,000$ N eingesetzt werden. Die Vorzeichen $w_1, w_2 < 0$ beziehen sich auf die Längenänderung; bei der in der Skizze nach unten positiv eingezeichneten Absenkung wären $w_1 = +0{,}5$ mm, $w_2 = +0{,}286$ mm.]

---

**Bsp. ② Variation von ①**

> Skizze: Gleicher abgesetzter Stab, unten eingespannt; oberer Teil „Stahl" mit $F_1$ (↓) oben, $F_2$ (↓) am Absatz; unterer Teil „Alu".

$\sigma_{zul}\big|_{Stab\,2} = 70\ \frac{\text{N}}{\text{mm}^2}$ (Zahl im Original überschrieben), $\quad E_{Alu} = 70$ GPa

- a) $\Delta L_1$, $\Delta L_2$?
- b) $A_2$ so, dass $|\sigma_2| \le \sigma_{zul}$

---

## Seite 21

**Lös.:**

a) Gleichungen von vorher:
$$\Delta L_1 = -\frac{F_1}{A_1 E_1} L_1 = -0{,}214\ \text{mm}$$
$$\Delta L_2 = -\frac{F_1 + F_2}{A_2 E_2} L_2 = -\frac{(12 + 9) \cdot 1000\ \text{N}\ \text{mm}^2}{140\ \text{mm}^2 \cdot 70.000\ \text{N}} \cdot 400\ \text{mm}$$
$$\Delta L_2 = -0{,}857\ [\text{mm}]$$
$\to$ 3-fache der Verschiebung von Stahl! ($E_{St} = 3 \times E_{Alu}$!)

Randnotiz: „Materialunterschiede spielen noch keine Rolle in Statik! $\Rightarrow$ gleiche Formeln"

b) $|\sigma_2| \le \sigma_{zul}$
$$\left| -\frac{F_1 + F_2}{A_2} \right| \le \sigma_{zul} \quad\Rightarrow\quad A_2 \ge \frac{F_1 + F_2}{\sigma_{zul}} = 300\ \text{mm}^2$$

Randnotiz: „unabhängig vom E-Modul! nur $\sigma_{zul}$ entscheidend, $F$, $A$"

[Prüfung: $\Delta L_2 = -21\,000 \cdot 400/(140 \cdot 70\,000) = -0{,}857$ mm ✓ (Einheit mm fehlt im Original). $A_2 \ge 21\,000/70 = 300$ mm² ✓. Hinweis: In a) wird noch $A_2 = 140$ mm² aus Bsp. ① verwendet; dabei wäre $|\sigma_2| = 150$ N/mm² $> \sigma_{zul} = 70$ N/mm², d. h. dieser Querschnitt ist für Alu unzulässig – erst mit b) ($A_2 = 300$ mm²) wird er korrekt dimensioniert, dann wäre $\Delta L_2 = -0{,}4$ mm.]

---

$\Rightarrow$ Längenänderung für Stab mit konstantem $E$, $A$:
$$\boxed{\Delta L = \frac{F L}{E A}}\ !$$

---

## Didaktische Gliederung

**Reihenfolge der Themen**
1. Motivation (S. 1–2): Übergang Stereostatik → Elastostatik; Schnittgrößen sind materialunabhängig, nun Frage nach Festigkeit und Verformung; Aufgabe der Starrkörperannahme. Zielstellung: minimaler Materialaufwand bei erforderlicher Sicherheit.
2. 1.1 Einleitung: Dimensionierung bzgl. Festigkeit (Bauteilbeanspruchung ≤ zulässige Beanspruchung) und Steifigkeit (Verformung innerhalb Grenzwerten).
3. 1.2 Voraussetzungen (A)–(D): verformbarer Körper, kleine Verformungen, Gleichgewicht am unverformten System, isotropes und homogenes Material.
4. 1.3 Beanspruchungsarten: Zug/Druck, Biegung, Torsion, Scherung/Schub, Knickung.
5. 1.4 Wichtige Größen: Spannung $\sigma$, Verzerrung $\varepsilon$, Materialgesetz (hier linear).
6. 2. Zug und Druck in Stäben – 2.1 Spannungen im Stab: Stabdefinition, Stabachse, $\sigma = N/A$, $\sigma(x) = N(x)/A(x)$; Bsp. ①/② (S. 7); Zerlegung in Normal- und Schubspannung; Prinzip von St. Venant.
7. 2.4 Kerbspannungen (S. 9–10, im Original vorgezogen): Nennspannung, Formzahl $k_t$.
8. 2.2 Dehnungen (S. 11–12): $\varepsilon = \Delta L/L$, allgemein $\varepsilon = du/dx$.
9. 2.3 Materialgesetz (S. 12–18): Zugversuch, $\sigma$-$\varepsilon$-Diagramm, Kennwerte; Hookesches Gesetz $\sigma = E\varepsilon$ mit E-Modul-Tabelle; Schub $\tau = G\gamma$; Temperatureinfluss $\varepsilon_{th} = \alpha_t \Delta T$; Querkontraktion $\nu$; Grundgleichungen; $G = E/(2(1+\nu))$.
10. Anwendungsbeispiele abgesetzter Stab (S. 19–21) und Zusammenfassung $\Delta L = FL/(EA)$.

**Definitionen**
- Stab: Länge ≫ Querschnittsabmessungen, nur Belastung in Stabrichtung (Normalkraft); Stabachse = Verbindungslinie der Querschnittsschwerpunkte.
- Isotrop: gleiche Eigenschaften in jeder Richtung; homogen: gleiche Eigenschaften an jedem Ort.
- Spannung: auf Flächenelement bezogene innere Kraft; Normalspannung $\sigma^*$ (senkrecht zur Fläche), Schubspannung $\tau$ (parallel zur Fläche).
- Dehnung $\varepsilon$: relative Längenänderung (dimensionslos); Schubwinkel $\gamma$.
- Materialgesetz; E-Modul, Schubmodul $G$, thermischer Ausdehnungskoeffizient $\alpha_t$, Querkontraktionszahl $\nu$ ($0 \ldots 0{,}5$).
- Kennwerte: Proportionalitätsgrenze $\sigma_P$, Elastizitätsgrenze $\sigma_E$, Streckgrenze $\sigma_F$, Zugfestigkeit $R_m$.
- Prinzip von St. Venant; Kerbspannung, Nennspannung, Formzahl $k_t$.

**Rechenschema Zug-/Druckstab**
1. Statik: Schnitt je Bereich, Normalkraft $N$ (Zug positiv) aus Gleichgewicht.
2. Spannung $\sigma = N/A$ (ggf. $\sigma(x) = N(x)/A(x)$, bei Kerben $\sigma_{max} = k_t F/A_K$).
3. Bemessung: $|\sigma| \le \sigma_{zul} \Rightarrow A \ge |N|/\sigma_{zul}$.
4. Dehnung $\varepsilon = \sigma/E\ (+\alpha_t \Delta T)$.
5. Längenänderung je Abschnitt $\Delta L_i = N_i L_i/(E_i A_i)$; Verschiebungen durch Aufsummieren vom festen Lager aus.

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| Bsp. ① (2.1) | Zugstab mit veränderlichem Querschnitt | $N = F$ konst., $A(x_1) > A(x_2)$ | $\sigma(x_1) < \sigma(x_2)$ (qualitativ) | 7 |
| Bsp. ② (2.1) | hängender Stab unter Eigengewicht, $A$ = const | $F_1$, $F_2$, $g$ | $N(x_1) > N(x_2)$, $\sigma(x_1) > \sigma(x_2)$ (im Original korrigiert) | 7 |
| Bohrung | Flachstab mit Loch | $k_t = 3$ | $\sigma_{max} = 3\,\sigma_{mittel}$ | 10 |
| Dehnung S235JR | Werkstoffkennwert | $\sigma = 235$ N/mm², $E = 210.000$ N/mm² | $\varepsilon = 0{,}0011 \approx 0{,}1\,\%$ (genauer 0,11 %) | 14 |
| Schubmodul Stahl | Umrechnung | $E = 210.000$ N/mm², $\nu = 0{,}3$ | $G = 80.770$ N/mm² | 18 |
| Beispiel ① | abgesetzter Stab (Stahl), unten eingespannt, $F_1$ oben, $F_2$ am Absatz | $F_1 = 12$ kN, $F_2 = 9$ kN, $L_1 = 30$ cm, $L_2 = 40$ cm, $A_1 = 80$ mm², $E = 210.000$ N/mm² | $\sigma_1 = -150$ N/mm²; $A_2 = 140$ mm²; $\Delta L_1 = -0{,}214$ mm, $\Delta L_2 = -0{,}286$ mm; $w_1 = -0{,}5$ mm, $w_2 = -0{,}286$ mm | 19–20 |
| Beispiel ② | wie ①, unterer Teil Alu | zusätzlich $E_{Alu} = 70$ GPa, $\sigma_{zul} = 70$ N/mm² | $\Delta L_1 = -0{,}214$ mm, $\Delta L_2 = -0{,}857$ mm (mit $A_2 = 140$ mm²); $A_2 \ge 300$ mm² | 20–21 |

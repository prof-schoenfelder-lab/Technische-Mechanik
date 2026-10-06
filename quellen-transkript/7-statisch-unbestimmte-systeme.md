# Technische Mechanik – 2.5 Statisch unbestimmte Stabsysteme (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen
Quelle: `Quellen/Vorlesung-2013/7-statisch-unbestimmte-systeme.pdf` (16 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten, Grün = Bemaßungen, Koordinaten, Hervorhebungen.
- Das Kapitel schließt an Abschnitt 2 „Zug und Druck in Stäben" aus `6-Festigkeitslehre` an.
- Unsichere Lesungen sind mit [?] markiert, Anmerkungen der Transkription mit [Prüfung: ...].

---

## Seite 1

### 2.5 Statisch unbestimmte Stabsysteme

- bisher: Gleichgewichtsbedingungen zum Lösen der Unbekannten
  $\to$ 3 Gleichungen (2D) $\hat=$ 3 Unbekannte
- jetzt: auch Gleichungen der Verformung, Materialverhalten!
  $\Rightarrow$ zusätzliche Gleichungen für die Lösung **statisch unbestimmter Systeme**

$\Rightarrow$ Erklärung am Bsp.:

> Skizze: Stab der Länge $L$ (grün bemaßt) zwischen zwei starren Wänden (Schraffur links und rechts); linkes Stabende $A$, rechtes Stabende $B$ (grün eingekreist).

Ein Stab der Länge $L$ passt im Ausgangszustand ohne Spiel zwischen zwei unverschiebliche Wände. Danach wird er gleichmäßig erwärmt.

geg.: $L$, $EA = \text{konst.}$, $\Delta T = \text{konst.}$, $\alpha$
ges.: Auflagerreaktionen, Wärmespannung

**Lös.:** (Statik)

> Skizze: Freigeschnittener Stab; links $F_A$ (→, rot), rechts $F_B$ (→, rot).

$$\rightarrow:\ F_A + F_B = 0$$
(Randnotiz: kein ↑, $\curvearrowleft$ [vertikales Gleichgewicht, Momentengleichgewicht], da Stab $\to$ nur axiale Last)

$\Rightarrow$ 1 Gleichung $\to$ 2 Unbekannte $\to$ Aufgabe ist einfach statisch unbestimmt

Schnittgrößen:

> Skizze: Linkes Stabstück bis zur Stelle $x$ (grün, Koordinate $x$ von links): links $F_A$ (→), am Schnitt $N(x)$ (→).

$$\rightarrow:\ F_A + N(x) = 0 \quad\Rightarrow\quad N(x) = -F_A = \text{konst.}$$

$\Rightarrow$ allein die Gleichgewichtsbedingungen reichen nicht aus!

---

## Seite 2

$\Rightarrow$ Zur Lösung der Aufgabe ist eine **Verformungsbetrachtung** erforderlich!

$\Rightarrow$ Querschnitte bei $x = 0$, $x = L$ verschieben sich nicht! (grün: Kinematik, Verformungsbedingungen)

(Kinematik)
$$\varepsilon = \frac{du}{dx} \quad\leadsto\quad u(x) = \int \varepsilon\, dx$$
$$u(x) = \int \left[\frac{\sigma}{E} + \alpha \Delta T\right] dx \qquad \Big|\ \sigma = \frac{N}{A}$$
$$u(x) = \int \left[\frac{N}{AE} + \alpha \Delta T\right] dx$$

$\Rightarrow$ integrieren:
$$u(x) = \frac{N}{EA}x + \alpha \Delta T x + C \qquad \big|\ \text{mit } N = -F_A$$
$$\underline{u(x) = -\frac{F_A}{EA}x + \alpha \Delta T x + C}$$

Aufgabe ist lösbar:
- Unbekannte: $F_A$ $\to$ statisch Unbekannte; $C$ $\to$ Integrationskonstante
- Randbedingungen: $u(x=0) = 0$, $u(x=L) = 0$

Allgemein gilt (grün umrandet):
$$\boxed{\text{Anzahl der linear unabhängigen Gleichungen aus Rand- und Übergangsbedingungen} = \sum\left[\text{Grad der statischen Unbestimmtheit} + \text{Anzahl der Integrationskonstanten}\right]}$$

---

## Seite 3

Gleichungen aus Randbedingungen:

$$u(x)\big|_{x=0} = 0 \ \to\ u(0) = -0 + 0 + C = 0 \quad\Rightarrow\quad \underline{C = 0}$$

$$u(x)\big|_{x=L} = 0 \ \to\ u(L) = -\frac{F_A}{EA}L + \alpha \Delta T L = 0$$
$$F_A = \frac{\alpha \Delta T L\, EA}{L} \quad\Rightarrow\quad \underline{F_A = \alpha \Delta T\, EA}$$

aus Statik:
$$\underline{F_B = -F_A = -\alpha \Delta T\, EA} \qquad \Rightarrow \text{Lagerreaktionen gelöst!}$$

**Wärmespannung:**
$$N(x) = -F_A = -\alpha \Delta T\, EA$$
$$\sigma(x) = \frac{N(x)}{A(x)} = -\frac{\alpha \Delta T E A}{A} = \underline{-\alpha \Delta T E} \qquad \Rightarrow \text{Wärmespannung gelöst!}$$

weitere Zusammenhänge (durchgestrichen):
$$u(x) = -\frac{F_A}{EA}x + \alpha \Delta T x \quad \text{mit } F_A = \alpha \Delta T EA$$
$$= -\frac{\alpha \Delta T EA}{EA}x + \alpha \Delta T x$$
$$\underline{u(x) = 0} \ \to\ \text{Verschiebung ist null} \quad (u(x) = 0!)$$

> Skizze (grün): Stab zwischen zwei Wänden, keine Verschiebung.

[Prüfung: Ergebnis korrekt; Vorzeichen konsistent ($F_A$ als → am linken Ende angesetzt, also Druck auf den Stab; $N = -\alpha\Delta T EA < 0$ für $\Delta T > 0$ = Druck). $\sigma = -\alpha \Delta T E$ ist unabhängig von $L$ und $A$. In der Zeile für $C$ steht im Original „$u(x) = -0 + 0 + C$", gemeint $u(0)$.]

---

## Seite 4

$\Rightarrow u(x) = 0 \to$ keine Dehnung?

**doch:**
$$\varepsilon = \varepsilon_{el} + \varepsilon_{th} = 0 \qquad (\text{wegen } u(x) = 0)$$
$$\varepsilon_{el} = -\varepsilon_{th} \quad\Rightarrow\quad \frac{\sigma}{E} = -\alpha \Delta T$$

$\Rightarrow$ Die auftretende thermische Dehnung muss durch eine entgegenwirkende elastische Dehnung kompensiert werden!

> Skizze (Gedankenmodell in drei Schritten, untereinander):
> 1. Stab links an Wand, rechts frei; durch $\Delta T$ verlängert er sich um $\varepsilon_{th} = \Delta T \alpha_t$ (grün gestrichelt) $\to$ spannungsfrei!
> 2. Stab wird um $\varepsilon_{el}$ zurückgedrückt (rote Druckspannungen $\sigma$ am rechten Ende) – „zurückdrücken auf Ausgangslänge"; $\Rightarrow$ Zwangsbedingung durch 2. Wand $\Rightarrow$ elastische Dehnung notwendig $\to$ Spannung.
> 3. Stab zwischen zwei Wänden in Ausgangslänge.

---

## Seite 5

- Lösung mit konkreten Zahlenwerten

Stahl: $\alpha = 1{,}2 \cdot 10^{-5}\ \text{K}^{-1}$, $E = 210.000\ \frac{\text{N}}{\text{mm}^2}$, $\Delta T = 100$ K ($25\,°\text{C} \to 125\,°\text{C}$), $\left(\sigma_{F0} = 240\ \frac{\text{N}}{\text{mm}^2}\right)$

$$\sigma_x = -\alpha \Delta T E = -252\ \frac{\text{N}}{\text{mm}^2} \quad (> \sigma_{F0}\,!)$$

[Prüfung: $1{,}2\cdot10^{-5} \cdot 100 \cdot 210\,000 = 252$ N/mm² ✓ – Betrag liegt über der Fließgrenze, der Stab würde plastisch stauchen (bzw. knicken).]

---

**Weiteres Beispiel für stat. unbestimmtes System: ①**

> Skizze: Starrer, horizontaler Balken der Länge $2L$ (grün bemaßt: $L$ + $L$). Rechtes Ende $A$: Festlager (Wandlager). Linkes Ende: senkrechter Stab 1 der Länge $L$ nach unten zum gelenkigen Lager $B$. Balkenmitte: schräger Stab 2 nach rechts oben zum gelenkigen Lager $C$; $C$ liegt senkrecht über $A$ im Abstand $2L$ (grün bemaßt). Am linken Balkenende Kraft $F$ (↓, rot). Grün umrandet: Freischnitt Balken.

geg.:
- starrer Balken
- gestützt durch ein Festlager und zwei Stäbe
- $F$, $L$, $E_1 A_1 = E_2 A_2 = EA$

ges.: – Auflagerreaktionen – Stabkräfte

---

## Seite 6

**Lös.: ① Statik**

> Skizze: Freigeschnittener Balken: links $F$ (↓) und Stabkraft $F_{S1}$ (↓, als Zug angesetzt); in der Mitte $F_{S2}$ schräg nach rechts oben unter Winkel $\alpha$ zur Balkenachse (Zerlegung im Kräfteparallelogramm); rechts bei $A$: $F_{AH}$ (→), $F_{AV}$ (↑). Bemaßung $L$ | $L$.

> Skizze rechts: rechtwinkliges Dreieck für Stab 2: Ankathete $L$, Gegenkathete $2L$, Hypotenuse $L_2$, Winkel $\alpha$.

$$L_2 = \sqrt{L^2 + 4L^2} = \sqrt5\, L$$
$$\sin\alpha = \frac{2L}{\sqrt5 L} = \frac{2}{\sqrt5}, \qquad \cos\alpha = \frac{L}{\sqrt5 L} = \frac{1}{\sqrt5} \qquad \Rightarrow \alpha = 63{,}43°$$

$$\rightarrow:\quad F_{S2}\cos\alpha + F_{AH} = 0 \qquad (1)$$
$$\uparrow:\quad -F - F_{S1} + F_{S2}\sin\alpha + F_{AV} = 0 \qquad (2)$$
$$\curvearrowleft A:\quad -L\,F_{S2}\sin\alpha + F\cdot 2L + F_{S1}\cdot 2L = 0 \qquad (3)$$

4 Unbekannte: $F_{S2}$, $F_{AH}$, $F_{AV}$, $F_{S1}$ – nur 3 Gleichungen! $\Rightarrow$ einfach statisch unbestimmt

$\to$ ② Kinematik, Verformung notwendig

> Skizze: System mit verdrehtem Balken (grün): Balken dreht sich um $A$ um den Winkel $\varphi$; Punkt I (linkes Ende, Anschluss Stab 1) und Punkt II (Mitte, Anschluss Stab 2) bewegen sich nach unten; die Stäbe 1 und 2 in verformter Lage.

exakte Betrachtung: $\to$ Punkte I und II bewegen sich auf einer Kreisbahn.

---

## Seite 7

vereinfachte Betrachtung:
- Stäbe elastisch
- Winkel $\varphi$ sehr klein
- $\Rightarrow$ Bahnkurven dürfen durch Tangenten an die Bahnkurve ersetzt werden

> Skizze: Balken um $A$ gedreht; Punkt I senkt sich um $u_1$, Punkt II um $u_2$ (senkrecht). Stab 2 vor und nach der Verformung mit Winkeln $\alpha$ und $\alpha'$ (grün).

$\Rightarrow$ Zwischen $u_1$ und $u_2$ existiert ein Zusammenhang $\Rightarrow$ **Zwangsbedingung**
$$\boxed{\frac{u_2}{L} = \frac{u_1}{2L}} \quad\Rightarrow\quad u_1 = 2u_2 \qquad (A)$$

Stab 1: $u_1$ führt zu Stabverkürzung
$$\Delta L_1 = -u_1 \qquad (B)$$

Stab 2:

> Skizze: Vergrößerung am Anschlusspunkt II: senkrechte Verschiebung $u_2$, Stabrichtung unter $\alpha$ bzw. $\alpha'$; die Projektion von $u_2$ auf die Stabachse (rot) ist die Verlängerung $\Delta L_2$.

Winkel $\alpha$ ändert sich bei kleinem $\varphi$ nur sehr wenig $\leadsto \alpha' \approx \alpha$
$$u_2 \sin\alpha = \Delta L_2 \qquad (C)$$

Einsetzen von (B) und (C) in (A) liefert:
$$-\Delta L_1 = \frac{2\,\Delta L_2}{\sin\alpha} \qquad (D)$$

---

## Seite 8

Allgemein gilt: $\dfrac{\Delta L}{L} = \varepsilon_x = \dfrac{\sigma_x}{E} = \dfrac{N}{AE}$

③ Materialgesetz
$$\to\ \Delta L_1 = \frac{N_1 L_1}{E_1 A_1} = \frac{F_{S1} L}{EA} \qquad (E)$$
$$\to\ \Delta L_2 = \frac{N_2 L_2}{E_2 A_2} = \frac{F_{S2}\sqrt5 L}{EA} \qquad (F)$$

Einsetzen von (E) und (F) in (D) führt auf
$$-\frac{F_{S1} L}{EA} = \frac{2 F_{S2}\sqrt5 L}{\sin\alpha\, EA} \qquad \left|\ \sin\alpha = \frac{2}{\sqrt5}\right.$$
$$-\frac{F_{S1} L}{EA} = \frac{2 F_{S2}\sqrt5 L \sqrt5}{2\, EA}$$
$$\boxed{-F_{S1} = 5 F_{S2}} \quad (4) \ \to \text{fehlende Gleichung zur Ermittlung der Lagerreaktionen und Stabkräfte}$$

(4) in (3):
$$-L F_{S2}\sin\alpha + F\,2L - 5F_{S2}\cdot 2L = 0$$
$$-F_{S2} L(\sin\alpha + 10) + F\,2L = 0$$
$$F_{S2} = \frac{2F}{\sin\alpha + 10} = 0{,}184\,F$$

---

## Seite 9

mit (4): $\quad F_{S1} = -0{,}92\,F$ (im Original zunächst „$-0{,}082$" [?] geschrieben, durchgestrichen und zu „$0{,}92$" korrigiert)

mit (1): $\quad F_{AH} = -F_{S2}\cos\alpha = -0{,}082\,F$

mit (2): $\quad F_{AV} = +F + F_{S1} - F_{S2}\sin\alpha = -0{,}084\,F$

[Prüfung: $F_{S2} = 2F/(10 + 0{,}8944) = 0{,}18358\,F$ ✓; $F_{S1} = -5F_{S2} = -0{,}9179\,F$ ✓; $F_{AH} = -0{,}18358 \cdot 0{,}4472\,F = -0{,}0821\,F$ ✓. **Rundungsfehler bei $F_{AV}$:** exakt $F_{AV} = F(1 - 0{,}91790 - 0{,}16420) = -0{,}0821\,F$, also $-0{,}082\,F$ (nicht $-0{,}084\,F$). Der Wert $-0{,}084$ entsteht durch Weiterrechnen mit den gerundeten Zwischenwerten $-0{,}92$ und $0{,}184$. Kontrolle über (3): $-0{,}18358\cdot0{,}8944 + 2 - 2\cdot0{,}9179 = 0$ ✓. Exakt gilt sogar $F_{AH} = F_{AV} = -\tfrac{2}{10\sqrt5 + 2}F$.]

---

$\to$ **Kochrezept für statisch unbestimmte Aufgaben**
1. Statik $\to$ Gleichgewichtsbedingungen
2. Kinematik / Verformung $\to$ Beziehung $u$, $\varepsilon$
3. Materialgesetz $\to$ Beziehungen $\varepsilon, \sigma \to F$

$\Rightarrow$ Lösen des Gleichungssystems

(Literaturhinweis eingerahmt: Dankert S. 186)

---

**Beispiel: stat. unbest. ②**

> Skizze: Starrer Kasten (Last $F$ ↓ im Inneren), seitlich zwischen zwei senkrechten Wänden geführt (Schraffur links/rechts, d. h. nur vertikal verschieblich). Oben hängt der Kasten an drei Seilen: Seil 2 (links, Länge $L_2$, an Decke befestigt), Seil 1 (Mitte, Länge $L_1$, an höher liegender Decke befestigt, $L_1 > L_2$), Seil 3 (rechts) läuft über eine feste Rolle zu einem Gegengewicht $F_G$ (↓, rot). Grün umrandet: Freischnitt Kasten.

geg.: – 3 Seile halten Last $F$
- $F = 8$ kN, $L_1 = 60$ cm, $A_1 = 36$ mm²
- $F_G = 5$ kN, $L_2 = 30$ cm, $A_2 = 12$ mm²
- $E = E_1 = E_2 = E_3$ (im Original „$E_2$" doppelt geschrieben)

ges.: Seilkräfte $F_{S1}$, $F_{S2}$

---

## Seite 10

**Lös.: ① Statik**

> Skizze: Freigeschnittener Kasten: oben $F_{S2}$, $F_{S1}$, $F_G$ (je ↑), unten $F$ (↓).

$$\uparrow:\ F_{S2} + F_{S1} + F_G - F = 0 \qquad (1)$$
($\rightarrow$: entfällt.) $\Rightarrow$ eine Gleichung, 2 Unbekannte $\to$ einfach statisch unbestimmt

② Kinematik / Verformung
$$\Delta L_1 = \Delta L_2 \quad (A) \ \to \text{gleiche Verlängerung!}$$

③ Materialgesetz $\quad \left(\Delta L = \varepsilon L = \dfrac{\sigma}{E}L = \dfrac{FL}{AE}\right)$
$$\Delta L_1 = \frac{F_{S1} L_1}{E A_1} \quad (B), \qquad \Delta L_2 = \frac{F_{S2} L_2}{E A_2} \quad (C)$$

(B) und (C) in (A):
$$\frac{F_{S1} L_1}{E A_1} = \frac{F_{S2} L_2}{E A_2} \quad\Rightarrow\quad F_{S1} = F_{S2}\frac{L_2}{L_1}\frac{A_1}{A_2} \qquad (2)$$

(2) in (1):
$$F_{S2}\left(1 + \frac{L_2}{L_1}\frac{A_1}{A_2}\right) + F_G - F = 0$$
$$F_{S2} = \frac{F - F_G}{1 + \underbrace{\tfrac{L_2}{L_1}}_{0{,}5}\underbrace{\tfrac{A_1}{A_2}}_{3}} = \frac{2}{5}(F - F_G)$$

---

## Seite 11

$$\underline{F_{S2} = 1200\ \text{N}}, \qquad F_{S1} = \underbrace{1{,}5}_{\frac{A_1}{A_2}\frac{L_2}{L_1}} F_{S2} = \underline{1800\ \text{N}}$$

[Prüfung: $\tfrac{L_2}{L_1}\tfrac{A_1}{A_2} = 0{,}5\cdot3 = 1{,}5$; $F_{S2} = 3000/2{,}5 = 1200$ N ✓; $F_{S1} = 1800$ N ✓; Kontrolle $1200 + 1800 + 5000 = 8000$ N $= F$ ✓.]

---

### Übungen zu Zug/Druck in Stäben

**① Eigengewicht Stab**

> Skizze: Senkrechter Stab der Länge $L$ (grün bemaßt), oben an der Decke eingespannt, unten Kraft $F$ (↓, rot). $\vec g$ (↓). Im Stab rote Pfeile ↓ (Eigengewicht $F_g$). Unteres Ende grün umkreist.

geg.: $F = 40$ kN, $L = 4$ m, $E = 210.000\ \frac{\text{N}}{\text{mm}^2}$, $\rho = 7{,}85\ \frac{\text{g}}{\text{cm}^3} = 7850\ \frac{\text{kg}}{\text{m}^3}$

ges.:
- a) Durchmesser für $\sigma_{zul} = 200$ N/mm²
- b) Verlängerung bei $d = 16$ mm

**Lös.: a)**

> Skizze: Unteres Stabstück der Länge $x$ freigeschnitten: oben $N(x)$ (↑), unten $F$ (↓), Eigengewicht $F_G$ (rote Pfeile ↓); Koordinate $x$ vom unteren Ende nach oben.

$F_g$? $\to$ Linienlast $\to$ Kraft/Länge

> Skizze: Stabelement der Länge $x$ mit Gewichtskraft $F_G = m\cdot g$.

$$m = V\rho = A\rho x, \qquad F_G = gA\rho x$$

$$\uparrow:\ N(x) - F - gA\rho x = 0 \quad\Rightarrow\quad N(x) = gA\rho x + F$$

> Skizze: $N$-Verlauf (Trapez) über die Stablänge: unten $F$, oben $F + gA\rho L$; Kennzeichnung „N".

$$\sigma(x) = \frac{N(x)}{A} = \frac{4N(x)}{\pi d^2}$$
$$\sigma(x)\big|_{max,\,x=L} = \frac{4(gA\rho L + F)}{\pi d^2} \le 200\ \frac{\text{N}}{\text{mm}^2}$$

---

## Seite 12

$$\frac{4\left(g\frac{\pi}{4}d^2\rho L + F\right)}{\pi d^2} \le \sigma_{zul}$$
$$g\rho L + \frac{4F}{\pi d^2} \le \sigma_{zul}$$
$$\frac{4F}{\pi d^2} \le \sigma_{zul} - g\rho L$$
$$d \ge \sqrt{\left[\frac{(\sigma_{zul} - g\rho L)\,\pi}{4F}\right]^{-1}}$$
$$\underline{d \ge 15{,}97\ \text{mm}}$$

Randnotiz „Einheiten!": $\dfrac{\text{m}}{\text{s}^2}\dfrac{\text{kg}}{\text{m}^3}\text{m} = \dfrac{\text{N}}{\text{m}^2}$

[Prüfung: $g\rho L = 9{,}81\cdot7850\cdot4 = 0{,}308$ N/mm²; $d \ge \sqrt{4\cdot40\,000/(\pi\cdot199{,}69)} = 15{,}97$ mm ✓. Das Eigengewicht ändert $d$ nur um ca. 0,01 mm.]

b) (durchgestrichener erster Ansatz: $\Delta L = \varepsilon L = \frac{\sigma(x)}{E}L = \frac{N(x)}{AE}L = \frac{(gA\rho x + F)}{EA}\dots$ – verworfen, Randnotiz: „Spannung nicht konstant $\to \varepsilon(x) \ne$ konst.!")

$$\varepsilon = \frac{du}{dx} \ \Rightarrow\ u(x) = \int_0^L \varepsilon(x)\,dx$$
$$u(x) = \int_0^L \frac{\sigma(x)}{E}dx = \int_0^L \frac{N(x)}{EA}dx = \int_0^L \frac{1}{EA}(gA\rho x + F)\,dx = \frac{1}{EA}\left[gA\rho\frac{x^2}{2} + Fx\right]_0^L$$

Randnotiz (eingerahmt): „ist bei $x = 0$ $u(x) = 0$? nicht $\Delta L_{max}$ $\to$ Bezugspunkt an Spitze! $\Rightarrow u(0) = 0$ $\Rightarrow$ KOS-Ursprung wird verschoben"

---

## Seite 13

$$u(x)\big|_{x=L} = \Delta L = \frac{1}{EA}\left[gA\rho\frac{L^2}{2} + F L - 0\right]$$
$$\Delta L = \frac{L^3}{EA}\left(\frac{gA\rho}{2L} + \frac{F}{L^2}\right) = \underline{3{,}79\ \text{mm}}$$

Randnotiz (grün): $\rho = 7{,}85\cdot10^{-6}\ \frac{\text{kg}}{\text{mm}^3}$, $g = 9{,}81\ \frac{\text{m}}{\text{s}^2}$ $\to$ Rest in N, mm

$\Rightarrow$ Berechnung ohne Eigengewicht $\left(gA\rho\frac{L^2}{2} = 0\right)$:
$$\Delta L = \frac{1}{EA}(F\cdot L) = 3{,}79\ \text{mm}$$

$\Rightarrow$ Eigengewicht häufig vernachlässigbar!

[Prüfung: $A = \pi\cdot16^2/4 = 201{,}1$ mm²; $FL/(EA) = 40\,000\cdot4000/(210\,000\cdot201{,}1) = 3{,}789$ mm; Eigengewichtsanteil $\rho g L^2/(2E) = 0{,}003$ mm; Summe $3{,}792$ mm ✓.]

---

**② Gewicht an Fachwerk** (Übungen 11, 1.1 – rot: „geändert $A_1$!")

> Skizze: Zwei Stäbe an einer senkrechten Wand gelenkig gelagert; die Lagerpunkte haben den senkrechten Abstand $L$ (grün). Stab 1 (oben) verläuft schräg nach rechts unten, Stab 2 (unten) waagerecht; beide treffen sich im Knoten; Winkel $\alpha$ zwischen Stab 1 und Stab 2 am Knoten. Am Knoten hängt Seil 3 der Länge $L_3$ (grün) senkrecht mit einer Masse; Gewichtskraft $m\cdot g$ (↓, rot). $\vec g$ (↓). Grün umkreist: Knoten mit Seil und Masse (Freischnitt).

geg.: – Halterung aus Stäben
- $L = 3$ m, $\alpha = 30°$, $E = 210.000\ \frac{\text{N}}{\text{mm}^2}$, $\rho = 7{,}86\ \text{g/cm}^3$
- Stab 1: $\sigma_{zul} = 160$ N/mm², $A_1 = 11$ cm²
- Stab 2: $\sigma_{zul} = 160$ N/mm², $A_2 = 20{,}4$ cm²
- Seil 3: $L_3 = 1$ m, $\sigma_{zul} = 450$ N/mm²

ges.:
- a) zulässige Last $m\cdot g$ $\to m_{max}$?
- b) $\Delta L_1$, $\Delta L_2$ für $m_{max}$?
- c) Querschnitt $A_3$ für $m_{max}$?
- d) für $\sigma_{zul}$ vom Seil für $m_{max}$: $u(x)$ und $\Delta L_3$?
- e) Berücksichtigung der Masse des Seils $m_3$?

---

## Seite 14

a)

> Skizze: Freigeschnittener Knoten: $F_{S1}$ entlang Stab 1 (nach links oben), $F_{S2}$ entlang Stab 2 (nach links), $m g$ (↓); Winkel $\alpha$ zwischen den Stäben.

$$\rightarrow:\ -F_{S2} - F_{S1}\cos\alpha = 0 \quad (1), \qquad \uparrow:\ -mg + F_{S1}\sin\alpha = 0 \quad (2)$$
$$\underline{F_{S1} = \frac{mg}{\sin\alpha} = 2mg}$$
$$F_{S2} = -F_{S1}\cos\alpha = -mg\frac{\cos\alpha}{\sin\alpha} = -\frac{2\sqrt3}{2}mg \quad\Rightarrow\quad \underline{F_{S2} = -\sqrt3\,mg}$$

Spannungen in Stäben:
$$\sigma_1 = \frac{F_{S1}}{A_1} = \frac{2mg}{11\ \text{cm}^2} \le \sigma_{zul} \ \Rightarrow\ m \le \frac{\sigma_{zul}A_1}{2g} \ \Rightarrow\ m \le 8.970\ \text{kg}$$
(grün: „in Übung $2\times A_1$ Doppelprofil!")

$$\sigma_2 = \frac{|F_{S2}|}{A_2} = \frac{|-\sqrt3\,mg|}{A_2} \le \sigma_{zul} \ \Rightarrow\ m \le \frac{\sigma_{zul}A_2}{\sqrt3\,g} \ \Rightarrow\ m \le 19.209\ \text{kg}$$
$\to$ geringerer Wert maßgebend:
$$\underline{m \le 8.970\ \text{kg}}$$

[Prüfung: $160\cdot1100/(2\cdot9{,}81) = 8970$ kg ✓; $160\cdot2040/(\sqrt3\cdot9{,}81) = 19\,210$ kg ✓ (Original 19.209). Im Original steht in der Zwischenzeile „$mg \le \ldots$ kg"; gemeint ist $m$. Hinweis: Stab 2 ist Druckstab – ein Knicknachweis wird hier (noch) nicht geführt.]

---

## Seite 15

b) $\Delta L_1$:
$$\varepsilon_1 = \frac{\Delta L_1}{L_1}, \qquad \Delta L_1 = \varepsilon_1 L_1 = \frac{\sigma_1}{E_1}L_1 = \frac{F_{S1}L_1}{A_1E_1}$$
$L_1 = \dfrac{L}{\sin\alpha}$ (im Original „$L\sin\alpha$" durchgestrichen und zu $L/\sin\alpha$ korrigiert)
$$\Delta L_1 = \frac{2mg}{A_1E_1}L\sin\alpha = \frac{4mgL}{A_1E}, \qquad \underline{\Delta L_1 = 4{,}57\ \text{mm}}$$

[Prüfung: **Schreibfehler** in der Zwischenzeile: Es muss $\frac{2mg}{A_1E}\cdot\frac{L}{\sin\alpha}$ heißen (nicht $L\sin\alpha$); nur damit ergibt sich $\frac{4mgL}{A_1E}$ (wegen $1/\sin30° = 2$). Endergebnis $4\cdot88\,000\cdot3000/(1100\cdot210\,000) = 4{,}57$ mm ✓.]

$\Delta L_2$:
$$\varepsilon_2 = \frac{\Delta L_2}{L_2}, \qquad \underline{\Delta L_2} = \varepsilon_2 L_2 = \frac{\sigma_2}{E}L_2 = \frac{F_{S2}}{A_2E}L_2 = \frac{-\sqrt3\,mg}{A_2E}\frac{L}{\tan\alpha} = \underline{-1{,}85\ \text{mm}}$$
mit $\tan\alpha = \dfrac{L}{L_2}$, $L_2 = \dfrac{L}{\tan\alpha}$

[Prüfung: $L_2 = 5196$ mm; $\Delta L_2 = -152\,420\cdot5196/(2040\cdot210\,000) = -1{,}85$ mm ✓.]

> Skizze: Stabzweischlag vor und nach der Verformung: Stab 1 verlängert, Stab 2 verkürzt; Knoten verschiebt sich nach links unten (Pfeile ↓ und ←).

c) $m = 8970$ kg

> Skizze: Masse freigeschnitten: $F_{S3}$ (↑), $mg$ (↓).

$$\sigma_3 = \frac{F_{S3}}{A_3} \le \sigma_{zul} \quad (F_{S3} = mg)$$
$$\frac{mg}{A_3} \le \sigma_{zul} \ \Rightarrow\ A_3 \ge \frac{mg}{\sigma_{zul}}, \qquad \underline{A_3 \ge 195{,}5\ \text{mm}^2}$$

[Prüfung: $87\,996/450 = 195{,}5$ mm² ✓ (mit $mg = 88\,000$ N: 195,6 mm²).]

---

## Seite 16

d)

> Skizze: Senkrechtes Seil der Länge $L_3$, oben am Knoten befestigt, Koordinate $x$ (↓, grün) vom oberen Ende; unten Masse mit $F_G$ (↓, rot).

$$\varepsilon = \frac{du}{dx} \ \leadsto\ u(x) = \int\varepsilon\,dx = \int\frac{\sigma}{E}dx = \int\frac{m_{max}g}{A_3E}dx$$
$$u(x) = \frac{m_{max}g}{A_3E}x + C$$
RB: $u(x)\big|_{x=0} = 0 \ \to\ C = 0$
$$\underline{u(x) = \frac{m_{max}g}{A_3E}x}$$
$$\underline{\Delta L_3} = u(x = L_3) = \frac{m_{max}g}{A_3E}L_3 = \underline{2{,}14\ \text{mm}}$$

[Prüfung: $\Delta L_3 = \sigma_{zul}L_3/E = 450\cdot1000/210\,000 = 2{,}14$ mm ✓. Hinweis: $u(x)$ ist hier die Verschiebung relativ zum Knoten; die Verschiebung des Knotens selbst (aus b) kommt für die absolute Absenkung der Masse noch hinzu.]

e)
$$m_3 = V_3\rho_{St}, \quad V_3 = A_3 L_3 \quad\Rightarrow\quad m_3 = A_3L_3\rho_{St}$$
$$\underline{m_3 = 1{,}54\ \text{kg}} \ll m_{max} \quad (\text{muss nicht berücksichtigt werden})$$
$$(m_3 \approx 0{,}017\,\%\ \text{von}\ m_{max})$$

[Prüfung: $195{,}5\cdot1000\cdot7{,}86\cdot10^{-6} = 1{,}54$ kg ✓; $1{,}54/8970 = 0{,}017\,\%$ ✓.]

---

## Didaktische Gliederung

**Reihenfolge der Themen**
1. Einordnung (S. 1): bisher nur Gleichgewicht (3 Gl. in 2D); jetzt zusätzlich Verformungs- und Materialgleichungen für statisch unbestimmte Systeme.
2. Einführungsbeispiel Wärmespannung im beidseitig gehaltenen Stab (S. 1–5): Statik allein unzureichend → Verformungsbetrachtung $u(x) = \int(\frac{N}{EA} + \alpha\Delta T)dx$ mit Randbedingungen; allgemeine Abzählregel (Gleichungen aus Rand-/Übergangsbedingungen = Grad der statischen Unbestimmtheit + Integrationskonstanten); physikalische Deutung $\varepsilon_{el} = -\varepsilon_{th}$; Zahlenbeispiel (Spannung über Fließgrenze).
3. Starrer Balken an zwei Stäben + Festlager (S. 5–9): Zwangsbedingung über Starrkörperdrehung, Linearisierung (kleine Winkel, Tangente statt Kreisbahn), Projektion der Verschiebung auf Stabachse.
4. „Kochrezept" (S. 9): Statik → Kinematik → Materialgesetz → Gleichungssystem lösen.
5. Last an drei Seilen mit Gegengewicht (S. 9–11): Verträglichkeit $\Delta L_1 = \Delta L_2$.
6. Übungen Zug/Druck (S. 11–16): Stab unter Eigengewicht (Linienlast, veränderliche Normalkraft, Integration von $\varepsilon(x)$), statisch bestimmter Stabzweischlag mit Seil (Bemessung, Längenänderungen, Seilquerschnitt, Verschiebungsfeld, Seilmasse).

**Definitionen / Begriffe**
- Statisch unbestimmt: mehr unbekannte Reaktionen als Gleichgewichtsbedingungen; Grad = Differenz.
- Verformungs-/Zwangsbedingung (Kinematik), Randbedingungen $u(0)$, $u(L)$, Integrationskonstante.
- Wärmespannung $\sigma = -\alpha\Delta T E$ (bei vollständiger Dehnungsbehinderung, unabhängig von $L$, $A$).
- Linienlast aus Eigengewicht $q = \rho g A$.

**Rechenschemata**
- Kochrezept: (1) Gleichgewicht am Freikörperbild (Stabkräfte als Zug ansetzen), Unbekannte vs. Gleichungen zählen; (2) Kinematik: Verschiebungsplan, kleine Verschiebungen, Zwangsbedingungen zwischen Verschiebungen und Stablängenänderungen ($\Delta L = u\cdot\cos\angle(u,\text{Stabachse})$); (3) Materialgesetz $\Delta L_i = N_iL_i/(E_iA_i)$ (ggf. $+\alpha\Delta T L$); (4) in Verträglichkeit einsetzen → fehlende Gleichung, Gleichungssystem lösen, rückwärts einsetzen.
- Alternativ (Feldansatz): $u(x) = \int\varepsilon\,dx$ mit $\varepsilon = N/(EA) + \alpha\Delta T$, Konstanten über Randbedingungen.
- Bemessung: $|\sigma| \le \sigma_{zul}$ je Stab, kleinster zulässiger Wert maßgebend.

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| Einführung | Stab zwischen zwei starren Wänden, gleichmäßig erwärmt (1-fach stat. unbest.) | $L$, $EA$, $\Delta T$, $\alpha$ | $F_A = \alpha\Delta T EA$, $F_B = -\alpha\Delta T EA$, $\sigma = -\alpha\Delta T E$, $u(x) = 0$ | 1–4 |
| Zahlenwerte | wie oben, Stahl | $\alpha = 1{,}2\cdot10^{-5}$/K, $E = 210.000$ N/mm², $\Delta T = 100$ K, $\sigma_{F0} = 240$ N/mm² | $\sigma = -252$ N/mm² ($> \sigma_{F0}$) | 5 |
| ① | starrer Balken $2L$, Festlager $A$ rechts, senkrechter Stab 1 (Länge $L$) links, schräger Stab 2 ($\sqrt5L$) zur Mitte, Last $F$ links | $F$, $L$, $EA$ gleich | $F_{S2} = 0{,}184F$, $F_{S1} = -0{,}92F$, $F_{AH} = -0{,}082F$, $F_{AV} = -0{,}084F$ [korrekt: $-0{,}082F$] | 5–9 |
| ② | Last in seitlich geführtem Kasten an zwei Seilen + Seil über Rolle mit Gegengewicht | $F = 8$ kN, $F_G = 5$ kN, $L_1 = 60$ cm, $L_2 = 30$ cm, $A_1 = 36$ mm², $A_2 = 12$ mm² | $F_{S2} = 1200$ N, $F_{S1} = 1800$ N | 9–11 |
| Übung ① | hängender Rundstab unter Eigengewicht + Endlast | $F = 40$ kN, $L = 4$ m, $E = 210.000$ N/mm², $\rho = 7850$ kg/m³, $\sigma_{zul} = 200$ N/mm² | a) $d \ge 15{,}97$ mm; b) $\Delta L = 3{,}79$ mm (mit/ohne Eigengewicht) | 11–13 |
| Übung ② | Stabzweischlag an Wand (Stab 1 schräg, Stab 2 waagerecht, $\alpha = 30°$) mit Seil 3 und Masse | $L = 3$ m, $E = 210.000$ N/mm², $\rho = 7{,}86$ g/cm³, $A_1 = 11$ cm², $A_2 = 20{,}4$ cm², $\sigma_{zul,1,2} = 160$, $\sigma_{zul,3} = 450$ N/mm², $L_3 = 1$ m | $F_{S1} = 2mg$, $F_{S2} = -\sqrt3mg$; $m_{max} = 8970$ kg; $\Delta L_1 = 4{,}57$ mm, $\Delta L_2 = -1{,}85$ mm; $A_3 \ge 195{,}5$ mm²; $\Delta L_3 = 2{,}14$ mm; $m_3 = 1{,}54$ kg (0,017 %) | 13–16 |

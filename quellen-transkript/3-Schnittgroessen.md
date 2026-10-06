# Technische Mechanik – Statik: 4. Schnittgrößen (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen
Quelle: `Quellen/Vorlesung-2013/3-Schnittgrößen.pdf` (23 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten/Schnittgrößen, Grün = Bemaßungen, Bereiche, Kommentare, Korrekturen.
- Durchgestrichene Zwischenwerte (Rechenfehler, im Original korrigiert) werden nur erwähnt, wenn sie inhaltlich relevant sind.
- Unsichere Lesungen sind mit [?] markiert.

---

## Seite 1

# 4. Schnittgrößen

### 4.1 Definition

- bisher: Schnitte durch Lager, ~~Tragwe~~ Stäbe

> Skizze: Links ein Balken auf zwei Lagern (links Festlager, rechts Loslager), grün umrandet (Freischnitt des ganzen Trägers). Darunter derselbe Balken freigeschnitten mit roten Lagerreaktionen (links horizontal →, vertikal ↑; rechts vertikal ↑). Rechts ein Knoten eines Stabwerks/Fachwerks (zwei Stäbe, an der Wand gelagert), Knoten grün umkreist; darunter der freigeschnittene Knoten mit zwei roten Stabkräften.

$\Rightarrow$ wirkende Kräfte sichtbar machen

---

- Schnitte durch Tragwerke (Balken, Stäbe im Folgenden) ermöglichen die Betrachtung der inneren Beanspruchungen
  $\to$ Ort der max. Beanspruchung?
- $\curvearrowright$ im allgemeinen Fall werden im Tragwerk Kräfte und Momente erzeugt durch die Wirkung der Bewegungsfreiheitsgrade (wie bei Einspannung)

> Skizze: Kragbalken, links eingespannt, am freien Ende schräge Kraft $F$ (rot). Zwei grüne Freischnitt-Umrandungen: I = ganzer Balken (Schnitt durch das Lager), II = Schnitt im Balken.
> – „I Lager": freigeschnittener Balken mit Einspannreaktionen $F_{AH}$ (←/→ horizontal), $F_{AV}$ (vertikal ↑), Einspannmoment $M$ (Drehpfeil), am Ende $F$.
> – „II Schnittgrößen": Balkenstück rechts vom Schnitt; am Schnittufer (linkes Ende des Reststücks, also negatives Schnittufer) $N$ (horizontal), $Q$ (vertikal), $M_B$ (Drehpfeil); am Ende $F$.

---

> Skizze: Räumlicher Balkenausschnitt (T-förmiger Querschnitt [?]) mit Schnittfläche, auf der viele rote Pfeile (verteilte Spannungen) eingezeichnet sind. Rote Beschriftung: „Schnittkraft sind die Resultierenden im Querschnitt".

Schnittgrößen (rechte Spalte, Bezeichnungen $F_N$, $F_Q$ durchgestrichen und ersetzt durch $N$, $Q$):

- $N$ – Normalkraft: senkrecht auf Schnittebene
- $Q$ – Querkraft (parallel zur Schnittebene, in Ebene)
- $M_B$ – Biegemoment / Schnittmoment

---

## Seite 2

> Skizze: Einfeldträger A–B, links in A Festlager [?] (gezeichnet als Lager mit Schraffur), rechts in B Loslager. Trapez-/Dreieckslast (rot) von links nach rechts zunehmend bis $q_0$ am rechten Ende. Koordinate $x$ ab A nach rechts (Pfeil). Ein grüner Freischnitt umschließt den linken Teil des Trägers (Schnitt an beliebiger Stelle $x$).

> Skizze: Beide Teilsysteme nach dem Schnitt:
> – Linkes Teilsystem (A bis Schnitt, Länge $x$): am rechten Schnittufer $M_B$ (Drehpfeil, im Uhrzeigersinn [?]), $N$ ($F_N$ durchgestrichen) nach rechts (→, aus dem Schnittufer heraus = Zug), $Q$ ($F_Q$) nach unten (↓). Pfeil zeigt auf dieses Ufer: **„positives Schnittufer" (auf Koordinaten-Seite)**, d. h. die Schnittfläche, deren äußere Normale in Richtung $+x$ zeigt.
> – Rechtes Teilsystem (Schnitt bis B): am linken Schnittufer $M_B$ entgegengesetzt drehend, $N$ nach links (←, ebenfalls Zug), $Q$ nach oben (↑). Bezeichnet als **„negatives Schnittufer"**.

- Schnittgrößen werden wie Lagerreaktionen in Gleichgewichtsbed. behandelt
  - $\curvearrowright$ Lösen, wenn erkennbar, am einfachsten Schnitt
- Schnittgrößen sind Funktionen von $x$ ($f(x)$)
  - $\curvearrowright$ Unstetigkeiten werden durch Unterteilung in Bereiche aufgelöst

Vorzeichenkonvention (rot, rechte Spalte):

- $N$ ($F_N$) immer als Zugkraft (vgl. Fachwerk)
- $Q$: $\downarrow$ am pos. Schnittufer, $\uparrow$ am neg. Schnittufer
- $M_B$ immer so, dass untere Faser (d. Trägers) auf Zug beansprucht wird

> Skizze (blau umrahmt): Diagramm $y$ über $f$ [?]: eine Funktion mit Sprung/Knick (Treppenstufe) rot durchgestrichen (✗), daneben eine glatte, stetige Kurve mit grünem Haken (✓) – Illustration: innerhalb eines Bereichs müssen die Schnittgrößen stetige Funktionen sein, Unstetigkeiten → neue Bereiche.

---

## Seite 3

- Unterteilung in Bereiche (neue Koordinate)

> Skizze: Einfeldträger mit Festlager links, Loslager rechts, Einzelkraft $F$ (rot, ↓) etwa in Feldmitte. Grüne Freischnitte: I (Schnitt links von $F$, Koordinate $x_1$ ab linkem Lager) und II (Schnitt rechts von $F$, Koordinate $x_2$ ab Lastangriffspunkt von $F$).

$\to$ neuer Bereich wenn:

- Ⓐ – Trägeranfang
- Ⓑ – Einleitungsstellen von Einzelkräften und -momenten
- Ⓒ – Beginn/Ende von Streckenlasten
- Ⓓ – Stelle ~~oder~~ Unstetigkeit der Streckenlast
- Ⓔ – Lager
- Ⓕ – Ecke, Verzweigung

(Zusatz links neben Ⓔ: „pf. im Gleichgewicht" [?] – sinngemäß: an den Bereichsgrenzen/Lagern …)

- $\curvearrowright$ jeder Bereich mit 3 Gleichgewichtsbed. $\to$ Schnitt
- $\curvearrowright$ Schnittgrößen gelten nur innerhalb des Bereiches

> Skizze: Rahmenartiges System: horizontaler Träger, links Festlager (Punkt Ⓐ, Trägeranfang), rechts Ecke Ⓕ, von dort vertikaler Stiel nach unten, der in einen gekrümmten Bogen (Viertelkreis, Radius $r$, Winkel $\varphi$) übergeht und unten auf einem Lager endet. Lasten (rot): Streckenlast $q(x)$ auf kurzem Abschnitt (Ⓒ Beginn/Ende), schräge Einzelkraft $F$ (Ⓑ), Einzelmoment $M$ (Ⓑ). Für jeden Bereich lokale Koordinaten (grün): $x_1 \dots x_5$ jeweils nach rechts entlang des Trägers, $z_1 \dots z_5$ jeweils nach unten; im Stiel $x_6$ nach unten, $z_6$ nach links (zur Innenseite); im Bogen $x_7$ entlang der Bogenachse, $z_7$ [?] radial. Unter dem Träger sind die Bereiche mit ihren Koordinatenursprüngen ($x_i \to$, $z_i \downarrow$) nochmals nebeneinander gezeichnet.

---

## Seite 4

### 4.2 Verfahrensweise zur Berechnung der Schnittgrößen eines Tragwerks („Kochrezept")

1. Ermittlung der Lager- und Verbindungsreaktionen
2. Einteilung in Bereiche / Festlegung KOS (Koordinatensystem)
3. Schnitte an beliebiger Stelle $x_i$ innerhalb des $i$-ten Bereiches
   $\to$ Gleichgewichtsbedingungen $\to$ Schnittkräfte als $f(x_i)$
   (Schleife: für $i = 1$ bis $n$)
4. $\to$ Berechnung der Schnittkräfte an bestimmten Orten
   $\to$ grafische Darstellung der Schnittkraftverläufe

---

## Seite 5

### Beispiel: Gerader Träger mit Einzelkräften

> Skizze: Einfeldträger mit Kragarm. A links: Festlager; B: Loslager. Bemaßung (grün): $a$ (A bis Angriffspunkt $F_1$), $2a$ ($F_1$ bis B), $a$ (B bis freies Ende). $F_1$ schräg unter Winkel $\alpha$ nach links unten wirkend (Pfeil von rechts oben nach links unten), $F_2$ senkrecht ↓ am freien Kragarmende.

geg.: $F_1 = 2000\,\mathrm{N}$, $F_2 = 500\,\mathrm{N}$, $a = 1\,\mathrm{m}$, $\alpha = 30^\circ$
ges.: Verläufe der Schnittkräfte

**Lös.:** ① Lagerreaktionen

> Skizze: Freigeschnittener Träger: $F_{AH}$ → (horizontal nach rechts) und $F_{AV}$ ↑ in A, $F_B$ ↑ in B, $F_1$ schräg, $F_2$ ↓.

$\to: \; F_{AH} - F_1\cos\alpha = 0 \quad\Rightarrow\quad F_{AH} = F_1\cos\alpha = 1732{,}0\,\mathrm{N}$

$\uparrow: \; F_{AV} + F_B - F_1\sin\alpha + F_2 = 0$ [Vorzeichen bei $F_2$ im Original so notiert; korrekt wäre $-F_2$, das Ergebnis unten rechnet mit $-F_2$]

$\curvearrowleft A: \; -F_1\, a \sin\alpha + 3a\,F_B - 4a\,F_2 = 0 \quad\Rightarrow\quad F_B = \tfrac{1}{3}(F_1\sin\alpha + 4F_2) = 1000\,\mathrm{N}$

$\Rightarrow F_{AV} = F_1\sin\alpha + F_2 - F_B = +500\,\mathrm{N}$

② Bereiche

> Skizze: Träger mit Reaktionen $F_{AH}$, $F_{AV}$, $F_B$ und Lasten $F_1$, $F_2$. Grüne Freischnitte I, II, III (verschachtelt, jeweils vom linken Ende aus). Koordinaten: $x_1$ ab A, $x_2$ ab Angriffspunkt $F_1$, $x_3$ ab B, jeweils nach rechts. Unten: Bereiche 1., 2., 3. mit geschweiften Klammern.

- 1. Bereich: $0 \le x_1 \le a$
- 2. Bereich: $0 \le x_2 \le 2a$
- 3. Bereich: $0 \le x_3 \le a$

---

## Seite 6

③ Schnittreaktionen

**1. Bereich** ($0 \le x_1 \le a$)

> Skizze: Links Teilsystem I: $F_{AH}$ →, $F_{AV}$ ↑ in A, Koordinate $x_1$; am rechten (positiven) Schnittufer $N(x_1)$ →, $Q(x_1)$ ↓, $M(x_1)$ Drehpfeil. Rechts das Restsystem mit negativem Schnittufer: $N(x_1)$ ←, $Q(x_1)$ ↑, $M(x_1)$ gegensinnig, dazu $F_1$, $F_B$, $F_2$.

Gleichgewicht am linken System:

$\to: \; F_{AH} + N(x_1) = 0 \;\Rightarrow\; N(x_1) = -F_{AH}$ (konstant)

$\uparrow: \; F_{AV} - Q(x_1) = 0 \;\Rightarrow\; Q(x_1) = F_{AV}$ (konstant)

$\curvearrowleft S: \; M(x_1) - F_{AV}\,x_1 = 0 \;\Rightarrow\; M(x_1) = F_{AV}\,x_1$ (lin. Fkt.)

(grüner Hinweis: Momentenbilanz stets um Schnittpunkt $S$)

$\Rightarrow M(0) = 0$!, $\; M(a) = F_{AV}\cdot a$!

**2. Bereich** ($0 \le x_2 \le 2a$)

> Skizze: Linkes Teilsystem: $F_{AH}$, $F_{AV}$ in A, Abstand $a$ bis $F_1$, Koordinate $x_2$ ab $F_1$; am pos. Schnittufer $N(x_2)$ →, $Q(x_2)$ ↓, $M(x_2)$. Rechtes Teilsystem mit $N(x_2)$ ←, $Q(x_2)$ ↑, $M(x_2)$, $F_B$, $F_2$. Grün: „linkes Teilsystem".

$\to: \; F_{AH} - F_1\cos\alpha + N(x_2) = 0$

$\uparrow: \; F_{AV} - F_1\sin\alpha - Q(x_2) = 0$

$\curvearrowleft S: \; M(x_2) + F_1\sin\alpha\, x_2 - F_{AV}(a + x_2) = 0$

---

## Seite 7

$\Rightarrow N(x_2) = F_1\cos\alpha - F_{AH} = 0$ (konst. Wert)

$\Rightarrow Q(x_2) = F_{AV} - F_1\sin\alpha$ (konst. Wert)

$\Rightarrow M(x_2) = F_{AV}(a + x_2) - F_1\sin\alpha\, x_2 = F_{AV}\,a + F_{AV}\,x_2 - F_1\sin\alpha\,x_2 = (F_{AV} - F_1\sin\alpha)\,x_2 + F_{AV}\,a$ (lin. Fkt.)

$M(x_2 = 0) = F_{AV}\,a$
$M(x_2 = 2a) = F_{AV}\,3a - F_1\sin\alpha\,2a$

**3. Bereich** ($0 \le x_3 \le a$)

> Skizze: Ganzer Träger links mit $F_{AH}$, $F_{AV}$, $F_1$, $F_B$, Koordinate $x_3$ ab B; am pos. Schnittufer $N(x_3)$, $Q(x_3)$, $M(x_3)$. Rechts das kurze Reststück (Länge $a - x_3$) mit $F_2$ ↓ am Ende und am negativen Schnittufer $N(x_3)$ ←, $Q(x_3)$ ↑, $M(x_3)$. Grün: „rechtes Teilsystem" (es wird das rechte Teilsystem betrachtet).

$\to: \; -N(x_3) = 0 \;\Rightarrow\; N(x_3) = 0$ (konst. Wert)

$\uparrow: \; Q(x_3) - F_2 = 0 \;\Rightarrow\; Q(x_3) = F_2$ (konst. Wert)

$\curvearrowleft S: \; -M(x_3) - F_2(a - x_3) = 0 \;\Rightarrow\; M(x_3) = -F_2(a - x_3)$ (lin. Fkt.)

$M(x_3 = 0) = -F_2\,a$
$M(x_3 = a) = 0$

---

## Seite 8

④ Grafische Darstellung

> Skizze: Oben der Träger (Festlager A links, Loslager B, $F_1$ schräg, $F_2$ am Kragende) mit Bereichsgrenzen (gestrichelte Senkrechte) „Bereich 1", „2", „3". Darunter drei Diagramme, jeweils mit vertikaler Achse (Pfeil nach oben; grüne Notiz: „Angabe der Richtung") und Werten:
> – **N-Verlauf**: Bereich 1 konstant $-F_{AH} = -1732\,\mathrm{N}$ (rot schraffiert, unterhalb der Achse); Bereiche 2 und 3: $0$.
> – **Q-Verlauf**: Bereich 1 konstant $F_{AV} = 500\,\mathrm{N}$ (oberhalb); Bereich 2 konstant $F_{AV} - F_1\sin 30^\circ = -500\,\mathrm{N}$ (unterhalb); Bereich 3 konstant $F_2 = 500\,\mathrm{N}$ (oberhalb). Sprünge an den Kraftangriffspunkten. (Ein erster, falscher Verlauf im Bereich 1 – Wert ca. $-1500$ [?] – ist durchgestrichen.)
> – **M-Verlauf**: linear von $0$ (A) auf $F_{AV}\,a = 500\,\mathrm{Nm}$ ($\oplus$, oberhalb der Achse) bei $F_1$, dann linear fallend auf $F_{AV}\,3a - F_1\sin\alpha\,2a = -500\,\mathrm{Nm}$ ($\ominus$, unterhalb) über B, dann linear auf $0$ am Kragende. Notiz rechts: $-F_2\cdot a$.
> Positive Werte werden in diesen Diagrammen **oberhalb** der Achse aufgetragen.

---

## Seite 9

### 4.3 Differentielle Zusammenhänge der Schnittgrößen: Streckenlast, Querkraft, Moment

- Betrachtung der Beziehungen zwischen $q(x)$, $Q(x)$ und $M(x)$ an einem differentiell kleinen Balkenabschnitt

> Skizze: Einfeldträger (Fest-/Loslager) mit beliebiger Streckenlast $q(x)$ (rot, nach unten); bei $x$ ein Element der Länge $dx$ herausgeschnitten (grün markiert). Pfeil nach unten zum vergrößerten Element:
> Balkenelement der Länge $dx$ mit $q(x)$ (Annahme: konstant über $dx$), nach unten gerichtet. Linkes (negatives) Schnittufer bei $S_1$: $N(x)$ ←, $Q(x)$ ↑, $M(x)$ Drehpfeil. Rechtes (positives) Schnittufer bei $S_2$: $N(x+dx)$ →, $Q(x+dx)$ ↓, $M(x+dx)$ Drehpfeil. Bemaßung $dx/2$ + $dx/2$.

- $\curvearrowright$ $M$ und $Q$ ändern sich über $dx$:

$M(x+dx) = M(x) + dM(x)$
$Q(x+dx) = Q(x) + dQ(x)$

$\Rightarrow$ Gleichgewichtsbedingungen liefern:

$\uparrow: \; Q(x) - \big(Q(x) + dQ(x)\big) - q(x)\,dx = 0$
$\quad -dQ(x) - q(x)\,dx = 0$

$$-q(x) = \frac{dQ(x)}{dx} \qquad (4.3.1)$$

---

## Seite 10

$\curvearrowleft S_2: \; M(x+dx) - M(x) - Q(x)\,dx + q(x)\,dx\cdot\frac{dx}{2} = 0$

$M(x) + dM(x) - M(x) - Q(x)\,dx + q(x)\frac{dx^2}{2} = 0$, wobei $q(x)\frac{dx^2}{2} \to 0$

(grün: $\to$ sehr klein gegenüber anderen Termen durch $dx^2$ $\to$ $dx$ klein, $dx^2 \ll dx$)

$$Q(x) = \frac{dM(x)}{dx} \qquad (4.3.2)$$

($Q(x)$ ist Ableitung des Moments!)

Weiterhin gilt mit 4.3.1 und 4.3.2:

$$-q(x) = \frac{dQ(x)}{dx} = \frac{d^2M(x)}{dx^2} \qquad (4.3.3)$$

Gln. 4.3.1, 4.3.2, 4.3.3: gewöhnliche Differentialgleichungen für $Q(x)$, $M(x)$
$\curvearrowright$ in der Regel leicht integrierbar, wenn $q(x)$ bekannt

---

## Seite 11

### Beispiel: Dreieckslast

> Skizze: Einfeldträger der Länge $L$, links Festlager [?], rechts Loslager [?] (beide als Dreieckslager gezeichnet). Dreieckslast $q(x)$ (rot, nach unten) von $0$ am linken Lager linear auf $q_0$ am rechten Lager. Koordinate $x$ ab linkem Lager nach rechts.

geg.: $q_0$, $L$
ges.: Verlauf $Q$, $M$, $M_{\max}$

$q(x) = \frac{q_0}{L}\,x$

**Lös.:** aus (4.3.1)

$-q(x) = \frac{dQ(x)}{dx} \;\leadsto\; dQ(x) = -q(x)\,dx$

$Q(x) = \int -q(x)\,dx = -\int \frac{q_0}{L}x\,dx = -\frac{q_0}{2}\frac{x^2}{L} + C_1$

aus (4.3.2)

$Q(x) = \frac{dM(x)}{dx} \;\leadsto\; dM(x) = Q(x)\,dx$

$M(x) = \int Q(x)\,dx = \int\left[-\frac{q_0}{L}\frac{x^2}{2} + C_1\right]dx$

$M(x) = \underbrace{-\frac{q_0}{L}\frac{x^3}{6}}_{\text{partielle Lösung}} + \underbrace{C_1 x + C_2}_{\text{homogene Lösung}}$ der DGL

---

## Seite 12

- Lösen der Integrationskonstanten $C_1$ und $C_2$ durch Randbedingungen (RB) für $Q$, $M$

RB für $M$:
$M(x=0) \overset{!}{=} 0 \;\leadsto\; C_2 = 0$
$M(x=L) \overset{!}{=} 0 \;\leadsto\; 0 = -\frac{q_0 L^2}{6} + C_1 L \;\Rightarrow\; C_1 = \frac{q_0}{6}L$

$\curvearrowright$ Lösung der Schnittgrößen:

$$Q(x) = -\frac{q_0 x^2}{2L} + \frac{q_0 L}{6}$$
$$M(x) = -\frac{q_0 x^3}{6L} + \frac{q_0 L}{6}x$$

- $Q$ ist Ableitung von $M$
  $\to$ $M$ ist maximal, wo $Q$ Nullstelle hat!

$Q(x_0) = 0 = -\frac{q_0 x_0^2}{2L} + \frac{q_0 L}{6}$
$\frac{q_0 x^2}{2L} = \frac{q_0 L}{6}$
$x_0 = \sqrt{\frac{2L^2}{6}} = \sqrt{\frac{1}{3}}\,L$

$\curvearrowright$ lokales Max.-Moment (zuerst „Minimum" geschrieben, durchgestrichen) an der Stelle $x_0 = \sqrt{\tfrac13}\,L$ $\;\to f''(x)$? [Hinweis auf Prüfung mit 2. Ableitung]

---

## Seite 13

> Skizze: Oben Träger mit Dreieckslast bis $q_0$. Darunter:
> – **Q-Verlauf**: Parabel, beginnt bei $\frac{q_0 L}{6}$ (oberhalb der Achse), Nullstelle bei $x_0$, endet bei $-\frac{q_0 L}{3}$ (unterhalb).
> – **M-Verlauf**: kubische Kurve, $0$ an beiden Enden, Maximum $M_{\max}$ bei $x_0$ (gestrichelte Verbindungslinie von der Q-Nullstelle zu $M_{\max}$); positiv, oberhalb der Achse aufgetragen.

$M_{\max} = M(x_0) = -\frac{q_0 x_0^3}{6L} + \frac{q_0 L}{6}x_0 = -\frac{q_0\left(\sqrt{\tfrac13}\right)^3 L^3}{6L} + \frac{q_0 L}{6}\sqrt{\tfrac13}\,L$
$= q_0 L^2\left(-\frac{(1/3)^{3/2}}{6} + \frac{\sqrt{1/3}}{6}\right)$ [Minuszeichen im Original in der Klammer schwer erkennbar]
$\approx 0{,}128\, q_0 L^2$ [?] (rechnerisch ergibt sich $\frac{q_0L^2}{9\sqrt3} \approx 0{,}064\,q_0L^2$; der notierte Wert 0,128 entspricht dem Doppelten)

---

- im Vergleich: Normale (statt „Alternative", durchgestrichen) Ermittlung der Schnittkräfte

> Skizze: Träger Länge $L$ mit Dreieckslast $q(x) = \frac{q_0}{L}x$ bis $q_0$; links Lagerkraft $F_A$ ↑, rechts $F_{BH}$ (←) und $F_{BV}$ ↑. Grüner Freischnitt ③ am linken Ende, Koordinate $x$.

① $F_{BH} = 0$, $\; F_{BV} = \frac{q_0 L}{3}$, $\; F_A = \frac{q_0 L}{6}$

② ein Bereich

---

## Seite 14

③

> Skizze: Linkes Teilsystem (Länge $x_1$) mit Teil der Dreieckslast (bis $q(x) = \frac{q_0}{L}x$), $F_A$ ↑, am pos. Schnittufer $N(x)$ →, $Q(x)$ ↓, $M(x)$. Rechtes Teilsystem mit Rest der Last, negatives Schnittufer $N(x)$ ←, $Q(x)$ ↑, $M(x)$, sowie $F_{BH}$ ←, $F_{BV}$ ↑.
> Darunter Ersatzsystem: Resultierende $F_q$ ↓ im Abstand $\frac23 x_1$ von A bzw. $\frac13 x_1$ vom Schnitt; $F_A$ ↑; am Schnitt $N(x)$, $Q(x)$, $M(x)$.

$F_q = \frac12 \cdot q_0^* L^* = \frac12\frac{q_0}{L}x^2 = \frac{x^2}{2}\frac{q_0}{L}$ (mit $q_0^* = \frac{q_0}{L}x$, $L^* = x$)

$\to: \; N(x) = 0$

$\uparrow: \; F_A - F_q - Q(x) = 0$

$Q(x) = F_A - F_q = \frac{q_0 L}{6} - \frac{x^2}{2}\frac{q_0}{L}$

$\curvearrowleft S: \; M(x) + F_q\,\tfrac13 x - F_A\,x = 0$

$M(x) = F_A\,x - F_q\,\tfrac13 x = \frac{q_0 L}{6}x - \frac{x^2}{2}\frac{q_0}{L}\frac13 x$

$$M(x) = \frac{q_0 L}{6}x - \frac{x^3}{6}\frac{q_0}{L}$$

(Ergebnis identisch mit der Integration über die Differentialbeziehungen.)

---

## Seite 15

### Übung, Bsp. Ⓐ [?] (eingekreistes Zeichen, evtl. „4"): Linienlast $q(x)$ nichtlinear

> Skizze: Einfeldträger Länge $L$, links Festlager [?], rechts Loslager. Parabelförmige Streckenlast (rot, nach unten), Null an beiden Enden, Maximum $q_0$ in Feldmitte. Koordinate $x$ ab linkem Lager nach rechts; grün eine $z$-Achse am linken Lager **nach oben** gezeichnet mit rotem „+" darüber [?] (vermutlich Auftragsrichtung der Lastfunktion; unterhalb des Lagers grünes Gekritzel – evtl. Korrektur der z-Richtung [?]).

$q(x) = \left(-\frac{x^2}{L^2} + \frac{x}{L}\right)4q_0$

geg.: $q(x)$, $L$
ges.: Verlauf $Q$, $M$, $M_{\max}$

**Lös.:** aus (4.3.1)

$dQ(x) = -q(x)\,dx \quad |\int$

$Q(x) = \int -q(x)\,dx = 4q_0\int\left(\frac{x^2}{L^2} - \frac{x}{L}\right)dx$

$Q(x) = 4q_0\left(\frac{x^3}{3L^2} - \frac{x^2}{2L}\right) + C_1$

aus (4.3.2)

$dM(x) = Q(x)\,dx \quad |\int$

$M(x) = \int Q(x)\,dx = \int\left[4q_0\left(\frac{x^3}{3L^2} - \frac{x^2}{2L}\right) + C_1\right]dx$

$M(x) = 4q_0\left(\frac{x^4}{12L^2} - \frac{x^3}{6L}\right) + C_1 x + C_2$

RB für $M$:
$M(0) \overset{!}{=} 0 \;\leadsto\; C_2 = 0$
$M(x=L) \overset{!}{=} 0 \;\leadsto\; 4q_0\left(\frac{L^4}{12L^2} - \frac{L^3}{6L}\right) + C_1 L = 0$

$C_1 = \left(\frac{L}{6} - \frac{L}{12}\right)4q_0 = \frac{L}{12}4q_0 = \frac{L}{3}q_0$

---

## Seite 16

$\curvearrowright$
$$Q(x) = 4q_0\left(\frac{x^3}{3L^2} - \frac{x^2}{2L}\right) + \frac{L}{3}q_0$$
$$M(x) = 4q_0\left(\frac{x^4}{12L^2} - \frac{x^3}{6L}\right) + \frac{q_0 L}{3}x$$

(eine zuerst ohne Vorfaktoren notierte Version ist durchgestrichen)

$Q(x_0) \overset{!}{=} 0 \to M_{\max}$

$0 = 4q_0\left(\frac{x^3}{3L^2} - \frac{x^2}{2L}\right) + \frac{Lq_0}{3} \quad |:q_0 \quad \to$ bestimmen

Raten: $x_0 = 0{,}5\,L$

$\curvearrowright 0 = 4\left(\frac{1}{8}\frac{L^3}{3L^2} - \frac14\frac{L^2}{2L}\right) + \frac{L}{3} = 4\left(\frac{1}{24}L - \frac18 L\right) + \frac L3 = -\frac{4}{12}L + \frac L3 = 0 \;✓$

$\frac{dQ(x)}{dx} = Q'(x)\;(= M''(x)) = 4q_0\left(\frac{x^2}{L^2} - \frac{x}{L}\right) = -q(x) \;\to$ negativ $\curvearrowright$ Maximum

$M_{\max} = M(x_0) = 4q_0\left(\frac{L^4}{16\cdot 12L^2} - \frac{L^3}{8\cdot 6L}\right) + \frac{q_0 L}{3}\frac12 L = \frac{11}{48}q_0L^2$ [?] (Nachrechnung ergibt $\frac{5}{48}q_0L^2$; notierter Wert gut lesbar „11/48")

---

## Seite 17

> Skizze: Träger mit parabelförmiger Last $q(x)$. Darunter:
> – **Q-Verlauf**: von $\frac{L}{3}q_0$ (oberhalb) über Nullstelle in Feldmitte auf $-\frac{L}{3}q_0$ (unterhalb), punktsymmetrisch.
> – **M-Verlauf**: symmetrische Kurve, $0$ an den Enden, Maximum $\frac{11}{48}q_0L^2$ in der Mitte, positiv ($\oplus$), oberhalb der Achse.

$Q(0) = \frac{L}{3}q_0$
$Q(L) = 4q_0\left(\frac L3 - \frac L2\right) + \frac L3 q_0 = -\frac L3 q_0$
$M(0) = 0$, $\; M(L) = 0$

---

(rechts oben: „Übung 7 / 7.10" [?])

### Beispiel Ⓑ: Rahmen mit Gelenk

> Skizze: Ebener Rahmen. Linker Stiel: unten Festlager A, Höhe $12a$ bis zur linken oberen Ecke. Dort horizontale Einzelkraft $F$ (rot, → nach rechts) an der Ecke. Riegel von der Ecke $4a$ nach rechts bis Gelenk G. Rechter Riegelteil $8a$ von G bis zur rechten Ecke, belastet mit konstanter Streckenlast $q_0$ (rot, ↓) über die ganzen $8a$. Rechter Stiel von der rechten Ecke $8a$ nach unten zum Festlager B. (Bemaßungen grün: $12a$, $4a$, $8a$ horizontal, $8a$ vertikal.) Beide Lager sind zweiwertig → Dreigelenkrahmen.

geg.: $F$, $q_0$, $a$; $\; F = 2q_0 a$
ges.: $N(x_i)$, $Q(x_i)$, $M(x_i)$

**Lös.:** ① Lagerreaktionen $\to$ Gelenk (Gerberträger)!

> Skizze: Linkes Teilsystem (grün beschriftet): Stiel + Riegel bis G; $F$ →, in A $F_{AH}$ → und $F_{AV}$ ↑; in G $G_H$ → und $G_V$ ↑.

$\to: \; G_H + F + F_{AH} = 0 \quad (1) \;\to\; F_{AH} = -F - G_H$

$\uparrow: \; F_{AV} + G_V = 0 \quad (2) \;\to\; F_{AV} = -G_V$

$\curvearrowleft G: \; F_{AV}\cdot 4a - F_{AH}\cdot 12a = 0 \quad (3)$

$\Rightarrow -G_V\,4a - (-F - G_H)\,12a = 0 \quad (7)$

---

## Seite 18

> Skizze: Rechtes Teilsystem (grün beschriftet): Riegel von G ($8a$) mit $q_0$ und rechter Stiel; in G (Gegenkräfte) $G_H$ ← und $G_V$ ↓; in B $F_{BH}$ ← und $F_{BV}$ ↑.

$\to: \; -G_H - F_{BH} = 0 \quad (4)$

$\uparrow: \; F_{BV} - G_V - q_0\cdot 8a = 0 \quad (5)$

$\curvearrowleft G: \; 4a\cdot q_0\,8a - F_{BV}\cdot 8a + F_{BH}\cdot 8a = 0 \quad (6)$

$F_{BH} = -G_H$, $\; F_{BV} = G_V + q_0 8a$ $\;\leadsto$ in (6):

$4a\,q_0\,8a - (G_V + q_0 8a)\,8a - G_H\,8a = 0 \quad (8)$

$4a\,q_0 - G_V - q_0 8a - G_H = 0$

Gleichungssystem:
$-4a\,q_0 - G_V - G_H = 0 \quad (10)$
(7): $\; F - \frac{G_V}{3} + G_H = 0 \quad (11)$

$\downarrow$
(11): $G_V = (G_H + F)\,3$
in (10): $-4a\,q_0 - 3G_H - 3F - G_H = 0$

$G_H = -\frac{3F}{4} - a q_0 = -\frac{3\cdot 2q_0a}{4} - aq_0$

$G_H = -\frac52 a q_0$

$\curvearrowright F_{BH} = \frac52 a q_0$
$\curvearrowright G_V = -\frac32 a q_0$
$\curvearrowright F_{BV} = 6{,}5\,a q_0$
$\curvearrowright F_{AV} = \frac32 a q_0$
$\curvearrowright F_{AH} = -F - G_H = -2q_0a + \frac52 aq_0$, $\; F_{AH} = 0{,}5\,aq_0$

(zahlreiche ursprüngliche Werte grün/blau durchgestrichen und korrigiert)

---

## Seite 19

> Skizze: Rahmen mit allen Reaktionen: A: $0{,}5\,q_0a$ (→), $\frac32 aq_0$ (↑); B: $\frac52 q_0 a$ (←), $6{,}5\,q_0a$ (↑); $F = 2q_0a$ → an der linken Ecke; $q_0$ auf dem rechten Riegel. Bereiche (grüne Freischnitte) und Koordinaten:
> – I: linker Stiel, $x_1$ ab A **nach oben**
> – II: linker Riegel, $x_2$ ab linker Ecke nach rechts
> – III: rechter Riegel, $x_3$ ab Gelenk G nach rechts
> – IV: rechter Stiel, $x_4$ ab rechter Ecke **nach unten**

Bereiche:
$0 \le x_1 \le 12a$, $\; 0 \le x_2 \le 4a$, $\; 0 \le x_3 \le 8a$, $\; 0 \le x_4 \le 8a$

**Ⓘ** $0 \le x_1 \le 12a$

> Skizze: Stielstück unten mit A: $0{,}5\,aq_0$ →, $\frac32 aq_0$ ↑. Am Schnitt (oben, positives Ufer bzgl. $x_1$): $N(x_1)$ ↑ (Zug, aus dem Schnitt heraus), $Q(x_1)$ → (Richtung $z_1$, zur Rahmeninnenseite), $M(x_1)$. Lokales KOS grün: $x_1$ nach oben, $z_1$ nach rechts.

$\to: \; Q(x_1) + \frac12 q_0a = 0 \;\Rightarrow\; Q(x_1) = -\frac12 q_0 a$

$\uparrow: \; N(x_1) + q_0 a\frac32 = 0 \;\Rightarrow\; N(x_1) = -\frac32 q_0 a$

$\curvearrowleft S: \; M(x_1) + \frac12 q_0a\cdot x_1 = 0 \;\Rightarrow\; M(x_1) = -\frac12 q_0a\,x_1$

$M(0) = 0$, $\; M(12a) = -6\,q_0a^2$

**Ⓘⓘ** $0 \le x_2 \le 4a$

> Skizze: Linker Stiel + Riegelstück bis Schnitt; $F = 2q_0a$ → an der Ecke; in A $\frac12 q_0a$ →, $\frac32 q_0a$ ↑. Am Schnitt $N(x_2)$ →, $Q(x_2)$ ↓, $M(x_2)$.

$\to: \; N(x_2) + 2q_0a + \frac12 q_0a = 0 \;\Rightarrow\; N(x_2) = -\frac52 q_0a$

$\uparrow: \; -Q(x_2) + \frac32 q_0a = 0 \;\Rightarrow\; Q(x_2) = +\frac32 q_0a$

$\curvearrowleft S: \; M(x_2) + \frac12 q_0a\cdot 12a - \frac32 q_0a\,x_2 = 0$ [Vorzeichen des letzten Terms im Original unklar] $\;\Rightarrow\; M(x_2) = \frac32 q_0a\,x_2 - 6\,q_0a^2$

$M(0) = -6\,q_0a^2$
$M(4a) = +6\,q_0a^2 - 6\,q_0a^2 = 0$! (Gelenk)

---

## Seite 20

**Ⓘⓘⓘ** $0 \le x_3 \le 8a$

> Skizze: Rechtes Teilsystem: Riegelstück der Länge $8a - x_3$ mit $q_0$, rechter Stiel, in B $\frac52 q_0a$ ← und $6{,}5\,q_0a$ ↑. Am negativen Schnittufer $N(x_3)$ ←, $Q(x_3)$ ↑, $M(x_3)$.

$\to: \; -N(x_3) - \frac52 q_0a = 0 \;\Rightarrow\; N(x_3) = -\frac52 q_0 a$

$\uparrow: \; Q(x_3) + 6{,}5\,q_0a - q_0(8a - x_3) = 0 \;\Rightarrow\; Q(x_3) = -q_0x_3 + \frac32 aq_0$ (Vorzeichen von $q_0x_3$ im Original undeutlich; aus den Randwerten folgt $-$)

(rot: $Q(x_0) = 0$ Nullstelle bei $x_0 = \frac32 a$)

$Q(0) = +\frac32 q_0a$, $\; Q(8a) = -q_0 8a + \frac32 q_0a = -6{,}5\,q_0a$

$\curvearrowleft S: \; M(x_3) + q_0(8a - x_3)\frac{(8a - x_3)}{2} + \frac52 q_0a\cdot 8a - 6{,}5\,q_0a(8a - x_3) = 0$

(ein erster Rechenweg mit falschen Zahlen ist komplett durchgestrichen)

$M(x_3) = -\frac{q_0}{2}(8a - x_3)^2 - \frac52 q_0a\cdot 8a + 6{,}5\,q_0a(8a - x_3)$
$= -\frac{q_0}{2}(64a^2 - 16ax_3 + x_3^2) - 20\,q_0a^2 + 52\,q_0a^2 - 6{,}5\,q_0a\,x_3$

$$M(x_3) = -\frac{q_0}{2}x_3^2 + \frac32 q_0a\,x_3$$

$M(0) = 0$ ✓
$M(8a) = -\frac{q_0}{2}64a^2 + \frac32 q_0a\,8a = -20\,q_0a^2$
$M(\tfrac32 a) = -\frac{q_0}{2}\frac94 a^2 + q_0a\frac32 a\frac32 = \frac98 q_0a^2$ (Maximum, rot)

---

## Seite 21

**Ⓘⓥ**

> Skizze: Unteres Stielstück (Länge $8a - x_4$) mit B: $\frac52 q_0a$ ←, $6{,}5\,q_0a$ ↑. Am Schnitt (oberes Ende = negatives Ufer bzgl. $x_4$ nach unten): $N(x_4)$ ↑, $Q(x_4)$ →, $M(x_4)$.

$\to: \; Q(x_4) - \frac52 q_0a = 0 \;\Rightarrow\; Q(x_4) = \frac52 q_0a$

$\uparrow: \; N(x_4) + 6{,}5\,q_0a = 0 \;\Rightarrow\; N(x_4) = -6{,}5\,q_0a$

$\curvearrowleft S: \; M(x_4) + \frac52 q_0a(8a - x_4) = 0 \;\Rightarrow\; M(x_4) = \frac52 q_0a\,x_4 - 20\,q_0a^2$

$M(0) = -20\,q_0a^2$
$M(8a) = \frac52 q_0a\,8a - 20\,q_0a^2 = 0$

Wertetabelle (grün):

| | Bereich 1: $x_1=0$ | $x_1=12a$ | Bereich 2: $0$ | $4a$ | Bereich 3: $0$ | $8a$ | Bereich 4: $0$ | $8a$ |
|---|---|---|---|---|---|---|---|---|
| $N(x)$ | $-\frac32 q_0a$ | $-\frac32 q_0a$ | $-\frac52 q_0a$ | $-\frac52 q_0a$ | $-\frac52 q_0a$ | $-\frac52 q_0a$ | $-6{,}5\,q_0a$ | $-6{,}5\,q_0a$ |
| $Q(x)$ | $-\frac12 q_0a$ | $-\frac12 q_0a$ | $\frac32 q_0a$ | $\frac32 q_0a$ | $+\frac32 q_0a$ | $-6{,}5\,q_0a$ | $\frac52 q_0a$ | $\frac52 q_0a$ |
| $M(x)$ | $0$ | $-6\,q_0a^2$ | $-6\,q_0a^2$ | $0$ | $0$ | $-20\,q_0a^2$ | $-20\,q_0a^2$ | $0$ |

(In der Tabelle ist pro Bereich bei konstanten Werten nur ein Wert eingetragen; bei Bereich 4 $N$ zunächst $-\frac52 q_0a$, korrigiert auf $-6{,}5\,q_0a$.)

> Skizze: **N-Verlauf** am Rahmen (Ⓝ): Rechteckflächen entlang aller Stäbe, alle $\ominus$ (Druck): linker Stiel $-\frac32 q_0a$, Riegel (beide Teile) $-\frac52 q_0a$, rechter Stiel $-6{,}5\,q_0a$. An jedem Bereich das lokale KOS (grün): $x_1$ nach oben, $x_2$, $x_3$ nach rechts, $x_4$ nach unten, jeweils mit $z$-Pfeil zur Rahmeninnenseite.

---

## Seite 22

> Skizze: **Q-Verlauf** am Rahmen (Ⓠ): linker Stiel konstant $-\frac12 q_0a$ ($\ominus$); linker Riegel konstant $\frac32 q_0a$ ($\oplus$, rot, unter dem Riegel aufgetragen); rechter Riegel linear von $+\frac32 q_0a$ am Gelenk auf $-6{,}5\,q_0a$ an der rechten Ecke (Nulldurchgang bei $x_3 = \frac32 a$; positiver Teil rot unten, negativer Teil oben); rechter Stiel konstant $\frac52 q_0a$ ($\oplus$). Eine erste Version (blau, mit $-\frac52 q_0 a$ / $-\frac32 q_0a$ oben am Riegel) ist teilweise durchgestrichen/überzeichnet.

> Skizze: **M-Verlauf** am Rahmen (Ⓜ): linker Stiel linear von $0$ (A) auf $-6\,q_0a^2$ (Ecke), $\ominus$, außen (links) aufgetragen; linker Riegel linear von $-6\,q_0a^2$ auf $0$ am Gelenk, $\ominus$, oben (außen) aufgetragen; rechter Riegel Parabel von $0$ (Gelenk) über kleines positives Maximum ($\oplus$, rot, unten/innen, $\frac98 q_0a^2$) auf $-20\,q_0a^2$ ($\ominus$, oben/außen) an der Ecke; rechter Stiel linear von $-20\,q_0a^2$ (Ecke) auf $0$ (B), $\ominus$, außen (rechts). Ein zuerst falsch gezeichneter großer Bogen über dem rechten Riegel ist durchgestrichen. Lokale KOS grün an jedem Bereich ($z$ zur Innenseite = gestrichelte/untere Faser). Negative Momente liegen damit auf der Außenseite (Zugseite), positive auf der Innenseite.

- $\curvearrowright$ $M$ ist stetig, wenn keine Einzelmomente eingeleitet werden

---

## Seite 23

- Alternative für Ⓘⓘⓘ 3. Bereich
  - $\curvearrowright$ erst Ⓘⓥ lösen
  - $\curvearrowright$ dann Ⓘⓘⓘ lösen

> Skizze (rechts oben): Rahmenskizze, der rechte Riegel (Bereich III*) grün umrandet.

**3. Bereich Ⓘⓘⓘ\***

> Skizze: Riegelstück (Länge $8a$) mit $q_0$ (rot, ↓). Am linken Ende (Gelenk) Gelenkkräfte $\frac52 aq_0$ (→) und $\frac32 aq_0$ ↑ [?]; $x_3$ ab Gelenk nach rechts. Am rechten Schnittufer (bei $8a$) $N(x_3)$ →, $Q(8a)$ ↓, $M(x_3)$.

$\to: \; N(8a) + \frac52 aq_0 = 0 \;\Rightarrow\; N(x) = -\frac52 aq_0$ ✓

$dQ(x) = -q(x)\,dx = -q_0\,dx \quad |\int$
$Q(x) = -q_0\int dx = -q_0x + C_1$

$dM(x) = Q(x)\,dx \quad |\int$
$M(x) = \int(-q_0x + C_1)\,dx = -\frac{q_0x^2}{2} + C_1x + C_2$

RB für $M$:
$M(0) = 0$ (Gelenk)
$M(8a) = -20\,q_0a^2$ $\to$ aus 4. Bereich
(grün umrahmt: $M$ muss stetig sein! (wenn kein Einzelmoment angreift / eingeleitet wird))

$M(0) \overset{!}{=} 0 = C_2 \;\leadsto\; C_2 = 0$
$M(8a) = -\frac{q_0 64a^2}{2} + C_1\,8a = -20\,q_0a^2$
$C_1 = (32\,q_0a^2 - 20\,q_0a^2)\frac{1}{8a} = \frac{12}{8}q_0a = \frac32 q_0a$

$$Q(x) = -q_0x + \frac32 q_0a \;✓$$
$$M(x) = -\frac{q_0x^2}{2} + \frac32 q_0a\,x \;✓$$

(stimmt mit dem direkten Schnittverfahren auf Seite 20 überein)

---

## Didaktische Gliederung

1. **Motivation / Definition (S. 1)**
   - Rückblick: bisher Schnitte durch Lager und Stäbe (Fachwerk) → äußere Kräfte sichtbar machen.
   - Neu: Schnitt *durch das Tragwerk* (Balken) → innere Beanspruchung, Ort der max. Beanspruchung.
   - Analogie Einspannung: im Schnitt wirken so viele Größen wie Freiheitsgrade gesperrt werden (eben: 3).
   - Schnittgrößen = Resultierende der Spannungen im Querschnitt: Normalkraft $N$ (⊥ Schnittebene), Querkraft $Q$ (∥ Schnittebene), Biegemoment $M_B$.
2. **Vorzeichenkonvention (S. 2)** – zentral:
   - Koordinate $x$ entlang der Stabachse (beim Balken nach rechts), $z$ senkrecht dazu **nach unten** (bzw. bei Rahmen zur Innenseite, wo die „untere"/gestrichelte Faser liegt).
   - **Positives Schnittufer** = Ufer „auf der Koordinatenseite", d. h. dessen äußere Normale in $+x$ zeigt (beim Balken das rechte Ende des linken Teilstücks); **negatives Schnittufer** = gegenüberliegendes Ufer.
   - $N$ positiv als **Zugkraft** (aus der Schnittfläche heraus, wie Fachwerk-Stabkräfte).
   - $Q$ positiv: am positiven Schnittufer **nach unten** (in $+z$), am negativen Schnittufer nach oben.
   - $M$ positiv, wenn die **untere Faser** (Seite $+z$) **auf Zug** beansprucht wird (am pos. Ufer im Uhrzeigersinn/Drehung um $+y$ bei $x$ rechts, $z$ unten).
   - Schnittgrößen werden in den Gleichgewichtsbedingungen wie Lagerreaktionen behandelt (stets positiv angesetzt, Vorzeichen ergibt sich aus der Rechnung); Momentenbilanz stets um den Schnittpunkt $S$; Lösung am einfacheren Teilsystem.
   - Schnittgrößen sind Funktionen von $x$; Unstetigkeiten → Bereichseinteilung.
3. **Bereichseinteilung (S. 3)**: neuer Bereich (mit neuer lokaler Koordinate $x_i$, $z_i$) bei Trägeranfang, Angriffspunkten von Einzelkräften/-momenten, Beginn/Ende und Unstetigkeitsstellen von Streckenlasten, Lagern, Ecken/Verzweigungen. Je Bereich 3 GGB, Schnittgrößen gelten nur im Bereich.
4. **Berechnungsschema „Kochrezept" (S. 4)**: ① Lager-/Verbindungsreaktionen → ② Bereiche + KOS → ③ Schnitt bei beliebigem $x_i$ in jedem Bereich, GGB → $N(x_i), Q(x_i), M(x_i)$ → ④ Werte an Bereichsgrenzen, grafische Darstellung.
5. **Beispiel 1 (S. 5–8)**: Kragträger mit Einzelkräften – vollständige Anwendung des Schemas inkl. Zustandslinien (konstante $N$, $Q$ mit Sprüngen; stückweise lineares $M$, Knicke an Lastangriffen; Positives im Diagramm nach oben aufgetragen).
6. **Differentielle Zusammenhänge (S. 9–10)**: GGB am Balkenelement $dx$ →
   $\frac{dQ}{dx} = -q$ (4.3.1), $\frac{dM}{dx} = Q$ (4.3.2), $\frac{d^2M}{dx^2} = -q$ (4.3.3); Vernachlässigung von $dx^2$-Termen; Integration bei bekanntem $q(x)$.
7. **Beispiel 2 (S. 11–14)**: Dreieckslast – Integration, Integrationskonstanten aus Randbedingungen ($M=0$ an gelenkigen Lagern), $M_{\max}$ an der Nullstelle von $Q$; Vergleich mit „normaler" Schnittmethode (Resultierende der Teillast) → gleiches Ergebnis.
8. **Beispiel 3 / Übung (S. 15–17)**: parabelförmige (nichtlineare) Streckenlast – Integration, RB, $x_0$ durch Raten/Symmetrie, Maximum-Nachweis über $M'' = -q < 0$, Zustandslinien.
9. **Beispiel 4 (S. 17–23)**: Dreigelenkrahmen (Gelenk im Riegel) – Lagerreaktionen über zwei Teilsysteme, 4 Bereiche mit lokalen KOS (Stiel $x$ nach oben/unten, $z$ nach innen), Wertetabelle, Zustandslinien $N$, $Q$, $M$ am Rahmen (Momente auf der Zugseite: negativ außen), Stetigkeit von $M$ ohne Einzelmomente, $M=0$ im Gelenk; alternative Lösung von Bereich III über Differentialbeziehungen mit Randbedingung aus Bereich IV (Stetigkeit von $M$ in der Ecke).

**Verwendete Vorzeichenkonvention (Zusammenfassung):** $x$ längs Stabachse (vom Bereichsanfang aus), $z$ senkrecht nach unten bzw. zur gestrichelten (Innen-)Faser; positives Schnittufer = Normale in $+x$-Richtung; $N > 0$ Zug; $Q > 0$ am positiven Ufer in $+z$ (nach unten); $M > 0$ erzeugt Zug in der unteren ($+z$-)Faser; Streckenlast $q$ positiv nach unten ($+z$) → $Q' = -q$, $M' = Q$.

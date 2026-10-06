# Technische Mechanik – Festigkeitslehre: 3.3 Biegung und Zug/Druck, 3.4 Schiefe Biegung (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen (Prof. Schönfelder)
Quelle: `Quellen/Vorlesung-2013/9-biegung+zug.pdf` (17 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Momente/Spannungen, Grün = Koordinaten, Bemaßungen, Umrahmungen, Kommentare.
- Unsichere Lesungen sind mit [?] markiert, Anmerkungen der Transkription mit [Prüfung: ...] bzw. [Anm.: ...].
- Fortsetzung von `8-balkenbiegung.md` (Kapitel 3.1/3.2).

---

## Seite 1

### 3.3 Zusammengesetzte Beanspruchung: Biegung und Zug/Druck

> Skizze: Räumlicher Balkenausschnitt, Schnittfläche mit Achsen $x$ (nach vorn), $y$ (links), $z$ (unten), grün; rot Momentenvektor $M$ (Doppelpfeil, $y$-Richtung) und Normalkraft $N$ (in $x$-Richtung).
> Daneben zwei Seitenansichten: links Spannungsverteilung aus $M_y$ (linear, Dreiecke, rot) → $\sigma_x(z) = \frac{M_y}{I_{yy}}z$; rechts aus $N$ (konstant, rot) → $\sigma_x = \frac{N}{A}$.

Lösung mit dem **Superpositionsprinzip** (Superposition = Überlagerung):
$$\sigma_x(N, M_y) = \sigma_x(N) + \sigma_x(M_y)$$

$$\boxed{\sigma_x(x,z) = \frac{N(x)}{A(x)} + \frac{M_y(x)}{I_{yy}(x)}\,z}$$

$\curvearrowright$ Die Überlagerung der Belastungen führt auf eine Verschiebung der neutralen Schicht (Spannungsnulllinie)
⇒ neutrale Schicht/Faser <u>nicht mehr bei $z = 0$!</u>

> Skizze: Superposition der Spannungsverteilungen am Schnittufer: $M_y$ (linear, Nulldurchgang bei $z = 0$) $+$ $N$ (konstant, Zug) $=$ resultierende lineare Verteilung mit verschobenem Nulldurchgang; grün markiert „Ort der neutralen Faser" (unterhalb der $x$-Achse).

## Seite 2

Gleichung der (Koordinate für) neutralen Faser an der Stelle $x$:
$$\sigma_x(x,z) = \frac{N}{A} + \frac{M_y}{I_{yy}}\,z = 0$$
$$\boxed{z = -\frac{N\,I_{yy}}{A\,M_y}}$$

- $N(x)$, $M_y(x)$ gleiches Vorzeichen → $z(x) < 0$
- $N(x)$, $M_y(x)$ unterschiedliches Vorzeichen → $z(x) > 0$

**Beispiel: Exzentrischer Zug**

> Skizze: Kragträger, rechts eingespannt; am freien linken Ende greift $F$ (rot, nach links) an der Oberkante an. Koordinaten $x$ (rechts), $z$ (unten). Rechteckquerschnitt $b \times h$, Achsen $y$ (links), $z$ (unten); Angriffspunkt von $F$ (⊙) mittig an der Oberkante.

geg.: $F, b, h$
ges.:
- $\sigma_{x,\max}$
- Position der neutralen Schicht

**Lös.:**
> Skizze: Linkes Balkenstück mit $F$ (←) an der Oberkante ($h/2$ über der Achse); am Schnittufer $N(x)$ (→) und $M_y(x)$ (Drehpfeil).

$$\rightarrow:\; -F + N(x) = 0 \;\to\; \underline{N(x) = F}$$
$$\curvearrowleft:\; M_y(x) + F\cdot\frac{h}{2} = 0 \;\to\; \underline{M_y(x) = -F\,\frac{h}{2}}$$

## Seite 3

$$\sigma_x = \frac{N}{A} + \frac{M_y}{I_{yy}}\cdot z, \qquad I_{yy} = \frac{b h^3}{12}, \quad A = b\cdot h$$
$$= \frac{F}{b h} - \frac{F h\cdot 12}{2\,b h^3}\,z$$
$$\underline{\sigma_x = \frac{F}{b h} - \frac{6F}{h^2 b}\cdot z}$$

Lage der neutralen Faser: $\sigma_x = 0$
$$0 = \frac{F}{b h} - \frac{6F}{h^2 b}\cdot z \;\to\; z = \left(-\frac{F}{bh}\right)\left(-\frac{h^2 b}{6F}\right), \qquad \underline{z = \frac{h}{6}}$$

> Skizze: Balken mit $F$ (←) an der Oberkante; gestrichelte neutrale Faser im Abstand $h/6$ unterhalb der Schwerachse; Querschnitt mit eingetragener neutraler Faser bei $h/6$ (grün).

> Skizze: Spannungsverteilung am Schnittufer (rot): oben großer Zug (Pfeile nach links), linear abnehmend, Nulldurchgang unterhalb der Mitte, unten kleiner Druck.

$$\underline{\sigma_x\!\left(z = \tfrac{h}{2}\right)} = \frac{F}{bh} - \frac{6F}{h^2 b}\cdot\frac{h}{2} = \underline{-\frac{2F}{bh}}$$
$$\underline{\sigma_x\!\left(z = -\tfrac{h}{2}\right)} = \frac{F}{bh} - \frac{6F}{h^2 b}\left(-\frac{h}{2}\right) = \underline{\frac{4F}{bh}} \;\to\; \underline{\sigma_{x,\max}}$$

Die maximale Spannung (betragsmäßig) entsteht immer in der von der neutralen Schicht weit entferntesten Schicht (→ $z_{\max}$!).

[Prüfung: korrekt. Kontrolle: lineare Verteilung von $+4F/(bh)$ (oben) bis $-2F/(bh)$ (unten) hat Nullstelle bei $z = h/6$ ✓.]

## Seite 4

**2. Beispiel:**

> Skizze: Abgewinkelter Träger (L-Form): senkrechter Stab, oben bei $A$ eingespannt, Länge $2L$; unten nach rechts abgewinkelter Arm der Länge $L$; am Ende des Arms $F$ (rot, nach unten). Koordinaten an $A$: $x$ nach unten, $z$ nach links [?]. Quadratquerschnitt $a \times a$.

gegeben: $F, L, a$
ges.:
- Spannungen in Längsstab (senkrechter Stab)
- Ort neutrale Faser

**Lös.:** ① (Lagerreaktionen)/Schnittgrößen

> Skizze: Unterer Teil des Trägers ab Schnitt (Abstand $2L - x$ bis zum Knick, Arm $L$) mit $F$; am Schnitt $N$, $Q$, $M$ (rot).

$$\rightarrow:\; \underline{Q = 0} \qquad \uparrow:\; N - F = 0 \;\to\; \underline{N = F}$$
$$\curvearrowleft_A:\; M_A + F\cdot L = 0 \;\to\; \underline{M_A = -F\cdot L}$$

> Skizze: $N$-Verlauf im senkrechten Stab $\oplus$ konstant (rot); $M$-Verlauf $\ominus$ konstant (blau).

## Seite 5

② Spannungen
$$A = a^2, \qquad I_{yy} = \frac{a^4}{12}$$
$$\sigma_x = \frac{N}{A} + \frac{M_y}{I_{yy}}\,z = \frac{F}{a^2} - \frac{F L\cdot 12}{a^4}\,z$$
$$\underline{\sigma_x = \frac{F}{a^2} - \frac{12\,F L}{a^4}\,z}$$

- Lage der neutralen Faser
$$\sigma_x = 0 = \frac{F}{a^2} - \frac{12\,F L}{a^4}\,z \;\to\; z = \frac{F}{a^2}\cdot\frac{a^4}{12\,F L} = \frac{a^2}{12\,L}$$

> Skizze: Senkrechter Stab mit Achsen $x$ (nach unten), $z$ (nach links); neutrale Faser gestrichelt im Abstand $\frac{a^2}{12L}$ von der Stabachse; unten lineare Spannungsverteilung (rot) mit Nulldurchgang bei der neutralen Faser.

→ abhängig von $L$ (Momentenwirkung):
- $L\uparrow$ → $z\downarrow \approx 0$ $\curvearrowright$ Moment dominiert
- $L\downarrow$ → $z \to \infty$ $\curvearrowright$ keine Biegung mehr vorhanden

[Prüfung: korrekt. Die maximale Spannung (ges. „Spannungen") wird im Original nicht ausgewertet: $\sigma_{\max} = \frac{F}{a^2} + \frac{6FL}{a^3}$ bei $z = -a/2$ bzw. $\sigma_{\min} = \frac{F}{a^2} - \frac{6FL}{a^3}$ bei $z = +a/2$.]

## Seite 6

### 3.4 Einführung in die schiefe Biegung (zweifache Biegung)

**Erinnerung:** zweifache (schiefe) Biegung
- → Hauptträgheitsachsen sind bekannt ($y$-, $z$-Achse)
- → Momentenvektor besitzt andere Richtung

> Skizze: Räumlicher Balkenausschnitt, Achsen $x$, $y$, $z$ (grün); schräger Momentenvektor $M$ (rot, Doppelpfeil) in der Schnittfläche.

$\curvearrowright$ **Lösung:** Bezug der Komponenten von $\vec M$ auf die jeweiligen Hauptachsen
1. Zerlegung des Biegemoments in zwei Komponenten in Richtung der Hauptachsen

> Skizze: Rechteckquerschnitt mit schrägem $M$ $=$ Querschnitt mit $M_y$ (in $y$-Richtung) $+$ Querschnitt mit $M_z$ (in $z$-Richtung).

2. Lösung der Biegespannungen für beide Hauptachsenfälle
3. Überlagerung (Superposition) der Lösungen der Biegespannungen

## Seite 7

$$\boxed{\sigma_x(x,y,z) = \frac{M_y(x)}{I_{yy}}\,z + \frac{M_z(x)}{I_{zz}}\,y} \quad \left(+\frac{N_x}{A}\right)$$

$\curvearrowright$ Zerlegung s. vorher

> Skizze: links Querschnitt (hochkant) mit $M_y$ (rot, in $y$-Richtung), Hinweis $I_{yy}$, $z_{\max}$ (grün); rechts derselbe Querschnitt um 90° gedreht dargestellt ($z$ nach rechts, $y$ nach unten) mit $M_z$, Hinweis $I_{zz}$, $y_{\max}$.

[Prüfung: Mit der in `8-balkenbiegung.md` S. 9 verwendeten Definition $M_z = -\int_A y\,\sigma_x\,dA$ (rechtshändiges System $x$, $y$, $z$) lautet die Formel $\sigma_x = \frac{M_y}{I_{yy}}z - \frac{M_z}{I_{zz}}y$. Das „$+$" ist nur richtig, wenn $M_z$ im Skript mit umgekehrtem Drehsinn positiv gezählt wird. Die nachfolgenden Beispiele rechnen konsequent mit „$+$"; die Spannungsbeträge bleiben gleich, die Lage der Nulllinie wird dadurch an der $z$-Achse gespiegelt.]

- neutrale Faser (Spannungs-Null-Linie)
$$\frac{M_y}{I_{yy}}\,z + \frac{M_z}{I_{zz}}\,y = 0$$
→ Gerade in $y$-$z$-Ebene (Querschnitt)

> Skizze: links „einfache Biegung": Rechteck, Nulllinie $\sigma = 0$ (rot) liegt auf der $y$-Achse. Rechts „zweifache (schiefe) Biegung": Nulllinie $\sigma = 0$ schräg durch den Querschnitt – (rot:) „geht durch Schwerpunkt!"

## Seite 8

**Bsp.:**

> Skizze: Kragträger (räumlich), rechts eingespannt (Wand), Länge $L$. Am freien Ende greift $F$ (rot) schräg an der linken oberen Ecke des Rechteckquerschnitts an. Rechts Querschnitt $b \times h$ mit Achsen $-y$/$y$, $z$ (unten); $F$ unter Winkel $\alpha$ gegen die Horizontale, Wirkungslinie (gestrichelt) durch den Schwerpunkt. Grün: Hinweis auf gedrehtes Koordinatensystem („oder", Blickrichtung).

geg.: $\tan\alpha = 2$, $h/b = 2$
ges.: Spannungsverlauf an Einspannung im Querschnitt

**Lös.:**
> Skizze: Zerlegung von $F$ am Querschnitt: $F \;\hat{=}\; F_z$ (↓, vertikal) $+$ $F_y$ (horizontal, in $y$-Richtung); Kräftedreieck mit $F$, $F_y$, $F_z$, Winkel $\alpha$.

$$F_y = \cos\alpha\,F, \qquad F_z = \sin\alpha\,F$$

a) > Skizze: Kragträger in $x$-$z$-Ebene (Höhe $h$), Last $F_z$ am freien Ende; Teilstück der Länge $x$ freigeschnitten.
$$\curvearrowleft:\; M_y + F_z\cdot x = 0 \;\to\; \underline{M_y = -F_z\,x}$$
$$x = L:\quad \underline{M_y(A) = -F_z\cdot L = -F\sin\alpha\,L}$$

b) > Skizze: Kragträger in $x$-$y$-Ebene (Breite $b$), Last $F_y$ am freien Ende.
$$\curvearrowleft:\; M_z + F_y\cdot x = 0 \;\to\; \underline{M_z = -F_y\,x}$$
$$\underline{M_z(A) = -F_y\cdot L = -F\cos\alpha\,L}$$
(Vorzeichen im Original überschrieben/korrigiert)

## Seite 9

$$\sigma_x(x,y,z) = \frac{M_y}{I_{yy}}\,z + \frac{M_z}{I_{zz}}\,y, \qquad I_{yy} = \frac{b h^3}{12}, \quad I_{zz} = \frac{h b^3}{12}$$

$$\sigma_x(A,y,z) = -\frac{12\,F\sin\alpha\,L}{b h^3}\,z - \frac{12\,F\cos\alpha\,L}{h b^3}\,y$$
$$\underline{\sigma_x(y,z) = -\frac{12\,F L}{b h}\left(+\frac{\sin\alpha}{h^2}\,z + \frac{\cos\alpha}{b^2}\,y\right)}$$
(Vorzeichen vor dem zweiten Term bzw. vor der Klammer im Original von $+$ auf $-$ überschrieben)

$\curvearrowright$ Spannungsverlauf über Querschnitt bei $x = L$ (Einspannung)

- Lage neutrale Faser (Spannungs-Null-Linie)
$$\sigma_x(y,z) = 0 = -\frac{12\,F L}{b h}\left(+\frac{\sin\alpha}{h^2}\,z + \frac{\cos\alpha}{b^2}\,y\right)$$
$$z = -\frac{\cos\alpha}{\sin\alpha}\,\frac{h^2}{b^2}\,y = -\frac{1}{2}\cdot 4\,y = \underline{-2y}$$

(rot:) $z(y = \tfrac{b}{2}) = +\dfrac{1}{\tan\alpha}\dfrac{h^2}{2b} = +\dfrac{h}{2}$

> Skizze: Rechteckquerschnitt ($-y$ links, $y$ rechts, $z$ unten); $F$ (rot) greift an der linken oberen Ecke unter $\alpha$ an. Grün gestrichelt: Drehachse des Gesamtmoments ($M = F\cdot L$), senkrecht zur Kraftrichtung. Rot: Spannungs-Null-Linie durch den Schwerpunkt, von der linken unteren Ecke $(-\tfrac{b}{2}, +\tfrac{h}{2})$ zur rechten oberen Ecke – „fällt nicht mit Drehachse des Gesamtmoments zusammen!"

[Prüfung: $z = -2y$ korrekt. Für $y = b/2$ folgt $z = -2\cdot b/2 = -b = -h/2$ (nicht $+h/2$); die rote Nebenrechnung hat einen Vorzeichenfehler. Die Skizze ist dagegen richtig: Die Nulllinie ist die Querschnittsdiagonale durch $(-\tfrac b2, +\tfrac h2)$ und $(+\tfrac b2, -\tfrac h2)$.]

## Seite 10

→ Extremwerte der Spannungen in Eckpunkten des Querschnitts

(durchgestrichen: $\sigma_x(\tfrac{b}{2}, -\tfrac{h}{2}) =$)

„2 Geraden ergeben Ebene"

> Skizze: Räumliche Darstellung der Spannungsebene über dem Rechteckquerschnitt (Achsen $-y$/$y$, $z$, $\sigma$ nach oben): ebene, schräg liegende Spannungsfläche; an einer Ecke $\sigma_{\max}$ (rot, oben), an der gegenüberliegenden Ecke $-\sigma_{\max}$ (blau, unten); die Diagonale durch die beiden anderen Ecken ist die Linie $\sigma = 0$ (rot).

$$\sigma_x\!\left(-\tfrac{b}{2}, -\tfrac{h}{2}\right) [?] = \frac{12\,F L}{b h}\left(+\frac{\sin\alpha}{h^2}\cdot\frac{h}{2} + \frac{\cos\alpha}{b^2}\cdot\frac{b}{2}\right) = \frac{12\,F L}{b h}\left(\frac{\sin\alpha}{2h} + \frac{\cos\alpha}{2b}\right)$$

> Skizze: Querschnitt mit $F$ an der linken oberen Ecke; Diagonale teilt in Zugbereich $\oplus$ (oben links, rot schraffiert) und Druckbereich $\ominus$ (unten rechts).

> Skizze (unten, unvollständig): Spannungsverläufe (Dreiecke) entlang von Querschnittsrändern.

[Prüfung: Der Maximalwert gilt an der Lastecke $(y, z) = (-\tfrac b2, -\tfrac h2)$ (dort sind beide Klammerterme negativ, das Vorzeichen vor der Klammer macht $\sigma$ positiv). Zahlenmäßig mit $\sin\alpha = 2/\sqrt5$, $\cos\alpha = 1/\sqrt5$, $h = 2b$: $\sigma_{\max} = \frac{12FL}{2b^2}\cdot\frac{1}{\sqrt5\,b} = \frac{6FL}{\sqrt5\,b^3} \approx 2{,}68\,\frac{FL}{b^3}$ (im Original nicht ausgerechnet). An den Ecken $(\tfrac b2, -\tfrac h2)$ und $(-\tfrac b2, \tfrac h2)$ ist $\sigma = 0$.]

## Seite 11

**Übung: Ü13, 4.5**

> Skizze: Welle (räumlich), Kreisquerschnitt $\varnothing d$, Länge $L$ (dreimal $L/3$, grün bemaßt). Lager $A$ links (Festlager), Lager $B$ rechts (Loslager). Koordinaten an $A$: $x$ entlang der Welle, $y$ (horizontal quer, $(-y)$ in Klammern), $z$ nach unten. $F_1$ (rot) vertikal nach unten bei $L/3$ von $A$; $F_2$ (rot) horizontal in $y$-Richtung bei $2L/3$ von $A$.

geg.:
- Lager $A$ Verschiebungen: $u_x = u_y = u_z = 0$, $\varphi_x = 0$ (keine Drehung)
- Lager $B$ Verschiebungen: $u_y = u_z = 0$
- $L = 300\,\text{mm}$, $d = 40\,\text{mm}$
- $F_1 = 1\,\text{kN}$, $F_2 = 1{,}2\,\text{kN}$

ges.: $\sigma_{\max}$

## Seite 12

**Lös.:** ① Aufteilung in Hauptachsenfälle

> Skizze a): Balken in $x$-$z$-Ebene, $F_1$ bei $L/3$ (Rest $\frac23L$). b): Balken in $x$-$y$-Ebene, $F_2$ bei $\frac23L$ (Rest $L/3$).

a)
> Skizze: Balken mit $A_x$ (→), $A_z$ (↑), $B_z$ (↑), $F_1$ (↓).

$$\rightarrow:\; A_x = 0 \qquad \uparrow:\; A_z - F_1 + B_z = 0 \qquad \curvearrowleft_A:\; -F_1\cdot\frac{L}{3} + B_z\cdot L = 0$$
$$\underline{B_z = \frac{F_1}{3}}, \qquad \underline{A_z = \frac{2}{3}F_1}$$

> Skizze: Bereiche I ($x_1$ von $A$ bis $F_1$) und II ($x_2$ ab $F_1$), grün umrandet; $\frac23F_1$ an $A$, $\frac{F_1}{3}$ an $B$.

I: $N_{x1} = 0$, $Q$ … (Fokus auf $M$)
$$\curvearrowleft\; M:\; M_{y1} - \tfrac{2}{3}F_1\,x_1 = 0 \;\to\; \underline{M_{y1} = \tfrac{2}{3}F_1\,x_1}$$
II:
$$M_{y2} + \tfrac{2}{3}F_1\left(\tfrac{L}{3} + x_2\right) + F_1 x_2 = 0$$
$$M_{y2} = \tfrac{2}{3}F_1\left(\tfrac{L}{3} + x_2\right) - F_1 x_2 = \underline{-\tfrac{1}{3}F_1 x_2 + \tfrac{2}{9}F_1 L}$$

[Prüfung: Ergebnis korrekt; die angeschriebene Gleichgewichtsgleichung hat jedoch falsche Vorzeichen (richtig: $M_{y2} - \tfrac23F_1(\tfrac L3 + x_2) + F_1 x_2 = 0$).]

> Skizze $M$: Dreieck $\oplus$ (nach unten, $z$-Richtung, aufgetragen), Maximum $\frac{2}{9}F_1 L$ bei $x = L/3$.

## Seite 13

b)
> Skizze: Balken mit $A_x$, $A_y$, $B_y$ und $F_2$ bei $\frac23L$ (Rest $\frac L3$).

$$\rightarrow:\; \underline{A_x = 0} \qquad \uparrow:\; A_y + B_y - F_2 = 0 \qquad \curvearrowleft_A:\; -F_2\cdot\tfrac{2}{3}L + B_y\cdot L = 0$$
$$\underline{B_y = \tfrac{2}{3}F_2}, \qquad \underline{A_y = \tfrac{1}{3}F_2}$$

> Skizze: Bereiche I ($x_3$) und II ($x_4$), grün umrandet; $\frac13F_2$ an $A$, $\frac23F_2$ an $B$; Koordinate $y$ nach unten dargestellt.

I:
$$M_{z1} - \tfrac{F_2}{3}\,x_1 = 0 \;\to\; \underline{M_{z3} = \tfrac{F_2}{3}\,x_3}$$
II:
$$M_{z4} - \tfrac{F_2}{3}\left(\tfrac{2}{3}L + x_4\right) + F_2\,x_4 = 0$$
$$M_{z4} = \tfrac{F_2}{3}\left(\tfrac{2}{3}L + x_4\right) - F_2 x_4 = \underline{-\tfrac{2}{3}F_2 x_4 + \tfrac{2\,F_2 L}{9}}$$

> Skizze $M$: Dreieck $\oplus$, Maximum $\frac{2}{9}F_2 L$ bei $x = \frac23L$.

[Prüfung: korrekt.]

## Seite 14

> Skizze: Welle mit $F_1$ (bei $L/3$) und $F_2$ (bei $\frac23L$, ⊙); darunter untereinander:
> – $M_y$-Verlauf ($M_{y1}$, $M_{y2}$; Knick bei $L/3$),
> – $M_z$-Verlauf ($M_{z1}$, $M_{z2}$; Knick bei $\frac23L$),
> – $\sigma$-Verlauf (schematisch): Bereiche $\alpha$ ($0 \ldots L/3$, $M_{y1} + M_{z1}$), $\beta$ ($L/3 \ldots \frac23L$, $M_{y2} + M_{z1}$), $\gamma$ ($\frac23L \ldots L$, $M_{y2} + M_{z2}$); $0$ an beiden Lagern; Knickstellen bei $L/3$ und $\frac23L$ jeweils grün markiert „Max?".

$I_{yy} = I_{zz}$! für Kreis

$$\sigma_\alpha(y,z,x) = \frac{2 F_1 x_1}{3\,I_{yy}}\,z + \frac{F_2\,x_3}{3\,I_{yy}}\,y$$
$$\sigma_\beta(x,y,z) = \frac{z}{I_{yy}}\left(-\tfrac{1}{3}F_1 x_2 + \tfrac{2}{9}F_1 L\right) + \frac{F_2\,x_3}{3\,I_{yy}}\,y$$
$$\sigma_\gamma(x,y,z) = \frac{z}{I_{yy}}\left(-\tfrac{1}{3}F_1 x_2 + \tfrac{2}{9}F_1 L\right) + \frac{y}{I_{yy}}\left(-\tfrac{2}{3}F_2 x_4 + \tfrac{2}{9}F_2 L\right)$$
(grün: jeweils Bereich 1, 2! – Indizes der Koordinaten nachträglich korrigiert)

## Seite 15

Max?
$$\sigma_\alpha\Big(\boxed{x_1 = \tfrac L3,\; x_3 = \tfrac L3}\Big) = \frac{2}{3}\frac{F_1 L}{3}\frac{z}{I_{yy}} + \frac{F_2}{3}\frac{L}{3}\frac{y}{I_{yy}} = \frac{1}{I_{yy}}\left(\tfrac{2}{9}F_1 L\,z + \tfrac{1}{9}F_2 L\,y\right)$$

Max?
$$\sigma_\beta\Big(\boxed{x_2 = \tfrac13L,\; x_3 = \tfrac23L}\Big) = \frac{z}{I_{yy}}\left(-\tfrac13F_1\tfrac13L + \tfrac29F_1L\right) + \frac{F_2}{3}\frac{2}{3}L\,\frac{y}{I_{yy}} = \frac{1}{I_{yy}}\left(\tfrac19F_1L\,z + \tfrac29F_2L\,y\right)$$

mit $F_2 = 1{,}2\,F_1 = \frac{6}{5}F_1$, $\;y = z$:

$$\sigma_\alpha = \frac{z}{I_{yy}}\left(\tfrac29F_1L + \tfrac19\cdot\tfrac65F_1L\right) = \frac{z}{I_{yy}}\left(\tfrac{48}{135}F_1L\right)$$
$$\sigma_\beta = \frac{z}{I_{yy}}\left(\tfrac19F_1L + \tfrac29\cdot\tfrac65F_1L\right) = \frac{z}{I_{yy}}\left(\tfrac{51}{135}F_1L\right) \;\Rightarrow\; \underline{\underline{\sigma_{\max}}}$$

$$\sigma_\beta\big|_{x_2 = L/3,\;x_3 = 2L/3} > \sigma_\alpha\big|_{x_1 = L/3,\;x_3 = L/3}$$

[Prüfung: Brüche korrekt ($\tfrac{16}{45} = \tfrac{48}{135}$, $\tfrac{17}{45} = \tfrac{51}{135}$). **Methodischer Fehler:** Die Annahme $y = z$ (mit später $y = z = d/2$) beschreibt den Punkt $(d/2, d/2)$, der **außerhalb** des Kreisquerschnitts liegt. Beim Kreis ist das maßgebende Moment das resultierende Moment $M_\text{res} = \sqrt{M_y^2 + M_z^2}$, die Randspannung $\sigma_{\max} = M_\text{res}/W$ mit $W = \pi d^3/32$. Stelle $\alpha$: $M_\text{res} = \tfrac L9\sqrt{(2F_1)^2 + F_2^2} = \tfrac{L}{9}\cdot 2{,}332\,\text{kN}$; Stelle $\beta$: $M_\text{res} = \tfrac L9\sqrt{F_1^2 + (2F_2)^2} = \tfrac L9\cdot 2{,}600\,\text{kN} = 86{,}7\,\text{Nm}$ → maßgebend ist zwar ebenfalls $\beta$, aber mit dem Zahlenwert unten (S. 16) gerechnet.]

## Seite 16

$$I_{yy} = \frac{\pi d^4}{64} \;\to\; z_{\max} = \frac{d}{2} = y_{\max}$$
$$\underline{\sigma_{\max}} = \frac{d\cdot 64}{2\,\pi d^4}\cdot\frac{51}{135}F_1 L = \frac{1632}{135}\,\frac{F_1 L}{\pi d^3} = \underline{18{,}0\,\frac{\text{N}}{\text{mm}^2}}$$

[Prüfung: Die Arithmetik ist richtig ($\frac{1632}{135\pi}\cdot\frac{10^3\cdot 300}{40^3} = 18{,}04$), das Ergebnis aber zu groß, weil der Punkt $y = z = d/2$ nicht auf dem Querschnitt liegt (s. S. 15). Korrekt: $\sigma_{\max} = \frac{32\,M_\text{res}}{\pi d^3} = \frac{32\cdot 86\,667\,\text{Nmm}}{\pi\cdot 64\,000\,\text{mm}^3} \approx 13{,}8\,\frac{\text{N}}{\text{mm}^2}$ (Stelle $x = \tfrac23L$; an $x = \tfrac L3$: $12{,}4\,\text{N/mm}^2$). Die Abweichung entspricht etwa dem Faktor $\frac{F_1 + 2F_2}{\sqrt{F_1^2 + (2F_2)^2}} = 1{,}31$.]

- Lage der neutralen Faser
$$\sigma_\alpha\big|_{x_1 = L/3,\;x_3 = L/3} = 0 = \frac{L}{I_{yy}}\left(\tfrac29F_1\,z + \tfrac19F_2\,y\right)$$
$$\underline{z} = \left(-\tfrac19F_2\,y\right)\frac{9}{2F_1} = -\frac12\cdot\frac65\,y = \underline{-\tfrac35\,y}$$

$$\sigma_\beta\big|_{x_2 = L/3,\;x_3 = 2L/3} = 0 = \frac{L}{I_{yy}}\left(\tfrac19F_1\,z + \tfrac29F_2\,y\right)$$
$$\underline{z} = \left(-\tfrac29F_2\,y\right)\frac{9}{F_1} = \underline{-2{,}4\,y}$$

[Prüfung: Werte korrekt im Rahmen der Vorzeichenkonvention $\sigma = \frac{M_y}{I}z + \frac{M_z}{I}y$ (vgl. Anmerkung S. 7).]

## Seite 17

> Skizze: Welle (Seitenansicht, Achsen $x$, $y$, $z$) mit Kraftangriffen; darunter zwei Kreisquerschnitte mit Achsen $y$ (links), $z$ (unten) und Lastpfeilen (vertikal $F_1$, horizontal $F_2$):
> – links (bei $x = L/3$): Spannungs-Null-Linie $\sigma = 0$ (rot) flach geneigt, $z = -0{,}6\,y$;
> – rechts (bei $x = \frac23L$): Nulllinie steil, $z = -2{,}4\,y$.
> Kleiner Kreis mit schraffiertem Band dazwischen.

$\curvearrowright$ Verwindung der Spannungs-Null-Linie über den Träger

> Skizze: räumliche Darstellung einer verwundenen (windschiefen) Fläche – die Nulllinie dreht sich entlang der Trägerachse.

---

## Didaktische Gliederung

1. **3.3 Zusammengesetzte Beanspruchung Biegung + Zug/Druck (S. 1–5)**
   - Superpositionsprinzip: $\sigma_x = \frac{N}{A} + \frac{M_y}{I_{yy}}z$.
   - Folge: Verschiebung der neutralen Faser aus dem Schwerpunkt; Gleichung $z_0 = -\frac{N I_{yy}}{A M_y}$; Vorzeichenregel (gleiches Vorzeichen $N$, $M_y$ → $z_0 < 0$).
   - Beispiel exzentrischer Zug (Rechteck, Kraft an Oberkante): $z_0 = h/6$, $\sigma_{\max} = 4F/(bh)$.
   - Beispiel abgewinkelter Träger: $z_0 = a^2/(12L)$, Diskussion Grenzfälle $L \to \infty$ (Biegung dominiert) / $L \to 0$ (reiner Zug).
   - Merksatz: Maximalspannung in der von der Nulllinie am weitesten entfernten Faser.
2. **3.4 Schiefe (zweifache) Biegung (S. 6–17)**
   - Lösungsweg in drei Schritten: ① Momentenvektor in Hauptachsenkomponenten zerlegen, ② Biegespannung je Hauptachse, ③ superponieren.
   - Formel $\sigma_x = \frac{M_y}{I_{yy}}z + \frac{M_z}{I_{zz}}y\;(+\frac{N}{A})$.
   - Spannungs-Null-Linie: Gerade durch den Schwerpunkt, im Allgemeinen nicht identisch mit der Drehachse des Gesamtmoments.
   - Spannungsverteilung als Ebene über dem Querschnitt; Extremwerte in Eckpunkten (Rechteck).
   - Übung Welle mit zwei Lasten in verschiedenen Ebenen: Zerlegung in zwei ebene Systeme, Bereichseinteilung, Suche des Maximums an Lastangriffspunkten, Verwindung der Nulllinie über die Trägerlänge.

**Rechenschema (wie im Skript):**
1. Kräfte in Hauptachsenrichtungen zerlegen ($F_y$, $F_z$) bzw. System in $x$-$z$- und $x$-$y$-Ebene aufteilen.
2. Lagerreaktionen und Schnittgrößen $N$, $M_y$, $M_z$ je Ebene/Bereich.
3. Querschnittswerte $A$, $I_{yy}$, $I_{zz}$.
4. Superposition $\sigma_x(x,y,z)$; Kandidaten für das Maximum: Momentenmaxima/Knickstellen und Querschnittspunkte mit maximalem Abstand von der Nulllinie (Ecken beim Rechteck; beim Kreis über $M_\text{res}$).
5. Nulllinie aus $\sigma_x = 0$.

**Definitionen:** Superpositionsprinzip, exzentrischer Zug, Spannungs-Null-Linie (neutrale Faser bei zusammengesetzter Beanspruchung), zweifache/schiefe Biegung, Hauptachsenzerlegung.

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| 1 | Kragträger, exzentrischer Zug $F$ an Oberkante, Rechteck $b \times h$ | $F, b, h$ | $N = F$, $M_y = -Fh/2$; $\sigma = \frac{F}{bh} - \frac{6F}{bh^2}z$; Nulllinie $z = h/6$; $\sigma_{\max} = 4F/(bh)$ (oben), $\sigma_{\min} = -2F/(bh)$ (unten) | 2–3 |
| 2 | L-förmiger Träger, oben eingespannt, Stiel $2L$, Arm $L$, $F$ am Armende, Quadrat $a \times a$ | $F, L, a$ | $N = F$, $Q = 0$, $M = -FL$; $\sigma = \frac{F}{a^2} - \frac{12FL}{a^4}z$; Nulllinie $z = a^2/(12L)$ | 4–5 |
| 3 | Kragträger, schräge Endlast an Querschnittsecke (schiefe Biegung), Rechteck | $\tan\alpha = 2$, $h/b = 2$, $F$, $L$ | $M_y = -F\sin\alpha L$, $M_z = -F\cos\alpha L$; $\sigma = -\frac{12FL}{bh}(\frac{\sin\alpha}{h^2}z + \frac{\cos\alpha}{b^2}y)$; Nulllinie $z = -2y$ (Diagonale); $\sigma_{\max}$ an Ecken, $= \frac{12FL}{bh}(\frac{\sin\alpha}{2h} + \frac{\cos\alpha}{2b}) \approx 2{,}68\,FL/b^3$ | 8–10 |
| 4 | Welle auf zwei Lagern (Ü13, 4.5), $F_1$ vertikal bei $L/3$, $F_2$ horizontal bei $\frac23L$, Kreis $d$ | $L = 300\,\text{mm}$, $d = 40\,\text{mm}$, $F_1 = 1\,\text{kN}$, $F_2 = 1{,}2\,\text{kN}$ | $A_z = \frac23F_1$, $B_z = \frac13F_1$, $A_y = \frac13F_2$, $B_y = \frac23F_2$; $M_{y,\max} = \frac29F_1L$, $M_{z,\max} = \frac29F_2L$; Original: $\sigma_{\max} = 18{,}0\,\text{N/mm}^2$ bei $x = \frac23L$ (korrekt: $\approx 13{,}8\,\text{N/mm}^2$); Nulllinien $z = -0{,}6y$ ($x = L/3$), $z = -2{,}4y$ ($x = \frac23L$) | 11–17 |

**Befunde der Nachrechnung (Zusammenfassung):** S. 7 Vorzeichen des $M_z$-Terms (mit der Definition aus Kap. 3.2 müsste es $-\frac{M_z}{I_{zz}}y$ heißen; im Skript konsequent „$+$"); S. 9 rote Nebenrechnung $z(b/2) = +h/2$ statt $-h/2$; S. 10 Eckpunkt des Maximums ist $(-b/2, -h/2)$ (Lastecke); S. 12 Vorzeichen in der Gleichgewichtsgleichung für $M_{y2}$ (Ergebnis richtig); S. 15–16 **wesentlicher Fehler**: Auswertung bei $y = z = d/2$ liegt außerhalb des Kreises → $\sigma_{\max} = 18{,}0$ statt korrekt $\approx 13{,}8\,\text{N/mm}^2$.

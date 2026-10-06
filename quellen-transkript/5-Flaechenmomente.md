# Technische Mechanik – Statik: 6. Flächenmomente (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen
Quelle: `Quellen/Vorlesung-2013/5-Flächenmomente.pdf` (39 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten/Hervorhebungen, Grün = Bemaßungen, Koordinaten, Ergebnisrahmen, Kommentare.
- Das Kapitel ist im Original als „6." nummeriert (Dateiname „5-Flächenmomente").
- Koordinaten mit Querstrich ($\bar x, \bar y$) = beliebiges (Bezugs-)System; ohne Querstrich ($x, y$) = Schwerpunktsystem.
- Unsichere Lesungen sind mit [?] markiert; Nachrechnungen und Fehlerhinweise mit [Prüfung: ...].

---

## Seite 1

# 6. Flächenmomente

- Flächenmomente sind Rechengrößen, die vor allem in der Festigkeitslehre benötigt werden.
- Man unterscheidet:
  - Flächenmomente 1. Ordnung (**statische Momente**)
  - Flächenmomente 2. Ordnung (**Flächenträgheitsmomente**)

### 6.1 Statische Momente und Schwerpunktermittlung

Wdh.: Berechnung der äquivalenten Einzelkraft einer Kräftegruppe

> Skizze: Waagerechter Balken mit parallelen, nach unten gerichteten Einzelkräften $F_1, F_2, F_3, \dots, F_i, \dots, F_n$ (rot); dazu die Resultierende $F_R$ (rot, länger). Grüne Abstandspfeile vom linken Bezugspunkt: $x_1, x_2, x_3$ und $x_R$ (Lage der Resultierenden).

$$F_R = \sum_{i=1}^{n} F_i \qquad x_R = \frac{\sum_{i=1}^{n} x_i F_i}{\sum_{i=1}^{n} F_i}$$

vgl. Streckenlasten:
$\to$ kontinuierliche Kräfteverteilung führt auf Integrale statt Summen

$$F_R = \int dF(x) \qquad x_R = \frac{\int x\,dF(x)}{\int dF(x)}$$

---

## Seite 2

$\to$ Fläche und Schwerpunkt

> Skizze: Fläche über der $x$-Achse (oberer Rand unregelmäßig), in senkrechte Streifen zerlegt; ein Streifen $dA$ schraffiert; Abstand $x_R$ vom Ursprung zur Resultierenden.

$$A = \int_A dA \qquad x_R = \frac{\int_A x\,dA}{\int_A dA}$$

- Übergang auf beliebige Flächen $\to$ Schwerpunktermittlung bei Flächen

> Skizze: Beliebig berandete ebene Fläche im $\bar x$-$\bar y$-System (Ursprung links unten). Schwerpunkt S mit eigenem Achsenkreuz $x$, $y$ (parallel). Flächenelement $dA = dx\,dy$ (schraffiertes Quadrat) mit Koordinaten $\bar x, \bar y$ (grün, im $\bar x$-$\bar y$-System); Schwerpunktkoordinaten $\bar x_S, \bar y_S$ (grün). Je ein senkrechter und ein waagerechter Streifen schraffiert.

Schwerpunktlage bei ebenen Flächen:

$$\boxed{\bar x_S = \frac{\int_A \bar x\,dA}{\int_A dA}} \quad (6.1.1) \qquad \boxed{\bar y_S = \frac{\int_A \bar y\,dA}{\int_A dA}} \quad (6.1.2)$$

---

## Seite 3

Die Terme $\int_A \bar x\,dA$ und $\int_A \bar y\,dA$ werden als **statische Momente** oder **Flächenmomente 1. Ordnung** bezeichnet.

$$\boxed{S_{\bar y} = \int_A \bar x\,dA} \quad (= \bar x_S\cdot A) \quad \text{Flächenmoment 1. Ordnung bezogen auf } \bar y\text{-Achse}$$
(wie ein Moment mit $A$ statt $F$)

> Skizze: Fläche mit senkrechtem schraffiertem Streifen (Abstand zur $\bar y$-Achse).

$$\boxed{S_{\bar x} = \int_A \bar y\,dA} \quad (= \bar y_S\cdot A) \quad \text{Flächenmoment 1. Ordnung bezogen auf die } \bar x\text{-Achse}$$

> Skizze: Fläche mit waagerechtem schraffiertem Streifen.

**WICHTIG:**
- Die statischen Momente in Bezug auf die Schwerpunktachsen $x$ und $y$ sind Null.
- Der Schwerpunkt liegt stets auf der Symmetrielinie.

**Beispiel:** Berechnung des Flächenschwerpunkts einer Viertelkreisfläche

> Skizze: Viertelkreis mit Radius $R$ im ersten Quadranten des $\bar x$-$\bar y$-Systems. Polarkoordinaten: Radius $r$, Winkel $\varphi$ (von der $\bar x$-Achse), Flächenelement mit Seiten $dr$ und $r\,d\varphi$ (grün), $dA = dr\cdot r\,d\varphi$.

$\bar x = r\cos\varphi$
$\bar y = r\sin\varphi$

---

## Seite 4

$$\bar x_S = \frac{\int_A \bar x\,dA}{\int dA} = \frac{\int_0^{\pi/2}\int_0^R r\cos\varphi\,dr\,r\,d\varphi}{\int_0^{\pi/2}\int_0^R dr\,r\,d\varphi} = \frac{\int_0^{\pi/2}\int_0^R r^2\cos\varphi\,dr\,d\varphi}{\int_0^{\pi/2}\int_0^R r\,dr\,d\varphi} = \frac{\int_0^{\pi/2}\frac{R^3}{3}\cos\varphi\,d\varphi}{\int_0^{\pi/2}\frac{R^2}{2}\,d\varphi}$$

$$\bar x_S = \frac{\left[\frac{R^3}{3}\sin\varphi\right]_0^{\pi/2}}{\left[\frac{R^2}{2}\varphi\right]_0^{\pi/2}} = \frac{\frac{R^3}{3}}{\frac{R^2}{2}\frac{\pi}{2}} = \underline{\frac{4}{3}\frac{R}{\pi}}$$

$$\bar y_S = \frac{\int_A \bar y\,dA}{\int dA} = \frac{\int_0^{\pi/2}\int_0^R r\sin\varphi\,dr\,r\,d\varphi}{\int_0^{\pi/2}\int_0^R dr\,r\,d\varphi} = \frac{\int_0^{\pi/2}\frac{R^3}{3}\sin\varphi\,d\varphi}{\int_0^{\pi/2}\frac{R^2}{2}\,d\varphi} = \frac{\left[-\frac{R^3}{3}\cos\varphi\right]_0^{\pi/2}}{\left[\frac{R^2}{2}\varphi\right]_0^{\pi/2}} = \frac{+\frac{R^3}{3}}{\frac{R^2}{2}\frac{\pi}{2}}$$

$$\bar y_S = \underline{+\frac{4}{3}\frac{R}{\pi} \approx 0{,}424\,R}$$

> Skizze: Viertelkreis im $\bar x$-$\bar y$-System mit eingezeichnetem Schwerpunkt S bei $(\bar x_S, \bar y_S)$.

[Prüfung: $4/(3\pi) = 0{,}4244$ – korrekt.]

---

## Seite 5

**Übersicht zu Flächenmomenten einfacher Flächen**

$\to$ Was braucht man? Schwerpunkte, Fläche, $I$ (FTM)

> Skizze: Allgemeines Dreieck, Basis $b$, Höhe $h$; Schwerpunkt S im Abstand $h/3$ (grün umkreist) über der Basis.

$$A = \frac{b\cdot h}{2}$$

> Skizze: Rechteck, Breite $b$, Höhe $h$, Schwerpunktachsen $x$ (waagerecht) und $y$ (senkrecht) durch S; Abstände $b/2$ und $h/2$ (grün umkreist).

$$A = b\cdot h \qquad I_{xx} = \frac{bh^3}{12} \qquad I_{yy} = \frac{b^3h}{12} \qquad I_{xy} = 0$$

> Skizze: Zwei rechtwinklige Dreiecke (Breite $b$, Höhe $h$) mit Schwerpunktachsen $x$, $y$ durch S; Schwerpunktabstände $b/3$ und $h/3$ (grün umkreist) jeweils von den Katheten.
> – links: rechter Winkel unten rechts (senkrechte Kathete rechts), Hypotenuse von links unten nach rechts oben: $I_{xy} = \dfrac{b^2h^2}{72}$
> – rechts: rechter Winkel unten links (senkrechte Kathete links), Hypotenuse von links oben nach rechts unten: $I_{xy} = -\dfrac{b^2h^2}{72}$

$$I_{xx} = \frac{bh^3}{36} \qquad I_{yy} = \frac{b^3h}{36}$$

[Prüfung: Mit der in 6.3.1 (S. 17, Gl. 6.3.2) eingeführten Konvention $I_{xy} = -\int_A xy\,dA$ sind beide Vorzeichen vertauscht: linkes Dreieck (rechter Winkel unten rechts) $I_{xy} = -\frac{b^2h^2}{72}$, rechtes Dreieck (rechter Winkel unten links) $I_{xy} = +\frac{b^2h^2}{72}$. Die Angaben im Original entsprechen der Konvention $I_{xy} = +\int xy\,dA$. Beträge $I_{xx}$, $I_{yy}$, $|I_{xy}|$ korrekt.]

---

## Seite 6

(Kasten: „als extra Blatt anfangen bei stat. Momente; dann FTM")

(grün) $\alpha$ im Bogenmaß!

> Skizze: Kreis, Radius $R$, Schwerpunkt S im Mittelpunkt, Achsen $x$, $y$.

$$A = \pi R^2 \qquad I_{xx} = I_{yy} = \frac{\pi R^4}{4} \qquad I_{xy} = 0$$

> Skizze: Kreisausschnitt (Sektor), Spitze unten, symmetrisch zur senkrechten $y$-Achse, halber Öffnungswinkel $\alpha$ beidseitig, Radius $R$; Schwerpunkt S auf der Symmetrieachse im Abstand $\dfrac{2R\sin\alpha}{3\alpha}$ (grün umkreist) von der Spitze; Achse $x$ waagerecht durch S.

$$A = R^2\alpha \qquad I_{xx} = \frac{R^4}{72}\left(18\alpha + 9\sin 2\alpha - 32\frac{\sin^2\alpha}{\alpha}\right)$$
$$I_{yy} = \frac{R^4}{8}(2\alpha - \sin 2\alpha) \qquad I_{xy} = 0$$

$\alpha = \pi/2$:

> Skizze: Halbkreis, Basis unten, Schwerpunkt S auf der $y$-Achse im Abstand $\dfrac{4}{3}\dfrac{R}{\pi}$ (grün umkreist) über der Basis.

$$A = \frac{\pi}{2}R^2$$
$$I_{xx} = \frac{R^4}{72}\left(9\pi - \frac{64}{\pi}\right) = R^4\left(\frac{\pi}{8} - \frac{8}{9\pi}\right)$$
(Vorzeichen im Original überschrieben, vermutlich von „+" zu „−" korrigiert [?])
$$I_{yy} = \frac{R^4}{8}(\pi - 0) = \frac{R^4\pi}{8} \qquad I_{xy} = 0$$

[Prüfung: Sektorformeln aus $I = \frac{R^4}{8}(2\alpha \pm \sin 2\alpha)$ und Steiner mit $y_S = \frac{2R\sin\alpha}{3\alpha}$ nachgerechnet – korrekt. Halbkreis: $I_{xx} = R^4(\pi/8 - 8/(9\pi)) = 0{,}1098\,R^4$; richtig ist das Minuszeichen.]

---

## Seite 7

- **Berechnung von Schwerpunkten zusammengesetzter Flächen**

$\to$ Flächen können in Teilflächen zerlegt werden, deren Schwerpunktlage bekannt ist
$\curvearrowright$ in den Glgn. (6.1.1), (6.1.2) kann Integration durch Summation ausgetauscht werden

$$\bar x_S = \frac{\int_A \bar x\,dA}{\int_A dA} \;\Rightarrow\; \boxed{\bar x_S = \frac{\sum_{i=1}^n \bar x_{Si}A_i}{\sum_{i=1}^n A_i}} \quad (6.1.3)$$

$$\bar y_S = \frac{\int_A \bar y\,dA}{\int_A dA} \;\Rightarrow\; \boxed{\bar y_S = \frac{\sum_{i=1}^n \bar y_{Si}A_i}{\sum_{i=1}^n A_i}} \quad (6.1.4)$$

**Beispiel:** Berechnung des Schwerpunktes einer zusammengesetzten Fläche

> Skizze: Im $\bar x$-$\bar y$-System: Fläche aus (1) rechtwinkligem Dreieck mit Ecken $(0,0)$, $(3a,0)$, $(3a,6a)$ und (2) Rechteck $3a \times 6a$ von $\bar x = 3a$ bis $6a$; (3) kreisförmiges Loch (Mittelpunkt $\bar x = 4{,}5a$, Höhe $4a$). Bemaßung grün: $3a$, $3a$ (horizontal), $6a$ (Gesamthöhe), $4a$ (Höhe des Kreismittelpunkts). Teilschwerpunkte $S_1, S_2, S_3$ und Gesamtschwerpunkt $S_{ges}$ eingezeichnet.

Fläche zusammengesetzt aus
1. Dreieck
2. Rechteck
3. Kreis

---

## Seite 8

| $i$ | $\bar x_{Si}\,[a]$ | $\bar y_{Si}\,[a]$ | $A_i\,[a^2]$ | $\bar x_{Si}A_i\,[a^3]$ | $\bar y_{Si}A_i\,[a^3]$ |
|---|---|---|---|---|---|
| 1 | 2 | 2 | 9 | 18 | 18 |
| 2 | 4,5 | 3 | 18 | 81 | 54 |
| 3 | 4,5 | 4 | $-\pi$ | −14,14 | −12,57 |
| $\Sigma$ | | | 23,86 | 84,86 | 59,43 |

(grün: $A = \frac{\pi}{4}d^2$, d. h. Lochdurchmesser $d = 2a$)

$$\bar x_S = \frac{\sum_1^3 \bar x_{Si}A_i}{\sum_1^3 A_i} = \frac{84{,}86\,a^3}{23{,}86\,a^2} = \underline{3{,}55\,a}$$

$$\bar y_S = \frac{\sum_1^3 \bar y_{Si}A_i}{\sum_1^3 A_i} = \frac{59{,}43\,a^3}{23{,}86\,a^2} = \underline{2{,}49\,a}$$

(Randnotiz: „weiteres Bsp.!")

[Prüfung: Tabellenwerte korrekt. $84{,}863/23{,}858 = 3{,}557$ $\Rightarrow$ gerundet $3{,}56\,a$ (Original: 3,55 a, Rundungsabweichung); $\bar y_S = 2{,}49\,a$ korrekt.]

### 6.2 Schwerpunktermittlung bei Massen, Volumina und Linien

- Glgn. (6.1.1) und (6.1.2) können analog für Massen, Volumina und Linien angewendet werden
  $\to$ ersetze $A$ durch Masse $m$, Volumen $V$, Linienlänge $L$

| | Masse $m$ | Volumen $V$ | Fläche $A$ | Linie $L$ |
|---|---|---|---|---|
| $\bar x_S =$ | $\dfrac{\int_m \bar x\,dm}{\int_m dm}$ | $\dfrac{\int_V \bar x\,dV}{\int_V dV}$ | $\dfrac{\int_A \bar x\,dA}{\int_A dA}$ | $\dfrac{\int_L \bar x\,dL}{\int_L dL}$ |

$\to \bar y_S$, $\bar z_S$ analog

---

## Seite 9

(Aufgeklebter Zettel: „Ergänzung Linienschwerpunkte")

**Linienschwerpunkte**

> Skizze: Achsenkreuz $x$, $y$.

$$x_S = \frac{\int_L x\,dL}{\int_L dL} \qquad y_S = \frac{\int_L y\,dL}{\int dL}$$

**(A) Linie gedreht**

> Skizze: Gerade Linie der Länge $L$ vom Ursprung unter dem Winkel $\alpha$ zur $x$-Achse; Endpunkt bei $x = L\cos\alpha$, $y = L\sin\alpha$. Linienelement $dL$ mit Projektionen $dx$, $dy$ (grün, Steigungsdreieck mit Winkel $\alpha$).

$\sin\alpha = \dfrac{dy}{dL} \to dL = \dfrac{dy}{\sin\alpha}$
$\cos\alpha = \dfrac{dx}{dL} \to dL = \dfrac{dx}{\cos\alpha}$

$$x_S = \frac{\int_L x\,dL}{\int_L dL} = \frac{\int_0^{L\cos\alpha} x\frac{dx}{\cos\alpha}}{\int_0^{L\cos\alpha}\frac{dx}{\cos\alpha}} = \frac{\frac{1}{\cos\alpha}\frac{x^2}{2}\Big|_0^{L\cos\alpha}}{\frac{1}{\cos\alpha}x\Big|_0^{L\cos\alpha}} = \frac{L^2\cos^2\alpha}{2L\cos\alpha} = \underline{\frac{1}{2}L\cos\alpha}$$

---

## Seite 10

$$y_S = \frac{\int_L y\,dL}{\int_L dL} = \frac{\int_0^{L\sin\alpha} y\frac{dy}{\sin\alpha}}{\int_0^{L\sin\alpha}\frac{dy}{\sin\alpha}} = \frac{\frac{1}{\sin\alpha}\frac{y^2}{2}\Big|_0^{L\sin\alpha}}{\frac{1}{\sin\alpha}y\Big|_0^{L\sin\alpha}} = \underline{\underline{\frac{1}{2}L\sin\alpha}}$$

(rot) $\curvearrowright$ der Schwerpunkt einer geraden Linie ist immer in der Mitte! unabhängig vom Drehwinkel!

$\curvearrowright$
- $\alpha = 0 \to x_S = \frac{L}{2}$, $y_S = 0$
  > Skizze: waagerechte Linie auf der $x$-Achse, S in der Mitte.
- $\alpha = 90° \to x_S = 0$, $y_S = \frac{L}{2}$
  > Skizze: senkrechte Linie auf der $y$-Achse, S in der Mitte.
- $\alpha = 45° \to x_S = \frac{L}{4}\sqrt{2}$, $y_S = \frac{L}{4}\sqrt{2}$
  > Skizze: Linie unter 45°, S in der Mitte mit Koordinaten $x_S$, $y_S$ (gestrichelt).

[Prüfung: korrekt. Hinweis: Für $\alpha = 0$ bzw. $90°$ ist die Substitution $dL = dy/\sin\alpha$ bzw. $dx/\cos\alpha$ nicht definiert; die Endergebnisse gelten aber als Grenzwerte.]

---

## Seite 11

**(B) Kreisbogen** (Kasten: s. Dankert, Gross TM 1)

> Skizze: Kreisbogen (Radius $r$) symmetrisch zur $y$-Achse, Mittelpunkt im Ursprung (unten), halber Öffnungswinkel $\alpha$ beidseitig der $y$-Achse; Bogenlänge $L = 2\alpha\cdot r$; Bogenelement $dL$ unter dem Winkel $d\alpha$; Sehne $b$ (grün), Stichhöhe $h$ (grün). Nebenskizze: Radius $r$ unter Winkel $\alpha$ zur $y$-Achse $\to y = r\cdot\cos\alpha$.

$y = r\cdot\cos\alpha$
$dL = d\alpha\cdot r$

$x_S = 0$

$$y_S = \frac{\int_L y\,dL}{\int_L dL} = \frac{\int_0^\alpha r^2\cos\alpha\,d\alpha}{\int_0^\alpha r\,d\alpha} = \frac{r^2\sin\alpha\big|_0^\alpha}{r\,\alpha} = \underline{\underline{r\frac{\sin\alpha}{\alpha}}}$$

[Prüfung: korrekt (Integration wegen Symmetrie nur über eine Hälfte). Formal unsauber: Integrationsvariable und obere Grenze tragen beide das Symbol $\alpha$.]

---

## Seite 12

$\curvearrowright$ für Viertelkreis(bogen)

> Skizze: Viertelkreisbogen im ersten Quadranten, Schwerpunkt S mit $x_S$, $y_S$.

$\to$ Nutzung der gleichen Beziehungen

> Skizze: Bogen mit Radius $r$, Winkel $\alpha$ gemessen von der $y$-Achse; grün: Projektionen $x$ und $y$; Bogenelement $dL$ unter $d\alpha$.

$y = r\cos\alpha$
$x = r\sin\alpha$
$dL = d\alpha\cdot r$

$$x_S = \frac{\int_L x\,dL}{\int_L dL} = \frac{\int_0^\alpha r\sin\alpha\,r\,d\alpha}{\int_0^\alpha r\,d\alpha}$$

$$\boxed{x_S = -\frac{r^2\cos\alpha\big|_0^\alpha}{r\,\alpha} = -\frac{(\cos\alpha - 1)r}{\alpha}}$$

s. vorher: $\boxed{y_S = r\dfrac{\sin\alpha}{\alpha}}$

$\alpha = \frac{\pi}{2} \to x_S = -\frac{2}{\pi}(-1)r = \frac{2r}{\pi} = \underline{0{,}6366}$
$\qquad\;\; y_S = r\frac{2\cdot 1}{\pi} = \frac{2r}{\pi} = 0{,}6366$

[Prüfung: korrekt; Einheit fehlt im Original: $0{,}6366\,r$.]

---

## Seite 13

**1. Fall**

> Skizze: Viertelkreisbogen im ersten Quadranten (Mittelpunkt im Ursprung), Schwerpunkt S bei $x_S = \frac{2r}{\pi}$, $y_S = \frac{2r}{\pi}$.

$x_S = 0{,}636\,r$
$y_S = 0{,}636\,r$

**2. Fall** mit KOS für $x_S = 0$

> Skizze: derselbe Viertelkreisbogen, aber symmetrisch zur $y$-Achse gelegt (Öffnung nach oben, Mittelpunkt im Ursprung), Öffnungswinkel $2\alpha = 2\frac{\pi}{4} = \frac{\pi}{2}$; S auf der $y$-Achse bei $0{,}9\,r$.

$x_S = 0$
$y_S = 0{,}90\,r$

$\curvearrowleft$ identisch mit Rotationsmatrix

$$\begin{pmatrix}\cos\alpha & -\sin\alpha\\ \sin\alpha & \cos\alpha\end{pmatrix}\begin{pmatrix}P_x\\ P_y\end{pmatrix}, \qquad \underline{\alpha = -\frac{\pi}{4}}$$

[Prüfung: $y_S = r\sin(\pi/4)/(\pi/4) = 0{,}9003\,r = \sqrt 2\cdot 0{,}6366\,r$ – korrekt. Mit der angegebenen (aktiven) Drehmatrix ergibt $\alpha = -\pi/4$ jedoch $(0{,}90\,r;\;0)$, also S auf der $x$-Achse; für $(0;\;0{,}90\,r)$ ist $\alpha = +\pi/4$ einzusetzen. $\alpha = -\pi/4$ passt nur bei Drehung des Koordinatensystems (dann transponierte Matrix).]

(Rest der Seite leer.)

---

## Seite 14

**Beispiel:**

> Skizze: Im $\bar x$-$\bar y$-System: (1) rechtwinkliges Dreieck links der $\bar y$-Achse mit Ecken $(-(a-c), 0)$, $(0,0)$, $(0,b)$; (2) Rechteck $c \times b$ rechts der $\bar y$-Achse von $\bar x = 0$ bis $c$. Aufhängepunkt A an der oberen linken Ecke des Rechtecks (auf der $\bar y$-Achse, Höhe $b$). Teilschwerpunkte $S_1$, $S_2$. Bemaßung grün: Höhe $b$, Rechteckbreite $c$, Gesamtbreite $a$.

- Aufhängung am Punkt A
$\to$ Wie groß muss $c$ sein, damit untere Kante waagerecht liegt?

**Lös.:**
- Schwerpunkt muss auf $\bar y$-Achse liegen!
  $\curvearrowright \bar x_S \overset{!}{=} 0$!

| $i$ | $\bar x_{Si}$ | $A_i$ | $\bar x_{Si}A_i$ |
|---|---|---|---|
| 1 | $-\frac{a-c}{3}$ | $\frac{(a-c)b}{2}$ | $-\frac{(a-c)^2b}{6}$ |
| 2 | $\frac{c}{2}$ | $cb$ | $\frac{c^2b}{2}$ |
| $\Sigma$ | | $\frac{(a+c)b}{2}$ | (s. u.) |

Nebenrechnung $\Sigma A_i$:
$\frac{(a-c)b}{2} + cb = \frac{ab}{2} - \frac{bc}{2} + cb = \frac{ab}{2} + \frac{cb}{2} = \frac{(a+c)b}{2}$

Nebenrechnung $\Sigma \bar x_{Si}A_i$:
$-\frac{(a^2 - 2ac + c^2)b}{6} + \frac{c^2b}{2} = -\frac{a^2b}{6} + \frac{2acb}{6} - \frac{bc^2}{6} + \frac{c^2b}{2} = b\left(-\frac{a^2}{6} + \frac{ac}{3} + \frac{c^2}{3}\right)$

$$\bar x_S = \frac{\sum \bar x_{Si}A_i}{\sum A_i} \overset{!}{=} 0 = \frac{2b\left(-\frac{a^2}{6} + \frac{ac}{3} + \frac{c^2}{3}\right)}{(a+c)b}$$

---

## Seite 15

$\curvearrowright$ Zähler muss Null werden!

$b\left(-\frac{a^2}{6} + \frac{ac}{3} + \frac{c^2}{3}\right) = 0 \quad |\cdot 3$
$-\frac{a^2}{2} + ac + c^2 = 0$
$c^2 + ac - \frac{a^2}{2} = 0$

(grün, Erinnerung: $ax^2 + bx + c = 0 \Rightarrow x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$)

$\to c_{1,2} = -\frac{a}{2} \pm \sqrt{\frac{a^2}{4} + \frac{a^2}{2}} = -\frac{a}{2} \pm \sqrt{\frac{3}{4}a^2}$

$c_1 = -\frac{a}{2} + \sqrt{\frac{3}{4}}\,a$

$$\underline{c_1 = a\left(\sqrt{\tfrac{3}{4}} - \tfrac{1}{2}\right) = 0{,}366\,a}$$

$\left(-\frac{a}{2} - \sqrt{\frac{3}{4}}\,a\right)$! nicht sinnvoll.

[Prüfung: $\sqrt{0{,}75} - 0{,}5 = 0{,}3660$ – korrekt.]

---

## Seite 16

$\curvearrowright$ dies gilt auch für die Berechnung aus bekannten Teilmassen, Teilvolumina und Einzellinien:

| | Masse $m$ | Volumen $V$ | Fläche $A$ | Linie $L$ |
|---|---|---|---|---|
| $\bar x_S =$ | $\dfrac{\sum \bar x_{Si}m_i}{\sum m_i}$ | $\dfrac{\sum \bar x_{Si}V_i}{\sum V_i}$ | $\dfrac{\sum \bar x_{Si}A_i}{\sum A_i}$ | $\dfrac{\sum \bar x_{Si}L_i}{\sum L_i}$ |

$\to \bar y_S$, $\bar z_S$ analog

### 6.3 Flächenmomente 2. Ordnung

#### 6.3.1 Definition

> Skizze: Beliebige Fläche im $\bar x$-$\bar y$-System; Schwerpunkt S mit parallelem $x$-$y$-System; Flächenelement $dA = d\bar x\,d\bar y$ mit Koordinaten $\bar x, \bar y$ (bzgl. $\bar x$-$\bar y$) und $x, y$ (bzgl. S).

**Axiale Flächenträgheitsmomente** (= Flächenmomente 2. Ordnung) bezüglich der Achsen $\bar x$ oder $\bar y$ bzw. $x$ oder $y$:

$$\boxed{I_{\bar x\bar x} = \int_A \bar y^2\,dA} \qquad \boxed{I_{xx} = \int_A y^2\,dA} \quad (6.3.1)$$
$$\boxed{I_{\bar y\bar y} = \int_A \bar x^2\,dA} \qquad \boxed{I_{yy} = \int_A x^2\,dA}$$

---

## Seite 17

**Deviationsmoment** (Zentrifugalmoment) bezüglich der Achsen $\bar x$ und $\bar y$ bzw. $x$ und $y$:

$$\boxed{I_{\bar x\bar y} = -\int_A \bar x\bar y\,dA} \qquad \boxed{I_{xy} = -\int_A xy\,dA} \quad (6.3.2)$$

$\to$ die Deviationsmomente können positiv, negativ oder gleich Null sein
$\to$ die axialen Flächenträgheitsmomente sind stets größer Null

**Beispiel:** Flächenträgheitsmomente eines Rechtecks

> Skizze: Rechteck (Breite $b$, Höhe $h$) mit linker unterer Ecke im Ursprung des $\bar x$-$\bar y$-Systems; Flächenelement $dA$.

$dA = d\bar x\,d\bar y$

$$I_{\bar x\bar x} = \int_A \bar y^2\,dA = \int_0^b\int_0^h \bar y^2\,d\bar y\,d\bar x = \underline{\frac{h^3b}{3}}$$
$$I_{\bar y\bar y} = \int_A \bar x^2\,dA = \int_0^b\int_0^h \bar x^2\,d\bar y\,d\bar x = \underline{\frac{hb^3}{3}}$$
$$I_{\bar x\bar y} = -\int_A \bar x\bar y\,dA = -\int_0^b\int_0^h \bar x\bar y\,d\bar y\,d\bar x = \underline{-\frac{b^2h^2}{4}}$$

[Prüfung: korrekt.]

---

## Seite 18

> Skizze: Rechteck (Breite $b$, Höhe $h$), symmetrisch zur senkrechten Achse $\bar y = y$, Unterkante auf der $\bar x$-Achse; Flächenelement $dA$.

$$I_{\bar x\bar x} = \int \bar y^2\,dA = \int_{-b/2}^{b/2}\int_0^h \bar y^2\,d\bar y\,d\bar x = \frac{h^3}{3}\left(\frac{b}{2} + \frac{b}{2}\right) = \frac{h^3b}{3}$$

$$I_{\bar y\bar y} = \int \bar x^2\,dA = \int_{-b/2}^{b/2}\int_0^h \bar x^2\,d\bar y\,d\bar x = \int_{-b/2}^{b/2} h\bar x^2\,d\bar x = \frac{h}{3}\left[\bar x^3\right]_{-b/2}^{b/2} = \frac{h}{3}\left[\frac{b^3}{8} - \left(-\frac{b^3}{8}\right)\right]$$

$$\underline{I_{\bar y\bar y} = \frac{b^3h}{12}}$$

(grün: $\curvearrowright$ Änderung, da andere Bezugsachse)

$$I_{\bar x\bar y} = -\int_{-b/2}^{b/2}\int_0^h \bar x\bar y\,d\bar y\,d\bar x = -\int_{-b/2}^{b/2}\bar x\frac{h^2}{2}\,d\bar x = -\frac{h^2}{2}\left[\frac{\bar x^2}{2}\right]_{-b/2}^{+b/2} = -\frac{h^2}{4}\left[\frac{b^2}{4} - \frac{b^2}{4}\right] = \underline{\underline{0}}$$

(grün umrandet) $\to$ ist Bezugsachse gleich der Symmetrieachse, dann ist $I_{xy} = 0$

[Prüfung: korrekt.]

---

## Seite 19

> Skizze: Rechteck (Breite $b$, Höhe $h$) links der $\bar y$-Achse (zweiter Quadrant), Unterkante auf der $\bar x$-Achse; Flächenelement $dA$.

$$I_{\bar x\bar y} = -\int_A \bar x\bar y\,dA = -\int_{-b}^0\int_0^h \bar x\bar y\,d\bar y\,d\bar x = -\int_{-b}^0 \bar x\frac{h^2}{2}\,d\bar x = \underline{+\frac{b^2h^2}{4}}$$

(grün umrandet) $\to$ Spiegeln der Fläche an einer Achse führt zu einem Vorzeichenwechsel bei $I_{xy}$ (Deviationsmoment)

[Prüfung: korrekt.]

#### 6.3.2 Satz von Steiner

**Satz von Steiner** $\to$ Transformation von Flächenträgheitsmomenten bezüglich einer allgemeinen Achse auf die dazu parallele Schwerpunktachse und umgekehrt.

> Skizze: Beliebige Fläche im $\bar x$-$\bar y$-System, Schwerpunkt S mit parallelem $x$-$y$-System; Flächenelement $dA = d\bar x\,d\bar y = dx\,dy$; grün: $\bar x = \bar x_S + x$, $\bar y = \bar y_S + y$ als Abstandspfeile.

---

## Seite 20

Es gilt:
$$\bar x = \bar x_S + x \qquad \bar y = \bar y_S + y$$
($\bar x_S, \bar y_S$ … Schwerpunktkoordinaten im $\bar x$-$\bar y$-KOS)

$$I_{\bar x\bar x} = \int_A \bar y^2\,dA = \int_A(\bar y_S + y)^2\,dA = \int_A\left(\bar y_S^2 + 2\bar y_S y + y^2\right)dA$$
$$= \bar y_S^2\underbrace{\int_A dA}_{=A} + 2\bar y_S\underbrace{\int_A y\,dA}_{=0} + \underbrace{\int_A y^2\,dA}_{I_{xx}}$$
($\int_A y\,dA$: stat. Moment in Bezug auf $x$-Achse = Schwerpunktachse)

$$I_{\bar x\bar x} = \bar y_S^2A + I_{xx}$$

$\curvearrowright$
$$\boxed{\begin{aligned} I_{\bar x\bar x} &= I_{xx} + \bar y_S^2A\\ I_{\bar y\bar y} &= I_{yy} + \bar x_S^2A\\ I_{\bar x\bar y} &= I_{xy} - \bar x_S\bar y_SA \end{aligned}} \quad \text{Satz von Steiner}$$

- Von allen parallelen Achsen sind die axialen Flächenträgheitsmomente bezüglich der Schwerpunktachsen die kleinsten.

---

## Seite 21

#### 6.3.3 Flächenmomente 2. Ordnung für zusammengesetzte Flächen

**Satz:** Lässt sich eine gegebene Querschnittsfläche $A$ in solche Teilflächen $A_i$ zerlegen, deren Flächenträgheitsmomente bezüglich eines beliebigen Koordinatensystems $\bar x, \bar y$ (oder auch $\bar y, \bar z$) bekannt sind, dann sind die Trägheitsmomente der Gesamtfläche bezüglich dieses Achsensystems gleich der Summe der Trägheitsmomente der Teilflächen.
Aussparungen werden als „negative Teilflächen" aufgefasst, d. h. die zugehörigen Flächenträgheitsmomente sind zu subtrahieren.

$\to$ **Vorgehensweise** bei der Berechnung von Flächenträgheitsmomenten (FTM) bezüglich des Schwerpunkts der Gesamtfläche bei bekannten Teilflächen:

1. Berechnung des Schwerpunktes (Koordinaten) der Gesamtfläche $\to \bar x_S, \bar y_S$
2. Berechnung der FTMe der Teilflächen bezüglich ihrer eigenen Schwerpunktachsen $\to I_{xxi}, I_{yyi}, I_{xyi}$
3. Berechnung der Steineranteile der Teilflächen bezüglich der Schwerpunktachsen der Gesamtfläche $\to y_{Si}^2A_i$, $x_{Si}^2A_i$, $x_{Si}y_{Si}A_i$

---

## Seite 22

4. Addition der Anteile aller Teilflächen $\to I_{xx}, I_{yy}, I_{xy}$

$$\boxed{\begin{aligned} I_{xx} &= \sum_{i=1}^n I_{\bar x\bar x i} = \sum_{i=1}^n\left(I_{xxi} + y_{Si}^2A_i\right)\\ I_{yy} &= \sum_{i=1}^n I_{\bar y\bar y i} = \sum_{i=1}^n\left(I_{yyi} + x_{Si}^2A_i\right)\\ I_{xy} &= \sum_{i=1}^n I_{\bar x\bar y i} = \sum_{i=1}^n\left(I_{xyi} - x_{Si}y_{Si}A_i\right) \end{aligned}} \quad (6.3.3)$$

(grün, Legende:)
- $I_{xx}, I_{yy}, I_{xy}$ – FTMe der Gesamtfläche bezüglich ihrer Schwerpunktachsen
- $I_{xxi}, I_{yyi}, I_{xyi}$ – FTMe der $i$-ten Teilfläche bezüglich ihrer eigenen Schwerpunktachsen
- $I_{\bar x\bar x i}, I_{\bar y\bar y i}, I_{\bar x\bar y i}$ – FTMe der $i$-ten Teilfläche bezüglich der Schwerpunktachsen der Gesamtfläche
- $x_{Si}, y_{Si}$ – Abstand des Schwerpunktes der $i$-ten Teilfläche vom Schwerpunkt der Gesamtfläche in $x$- bzw. $y$-Richtung mit
  $x_{Si} = \bar x_{Si} - \bar x_S$, $\quad y_{Si} = \bar y_{Si} - \bar y_S$

---

## Seite 23

**Beispiel:** (L-Profil)

> Skizze: L-förmige Fläche im $\bar x$-$\bar y$-System: (1) senkrechter Schenkel, Breite $a$, Höhe $4a$, von $\bar x = 0$ bis $a$; (2) waagerechter Schenkel rechts unten, Breite $2a$, Höhe $a$, von $\bar x = a$ bis $3a$. Bemaßung grün: $4a$ (Gesamthöhe), $3a$ (Gesamtbreite), $2a$, $a$. Teilschwerpunkte $S_1$, $S_2$ mit eigenen Achsen $x_1, y_1$ bzw. $x_2, z$ [?] (grün).

geg.: $a$
ges.: $I_{xx}, I_{yy}, I_{xy}$

**(1) Schwerpunkt**

| $i$ | $\bar x_{Si}\,[a]$ | $\bar y_{Si}\,[a]$ | $A_i\,[a^2]$ | $\bar x_{Si}A_i\,[a^3]$ | $\bar y_{Si}A_i\,[a^3]$ |
|---|---|---|---|---|---|
| 1 | 1/2 | 2 | 4 | 2 | 8 |
| 2 | 2 | 1/2 | 2 | 4 | 1 |
| $\Sigma$ | / | / | 6 | 6 | 9 |

$$\bar x_S = \frac{\sum\bar x_{Si}A_i}{\sum A_i} = \frac{6a^3}{6a^2} = \underline{a} \qquad \bar y_S = \frac{\sum\bar y_{Si}A_i}{\sum A_i} = \frac{9a^3}{6a^2} = \underline{\frac{3}{2}a}$$

---

## Seite 24

**(2) FTMe** $\quad$ (Rechteck: $\frac{bh^3}{12}$ $\to$ Tabellen!)

| $i$ | $x_{Si} = \bar x_{Si} - \bar x_S\,[a]$ | $y_{Si} = \bar y_{Si} - \bar y_S\,[a]$ | $A_i\,[a^2]$ | $I_{xxi}\,[a^4]$ | $y_{Si}^2A_i\,[a^4]$ | $I_{yyi}\,[a^4]$ | $x_{Si}^2A_i\,[a^4]$ | $I_{xy}\,[a^4]$ | $x_{Si}y_{Si}A_i\,[a^4]$ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | $\frac12 - 1 = -\frac12$ | $2 - \frac32 = \frac12$ | 4 | $\frac{1\cdot 4^3}{12} = \frac{16}{3}$ | $(\frac12)^2\cdot 4$ | $\frac{1^3\cdot 4}{12}$ | $\frac14\cdot 4$ | 0 | $(-\frac12)\frac12\cdot 4$ |
| 2 | $2 - 1 = 1$ | $\frac12 - \frac32 = -1$ | 2 | $\frac{2\cdot 1^3}{12}$ | $(-1)^2\cdot 2$ | $\frac{2^3\cdot 1}{12}$ | $1^2\cdot 2$ | 0 | $1\cdot(-1)\cdot 2$ |
| $\Sigma$ | / | / | 6 | $\frac{11}{2}$ | 3 | 1 | 3 | 0 | −3 |

(unter den Spaltenpaaren: „+", „+", „−")

mit 6.3.3:
$$I_{xx} = \frac{11}{2}a^4 + 3a^4 = \underline{8{,}5\,a^4}$$
$$I_{yy} = 1a^4 + 3a^4 = \underline{4\,a^4}$$
$$I_{xy} = 0a^4 - (-3a^4) = \underline{3\,a^4}$$

[Prüfung: alle Tabellenwerte und Ergebnisse nachgerechnet – korrekt.]

$\curvearrowright$ **Tabelle als Rechenschema!**

> (grün umrandet) Schwerpunkt-Tabelle: $i \mid \bar x_{Si} \mid \bar y_{Si} \mid A_i \mid \bar x_{Si}A_i \mid \bar y_{Si}A_i$ $\to$ Schwerpunkt
> FTM-Tabelle: $i \mid x_{Si} \mid y_{Si} \mid A_i \mid I_{xxi} \mid y_{Si}^2A_i \mid I_{yyi} \mid x_{Si}^2A_i \mid I_{xy} \mid x_{Si}y_{Si}A_i$, mit $x_{Si} = \bar x_{Si} - \bar x_S$

$\to$ s. Rückseite

---

## Seite 25

(Erläuterung der Tabellenspalten, grün)

- $i$ $\to$ Flächenindex
- $\bar x_{Si}$, $\bar y_{Si}$ } Schwerpunktkoordinaten der Teilflächen im $\bar x$-$\bar y$-KOS
- $A_i$ $\to$ Flächeninhalt
- $\bar x_{Si}A_i$, $\bar y_{Si}A_i$
  } $\to$ Schwerpunkt $\bar x_S$, $\bar y_S$
- $x_{Si} = \bar x_{Si} - \bar x_S$, $\;y_{Si} = \bar y_{Si} - \bar y_S$ } Abstände der Schwerpunkte der Teilflächen zum Schwerpunkt des Systems
- $I_{xxi}$ $\to$ Flächenträgheitsmomente bezgl. $x$-Achse der Teilfläche
- $y_{Si}^2A_i$ $\to$ Steiner-Anteil – „ –
- $I_{yyi}$ $\to$ FTM bezgl. $y$-Achse
- $x_{Si}^2A_i$ $\to$ Steiner-Anteil – „ –
- $I_{xy}$, $x_{Si}y_{Si}A_i$ } Deviationsmoment, Steiner-Anteil der Teilfläche
  } FTM der (Systems) Gesamtfläche

$\Rightarrow$ Einsetzen in (6.1.3) + (6.1.4) und (6.3.3)

---

## Seite 26

**Beispiel: Gussrippe**

> Skizze: Symmetrischer Querschnitt (schraffiert) aus oberem Flansch und nach unten verjüngtem Steg (Trapez). Bemaßung (grün, mm): Flanschbreite 120, Flanschhöhe 50, Gesamthöhe 140, Stegbreite oben 60, Stegbreite unten 40. Bezugssystem: $\bar y$ waagerecht an der Unterkante, $\bar z$ senkrecht auf der Symmetrieachse; Schwerpunktachsen $y$, $z$.

ges.: Schwerpunkt und Flächenträgheitsmomente $I_{yy}$, $I_{zz}$

**(1) Schwerpunkt**
$\to \bar y_S = 0$, da symmetrisches Problem
$\to$ Teilflächen

> Skizze: Zerlegung: 1 = Flansch (Rechteck 120 × 50), 2 = Rechteck in der Stegmitte (40 × 90), 3 und 4 = Dreiecke links und rechts (Breite 10 oben, Höhe 90, Spitze unten); Teilschwerpunkte $S_1 \dots S_4$.

| $i$ | $\bar z_{Si}$ [mm] | $A_i$ [mm²] | $\bar z_{Si}A_i$ [mm³] |
|---|---|---|---|
| 1 | 115 | 6000 | 690 000 |
| 2 | 45 | 3600 | 162 000 |
| 3 | 60 | 450 | 27 000 |
| 4 | 60 | 450 | 27 000 |
| $\Sigma$ | / | 10 500 | 906 000 |

$$\bar z_S = \frac{\sum\bar z_{Si}A_i}{\sum A_i} = \frac{906\,000}{10\,500} = \underline{86{,}285\ \text{mm}}$$

[Prüfung: Geometrie (Steghöhe $140 - 50 = 90$, Dreiecke $10 \times 90$) und Tabelle korrekt; $\bar z_S = 86{,}2857$ mm (gerundet 86,29 mm, im Original abgeschnitten 86,285).]

**(2) FTM**

| $i$ | $y_{Si}$ | $z_{Si}$ | $I_{yyi}$ | $z_{Si}^2A_i$ | $I_{zzi}$ | $y_{Si}^2A_i$ | $I_{yz}$ | $y_{Si}z_{Si}A_i$ |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 28,715 | 1 250 000 | 4 947 307,35 | 7 200 000 | 0 | 0 | 0 |
| 2 | 0 | −41,285 | 2 430 000 | 6 136 024,41 | 480 000 | 0 | 0 | 0 |
| 3 | $-10/3 - 20$ | −26,285 | 202 500 | 310 905,55 | 2 500 | 245 000 | 11 250 | 275 992,5 |
| 4 | $10/3 + 20$ | −26,285 | 202 500 | 310 905,55 | 2 500 | 245 000 | −11 250 | −275 992,5 |
| $\Sigma$ | / | / | 4 085 000 | 11 705 142,86 | 7 685 000 | 490 000 | 0 | 0 |

(Korrekturen im Original: in der Spalte $y_{Si}z_{Si}A_i$ durchgestrichen „39 427,5" (falsch mit $y = 10/3$ statt $10/3 + 20$ gerechnet), ersetzt durch $\pm 275\,992{,}5$; Summe $y_{Si}^2A_i$ von „10 000" auf „490 000" korrigiert.)

[Prüfung: $I_{yyi}$: $120\cdot 50^3/12$, $40\cdot 90^3/12$, $10\cdot 90^3/36$ – korrekt; $I_{zzi}$: $50\cdot 120^3/12$, $90\cdot 40^3/12$, $90\cdot 10^3/36$ – korrekt; $I_{yz}$ der Dreiecke $\pm 10^2\cdot 90^2/72 = \pm 11\,250$ – korrekt; Steiner-Anteile korrekt.]

---

## Seite 27

$$I_{yy} = \sum_{i=1}^n\left(I_{yyi} + z_{Si}^2A_i\right) = 15\,796\,142{,}86\ \text{mm}^4$$
$$\underline{I_{yy} = 1579\ \text{cm}^4}$$

[Prüfung: $4\,085\,000 + 11\,705\,142{,}86 = 15\,790\,142{,}86$ mm⁴ (Additionsfehler im Original: 15 796 142,86). Das gerundete Ergebnis 1579 cm⁴ ist korrekt (exakt 1579,01 cm⁴).]

$$I_{zz} = \sum_{i=1}^n\left(I_{zzi} + y_{Si}^2A_i\right) = 8\,175\,000\ \text{mm}^4 \quad (\text{korrigiert aus } 7\,695\,000)$$
$$\underline{I_{zz} = 817{,}5\ \text{cm}^4} \quad (\text{korrigiert aus } 769{,}5)$$

[Prüfung: $7\,685\,000 + 490\,000 = 8\,175\,000$ mm⁴ – korrekt.]

$$I_{yz} = \sum_{i=1}^n\left(I_{yzi} - y_{Si}z_{Si}A_i\right) = \underline{0} \;\to\; \text{symmetrischer Querschnitt!}$$

---

## Seite 28

#### 6.3.4 Flächenträgheitsmomente bei Drehung des Koordinatensystems

> Skizze links: Rechteck mit Schwerpunktachsen parallel zu den Seiten (schraffiert).
> Skizze rechts: dasselbe Rechteck um ca. 45° gedreht im unveränderten Achsenkreuz, Teilflächen grün schraffiert $\to$ „$I$? $I_{xy} \ne 0$".

> Skizze: Beliebige Fläche mit Schwerpunktachsen $x$, $y$; dazu um den Winkel $\varphi$ gedrehtes Achsensystem $u$ (= $x^*$) und $v$ (= $y^*$) (grün).

geg.: $I_{xx}, I_{yy}, I_{xy}$
ges.: $I_{uu}, I_{vv}, I_{uv}$

es gilt analog:
$$I_{uu} = \int_A v^2\,dA \qquad I_{vv} = \int_A u^2\,dA \qquad I_{uv} = -\int_A uv\,dA \qquad (6.3.4)$$

---

## Seite 29

- **Koordinatentransformation:**

> Skizze: Achsenkreuz $x$, $y$ und um $\varphi$ gedrehtes Achsenkreuz $u$, $v$ (gleicher Ursprung). Punkt $P(x, y)$ bzw. $P(u, v)$. Die Koordinaten $u$ und $v$ sind über Hilfslinien in Teilstrecken I, II (Anteile von $u$) und III, IV (Anteile von $v$) zerlegt, rechte Winkel markiert, Winkel $\varphi$ an mehreren Stellen eingetragen.

$$\left.\begin{aligned} u &= \underbrace{x\cos\varphi}_{I} + \underbrace{y\sin\varphi}_{II}\\ v &= \underbrace{y\cos\varphi}_{III} - \underbrace{x\sin\varphi}_{IV} \end{aligned}\right\} \quad (6.3.5)$$

Einsetzen von (6.3.5) in (6.3.4):

$$I_{uu} = \int_A(-x\sin\varphi + y\cos\varphi)^2\,dA = \int_A\left(x^2\sin^2\varphi - 2xy\sin\varphi\cos\varphi + y^2\cos^2\varphi\right)dA$$
$$= \sin^2\varphi\underbrace{\int_A x^2\,dA}_{I_{yy}} - 2\sin\varphi\cos\varphi\underbrace{\int_A xy\,dA}_{(-)I_{xy}} + \cos^2\varphi\underbrace{\int_A y^2\,dA}_{I_{xx}}$$

(grün: „$-$" wird „$+$", da $(-)I_{xy}$)

---

## Seite 30

$$I_{uu} = \sin^2\varphi\,I_{yy} + 2\sin\varphi\cos\varphi\,I_{xy} + \cos^2\varphi\,I_{xx}$$

> (grün umrandet) $\curvearrowright$ trigonometrische Funktionen:
> $\sin^2\varphi + \cos^2\varphi = 1$
> $\cos^2\varphi - \sin^2\varphi = \cos(2\varphi) = 2\cos^2\varphi - 1 = 1 - 2\sin^2\varphi$
> $2\sin\varphi\cos\varphi = \sin(2\varphi)$

$$\Rightarrow \boxed{\begin{aligned} I_{uu} &= \frac{I_{xx} + I_{yy}}{2} + \frac{I_{xx} - I_{yy}}{2}\cos 2\varphi + I_{xy}\sin 2\varphi\\ I_{vv} &= \frac{I_{xx} + I_{yy}}{2} - \frac{I_{xx} - I_{yy}}{2}\cos 2\varphi - I_{xy}\sin 2\varphi\\ I_{uv} &= -\frac{I_{xx} - I_{yy}}{2}\sin 2\varphi + I_{xy}\cos 2\varphi \end{aligned}} \quad (6.3.6)$$

[Prüfung: aus (6.3.4)/(6.3.5) mit $I_{xy} = -\int xy\,dA$ nachgerechnet – korrekt.]

- **Berechnung der Extremwerte** von $I_{uu}, I_{vv}$ $\to I_1, I_2$ (Hauptträgheitsmomente)

$$\left.\frac{\partial I_{uu}}{\partial\varphi}\right|_{\varphi = \varphi_0} = 0$$

$$\curvearrowright \boxed{\tan 2\varphi_0 = \frac{2I_{xy}}{I_{xx} - I_{yy}}}$$

> Skizze (grün): Verlauf von $\tan$ über $2\varphi$ mit Polstellen bei $\pi/2$ und $3\pi/2$, Markierungen $\pi$, $2\pi$.

(grün) $\curvearrowright$ tan bei 0°–360° für $2\varphi$ zwei Lsg. im Unterschied 180°
$\to \varphi_0$ zwei Lsg. im Unterschied 90°
$\curvearrowright$ senkrecht aufeinander stehende Richtungen!

---

## Seite 31

einsetzen für $I_{uu}, I_{vv}$:

$$\Rightarrow \boxed{I_{1,2} = \frac{I_{xx} + I_{yy}}{2} \pm \sqrt{\frac{(I_{xx} - I_{yy})^2}{4} + I_{xy}^2}}$$

($\pm$ aus $I_{uu}$-, $I_{vv}$-Glg.)

$$\underline{I_{uv}(\varphi = \varphi_0) = 0}\,!$$

$$\boxed{\varphi_0 = \frac{1}{2}\arctan\left(\frac{2I_{xy}}{I_{xx} - I_{yy}}\right)}$$

$\varphi_0 + 90° \to$ 2. Hauptachse

Die unter dem Winkel $\varphi_0$ gedrehten Achsen heißen „**Hauptachsen**".
Die dazugehörigen Extremwerte $I_{1,2}$ der FTM heißen **Hauptträgheitsmomente**.
Der Vorgang der Transformation heißt „**Hauptachsentransformation**".

$\curvearrowright$ Deviationsmoment bezüglich der Hauptachsen ist gleich Null.

$\curvearrowright$ (rot markiert) keine Eindeutigkeit, was 1., 2. Hauptachse ist! (s. Dankert, S. 228)

$$\boxed{\tan\varphi_{0_1} = \frac{I_{xy}}{I_1 - I_{yy}}}$$

[Prüfung: Diese Formel liefert eindeutig die Richtung zu $I_1$ (Eigenvektorbedingung $I_{xy}\cos\varphi + (I_{yy} - I_1)\sin\varphi = 0$) – korrekt.]

---

## Seite 32

(Kasten: Herleitung $I_{1,2}$!)

$$\frac{\partial I_{uu}}{\partial\varphi} = -(I_{xx} - I_{yy})\sin 2\varphi + 2I_{xy}\cos 2\varphi = 0 \quad |:\cos 2\varphi$$

(im Original „$|:\cos\varphi$" [?])

$$-(I_{xx} - I_{yy})\tan 2\varphi + 2I_{xy} = 0 \;\to\; \boxed{\tan 2\varphi = \frac{2I_{xy}}{I_{xx} - I_{yy}}}$$

mit $\sin(\varphi) = \dfrac{\tan\varphi}{\sqrt{1 + \tan^2\varphi}}$ und $\cos\varphi = \dfrac{1}{\sqrt{1 + \tan^2\varphi}}$ (? s. Wiki)

einsetzen:

$$I_{uu,max} = \frac{I_{xx} + I_{yy}}{2} + \frac{I_{xx} - I_{yy}}{2}\frac{1}{\sqrt{1 + \left(\frac{2I_{xy}}{I_{xx} - I_{yy}}\right)^2}} + I_{xy}\frac{2I_{xy}}{I_{xx} - I_{yy}}\frac{1}{\sqrt{1 + \left(\frac{2I_{xy}}{I_{xx} - I_{yy}}\right)^2}}$$

(grün: Erweitern mit $\frac{I_{xx} - I_{yy}}{I_{xx} - I_{yy}}$ und unter die Wurzel ziehen)

$$= \frac{I_{xx} + I_{yy}}{2} + \frac{(I_{xx} - I_{yy})^2}{2}\frac{1}{\sqrt{(I_{xx} - I_{yy})^2 + 4I_{xy}^2}} + 2I_{xy}^2\frac{1}{\sqrt{(I_{xx} - I_{yy})^2 + 4I_{xy}^2}}$$

(grün: „4 raus $\Rightarrow$ 2")

$$= \frac{I_{xx} + I_{yy}}{2} + \frac{1}{\sqrt{\frac{(I_{xx} - I_{yy})^2}{4} + I_{xy}^2}}\left(\frac{(I_{xx} - I_{yy})^2}{4} + I_{xy}^2\right) \quad \left(\text{grün: } \frac{a}{\sqrt a} = \sqrt a,\ \text{Exp. } 1 - \tfrac12\right)$$

$$\underline{I_{uu} = \frac{I_{xx} + I_{yy}}{2} + \sqrt{\frac{(I_{xx} - I_{yy})^2}{4} + I_{xy}}}$$

[Prüfung: (1) In der letzten Zeile fehlt das Quadrat: richtig $+I_{xy}^2$ unter der Wurzel (vgl. korrekte Formel auf S. 31). (2) Die Ersetzungen müssen für $2\varphi$ gelten: $\sin 2\varphi = \tan 2\varphi/\sqrt{1 + \tan^2 2\varphi}$, $\cos 2\varphi = 1/\sqrt{1 + \tan^2 2\varphi}$ – so wird auch tatsächlich eingesetzt; die angeschriebenen Hilfsformeln mit $\varphi$ sind ungenau. Vorzeichenwahl der Wurzel: positiver Zweig ergibt $I_1$ nur, wenn $\cos 2\varphi_0$ und $(I_{xx} - I_{yy})$ gleiches Vorzeichen haben.]

---

## Seite 33

entsprechend Beispiel: s. oben (L-Profil, S. 23–24)

> Skizze: L-Profil (Teilflächen 1 und 2) mit $\bar x$-$\bar y$-System, Schwerpunkt S mit $x$-$y$-Achsen; Hauptachse 1 um $\varphi_0$ gegen $x$ gedreht (nach rechts oben), Hauptachse 2 senkrecht dazu (nach links oben).

$I_{xx} = 8{,}5\,a^4 \qquad I_{yy} = 4\,a^4 \qquad I_{xy} = 3\,a^4$

$$I_{1,2} = \frac{I_{xx} + I_{yy}}{2} \pm \sqrt{\frac{(I_{xx} - I_{yy})^2}{4} + I_{xy}^2}$$

$$\underline{I_1 = 10\,a^4} \quad (\text{korrigiert aus } 13[?]) \qquad \underline{I_2 = 2{,}5\,a^4}$$

$$\varphi_0 = \frac12\arctan\left(\frac{2I_{xy}}{I_{xx} - I_{yy}}\right) = \frac12\arctan\left(\frac{6a^4}{(8{,}5 - 4)a^4}\right) = \frac12\arctan\left(\frac{12}{9}\right) = \frac12\arctan\left(\frac43\right)$$

$$\varphi_0 = 26{,}56° \qquad \varphi_0 + 90° = 116{,}56°\ (2.\ \text{Achse})$$

[Prüfung: $6{,}25 \pm \sqrt{2{,}25^2 + 9} = 6{,}25 \pm 3{,}75$ $\Rightarrow$ $I_1 = 10\,a^4$, $I_2 = 2{,}5\,a^4$ – korrekt; $\varphi_0 = 26{,}57°$ – korrekt (Kontrolle: $\tan\varphi_{0_1} = 3/(10 - 4) = 0{,}5$ ✓). Im Original zwischendurch „26/9" geschrieben und zu „12/9" korrigiert.]

> Skizze: L-Profil maßstäblich mit Bemaßung $a$ (Schenkelbreite oben), $4a$ (Höhe), $3a$ (Gesamtbreite), $a$ (Höhe des unteren Schenkels); Schwerpunkt S, Achse 1 unter $\varphi_0 = 26{,}56°$ zur $x$-Achse, Achse 2 senkrecht dazu.

---

## Seite 34

**Beispiel 2:**

> Skizze: Rechteck, Breite $b$, Höhe $h$ (im Original beide Seiten mit „$b$" beschriftet [?]), Schwerpunktachsen $x$, $y$; gedrehte Achsen $u$ (um $\varphi$ gegen $x$) und $v$ (grün).

$I_{xx} = \dfrac{bh^3}{12} \qquad I_{yy} = \dfrac{b^3h}{12} \qquad I_{xy} = 0$

$\varphi = \frac{\pi}{2}$:

$$I_{uu} = \frac{I_{xx} + I_{yy}}{2} + \frac{I_{xx} - I_{yy}}{2}\cos 2\varphi + I_{xy}\sin 2\varphi = \frac{bh^3}{24} + \frac{b^3h}{24} + (-1)\left(\frac{bh^3}{24} - \frac{b^3h}{24}\right) + 0$$

$$I_{uu} = \frac{b^3h}{24} + \frac{b^3h}{24} = \frac{b^3h}{12} = I_{yy}\ ✓$$

$\varphi = \frac{\pi}{4}$:

> Skizze: Rechteck um 45° gedreht im $u$-$v$-System.

$$\underline{I_{uu}} = \frac{I_{xx} + I_{yy}}{2} + \frac{I_{xx} - I_{yy}}{2}\cos 2\varphi + I_{xy}\sin 2\varphi = \frac{bh^3 + b^3h}{24} + 0 + 0$$

$$\underline{I_{vv}} = \frac{I_{xx} + I_{yy}}{2} - \frac{I_{xx} - I_{yy}}{2}\cos 2\varphi - I_{xy}\sin 2\varphi = \frac{bh^3 + b^3h}{24} - 0 - 0$$

---

## Seite 35

$$\underline{I_{uv}} = -\frac{I_{xx} - I_{yy}}{2}\sin 2\varphi + I_{xy}\cos 2\varphi = -\frac{bh^3 - b^3h}{24} + 0$$

[Prüfung: Beispiel 2 korrekt.]

**Aufgabe:** Übung FTM 3.11

> Skizze: Profil aus drei Rechtecken: (1) oberer Flansch, Länge $L_1$, Dicke $h_1$, geneigt (steigt nach rechts an), Winkel $\alpha$ an der rechten oberen Ecke markiert; (2) senkrechter Steg, Höhe $L_2$, Dicke $h_2$; (3) unterer waagerechter Flansch, Länge $L_3$, Dicke $h_3$. Schwerpunkt S auf dem Steg mit Achsen $y$ (waagerecht), $z$ (senkrecht). Bemaßungen grün.

- dünnwandiges Profil
  $\to$ Flächenüberschneidungen vernachlässigbar!

geg.: $\alpha = 60°$, $L_1 = 200$ mm, $h_1 = 25$ mm, $L_2 = 350$ mm, $h_2 = 15$ mm, $L_3 = 200$ mm, $h_3 = 25$ mm

ges.: $I_{yy}, I_{zz}, I_{yz}$, $I_{1,2}$, $\varphi_0$

**Lös.:**

> Skizze: Zerlegung in Teilflächen 1 (geneigter Flansch, Schwerpunkt $S_1$ auf der Stegachse), 2 (Steg, $S_2$ = S), 3 (unterer Flansch, $S_3$); Bezugssystem $\bar y$ an der Unterkante, $\bar z = z$ auf der Stegachse. Einzelskizzen (1), (2), (3) jeweils mit lokalem $\bar y$-$\bar z$-System.

(grün) Skizze eines symmetrischen I-Profils $\to$ hier wäre Schwerpunkt im Zentrum $\curvearrowright$ auch hier!

---

## Seite 36

- **Schwerpunkt**

| $i$ | $\bar z_{Si}$ | $A_i$ | $\bar z_{Si}A_i$ |
|---|---|---|---|
| 1 | $L_2 + \frac{h_3}{2}$ | $L_1\cdot h_1$ | |
| 2 | $\frac{L_2}{2} + \frac{h_3}{2}$ | $L_2\cdot h_2$ | |
| 3 | $\frac{h_3}{2}$ | $L_3\cdot h_3$ | |
| 1 | 362,5 (korr. aus 437,5 [?]) | 5000 | 1 812 500 |
| 2 | 187,5 | 5250 | 984 375 |
| 3 | 12,5 | 5000 | 62 500 |
| $\Sigma$ | / | 15 250 | 2 859 375 |

$\bar y_S = 0$

$$\bar z_S = \frac{\sum\bar z_{Si}A_i}{\sum A_i} = \underline{\underline{187{,}5\ \text{mm}}} \;\hat=\; S_2\ ✓$$

[Prüfung: korrekt; $2\,859\,375/15\,250 = 187{,}5$ mm.]

- **FTM**

Drehung an der Teilfläche $A_1$

> Skizze: geneigtes Rechteck (Länge $L_1$, Dicke $h_1$) mit eigenem Achsensystem $u$ (Längsrichtung), $v$ und dem Achsensystem $y$, $z$; Winkel $\alpha$ zwischen $u$ und $y$.

~~$I_{u,v}$ bekannt~~ $I(u, v)$ bekannt
$\to$ Überführung in $y$-$z$-KOS
$\to \underline{\alpha = -60°}$ (negativ!)

$$I_{uu} = \frac{L_1h_1^3}{12} \qquad I_{vv} = \frac{L_1^3h_1}{12} \qquad I_{uv} = 0$$

$\to$ Nutzung von Glg. (6.3.6)

---

## Seite 37

$$I_{yy} = \frac{I_{uu} + I_{vv}}{2} + \frac{I_{uu} - I_{vv}}{2}\cos 2\alpha + I_{uv}\sin 2\alpha = \frac{L_1h_1^3 + L_1^3h_1}{24} + \frac{L_1h_1^3 - L_1^3h_1}{24}(-0{,}5) + 0$$
$$= \frac{2L_1h_1^3 + 2L_1^3h_1 - L_1h_1^3 + L_1^3h_1}{48} = \frac{L_1h_1^3 + 3L_1^3h_1}{48} = \frac{L_1h_1^3}{48} + \frac{L_1^3h_1}{16}$$
$$= 12\,565\,104{,}17\ \text{mm}^4 \qquad \underline{I_{yy} = 1256{,}5\ \text{cm}^4}$$

$$I_{zz} = \frac{I_{uu} + I_{vv}}{2} - \frac{I_{uu} - I_{vv}}{2}\cos 2\alpha - \underbrace{I_{uv}}_{0}\sin 2\alpha = \frac{L_1h_1^3 + L_1^3h_1}{24} - \frac{L_1h_1^3 - L_1^3h_1}{24}(-0{,}5)$$
$$= \frac{2L_1h_1^3 + 2L_1^3h_1 + L_1h_1^3 - L_1^3h_1}{48} = \frac{L_1h_1^3}{16} + \frac{L_1^3h_1}{48}$$
$$I_{zz} = 4\,361\,979{,}167\ \text{mm}^4 = \underline{436{,}2\ \text{cm}^4}$$

$$I_{yz} = -\frac{I_{uu} - I_{vv}}{2}\sin 2\alpha + \underbrace{I_{uv}}_{0}\cos 2\alpha = -\frac{L_1h_1^3 - L_1^3h_1}{24}\sin(-120°)$$
$$= -7\,104\,114{,}6\ \text{mm}^4 \quad (\text{korrigiert aus } 142\,763{,}7)$$
$$\underline{I_{yz} = -710{,}4\ \text{cm}^4} \quad (\text{korrigiert aus } 14{,}3)$$

(Auf der Zwischenzeile „$+\frac{L_1h_1^3}{12}$"-Bruchrechnung im Original teilweise durchgestrichen.)

[Prüfung: $I_{uu} = 260\,416{,}7$, $I_{vv} = 16\,666\,667$ mm⁴; mit $\cos(-120°) = -0{,}5$, $\sin(-120°) = -0{,}866$: $I_{yy} = 12\,565\,104$, $I_{zz} = 4\,361\,979$, $I_{yz} = -7\,104\,115$ mm⁴ – korrekt. Hinweis: $\alpha = -60°$ entspricht einer Flanschneigung von 60° gegen die Horizontale; die Skizze ist mit flacherer Neigung (ca. 30°) gezeichnet [?].]

---

## Seite 38

- **FTMe für Gesamtfläche**

| $i$ | $y_{Si}$ [cm] | $z_{Si}$ [cm] | $I_{yyi}$ [cm⁴] | $z_{Si}^2A_i$ [cm⁴] | $I_{zzi}$ [cm⁴] | $y_{Si}^2A_i$ [cm⁴] | $I_{yz}$ [cm⁴] | $y_{Si}z_{Si}A_i$ [cm⁴] |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 17,5 | 1256,5 | 15 312,5 | 436,2 | 0 | −710,4 (korr. aus 14,3) | 0 |
| 2 | 0 | 0 | 5359,4 | 0 | 9,84 | 0 | 0 | 0 |
| 3 | 0 | −17,5 | 26,0 | 15 312,5 | 1666,7 | 0 | 0 | 0 |
| $\Sigma$ | / | / | 6641,9 | 30 625 | 2112,7 | 0 | −710,4 | 0 |

$$I_{yy} = \sum_{i=1}^n\left(I_{yyi} + z_{Si}^2A_i\right) = \underline{37\,267\ \text{cm}^4}$$
$$I_{zz} = \sum_{i=1}^n\left(I_{zzi} + y_{Si}^2A_i\right) = \underline{2112{,}7\ \text{cm}^4}$$
$$I_{yz} = \sum_{i=1}^n\left(I_{yzi} - y_{Si}z_{Si}A_i\right) = \underline{-710{,}4\ \text{cm}^4}$$

[Prüfung: $I_{yy2} = 15\cdot 350^3/12 = 5359{,}4$ cm⁴, $I_{zz2} = 350\cdot 15^3/12 = 9{,}84$ cm⁴, $I_{yy3} = 26{,}0$ cm⁴, $I_{zz3} = 1666{,}7$ cm⁴, $z_{Si}^2A_i = 17{,}5^2\cdot 50 = 15\,312{,}5$ cm⁴; Summen korrekt. Im Original sind die Formeln mit „$z_{Si}A_i$" bzw. „$y_{Si}A_i$" ohne Quadrat geschrieben (Schreibfehler, gerechnet wurde mit Quadrat).]

---

## Seite 39

- **Hauptträgheitsmomente**

$$I_{1,2} = \frac{I_{yy} + I_{zz}}{2} \pm \sqrt{\frac{(I_{yy} - I_{zz})^2}{4} + I_{yz}^2}$$

$\underset{(+)}{I_1} = 37\,281\ \text{cm}^4$
$\underset{(-)}{I_2} = 2098\ \text{cm}^4$
} kaum Unterschiede zu $I_{yy}$ und $I_{zz}$

$$\varphi_0 = \frac12\arctan\left(\frac{2I_{yz}}{I_{yy} - I_{zz}}\right) \qquad \underline{\varphi_0 = -1{,}16°}$$

(grün) $\curvearrowright$ klar, $\varphi_0$ sehr klein

> Skizze: Profil mit Schwerpunkt S, Achsen $y$, $z$; Hauptachse 1 leicht im Uhrzeigersinn gegen $y$ gedreht (um $\varphi_0$), Hauptachse 2 senkrecht dazu.

[Prüfung: $\frac{I_{yy} + I_{zz}}{2} = 19\,689{,}9$; $\sqrt{17\,577{,}2^2 + 710{,}4^2} = 17\,591{,}5$ $\Rightarrow$ $I_1 = 37\,281$ cm⁴, $I_2 = 2098$ cm⁴; $\varphi_0 = \frac12\arctan(-0{,}04041) = -1{,}157°$ – korrekt. In der Skizze ist Achse 2 zu stark geneigt (ca. 45° statt 90° − 1,16°) – nur schematisch.]

---

## Didaktische Gliederung

1. **Einleitung** (S. 1): Flächenmomente als Rechengrößen der Festigkeitslehre; Flächenmomente 1. Ordnung (statische Momente) und 2. Ordnung (Flächenträgheitsmomente).
2. **6.1 Statische Momente und Schwerpunktermittlung** (S. 1–8)
   - Herleitung über die Resultierende paralleler Kräfte $\to$ Streckenlast $\to$ Fläche.
   - Def. Flächenschwerpunkt (6.1.1), (6.1.2); Def. **statische Momente** $S_{\bar y} = \int\bar x\,dA$, $S_{\bar x} = \int\bar y\,dA$.
   - Merksätze: statische Momente bzgl. Schwerpunktachsen = 0; Schwerpunkt liegt auf Symmetrielinie.
   - Beispiel Viertelkreisfläche (Polarkoordinaten).
   - Formelübersicht einfacher Flächen (Rechteck, Dreieck, Kreis, Kreisausschnitt, Halbkreis) mit $A$, Schwerpunktlage, $I_{xx}, I_{yy}, I_{xy}$.
   - Zusammengesetzte Flächen: Summenformeln (6.1.3), (6.1.4), Aussparungen als negative Flächen; Tabellenschema.
3. **6.2 Schwerpunkte von Massen, Volumina, Linien** (S. 8–16): analoge Integral- und Summenformeln; Ergänzung Linienschwerpunkte (gerade Linie, Kreisbogen, Viertelkreisbogen, Drehung des KOS); Anwendung: Aufhängung (Schwerpunkt unter Aufhängepunkt).
4. **6.3 Flächenmomente 2. Ordnung** (S. 16–39)
   - 6.3.1 Def. **axiale FTM** (6.3.1) und **Deviationsmoment** (6.3.2) (Vorzeichenkonvention $I_{xy} = -\int xy\,dA$); axiale FTM stets > 0, $I_{xy}$ beliebig; Rechteck bzgl. Ecke/Symmetrieachse; Symmetrie $\Rightarrow I_{xy} = 0$; Spiegelung $\Rightarrow$ Vorzeichenwechsel von $I_{xy}$.
   - 6.3.2 **Satz von Steiner** (Herleitung, Formeln); Schwerpunktachsen liefern kleinste axiale FTM.
   - 6.3.3 **Zusammengesetzte Flächen**: Satz, 4-Schritt-Vorgehen, (6.3.3), Tabellen-Rechenschema mit Spaltenerklärung.
   - 6.3.4 **Drehung des KOS**: Koordinatentransformation (6.3.5), Transformationsformeln (6.3.6), Extremwerte $\to$ **Hauptträgheitsmomente** $I_{1,2}$, **Hauptachsen** $\varphi_0$, $I_{uv} = 0$ bzgl. Hauptachsen, Zuordnung 1./2. Achse über $\tan\varphi_{0_1} = I_{xy}/(I_1 - I_{yy})$; Herleitung $I_{1,2}$.

**Rechenschema Schwerpunkt (Tabelle):** $i \mid \bar x_{Si} \mid \bar y_{Si} \mid A_i \mid \bar x_{Si}A_i \mid \bar y_{Si}A_i$ $\to$ $\bar x_S = \Sigma\bar x_{Si}A_i/\Sigma A_i$, $\bar y_S$ analog.

**Rechenschema FTM (Tabelle):** $i \mid x_{Si} = \bar x_{Si} - \bar x_S \mid y_{Si} = \bar y_{Si} - \bar y_S \mid A_i \mid I_{xxi} \mid y_{Si}^2A_i \mid I_{yyi} \mid x_{Si}^2A_i \mid I_{xyi} \mid x_{Si}y_{Si}A_i$ $\to$ $I_{xx} = \Sigma(I_{xxi} + y_{Si}^2A_i)$, $I_{yy} = \Sigma(I_{yyi} + x_{Si}^2A_i)$, $I_{xy} = \Sigma(I_{xyi} - x_{Si}y_{Si}A_i)$.

**Rechenschema Hauptachsen:** $I_{1,2}$ aus Mittelwert ± Radius; $\varphi_0 = \frac12\arctan\frac{2I_{xy}}{I_{xx} - I_{yy}}$; Zuordnung über $\tan\varphi_{0_1} = I_{xy}/(I_1 - I_{yy})$; geneigte Teilflächen über (6.3.6) aus ihrem eigenen Hauptachsensystem transformieren.

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| 1 | Viertelkreisfläche (Schwerpunkt, Polarkoordinaten) | $R$ | $\bar x_S = \bar y_S = \frac{4R}{3\pi} \approx 0{,}424R$ | 3–4 |
| 2 | Zusammengesetzte Fläche: Dreieck + Rechteck − Kreisloch | Maße in $a$ ($3a$, $3a$, $6a$, Loch $d = 2a$ bei $4{,}5a$/$4a$) | $A = 23{,}86a^2$, $\bar x_S = 3{,}55a$ [Prüfung: 3,56a], $\bar y_S = 2{,}49a$ | 7–8 |
| 3 | Gerade Linie unter Winkel $\alpha$ (Linienschwerpunkt) | $L$, $\alpha$ | $x_S = \frac{L}{2}\cos\alpha$, $y_S = \frac{L}{2}\sin\alpha$ (Mitte) | 9–10 |
| 4 | Kreisbogen (symmetrisch, halber Winkel $\alpha$) | $r$, $\alpha$ | $x_S = 0$, $y_S = r\sin\alpha/\alpha$ | 11 |
| 5 | Viertelkreisbogen (zwei Lagen des KOS) | $r$ | $x_S = y_S = 2r/\pi = 0{,}637r$; symmetrisch gelegt: $y_S = 0{,}90r$ | 12–13 |
| 6 | Aufgehängte Fläche (Dreieck + Rechteck), untere Kante waagerecht | $a$, $b$ | $c^2 + ac - a^2/2 = 0 \Rightarrow c = a(\sqrt{3/4} - 1/2) = 0{,}366a$ | 14–15 |
| 7 | Rechteck: FTM bzgl. Ecke / Symmetrieachse / gespiegelt | $b$, $h$ | $I_{\bar x\bar x} = bh^3/3$, $I_{\bar y\bar y} = hb^3/3$ bzw. $b^3h/12$; $I_{\bar x\bar y} = -b^2h^2/4$, $0$, $+b^2h^2/4$ | 17–19 |
| 8 | L-Profil (zwei Rechtecke) | $a$ | $\bar x_S = a$, $\bar y_S = 1{,}5a$; $I_{xx} = 8{,}5a^4$, $I_{yy} = 4a^4$, $I_{xy} = 3a^4$; $I_1 = 10a^4$, $I_2 = 2{,}5a^4$, $\varphi_0 = 26{,}56°$ | 23–24, 33 |
| 9 | Gussrippe (Flansch + Trapezsteg, symmetrisch) | 120/50/140/60/40 mm | $\bar z_S = 86{,}29$ mm; $I_{yy} = 1579$ cm⁴, $I_{zz} = 817{,}5$ cm⁴, $I_{yz} = 0$ | 26–27 |
| 10 | Rechteck, gedrehtes KOS ($\varphi = \pi/2$, $\pi/4$) | $b$, $h$ | $\varphi = \pi/2$: $I_{uu} = I_{yy}$; $\varphi = \pi/4$: $I_{uu} = I_{vv} = (bh^3 + b^3h)/24$, $I_{uv} = -(bh^3 - b^3h)/24$ | 34–35 |
| 11 | Dünnwandiges Profil mit geneigtem Flansch (Übung FTM 3.11) | $\alpha = 60°$, $L_1 = 200$, $h_1 = 25$, $L_2 = 350$, $h_2 = 15$, $L_3 = 200$, $h_3 = 25$ mm | $\bar z_S = 187{,}5$ mm; Flansch: $I_{yy1} = 1256{,}5$, $I_{zz1} = 436{,}2$, $I_{yz1} = -710{,}4$ cm⁴; gesamt: $I_{yy} = 37\,267$, $I_{zz} = 2112{,}7$, $I_{yz} = -710{,}4$ cm⁴; $I_1 = 37\,281$, $I_2 = 2098$ cm⁴, $\varphi_0 = -1{,}16°$ | 35–39 |

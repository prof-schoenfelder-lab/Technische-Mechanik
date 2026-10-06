# Technische Mechanik – Statik: 5. Haftung und Reibung bei starren Körpern (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen
Quelle: `Quellen/Vorlesung-2013/4-Haftung.pdf` (22 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten, Grün = Bemaßungen, Hervorhebungen, Ergebnisse, Kommentare.
- Das Kapitel ist im Original als „5." nummeriert (Dateiname „4-Haftung").
- Unsichere Lesungen sind mit [?] markiert; Nachrechnungen und Fehlerhinweise mit [Prüfung: ...].

---

## Seite 1

# 5. Haftung und Reibung bei starren Körpern

### 5.1 Grundlagen

Bei Bewegung
- zweier Festkörper gegeneinander
- eines Festkörpers in einem flüssigen/gasförmigen Medium

tritt ein **Bewegungswiderstand** auf.

Bsp.:
- Verschieben einer Kiste auf rauem Boden (Festkörper / Festkörper)
- Schiff im Wasser (Festkörper / Flüssigkeit)
- Flugzeug in Luft (Festkörper / Gas)

$\Rightarrow$ in Kontaktbereichen tritt eine **Reibungskraft** $R$ auf – *Richtung der Relativbewegung entgegengerichtet!* (grün)

> Skizze (obere Reihe, grün): vier Fälle „kleiner Block auf großem Block" mit Geschwindigkeitspfeilen: (1) nur oberer Block bewegt, $v_1$ nach rechts; (2) nur unterer Block bewegt, $v_2$ nach rechts; (3) beide bewegt, $v_2 > v_1$; (4) beide bewegt, $v_1 > v_2$.
> Skizze (untere Reihe, rot): jeweils die beiden Körper auseinandergezogen mit den Reibungskräften $R$ an beiden Kontaktflächen (actio = reactio): (1) am oberen Block $R$ nach links, am unteren $R$ nach rechts; (2) am oberen Block $R$ nach rechts, am unteren nach links; (3) wie (2) (oberer Block wird vom schnelleren unteren mitgenommen); (4) wie (1).

**Statik!** $\to$ nur Behandlung Festkörper / Festkörper
$\to$ Ausschluss der Verformungsarbeit der Festkörper („starrer Körper")

---

## Seite 2

Ursachen der Reibung:
- Rauheit der Oberflächen
- Temperatur, Feuchtigkeit
- Van-der-Waals-Kräfte
- …

} physikalische Eigenschaften der Kontaktpartner

**Gedankenexperiment**

> Skizze: Block mit Gewicht $G$ auf schraffiertem (rauem) Boden, horizontale Zugkraft $F$ (rot) nach rechts. Daneben Diagramm $F$ über $t$: Gerade vom Ursprung ansteigend, Beschriftung „monoton steigend".

- $F$ wird von 0 N gesteigert

$\curvearrowright$ **1. Möglichkeit:** Körper bewegt sich nicht $\to$ **Haftung**

> Skizze: freigeschnittener Block: $G$ nach unten, $F$ nach rechts, in der Kontaktfläche $F_H$ nach links („Haftkraft"), $F_N$ nach oben („Normalkraft").

$\rightarrow:\; F - F_H = 0$
$\uparrow:\; F_N - G = 0$

**2. Möglichkeit:** Körper bewegt sich (gleitet auf Oberfläche) $\to$ **Gleitreibung** (dyn. Problem)

> Skizze: Block mit $G$ ↓, $F$ →, Reibkraft $R$ ← in der Kontaktfläche, $F_N$ ↑ (im Original als „$F_H$" [?] beschriftet).

$\uparrow:\; F_N - G = 0$
$\rightarrow:$ dynamisches Grundgesetz $m \cdot a = F - R$

---

## Seite 3

**Praktische Bedeutung von Haftung und Reibung**

Haftung:
- Fortbewegung auf festem Boden erst durch Haftung möglich (Beschleunigung / Bremsen)
- Nägel / Schrauben halten durch Haftung

Gleitreibung:
- häufig unerwünscht / nach „Haftungsversagen"
- Erwärmung an Kontaktflächen $\to$ Energieverluste

### 5.2 Coulombsche Reibungsgesetze

#### 5.2.1 Haftung

(s. Gedankenexperiment)

> Skizze: Block, $G$ ↓, $F$ →, $F_H$ ←, $F_N$ ↑.

$\rightarrow:\; F - F_H = 0$
$\uparrow:\; F_N - G = 0$

- $F$ wächst monoton
  $\to 0 \le F \le F_0$: keine Bewegung des Körpers
  $\curvearrowright F_H = F$
  (am Grenzwert) $F_{H0} = F_0$
- nach Überschreiten von $F_0$ setzt Bewegung ein

---

## Seite 4

- Coulomb, Charles Augustin (1736–1806) zeigte, dass der **Grenzwert $F_{H0}$ proportional zur Normalkraft $F_N$** ist:

$$F_{H0} \sim F_N \;\to\; \frac{F_N}{F_{H0}} = \text{const.}$$

$\curvearrowright$ Proportionalitätsfaktor $\mu_0$:

$$\boxed{F_{H0} = \mu_0 \cdot F_N}$$

$\mu_0$ … Haftungskoeffizient (auch Haftreibungskoeffizient)

$\Rightarrow$ Ein Körper haftet solange, wie die Haftbedingung

$$F_H \le F_{H0} = \mu_0 F_N \qquad (5.2.1)$$

erfüllt ist.

**$F_H$ ist eine Reaktionskraft.**

- Mit der Kenntnis von $\mu_0$ ist es möglich, einen sogenannten **Haftungskegel** zu definieren:

$$F_{H0} = \mu_0 F_N \;\to\; \mu_0 = \frac{F_{H0}}{F_N} = \tan\rho_0$$

> Skizze links: Vektordreieck – $F_N$ senkrecht (rot), $F_{H0}$ waagerecht (rot) an der Spitze von $F_N$, die Resultierende (grün) schließt mit $F_N$ den Winkel $\rho_0$ ein; gestrichelt gespiegelt zur anderen Seite.
> Skizze rechts: Kegel (grün) mit Spitze im Kontaktpunkt (oben), Achse = $F_N$ (rot), halber Öffnungswinkel $\rho_0$.

---

## Seite 5

> Liegt die Wirkungslinie aller eingeprägten Kräfte innerhalb des Haftungskegels, so liegt Gleichgewicht = Zustand der Ruhe (Haftung) vor.

#### 5.2.2 Gleitreibung

- für $F = F_H > F_{H0}$ $\to$ Körper bewegt sich
  $\curvearrowright$ dabei tritt eine ~~der Bewegung entgegengesetzte gerichtete~~ Kraft $R$ auf
- **Coulomb** hat durch Versuche herausgefunden, dass $R$
  - proportional zur Normalkraft $F_N$ ist: $F_R \sim F_N$
  - unabhängig von der Größe der Relativgeschwindigkeit ist
  - entgegengesetzt zur Richtung der Relativbewegung ist

$\curvearrowright$ Proportionalitätsfaktor $\mu$:

$$\boxed{R = \mu F_N} \qquad (5.2.2)$$

$\mu$ … Gleitreibungskoeffizient

**$R$ ist eine eingeprägte Kraft** (Unterschied zu $F_{H0}$!)

- bei vergleichbaren Kontaktbedingungen gilt $\mu < \mu_0$

---

## Seite 6

### 5.3 Beispiele

#### 5.3.1 Masse auf schiefer Ebene

> Skizze: Schiefe Ebene, Neigungswinkel $\alpha$ zur Horizontalen (unten links). Block auf der Ebene, Gewicht $F_G$ (rot, senkrecht ↓), Kraft $F$ (rot) parallel zur Ebene hangaufwärts. Kontaktfläche grün mit $\mu_0$ bezeichnet.

geg.: $F_G$, $\alpha$, $\mu_0$
ges.: Zwischen welchen Werten darf $F$ liegen, damit die Masse in Ruhe bleibt?

**Fallunterscheidung notwendig!**

**(1.)** Ist $F$ zu klein $\to$ Masse rutscht nach unten; $F_H$ wirkt der Bewegung entgegen (also hangaufwärts).

> Skizze: freigeschnittener Block: $F_G$ ↓, $F$ hangaufwärts, $F_H$ hangaufwärts (in der Kontaktfläche), $F_N$ senkrecht zur Ebene; Winkel $\alpha$ zwischen $F_N$ und der Vertikalen (grün).

$\nearrow:\; F + F_H - F_G \sin\alpha = 0 \quad (1)$
$\nwarrow:\; F_N - F_G \cos\alpha = 0 \quad (2)$
$F_H \le \mu_0 F_N \quad (3)$

(1) und (2) in (3) liefert

$$F_G \sin\alpha - F \le \mu_0 F_G \cos\alpha$$
$$\boxed{F \ge F_G(\sin\alpha - \mu_0\cos\alpha)} \quad F_{min}$$

---

## Seite 7

**(2.)** Ist $F$ zu groß $\to$ Masse rutscht nach oben; $F_H$ wirkt der Bewegung entgegen (also hangabwärts).

> Skizze: Block, $F_G$ ↓, $F$ hangaufwärts, $F_H$ hangabwärts, $F_N$ senkrecht zur Ebene, Winkel $\alpha$ (grün).

$\nearrow:\; F - F_H - F_G \sin\alpha = 0 \quad (4)$
$\nwarrow:\; F_N - F_G \cos\alpha = 0 \quad (5)$
$F_H \le \mu_0 F_N \quad (6)$

(4) und (5) in (6) liefert:

$$F - F_G\sin\alpha \le \mu_0 F_G\cos\alpha$$
$$\boxed{F \le F_G(\sin\alpha + \mu_0\cos\alpha)} \quad F_{max}$$

Lösung aus beiden Ergebnissen:

$$F_G(\sin\alpha - \mu_0\cos\alpha) \le F \le F_G(\sin\alpha + \mu_0\cos\alpha)$$

Zahlenbeispiel für: $\alpha = 30°$, $\mu_0 = 0{,}15$ (Stahl/Stahl)

$$\boxed{0{,}37\,F_G \le F \le 0{,}63\,F_G}$$

[Prüfung: $\sin 30° = 0{,}5$; $0{,}15 \cdot \cos 30° = 0{,}130$ $\Rightarrow$ $0{,}370\,F_G \le F \le 0{,}630\,F_G$ – korrekt.]

---

## Seite 8

#### 5.3.2 Leiter an einer Wand

> Skizze: Senkrechte Wand links (schraffiert), Boden unten (schraffiert). Leiter von Fußpunkt A (am Boden, rechts) nach B (an der Wand, oben). Winkel $\alpha$ zwischen Leiter und Boden bei A. Leiterlänge $L$ (grün). Eine Person (Strichmännchen) steht auf der Leiter. Kontakt bei B mit $\mu_{0B}$, bei A mit $\mu_{0A}$ (grün).

Eine Leiter ist an eine Wand angelegt. Wie groß muss der Winkel $\alpha$ sein, damit eine Person vom Gewicht $F_G$ die Leiter voll besteigen kann, ohne dass diese rutscht?

geg.: $\mu_{0A}$, $\mu_{0B}$, $F_G$, $L$
ges.: $\alpha$ so, dass kein Gleiten auftritt

**Lös.:**

> Skizze: freigeschnittene Leiter: in B $F_{NB}$ (→, von der Wand weg) und $F_{HB}$ (↑); $F_G$ (↓) im Abstand $L_S$ von A (entlang der Leiter gemessen); in A $F_{HA}$ (←, zur Wand hin) und $F_{NA}$ (↑). Winkel $\alpha$ bei A.

$\rightarrow:\; F_{NB} - F_{HA} = 0 \quad (1)$
$\uparrow:\; F_{HB} + F_{NA} - F_G = 0 \quad (2)$
$\curvearrowleft A:\; -F_{NB} L\sin\alpha - F_{HB} L\cos\alpha + F_G L_S\cos\alpha = 0 \quad (3)$

$F_{HA} \le \mu_{0A} F_{NA} \quad (4)$
$F_{HB} \le \mu_{0B} F_{NB} \quad (5)$

Unbekannte: $F_{NA}, F_{HA}, F_{NB}, F_{HB}, \alpha \to 5$ $\to$ 5 Gleichungen

---

## Seite 9

Ermittlung von $\alpha$ für Grenzfall „$=$":

$F_{HA} = \mu_{0A} F_{NA}$
$F_{HB} = \mu_{0B} F_{NB}$

- $L_S = L$ – Leiter ist voll bestiegen

(4) und (5) in (1)–(3) liefert:

$F_{NB} - \mu_{0A}F_{NA} = 0 \;\to\; F_{NB} = \mu_{0A}F_{NA} \quad (6)$
$\mu_{0B}F_{NB} + F_{NA} - F_G = 0 \quad (7)$
$-F_{NB}L\sin\alpha - \mu_{0B}F_{NB}L\cos\alpha + F_G L\cos\alpha = 0 \quad |:L\cos\alpha$
$-F_{NB}\tan\alpha - \mu_{0B}F_{NB} + F_G = 0 \quad (8)$ $\quad\left(\to F_{NB} = \dfrac{F_G}{\tan\alpha + \mu_{0B}}\right)$

(grün: Lösungsweg „$F_{NA} \to F_{NB} \to \alpha$"; ein durchgestrichener Ansatz „$-\mu_{0A}F_{NA}\tan\alpha - \mu_{0B}\mu_{0A}F_{NA} + F_G$")

(6) in (7): $\mu_{0B}\mu_{0A}F_{NA} + F_{NA} - F_G = 0$

$$F_{NA} = \frac{F_G}{1 + \mu_{0B}\mu_{0A}}$$

(6) $\to$
$$F_{NB} = \frac{F_G\,\mu_{0A}}{1 + \mu_{0B}\mu_{0A}}$$

(8) $\to$
$$\tan\alpha = \frac{F_G}{F_{NB}} - \mu_{0B} = \frac{1 + \mu_{0B}\mu_{0A}}{\mu_{0A}} - \frac{\mu_{0B}\mu_{0A}}{\mu_{0A}} = \frac{1 + \mu_{0B}\mu_{0A} - \mu_{0B}\mu_{0A}}{\mu_{0A}}$$

$$\tan\alpha = 1/\mu_{0A}$$

---

## Seite 10

$$\alpha = \arctan\left(\frac{1}{\mu_{0A}}\right)$$

Bsp.: $\mu_{0A} = 0{,}15 \;\to\; \alpha = 81{,}5°$

[Prüfung: $\arctan(1/0{,}15) = \arctan 6{,}667 = 81{,}47°$ – korrekt. Herleitung nachgerechnet, korrekt; das Ergebnis ist unabhängig von $\mu_{0B}$. Hinweis: Es handelt sich um den Grenzwinkel; Bedingung für Haften ist $\alpha \ge \arctan(1/\mu_{0A})$. Eigengewicht der Leiter vernachlässigt.]

(Rest der Seite leer.)

---

## Seite 11

### 5.4 Seilhaftung und Seilreibung

Erfahrung: Ein über eine starre Rolle gelegtes Seil kann an seinen Enden mit unterschiedlich großen Gewichten belastet werden, ohne dass es sich bewegt.

> Skizze: feststehende Rolle (Lager angedeutet), Seil darübergelegt, links hängt ein Gewicht $F_{G1}$, rechts $F_{G2}$; $F_{G1} < F_{G2}$ (rot).

Ursache: Haftungskraft zwischen Rolle und Seil
$\downarrow$
Freischnitt eines Teilabschnitts $ds$

> Skizze: Kreisausschnitt mit Öffnungswinkel $d\varphi$ (Spitze im Rollenmittelpunkt). Seilelement der Länge $ds$ (grün) auf dem Bogen. Links Seilkraft $F_S$ (rot, tangential nach links unten), rechts $F_S + dF_S$ (rot, tangential nach rechts unten); beide Tangenten gegen die Horizontale um $d\varphi/2$ geneigt (grün). In der Mitte des Elements: $dF_H$ (←, tangential) und $dF_N$ (↑, radial, auf das Seil wirkend).

Gleichgewicht über $ds$:

$\rightarrow:\; -F_S\cos\left(\frac{d\varphi}{2}\right) + (F_S + dF_S)\cos\left(\frac{d\varphi}{2}\right) - dF_H = 0 \quad (1)$

$\uparrow:\; -F_S\sin\left(\frac{d\varphi}{2}\right) - (F_S + dF_S)\sin\left(\frac{d\varphi}{2}\right) + dF_N = 0 \quad (2)$

> (grün umrandet) da $d\varphi \ll 1$: $\cos\left(\frac{d\varphi}{2}\right) \approx 1$ und $\sin\left(\frac{d\varphi}{2}\right) \approx \frac{d\varphi}{2}$

(1) $\leadsto dF_S - dF_H = 0$
(2) $\leadsto -F_S\,d\varphi - \underbrace{dF_S\frac{d\varphi}{2}}_{\text{kann gegenüber anderen Termen vernachlässigt werden!}} + dF_N = 0$

---

## Seite 12

$\curvearrowright$
$dF_S = dF_H \quad (3)$
$F_S\,d\varphi = dF_N \quad (4)$

- Coulombsche Haftung im Grenzfall
  $F_H = \mu_0 F_N \leadsto dF_H = \mu_0\,dF_N \quad (5)$

(5) in (3): $dF_S = \mu_0\,dF_N \quad (6)$
(4) in (6): $dF_S = \mu_0 F_S\,d\varphi$

$$\frac{dF_S}{F_S} = \mu_0\,d\varphi \quad (7)$$

Integration von (7):

> Skizze: Rolle mit Seil, links $F_{S1}$, rechts $F_{S2}$; Umschlingungswinkel $\alpha$ eingezeichnet; grün: „angenommene Zugrichtung".

$$\int_{F_{S1}}^{F_{S2}}\frac{dF_S}{F_S} = \int_0^\alpha \mu_0\,d\varphi$$

$$\ln\left(\frac{F_{S2}}{F_{S1}}\right) = \mu_0\alpha \;\to\; F_{S2} = F_{S1}\,e^{\mu_0\alpha}$$

(grün: $F_{S1}$, $F_{S2}$ können auch vertauscht werden, wenn Zugrichtung wechselt)

$\alpha$ … Umschlingungswinkel

> Skizze (grün): Graph $y = e^x$; bei $x = 0$ ist $y = 1$; für $x > 0$ ist $y > 1 \curvearrowright F_{S2} > F_{S1}$! Für $x = 0$ (d. h. $\mu_0 \ne 0$, $\alpha = 0$): $F_1 = F_2$.

$$\boxed{F_{S2} \le F_{S1}\,e^{\mu_0\alpha}} \quad \text{Seilhaftung}$$
$$\boxed{F_{S2} = F_{S1}\,e^{\mu\alpha}} \quad \text{Seilreibung}$$

Euler (1762) – Eytelweinsche Formel (≈ 1800)

---

## Seite 13

> Skizze: Rolle mit Seil; $F_{S1}$ links senkrecht nach unten; $F_{S2}$ in drei Varianten: waagerecht oben nach rechts (Umschlingung 90°), schräg nach links unten (Zwischenwert) und senkrecht nach unten rechts (180°); Umschlingungswinkel 90° und 180° als Bögen eingezeichnet.

Beispiel für Leder auf Holz, $\mu_0 = 0{,}5$:

| $\alpha$ | $F_{S2}/F_{S1}$ |
|---|---|
| 0 | 1 |
| 45° | 1,28 |
| 90° | 1,65 |
| 180° | 2,72 |
| 360° | 7,39 |

$\to$ mit 7,39-facher Last bei $F_{S2}$ ziehen, um $F_{S1}$ zu erreichen [?]

[Prüfung: Mit $\mu_0 = 0{,}5$ und $\alpha$ im Bogenmaß ergibt sich $e^{0{,}5\alpha}$: 45° → 1,48; 90° → 2,19; 180° → 4,81; 360° → 23,1. Die Tabellenwerte ($e^{0,25}, e^{0,5}, e^{1}, e^{2}$) entsprechen $\mu_0\alpha = 1$ bei 180°, also $\mu_0 = 1/\pi \approx 0{,}32$ bzw. einer falschen Winkelumrechnung. Tabelle ist für $\mu_0 = 0{,}5$ falsch.]

---

**Bsp.: (1) Die Pferd-vor-dem-Saloon-Situation**

> Skizze: Waagerechte Holzstange (Zylinder) an einer Wand/Pfosten befestigt; ein Riemen ist mehrfach um die Stange geschlungen (Kontakt $\mu_0$, grün). Ein Ende hängt senkrecht mit Gewicht $F_G$ nach unten, das andere Ende wird waagerecht mit $F$ (rot, Pferd) gezogen. Querschnittsskizze: Kreis, $F$ nach links (oben abgehend), $F_G$ nach unten (rechts abgehend), Zusatzwinkel $90° = \pi/2$.

geg.:
- Lederriemen um Holzstange geschlungen
- freies Ende mit Gewicht $F_G$ (200 g) belastet
- Pferd zieht mit $F$ (4 kN)
  ($n$ … Anzahl der Umschlingungen)
- $\mu_0 = 0{,}5$

- Umschlingungswinkel $\alpha = 2\pi n + \frac{\pi}{2}$

ges.: Umschlingungen $n$, um $F$ und $F_G$ im Gleichgewicht zu halten?

**Lös.:**
$F = F_G\,e^{\mu_0\alpha}$ (Grenzfall)
$\frac{F}{F_G} = e^{\mu_0\alpha} \quad |\ln$
$\ln\left(\frac{F}{F_G}\right) = \mu_0\alpha$
$\alpha = \frac{1}{\mu_0}\ln\left(\frac{F}{F_G}\right) = 15{,}24$

$\to n = \frac{\alpha}{2\pi} - \frac{1}{4} = 2{,}18$

$\curvearrowright$ **$n = 3$** ($\alpha = 6{,}5\pi$)

[Prüfung: $F_G = 0{,}2 \cdot 9{,}81 = 1{,}962$ N; $\ln(4000/1{,}962) = 7{,}620$; $\alpha = 15{,}24$ – korrekt; $n = 2{,}43 - 0{,}25 = 2{,}18$ – korrekt.]

---

## Seite 14

- $F_{max}$ für $n = 3$?
  $n = 3 \to \alpha = 6{,}5\pi = 20{,}42$

$$F = F_G\,e^{\mu_0\alpha} = 54\,347\ \text{N} = \underline{54\ \text{kN}}$$
$\downarrow$ Faktor 27 000 zu $F_G$!

[Prüfung: $e^{0{,}5 \cdot 20{,}42} = e^{10{,}21} = 27\,173$. Mit $F_G = 2$ N folgt $F = 54\,347$ N (so im Original); mit dem zuvor verwendeten $F_G = 1{,}962$ N wäre $F = 53\,316$ N ≈ 53 kN. Kleine Inkonsistenz im Ansatz von $F_G$, Größenordnung korrekt.]

---

**(2) Stab an der Wand**

> Skizze: Senkrechte Wand links (schraffiert). Waagerechter Stab der Länge $a$ liegt mit dem linken Ende an der Wand an (Kontakt $\mu_0$, grün). Ein Seil verläuft von einem Punkt an der Wand (Höhe $a$ über dem Stab) schräg zu Punkt C auf dem Stab; Winkel $\alpha$ zwischen Seil und Stab bei C. Koordinate $x$ von der Wand nach rechts bis C. Gewicht $F_G$ (rot ↓) in Stabmitte $a/2$.

geg.: $F_G$, $\mu_0 = 0{,}5$, $a = 1$ m
ges.: $x_{min}$, $x_{max}$

**Fallunterscheidung!**

**Lös.: 1. Fall:** Balken klappt rechts runter

> Skizze: Stab freigeschnitten: am linken Ende $F_N$ (→, von der Wand) und $F_H$ (↓); Seilkraft $F_S$ in C schräg nach links oben, Winkel $\alpha$; $F_G$ ↓ bei $a/2$; Abstand $x_{min}$ von der Wand bis C.

$\uparrow:\; -F_H - F_G + F_S\sin\alpha = 0 \quad (1)$
$\rightarrow:\; F_N - F_S\cos\alpha = 0 \quad (2)$
$\curvearrowleft C:\; F_H\,x_{min} - F_G\left(\frac{a}{2} - x\right) = 0 \quad (3)$

aus (1): $F_H = F_S\sin\alpha - F_G \quad (4)$
in (3): $(F_S\sin\alpha - F_G)x - F_G\left(\frac{a}{2} - x\right) = 0$
$F_S\sin\alpha\cdot x - F_G x - F_G\frac{a}{2} + F_G x = 0$

$$F_S\sin\alpha\,x - F_G\frac{a}{2} = 0 \quad (5)$$

(rot: hier jetzt erst einmal nur $F_S$ unbek.)

---

## Seite 15

(rot: $\downarrow$ $F_S$ bestimmen)

$F_H \le \mu_0 F_N$
aus (2): $F_N = F_S\cos\alpha$ $\;$ mit (4):

$\mu_0 F_N = F_S\sin\alpha - F_G$
$\mu_0 F_S\cos\alpha = F_S\sin\alpha - F_G$
$F_S(\mu_0\cos\alpha - \sin\alpha) = -F_G$

$$F_S = \frac{F_G}{\sin\alpha - \mu_0\cos\alpha} \quad (6)$$

(6) in (5) (rot: $\to$ wieder Lsg. mit $x$ aufgreifen)

$\dfrac{F_G\sin\alpha\,x}{\sin\alpha - \mu_0\cos\alpha} - F_G\dfrac{a}{2} = 0 \quad |:F_G$

$\dfrac{\sin\alpha\,x}{\sin\alpha - \mu_0\cos\alpha} = \dfrac{a}{2}$

$x = \dfrac{a(\sin\alpha - \mu_0\cos\alpha)}{2\sin\alpha}$

$x = \dfrac{a}{2}\left(1 - \mu_0\dfrac{\cos\alpha}{\sin\alpha}\right)$ $\quad\left(\dfrac{\cos\alpha}{\sin\alpha} = \dfrac{1}{\tan\alpha}\right)$

$\tan\alpha = \dfrac{a}{x}$ ! $\;\to\; x = \dfrac{a}{2}\left(1 - \mu_0\dfrac{x}{a}\right)$

$x\left(1 + \dfrac{\mu_0}{2}\right) = \dfrac{a}{2}$

$$x_{min} = \frac{a}{2\left(1 + \frac{\mu_0}{2}\right)} = \frac{a}{2 + \mu_0}$$

---

## Seite 16

**2. Fall:** Balken klappt links runter

> Skizze: Stab freigeschnitten: links $F_N$ (→) und $F_H$ (↑); Seilkraft $F_S$ in C schräg nach links oben (Winkel $\alpha$); $F_G$ ↓ bei $a/2$; C liegt rechts der Mitte, Abstand $x_{max}$.

$\rightarrow:\; F_N - F_S\cos\alpha = 0 \quad (1)$
$\uparrow:\; F_H - F_G + F_S\sin\alpha = 0 \quad (2)$
$\curvearrowleft C:\; -F_H\cdot x_{max} + F_G\left(x - \frac{a}{2}\right) = 0 \quad (3)$
$F_H \le \mu_0 F_N \to F_H = \mu_0 F_N \quad (4)$

(rot: gleich $F_S$ lösen)
(4) in (2): $\mu_0 F_N - F_G + F_S\sin\alpha = 0 \quad (5)$
aus (1): $F_N = F_S\cos\alpha \quad (6)$
(6) in (5): $\mu_0 F_S\cos\alpha - F_G + F_S\sin\alpha = 0$
$F_S(\mu_0\cos\alpha + \sin\alpha) = F_G$

$$F_S = \frac{F_G}{\mu_0\cos\alpha + \sin\alpha} \quad (7)$$

(rot: dann $F_S$ in Glg. mit $x_{max}$)
(2) in (3): $-(F_G - F_S\sin\alpha)x + F_G\left(x - \frac{a}{2}\right) = 0$
$-F_G x + F_S\sin\alpha\,x + F_G x - F_G\frac{a}{2} = 0$
$F_S\sin\alpha\cdot x - F_G\frac{a}{2} = 0 \quad (8)$

(7) in (8): $\dfrac{F_G\sin\alpha\cdot x}{\mu_0\cos\alpha + \sin\alpha} - F_G\dfrac{a}{2} = 0$

$\sin\alpha\,x = \frac{a}{2}(\mu_0\cos\alpha + \sin\alpha) \quad |:\sin\alpha$
$x = \frac{a}{2}\left(\frac{\mu_0}{\tan\alpha} + 1\right)$, $\quad \tan\alpha = \frac{a}{x}$
$x = \frac{a}{2}\left(\frac{\mu_0 x}{a} + 1\right)$
$x\left(1 - \frac{\mu_0}{2}\right) = \frac{a}{2}$

---

## Seite 17

$$x_{max} = \frac{a}{2 - \mu_0}$$

$x_{min} \le x \le x_{max}$

$$\boxed{\frac{a}{2 + \mu_0} \le x \le \frac{a}{2 - \mu_0}}$$

$$\frac{2}{5}\,\text{m} \le x \le \frac{2}{3}\,\text{m} \quad (0{,}4) \;\; (0{,}67)$$

[Prüfung: $1/2{,}5 = 0{,}4$ m; $1/1{,}5 = 0{,}667$ m – korrekt; beide Herleitungen nachgerechnet, korrekt.]

> Skizze: Wand mit Stab, Seil; auf dem Stab markiert der zulässige Bereich zwischen 0,4 m und 0,67 m.

---

**(3.)**

> Skizze: Dreieckige Scheibe (schraffiert), unten links in Festlager B gelagert. Die linke Kante ist senkrecht, Höhe $L$ (Spitze oben). An der Spitze greift $F$ (rot) schräg nach rechts unten an, Winkel $\alpha$ zur Horizontalen. Rechte Ecke der Scheibe (Gelenk) im horizontalen Abstand $a$ von B. Von dort führt ein Pendelstab schräg nach rechts unten zu Punkt A auf einem Klotz, der auf rauem Boden ($\mu_0$) liegt; horizontaler Abstand $c$, Höhe $b$ (grün). A und B liegen auf gleicher Höhe.

geg.: $a, b, c, L, \alpha, F$
ges.: $\mu_0$, so dass Speicher [?] (Klotz) in Ruhe

**Lös.: (I)** $F_P$? $\to$ gleich weiter zu (II)
(rot umrandet: nur Zusatz, um Lagerkräfte zu bestimmen für $\mu_0 \ge \frac{c}{b}$ [?])

> Skizze: Scheibe freigeschnitten: $F$ an der Spitze (Winkel $\alpha$), $F_{BH}$ (→) und $F_{BV}$ (↑) in B; Pendelstabkraft $F_P$ an der rechten Ecke entlang des Stabes (nach rechts unten zeigend), Winkel $\beta$ zur Vertikalen.

$\rightarrow:\; F\cos\alpha + F_{BH} - F_P\sin\beta = 0$
$\uparrow:\; -F\sin\alpha + F_{BV} + F_P\cos\beta = 0$
$\curvearrowleft B:\; F\cdot L\cos\alpha - F_P(a + c)\sin\gamma = 0$ $\quad$ (grün: oder über $F_x\cdot y$, $F_y\cdot 0$)

$\beta = \arctan\left(\frac{c}{b}\right)$

> Hilfsskizze (grün, links): Hebelarm von $F$ um B: $x_F = L\cos\alpha$, $\cos\alpha = x_F/L$.
> Hilfsskizze (grün, rechts): Dreieck mit Hypotenuse $\sqrt{a^2 + b^2}$ [?], Basis $a + c$, Hebelarm von $F_P$: $x_{FP} = (a + c)\sin\gamma$, $\gamma = \arctan\left(\frac{b}{c}\right)$ (Winkel des Pendelstabes zur Horizontalen).

---

## Seite 18

$$F_P = F\frac{L\cos\alpha}{(a + c)\sin\gamma} = F\frac{L\cos\alpha}{(a + c)\sin\left(\arctan\frac{b}{c}\right)}$$

**(II)** $\mu_0$?

> Skizze: Klotz auf rauem Boden ($\mu_0$), Pendelstabkraft $F_P$ greift schräg von links oben an, Winkel $\gamma$ zur Horizontalen. Freigeschnitten: $F_P$ schräg nach rechts unten, $F_H$ (←) und $F_N$ (↑) in der Kontaktfläche.

$F_H \le F_N/\mu_0$ $\;$ (durchgestrichen: $F_H = F_N/\mu_0$)

[Prüfung: Schreibfehler – richtig ist $F_H \le \mu_0 F_N$; unten wird korrekt damit gerechnet.]

$\rightarrow:\; -F_H + F_P\cos\gamma = 0$
$\uparrow:\; F_N - F_P\sin\gamma = 0$

$F_H = F_P\cos\gamma$
$F_N = F_P\sin\gamma$

$\curvearrowright$ $F_P\cos\gamma \le \mu_0 F_P\sin\gamma$ $\quad$ (links: „$\curvearrowright$ (I) $F_P$ nicht notwendig!")

$$\mu_0 \ge \frac{\cos\gamma}{\sin\gamma} = \frac{1}{\tan\gamma} = \frac{1}{\tan\left(\arctan\frac{b}{c}\right)} = \frac{c}{b}, \qquad \gamma = \arctan\left(\frac{b}{c}\right)$$

$$\boxed{\mu_0 \ge \frac{c}{b}}$$

[Prüfung: korrekt; Ergebnis unabhängig von $F$, $L$, $a$, $\alpha$.]

> Skizze links (grün): steiler Pendelstab, kleines $c$, großes $b$ $\curvearrowright \mu_0 = 0{,}1$.
> Skizze rechts (grün): flacher Pendelstab, $c$ groß gegenüber $b$ $\curvearrowright \mu_0 \ge 2$.

---

## Seite 19

**(4) Hülse** (durchgestrichen: „Seil…")

> Skizze: Senkrechte Stange (Durchmesser $d$), darauf eine Hülse der Höhe $h$. An der Hülse seitlich ein waagerechter Arm, an dessen Ende $F_G$ (rot ↓) im Abstand $a$ von der Stangenachse hängt.

geg.: $a, h, d, F_G$
ges.: $\mu_0$, so dass Selbsthemmung Abrutschen verhindert

(grün umrandet, oben rechts: $\mu_0 \ge 0{,}5\,h/a$)

> Skizze: Hülse verkantet an der Stange: Kontaktpunkt 1 oben links, Kontaktpunkt 2 unten rechts (rot markiert, je $\mu_0$). Bemaßung $h$ (Abstand der Kontaktpunkte vertikal), $d$ (horizontal), $a$.
> Freischnitt: im Punkt 1 $F_{N1}$ (←) und $F_{H1}$ (↑); im Punkt 2 $F_{N2}$ (→) und $F_{H2}$ (↑); $F_G$ ↓ am Armende.

$\rightarrow:\; -F_{N1} + F_{N2} = 0 \leadsto \underline{F_{N1} = F_{N2}} \quad (1)$
$\uparrow:\; F_{H1} + F_{H2} - F_G = 0 \quad (2)$
$\curvearrowright 2:\; F_G\left(a - \frac{d}{2}\right) + F_{H1}\cdot d - F_{N1}\cdot h = 0 \quad (3)$ (Uhrzeigersinn positiv)

$F_{H1} \le \mu_0 F_{N1} \quad (4) \qquad F_{H2} \le \mu_0 F_{N2} \quad (5)$

(4) und (5) in (1):
$\dfrac{F_{H1}}{\mu_0} = \dfrac{F_{H2}}{\mu_0} \leadsto \underline{F_{H1} = F_{H2}} \quad (6)$

(4) in (3):
$F_G\left(a - \frac{d}{2}\right) + \mu_0 F_{N1}\cdot d - F_{N1}\cdot h = 0$
$F_G\left(a - \frac{d}{2}\right) + F_{N1}(\mu_0 d - h) = 0$

$$F_{N1} = -F_G\frac{a - d/2}{\mu_0 d - h} \quad (7)\,[?]$$

(rot: $F_N > 0$, da $(\mu_0 d - h) < 0$ $\to$ nur so macht es Sinn)

---

## Seite 20

(6) in (2):
$F_{H1} + F_{H1} - F_G = 0$
$2F_{H1} = F_G$

$$F_{H1} = \frac{F_G}{2}$$

$\curvearrowright$ mit (4) und (7):

$\dfrac{F_G}{2} \le \mu_0\left(-F_G\dfrac{a - d/2}{\mu_0 d - h}\right)$

$\dfrac{F_G}{2} \le -F_G\dfrac{\mu_0(a - d/2)}{\mu_0 d - h} \quad |\cdot(\mu_0 d - h)$ (rot: $\to$ Ungleichheitszeichen dreht sich)

$\mu_0 d - h \ge -2\mu_0\left(a - \frac{d}{2}\right) \quad |:\mu_0$ (rot korrigiert von $\le$ zu $\ge$)
$d - \dfrac{h}{\mu_0} \ge -2\left(a - \dfrac{d}{2}\right)$
$\dfrac{h}{\mu_0} \le d + 2\left(a - \dfrac{d}{2}\right)$
$\dfrac{h}{\mu_0} \le 2a$

$$\mu_0 \ge \frac{h}{2a} = \frac{1}{2}\frac{h}{a}$$

(rot: $(\mu_0 d - h) < 0$, da $d \le h$, $\mu_0 < 1$ $\curvearrowright$ sonst $F_{N1} < 0$, macht kein Sinn)

[Prüfung: Herleitung nachgerechnet, korrekt. Gleichungsnummer: auf S. 19 ist die Gleichung für $F_{N1}$ undeutlich nummeriert ((8) oder (7)); auf S. 20 wird sie als (7) referenziert.]

---

## Seite 21

**(5)** s. Übung Reibung A.14 [?]

> Skizze: Trommel (Radius $r$) und Bremsscheibe (Radius $R$) fest miteinander verbunden, drehbar gelagert in O. Am Seil auf der Trommel hängt $F_G$ (rot ↓, Fördereinrichtung). Ein Bremsband umschlingt die Bremsscheibe mit Umschlingungswinkel $\alpha$: ein Ende links am Boden festgelegt (Festpunkt), das andere Ende senkrecht nach unten zu einem Hebel. Hebel: waagerecht, links in A drehbar gelagert (Festlager), Bremsband greift im Abstand $a$ von A an, Kraft $F$ (rot ↓) am Hebelende im Abstand $L$ von A. Grüne Umrandungen: I = Scheibe/Trommel, II = Hebel.

- Fördereinrichtung für $F_G$
- Trommel und Bremsscheibe fest miteinander verbunden

$\to$ Wie groß muss $F$ sein, damit gleichförmiges Absenken der Kraft (Last) gewährleistet ist?

geg.: $F_G = 2$ kN, $\alpha = 210°$, $\mu = 0{,}2$, $L/a = 25$, $R/r = 5$
ges.: $F$

**Lös.:** $\curvearrowright$ Seilreibung!

$$F_{S1} = F_{S2}\,e^{\mu\alpha} \quad (1)$$

$\curvearrowright$ Reibkraft $\to$ Moment, Gewicht $\to$ Moment } müssen im Gleichgewicht sein!

(durchgestrichen: „Moment durch $F_G$ (um O): $M_{F_G} = F_G r$")

**I**

> Skizze: Scheibe um O; $F_{S1}$ (links unten, schräg), $F_{S2}$ (rechts, ↓), $F_G$ (↓ an der Trommel, Radius $r$).

$\curvearrowleft O:\; F_{S2}\cdot R - F_{S1}\cdot R + F_G\cdot r = 0$

mit (1):
$F_{S2}\cdot R - F_{S2}e^{\mu\alpha}R + F_G\cdot r = 0$
$F_{S2}R(1 - e^{\mu\alpha}) + F_G r = 0$

$$F_{S2} = -F_G\frac{r}{R}\frac{1}{1 - e^{\mu\alpha}} \quad (2)$$

---

## Seite 22

**II**

> Skizze: Hebel, in A gelagert ($F_{AH}$ →, $F_{AV}$ ↑), Bandkraft $F_{S2}$ (↑) im Abstand $a$, $F$ (↓) am Ende im Abstand $L$.

$\rightarrow:\; F_{AH} = 0 \quad (3)$
$\uparrow:\; F_{AV} + F_{S2} - F = 0 \quad (4)$
$\curvearrowleft A:\; -F_{S2}\cdot a + F\cdot L = 0 \quad (5)$

aus (5): $F = F_{S2}\dfrac{a}{L}$

mit (2):
$$\underline{F = -F_G\frac{r}{R}\frac{1}{1 - e^{\mu\alpha}}\frac{a}{L}}$$

$F = -2000\cdot\frac{1}{5}\cdot\frac{1}{1 - e^{0{,}2\alpha}}\cdot 25^{-1} = -\frac{400}{25}\frac{1}{1 - e^{0{,}2\alpha}} = \frac{-16}{1 - e^{0{,}2\alpha}} = \underline{\underline{14{,}79\ \text{N}}}$

[Prüfung: $\alpha = 210° = 3{,}665$ rad; $\mu\alpha = 0{,}733$; $e^{0{,}733} = 2{,}082$; $F = 16/1{,}082 = 14{,}79$ N – korrekt. Hinweis: Im Zahlenausdruck muss $\alpha$ im Bogenmaß eingesetzt werden.]

---

## Didaktische Gliederung

1. **5.1 Grundlagen** (S. 1–3)
   - Bewegungswiderstand bei Relativbewegung (fest/fest, fest/flüssig, fest/gas); Reibungskraft $R$ ist der Relativbewegung entgegengerichtet; Wechselwirkung an beiden Kontaktpartnern.
   - Beschränkung der Statik auf Festkörper/Festkörper, starre Körper.
   - Ursachen der Reibung (Rauheit, Temperatur, Feuchte, Van-der-Waals).
   - Gedankenexperiment (Klotz mit steigender Zugkraft): 1. Haftung (Gleichgewicht), 2. Gleitreibung (dynamisches Problem, $ma = F - R$).
   - Praktische Bedeutung (Fortbewegung, Nägel/Schrauben; Gleitreibung: Erwärmung, Energieverluste).
2. **5.2 Coulombsche Reibungsgesetze** (S. 3–5)
   - 5.2.1 Haftung: $F_H = F$ bis Grenzwert $F_{H0}$; Def. **Haftbedingung** $F_H \le F_{H0} = \mu_0 F_N$ (5.2.1); $F_H$ ist **Reaktionskraft**; Def. **Haftkoeffizient** $\mu_0$; **Haftungskegel** $\tan\rho_0 = \mu_0$ (Gleichgewicht, wenn Wirkungslinie der Resultierenden innerhalb des Kegels).
   - 5.2.2 Gleitreibung: $R = \mu F_N$ (5.2.2), unabhängig von der Relativgeschwindigkeit, entgegen der Relativbewegung; $R$ ist **eingeprägte Kraft**; $\mu < \mu_0$.
3. **5.3 Beispiele** (S. 6–10): schiefe Ebene (Fallunterscheidung Rutschen nach unten/oben), Leiter an der Wand (Grenzfall in beiden Kontaktstellen).
4. **5.4 Seilhaftung und Seilreibung** (S. 11–13): Freischnitt eines Seilelements $ds$, Kleinwinkelnäherung, Vernachlässigung von Termen höherer Ordnung, DGL $dF_S/F_S = \mu_0\,d\varphi$, Integration $\to$ **Euler-Eytelwein-Formel** $F_{S2} \le F_{S1}e^{\mu_0\alpha}$ (Haftung), $F_{S2} = F_{S1}e^{\mu\alpha}$ (Reibung); Umschlingungswinkel $\alpha$ im Bogenmaß.
5. **Weitere Beispiele** (S. 13–22): Seilhaftung (Pferd/Saloon), Stab an der Wand (Fallunterscheidung), Scheibe mit Pendelstab und Klotz, Hülse (Selbsthemmung), Bandbremse.

**Rechenschema Haftungsaufgaben (wie im Skript angewandt):**
1. Mögliche Bewegungsrichtung(en) überlegen $\to$ **Fallunterscheidung** (Haftkraft wirkt der drohenden Bewegung entgegen).
2. Freischnitt mit $F_N$ (senkrecht zur Kontaktfläche) und $F_H$ (tangential) in jeder Kontaktstelle.
3. Gleichgewichtsbedingungen aufstellen ($\sum F_x$, $\sum F_y$, $\sum M$).
4. Haftbedingung $F_H \le \mu_0 F_N$ je Kontaktstelle; Anzahl Unbekannte = Anzahl Gleichungen prüfen.
5. Grenzfall „=" einsetzen, nach gesuchter Größe auflösen, dann Ungleichung/Bereich angeben (Vorsicht: Vorzeichenwechsel beim Multiplizieren mit negativen Ausdrücken).

**Rechenschema Seilreibung:** Zugrichtung festlegen (größere Kraft auf der Seite, in die gezogen wird) $\to$ $F_{groß} = F_{klein}\,e^{\mu\alpha}$ $\to$ mit Momenten-/Kräftegleichgewicht der angeschlossenen Körper koppeln.

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| 5.3.1 | Masse auf schiefer Ebene, Kraft $F$ hangparallel | $F_G$, $\alpha$, $\mu_0$; Zahlen: $\alpha = 30°$, $\mu_0 = 0{,}15$ | $F_G(\sin\alpha - \mu_0\cos\alpha) \le F \le F_G(\sin\alpha + \mu_0\cos\alpha)$; $0{,}37F_G \le F \le 0{,}63F_G$ | 6–7 |
| 5.3.2 | Leiter an Wand, Person ganz oben | $\mu_{0A}$, $\mu_{0B}$, $F_G$, $L$; Zahl: $\mu_{0A} = 0{,}15$ | $F_{NA} = F_G/(1+\mu_{0A}\mu_{0B})$, $F_{NB} = \mu_{0A}F_{NA}$, $\tan\alpha = 1/\mu_{0A}$, $\alpha = 81{,}5°$ | 8–10 |
| – | Tabelle Seilhaftung Leder/Holz | $\mu_0 = 0{,}5$, $\alpha = 0 \dots 360°$ | 1; 1,28; 1,65; 2,72; 7,39 [Prüfung: falsch, richtig 1; 1,48; 2,19; 4,81; 23,1] | 13 |
| (1) | Pferd vor dem Saloon (Riemen um Stange) | $F_G$ = 200 g, $F$ = 4 kN, $\mu_0 = 0{,}5$, $\alpha = 2\pi n + \pi/2$ | $\alpha = 15{,}24$, $n = 2{,}18 \to n = 3$; $F_{max} = 54$ kN (Faktor 27 000) | 13–14 |
| (2) | Stab an der Wand, Seil zu Punkt C | $F_G$, $\mu_0 = 0{,}5$, $a = 1$ m | $x_{min} = a/(2+\mu_0) = 0{,}4$ m, $x_{max} = a/(2-\mu_0) = 0{,}67$ m | 14–17 |
| (3) | Dreiecksscheibe (Festlager B) mit Pendelstab auf Klotz | $a, b, c, L, \alpha, F$ | $F_P = FL\cos\alpha/((a+c)\sin\gamma)$, $\gamma = \arctan(b/c)$; $\mu_0 \ge c/b$ | 17–18 |
| (4) | Hülse auf Stange mit Kragarm (Selbsthemmung) | $a, h, d, F_G$ | $F_{N1} = F_{N2}$, $F_{H1} = F_{H2} = F_G/2$; $\mu_0 \ge h/(2a)$ | 19–20 |
| (5) | Bandbremse an Fördertrommel (Hebel) | $F_G = 2$ kN, $\alpha = 210°$, $\mu = 0{,}2$, $L/a = 25$, $R/r = 5$ | $F = -F_G\frac{r}{R}\frac{a}{L}\frac{1}{1-e^{\mu\alpha}} = 14{,}79$ N | 21–22 |

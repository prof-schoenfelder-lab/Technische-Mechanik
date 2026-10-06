# Technische Mechanik – Statik: Inhalt, Grundlagen, Kräfte, Momente, Lager (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen (Prof. Schönfelder)
Quelle: `Quellen/Vorlesung-2013/1-Inhalt-Kräfte-Momente-Lager.pdf` (44 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Lasten/Ergebnisse, Grün = Bemaßungen, Kommentare, Korrekturen.
- Text sinngemäß-wörtlich; durchgestrichene Passagen nur, wenn inhaltlich relevant (als ~~…~~).
- Unsichere Lesungen sind mit [?] markiert; Anmerkungen zur Nachrechnung mit [Prüfung: …].

---

## Seite 1

### Inhalt

0. Grundlagen – Kräfte und Momente
1. Äquivalenz und Gleichgewicht im ebenen zentralen und allgemeinen Kraftsystem
2. Berechnung Lager- und Verbindungsreaktionen
3. Fachwerke
4. Schnittreaktionen
5. Reibung
6. Berechnung von Schwerpunkten und Flächenmomenten 1. + 2. Ordnung
7. Grundlagen der Festigkeitslehre
   → Spannung, Verzerrung und Materialgesetz
8. Zug + Druck in Stäben
9. Einfache Balkenbiegung

---

## Seite 2

Randnotiz oben rechts: *Altenbach, Holzmann/Meyer/Schumpich [?], Technische Mechanik (Literaturhinweis), 2012* [?]

### 0. ~~Grundlagen~~ Einführung

- Mechanik ist ein grundlegendes Fach der Physik (älteste Disziplin in der Physik)
  - ↳ beschäftigt sich mit Bewegungen materieller Körper und den Kräften und Momenten, die diese hervorrufen
  - Randnotizen: • Wurzeln in Antike • Naturerscheinungen erkunden • eng mit Mathematik verbunden
- Technische Mechanik
  - → Teil der Ingenieurwissenschaften
  - → liefert theoretische Berechnungsverfahren für Maschinenbau und Bauingenieurwesen
  - (→ Aufteilung in Spezialisierungen (Strömungsmechanik, Festigkeitslehre, …))

> Skizze (Baumdiagramm): „Mechanik" verzweigt in
> – links: „Körper in Bewegung" → **Dynamik** (rot)
> – rechts: „Körper in Ruhe oder gleichförmiger geradliniger Bewegung" → **Statik** (rot), diese verzweigt in „unverformbare Körper" → **Stereostatik** und „verformbare Körper" → **Elastostatik (Festigkeitslehre)**.
> Der Statik-Zweig ist rot gestrichelt umrandet: „Inhalt der Vorlesung".

---

## Seite 3

**Bsp.**

> Skizze 1 „Rad – Maschinenbau": Fahrrad (zwei Räder, Rahmen aus Stäben). Rote Kräfte $F$: schräg auf den Lenker, senkrecht nach unten auf den Sattel, senkrecht nach unten am Tretlager (Pedal).

> Skizze 2 „Umlenkrolle": Rolle, über zwei Stäbe an einer Wand befestigt (Halterung oben schräg, unten horizontal). Ein Seil läuft über die Rolle; ein Seilende senkrecht nach unten mit Kraft $F$, das andere schräg nach rechts unten mit Kraft $F$. Oben: „$\neq\; L\,?\; \neq$" (Frage nach der Länge/Lage der Halterung [?]).

> Skizze 3 „Weinständer – Gleichgewicht": Flasche, die schräg in einem schräg stehenden Brett (Weinflaschenhalter) steckt, unten auf dem Boden abgestützt. Gewichtskraft $F$ im Flaschenschwerpunkt; rote Fragezeichen mit Drehpfeilen links und rechts (kippt das System?).

> Skizze 4 „Brücke – Bauwerke": Schrägseilbrücke über einem Tal mit zwei Pylonen (unten eingespannt), Seile vom Pylonkopf zur Fahrbahn. Rote Frage an Pylon und Seil: „$t, L$?" (Dicke, Länge?).

---

## Seite 4

### 1. Grundlagen

#### 1.1 Die Kraft und das Moment

**Kraft**

$$F = m\cdot a \;\Rightarrow\; m\cdot g = F_G \quad\text{(Gewichtskraft)}$$

$$[F] = \mathrm{N} = \frac{\mathrm{kg\,m}}{\mathrm{s}^2}$$

Randnotiz: • Gewichtskraft

> Skizze: Klotz (Masse $m$) auf schraffiertem Boden, Erdbeschleunigung $\vec g$ nach unten; rote Gewichtskraft $F_G$ im Schwerpunkt nach unten.

- Kräfte (auch Momente) sind unsichtbar und können an ihren Wirkungen erkannt werden
  - → Bewegungsänderung (Beschleunigung)
  - → Deformationen

Randnotiz: $a = 0$, $v = \text{const.}$ ! $\;F = 0$ !

> Skizze: Kraft $F$ drückt auf eine Unterlage, die sich dabei eindellt (Deformation, gestrichelt die unverformte Oberfläche).

> Skizze: Klotz auf schraffierter Unterlage, Seil schräg über eine Umlenkrolle, am anderen Seilende hängt ein Gewicht ($F_G$). Pfeil → freigeschnittener Klotz mit roter Kraft $\vec F$ an der oberen rechten Ecke, schräg nach oben rechts; beschriftet „Angriffspunkt", „Betrag" (Abstand zwischen zwei Kreuzen auf dem Pfeil), „Richtungssinn" (Pfeilspitze) und gestrichelte „Wirkungslinie".

↳ Kraft kann als Vektor beschrieben werden durch Angabe:
- skalarer Wert (Betrag)
- Richtung – Wirkungslinie
- Richtungssinn – Pfeilspitze
- Angriffspunkt

---

## Seite 5

$$\vec F = F\,\vec e \qquad (\vec e:\ \text{Basisvektor})$$

> Skizze: Horizontaler roter Pfeil $F$, darunter grün der Einheitsvektor $\vec e$ in gleicher Richtung.

- im kartesischen KOS (Koordinatensystem)

$$\vec F = \underbrace{\vec F_x}_{\text{Komponente}} + \vec F_y + \vec F_z = \underbrace{F_x}_{\text{Koordinate}}\,\vec e_x + F_y\,\vec e_y + F_z\,\vec e_z$$

> Skizze: Räumliches Koordinatensystem $x$ (nach rechts), $y$ (nach oben), $z$ (nach vorn links unten) mit Quader (blau) als Hilfskonstruktion. Vom Ursprung roter Kraftvektor $F$ zur gegenüberliegenden Quaderecke; rote Komponenten $F_x$ (auf $x$-Achse), $F_y$ (auf $y$-Achse), $F_z$ (auf $z$-Achse). Grüne Einheitsvektoren $\vec e_x, \vec e_y, \vec e_z$ am Ursprung. Winkel $\alpha$ zwischen $F$ und $x$-Achse, $\beta$ zwischen $F$ und $y$-Achse, $\gamma$ zwischen $F$ und $z$-Achse.

Richtungskosinus:
$$\cos\alpha = \frac{F_x}{F},\qquad \cos\beta = \frac{F_y}{F},\qquad \cos\gamma = \frac{F_z}{F}$$

$$F = |\vec F| = \sqrt{F_x^2 + F_y^2 + F_z^2}$$

---

## Seite 6

- Darstellung in der Ebene / Zerlegung der Kraft

> Skizze: Ebenes $x$-$y$-Koordinatensystem, grüne Einheitsvektoren $\vec e_x$, $\vec e_y$. Rote Kraft $F$ vom Ursprung schräg nach rechts oben; gestricheltes Kräfteparallelogramm (Rechteck) mit Komponenten $F_x$ auf der $x$-Achse und $F_y$ auf der $y$-Achse. Winkel $\alpha$ zwischen $F$ und $x$-Achse, $\beta$ zwischen $F$ und $y$-Achse (auch an der Pfeilspitze wiederholt eingetragen).

$$\cos\alpha = \frac{F_x}{F},\quad \sin\beta = \frac{F_x}{F},\qquad \cos\beta = \frac{F_y}{F},\quad \sin\alpha = \frac{F_y}{F}$$

$$F_x = \cos\alpha\cdot F = \sin\beta\,F,\qquad F_y = \cos\beta\cdot F = \sin\alpha\,F$$

- Einzelkräfte mit Angriffspunkt und Wirkungslinie sind Idealisierungen:
  - ↳ Kräfte wirken in der Realität als
    - Volumenkräfte

      > Skizze: Körper mit vielen kleinen roten Pfeilen nach unten (verteilte Gewichtskraft) ⇒ derselbe Körper mit einer resultierenden Einzelkraft $F_G$ im Schwerpunkt.
    - Flächenkräfte, z. B. Staumauer

      > Skizze: Staumauer (Querschnitt, keilförmig) mit roten Pfeilen (Wasserdruck), die auf die senkrechte Mauerseite wirken.

---

## Seite 7

### Das Moment

- Kräftepaar: – gleich große Kräfte auf parallelen Wirkungslinien (entgegengesetzt gerichtet)

> Skizze: Zwei parallele vertikale Wirkungslinien im Abstand $b$; links Kraft $F$ nach oben, rechts Kraft $F$ nach unten.

- ↳ keine Resultierende möglich
- ↳ Drehbewegung am Körper

> Skizze: Quader (Breite $b$), an zwei gegenüberliegenden Seiten je eine Kraft $F$ in entgegengesetzter Richtung (horizontal). Daraus resultierendes Moment $M$ als Doppelpfeil senkrecht nach oben mit Drehsinn-Kringel.

$$\boxed{F\cdot b = M}\quad\text{, das Moment } M$$

$$[M] = \frac{\mathrm{kg\,m^2}}{\mathrm{s^2}} = \mathrm{Nm}$$

(↳ Darstellung als Doppelpfeil)

Kasten links: *s. Dankert S. 11* [?] (Literaturverweis)

> Skizze (Kasten): Körper mit Kräftepaar „$F$" [?] = Körper mit Momenten-Drehpfeil (Kräftepaar und Moment sind gleichwertig).

- man kann zeigen, dass das Kräftepaar entlang der Wirkungslinien verschoben und durch Drehung der Wirkungslinien an jeden beliebigen Punkt eines starren Körpers verschoben werden kann, so dass gilt: **ein Moment darf beliebig in der Ebene verschoben werden**
  - ↳ Momente dürfen zu einem resultierenden Moment addiert werden

---

## Seite 8

> Skizze: Punkt $0$ (Bezugspunkt), schräge rote Kraft $F$ mit gestrichelter Wirkungslinie. Grüner Ortsvektor $\vec r$ von $0$ zum Angriffspunkt der Kraft; Winkel $\sphericalangle(\vec r, \vec F)$ am Angriffspunkt. Senkrechte (rechter Winkel markiert) von $0$ auf die Wirkungslinie = Hebelarm $b$ (blau beschriftet „Hebelarm").

Moment am Punkt 0: Produkt aus Hebelarm $b$ (kürzester Abstand zur Wirkungslinie) und Kraft

$$M = F\cdot b$$

↳ Moment ändert sich mit Wahl des Bezugspunkts, aber nicht mit Verschiebung der Kraft auf der Wirkungslinie

als Vektor:
$$\vec M = \vec r \times \vec F \qquad\text{(Vektorprodukt)}$$

$$\boxed{M = |\vec M| = |\vec r|\cdot|\vec F|\cdot \sin\sphericalangle(\vec F, \vec r)}$$

mit $\sin\sphericalangle(\vec F,\vec r) = \dfrac{b}{|\vec r|}$.

> Skizze (Rechte-Hand-Regel): Vektoren $\vec a$ (nach rechts), $\vec b$ (schräg nach hinten), $\vec c$ (nach oben) mit $\vec a \times \vec b = \vec c$.

- wie bei $F$:
$$\vec M = \vec M_x + \vec M_y + \vec M_z = M_x\,\vec e_x + M_y\,\vec e_y + M_z\,\vec e_z$$

---

## Seite 9

### 1.2 Axiome der Statik

(• Axiome sind Lehrsätze, die keinen Beweis bedürfen
  → aus Beobachtungen entnommen, aus Erfahrungen stammend)

- Annahme des starren Körpers
  - → Ein starrer Körper ist ein fiktives Modell, das sich unter Einwirkung von Kräften nicht verformt.

> Skizze: Links „starr": Kugel auf Unterlage mit Kraft $F$ von oben (bleibt rund); darunter Balken auf zwei Lagern (Fest- und Loslager) mit Kraft $F$, gerade bleibend → „Statik". Rechts „deformierbar": Kugel wird unter $F$ plattgedrückt (daneben schraffierte, eingedellte Kugel); darunter Balken auf zwei Lagern, unter $F$ durchgebogen → „(Elastostatik)".

Randnotiz: Axiome der Statik bauen auf der Idealisierung des starren Körpers! ↓ gilt nicht immer, kann aber oft angenommen werden! (Gummi / Stahl)

**1. Axiom: Linienflüchtigkeit der Kräfte**
- → die Wirkung einer Kraft auf einen starren Körper bleibt unverändert, wenn man sie entlang ihrer Wirkungslinie verschiebt

> Skizze: Starrer Block auf einem Lager mit Kräften $F_1$ (links oben) und $F_2$ (rechts oben), beide nach unten = derselbe Block, bei dem $F_1$ entlang seiner Wirkungslinie an die Unterseite verschoben ist (zieht unten nach unten).

---

## Seite 10

**2. Axiom: Kräfteparallelogramm**
- → Die Wirkung zweier Kräfte $F_1$ und $F_2$, die an einem gemeinsamen Punkt angreifen, ist gleich einer Kraft $F_R$, die sich als Diagonale eines mit den Seiten $F_1$ und $F_2$ gebildeten Parallelogramms ergibt.

> Skizze: Gemeinsamer Angriffspunkt, $\vec F_1$ schräg nach rechts oben, $\vec F_2$ schräg nach rechts unten; gestricheltes Parallelogramm, Diagonale $\vec F_R$.

↳ **Äquivalenz von Kräftegruppen**
Zwei Kräftegruppen heißen statisch äquivalent, wenn sie auf einen starren Körper dieselbe Wirkung ausüben
$$(\vec F_1, \vec F_2 \;\widehat{=}\; \vec F_R)$$

**3. Axiom: Gleichgewicht**
- → zwei Kräfte befinden sich im Gleichgewicht, wenn sie
  - gleich groß sind
  - auf derselben Wirkungslinie liegen
  - entgegengesetzt gerichtet sind

---

## Seite 11

**Bsp.:**

> Skizze: Körper (blaue Umrisslinie) mit gemeinsamem Angriffspunkt im Inneren; rote Kräfte $\vec F_1$ (nach rechts oben), $\vec F_2$ (nach rechts unten), deren Resultierende $\vec F_{12}$ (gestrichelt, nach rechts) und $\vec F_3$ (nach links, entgegengesetzt zu $\vec F_{12}$).

ges.: $\vec F_3$ so, dass Körper im Gleichgewicht → keine Bewegung

$$\underbrace{\vec F_1 + \vec F_2}_{\vec F_{12}} + \vec F_3 = \vec 0 \quad\Rightarrow\quad \vec F_3 = -\vec F_{12}$$

bedeutet auch:
$$\boxed{\Rightarrow \vec F_R = \vec 0}$$

**4. Axiom: Wechselwirkungsgesetz**
- → Wird von einem Körper auf einen zweiten eine Kraft ausgeübt, so reagiert dieser mit
  - einer gleich großen Kraft
  - auf der gleichen Wirkungslinie
  - aber entgegengesetzter Richtung

$$\boxed{\text{Newton: actio} = \text{reactio}}$$

↳ **Schnittprinzip (Euler)**
- → um Kräfte zwischen oder in Körpern sichtbar zu machen
- → gedankliche Schnitte, um
  - komplexe Probleme in Teilprobleme zu zerlegen
  - alle angreifenden Kräfte sichtbar zu machen

↳ an Schnittufern immer paarweise Kräfte entgegengesetzt

---

## Seite 12

**Bsp.** (Freischneiden und Wechselwirkung)

> Skizze ⓐ: (1) Block auf schraffiertem Boden, grün umrandet (freigeschnitten), Gewichtskraft $F_G$ nach unten, Bodenkraft nach oben. (2) Block über Boden, freigeschnitten: am Block Kraft nach oben, am Boden gleich große Kraft nach unten (Kraftpaar an der Schnittstelle). (3) Strichmännchen auf dem Boden (blau umrandet): an beiden Füßen Kräfte nach unten auf den Boden und nach oben auf die Füße.

> Skizze ⓑ: Zwei sich berührende Kugeln, von außen mit Kräften zusammengedrückt (links →, rechts ←); grüner Schnitt durch die Berührstelle. Rechts: beide Kugeln getrennt, an der Berührstelle je eine Kontaktkraft, entgegengesetzt gerichtet (rechte Kugel grün umrandet).

> Skizze ⓒ: Stab, an beiden Enden mit $F$ auseinandergezogen (links ←, rechts →); grüner Schnitt durch den Stab. Darunter beide Teilstäbe: linkes Teil mit $F$ (←) und Schnittkraft $F_i$ (→), rechtes Teil mit $F_i$ (←) und $F$ (→). Rot: „Wechselwirkung!"

> Skizze ⓓ: Rolle an der Decke aufgehängt, Seil über die Rolle, an beiden Seilenden hängen Massen (Gewichte $F_{G1}$, $F_{G2}$); $\vec g$ nach unten. Grüne Schnittbereiche I (Masse 1), II (Masse 2), III (Achse der Rolle), IV (Aufhängung/Rolle), V (gesamte Rolle).
> – Schnitt I/II: Seilkräfte am Seil $-K_1$ [?], $-K_2$ [?] (nach unten), an den Massen $K_1$, $K_2$ (nach oben) und $F_{G1}$, $F_{G2}$ (nach unten).
> – Schnitt III/IV: Rolle mit Seilkräften $-K_1$, $-K_2$ nach unten; an der Achse $+A$ (nach oben auf die Rolle), $-A$ (nach unten auf die Aufhängung).
> – Aufhängung: an der Decke $-B$/$+B$ als Wechselwirkungspaar; am Stab $-A$ nach unten.
> – V (gesamte Rolle als ein Teilsystem): $B$ nach oben, $F_{G1}$, $F_{G2}$ nach unten.

---

## Seite 13

### 2. Kräftesysteme

#### 2.1 Ebenes zentrales Kräftesystem

- ein ebenes zentrales Kräftesystem liegt vor, wenn
  - → alle Kräfte in einer Ebene liegen
  - → alle Wirkungslinien dieser Kräfte sich in einem Punkt schneiden

> Skizze: $x$-$y$-Koordinatensystem; drei rote Kräfte $F_1$ (nach rechts oben), $F_2$ (nach links oben), $F_3$ (steil nach oben) mit gemeinsamem Angriffspunkt im Ursprung; Wirkungslinien gestrichelt nach unten verlängert (schneiden sich im Ursprung).

##### 2.1.1 Äquivalenz

$$\vec F_{res} = \vec F_1 + \vec F_2 + \ldots + \vec F_i + \ldots + \vec F_n = \sum_{i=1}^{n} \vec F_i$$

Randnotiz: • Kräftegruppen können ersetzt werden (2. Axiom) → Vektoren addieren sich

- grafische Lösung

> Skizze: Krafteck (Kräftepolygon): $\vec F_2$, daran $\vec F_1$, daran $\vec F_3$ aneinandergehängt (Spitze an Fuß); $\vec F_{res}$ vom Anfang von $\vec F_2$ zur Spitze von $\vec F_3$.

- so konstruieren, dass sich die Linien nicht „durchschneiden" → umfahrbar
- Randnotiz: • ohne praktische Bedeutung → aber wichtig für Verständnis

---

## Seite 14

- analytische Lösung
  - ↳ Nutzung der Komponenten $F_x$, $F_y$ ($F_z$)

> Skizze: $x$-$y$-System; rote Kraft $\vec F$ unter Winkel $\alpha$ zur $x$-Achse, zerlegt in $\vec F_x$ (horizontal) und $\vec F_y$ (vertikal) als Rechteck.

$$\vec F = \vec F_x + \vec F_y,\qquad \vec F = F\cdot\vec e$$

$$\vec F_1 = F_{1x}\,\vec e_x + F_{1y}\,\vec e_y,\quad \vec F_2 = F_{2x}\,\vec e_x + F_{2y}\,\vec e_y,\quad \ldots,\quad \vec F_n = F_{nx}\,\vec e_x + F_{ny}\,\vec e_y$$

↳ Äquivalenz für $\vec F_1$ und $\vec F_2$:
$$\vec F_R = \vec F_1 + \vec F_2 = F_{1x}\vec e_x + F_{1y}\vec e_y + F_{2x}\vec e_x + F_{2y}\vec e_y = \underbrace{(F_{1x}+F_{2x})}_{R_x}\vec e_x + \underbrace{(F_{1y}+F_{2y})}_{R_y}\vec e_y$$

$$\sum_{i=1}^{n}\vec F_i = \vec F_R = R_x\,\vec e_x + R_y\,\vec e_y,\qquad R_x = F_{1x}+F_{2x},\quad R_y = F_{1y}+F_{2y}$$

↳
$$\boxed{F_{Rx} = \sum_i^n F_{ix} = R_x,\qquad F_{Ry} = \sum_i^n F_{iy} = R_y}$$

$$\boxed{F_R = \sqrt{F_{Rx}^2 + F_{Ry}^2}},\qquad \tan\alpha_R = \frac{F_{Ry}}{F_{Rx}}$$

---

## Seite 15

**Bsp.:** Resultierende zweier Kräfte

> Skizze: $x$-$y$-System; $F_1$ im 1. Quadranten unter $30°$ zur $x$-Achse (Komponente $F_{1x}$ gestrichelt), $F_2$ im 2. Quadranten unter $45°$ zur negativen $x$-Achse; Resultierende $F_R$ (grün) fast senkrecht nach oben, leicht nach links.

geg.: $F_1 = 20\,\mathrm N$, $F_2 = 30\,\mathrm N$; ges.: $F_R$

$$F_{1x} = F_1\cdot\cos 30° = 17{,}32\,\mathrm N\ (\text{korrigiert aus } \sout{8{,}66\,\mathrm N}),\qquad F_{1y} = F_1\cdot\sin 30° = 10\,\mathrm N$$
$$F_{2x} = -F_2\cos 45° = -21{,}21\,\mathrm N,\qquad F_{2y} = F_2\sin 45° = 21{,}21\,\mathrm N$$

(Im Original steht bei $F_{2x}$ der Wert ohne Minuszeichen „$= 21{,}21\,\mathrm N$", bei $F_{2y}$ ist „$\sin 85°$" [?] zu „$\sin 45°$" korrigiert.)

$$F_{Rx} = F_{1x} + F_{2x} = -3{,}89\,\mathrm N,\qquad F_{Ry} = F_{1y} + F_{2y} = 31{,}2\,\mathrm N$$

> Skizze (grün, Nebenrechnung): Einheitskreis mit rechtwinkligem Dreieck (Hypotenuse $c$, Gegenkathete $a$, Ankathete $b$, Winkel $\alpha$): $\sin\alpha = a/c$, $\cos\alpha = b/c$, $\tan\alpha = a/b$, $\cot\alpha = b/a$.

$$F_R = \sqrt{F_{Rx}^2 + F_{Ry}^2} = \underline{31{,}44\,\mathrm N}$$

[Prüfung: $\sqrt{3{,}893^2 + 31{,}213^2} = 31{,}455\,\mathrm N \approx 31{,}46\,\mathrm N$; Abweichung im Original nur Rundung.]

$$\tan\alpha_R = \frac{F_{Ry}}{F_{Rx}},\qquad \arctan\frac{F_{Ry}}{F_{Rx}} = -82{,}9° = \alpha_R\ (\text{Taschenrechner}) \;\to\; \alpha_R = 97{,}1°$$

> Skizze: kleines Koordinatenkreuz mit Pfeil im 2. Quadranten und Drehpfeil „$+180°$".

[Prüfung: $\alpha_R = 180° - 82{,}89° = 97{,}11°$ ✓.]

Quadrantenregel für $\alpha_R$ (vier Skizzen, $\alpha$ jeweils von der positiven $x$-Achse gemessen):
| Quadrant | $F_{Rx}$ | $F_{Ry}$ | Korrektur zu $\arctan(F_{Ry}/F_{Rx})$ |
|---|---|---|---|
| I | $>0$ | $>0$ | – |
| II | $<0$ | $>0$ | $+180°$ |
| III | $<0$ | $<0$ | $+180°$ |
| IV | $>0$ | $<0$ | – (bzw. $+360°$) |

---

## Seite 16

##### 2.1.2 Gleichgewicht

- Körper ist im Gleichgewicht, wenn gilt
$$\boxed{\vec F_R = \vec 0}$$
  ↳ keine resultierende Kraft, keine Änderung der Bewegung | Es fliegt nicht

Erinnerung: Äquivalenz!

> Skizze: Zentrales System mit $F_1$, $F_2$, $F_3$; daneben Krafteck $F_1 \to F_2 \to F_3$, das sich **nicht** schließt; Schlusslinie $F_R$ (eingerahmt): $F_R \neq 0$.

↳ Gleichgewicht

> Skizze: Zentrales System $F_1$ (rechts oben), $F_2$ (links oben), $F_3$ (links unten); Krafteck $F_1, F_2, F_3$ als geschlossenes Dreieck: „geschlossenes Kräftepolygon!"

$$\Rightarrow\quad \boxed{F_{Rx} = \sum F_{ix} \overset{!}{=} 0,\qquad F_{Ry} = \sum F_{iy} \overset{!}{=} 0,\qquad F_{Rz} = \sum F_{iz} \overset{!}{=} 0}$$

- 3 Gleichgewichtsbedingungen beim räumlichen zentralen Kräftesystem

---

## Seite 17

für ebenes zentrales Kräftesystem:
$$\boxed{\sum F_{ix} \overset{!}{=} 0,\qquad \sum F_{iy} \overset{!}{=} 0}\qquad\text{2 Gleichgewichtsbedingungen}$$

**Bsp.:** Kugel an Seil an glatter Wand

> Skizze: Senkrechte Wand (links, schraffiert). Am Wandpunkt oben ist ein Seil der Länge $L$ befestigt, das zum Mittelpunkt einer Kugel (Radius $r$, Masse $m$) führt; die Kugel liegt an der Wand an. Winkel zwischen Wand und Seil markiert (grün, $*$). Gewichtskraft $F_G$ im Mittelpunkt nach unten. Kugel grün umrandet (Freischnitt).

geg.: $L = 40\,\mathrm{cm}$, $r = 10\,\mathrm{cm}$
ges.: Kraft $F_S$ im Seil, $F_N$ an Wand

**Lös.:** ① KOS: $x$ nach rechts, $y$ nach oben

> Skizze (Freikörperbild): Kugel freigeschnitten; Seilkraft $F_S$ entlang des Seils zum Aufhängepunkt (Wechselwirkungspaar am Seil eingezeichnet), Wandnormalkraft $F_N$ horizontal nach rechts auf die Kugel (Gegenkraft an der Wand nach links), Gewicht $m g$ nach unten. Winkel $\alpha$ zwischen Seil und Horizontaler am Kugelmittelpunkt.

→ ebenes zentrales Kräftesystem

$$\sum F_x \overset{!}{=} 0:\quad F_N - F_S\cos\alpha \overset{!}{=} 0$$
$$\sum F_y \overset{!}{=} 0:\quad F_S\sin\alpha - m g \overset{!}{=} 0$$

Nebenrechnung (grüner Kasten, rechtwinkliges Dreieck mit Hypotenuse $L$, Ankathete $r$):
$$\sin\alpha = \frac{\sqrt{L^2 - r^2}}{L} = \frac{\sqrt{15}}{4},\qquad \cos\alpha = \frac{r}{L} = \frac14$$

↳ lin. Gleichungssystem:
$$F_S = \frac{m g}{\sin\alpha} = m g\left(\frac{\sqrt{15}}{4}\right)^{-1},\qquad F_N = m g\cdot\frac{\cos\alpha}{\sin\alpha} = m g\,\frac{1}{\sqrt{15}}$$

[Prüfung: $F_S = 4/\sqrt{15}\;mg \approx 1{,}033\,mg$, $F_N = mg/\sqrt{15} \approx 0{,}258\,mg$ ✓. Beachte: $L$ ist hier die Länge vom Aufhängepunkt bis zum Kugel**mittelpunkt** (wegen $\cos\alpha = r/L$).]

---

## Seite 18

② Alternative mit gedrehtem KOS ($x$ schräg nach rechts oben, $y$ schräg nach links oben, $y$ in Seilrichtung)

> Skizze: Kugel freigeschnitten mit $F_S$ (entlang Seil), $F_N$ (horizontal auf die Kugel), $m\cdot g$ (nach unten), Winkel $\alpha$ am Mittelpunkt.

$$\sum F_x = 0:\quad F_N\sin\alpha - m g\cos\alpha = 0 \quad (1)$$
$$\sum F_y = 0:\quad F_S - F_N\cos\alpha - m g\sin\alpha = 0 \quad (2)$$

aus (1):
$$F_N = m g\,\frac{\cos\alpha}{\sin\alpha}\ \checkmark$$

einsetzen in (2), mit $\sin^2\alpha + \cos^2\alpha = 1 \Rightarrow \cos^2\alpha = 1 - \sin^2\alpha$:
$$F_S = m g\left(\frac{\cos^2\alpha}{\sin\alpha} + \sin\alpha\right) = m g\left(\frac{1}{\sin\alpha} - \frac{\sin^2\alpha}{\sin\alpha} + \sin\alpha\right)$$
$$F_S = \frac{m g}{\sin\alpha}\ \checkmark$$

(grüner Kasten)
- ↳ $F_N$ ist positiv → Richtung richtig angetragen; $F_S$ ebenso
  - → sonst würde es sich in dem Ergebnis zeigen und ausrichten
- ↳ ~~Skizze~~ Ergebnis passt immer zur Skizze und gewähltem KOS

---

## Seite 19

### Übung (zentrales Kräftesystem)

**① Bolzen mit Einzelkräften**

> Skizze: Senkrechter Bolzen auf einer Platte eingespannt; am Bolzenkopf greifen vier rote Kräfte in der horizontalen Ebene an: $F_1$ (nach rechts, $30°$ unter der $x$-Achse), $F_2$, $F_3$ (nach links vorn), $F_4$ ($60°$-Winkel eingetragen). Lokales KOS $x$, $y$.

geg.: $F_1 = 1000\,\mathrm N$, $F_2 = 500\,\mathrm N$, $F_3 = 1500\,\mathrm N$, $F_4 = 800\,\mathrm N$ (Feld rechts daneben mit blauem Klebezettel abgedeckt)
ges.: $\vec F_R$, $\alpha_R$

**Lös.:**

> Skizze (Draufsicht): $x$-$y$-System; $F_1$ nach rechts unten ($30°$ unter $+x$), $F_2$ senkrecht nach unten ($-y$), $F_3$ nach links unten ($60°$ zur $-x$-Achse), $F_4$ nach links ($-x$). Resultierende $F_R$ steil nach links unten; Winkel $\alpha_R$ von $+x$ gemessen (großer Bogen). Nebenskizze: Zerlegung $F_{1x} = F_1\cos 30°$.

$$F_{Rx} = \sum F_{ix} = F_1\cos 30° - F_3\sin 30° - F_4 = -684\,\mathrm N$$
$$F_{Ry} = \sum F_{iy} = -F_1\sin 30° - F_2 - F_3\cos 30° = -2299\,\mathrm N$$
$$F_R = \sqrt{F_{Rx}^2 + F_{Ry}^2} = \underline{\underline{2398{,}6\,\mathrm N}}$$
$$\alpha_R = \arctan\frac{F_{Ry}}{F_{Rx}} = 73{,}4° + 180° = \underline{\underline{253°}}$$

[Prüfung: $866{,}0 - 750 - 800 = -684{,}0$; $-500 - 500 - 1299{,}0 = -2299{,}0$; $F_R = 2398{,}6\,\mathrm N$; $\alpha_R = 253{,}4°$ ✓ (3. Quadrant).]

---

## Seite 20

**② Seilkräfte / Stabkräfte**

> Skizze: Zwei Wände im Abstand $c$. Seil ① vom linken Wandpunkt zum Knoten $K$, Seil ② vom Knoten zum rechten Wandpunkt, der um $a$ höher liegt als der linke [?]. Am Knoten hängt die Masse $m$; $\vec g$ nach unten. Bemaßung (grün): $a$ (Höhenversatz der Aufhängepunkte), $b$ (horizontaler Abstand linke Wand – Knoten), $c$ (Wandabstand), $L$ (Länge Seil ①). Knoten mit Masse grün umrandet: Schnitt I.

geg.: $m = 30\,\mathrm{kg}$, $g = 9{,}81\,\mathrm{m/s^2}$, $a = 2\,\mathrm m$, $b = 4\,\mathrm m$, $c = 10\,\mathrm m$, $L = 4{,}5\,\mathrm m$
ges.: Seilkräfte $N_1$, $N_2$

**Lös.:** (I) Freischnitt des Knotens

> Skizze: Knoten im $x$-$y$-System; $N_1$ entlang Seil ① nach links oben (Winkel $\beta$ zur Horizontalen), $N_2$ entlang Seil ② nach rechts oben (Winkel $\alpha$), $F_G = m\cdot g$ nach unten.

Nebenrechnungen (grün):
- Dreieck für $\alpha$ mit Katheten $a + d$ (vertikal) und $c - b$ (horizontal): $\tan\alpha = \dfrac{a+d}{c-b}$, $\alpha = \arctan\dfrac{a+d}{c-b}$
- Dreieck für $\beta$ mit Hypotenuse $L$, Ankathete $b$, Gegenkathete $d$: $\cos\beta = \dfrac bL$, $\beta = \arccos\dfrac bL$, $d = L\sin\beta = L\sin(\arccos\tfrac bL)$

↳ Gleichgewicht!
$$\sum F_x = 0:\quad -N_1\cos\beta + N_2\cos\alpha = 0\quad (1)$$
$$\sum F_y = 0:\quad -F_G + N_1\sin\beta + N_2\sin\alpha = 0\quad (2)$$

aus (1): $N_2 = N_1\,\dfrac{\cos\beta}{\cos\alpha}$; ↳ in (2):
$$F_G = N_1\left(\sin\beta + \sin\alpha\,\frac{\cos\beta}{\cos\alpha}\right)\quad\Big|\ :\cos\beta$$
$$\frac{F_G}{\cos\beta} = F_G\,\frac{L}{b} = N_1\left(\tan\beta + \tan\alpha\right),\qquad \tan\alpha = \frac{a+d}{c-b}$$
$$N_1 = \frac{L\cdot m g}{b\,(\tan\beta + \tan\alpha)} \;\to\; N_2 = \frac{L\,m g}{b}\,\frac{1}{\tan\beta + \tan\alpha}\,\frac{\cos\beta}{\cos\alpha} = m g\left[\left(\frac{\tan\beta}{\cos\alpha} + \frac{\tan\alpha}{\cos\alpha}\right)\cos\beta\right]^{-1}\ [?]$$

(Die letzte Umformung ist am Seitenrand abgeschnitten.)

---

## Seite 21

$$N_1 = m g\,\frac Lb\,\frac{1}{\tan(\arccos\frac bL) + \dfrac{a + L\sin(\arccos\frac bL)}{c-b}} \quad \left(= \frac{m g\,L/b}{\tan\alpha + \tan\beta}\right)$$
$$\underline{N_1 = 277{,}7\,\mathrm N}$$

$$N_2 = m g\Big/\left(\cos\alpha\,(\tan\alpha + \tan\beta)\right)\cdot\ldots\ [?]$$
(mehrere durchgestrichene Zwischenausdrücke mit $\cos(\arctan\frac{a+d}{c-b})$, Zwischenwerte ~~0,622~~, ~~0,960~~ [?])

$$\underline{N_2 = 298{,}1\,\mathrm N}\quad(\text{korrigiert aus } \sout{348{,}03\,\mathrm N})$$

$\beta = 27{,}266°$, $\alpha = 34{,}1°$

[Prüfung: $\beta = \arccos(4/4{,}5) = 27{,}27°$, $d = 2{,}062\,\mathrm m$, $\alpha = \arctan(4{,}062/6) = 34{,}10°$; $N_1 = 294{,}3\,\mathrm N/(0{,}8889\cdot(0{,}5154 + 0{,}6770)) = 277{,}7\,\mathrm N$ ✓; $N_2 = N_1\cos\beta/\cos\alpha = 298{,}1\,\mathrm N$ ✓. Der zunächst notierte Wert 348,03 N war falsch und wurde im Original korrigiert. Die Lösung setzt voraus, dass der rechte Aufhängepunkt um $a$ **höher** liegt als der linke.]

**Nachtrag:** Kräfte an Wänden in $x$-Richtung

> Skizze: Wandpunkt mit schrägem Seil, Fragezeichen an der horizontalen Wandkraft.

$$N_1\cdot\cos\beta = N_2\cos\alpha \;\Rightarrow\; \underline{\pm 246{,}8\,\mathrm N}$$

[Prüfung: $277{,}7\cdot\cos 27{,}27° = 246{,}8\,\mathrm N$ ✓.]

---

## Seite 22

#### 2.2 Das allgemeine ebene Kräftesystem

- Wirkungslinien treffen sich nicht in einem Punkt!

> Skizze: Rechteckiger Körper; $F_1$ horizontal an der linken unteren Ecke (nach rechts), $F_2$ schräg an der linken Seite (Winkel $\alpha$), $F_3$ schräg nach rechts oben an der Oberseite (Winkel $\beta$), $F_4$ senkrecht nach unten an der rechten oberen Ecke. KOS $x$ nach rechts, $y$ nach oben (grün).

##### 2.2.1 Äquivalenz

- wie bei Kräften → zwei Kräftesysteme mit gleicher Kraftwirkung ($F_{R1} = F_{R2}$)
- zusätzlich Berücksichtigung von Momenten → zwei Kräftesysteme mit gleicher Drehwirkung bezüglich eines beliebigen Punktes
  (Intensität und Drehrichtung sind abhängig vom Punkt!)

↳

> Skizze: Rechteck mit schräger Kraft $F$ an der linken oberen Ecke (Wirkungslinie gestrichelt) = Rechteck, bei dem $F$ parallel an einen anderen Punkt verschoben ist (neue Wirkungslinie gestrichelt) und zusätzlich ein Moment $M = F\cdot a$ (Drehpfeil) wirkt; $a$ = senkrechter Abstand der beiden Wirkungslinien (grün).

- Parallelverschiebung der Wirkungslinie möglich, wenn dies durch ein zusätzliches Moment kompensiert wird (**Versatzmoment**)

---

## Seite 23

> Skizze: Räumliches KOS $x, y, z$; drei Kräfte $\vec F_1, \vec F_2, \vec F_3$ (rot) mit grünen Ortsvektoren $\vec r_1, \vec r_2, \vec r_3$ vom Ursprung zu ihren Angriffspunkten. ⇒ äquivalentes System im Ursprung: resultierende Kraft $\vec F_R$ und resultierendes Moment $\vec M_R$ (Doppelpfeil).

bekannt:
$$\vec F_R = \vec F_1 + \vec F_2 + \ldots = \sum_{i=1}^n \vec F_i$$
$$\boxed{F_{Rx} = \sum_{i=1}^n F_{ix},\quad F_{Ry} = \sum_{i=1}^n F_{iy},\quad F_{Rz} = \sum_{i=1}^n F_{iz}}$$

für Momente:
$$\vec M_R = \sum_{i=1}^n \vec M_i \qquad\text{(Vektor → kann addiert werden)}$$

$$\vec M = \vec r\times\vec F,\qquad \vec r = x\,\vec e_x + y\,\vec e_y + z\,\vec e_z,\qquad \vec F = F_x\,\vec e_x + F_y\,\vec e_y + F_z\,\vec e_z$$

↳ s. Tafelwerk
$$\vec M = \vec e_x\underbrace{(yF_z - zF_y)}_{M_x} + \vec e_y\underbrace{(zF_x - xF_z)}_{M_y} + \vec e_z\underbrace{(xF_y - yF_x)}_{M_z}$$

---

## Seite 24

↳ analog zu Kräften
$$\boxed{\begin{aligned}
M_{Rx} &= \sum_{i=1}^n M_{ix} = \sum_{i=1}^n (y_i F_{iz} - z_i F_{iy})\\
M_{Ry} &= \sum_{i=1}^n M_{iy} = \sum_{i=1}^n (z_i F_{ix} - x_i F_{iz})\\
M_{Rz} &= \sum_{i=1}^n M_{iz} = \sum_{i=1}^n (x_i F_{iy} - y_i F_{ix})
\end{aligned}}$$

> Skizze „Bsp. $M_{Rz}$" (Randskizze): Bezugspunkt $0$; Kraftkomponente $F_{iy}$ (vertikal) mit Hebelarm $x_i$, Kraftkomponente $F_{ix}$ (horizontal) mit Hebelarm $y_i$.

- im ebenen Fall
$$[\vec F] = \begin{bmatrix}F_x\\F_y\\0\end{bmatrix},\qquad [\vec r] = \begin{bmatrix}x\\y\\0\end{bmatrix}$$

> Skizze: $x$-$y$-Ebene; Angriffspunkt $(x, y)$ mit grünem Ortsvektor $\vec r$; rote Kraft $\vec F$ mit Komponenten $F_x$, $F_y$. Im Ursprung das Moment $\vec M$ als Drehpfeil (Kreis) – „Darstellung in Ebene".

$$[\vec M] = \begin{bmatrix}M_x\\M_y\\M_z\end{bmatrix} = \begin{bmatrix}yF_z - zF_y\\ zF_x - xF_z\\ xF_y - yF_x\end{bmatrix} = \begin{bmatrix}0\\0\\xF_y - yF_x\end{bmatrix}$$

$$\boxed{[\vec M] = M_z = xF_y - yF_x}\qquad (x\text{-}y\text{-Ebene})$$

---

## Seite 25

- Belastung durch $\vec F_R$ und $\vec M_R$ kann auch allein durch Kraft $\vec F_R$ dargestellt werden
  - → Wirkungslinie muss verschoben werden

> Skizze: Links: $x$-$y$-System, im Ursprung $\vec F_R$ (nach rechts oben) und Moment $\vec M_R$ (Drehpfeil). ⇒ Rechts: nur $\vec F_R$ auf einer parallel verschobenen Wirkungslinie (gestrichelt), die die $x$-Achse unter dem Winkel $\alpha$ schneidet.

↳ **Berechnung der verschobenen Wirkungslinie**
- es muss gelten:
$$\boxed{\underset{\text{bekannt}}{\vec M_R} = \underset{\text{unbekannt}}{\vec r_R} \times \underset{\text{bekannt}}{\vec F_R}}$$

2D:
$$\boxed{M_{Rz} = x_R F_{Ry} - y_R F_{Rx}}$$

↳ Geradengleichung der Wirkungslinie von $\vec F_R$ (vgl. $y = m\cdot x + n$):
$$y_R = x_R\underbrace{\frac{F_{Ry}}{F_{Rx}}}_{m} - \underbrace{\frac{M_{Rz}}{F_{Rx}}}_{n}$$

---

## Seite 26

**Bsp.:** Resultierende eines allgemeinen ebenen Kräftesystems

> Skizze: Rechteckige Scheibe; KOS (grün) mit Ursprung $0$ in der linken unteren Ecke [?]. $F_1$ horizontal nach rechts an einem Punkt links oben, $F_2$ senkrecht nach unten am gleichen Punkt, $F_4$ senkrecht nach unten und $F_3$ horizontal nach rechts an einem Punkt rechts.
> Darunter die bemaßte Ersatzskizze: $x$ nach rechts, $y$ nach oben; Angriffspunkt von $F_1$ und $F_2$ bei $(0,\,2c)$ (Ortsvektoren $\vec r_1 = \vec r_2$), Angriffspunkt von $F_4$ bei $(6c,\,0)$ (Ortsvektor $\vec r_4$), Angriffspunkt von $F_3$ bei $(6c,\,-c)$ (Ortsvektor $\vec r_3$). Teilung der $x$-Achse $c, 3c, 6c$; $y$-Achse $-c, c, 2c$. Gestrichelt die gesuchte Wirkungslinie „WL von $F_R$", fallend von links oben nach rechts unten.

geg.: $F_1 = F_4 = F$, $F_2 = 2F$, $F_3 = 3F$
ges.: Resultierende $F_R$ und Wirkungslinie von $F_R$

**Lös.:**
$$F_{Rx} = \sum_i F_{ix} = F_1 + F_3 = F + 3F = \underline{\underline{4F}}$$
$$F_{Ry} = \sum_i F_{iy} = -F_2 - F_4 = -2F - F = \underline{\underline{-3F}}$$
$$F_R = \sqrt{F_{Rx}^2 + F_{Ry}^2} = \sqrt{16F^2 + 9F^2} = \underline{\underline{5F}}$$
(die „9" ist im Original wie eine 8 geschrieben [?]; das Ergebnis $5F$ ist korrekt)

$$\alpha_R = \arctan\frac{F_{Ry}}{F_{Rx}} = \arctan\left(-\frac34\right) = -36{,}9° \;+180° = \underline{143{,}1°}$$

[Prüfung: **Fehler im Original.** Mit $F_{Rx} = +4F > 0$ und $F_{Ry} = -3F < 0$ liegt $\vec F_R$ im **4. Quadranten** (vgl. Quadrantenregel S. 15): keine Korrektur um $+180°$, also $\alpha_R = -36{,}9°$ (bzw. $323{,}1°$). $143{,}1°$ ist die Richtung des entgegengesetzten Vektors $(-4F,\,3F)$; die Wirkungslinie selbst (Gerade) ist davon unberührt.]

$$M_{Rz}\big|_0 = \sum_{i=1}^n M_{iz} = \sum_{i=1}^n (x_i F_{iy} - y_i F_{ix})$$

$$\vec F_1 = \begin{pmatrix}F\\0\end{pmatrix},\ \vec F_2 = \begin{pmatrix}0\\-2F\end{pmatrix},\ \vec F_3 = \begin{pmatrix}3F\\0\end{pmatrix},\ \vec F_4 = \begin{pmatrix}0\\-F\end{pmatrix};\qquad \vec r_1 = \begin{pmatrix}0\\2c\end{pmatrix} = \vec r_2,\ \vec r_3 = \begin{pmatrix}6c\\-c\end{pmatrix},\ \vec r_4 = \begin{pmatrix}6c\\0\end{pmatrix}$$

$$M_{Rz}\big|_0 = (x_1F_{1y} - y_1F_{1x}) + (x_2F_{2y} - y_2F_{2x}) + (x_3F_{3y} - y_3F_{3x}) + (x_4F_{4y} - y_4F_{4x})$$
$$= (0 - 2cF) + (0 - 0) + (6c\cdot 0 - (-c)\,3F) + (-6cF - 0) = -2cF + 3cF - 6cF = \underline{\underline{-5cF}}$$

[Prüfung: ✓]

---

## Seite 27

↳ Geradengleichung
$$y_R = x_R\left(\frac{F_{Ry}}{F_{Rx}}\right) - \left(\frac{M_{Rz}}{F_{Rx}}\right) = x_R\left(-\frac{3F}{4F}\right) - \frac{-5cF}{4F}$$
$$\boxed{y_R = -\frac34\,x_R + \frac54\,c}$$

↳ einzeichnen

> Randskizze (rot): „$M_{Rz}$ + $F_R$ →": im Ursprung $F_R$ nach rechts unten mit Moment $M_{Rz}$ (Drehpfeil im Uhrzeigersinn, negativ) ⇒ nur $F_R$ nach rechts unten auf einer nach oben/rechts verschobenen Wirkungslinie (Fragezeichen am Schnittwinkel).

**Kontrolle $\alpha_R$:** → muss durch WL abgebildet werden

> Skizze: Gerade schneidet die $y$-Achse bei $\tfrac54 c$ und die $x$-Achse bei $x_{R0}$; Winkel $\beta$ zwischen Gerade und $y$-Achse; Pfeil der Kraft eingezeichnet nach rechts oben [?].

$$x_{R0} = \frac{5/4}{3/4}\,c = \underline{\frac53\,c}$$
$$\tan\beta = \frac{\frac53 c}{\frac54 c} = \frac43,\qquad \beta = 53{,}1°\ +90° = 143{,}1°\ \checkmark = \underline{\underline{\alpha_R}}$$

[Prüfung: $x_{R0}$ und $\beta$ korrekt. Die Kontrolle bestätigt aber nur den Winkel der **Geraden**; der Richtungssinn von $\vec F_R$ (nach rechts unten, $F_{Rx}>0$, $F_{Ry}<0$) ergibt $\alpha_R = 143{,}1° - 180° = -36{,}9°$. Die Wirkungslinie $y_R = -\tfrac34 x_R + \tfrac54 c$ ist richtig; Probe: $M_{Rz} = x F_{Ry} - y F_{Rx}$ im Punkt $(0,\,\tfrac54 c)$: $-\tfrac54 c\cdot 4F = -5cF$ ✓.]

---

## Seite 28

##### 2.2.2 Gleichgewicht im allgemeinen ebenen Kräftesystem

- wie beim zentralen Kräftesystem herrscht Gleichgewicht, wenn gilt
$$\boxed{\vec F_R = \vec 0}$$
- im allgemeinen Kräftesystem muss ebenfalls gelten
$$\boxed{\vec M_R = \vec 0}$$

↳
$$\boxed{F_{Rx} = \sum_{i=1}^n F_{ix} \overset{!}{=} 0,\quad F_{Ry} = \sum_{i=1}^n F_{iy} \overset{!}{=} 0,\quad F_{Rz} = \sum_{i=1}^n F_{iz} \overset{!}{=} 0}$$
$$\boxed{M_{Rx} = \sum_{i=1}^n M_{ix} = \sum (y_iF_{iz} - z_iF_{iy}) \overset{!}{=} 0,\quad M_{Ry} = \sum (z_iF_{ix} - x_iF_{iz}) \overset{!}{=} 0,\quad M_{Rz} = \sum (x_iF_{iy} - y_iF_{ix}) \overset{!}{=} 0}$$

↳ **6** Gleichgewichtsbedingungen im allgemeinen Kräftesystem

↳ ebenes allg. Kräftesystem:
$$\boxed{F_{Rx} = \sum F_{ix} \overset{!}{=} 0,\qquad F_{Ry} = \sum F_{iy} \overset{!}{=} 0,\qquad M_{Rz} = \sum M_{iz} \overset{!}{=} 0}$$
→ **3** Glg. im ebenen allgemeinen Kräftesystem!

---

## Seite 29

**Beachte:**
- $x$- und $y$-Richtung in den Kraft-Gleichgewichtsbedingungen müssen nicht senkrecht zueinander sein und beliebige Richtungen sein
- Bezugspunkt für Momentengleichgewicht kann beliebig in der Ebene festgelegt sein
- **3 Glg. → nur 3 Unbekannte möglich!**
- positiver Richtungssinn der Kräfte und Drehsinn der Momente kann beliebig gewählt werden
- in Kräftegleichgewicht gehen alle Einzelkräfte ein
  - → verteilte Belastungen (Volumen, Fläche, Linie) müssen vorher auf resultierende äquivalente Kraft reduziert werden

---

## Seite 30

##### 2.2.3 Lager und Lagerreaktionen in der Ebene

- jeder Körper in der Ebene hat 3 Freiheitsgrade: 2× translatorisch, 1× rotatorisch

> Skizze: Achsenkreuz mit zwei Verschiebungspfeilen ($x$, $y$) und einem Drehpfeil.

⇒ Behinderung durch Lager(bedingungen)

**Bsp.:**

> Skizze 1 „Brücke": Bogenbrücke, links Festlager, rechts Loslager (Rollen); grüner Verschiebungspfeil am Loslager horizontal (möglich), vertikal durchgestrichen (verhindert).
> Skizze 2: Balken mit T-förmiger Stütze (Auflager auf Stütze), Verschiebung in einer Richtung durchgestrichen.
> Skizze 3: Balken in Wand eingespannt; alle Bewegungen (horizontal, vertikal, Drehung) grün durchgestrichen.

**① Loslager**

> Skizze: Balkenende auf Loslager (Dreieck auf Rollen/Schraffur), KOS $x$, $y$. Verschiebung in $y$-Richtung verhindert (grüner Doppelpfeil), Verschiebung in $x$-Richtung möglich („mögl."). ⇒ nach Schnitt: Balkenende mit roter Lagerkraft $F_A$ senkrecht nach oben.

**② Festlager**

> Skizze: Balkenende auf Festlager (Dreieck auf Schraffur). Verschiebung in $x$- und $y$-Richtung verhindert. ⇒ nach Schnitt: $F_H$ (horizontal →) und $F_V$ (vertikal ↑).

**③ Einspannung**

> Skizze: Balken in Wand eingespannt. Verschiebung/Rotation in $x$-$y$-Richtung verhindert (Doppelpfeile und Drehpfeil). ⇒ nach Schnitt: $F_H$ (→), $F_V$ (↑) und Einspannmoment $M$ (Drehpfeil).

---

## Seite 31

**④ Gelenk**

> Skizze: Zwei Stäbe, durch ein Gelenk (Kreis) verbunden. Verschiebung in $x$- und $y$-Richtung verhindert (Drehung frei). ⇒ freigeschnittener Stab mit $F_V$ (↑) und $F_H$ (→) am Gelenk.

**⑤ Hülse**

> Skizze: Stab in einer Hülse (Führung zwischen zwei schraffierten Wänden). Verhindert: Drehung und Verschiebung in $y$-Richtung (Verschiebung in $x$-Richtung frei). ⇒ freigeschnittener Stab mit $F_V$ (↑) und Moment $M$.

**Bsp.:**

> Skizze: Balken, links überkragend, mit schräger Kraft $F$ am linken Ende (nach rechts unten). Lager $A$ = Loslager (etwas rechts vom linken Ende), Lager $B$ = Festlager am rechten Ende. Grün umrandet (Freischnitt).
> Darunter das Freikörperbild: $F$ am linken Ende, $F_A$ (↑) an $A$, $F_{BH}$ (← horizontal) und $F_{BV}$ (↑) an $B$.

(⇒ Richtung der Lagerreaktionen häufig nicht vorhersehbar und daher willkürlich festgelegt!)

---

## Seite 32

- **Pendelstütze**
  - → wie Stab: nur Zug- und Druckkräfte

Randnotiz: später bei Beispielen zu Schnittgrößen im Tabellen [?]?

> Skizze: Balken, links Festlager, rechts über eine schräge Pendelstütze (Stab mit Gelenken an beiden Enden) an ein Festlager angeschlossen. Darunter freigeschnitten: links $F_{AH}$ (→), $F_{AV}$ (↑); rechts Pendelstützenkraft $F_P$ in Stabrichtung.

- → nicht unbestimmt, obwohl 2 Festlager
  (→ $F_{BH}$, $F_{BV}$ über Pendelstütze in Abhängigkeit)

---

## Seite 33

##### 2.2.4 Statisch bestimmte Lagerung und Abzählkriterium

- ein Körper ist statisch bestimmt gelagert, wenn alle Lagerreaktionen allein aus den Gleichgewichtsbedingungen berechnet werden können

> Skizze: Kragbalken der Länge $L$, links in der Wand eingespannt ($A$), am freien rechten Ende Kraft $F$ senkrecht nach unten; grün umrandet. Freigeschnitten: an $A$ die Reaktionen $F_H$ (←), $F_V$ (↓ eingezeichnet) und Einspannmoment $M$ (Drehpfeil); Bemaßung $L$ (grün).

$$\sum F_{ix} \overset{!}{=} 0 \;\to\; \underline{F_H = 0}$$
$$\sum F_{iy} \overset{!}{=} 0 \;\to\; F_V + F = 0,\quad \underline{F_V = -F}$$
$$\sum M_{iz} \overset{!}{=} 0 \;\to\; \big|_A\ M + F\cdot L = 0,\quad \underline{M = -F\cdot L}$$

(Vorzeichen: $F_V$ und $F$ beide nach unten positiv angesetzt; $F_V = -F$ heißt, $F_V$ wirkt tatsächlich nach oben. Der Momenten-Drehsinn ist so gewählt, dass $F$ positiv beiträgt.)

- **Abzählkriterium**

> Skizze: Dreigelenkrahmen aus zwei Teilen (I links, II rechts), oben durch ein Gelenk verbunden, unten je ein Festlager. Auf Teil I wirkt $F_2$ schräg, auf Teil II wirkt $F_1$ schräg. Beide Teile grün umrandet (Schnitte I, II).

- → jeder Schnitt stellt 3 Glg. aus der Forderung nach Gleichgewicht zur Verfügung

$n$: Anzahl der Schnitte (Teilkörper)
$a$: Anzahl der Auflagerreaktionen
$z$: Anzahl der Zwischenreaktionen

$$\boxed{\underbrace{3\cdot n}_{\text{Anzahl Glg.}} = \underbrace{a + z}_{\text{Anzahl der Unbekannten}}}\;\to\;\text{statisch bestimmt}$$

$$3n < a + z \;\to\; \text{statisch unbestimmt (n. l. in der Stereostatik [nicht lösbar])}$$
$$3n > a + z \;\to\; \text{statisch unterbestimmt (verschieblich → Dynamik!)}$$

---

## Seite 34

**ACHTUNG:** Abzählkriterium ist notwendige, aber keine hinreichende Bedingung für statische Bestimmtheit

> Skizze: Starrer (schraffierter) Körper auf drei Loslagern (alle vertikal): $3 = 3$ ↳ aber verschieblich! (horizontal) ↳ statisch unbestimmt [im Sinne von: nicht brauchbar gelagert]

- Vorteile bestimmter Lagerung in technischer Praxis:
  - → Lösbarkeit mit Statik (einfach)
  - → Fertigungsungenauigkeiten führen weder zu Spannungen noch veränderten Tragverhalten

> Skizze: „bestimmt": Balken auf Fest- und Loslager; bei Längenänderung (gestrichelt, verlängert) bleibt der Balken zwanglos gelagert. „unbestimmt": Balken auf Loslager – Festlager – Loslager [?] bzw. Fest- und zwei weiteren Lagern; Verformung (gestrichelt) wird behindert.

  - → thermische Dehnungen können sich frei ausbilden und führen nicht zu inneren Spannungen im Bauteil

---

## Seite 35

**Bsp.: ①** Einfeldträger mit Kragarm

> Skizze: Balken; links in $A$ Festlager, in $B$ Loslager im Abstand $L$ von $A$; Kragarm der Länge $b$ rechts über $B$ hinaus. $F_1$ senkrecht nach unten im Abstand $a$ von $A$, $F_2$ senkrecht nach unten am Kragarmende. KOS $x$ nach rechts (grün). Bemaßung: $a$, $L$, $b$.

geg.: $F_1 = F$, $F_2 = 2F$, $b = L/10$, $a = L/2$
ges.: Lagerreaktionen

**Lös.:**

> Skizze (Freikörperbild): $F$ bei $L/2$ (↓), $2F$ am Ende (↓), $F_{AH}$ (→) und $F_{AV}$ (↑) in $A$, $F_B$ (↑) in $B$; Bemaßung $L/2$, $L$, $L/10$.

$(3\cdot 1 = 3 + 0,\ 3 = 3\ \checkmark)$

$$\sum F_x \overset{!}{=} 0:\quad \underline{F_{AH} = 0}\quad (1)$$
$$\sum F_y \overset{!}{=} 0:\quad F_{AV} - F + F_B - 2F = 0\quad (2)$$
$$\sum M\big|_A \overset{!}{=} 0:\quad F\cdot\frac L2 - F_B\cdot L + 2F\,L\left(1 + \frac{1}{10}\right) = 0\quad (3)$$

aus (3):
$$F_B\cdot L = F\cdot\frac L2 + 2F\,L\left(1 + \frac1{10}\right)\;\Rightarrow\; F_B = F\left(\frac12 + 2 + \frac15\right) = \left(2 + \frac{7}{10}\right)F = \underline{\underline{2{,}7\,F}}$$

in (2):
$$F_{AV} - F + 2{,}7F - 2F = 0 \;\Rightarrow\; \underline{\underline{F_{AV} = 0{,}3\,F}}\quad(\text{korrigiert aus } \sout{1{,}7\,F})$$

(Im Original ist die Zeile als „$F_{AV} = F + 2{,}7F + 2F = 0$" [?] notiert – Vorzeichen in der Umstellung unsauber, Endergebnis korrekt.)

- Lager $B$ trägt mehr in $y$-Richtung
- keine horizontale Kraft

[Prüfung: $F_B = 2{,}7F$, $F_{AV} = 0{,}3F$ ✓; Kontrolle Momente um $B$: $F_{AV}L - F\cdot L/2 + 2F\cdot L/10 = 0{,}3 - 0{,}5 + 0{,}2 = 0$ ✓.]

---

## Seite 36

**②** Kragbalken (eingespannt)

> Skizze: Balken links in $A$ eingespannt, KOS $x$ nach rechts. $F_1$ (↓) im Abstand $a$ von $A$, $F_2$ (↓) am Ende bei $L$. Ein Loslager $B$ unter dem Ende ist durchgestrichen (entfällt), ebenso die Angabe ~~$b = L/10$~~. Grün umrandet.

geg.: $F_1 = F$, $F_2 = 2F$, ~~$b = L/10$~~, $a = L/2$
ges.: Lagerreaktionen

**Lös.:** nach Schnitt

> Skizze: Freigeschnittener Balken: $F_{AH}$ (→), $F_{AV}$ (↓), Einspannmoment $M_A$ (Drehpfeil) in $A$; $F_1$, $F_2$ (↓); Lagerkraft $F_B$ durchgestrichen.

$(3\cdot 1 = 3 + 0,\ 3 = 3\ \checkmark)$

$$\checkmark\ \sum F_x = 0 \;\leadsto\; \underline{F_{AH} = 0}$$
$$\checkmark\ \sum F_y = 0 \;\leadsto\; -F_{AV} - F_1 - F_2 = 0 \;\to\; F_{AV} = -(F_1 + F_2) = \underline{-3F}$$
$$\sum M\big|_A = 0 \;\leadsto\; M_A + F_1\cdot\frac L2 + F_2\cdot L = 0$$
$$M_A = -F_1\frac L2 - F_2 L = -\frac{FL}{2} - 2FL,\qquad \checkmark\ \underline{M_A = -2{,}5\,F\cdot L}$$

[Prüfung: ✓. Hinweis: $F_{AV}$ ist nach unten angetragen, das negative Ergebnis bedeutet $3F$ nach oben. Im Original steht in der $F_y$-Gleichung zunächst „$+F_1$" bzw. bei $M_A$ „$+F_2L$" (unsauber korrigiert), die Ergebniszeilen sind richtig.]

---

## Seite 37

##### Äquivalenzbetrachtungen von Streckenlasten (grün eingerahmte Überschrift)

- bisher: Kräfte und Momente beschreiben das Kräftesystem
- **Aber:** reale Lastverteilungen müssen durch Einzelkräfte und Momente repräsentiert werden, um die erlernten Methoden nutzen zu können

**Streckenlast**

> Skizze: Balken entlang der $x$-Achse (KOS: $y$ aus der Ebene heraus ⊙, $z$ nach unten). Zwischen $x = a$ und $x = b$ wirkt eine rote verteilte Last $q(x)$ (Lastkurve, Pfeile nach unten). Ein Streifen der Breite $\mathrm dx$ ist schraffiert: $\mathrm dF(x) = q(x)\,\mathrm dx$.

$q(x)$ … Intensität der Streckenlast, $\quad [q(x)] = \dfrac{\text{Kraft}}{\text{Länge}}$

- → Streckenlasten können auf eine resultierende Einzelkraft zurückgeführt werden
  - Dabei muss die resultierende Einzelkraft in ihrer Kraft- und Momentenwirkung der Streckenlast äquivalent sein!

> Skizze: Balken mit Streckenlast (schraffiert) ⇒ derselbe Balken mit einer Einzelkraft $F_R$ (↓) im Abstand $x_R$ vom Ursprung (grüne Bemaßung).

---

## Seite 38

- zur Streckenlast äquivalente Einzelkraft:
$$\boxed{F_R = \int \mathrm dF(x) = \int_{x=a}^{b} q(x)\,\mathrm dx}$$

Randnotiz: Integrationskonstante? (fliegen raus, bestimmtes Integral!)

- zur Streckenlast äquivalentes Moment:
$$\boxed{M_R = \int \mathrm dM = \int \mathrm dF\,x = \int_{x=a}^{b} q(x)\cdot x\,\mathrm dx}$$

↳ Forderung, dass $M_R = F_R\cdot \boxed{x_R}$:
$$\boxed{x_R = \frac{\displaystyle\int_a^b q(x)\,x\,\mathrm dx}{\displaystyle\int_a^b q(x)\,\mathrm dx}}$$

**Beispiele:**
- konstante Last (Rechteckslast)

> Skizze: Balken der Länge $L$ mit konstanter Streckenlast $q(x) = q = \text{const.}$ (rot), $x$ ab linkem Ende. ⇒ Balken mit Einzelkraft $F_R = q\cdot L$ in der Mitte (Bemaßung $L/2$, $L/2$).

$$F_R = \int_0^L q(x)\,\mathrm dx = q\int_0^L \mathrm dx = q\,(L - 0) = q\cdot L$$
$$M_R = \int_0^L q(x)\,x\,\mathrm dx = q\int_0^L x\,\mathrm dx = q\left(\frac{L^2}{2} - 0\right) = q\,\frac{L^2}{2}$$

---

## Seite 39

$$x_R = \frac{M_R}{F_R} = \frac{q L^2}{2\,q L} = \frac L2$$

- Dreieckslast

> Skizze: Balken der Länge $L$, linear von $0$ (links) auf $q_0$ (rechts) ansteigende Last (rot); $x$ nach rechts, $z$ nach unten.

$$q(x) = +\frac{q_0}{L}\,x$$
$$F_R = \int_0^L q(x)\,\mathrm dx = +\frac{q_0}{L}\int_0^L x\,\mathrm dx = +\frac{q_0}{L}\left(\frac{L^2}{2} - 0\right),\qquad \underline{F_R = +\frac{q_0 L}{2}}$$
$$M_R = \int_0^L q(x)\,x\,\mathrm dx = \frac{q_0}{L}\int_0^L x^2\,\mathrm dx = \frac{q_0}{L}\left(\frac{L^3}{3} - 0\right) = \underline{\frac{q_0 L^2}{3}}$$
$$\underline{x_R = \frac{M_R}{F_R} = \frac{q_0 L^2\cdot 2}{3\,q_0 L} = \frac23 L}$$

> Skizze: Balken mit Einzelkraft $F_R = \tfrac12 q_0 L$ bei $\tfrac23 L$ vom linken Ende (Bemaßung $\tfrac23 L$, $\tfrac13 L$).

[Prüfung: ✓]

---

## Seite 40

Gelber Klebezettel: *Ergänzung Linienlasten*

**Bsp.: Innendruck auf Halbkreisbogen**

> Skizze: Halbkreisbogen (Durchmesser $2r$), auf den von innen ein konstanter Druck $p$ radial nach außen wirkt (rote Pfeile). Detail: Wandelement mit Druck $p$ unter Winkel $\alpha$, zerlegt in $p_x$ (horizontal) und $p_y$ (vertikal). $\alpha = 0 \ldots \pi$.

$$p_y = \sin\alpha\;p,\qquad p_x = \cos\alpha\;p$$

> Skizze: Diagramm $p_y$ über der Bogenlänge $x$ von $0$ bis $\pi r$ (statt $2r$, korrigiert): sinusförmige Verteilung mit Maximum $p$ in der Mitte. „Entlang des Umfanges (nur Halbkreis: $0 - \pi r$)".

(Mehrere durchgestrichene Ansätze: $\alpha = \frac{x}{2r}\pi$, $x = r - r\cos\alpha$, $\arccos\frac{x-r}{r} = \alpha$.)

Koordinate (Nebenskizze: Halbkreis, Bogenlänge $x$ zum Winkel $\alpha$, Radius $r$):
$$x = \alpha\cdot r,\qquad \alpha = \frac xr$$

$$F_R = \int_L q(x)\,\mathrm dx = \int_0^{\pi r} p\sin\left(\frac xr\right)\mathrm dx,\qquad F_R = p\left[-r\cos\left(\frac xr\right)\right]_0^{\pi r}$$
$$\boxed{F_{Ry} = 2pr}\quad\to\text{ entspricht Druck auf Projektionslinie } |2r|!$$
$$F_{Rx} = \int_L q_x(x)\,\mathrm dx = \int_0^{\pi r} p\cos\left(\frac xr\right)\mathrm dx = p\left[r\sin\left(\frac xr\right)\right]_0^{\pi r} = \underline{0}\ \text{(Glgw.!)}$$

[Prüfung: $p[-r\cos\pi + r\cos 0] = 2pr$ ✓; $F_{Rx} = 0$ ✓ (Symmetrie).]

---

## Seite 41

↳ $F_{R,x}$ (nur über eine Hälfte des Bogens)

> Skizze: Halbkreisbogen mit horizontalen Druckkomponenten: links nach links, rechts nach rechts (rote Pfeile) – heben sich gegenseitig auf.

> Skizze: Diagramm $q_x$ über $x$ von $0$ bis $\pi r$: positive Fläche in der ersten Hälfte, negative in der zweiten (beide schraffiert, gegengleich) → wird $0$.

[Prüfung: Der Verlauf $q_x = p\cos(x/r)$ ist eine Kosinuskurve mit Endwerten $+p$ und $-p$; die Skizze im Original zeichnet die Kurve an den Rändern stark überhöht (fast singulär) – nur qualitativ gemeint.]

$$\boxed{F_{R,x}\Big|_0^{\frac{\pi}{2}r} = p\left[r\sin\left(\frac xr\right)\right]_0^{\frac\pi2 r} = \underline{p\,r}}\quad\to\text{ entspricht Druck × Projektionslinie}$$

> Skizze: Viertelkreis mit horizontalen Druckpfeilen → $F_{R,x}\big|_0^{\frac\pi2 r}$ (Projektion auf die senkrechte Linie der Länge $r$).

---

## Seite 42

**Bsp.: Kfz mit Anhänger**

> Skizze: Pkw mit angekuppeltem einachsigem Anhänger.

geg.: Auto mit 1,5 t Gewicht (+ Fahrer (100 kg)) + Anhänger mit (250 kg [?], überschrieben aus 260 [?]) verteilt mit 1250 N/m; • angezogene Handbremse
ges.: Lasten auf Achsen

> Skizze (Modell): Balken „Kfz" (Länge $L_K$) und Balken „Anhänger" (Länge $L_A$), verbunden durch ein Gelenk $G$ (Anhängerkupplung) am rechten Ende des Kfz. Kfz: Achse $A$ (Lager, Abstand $L_K/5$ vom linken Ende [?]), Achse $B$ (Lager bei $\tfrac45 L_K$), Gewichtskraft $F_K$ (↓) bei $\tfrac25 L_K$ vom linken Ende. Anhänger: konstante Streckenlast $q_0 = \dfrac{2500}{L_A} = 1250\,\mathrm{N/m}$ über die ganze Länge, Achse $C$ (Loslager) bei $L_A/2$. KOS $x$ nach rechts, $y$ nach oben.

**Lös.:**

> Skizze: Schnitte I (Kfz) und II (Anhänger), grün umrandet, getrennt am Gelenk.
> Freikörperbild I: $F_K$ (↓), $F_A$ (↑) an $A$, $F_{BV}$ (↑) und $F_{BH}$ (←) an $B$, Gelenkkräfte $G_V$ (↑) und $G_H$ (→) am rechten Ende.
> Freikörperbild II: Gelenkkräfte $G_V$ (↓) und $G_H$ (←) am linken Ende (Wechselwirkung), Streckenlast $q_0$, $F_C$ (↑) an $C$.

statisch bestimmt? $\;3\cdot n \overset{?}{=} a + z$ mit $n = 2$, $a = 4$, $z = 2$: $\;6 = 6\ \checkmark$

**I:**
$$\sum F_x = 0 \;\leadsto\; G_H - F_{BH} = 0\quad (1)$$
$$\sum F_y = 0 \;\leadsto\; F_A - F_K + F_{BV} + G_V = 0\quad (2)$$
$$\sum M\big|_B = 0 \;\leadsto\; F_A\left(\tfrac35 L_K\right) - F_K\,\tfrac25 L_K + G_V\,\tfrac15 L_K = 0\quad (3)$$

aus (1): $G_H = F_{BH}$

---

## Seite 43

**II:** $F_q = q_0\cdot L_A$, $\quad x_q = L_A/2$

$$\sum F_x = 0 \;\leadsto\; -G_H = 0\quad (4)$$
$$\sum F_y = 0 \;\leadsto\; -G_V + F_C - F_q = 0\quad (5)$$
$$\sum M\big|_G = 0 \;\leadsto\; F_C\,\frac{L_A}{2} - F_q\,\frac{L_A}{2} = 0\quad (6)$$

aus (4): $\checkmark\ \underline{G_H = 0}$
aus (6): $\checkmark\ \underline{F_C = F_q = q_0 L_A}$
aus (5): $\checkmark\ \underline{G_V = 0}$

↳ aus (1): $\checkmark\ F_{BH} = G_H = 0$

aus (3):
$$F_A\,\tfrac35 L_K - F_K\,\tfrac25 L_K + 0 = 0 \;\Rightarrow\; F_A = F_K\,\tfrac25 L_K\,\frac{5}{3L_K},\qquad \checkmark\ \underline{F_A = \tfrac23 F_K}$$

aus (2):
$$\tfrac23 F_K - F_K + F_{BV} + \underbrace{G_V}_{=0} = 0 \;\Rightarrow\; \checkmark\ \underline{F_{BV} = \tfrac13 F_K}$$

[Prüfung: Mit der Geometrie $A$ bei $\tfrac15 L_K$, $F_K$ bei $\tfrac25 L_K$, $B$ bei $\tfrac45 L_K$, $G$ bei $L_K$ sind die Hebelarme um $B$ ($\tfrac35$, $\tfrac25$, $\tfrac15$) und die Ergebnisse korrekt. Zahlenwerte werden nicht ausgerechnet; mit $F_K = 1600\,\mathrm{kg}\cdot 9{,}81\,\mathrm{m/s^2} \approx 15{,}7\,\mathrm{kN}$ wären $F_A \approx 10{,}5\,\mathrm{kN}$, $F_{BV} \approx 5{,}2\,\mathrm{kN}$, $F_C = 2500\,\mathrm N$ (das entspricht 250 kg mit $g \approx 10\,\mathrm{m/s^2}$; aus $q_0 = 1250\,\mathrm{N/m}$ folgt $L_A = 2\,\mathrm m$). Die Angabe „angezogene Handbremse" spielt ohne Horizontallast keine Rolle ($F_{BH} = G_H = 0$).]

---

## Seite 44

> Skizze (Zusammenfassung): Gesamtsystem Kfz–Gelenk–Anhänger mit $F_K$ und $q_0 L_A$ (↓); Achslasten (rot): $\tfrac23 F_K$ an $A$, $\tfrac13 F_K$ an $B$, $q_0 L_A$ an $C$; am Gelenk (rot umkreist) „$= 0$".

Kasten (rot) „Variationen": Anhänger mit Dreieckslast (ansteigend auf $q_0$) bzw. Rechteckslast $q_0$ nur über einen Teil der Länge $L_A$ – „?" → Übung

---

## Didaktische Gliederung

**Reihenfolge der Themen**
1. Inhaltsübersicht der gesamten Vorlesung (S. 1)
2. Einführung: Mechanik als Teilgebiet der Physik, Technische Mechanik, Gliederung Dynamik / Statik (Stereostatik, Elastostatik); Motivationsbeispiele Fahrrad, Umlenkrolle, Weinständer, Brücke (S. 2–3)
3. Grundlagen – Kraft (S. 4–6): $F = m a$, Gewichtskraft, Einheit N, Wirkungen (Bewegungsänderung, Deformation), Kraft als Vektor (Betrag, Wirkungslinie, Richtungssinn, Angriffspunkt), Komponenten/Koordinaten im kartesischen KOS, Richtungskosinus, Zerlegung in der Ebene, Einzelkraft als Idealisierung (Volumen-, Flächenkräfte)
4. Grundlagen – Moment (S. 7–8): Kräftepaar, $M = F b$, Einheit Nm, Doppelpfeil, freie Verschiebbarkeit des Moments, Moment bezüglich eines Punktes, Hebelarm, $\vec M = \vec r\times\vec F$
5. Axiome der Statik (S. 9–12): starrer Körper; 1. Linienflüchtigkeit, 2. Kräfteparallelogramm (→ statische Äquivalenz), 3. Gleichgewicht, 4. Wechselwirkung (actio = reactio) → Schnittprinzip (Euler); Beispiele zum Freischneiden
6. Ebenes zentrales Kräftesystem (S. 13–21): Äquivalenz (grafisch: Krafteck; analytisch: Komponentensummen), Quadrantenregel für $\alpha_R$, Gleichgewicht (geschlossenes Krafteck, $\sum F_x = \sum F_y = 0$), Beispiele/Übungen
7. Allgemeines Kräftesystem (S. 22–29): Versatzmoment, resultierende Kraft und Moment (räumlich, eben), Lage der Wirkungslinie der Resultierenden, Gleichgewicht (6 bzw. 3 Gleichungen), Hinweise zur Anwendung
8. Lager und Lagerreaktionen (S. 30–32): Freiheitsgrade, Loslager, Festlager, Einspannung, Gelenk, Hülse, Pendelstütze
9. Statische Bestimmtheit und Abzählkriterium (S. 33–34), Vorteile statisch bestimmter Lagerung
10. Berechnung von Lagerreaktionen (S. 35–36)
11. Streckenlasten und Linienlasten (S. 37–41): resultierende Kraft, Moment, Lage $x_R$; Rechteck-, Dreieckslast; Druck auf Halbkreisbogen (Projektionsprinzip)
12. Anwendungsbeispiel Mehrkörpersystem mit Gelenk: Kfz mit Anhänger (S. 42–44)

**Definitionen**
- Statik: Lehre von Körpern in Ruhe oder gleichförmiger geradliniger Bewegung; Stereostatik (starr) / Elastostatik (verformbar) (S. 2)
- Kraft: Vektor mit Betrag, Wirkungslinie, Richtungssinn, Angriffspunkt (S. 4)
- Moment: Kräftepaar $M = F\cdot b$; Moment einer Kraft um Punkt: $\vec M = \vec r\times\vec F$, $|M| = F\cdot b$ mit Hebelarm $b$ (S. 7–8)
- Starrer Körper (S. 9); statische Äquivalenz (S. 10); Gleichgewicht $\vec F_R = \vec 0$ (und $\vec M_R = \vec 0$) (S. 11, 16, 28)
- Ebenes zentrales Kräftesystem: alle Kräfte in einer Ebene, Wirkungslinien schneiden sich in einem Punkt (S. 13)
- Allgemeines ebenes Kräftesystem: Wirkungslinien schneiden sich nicht in einem Punkt (S. 22)
- Lagerwertigkeiten: Loslager (1), Festlager (2), Einspannung (3), Gelenk (2 Zwischenreaktionen), Hülse (Kraft quer + Moment), Pendelstütze (Kraft in Stabrichtung) (S. 30–32)
- Statisch bestimmt: alle Lagerreaktionen aus Gleichgewichtsbedingungen berechenbar (S. 33)
- Streckenlast $q(x)$ [Kraft/Länge] (S. 37)

**Rechenschemata**
- Resultierende im zentralen System: $F_{Rx} = \sum F_{ix}$, $F_{Ry} = \sum F_{iy}$, $F_R = \sqrt{F_{Rx}^2 + F_{Ry}^2}$, $\tan\alpha_R = F_{Ry}/F_{Rx}$ mit Quadrantenkorrektur ($+180°$ bei $F_{Rx}<0$) (S. 14–15)
- Gleichgewicht zentral: Freischneiden → KOS wählen → $\sum F_x = 0$, $\sum F_y = 0$ → lin. Gleichungssystem; positives Ergebnis = angenommene Richtung stimmt (S. 17–18)
- Resultierende allgemein: $F_{Rx}, F_{Ry}$ wie oben, $M_{Rz} = \sum (x_iF_{iy} - y_iF_{ix})$; Wirkungslinie $y_R = x_R\,F_{Ry}/F_{Rx} - M_{Rz}/F_{Rx}$ (S. 23–27)
- Lagerreaktionen: System skizzieren → Abzählkriterium $3n = a + z$ prüfen → freischneiden (Reaktionen willkürlich antragen) → $\sum F_x$, $\sum F_y$, $\sum M|_P$ (Bezugspunkt geschickt in ein Lager) → auflösen → Kontrolle (S. 33–36, 42–43)
- Mehrteilige Systeme: an Gelenken trennen, Zwischenreaktionen als Wechselwirkungspaare, zuerst das Teilsystem mit ≤ 3 Unbekannten lösen (S. 42–43)
- Streckenlast: $F_R = \int_a^b q\,\mathrm dx$, $M_R = \int_a^b q\,x\,\mathrm dx$, $x_R = M_R/F_R$; Rechteck: $qL$ bei $L/2$; Dreieck: $\tfrac12 q_0L$ bei $\tfrac23 L$ (vom Nullpunkt der Last) (S. 38–39)
- Druck auf gekrümmte Fläche: resultierende Kraft = Druck × Projektionslänge (S. 40–41)

---

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| 1 | Resultierende zweier Kräfte (zentral) | $F_1 = 20\,\mathrm N$ ($30°$), $F_2 = 30\,\mathrm N$ ($135°$) | $F_{Rx} = -3{,}89\,\mathrm N$, $F_{Ry} = 31{,}2\,\mathrm N$, $F_R = 31{,}44\,\mathrm N$ (exakt 31,46 N), $\alpha_R = 97{,}1°$ | 15 |
| 2 | Kugel an Seil an glatter Wand | $L = 40\,\mathrm{cm}$, $r = 10\,\mathrm{cm}$, $m$ | $F_S = mg/\sin\alpha = 4mg/\sqrt{15}$, $F_N = mg/\sqrt{15}$; zwei KOS-Varianten | 17–18 |
| 3 | Bolzen mit 4 Kräften (Übung ①) | $F_1 = 1000$, $F_2 = 500$, $F_3 = 1500$, $F_4 = 800\,\mathrm N$ | $F_{Rx} = -684\,\mathrm N$, $F_{Ry} = -2299\,\mathrm N$, $F_R = 2398{,}6\,\mathrm N$, $\alpha_R = 253°$ | 19 |
| 4 | Masse an zwei Seilen (Übung ②) | $m = 30\,\mathrm{kg}$, $a = 2$, $b = 4$, $c = 10$, $L = 4{,}5\,\mathrm m$ | $\beta = 27{,}27°$, $\alpha = 34{,}1°$, $N_1 = 277{,}7\,\mathrm N$, $N_2 = 298{,}1\,\mathrm N$, Wandkraft horizontal $\pm 246{,}8\,\mathrm N$ | 20–21 |
| 5 | Scheibe mit 4 Kräften (allg. ebenes System) | $F_1 = F_4 = F$, $F_2 = 2F$, $F_3 = 3F$, Lagen in $c$ | $F_R = 5F$, $M_{Rz}|_0 = -5cF$, WL $y = -\tfrac34 x + \tfrac54 c$, $x_{R0} = \tfrac53 c$; $\alpha_R$ im Original $143{,}1°$ (richtig: $-36{,}9°$) | 26–27 |
| 6 | Kragbalken mit Endlast | $F$, $L$ | $F_H = 0$, $F_V = -F$, $M = -FL$ | 33 |
| 7 | Einfeldträger mit Kragarm | $F_1 = F$ bei $L/2$, $F_2 = 2F$ bei $1{,}1L$ | $F_{AH} = 0$, $F_B = 2{,}7F$, $F_{AV} = 0{,}3F$ | 35 |
| 8 | Eingespannter Balken | $F_1 = F$ bei $L/2$, $F_2 = 2F$ bei $L$ | $F_{AH} = 0$, $F_{AV} = -3F$, $M_A = -2{,}5FL$ | 36 |
| 9 | Rechteckslast | $q$, $L$ | $F_R = qL$, $M_R = qL^2/2$, $x_R = L/2$ | 38–39 |
| 10 | Dreieckslast | $q_0$, $L$ | $F_R = q_0L/2$, $M_R = q_0L^2/3$, $x_R = \tfrac23 L$ | 39 |
| 11 | Innendruck auf Halbkreisbogen | $p$, $r$ | $F_{Ry} = 2pr$, $F_{Rx} = 0$; Viertelbogen $F_{Rx} = pr$ | 40–41 |
| 12 | Kfz mit Anhänger (Gelenk) | Kfz 1,5 t + 100 kg, Anhänger $q_0 = 1250\,\mathrm{N/m}$ | $G_H = G_V = 0$, $F_C = q_0L_A$, $F_{BH} = 0$, $F_A = \tfrac23 F_K$, $F_{BV} = \tfrac13 F_K$ | 42–44 |

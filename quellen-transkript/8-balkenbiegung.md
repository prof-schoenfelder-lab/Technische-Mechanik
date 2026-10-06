# Technische Mechanik – Festigkeitslehre: 3. Biegung des geraden Balkens (Vorlesung 2013)

Transkript der handschriftlichen Vorlesungsunterlagen (Prof. Schönfelder)
Quelle: `Quellen/Vorlesung-2013/8-balkenbiegung.pdf` (32 gescannte Seiten)

Hinweise zur Transkription:
- Farben im Original: Blau = Haupttext/Systeme, Rot = Kräfte/Momente/Spannungen, Grün = Koordinaten, Bemaßungen, Umrahmungen, Kommentare.
- Unsichere Lesungen sind mit [?] markiert, Anmerkungen der Transkription mit [Prüfung: ...] bzw. [Anm.: ...].

---

## Seite 1

# 3. Biegung des geraden Balkens

**Definition:** Biegung liegt dann vor, wenn unter der Einwirkung einer Belastung die **Krümmung** der Stab- bzw. Balkenachse verändert wird.

> Skizze: Links Einfeldträger (links Festlager, rechts Loslager) mit Einzelkraft $F$ (rot, nach unten) in Feldmitte; grün die durchgebogene Biegelinie. Rechts ein Balken, an beiden Enden durch Momente $M$ (rot, gegensinnige Drehpfeile) belastet; grün die gleichmäßig gekrümmte Biegelinie.

Ein linienförmiges Bauteil, das auf **Biegung** beansprucht wird, heißt **Balken**.

> Kasten rechts: „bisher: nur Zug/Druck" – Skizze eines Stabes mit roter Zugkraft (Pfeil nach rechts).

### 3.1 Begriffsbestimmung

#### 3.1.1 Einteilung der Biegung in Abhängigkeit des Vorhandenseins der Querkraft $Q$

- **Reine Biegung** (grün umrahmt): liegt (in einem Bereich) vor, wenn nur die **Biegemomente** der Schnittreaktionen von Null verschieden sind.
- **Querkraftbiegung** (grün umrahmt): liegt in einem Bereich vor, wenn neben den **Biegemomenten** auch die **Querkräfte** verschieden von Null sind.

(rot:) Schnittgrößen!

## Seite 2

**Beispiel:**

> Skizze: Einfeldträger (links Festlager, rechts Loslager) mit zwei gleich großen Einzelkräften $F$ (rot, nach unten), jeweils im Abstand $a$ von den Lagern (grün bemaßt). Darunter:
> – $Q$-Linie: im linken Bereich $(+)$ konstant, im Mittelbereich $0$, im rechten Bereich $(-)$ konstant (rot schraffiert).
> – $M$-Linie: linear ansteigend bis $x=a$, im Mittelbereich konstant $(+)$, rechts linear abfallend auf null (rot schraffiert, Trapez).
> – Bereichsmarkierungen darunter: Ⓐ – Ⓑ – Ⓐ.

Legende (grün umrahmt): Ⓐ Querkraftbiegung, Ⓑ reine Biegung

**Reine Biegung:**
$$\frac{dM(x)}{dx} = Q(x) = 0 \;\curvearrowright\; \underline{M(x) = \text{konst.}}$$

[Anm.: Mit den Auflagerkräften $A = B = F$ gilt $Q = +F$ bzw. $-F$ in den Randbereichen und $M_{\max} = F\,a$ im Mittelbereich – konsistent mit der Skizze.]

#### 3.1.2 Einteilung der Biegung in Abhängigkeit der Richtung des Biegemomentenvektors gegenüber den Hauptträgheitsachsen

**Einfache Biegung** (grün umrahmt) (Biegung um eine Hauptträgheitsachse)
- → Hauptträgheitsachsen sind bekannt → $y$-, $z$-Achse
- → Momentenvektor verläuft parallel zu einer Hauptträgheitsachse, d. h. zur $y$- oder $z$-Achse

## Seite 3

> Skizze: Zwei rechteckige Balkenquerschnitte (Beschriftung „Querschnitt Balken"), Achsen grün: $y$ nach links, $z$ nach unten, $x$ aus der Ebene heraus (⊙). Links: Momentenvektor $M_y$ (roter Doppelpfeil) in Richtung $y$. Rechts: Momentenvektor $M_z$ (roter Doppelpfeil) in Richtung $z$.

**Zweifache Biegung** (grün umrahmt)
- → Hauptträgheitsachsen sind bekannt ($y$-, $z$-Achse)
- → Momentenvektor besitzt andere Richtung als Hauptträgheitsachsen

> Skizze: Rechteckquerschnitt mit schräg liegendem Momentenvektor $M$ (rot, Doppelpfeil) $=$ Querschnitt mit $M_y$ (in $y$-Richtung) $+$ Querschnitt mit $M_z$ (in $z$-Richtung).

$$\vec M = \vec M_y + \vec M_z$$

**Allgemeine schiefe Biegung** (grün umrahmt)
- → Hauptträgheitsachsen „unbekannt", gewählte Achsen $y, z \neq$ Hauptträgheitsachsen der Fläche
- → beliebige Richtung des Momentenvektors

(rot, Randnotiz:) Lg [Lösung?]: s. Bücher! Gross 2009 [?]

## Seite 4

> Skizze: Unsymmetrischer (L-förmiger) Querschnitt („Querschnittsfläche des Balkens"), Achsen $y$ (links) und $z$ (unten) grün im Schwerpunkt [?], schräger Momentenvektor $M$ (rot, Doppelpfeil) – Beispiel für allgemeine schiefe Biegung.

### 3.2 Spannungen bei einfacher Biegung

(unter „einfacher Biegung" Hinweis: s. o.)

> Skizze: Links räumlicher Balkenausschnitt mit Rechteckquerschnitt; Achsen $x$ (Balkenachse, nach vorn/rechts), $y$ (links), $z$ (unten), grün. Am Schnittufer rot: Querkraft $Q$ (nach unten) und Momentenvektor $M$ (Doppelpfeil in $y$-Richtung). Rechts Seitenansicht: Balken, Schnittufer mit $Q$ (vertikal), Drehpfeil $M$, Achsen $x$ (rechts), $z$ (unten), $y$ (⊙).

**Biegespannungen**

> Skizze: Balkenstück mit Moment $M$ (Drehpfeil) → am Schnittufer ein Kräftepaar $F_D$ (oben, Druck, nach links) und $F_Z$ (unten, Zug, nach rechts) → linear verteilte Normalspannungen über die Höhe (rote Dreiecke, oben nach innen, unten nach außen); Beschriftung rot „Normalspannungen".

$\curvearrowright$ Biegespannungen sind Normalspannungen, die in jedem Querschnitt als Zug- und Druckspannungen vorhanden sind.

## Seite 5

**Voraussetzungen zur Herleitung:**
- prismatischer Träger (d. h. konstanter Querschnitt)
- Balkenachse sei gerade
- reine Biegung (nur Biegemoment, keine Querkraft)

$\curvearrowright$ Die im Folgenden hergeleiteten Beziehungen gelten streng genommen nur für die obigen Voraussetzungen.

Sie stellen aber auch gute Näherungen dar bei
- schwach gekrümmten Balken
- Balken mit stetig veränderlichen Querschnitten
- Balken mit Querkraftbiegung

**Annahmen zur Verformung:**
- → Längsachse des Balkens nimmt Form einer gekrümmten Kurve in der $x$-$z$-Ebene an
- → Verformungen senkrecht zur Längsachse (Balkenachse) in der $y$-$z$-Ebene werden vernachlässigt (sehr flache Schnitte, keine Querkontraktion!)
- → Querschnitte des Balkens **bleiben eben** $\curvearrowright$ **Bernoulli-Hypothese**

## Seite 6

> Skizze: Links unverformter Balken mit Achsen $x$ (rechts), $z$ (unten), $y$ (⊙), mit senkrechten Querschnittslinien und rechten Winkeln. Rechts derselbe Balken unter Momenten $M_y$ (rot, an beiden Enden) gekrümmt; Querschnittslinien laufen zum Krümmungsmittelpunkt (grün, oben) zusammen, rechte Winkel bleiben erhalten. Rot beschriftet: oben „Stauchung $\sigma_x < 0$", unten „Dehnung $\sigma_x > 0$", rote Mittellinie „neutrale Faser/Schicht → keine Längenänderung, $\sigma_x = 0$".

- → Verformung/Biegung so, dass alle Schichten mit $z = \text{konst.}$ konzentrische Kreise um einen Krümmungsmittelpunkt bilden.

> Skizze: Kreissektor mit Spitze im Krümmungsmittelpunkt; grüner Radius $\rho_0$ bis zur roten neutralen Schicht/Faser.

$\rho_0$ … Krümmungsradius der neutralen Schicht

$\curvearrowright$ **Vereinbarung:** Ursprung des Koordinatensystems soll in neutraler Schicht liegen.
aber: Lage der neutralen Schicht <u>noch</u> unbekannt!

## Seite 7

> Skizze: Balken unter $M_y$ an beiden Enden, Achsen $x$, $z$; herausgegriffenes Element der Länge $dx$.

→ Betrachtung eines Balkenelements der Länge $dx$

> Skizze: links „unverformt": Rechteckelement der Länge $dx$, rote Linie „neutr. Schicht" auf Höhe $z = 0$. Rechts „verformt": Kreisringsektor mit Öffnungswinkel $d\varphi$, Radius $\rho_0$ bis zur neutralen Schicht (Bogenlänge $ds_0$, rot), darunter Schicht im Abstand $z$ mit Bogenlänge $ds(z)$ (grün).

$ds_0$ … Länge der neutralen Schicht
$ds(z)$ … Länge der Schicht bei $z$

Verzerrung in einer Schicht bei $z$:
$$\varepsilon_x = \frac{ds(z) - ds_0}{ds_0} = \frac{(\rho_0 + z)\,d\varphi - \rho_0\,d\varphi}{\rho_0\,d\varphi} = \underline{\frac{z}{\rho_0}}$$

> Kasten (grün): Bogenmaß – Kreissektor mit Radius $r$, Winkel $\alpha$, Bogen $b$: $b = r\cdot\alpha$

## Seite 8

Bei reiner Biegung treten nur Spannungen in $x$-Richtung auf
→ einachsiger Spannungszustand

$$\varepsilon_x = \frac{\sigma_x}{E} \;\curvearrowright\; \boxed{\sigma_x = \varepsilon_x \cdot E = \frac{E\,z}{\rho_0}}$$

Zur Ermittlung von $\rho_0$ sind weitere Beziehungen notwendig.
⇒ Äquivalenzbetrachtungen zwischen Schnittgrößen ($N$ [?], $M_y$, $M_z$) und Spannungen ($\sigma_x$)

> Skizze: Räumlicher Balkenausschnitt, Schnittfläche mit Achsen $x$, $y$, $z$ (grün); Momentenvektor $M$ (rot, Doppelpfeil in $y$-Richtung); Flächenelement $dA$ an der Stelle $(y, z)$; daran rote Kraft $dF_x = \sigma_x\,dA$.

**1. Äquivalenzbedingung:** Die Biegespannung hat [?] keine resultierende Kraftwirkung.

$$N \overset{!}{=} 0 = \int_A \sigma_x\,dA = \int_A \frac{E\,z}{\rho_0}\,dA = \frac{E}{\rho_0}\int_A z\,dA$$

(grün: $\int_A z\,dA$ = statisches Moment)

## Seite 9

$$\int_A z\,dA \;\longrightarrow\; \text{stat. Moment } (S_y)$$

$\curvearrowright$ $\underline{S_y = 0}$, nur wenn Ursprung des Koordinatensystems im Schwerpunkt der Fläche liegt.
→ <u>Querschnittsschwerpunkt in neutraler Schicht!</u>
(Wolke: bzw. umgekehrt → neutrale Faser im Schwerpunkt)

**2. Äquivalenzbedingung:** Resultierende Momentwirkung der Biegespannung um die $y$-Achse muss gleich dem Biegemoment $M_y$ sein.

$$M_y = \int dM_y = \int z\,dF_x = \int_A z\,\sigma_x\,dA = \int_A z\,\frac{E\,z}{\rho_0}\,dA = \frac{E}{\rho_0}\underbrace{\int_A z^2\,dA}_{I_{yy}}$$

$$\boxed{M_y = \frac{E}{\rho_0}\,I_{yy}} \;\to\; \underline{\frac{1}{\rho_0} = \frac{M_y}{E\,I_{yy}}} \qquad (3.2.1)$$

**3. Äquivalenzbedingung:** Die Biegespannung hat keine resultierende Momentwirkung um die $z$-Achse.

$$\underline{M_z = 0}: \quad M_z = \int dM_z = -\int y\,dF_x = -\int_A y\,\sigma_x\,dA$$

## Seite 10

$$M_z = -\int_A y\,\frac{E\,z}{\rho_0}\,dA = -\frac{E}{\rho_0}\underbrace{\int y z\,dA}_{I_{yz}} = \frac{E}{\rho_0}\,I_{yz} \overset{!}{=} 0$$

[Anm.: Im Original fehlt im letzten Schritt das Minuszeichen ($-\frac{E}{\rho_0}I_{yz}$); für die Aussage $=0$ ohne Belang.]

$I_{yz} = 0$, da $y$ und $z$ Hauptträgheitsachsen!
$\curvearrowright$ $I_{yz}$ muss verschwinden! → macht es auch!
$\curvearrowright$ sonst schiefe Biegung (!)

⇒ Mit der Gleichung (3.2.1) entsteht aus
$$\sigma_x(z) = \frac{E}{\rho_0}\,z$$

$$\boxed{\sigma_x(z) = \frac{M_y}{I_{yy}}\cdot z} \qquad (3.2.2)$$

(grün:) **Biegespannungsformel**
- → KOS im Schwerpunkt der Querschnittsfläche
- → Deviationsmoment $= 0$

## Seite 11

- Die Biegespannung hängt linear von $z$ ab.

> Skizze: Räumlicher Balkenausschnitt mit Rechteckquerschnitt, Schwerpunkt $S$ (rot) auf der roten Nulllinie; oben dreieckförmige rot schraffierte Spannungsverteilung „Druck", unten „Zug" (linear über die Höhe, null in der Schwerachse).

- Erweiterung von (3.2.2) auf
  - veränderliche Querschnitte ($I_{yy}(x)$) und
  - Querkraftbiegung ($M_y(x)$)

$$\boxed{\sigma_x(x,z) = \frac{M_y(x)}{I_{yy}(x)}\,z}$$

## Seite 12

**Beispiel:** (Kragträger, Vergleich Kreis-/Kreisringquerschnitt)

geg.: $F, L, d$
ges.:
- a) $\sigma_{\max}$?
- b) $d_a$, damit gleiche maximale Spannung wie Fall (I) auftritt
- c) Materialaufwand
- d) Rechteckquerschnitt, $b = d$ (nachträglich ergänzt)

> Skizze: Kragträger, links eingespannt, Länge $L$ (grün bemaßt), am freien rechten Ende Einzelkraft $F$ (rot, nach unten). Koordinaten am freien Ende: $x$ nach links, $z$ nach unten.

I) Vollquerschnitt (Kreis): Kreis mit Durchmesser $d$, Achsen $y$ (links), $z$ (unten).
II) Hohlquerschnitt (Ring): Außendurchmesser $d_a$, Innendurchmesser $d_i$; (grün) $d_i = 0{,}9\,d_a$.

**Lös.:**
- Schnittkräfte

> Skizze: Rechtes Balkenstück (Länge $x$ vom freien Ende) mit $F$; am Schnittufer rot $N$ (nach links), $Q$ (nach unten), $M$ (Drehpfeil). Koordinaten $x$ (links), $z$ (unten).

$$\rightarrow:\; \underline{N = 0} \qquad \uparrow:\; \underline{Q(x) = -F} \qquad \curvearrowleft:\; M_y(x) + F\cdot x = 0$$
$$\underline{M_y(x) = -F\,x}, \qquad \underline{M_{y,\max} = -F\,L}$$

> Skizze: Kragträger mit $F$; darunter $Q$-Linie konstant $(-)$ (rot), $M$-Linie dreieckförmig $(-)$, an der Einspannung $-F\,L$, am freien Ende null.

## Seite 13

$$\sigma_x(x,z) = \frac{M_y(x)}{I_{yy}}\cdot z$$

a) (grün: „Tabellen")
$$I_{yy,\text{Kreis}} = \frac{\pi}{64}d^4 = 0{,}0491\,d^4$$
$$I_{yy,\text{Ring}} = \frac{\pi}{64}(d_a^4 - d_i^4) = \frac{\pi}{64}\left(d_a^4 - (0{,}9\,d_a)^4\right) = 0{,}0169\,d_a^4$$

$$\underline{\sigma_{x,\max}\big|_\text{Kreis}} = \frac{-F L}{0{,}0491\,d^4}\left(\pm\frac{d}{2}\right) = (\pm)\left(\frac{F L}{0{,}0982\,d^3}\right)$$
(grün: $\pm d/2$ = (max.) $z$, Abstand von neutraler Schicht; $\pm$ → Zug/Druck!)

$$\underline{\sigma_{x,\max}\big|_\text{Ring}} = \frac{-F L}{0{,}0169\,d_a^4}\left(\pm\frac{d_a}{2}\right) = (\pm)\left(\frac{F L}{0{,}0338\,d_a^3}\right)$$

> Skizze (grün umrahmt): Balkenstück mit linearer Spannungsverteilung über die Höhe, oben $+\sigma_{\max}$, unten $-\sigma_{\max}$ (rot).

[Prüfung: Zahlenwerte korrekt ($\pi/64 = 0{,}04909$; $\tfrac{\pi}{64}(1-0{,}9^4) = 0{,}01688$). Streng genommen ergibt $-F L\cdot(\pm d/2)$ das Vorzeichen $\mp$: Zug ($+$) bei $z = -d/2$ (Oberseite, Kragträger mit negativem Moment), Druck unten – passt zur Skizze rechts.]

b)
$$\sigma_{x,\max}\big|_\text{Kreis} = \sigma_{x,\max}\big|_\text{Ring}: \quad \frac{F L}{0{,}0982\,d^3} = \frac{F L}{0{,}0338\,d_a^3}$$
$$d_a^3 = \frac{0{,}0982}{0{,}0338}\,d^3$$
$$\underline{d_a = 1{,}427\,d}, \qquad \underline{d_i = 0{,}9\,d_a = 1{,}284\,d}$$

[Prüfung: $(2{,}905)^{1/3} = 1{,}427$ ✓; $0{,}9\cdot 1{,}427 = 1{,}284$ ✓]

## Seite 14

c) Materialaufwand
$$V_\text{Kreis} = A_\text{Kreis}\cdot L = \underline{\frac{\pi}{4}d^2 L}$$
$$V_\text{Ring} = A_\text{Ring}\cdot L = \frac{\pi}{4}(d_a^2 - d_i^2)L = \frac{\pi}{4}\left((1{,}427\,d)^2 - (1{,}284\,d)^2\right)L = \underline{\frac{\pi d^2}{4}L\cdot 0{,}388}$$

$$\frac{V_\text{Kreis}}{V_\text{Ring}} = \frac{1}{0{,}388} = 2{,}58$$
$\curvearrowright$ Kreisringquerschnitt braucht weniger Material ⇒ günstiger

[Prüfung: $2{,}0363 - 1{,}6487 = 0{,}3876$ ✓; $1/0{,}388 = 2{,}58$ ✓]

d) Vergleich Rechteckquerschnitt mit $\sigma_{\max,\circ}$, $b = d$, $h$?

> Skizze: Rechteckquerschnitt Breite $b$, Höhe $h$, Achsen $y$ (links), $z$ (unten) im Schwerpunkt; $h/2 = z_{\max}$ (grün).

$$\sigma_{\max,\square} = \sigma_{\max,\circ}: \quad \frac{M_y}{I_{yy}}\cdot z_{\max} = \frac{F L}{0{,}0982\,d^3}$$
(ein erster Ansatz ist durchgestrichen)
$$\frac{M_y}{I_{yy}}\cdot z_{\max} = \frac{F L\cdot 12}{b h^3}\cdot\frac{h}{2} = \frac{F L\cdot 6}{b h^2}$$

## Seite 15

$$\sigma_{\max,\square} = \sigma_{\max,\circ}: \quad \frac{6 F L}{d\,h^2} = \frac{F L}{0{,}0982\,d^3}$$
$$h^2 = 6\cdot 0{,}0982\,d^2, \qquad h = \sqrt{6\cdot 0{,}0982}\;d = 0{,}77\,d$$
(ein zuerst notierter falscher Wert ist durchgestrichen und durch $0{,}77$ ersetzt)

[Prüfung: $\sqrt{0{,}589} = 0{,}768$ ✓]

> Skizze: Kreisquerschnitt mit einbeschriebenem Rechteck (grün schraffiert, Breite $= d$, Höhe $h < d$); daneben grün umrahmt: $\uparrow \sigma_\square\!\downarrow\, < \sigma_\circ$ und $\downarrow \sigma_\square\!\uparrow\, > \sigma_\circ$ [?] – „führt zur gleichen max. Spannung in Randschicht!"

$$A_\square = d\cdot h = 0{,}77\,d^2, \qquad A_\circ = \frac{\pi}{4}d^2 = 0{,}78\,d^2$$
$\curvearrowright$ <u>kaum Materialunterschied!</u>

(rechts, Herleitung über Widerstandsmoment:)
$$I_{yy,\circ} = \frac{\pi d^4}{64}, \qquad W_{yy,\circ} = \frac{\pi d^4\cdot 2}{64\,d} = \frac{\pi}{32}d^3$$
$$I_{yy,\square} = \frac{b h^3}{12}, \qquad W_{yy,\square} = \frac{b h^3\cdot 2}{12\,h} = \frac{b h^2}{6}$$

$$W_{yy,\circ} = W_{yy,\square}: \quad \frac{\pi}{32}d^3 = \frac{d\,h^2}{6} \;\to\; \frac{3}{16}\pi\,d^2 = h^2 \;\to\; h = \sqrt{\tfrac{3}{16}\pi}\;d = 0{,}77\,d$$

> Skizze: Diagramm $W$ über $h$: $W_\circ$ konstant (waagerechte Linie), $W_\square$ parabelförmig ansteigend; Schnittpunkt bei $h^*$.

(grün:) ab $h > h^*$: $W_\square > W_\circ$ $\curvearrowright$ mehr Fläche mit großem Abstand $z$ von neutraler Faser

## Seite 16

**Variante 2 der Aufgabe**
(f) [?] veränderlicher Querschnitt, so dass $\sigma(x) = \text{konst.} = \sigma(x = L)$

$\curvearrowright$ Rechteckquerschnitt

> Skizze: Rechteckquerschnitt Breite $b$, Höhe $h$, Achsen $y$, $z$; daneben „$b = 1\,\text{mm}$" durchgestrichen. Kragträger links eingespannt, $F$ am freien Ende. $M$-Linie: Dreieck, an der Einspannung $-F L$, Koordinate $x$ vom freien Ende nach links.

$$M_y(x) = -F\,x, \qquad M_y(x = L) = -F\,L$$
$$\sigma_x(x,z) = \frac{M_y(x)}{I_{yy}(x)}\,z$$
$$\sigma_x\!\left(x = L,\; z = -\tfrac{h}{2}\right) = \frac{-F L\cdot 12}{b_L h_L^3}\cdot\left(-\frac{h_L}{2}\right) = +6\,\frac{F L}{b_L h_L^2}$$

$$\sigma_x\!\left(x,\; z = -\tfrac{h}{2}\right) = \frac{M_y(x)}{I_{yy}(x)}\,z: \quad 6\,\frac{F L}{b_L h_L^2} = \frac{-12\,F x}{b\,h^3}\cdot\left(-\frac{h}{2}\right) = \frac{6 F x}{b\,h^2}$$
$$\underline{b\,h^2(x) = \frac{x}{L}\,b_L h_L^2}$$

für $b = b_L$ → $h(x) = \sqrt{\dfrac{x}{L}\,h_L^2} = h_L\sqrt{x/L}$

> Skizze: Diagramm $h$ über $x$ (vom freien Ende): Wurzelparabel von $0$ bis $h_L$. Rechts Kragträger mit nach rechts spitz zulaufender, parabelförmig berandeter Höhe $h(x)$, konstante Breite $b$, Last $F$ am freien Ende.

$\curvearrowright$ (rot) $\sigma_x = \text{const} = 6\,\dfrac{F L}{b_L h_L^2}$ – „Träger gleicher Festigkeit"

(Randkasten:) besser auf $\sigma = \sigma_\text{zul}$! anstatt $\sigma(x = L, z_{\max})$

[Prüfung: Herleitung korrekt. Hinweis: Bei $x \to 0$ würde $h \to 0$ – praktisch ist am Lastangriffspunkt eine Mindesthöhe aus der Schubbeanspruchung nötig (in der Vorlesung nicht thematisiert).]

## Seite 17

**Wdhlg.** (Wiederholung)

- einfache Biegung

> Skizze: Rechteckquerschnitt mit Achsen $y$ (links), $z$ (unten); Beschriftung „Biegung um eine Hauptträgheitsachse".

- > Skizze: Balkenstück mit linearer Spannungsverteilung (rot) $\;\hat{=}\;$ Moment $M$ (Drehpfeil) $\;\hat{=}\;$ Kräftepaar $F$ (oben nach rechts, unten nach links).

(rot:) (Bernoulli-Hypothese)

- > Skizze: Gekrümmter Balken unter $M_y$; Achsen $x$, $z$ (grün); senkrecht bleibende Querschnittslinien mit rechten Winkeln („ebene Querschnitte"); oben „Stauchung", unten „Dehnung" (rot); grün unterstrichen „neutrale Schicht/Faser → $\sigma_x = 0$" (rot), darunter grün: „in Querschnittsschwerpunkt! ($S_y = 0$!)".

- $$\boxed{\sigma_x(z) = \frac{M_y}{I_{yy}}\cdot z}$$

> Skizze: Gekrümmter Balken mit $M_y$ an beiden Enden, Achsen $x$, $z$; daneben schraffierter Querschnitt mit Hinweis $I_{yy}$.

> Skizze: Diagramm $z$ über $\sigma_x$ (bzw. Querschnittshöhe): lineare Spannungsverteilung, oben $\ominus$, unten $\oplus$ [?]; Text: „$\sigma_x$ linear (da Bernoulli-Hypothese)". Daneben Symbol $\|\to/\backslash$: $\varepsilon \to$ linear $\to \sigma$ linear; grün: „Dankert S. 216".

## Seite 18

(Rückseite eines Blattes, auf dem Kopf stehend beschriftet:) **Wdhlg / Zusammenfassung einfache Biegung** – ansonsten leer.

## Seite 19

**Beispiel: 3-Punkt-Biegung**

> Skizze: Einfeldträger, links Festlager $A$, rechts Loslager $B$, Gesamtlänge $L$ ($L/2 + L/2$, grün bemaßt), Einzelkraft $F$ (rot, nach unten) in Feldmitte. Koordinate $x$ ab $A$ nach rechts, $z$ nach unten. Rechteckquerschnitt $b \times h$ (schraffiert). Grüne Umrandungen der Schnittbereiche I (links) und II.

geg.: $F, L, b, h$
ges.: Verlauf Biegespannung $\sigma_x(x,z)$, $\sigma_{x,\max}$

**Lös.:**
① (~~Schnittgrößen~~) Gleichgewicht, Lagerreaktionen

> Skizze: Freigeschnittener Balken mit $A_H$ (→), $A_V$ (↑), $B$ (↑), $F$ (↓).

$$\rightarrow:\; \underline{A_H = 0} \qquad \uparrow:\; -F + A_V + B = 0 \qquad \curvearrowleft_A:\; -F\frac{L}{2} + B\cdot L = 0$$
$$\underline{B = \frac{F}{2}}, \qquad \underline{A_V = \frac{F}{2}}$$

② Schnittreaktionen

**I** $\;0 \le x \le L/2$

> Skizze: Linkes Teilstück mit $F/2$ (↑) am Lager; am Schnittufer $N(x)$ (→), $Q(x)$ (↓), $M(x)$ (Drehpfeil).

$$\rightarrow:\; \underline{N(x) = 0} \qquad \updownarrow:\; Q(x) - \tfrac{F}{2} = 0 \;\to\; \underline{Q(x) = +\tfrac{F}{2}}$$
(Vorzeichen im Original rot korrigiert, $+F/2$ in der Gleichung zu $-F/2$)
$$\curvearrowleft:\; M(x) - \tfrac{F}{2}\cdot x = 0 \;\to\; \underline{M_y(x) = \tfrac{F}{2}\,x} \quad (1)$$

## Seite 20

**II** $\;L/2 \le x \le L$

> Skizze: Teilstück von $A$ bis zum Schnitt, $F/2$ (↑) am Lager, $F$ (↓) bei $L/2$; lokale Koordinate $x_2$ ab Lastangriff nach rechts; am Schnittufer $N(x)$, $Q(x)$ (↓, rot), $M(x)$.

$$\rightarrow:\; \underline{N(x_2) = 0}$$
$$\updownarrow:\; Q(x_2) - \tfrac{F}{2} + F = 0 \;\to\; \underline{Q(x) = -\tfrac{F}{2}}$$
(Vorzeichen im Original rot korrigiert)
$$\curvearrowleft:\; M_y(x_2) - \tfrac{F}{2}\left(\tfrac{L}{2} + x_2\right) + F\cdot x_2 = 0$$
$$M_y(x_2) = +\frac{F}{2}\frac{L}{2} + \frac{F}{2}x_2 - F x_2 = \underline{-\frac{F}{2}x_2 + \frac{F}{4}L} \quad (2)$$

> Skizze: Schnittgrößenverläufe unter dem Träger ($F/2$ an beiden Lagern, $F$ in der Mitte), Koordinaten $x_I$, $x_{II}$:
> – $N$: überall $0$.
> – $Q$: Bereich I $(+)\,F/2$ (unter der Achse aufgetragen), Bereich II $(-)$ (über der Achse, rot, nachträglich umgezeichnet; Randbeschriftung „$+F/2$" [?]).
> – $M_y(x)$: Dreieck, $0$ an den Lagern, Maximum $\frac{F}{4}L$ in Feldmitte, $\oplus$.

$\curvearrowright$ $\sigma_x = \dfrac{M_y(x)}{I_{yy}}\,z$ – für $I_{yy}, z = \text{const}$ ist der Verlauf von $\sigma_x$ qualitativ identisch zu $M_y$!

[Prüfung: $Q$ und $M$ korrekt ($M_{\max} = FL/4$). Die Randbeschriftung „$+F/2$" im Bereich II müsste $-F/2$ lauten; zudem ist $Q$ (positiv nach unten) und $M$ (positiv nach oben) mit unterschiedlicher Auftragsrichtung gezeichnet.]

## Seite 21

③ Spannungen

> Skizze: Diagramm $\sigma$ über $x$: für $z$ positiv (Unterseite) dreieckförmig $\oplus$ (rot) mit Spitze „$\sigma_{\max}$?" in Feldmitte, $0$ an den Lagern; für $z$ negativ spiegelbildlich $\ominus$ (blau). Koordinaten $x_I$, $x_{II}$.

$$\sigma_x(x,z) = \frac{M_y(x)}{I_{yy}}\,z$$

- Rechteck → $I_{yy} = \dfrac{b h^3}{12}$
- $z$ → max. $\pm\dfrac{h}{2}$
- $M_y(x)$ → aus (1) o. (2)
- $M_{y,\max}$ → (1) → $x = L/2$; (2) → $x = 0$

$$\underline{\sigma^{I}_{x,\max}} = \frac{M^I_y(x_I = L/2)\cdot 12}{b h^3}\cdot\frac{h}{2} = \frac{6}{b h^2}\cdot\frac{F}{2}\cdot\frac{L}{2} = \underline{\frac{3}{2}\frac{F L}{b h^2}}$$
$$\underline{\sigma^{II}_{x,\max}} = \frac{M^{II}_y(x_{II} = 0)\cdot 12}{b h^3}\cdot\frac{h}{2} = \frac{6}{b h^2}\left(-\frac{F}{2}\cdot 0 + \frac{F}{4}L\right) = \underline{\frac{3}{2}\frac{F L}{b h^2}}$$
(grün:) identisch!

## Seite 22

- Verlauf über Querschnitt

$$\sigma_x(x,z) = \frac{12\,M_y(x)}{b h^3}\cdot z \quad \text{für } x_I = \frac{L}{2}$$
$$\underline{\sigma_x(z)} = \frac{12}{b h^3}\cdot\frac{F L}{2\cdot 2}\,z = \underline{3\,\frac{F L}{b h^3}\cdot z}$$

> Skizze: Balken (Draufsicht mit Schnitt in Feldmitte), vergrößerter Querschnitt der Höhe $h$ ($h/2$ + $h/2$ grün bemaßt), Koordinate $z$ nach unten. Lineare Spannungsverteilung (rot): oben $-\frac{3}{2}\frac{FL}{bh^2}$ $\ominus$, im Schwerpunkt $0$, unten $+\frac{3}{2}\frac{FL}{bh^2}$ $\oplus$ („$\sim \sigma(z)$"). Rechts für drei Fasern (oben, Mitte, unten) der Spannungsverlauf entlang $x$: oben Dreieck $\ominus$, Mitte $0$, unten Dreieck $\oplus$.

→ maximale Belastung in den äußersten Schichten des Balkens bei $z_{\max} = \pm\dfrac{h}{2}$ (für Rechteck)

$\curvearrowright$ **Widerstandsmoment** $W_y$
$$\boxed{W_y = \frac{I_{yy}}{z_{\max}}} \qquad \curvearrowright\; \boxed{\sigma_x = \frac{M_y}{W_y}}$$
$$\underline{W_{y,\square}} = \frac{b h^3\cdot 2}{12\,h} = \underline{\frac{b h^2}{6}}$$

[Anm.: Im Original $W_y = I_{yz}/z_{\max}$ geschrieben [?] – gemeint ist $I_{yy}$.]

## Seite 23

**Übung Biegung**

> Skizze: Rahmen (U-förmig, nach oben offen). Linker Stiel von Lager $A$ (oben, Festlager) nach unten, Länge $3c + 3c$; bei $3c$ unter $A$ Querschnitt I: Vollquadrat $a \times a$ (grün). Riegel unten, Länge $4c$ (grün bemaßt), Querschnitt II bei $2c$ vom linken Eck: Quadrat $b \times b$ mit zentrischer Bohrung Durchmesser $d$. Rechter Stiel vom rechten Eck nach oben, Länge $3c$, oben Loslager $B$ (horizontal wirkend). Lasten (rot): $2F$ horizontal nach rechts am linken unteren Eck, $F$ vertikal nach unten am rechten unteren Eck.

geg.: $F = 160\,\text{N}$, $c = 32\,\text{mm}$, $b = 10\,\text{mm}$, $\sigma_\text{zul} = 240\,\text{N/mm}^2$

ges.:
- a) Kantenlänge $a$ (für $\sigma_{\max} \le \sigma_\text{zul}$) bei $3c$
- b) max. zulässiger Durchmesser $d$ bei $2c$, so dass zulässige Biegespannung nicht überschritten wird.

**Lös.:** ① Lagerreaktionen

> Skizze: Freigeschnittener Rahmen mit $A_H$ (→), $A_V$ (↓) an $A$, $B$ (←) am rechten Stiel, $2F$ (→) und $F$ (↓).

$$\rightarrow:\; A_H + 2F - B = 0$$
$$\uparrow:\; -A_V - F = 0 \;\to\; \underline{A_V = -F}$$
$$\curvearrowleft_A:\; -B\cdot 3c - F\cdot 4c + 2F\cdot 6c = 0 \;\to\; \underline{B = \frac{8 F c}{3 c} = \frac{8}{3}F}$$
$$\underline{A_H = \frac{2}{3}F}$$

[Prüfung: korrekt.]

## Seite 24

② Schnittgrößen

> Skizze: Rahmen mit tatsächlichen Lagerkräften: an $A$ $F$ (↑) und $\frac{2}{3}F$ (→), am rechten Stiel $\frac{8}{3}F$ (←), $2F$ und $F$ wie gegeben. Koordinaten $x_1$ (am linken Stiel von $A$ nach unten), $x_2$ (Riegel von links nach rechts), $x_3$ (rechter Stiel von unten nach oben). Grün umrandete Bereiche I, II, III.

**I**
> Skizze: Oberes Stielstück mit $F$ (↑), $\frac{2}{3}F$ (→); am Schnitt $N_1$ (↓), $Q_1$ (←), $M_1$.

$$\downarrow:\; N_1 - F = 0 \;\to\; \underline{N_1 = F}$$
$$\rightarrow:\; -Q_1 + \tfrac{2}{3}F = 0 \;\to\; \underline{Q_1 = +\tfrac{2}{3}F}$$
$$\curvearrowleft:\; M_1 - \tfrac{2}{3}F\cdot x_1 = 0 \;\to\; \underline{M_1 = \tfrac{2}{3}F\,x_1}$$

**II**
> Skizze: Linker Stiel + Riegelstück bis $x_2$ mit $F$ (↑), $\frac{2}{3}F$ (→) oben, $2F$ (→) am Eck; am Schnitt $N_2$ (→), $Q_2$ (↑/↓), $M_2$.

$$\rightarrow:\; N_2 + 2F + \tfrac{2}{3}F = 0 \;\to\; \underline{N_2 = -\tfrac{8}{3}F}$$
$$\uparrow:\; -Q_2 + F = 0 \;\to\; \underline{Q_2 = +F}$$
$$\curvearrowleft:\; M_2 - \tfrac{2}{3}F\cdot 6c - F\cdot x_2 = 0 \;\to\; \underline{M_2 = F(x_2 + 4c)}$$

**III**
> Skizze: Oberes Stück des rechten Stiels (Länge $3c - x_3$) mit $\frac{8}{3}F$ (←) oben; am Schnitt $N_3$ (↓), $Q_3$ (←), $M_3$; $x_3$ nach oben.

$$\uparrow:\; -N_3 = 0 \;\to\; \underline{N_3 = 0}$$
$$\rightarrow:\; -Q_3 - \tfrac{8}{3}F = 0 \;\to\; \underline{Q_3 = -\tfrac{8}{3}F}$$
$$\curvearrowleft:\; M_3 - \tfrac{8}{3}F(3c - x_3) = 0 \;\to\; \underline{M_3 = \tfrac{8}{3}F(3c - x_3)}$$

[Prüfung: Übergangsbedingungen erfüllt – $M_1(6c) = 4Fc = M_2(0)$; $M_2(4c) = 8Fc = M_3(0)$.]

## Seite 25

> Skizze $N$: linker Stiel $\oplus$ konstant $F$ (rot); Riegel $\ominus$ konstant $-\frac{8}{3}F$; rechter Stiel $0$. Lokale Koordinaten $x_i$, $z_i$ grün.

> Skizze $Q$: linker Stiel $\oplus$ konstant $\frac{2}{3}F$; Riegel $\oplus$ konstant $F$; rechter Stiel $\ominus$ $\frac{8}{3}F$ (eine zuerst falsch eingezeichnete $\oplus$-Fläche durchgestrichen).

> Skizze $M$: linker Stiel dreieckförmig $\oplus$ von $0$ (bei $A$) bis $4Fc$ (unten); Riegel trapezförmig $\oplus$ von $4Fc$ bis $8Fc$; rechter Stiel dreieckförmig $\oplus$ von $8Fc$ (unten) bis $0$ (bei $B$).

## Seite 26

③ Spannungen, nur Biegung

$$\sigma_x = \left(\cancel{\frac{N_x}{A}} +\right)\frac{M_y}{I_{yy}}\,z$$
(Normalkraftanteil grün durchgestrichen)

> Skizze: Rahmen mit Querschnitt I (Quadrat $a\times a$) am linken Stiel und Querschnitt II (Quadrat $b\times b$ mit Bohrung $d$) am Riegel; Lasten $2F$, $F$.

**I** $\quad A = a^2, \quad I_{yy} = \dfrac{b h^3}{12} = \dfrac{a^4}{12}, \quad z_{\max} = \dfrac{a}{2}$

$N_{1,\max} = F$, $\quad M_{y1,\max} = 4Fc$

$$\sigma^I_{x,\max} = \left(\cancel{\tfrac{F}{a^2}}\right) + \frac{4Fc\cdot 12\,a}{a^4\cdot 2} = \left(\cancel{\tfrac{F}{a^2}}\right) + \frac{24\,Fc}{a^3}$$
$$\sigma_{x,\max} \le \sigma_\text{zul}: \quad \frac{24\,Fc}{a^3} \le \sigma_\text{zul} \;\to\; \underline{a \ge \sqrt[3]{\frac{24\,Fc}{\sigma_\text{zul}}}} \qquad \underline{a \ge 8\,\text{mm}} \text{ für } \sigma_{\max}$$

Bei $3c$:
$$M_{y1}\big|_{3c} = 2Fc, \qquad \sigma_{x,\max} = \frac{12\,Fc}{a^3} \;\to\; a \ge \sqrt[3]{256}, \quad \underline{a \ge 6{,}35\,\text{mm}}$$

[Prüfung: $24\cdot 160\cdot 32/240 = 512 = 8^3$ ✓; $12\cdot 160\cdot 32/240 = 256$, $\sqrt[3]{256} = 6{,}35$ ✓. Gefragt war $a$ bei $3c$ → $a \ge 6{,}35\,\text{mm}$; $8\,\text{mm}$ gilt für das Maximum an der Rahmenecke.]

## Seite 27

**II**
$$A_1 = b^2, \quad A_2 = \frac{\pi}{4}d^2, \quad \underline{A = b^2 - \frac{\pi}{4}d^2}$$

> Skizze: Quadrat $b \times b$ mit zentrischer Bohrung $d$, Achsen $y$, $z$ im Mittelpunkt. „zusammengesetzte Fläche für $I_{yy}$".

(Tabellenköpfe für zusammengesetzte Flächen: $i$, $\bar z_{Si}$, $\bar y_{Si}$, $A_i$, $\bar z_{Si}A_i$, $\bar y_{Si}A_i$ bzw. $i$, $\bar z_{Si} - \bar z_S$, $\bar y_{Si} - \bar y_S$, $A_i$, $I_{yy,i}$, $z_{Si}^2 A_i$ – Schwerpunktabstände alle $0$, daher durchgestrichen.)

$$\underline{I_{yy} = I_{yy,1} - I_{yy,2} = \frac{b^4}{12} - \frac{\pi d^4}{64}}, \qquad \underline{z_{\max} = \frac{b}{2}}$$

$$\sigma_x = \frac{M^{II}_y}{I_{yy}}\,z, \qquad M_{y2}\big|_{2c} = 6Fc \;\;(\text{zuerst } 8Fc, \text{ korrigiert})$$

$$\sigma_{x,2c} \le \sigma_\text{zul}: \quad \frac{6Fc}{\frac{b^4}{12} - \frac{\pi d^4}{64}}\cdot\frac{b}{2} \le \sigma_\text{zul}$$
$$3Fcb \le \sigma_\text{zul}\left(\frac{b^4}{12} - \frac{\pi d^4}{64}\right)$$
$$-3Fcb + \sigma_\text{zul}\frac{b^4}{12} \ge \sigma_\text{zul}\frac{\pi d^4}{64}$$
$$d \le \sqrt[4]{-\frac{3Fcb\cdot 64}{\sigma_\text{zul}\,\pi} + \frac{16\,b^4}{3\pi}} = \sqrt[4]{-\frac{192\,Fcb}{\sigma_\text{zul}\,\pi} + \frac{16\,b^4}{3\pi}}$$
$$\underline{d \le 7{,}92\,\text{mm}}$$

[Prüfung: $16\cdot 10^4/(3\pi) = 16\,977$; $192\cdot 160\cdot 32\cdot 10/(240\pi) = 13\,038$; Differenz $3\,939$, $\sqrt[4]{3939} = 7{,}92$ ✓.]

## Seite 28

- für $\sigma^{II}_{x,\max}$ (bei $8Fc$) kann man $d$ nicht bestimmen → Gleichung nicht lösbar

$\curvearrowright$ Test mit Vollquadrat $b \times b$:
$$\sigma_{x,\max} = \frac{8Fc\cdot 12}{b^4}\cdot\frac{b}{2} \le \sigma_\text{zul}: \qquad 245{,}8\,\frac{\text{N}}{\text{mm}^2} \not\le 240\,\frac{\text{N}}{\text{mm}^2}$$

(rot:) $\curvearrowright$ mit gegebenem Profil wird zulässige Spannung überschritten (→ $d < 0$ $\curvearrowright$ Quatsch)

[Prüfung: $48\cdot 160\cdot 32/1000 = 245{,}76$ ✓.]

**Erweiterung**
mit $\dfrac{N}{A} + \dfrac{M}{I}z$
→ $a$ von Lsg. unten [?] prüfen, ob $\sigma_x \le \sigma_\text{zul}$ für $a_\text{Lsg}$?

[Prüfung: Für $a = 8\,\text{mm}$ an der Ecke: $N/A = 160/64 = 2{,}5\,\text{N/mm}^2$ → $\sigma = 242{,}5 > 240\,\text{N/mm}^2$ (knapp überschritten). Bei $3c$ mit $a = 6{,}35\,\text{mm}$: $160/40{,}3 = 4{,}0\,\text{N/mm}^2$ → $244\,\text{N/mm}^2$, ebenfalls knapp überschritten.]

## Seite 29

**Aufgabe Lineal**

> Skizze: Lineal (räumlich), Länge $300$ (mm, grün bemaßt), Querschnitt $2 \times 30\,\text{mm}$. Daneben zwei Hände, die das Lineal an den Enden fassen und gegensinnig biegen (Drehpfeile).

Berechnung der Biegespannung für <u>flach</u>/<u>hochkant</u> Biegung per Hand

**Lös.:** Lastfall

> Skizze links: Balken der Länge $L$, an beiden Enden von oben gehalten (Lager $A$ links, $B$ rechts), im Abstand $a$ von den Enden je eine Kraft $F$ nach oben (rot). Rechts gleichwertiges System: Kräfte $F$ an den Enden nach unten, zwei Auflager innen. (rot:) $F = 1\,\text{N}$.

Momentenverlauf:
Glgw. (Gleichgewicht)

> Skizze: Balken mit $A_H$ (→), $A_V$ (↓), $B$ (↓), zwei Kräfte $F$ (↑).

$$\rightarrow:\; \underline{A_H = 0}$$
$$\uparrow:\; 2F - A_V - B = 0$$
$$\curvearrowleft_A:\; F\cdot a + F(L - a) - B\cdot L = 0 \;\to\; \underline{B = F}, \quad \underline{A_V = F}$$

## Seite 30

Schnittgrößen: hier nur für Momente! (Vereinfachung)

> Skizze: Balken mit $F$ (↓) an beiden Enden und $F$ (↑) an den inneren Punkten; Koordinaten $x_1$, $x_2$, $x_3$ jeweils ab Bereichsanfang; grüne Umrandungen I, II.

**I** (Teilstück mit Endkraft $F$):
$$M_{y1} + F\,x_1 = 0 \;\to\; \underline{M_{y1} = -F\,x_1}$$

**II** (mit Endkraft $F$ und innerer Kraft $F$):
$$M_{y2} + F(a + x_2) - F\,x_2 = 0 \;\to\; \underline{M_{y2} = -F\,a}$$

**III** (mit Endkraft und beiden inneren Kräften):
$$M_{y3} + F(L - a + x_3) - F(L - 2a + x_3) - F\,x_3 = 0$$
$$M_{y3} + F(a - x_3) = 0 \;\to\; \underline{M_{y3} = -F(a - x_3)}$$

> Skizze $M$: Trapez $\ominus$; von $0$ an den Enden linear auf $-F a$ an den inneren Kraftangriffspunkten, dazwischen konstant $-F a$.

$\curvearrowright$ $|M_{\max}| = F\cdot a$ – konstant zwischen inneren Kräften

[Prüfung: korrekt (Mittelbereich: reine Biegung).]

## Seite 31

$$\sigma_{x,\max}(z,x) = \frac{M_{\max}}{I_{yy}}\,z, \qquad z_{\max} = \frac{h}{2}, \qquad I_{yy} = \frac{b h^3}{12}$$

① flach

> Skizze: Querschnitt liegend, Breite $b = 30$, Höhe $h$ (= 2), Achsen $y$, $z$.

$$\sigma^{\text{flach}}_{x,\max} = \frac{F a\cdot 12}{b h^3}\cdot\frac{h}{2} = \frac{6}{b h^2}\,F a$$

$a = 40\,\text{mm}$, $F = 1\,\text{N}$:
$$\to\; \sigma^{\text{flach}}_{x,\max} = \frac{6}{120\,\text{mm}^2}\cdot 1\cdot 40\,\text{mm} = 2\,\frac{\text{N}}{\text{mm}^2}$$
(zuerst $4$, korrigiert auf $2$)

② hochkant

> Skizze: Querschnitt stehend, Breite $b$ (= 2), Höhe $h$ (= 30), Achsen $y$, $z$.

$$\sigma^{\text{hochkant}}_{x,\max} = \frac{6\,F a}{b h^2} = \frac{6\cdot 1\,\text{N}\cdot 40\,\text{mm}}{2\cdot 30^2\,\text{mm}^3} = 0{,}13\,\frac{\text{N}}{\text{mm}^2}$$

⇒ bei gleicher Belastung ~~gleiche~~ [unterschiedliche] Spannung! (Verformung auch unterschiedlich)
↓ ③

[Prüfung: $240/120 = 2{,}0$ ✓; $240/1800 = 0{,}133$ ✓. Einheit im Nenner von ① müsste $\text{mm}^3$ lauten ($b h^2 = 30\cdot 2^2 = 120\,\text{mm}^3$). Der Wert $a = 40\,\text{mm}$ wird erst hier festgelegt.]

## Seite 32

> Skizze oben: Stark gekrümmtes dickes Balkenstück (Höhe $h_1$), Krümmungsradius $r$; oben „Stauchung", unten „Dehnung" (Längenänderungen der Randfasern bemaßt).
> Rechts daneben: $r$ klein; $\curvearrowright$ bei $h$ groß auch Dehnung groß ↓ $\sigma\uparrow$.

> Skizze Mitte: Dünneres Balkenstück (Höhe $h_2 < h_1$), gleicher Radius $r$, kleinere Randfaser-Dehnung; „Dehnung $\varepsilon$ ($\sigma = E\cdot\varepsilon$)".
> Text: $r$ muss groß sein, damit bei $h_2 < h_1$ die gleiche Dehnung erreicht wird.

(Der obere Teil der Seite ist mit einer Diagonale durchgestrichen; links senkrecht notiert: „passt nicht mehr" [?].)

**Variation der Aufgabe:** mit ~~Dreieck~~ Dreieck – Variation $I_{yy} = I_{yy}(x)$ für Bereich in der Mitte – $\sigma_x(x)$?

> Skizze: Draufsicht Lineal-Mittelbereich als Dreieck, Breite $b(x) = x$, Höhe der Spitze $80$, halbe Basis $80$ (mm).
> Skizze: $M$-Verlauf (Trapez, konstant $F a$ im Mittelbereich); darunter $\sigma$-Verlauf: U-förmig, Minimum $0{,}75\,\text{N/mm}^2$ in der Mitte, zu den Rändern des Bereichs gegen unendlich.

$$\sigma = \frac{6\,F a}{b(x)\,h^2} = \frac{1}{x}\cdot\frac{6 F a}{h^2}, \qquad b(x) = x, \quad x = 0 \ldots 80$$
(rot:) $\infty$ bei $x = 0$!

[Prüfung: Mit $h = 2\,\text{mm}$, $F a = 40\,\text{Nmm}$: $\sigma = 60/x$, bei $x = 80\,\text{mm}$ $\sigma = 0{,}75\,\text{N/mm}^2$ ✓.]

---

## Didaktische Gliederung

1. **Einführung Biegung (S. 1):** Definition (Krümmungsänderung der Stabachse), Begriff Balken; Abgrenzung zu Zug/Druck.
2. **Einteilung nach Querkraft (S. 1–2):** reine Biegung ($Q = 0$, $M = \text{konst.}$, aus $dM/dx = Q$) vs. Querkraftbiegung; Beispiel Vierpunkt-Biegung (Bereiche A/B).
3. **Einteilung nach Momentenvektor (S. 2–4):** einfache Biegung (Vektor ∥ Hauptachse), zweifache Biegung ($\vec M = \vec M_y + \vec M_z$), allgemeine schiefe Biegung (Achsen ≠ Hauptachsen; Verweis auf Literatur).
4. **Spannungen bei einfacher Biegung (S. 4–11):**
   - Biegespannungen sind Normalspannungen (Zug/Druck im Querschnitt).
   - Voraussetzungen: prismatisch, gerade Achse, reine Biegung; Näherung für schwach gekrümmte Balken, veränderliche Querschnitte, Querkraftbiegung.
   - Verformungsannahmen: Krümmung in $x$-$z$-Ebene, keine Querkontraktion, **Bernoulli-Hypothese** (Querschnitte bleiben eben).
   - Kinematik: neutrale Faser, $\varepsilon_x = z/\rho_0$ (Bogenmaß).
   - Hooke (einachsig): $\sigma_x = E z/\rho_0$.
   - Drei Äquivalenzbedingungen: $N = 0 \Rightarrow S_y = 0$ (neutrale Faser durch Schwerpunkt); $M_y = \frac{E}{\rho_0}I_{yy}$ ⇒ $\frac{1}{\rho_0} = \frac{M_y}{E I_{yy}}$ (3.2.1); $M_z = 0 \Rightarrow I_{yz} = 0$ (Hauptachsen).
   - **Biegespannungsformel** $\sigma_x = \frac{M_y}{I_{yy}}z$ (3.2.2), erweitert auf $\sigma_x(x,z) = \frac{M_y(x)}{I_{yy}(x)}z$.
5. **Anwendung Querschnittsvergleich (S. 12–16):** Kreis/Ring/Rechteck bei gleicher Randspannung, Materialaufwand, Widerstandsmoment; Träger gleicher Festigkeit.
6. **Wiederholung/Zusammenfassung (S. 17–18).**
7. **Spannungsverlauf längs und quer (S. 19–22):** 3-Punkt-Biegung; $\sigma$-Verlauf entlang $x$ affin zu $M$; Maximum in Randfasern; **Widerstandsmoment** $W_y = I_{yy}/z_{\max}$, $\sigma = M_y/W_y$, $W_\square = bh^2/6$.
8. **Bemessung (S. 23–28):** Rahmen – Querschnittsbemessung ($a$, $d$) über $\sigma_{\max} \le \sigma_\text{zul}$; zusammengesetzte Flächen; Grenzfall nicht lösbar; Ausblick $N/A + Mz/I$.
9. **Anschauungsbeispiel Lineal (S. 29–32):** flach vs. hochkant, Krümmungsradius vs. Höhe, veränderliche Breite.

**Rechenschema Biegespannung (wie im Skript angewandt):**
1. Lagerreaktionen aus Gleichgewicht.
2. Schnittgrößen bereichsweise ($N$, $Q$, $M_y$), Verläufe zeichnen, $M_{\max}$ bestimmen.
3. Querschnittswerte: Schwerpunkt, $I_{yy}$ (ggf. zusammengesetzt), $z_{\max}$ bzw. $W_y$.
4. $\sigma_x = \frac{M_y}{I_{yy}}z$ bzw. $\sigma_{\max} = \frac{M_{\max}}{W_y}$; Vorzeichen → Zug/Druck.
5. Bemessung/Nachweis: $\sigma_{\max} \le \sigma_\text{zul}$ nach gesuchter Größe auflösen.

**Wichtige Definitionen:** Biegung, Balken, reine Biegung, Querkraftbiegung, einfache/zweifache/schiefe Biegung, neutrale Faser/Schicht, Krümmungsradius $\rho_0$, Bernoulli-Hypothese, statisches Moment $S_y$, Flächenträgheitsmoment $I_{yy}$, Deviationsmoment $I_{yz}$, Widerstandsmoment $W_y$, Träger gleicher Festigkeit.

## Beispiele

| Nr. | System | Gegeben | Ergebnisse | Seite |
|---|---|---|---|---|
| 1 | Einfeldträger, zwei Lasten $F$ im Abstand $a$ von den Lagern (qualitativ) | $F$, $a$ | Bereiche Querkraftbiegung / reine Biegung; $M = \text{konst.}$ in Mitte | 2 |
| 2 | Kragträger, Einzelkraft am Ende; Kreis vs. Kreisring ($d_i = 0{,}9 d_a$) vs. Rechteck ($b = d$) | $F, L, d$ | $M_{\max} = -FL$; $\sigma_\text{Kreis} = \pm FL/(0{,}0982 d^3)$; $\sigma_\text{Ring} = \pm FL/(0{,}0338 d_a^3)$; $d_a = 1{,}427d$, $d_i = 1{,}284d$; $V_\text{Kreis}/V_\text{Ring} = 2{,}58$; Rechteck $h = 0{,}77d$, $A_\square \approx A_\circ$ | 12–15 |
| 3 | Kragträger, Träger gleicher Festigkeit (Rechteck, $b$ konst.) | $F, L, b_L, h_L$ | $h(x) = h_L\sqrt{x/L}$; $\sigma = 6FL/(b_L h_L^2)$ konst. | 16 |
| 4 | 3-Punkt-Biegung, Einfeldträger, $F$ mittig, Rechteck $b \times h$ | $F, L, b, h$ | $A_V = B = F/2$; $Q = \pm F/2$; $M_{\max} = FL/4$; $\sigma_{\max} = \frac{3}{2}\frac{FL}{bh^2}$; $\sigma(z) = 3FLz/(bh^3)$ | 19–22 |
| 5 | U-Rahmen (Stiele $6c$/$3c$, Riegel $4c$), $2F$ horizontal, $F$ vertikal | $F = 160\,\text{N}$, $c = 32\,\text{mm}$, $b = 10\,\text{mm}$, $\sigma_\text{zul} = 240\,\text{N/mm}^2$ | $A_H = \frac23F$, $A_V = -F$, $B = \frac83F$; $M$: $4Fc$ (linke Ecke), $8Fc$ (rechte Ecke); $a \ge 6{,}35\,\text{mm}$ (bei $3c$), $a \ge 8\,\text{mm}$ (an Ecke); $d \le 7{,}92\,\text{mm}$ (bei $2c$); bei $8Fc$ Vollquadrat $245{,}8 > 240\,\text{N/mm}^2$ | 23–28 |
| 6 | Lineal $300 \times 30 \times 2\,\text{mm}$, Handbiegung (4-Punkt) | $F = 1\,\text{N}$, $a = 40\,\text{mm}$ | $|M_{\max}| = Fa$; flach $\sigma = 2\,\text{N/mm}^2$; hochkant $0{,}13\,\text{N/mm}^2$; Variante Dreiecksbreite: $\sigma = 60/x$, min. $0{,}75\,\text{N/mm}^2$ | 29–32 |

**Befunde der Nachrechnung (Zusammenfassung):** Alle Endergebnisse stimmen. Kleinere Unstimmigkeiten: S. 10 fehlendes Minus bei $I_{yz}$-Term; S. 13 Vorzeichen $\pm$ statt $\mp$; S. 20 Beschriftung $+F/2$ statt $-F/2$ im $Q$-Verlauf Bereich II; S. 22 $I_{yz}$ statt $I_{yy}$ [?] in $W_y$; S. 26 gesucht war $a$ bei $3c$ ($6{,}35\,\text{mm}$), zusätzlich $8\,\text{mm}$ an der Ecke; S. 31 Einheit $\text{mm}^2$ statt $\text{mm}^3$; S. 28 Erweiterung um $N/A$ führt zu knapper Überschreitung von $\sigma_\text{zul}$ (≈ $242$–$244\,\text{N/mm}^2$).

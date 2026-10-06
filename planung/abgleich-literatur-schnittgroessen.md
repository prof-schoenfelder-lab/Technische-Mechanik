# Abgleich Vorlesung „Schnittgrößen“ mit der Literatur

Stand: 2026-10-06

Geprüft:

- `kurs/vorlesung/03-schnittgroessen.qmd` (im Folgenden **VL**), inkl. der Grafiken `grafiken/schnittgroessen/{vorzeichen,traeger-einzelkraefte,einfeldtraeger-dreieckslast}.svg`
- `kurs/quellen-transkript/3-Schnittgroessen.md` (im Folgenden **Transkript**, Vorlesung 2013)

Literatur (Seitenangaben = gedruckte Buchseiten, in Klammern PDF-Seite):

- **Gross**: Gross/Hauger/Schröder/Wall, *Technische Mechanik 1 – Statik*, 11. Aufl. 2011, Kap. 7 „Balken, Rahmen, Bogen“, S. 171–215 (PDF 180–224; PDF = Buchseite + 9)
- **Dankert**: J. Dankert/H. Dankert, *Technische Mechanik*, 7. Aufl. 2013, Kap. 7 „Schnittgrößen“, S. 93–108 (PDF 111–126; PDF = Buchseite + 18)

---

## 1. Vergleich von Definitionen, Konventionen, Bezeichnungen und Herleitungen

### 1.1 Übersicht

| Punkt | VL / Transkript | Gross | Dankert |
|:--|:--|:--|:--|
| Bezeichnungen | $N$, $Q$, $M$ (Transkript: $F_N$, $F_Q$ durchgestrichen → $N$, $Q$; $M_B$) | $N$, $Q$, $M$ (S. 172) | $F_N$, $F_Q$, $M_b$ (S. 93) |
| Längskoordinate | $x$ nach rechts, $z$ nach unten | $x$ nach rechts, $z$ nach unten, $y$ aus der Ebene heraus (Rechtssystem), S. 172 Abb. 7.3 | **$z$** ist die Längskoordinate (S. 93, Abb. auf S. 93/97); Querschnittsachsen sind $x$, $y$ |
| Lagerreaktionen | $F_{AH}$, $F_{AV}$, $F_B$ | $A_H$, $A_V$, $B$ (S. 174) | $F_{AH}$, $F_{AV}$, $F_B$ (S. 98) – wie VL |
| Positives Schnittufer | äußere Normale in $+x$, „auf der Koordinatenseite“ | äußere Normale $\vec n$ in $+x$ (S. 172 f., Abb. 7.3) | „Schnittufer auf der Koordinatenseite“ (S. 93) |
| Vorzeichenregel | $N$ Zug, $Q$ am pos. Ufer nach unten, $M$ so, dass untere Faser auf Zug | **eine** Regel für alle drei: positive Schnittgrößen zeigen am positiven (negativen) Ufer in positive (negative) Koordinatenrichtung; $M$ als Momentenvektor in $y$-Richtung (Rechtsschraube), S. 173 | wie VL, über „untere Faser auf Zug“ (S. 94) |
| Rahmen | Transkript S. 3, 19, 21: $z_i$ zur Rahmeninnenseite („gestrichelte/untere Faser“); VL: fehlt | „gestrichelte Faser“ als Unterseite, $x$ entlang, $z$ zur gestrichelten Seite (S. 173 f., Abb. 7.4) | „Bezugsfaser“, gestrichelt (S. 94); Empfehlung: Koordinaten gleichsinnig, Bezugsfaser innen (S. 95, Abb. 7.3/7.4) |
| Auftrag der Verläufe | VL: positive Werte oberhalb der Achse (Schritt „Normalkraftverlauf“) | positiv nach oben, Achsen mit Pfeil und ⊕/⊖ (Abb. 7.5e, 7.7c, 7.11); beim Rahmen positiv auf der der gestrichelten Faser **abgewandten** Seite (Abb. 7.23c) | positiv „nach oben“ bzw. auf der der Bezugsfaser gegenüberliegenden Seite (S. 96 f.) |
| Bereichseinteilung | 6 Regeln (Anfang, Einzellasten, Beginn/Ende und Unstetigkeit von $q$, Lager, Ecken/Verzweigungen) | Schnitt „zwischen Einzelkräften“, nicht an der Kraftangriffsstelle (S. 175); bei Integration: Felder bei Unstetigkeit von $q$, am lastfreien Gelenk **keine** Teilung nötig (S. 193, B7.6) | praktisch identische Liste wie VL (S. 94) |
| Rechenschema | 4 Schritte („Kochrezept“) | Zusammenfassung S. 215: Schnitt → KOS → Freikörperbild mit **positiv** eingezeichneten Schnittgrößen → 3 GGB → auflösen | kein nummeriertes Schema; Empfehlung: Kraft-GGB in $N$- und $Q$-Richtung + Momente um die Schnittstelle (S. 94) |
| Differentialbeziehungen | Element $\mathrm dx$, Momente um (implizit) rechtes Ufer, $\mathrm dx^2 \to 0$ | Element $\mathrm dx$, $q\,\mathrm dx$ als Einzellast $\mathrm dF$, Momente um rechten Rand $C$, Glied mit $\mathrm dx\cdot\mathrm dx$ „klein von höherer Ordnung“ (S. 183 f., Gl. 7.4–7.8) | Element $\Delta z$, Momente um Elementmitte, Grenzübergang $\Delta z \to 0$ (S. 99, Gl. 7.1) |
| Integrationsmethode | VL: ein Feld, RB $M(0)=M(L)=0$ | Integration + Randbedingungstabelle (7.11) S. 186; Übergangsbedingungen S. 190–192; Föppl-Symbol S. 196–200; punktweise Ermittlung S. 200–204 | keine Integrationsmethode; stattdessen Kontrollregeln und „Zeichnen ohne Rechnung“ (Kap. 7.3, S. 103–107) |

### 1.2 Unterschiede im Einzelnen

1. **Vorzeichenregel für $M$.** VL und Dankert (S. 94) definieren $M$ anschaulich über die gezogene untere Faser. Gross (S. 173) definiert dagegen alle drei Schnittgrößen über eine einzige Regel, mit $M$ als Momentenvektor um $+y$. Beide Definitionen sind gleichwertig. Die Gross-Regel lässt sich leichter auf Rahmen, Bögen und räumliche Tragwerke übertragen; die VL-Regel ist anschaulicher. Für die VL passt die anschauliche Form, ein Satz zur Gross-Regel als Merkhilfe wäre aber nützlich (siehe Vorschlag 3.2).
2. **$x$ nach links.** Gross (S. 173, Beispiel 7.4 auf S. 190) weist darauf hin: Zeigt $x$ nach links, dreht sich nur die positive Richtung von $Q$ um, $N$ und $M$ bleiben gleich. In der VL fehlt das. Für Kragarme lohnt sich der Hinweis, weil Studierende dort gern von der freien Seite aus zählen.
3. **Längskoordinate bei Dankert ist $z$.** Wer parallel mit Dankert lernt, stolpert darüber (Dankert benutzt $z$ wegen der späteren Festigkeitslehre). Ein Satz in der VL oder auf der Literaturseite genügt.
4. **Rahmen und gestrichelte Faser bzw. Bezugsfaser.** Im Transkript sind sie da (S. 3: Koordinaten $x_6$/$z_6$ im Stiel; Rahmenbeispiel S. 17–23), in der VL fehlen sie ganz. Die Regel aus dem Transkript ($z$ zeigt zur Rahmeninnenseite, $x$ läuft gleichsinnig ums Tragwerk) entspricht genau der Empfehlung von Dankert (S. 95) und der gestrichelten Faser bei Gross (S. 173 f.).
5. **Auftrag der Verläufe beim Rahmen: Widerspruch im Transkript.** Beim Balken (Transkript S. 8, VL) werden positive Werte oben aufgetragen, also auf der Seite **gegenüber** der Bezugsfaser. Das stimmt mit Gross und Dankert überein. Beim Dreigelenkrahmen (Transkript S. 22) ist das positive Feldmoment dagegen „unten/innen“ eingezeichnet, also **auf** der Bezugsfaserseite, und negative Momente liegen außen. Damit trägt das Transkript beim Rahmen auf der Zugseite auf, beim Balken aber auf der Druckseite. Bevor ein Rahmen in die VL kommt, muss eine Konvention festgelegt werden (Empfehlung siehe 3.13).
6. **Momentenbezugspunkt am Element.** Die VL schreibt „$\curvearrowleft:$“ ohne Bezugspunkt. Das Ergebnis stimmt nur, wenn um das rechte Ufer (bzw. um den Angriffspunkt von $Q+\mathrm dQ$) summiert wird. Das Transkript nennt den Punkt ($S_2$, S. 10), Gross nennt ihn $C$ (S. 184), Dankert nimmt die Elementmitte (S. 99). Empfehlung: in der VL „$\curvearrowleft S_2$ (rechtes Ufer)“ schreiben.
7. **Bereichseinteilung.** Die VL-Liste ist ein Rezept für die Schnittmethode und stimmt mit Dankert (S. 94) überein. Gross ergänzt, dass bei der Integration an einem lastfreien Gelenk **keine** neue Bereichsgrenze nötig ist, weil die Verläufe dort stetig sind (S. 193). Beides widerspricht sich nicht, man sollte die Listen aber nicht als „Pflicht“-Grenzen verkaufen.
8. **Lagerreaktionen nicht immer nötig.** Gross zeigt zwei Ausnahmen: beim Kragträger (Teilsystem am freien Ende, S. 181) und bei der Integration, wo die Reaktionen aus $Q$ und $M$ an den Rändern abgelesen werden (S. 186, 188). Schritt 1 des VL-Rezepts lässt sich deshalb mit „in der Regel“ abschwächen.
9. **Rechenschema.** Ein ausdrücklicher Hinweis fehlt in der VL: Schnittgrößen werden **immer in positiver Richtung** eingezeichnet, das Vorzeichen des Ergebnisses ergibt sich dann aus der Rechnung. Im Transkript steht er (S. 2: „wie Lagerreaktionen behandeln“), bei Gross ebenfalls (S. 174, S. 215). Das ist die häufigste Fehlerquelle.
10. **Tabelle der Differentialbeziehungen.** Die Tabelle der VL deckt sich mit Gross S. 185 und S. 192. Zwei Dinge fehlen: (a) eine Zeile „Sprung in $q$ (Beginn/Ende einer Streckenlast) → $Q$ mit Knick, $M$ ohne Knick“ (Gross S. 191 f.; Dankert S. 101); (b) bei der Einzelkraft ist nur die **Querkomponente** maßgeblich. Die Längskomponente erzeugt einen Sprung in $N$ (Gross S. 175).

---

## 2. Nachrechnung der Formeln und Zahlenwerte der VL

### 2.1 Vorzeichen-Grafik (`vorzeichen.svg`)

- Positives Ufer: $N \to$, $Q \downarrow$, $M$ gegen den Uhrzeigersinn (Drehung um $+y$, wobei $y$ aus der Ebene zeigt). **Richtig.** Das entspricht Gross Abb. 7.3 und Dankert S. 97.
- Negatives Ufer: alles entgegengesetzt. **Richtig.**
- Hinweis zum Transkript: In der „Didaktischen Gliederung“ (Z. 635) steht „am pos. Ufer im Uhrzeigersinn“, und auf S. 2 (Z. 52) „im Uhrzeigersinn [?]“. Beides ist **falsch**. Am positiven Ufer dreht das positive $M$ gegen den Uhrzeigersinn. Die VL-Grafik ist korrekt, das Transkript sollte korrigiert werden.

### 2.2 Beispiel Träger mit Kragarm

Gegeben: $F_1 = 2000$ N, $F_2 = 500$ N, $\alpha = 30^\circ$, $a = 1$ m. $F_1$ wirkt nach links unten.

| Größe | VL | Nachrechnung | ok? |
|:--|:--|:--|:-:|
| $F_{AH} = F_1\cos\alpha$ | 1732 N | 1732,05 N | ✓ |
| $F_B = (F_1\sin\alpha + 4F_2)/3$ | 1000 N | (1000 + 2000)/3 = 1000 N | ✓ |
| $F_{AV} = F_1\sin\alpha + F_2 - F_B$ | 500 N | 500 N | ✓ |
| $N_I = -F_{AH}$ | −1732 N (Druck) | ✓, physikalisch plausibel ($F_1$ drückt in Richtung A) | ✓ |
| $Q_I$, $M_I$ | $500$ N, $F_{AV}x_1$ | ✓ (Momentenrichtung mit Grafik konsistent) | ✓ |
| $N_{II}$ | 0 | ✓ | ✓ |
| $Q_{II}$ | −500 N | 500 − 1000 = −500 N | ✓ |
| $M_{II}(0)$, $M_{II}(2a)$ | 500 Nm, −500 Nm | 500; 1500 − 2000 = −500 | ✓ |
| $N_{III}$, $Q_{III}$, $M_{III}$ | 0; 500 N; $-F_2(a-x_3)$ | ✓; $M_{III}(0) = -500$ Nm (stetig zu Bereich II) | ✓ |
| Sprünge von $Q$ | an $F_1$: 1000 = $F_1\sin\alpha$; an B: 1000 = $F_B$; am Ende: 500 → 0 | ✓ | ✓ |

**Inhaltliche Fehler bzw. Unschärfen im Text:**

1. Schritt „④ Momentenverlauf“: Der Satz „An den gelenkigen Lagern und am freien Ende ist $M = 0$“ ist **falsch**, denn bei B (Loslager, also gelenkig) ist $M = -500$ Nm. Richtig ist: $M = 0$ an gelenkigen Lagern **am Trägerende** und am freien Ende (Gross S. 178; Dankert S. 105).
   Vorschlag: „Am Endauflager A und am freien Kragarmende ist $M = 0$. Über dem Lager B ist $M \neq 0$: Der Kragarm hängt dort am Träger (Stützmoment).“
2. „Das betragsmäßig größte Moment tritt bei B auf: $|M| = 500$ Nm“ ist unvollständig, denn auch unter $F_1$ ist $M = +500$ Nm. Der Betrag ist an beiden Stellen gleich, das Vorzeichen verschieden (Feldmoment bzw. Stützmoment).
   Vorschlag: „Die betragsgrößten Momente treten unter $F_1$ ($+500$ Nm, unten gezogen) und über B ($-500$ Nm, oben gezogen) auf. An beiden Stellen wechselt $Q$ sein Vorzeichen.“ Damit ist gleich die Brücke zur Extremwertregel geschlagen.
3. „Was fällt auf?“: Der erste Punkt sollte ergänzt werden, damit er auch die Normalkraft abdeckt: „… springt $Q$ um die Querkomponente, $N$ um die Längskomponente der Kraft.“ Das Lager B und die Kraft $F_2$ sind ebenfalls Einzelkräfte. In der Grafik `bezug` ist der Knick nur bei $F_1$ beschriftet; er sollte auch bei B stehen.
4. Kleinigkeit: In Bereich II stehen nur Ergebnisse, die Gleichgewichtsbedingungen fehlen (Bereich I und III zeigen sie). Aus didaktischen Gründen sollte man sie wie im Transkript S. 6 mit angeben.

### 2.3 Dreieckslast und Differentialbeziehungen

- Element: $\downarrow$: $-Q + q\,\mathrm dx + Q + \mathrm dQ = 0 \Rightarrow Q' = -q$ ✓. Momente um das rechte Ufer: $-M + M + \mathrm dM - Q\,\mathrm dx + q\,\mathrm dx^2/2 = 0 \Rightarrow M' = Q$ ✓. Der Bezugspunkt fehlt im Text (siehe 1.2 Nr. 6). Die Drehpfeile in der Grafik `element` sind richtig (links im Uhrzeigersinn, rechts gegen den Uhrzeigersinn).
- $F_A = q_0L/6$, $F_B = q_0L/3$ ✓ (Resultierende $q_0L/2$ bei $2L/3$).
- $Q(x) = -q_0x^2/(2L) + C_1$, $M(x) = -q_0x^3/(6L) + C_1x + C_2$ ✓; $C_2 = 0$, $C_1 = q_0L/6$ ✓.
- $Q(L) = -q_0L/2 + q_0L/6 = -q_0L/3$ ✓.
- $x_0 = L/\sqrt3 \approx 0{,}577\,L$ ✓.
- $M_\text{max} = \dfrac{q_0L^2}{6\sqrt3}\left(1-\tfrac13\right) = \dfrac{q_0L^2}{9\sqrt3} \approx 0{,}0642\,q_0L^2$ ✓. Im Transkript steht hier der falsche Wert 0,128; die VL ist korrekt.
- Anfangssteigung von $M$ gleich $Q(0) = q_0L/6$ ✓. In der Grafik liegt der Nulldurchgang von $Q$ und das Maximum von $M$ bei $x \approx 374$ px, das entspricht $0{,}577\,L$ ✓.
- Formulierung „Statt Bereiche zu schneiden, können wir … durch Integration gewinnen“: missverständlich. Auch bei der Integration braucht man bei unstetiger Last Bereiche plus Übergangsbedingungen (Gross S. 190 ff.). Besser: „Statt an jeder Stelle neu zu schneiden …“.
- Lagerung: Laut Transkript S. 13 liegt das Festlager rechts ($F_{BH}$). Für das Ergebnis spielt das keine Rolle; Grafik und Text sollten nur zueinander passen.

### 2.4 Zusammenfassungstabelle

Die Tabelle ist korrekt. Ergänzt werden sollte: „Einzelkraft → Sprung um die **Querkomponente** $F_\perp$ (in $N$: Sprung um die Längskomponente)“ sowie die Zeile „Beginn/Ende einer Streckenlast: $Q$ mit Knick, $M$ glatt“.

### 2.5 Fehler im Transkript (für Seminar/Notebook relevant, nicht in der VL)

- S. 5: Die Gleichung $\uparrow$ ist mit $+F_2$ notiert, richtig ist $-F_2$. Das Ergebnis stimmt (im Transkript bereits vermerkt).
- S. 13: $M_\text{max} \approx 0{,}128\,q_0L^2$ ist falsch, richtig ist $0{,}0642\,q_0L^2$.
- S. 16/17: $M_\text{max} = \tfrac{11}{48}q_0L^2$ ist falsch, nachgerechnet ergibt sich $\tfrac{5}{48}q_0L^2 \approx 0{,}104\,q_0L^2$:
  $M(L/2) = 4q_0L^2\left(\tfrac{1}{192} - \tfrac{1}{48}\right) + \tfrac{q_0L^2}{6} = \tfrac{-12 + 32}{192}q_0L^2$.
- Dreigelenkrahmen S. 17–23: nachgerechnet. $F_{AH} = 0{,}5\,q_0a$ (→), $F_{AV} = 1{,}5\,q_0a$, $F_{BH} = 2{,}5\,q_0a$ (←), $F_{BV} = 6{,}5\,q_0a$, Eckmomente $-6\,q_0a^2$ und $-20\,q_0a^2$, Feldmaximum $\tfrac98 q_0a^2$ bei $x_3 = 1{,}5a$, $M = 0$ im Gelenk: alles ✓. Das Beispiel kann so übernommen werden; nur die Auftragsseite muss geklärt werden (1.2 Nr. 5).
- Z. 635 und Z. 52: Drehsinn von $M$ (siehe 2.1).

---

## 3. Vorschläge für Ergänzungen der VL

Priorität: **A** = sollte rein, **B** = sinnvoll, **C** = optional/Vertiefung.

### 3.1 Schnittgrößen als Resultierende der Spannungen (A)

- **Warum:** Die VL sagt, *dass* drei Größen übertragen werden, aber nicht, *was* sie physikalisch sind. Das ist die Brücke zur Festigkeitslehre.
- **Quelle:** Gross S. 171 f., Abb. 7.1; Transkript S. 1 (Skizze mit Spannungspfeilen).
- **Formulierung:** „In Wirklichkeit wird über die ganze Schnittfläche eine verteilte Flächenkraft übertragen, die Spannung. Für die Statik genügt ihre Wirkung, zusammengefasst im Schwerpunkt des Querschnitts: Die Komponente senkrecht zur Schnittfläche ist $N$, die Komponente in der Schnittfläche ist $Q$, und das resultierende Moment ist $M$. Wie sich die Spannungen über den Querschnitt verteilen, klärt später die Festigkeitslehre.“

### 3.2 „Immer positiv antragen“ und die Kurzregel (A)

- **Warum:** häufigste Fehlerquelle; im Transkript vorhanden, in der VL nicht.
- **Quelle:** Gross S. 173 (Kurzregel), S. 174, S. 215; Transkript S. 2.
- **Formulierung (in Schritt 3 des Rechenschemas):** „Zeichnen Sie die Schnittgrößen am Schnittufer **immer in positiver Richtung** ein, auch wenn Sie schon ahnen, dass das Ergebnis negativ wird. Das Vorzeichen des Ergebnisses sagt Ihnen dann direkt: $N<0$ heißt Druck, $M<0$ heißt Zug oben.“ Merkhilfe nach Gross: „Am positiven Ufer zeigen positive Schnittgrößen in die positiven Koordinatenrichtungen, am negativen Ufer in die negativen.“

### 3.3 Anschauliche Deutung, Bezug zur Gebäudetechnik (A)

- **Warum:** Mit Vorzeichen allein können EGB-Studierende wenig anfangen. Ein Bild vom durchhängenden Balken hilft, Ergebnisse zu prüfen.
- **Quelle:** Dankert S. 106, Beispiel 4 (Vorzeichen von $M$ „aus der Anschauung“); Gross S. 171 (Schnittgrößen als Maß der Materialbeanspruchung).
- **Formulierung:** „Ein positives Moment krümmt den Balken wie eine durchhängende Decke: unten gezogen, oben gedrückt (Feldmoment). Ein negatives Moment tritt über Stützen und an Kragarmen auf, etwa bei einem Balkon oder einer Rohrkonsole; dann ist die Oberseite gezogen. Im Stahlbeton liegt die Bewehrung deshalb dort, wo die Momentenlinie Zug anzeigt. Prüfen Sie jedes Vorzeichen mit dieser Vorstellung.“

### 3.4 Kontrollregeln für Verläufe als Checkliste (A)

- **Warum:** Mit den Regeln lassen sich Ergebnisse prüfen und Verläufe ohne Rechnung skizzieren; sie sind klausurrelevant.
- **Quelle:** Dankert Kap. 7.3, S. 103–106; Gross S. 178, 184 f., 191 f.
- **Formulierung (Merke-Box):**
  - $Q$ ist konstant ohne Streckenlast und linear bei konstanter Streckenlast. An einer Einzelkraft springt $Q$ um deren Querkomponente, und zwar in Richtung der Kraft, wenn man in $+x$-Richtung läuft.
  - $M$ hat die Steigung $Q$: Bei $Q>0$ steigt $M$, bei $Q<0$ fällt $M$, wo $Q$ springt, hat $M$ einen Knick.
  - $M$ springt nur dort, wo ein Moment eingeleitet wird (Einzelmoment, Einspannung). Sonst ist $M$ stetig, auch über Ecken hinweg.
  - $M = 0$ am freien Ende, am gelenkigen Endlager und im Gelenk.
  - Probe am Ende: Der Querkraftverlauf muss am rechten Rand mit der letzten Kraft genau auf null zurückspringen. Bleibt ein Rest, stimmt das Gleichgewicht nicht.

### 3.5 Querkraftverlauf „mit den Kräften laufen“ (B)

- **Warum:** schnelle und anschauliche Methode, bei der man sofort sieht, wie Lasten und Verlauf zusammenhängen.
- **Quelle:** Dankert S. 103 f., Beispiele 1 und 2.
- **Formulierung:** „Bei reinen Einzellasten lässt sich der Querkraftverlauf ohne Rechnung zeichnen. Man startet links bei null und folgt jeder Kraft: Eine Kraft nach oben hebt die Linie um ihren Betrag, eine Kraft nach unten senkt sie. Zwischen den Kräften bleibt die Linie waagerecht. Am rechten Ende muss man wieder bei null ankommen; das ist zugleich die Probe für die Lagerreaktionen.“ Am Beispiel der VL: 0 → +500 → −500 → +500 → 0.

### 3.6 Wo liegt das größte Moment? Extremwerte auch an Bereichsgrenzen (A)

- **Warum:** Die VL nennt nur „$Q = 0$“. Im eigenen Beispiel 1 liegen die Maxima aber genau dort, wo $Q$ **springend** das Vorzeichen wechselt.
- **Quelle:** Gross S. 185; Dankert S. 105.
- **Formulierung:** „$M$ hat überall dort ein Extremum, wo $Q$ das Vorzeichen wechselt, sei es durch einen stetigen Nulldurchgang oder durch einen Sprung an einer Einzelkraft. Das betragsgrößte Moment kann außerdem an Bereichsgrenzen, an Lagern oder an Ecken liegen. Vergleichen Sie deshalb immer die Extremwerte innerhalb der Bereiche **und** die Werte an allen Bereichsgrenzen.“

### 3.7 Randbedingungen und Reaktionen bei der Integration (B)

- **Warum:** Die VL nutzt nur $M(0) = M(L) = 0$. Für den Kragarm und für Gelenkträger braucht man die Tabelle.
- **Quelle:** Gross S. 185–188, Tabelle (7.11), Abb. 7.11; Übergangsbedingungen S. 190–192, (7.14)–(7.17).
- **Formulierung:** „Welche Randbedingungen gelten, hängt vom Lager ab: Am gelenkigen Lager ist $M = 0$, am freien Ende $Q = 0$ **und** $M = 0$, an der Einspannung ist dagegen nichts null. Aussagen der Form ‚$\neq 0$‘ sind keine Randbedingungen. Umgekehrt kann man die Lagerkräfte am Ende aus dem Verlauf ablesen: $F_A = Q(0)$ und $F_B = -Q(L)$.“ Dazu passt Gross Abb. 7.11 (gleiche Last, drei Lagerungen) als kleine Grafik.

### 3.8 Typische Fehler (A)

- **Warum:** Die Fehler sind in beiden Büchern verstreut beschrieben, eine kompakte Liste hilft beim Üben.
- **Quellen:** Gross S. 175, S. 188, S. 173/190; Dankert S. 96 (Abb. 7.6/7.7), S. 106.
- **Formulierung (Liste):**
  1. Die Streckenlast wird **vor** dem Schnitt zur Resultierenden zusammengefasst. Erst schneiden, dann nur den Lastanteil am Teilsystem zusammenfassen (Gross S. 188).
  2. Ein Einzelmoment wird verschoben. Für die Lagerreaktionen ist das erlaubt, für den Momentenverlauf nicht (Dankert S. 106).
  3. Es wird genau an der Kraftangriffsstelle geschnitten. Dort ist $Q$ nicht eindeutig; immer knapp daneben schneiden (Gross S. 175).
  4. Die Momentenbilanz wird nicht um den Schnittpunkt $S$ gebildet. Dann tauchen $N$ und $Q$ in der Gleichung auf.
  5. Es wird nur das Bereichsstück betrachtet und die Schnittgrößen am anderen Bereichsende werden vergessen (Dankert S. 96, Abb. 7.7).
  6. Bei Koordinaten von rechts nach links wird nicht beachtet, dass sich das Vorzeichen von $Q$ umkehrt (Gross S. 173).

### 3.9 Beispiel mit Einzelmoment (B)

- **Warum:** In der Tabelle steht „Einzelmoment → Sprung in $M$“, ein Beispiel gibt es in der VL aber nicht.
- **Quelle:** Gross B7.2 (Kragträger, S. 180 f.) und B7.3 (S. 181–183); Dankert S. 106, Beispiel 5.
- **Formulierung:** „Ein eingeleitetes Moment ändert die Querkraft nicht; beide Geraden der Momentenlinie haben deshalb die gleiche Steigung. Die Momentenlinie springt an der Angriffsstelle um den Betrag des Moments. Für die Lagerkräfte ist es egal, wo das Moment angreift, für den Momentenverlauf nicht.“

### 3.10 Gelenkträger (Gerberträger) (B)

- **Warum:** Er kommt in der Praxis häufig vor (Pfetten, Durchlaufträger mit Gelenk) und ist eine einfache Anwendung von „$M = 0$ im Gelenk“.
- **Quelle:** Gross S. 192 f., Tabelle (7.17), B7.6 S. 194–196, B7.8 S. 202–204; Dankert S. 96 Abb. 7.6, S. 106 Beispiel 6.
- **Formulierung:** „Im Gelenk wird kein Moment übertragen, $M = 0$, eine Querkraft aber sehr wohl. Daraus folgt eine zusätzliche Gleichung, mit der sich die Gelenkkräfte bestimmen lassen. Den Momentenverlauf kann man oft ohne Rechnung zeichnen: Die Gerade vom Feldwert läuft durch den Nullpunkt im Gelenk bis zum nächsten Lager weiter, denn erst dort darf sie abknicken.“

### 3.11 Punktweise Ermittlung (B)

- **Warum:** Das ist das ökonomischste Verfahren für Klausur und Praxis: Werte nur an den Bereichsgrenzen ausrechnen und mit der passenden Kurvenform verbinden.
- **Quelle:** Gross Abschnitt 7.2.6, S. 200–204; Dankert S. 103 (Beispiel 2 c: bei linearen Verläufen genügt der Vergleich der Grenzwerte).
- **Formulierung:** „Oft braucht man keine Funktionen, sondern nur Werte. Man berechnet $Q$ und $M$ links und rechts jeder Bereichsgrenze und verbindet die Punkte mit Geraden oder Parabeln, je nachdem, was die Belastung im Bereich vorgibt. Bei Parabeln hilft $M' = Q$, um die Tangentenrichtung an den Enden festzulegen.“

### 3.12 Integrationsmethode mit mehreren Feldern / Föppl-Klammer (C)

- **Warum:** Die Föppl-Klammer ist elegant und passt gut zum Python/marimo-Notebook (dort entspricht sie `np.heaviside` bzw. `sympy.SingularityFunction`). Für EGB ist sie aber kein Pflichtstoff. Vorschlag: als aufklappbarer Exkurs oder nur im Notebook.
- **Quelle:** Gross Abschnitt 7.2.5, S. 196–200, Gl. (7.18)–(7.24), B7.7.
- **Formulierung:** „Die spitze Klammer $\langle x-a\rangle^n$ ist links von $a$ null und rechts davon gleich $(x-a)^n$. Damit lassen sich Lasten, die erst ab einer Stelle wirken, in **einer** Formel für den ganzen Balken schreiben, sodass keine Bereiche mehr nötig sind. Man integriert sie wie eine gewöhnliche Klammer; die Übergangsbedingungen sind dann automatisch erfüllt.“

### 3.13 Rahmen: Bezugsfaser, Ecken, Auftragsseite (A/B)

- **Warum:** Rahmen kommen in der Gebäudetechnik ständig vor (Hallenrahmen, Rohrbrücken, Konsolen). Das Transkript enthält ein vollständiges, nachgerechnetes Beispiel (Dreigelenkrahmen S. 17–23). In der Liste der Bereichsgrenzen nennt die VL „Ecken“ schon, erklärt sie aber nicht.
- **Quelle:** Gross S. 173 f. (gestrichelte Faser), S. 204–207 (Ecken, Gl. 7.25, B7.9); Dankert S. 94 f. (Bezugsfaser, Empfehlungen), S. 101–104 (Rahmenbeispiel, Abb. 7.13).
- **Formulierung:** „Bei Rahmen gibt es kein eindeutiges ‚unten‘. Wir markieren deshalb eine Seite jedes Stabes gestrichelt, die Bezugsfaser, am besten durchgehend auf der Innenseite. Sie übernimmt die Rolle der Unterseite: $z$ zeigt zu ihr hin, und positives $M$ zieht sie. An einer unbelasteten rechtwinkligen Ecke geht $M$ unverändert um die Ecke, während Normal- und Querkraft die Rollen tauschen.“
- **Entscheidung zur Auftragsseite (vorher klären):** Gross und Dankert tragen positive Werte auf der der Bezugsfaser **abgewandten** Seite auf. Das entspricht dem Balken mit „positiv oben“ und damit der VL. Das Transkript trägt beim Rahmen dagegen auf der Zugseite auf. Empfehlung: in der VL konsequent nach Gross/Dankert auftragen und **zusätzlich** in einem Satz erwähnen, dass Tragwerksplaner die Momentenlinie meist auf der Zugseite zeichnen (positives Feldmoment unten). Studierende der Gebäudetechnik begegnen dieser Darstellung später in Statiken und sollten sie nicht falsch lesen.

### 3.14 Hinweis zu Bezeichnungen in der Literatur (C)

- **Formulierung (Fußnote/Literaturkasten):** „Bei Dankert heißen die Schnittgrößen $F_N$, $F_Q$, $M_b$, und die Balkenachse ist $z$. Gross verwendet wie wir $N$, $Q$, $M$ und $x$, nennt die Lagerkräfte aber $A_H$, $A_V$, $B$ statt $F_{AH}$, $F_{AV}$, $F_B$. Die Vorzeichenkonvention ist in allen drei Fällen dieselbe.“

---

## 4. Abbildungsstil bei Gross (Stilreferenz)

Beobachtet an Abb. 7.2, 7.3, 7.5, 7.7, 7.11 und 7.23 (S. 172–206):

- **Balken:** schmales Rechteck, hellgrau gefüllt, schwarze Kontur. In Freikörperbildern teils nur als dicke schwarze Linie (Abb. 7.7b).
- **Lager:** Festlager als kleines Dreieck mit Gelenkkreis an der Spitze, darunter eine Bodenlinie mit kurzer Schrägschraffur. Loslager genauso, zusätzlich mit einem Strich zwischen Dreieck und Boden. Einspannung als senkrechte, schraffierte Wand (Abb. 7.8, 7.11). Die Schraffur ist kurz, dicht und unter 45°, nur auf einer Seite der Bodenlinie.
- **Kräfte:** alle Lasten **und** Reaktionen in Rot, gerade Pfeile mit gefüllter Spitze. Streckenlasten als rote Pfeilreihe mit Umrisslinie, die Fläche zart rot hinterlegt (Abb. 7.11). Beschriftung in roter Kursivschrift neben dem Pfeil ($F$, $q_0$, $A_V$).
- **Momente:** roter Kreisbogen (etwa ¾-Kreis) mit Pfeilspitze, um den Angriffspunkt gelegt.
- **Schnittufer:** Die Schnittfläche ist durch zwei kurze rote Querstriche markiert; der Normalenvektor $\vec n$ ist als kurzer grüner Pfeil mit Beschriftung „positives/negatives Schnittufer“ in Grün eingezeichnet (Abb. 7.3). Die Schnittlinie im Gesamtsystem ist grün gestrichelt mit dem Wort „Schnitt“, der Schnittpunkt $S$ grün (Abb. 7.5b,c). $N$, $Q$, $M$ sind rot, $M$ als Bogen um das Ufer.
- **Koordinaten:** kurzer blauer Pfeil $x$ (blaue Kursivschrift) unter dem Balken, oft mit Bemaßungsanfang. Das Achsenkreuz $x$, $y$, $z$ nur bei der Definition (Abb. 7.3), $y$ als Punkt im Kreis (aus der Ebene heraus).
- **Bemaßung:** schwarze Maßlinien mit Pfeilspitzen und senkrechten Begrenzungsstrichen, Maß kursiv in der Mitte ($a$, $b$, $l$).
- **Verläufe:** unter dem System, horizontal ausgerichtet. Jedes Diagramm hat eine eigene senkrechte Achse mit Pfeil und Kursivbeschriftung ($Q$, $N$, $M$); eine waagerechte Nullachse ist nur angedeutet. Flächen zart rosa/rot gefüllt mit roter Randlinie. Vorzeichen als ⊕/⊖ im Kreis mitten in der Fläche. Werte in Rot an den Ecken der Fläche, teils mit kleiner Hinweislinie. Schwarze, gestrichelte senkrechte Hilfslinien verbinden Lastangriffspunkte und Diagramme. Kurvenarten werden zusätzlich als Text angeschrieben („quadratische Parabel“, „kubische Parabel“, Abb. 7.13, 7.16). $M_\text{max}$ ist mit einer gestrichelten Linie zur Nullstelle von $Q$ verbunden (Abb. 7.11a).
- **Rahmen:** Die gestrichelte Faser ist grün gestrichelt auf der Innenseite. Bereichsnummern stehen als Ziffern im Kreis (①–④). Die Verläufe sind direkt an die Stäbe gezeichnet, je ein Bild für „N-Linie“, „Q-Linie“ und „M-Linie“ (Abb. 7.23c).
- **Beschriftung allgemein:** Teilbilder sind mit kleinen fetten Buchstaben a, b, c … in Blau unten links gekennzeichnet, die Abbildungsnummer steht in Blau („Abb. 7.5“) rechts unten. Formelzeichen kursiv (Serifenschrift), Ziffern aufrecht. Insgesamt sparsam: keine Rahmen, keine Schatten, nur Rot (Lasten/Schnittgrößen), Blau (Koordinaten/Labels), Grün (Schnitt/Fasern) und Schwarz/Grau (Geometrie).

Abgleich mit dem eigenen Stil: Die VL-Grafiken verwenden für $N$, $Q$, $M$ und die Verläufe Blau mit senkrechter Strichschraffur, Rot für Lasten und Grün für Koordinaten und Maße. Das ist ein konsistentes eigenes Schema, das an die Farben der Vorlesung 2013 anknüpft. Lohnenswert wären folgende Übernahmen von Gross: ⊕/⊖ in den Flächen, eine Achsenbeschriftung mit Pfeil (die VL zeigt sie bisher nur ohne Pfeil), gestrichelte senkrechte Hilfslinien zwischen System und Verläufen (in `traeger-einzelkraefte.svg` bereits vorhanden) und die Kurvenbezeichnung als Text bei Parabeln.

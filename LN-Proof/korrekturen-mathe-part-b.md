# Formelprüfung Part B (Teil II): Satz und Notation

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184). Geprüft am 14.10.2026; Stand der Umsetzung: 20.10.2026.

**Umfang:** Teil II, Kap. 1–4, geprüft im LaTeX-Quelltext (Branch `fahnenkorrektur`). Geprüft wurden nur Satz und Notation in Formeln: Tippfehler, Klammern, Indizes, uneinheitliche Schreibweisen, Mathemodus, Satzzeichen an Formeln, Verweise. Beweise wurden **nicht** nachgerechnet; wo ein Befund inhaltlich wirkt, steht „bitte prüfen“.

**Stand 20.10.2026:** **Kap. 1, 2 und 3 sowie Abschnitt 4.2 sind erledigt** (Kap. 1 nach Durchsicht durch Rainer Nagel, Kap. 3 und Abschnitt 4.2 nach Freigabe durch Günther Greiner; in der Spalte Kommentar mit **Umgesetzt** markiert, Abweichungen und Ausnahmen ebenda). Kap. 4 ist außer Abschnitt 4.2 noch offen. Die Zeilenangaben beziehen sich auf den Stand vom 14.10.2026.

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

**Spalten:** S. = gedruckte Buchseite, ermittelt über das nächstgelegene Label (kann um eine Seite abweichen). Z. = Zeile in der .tex-Datei. Sicherheit: ● eindeutig · ◐ sehr wahrscheinlich · ○ Hinweis/Ermessen.

Insgesamt **206 Punkte**: 50 ●, 93 ◐, 63 ○. Davon stehen 13 bereits in der Arbeitsliste `Fahnenkorrektur_Springer_LNM1184.md` (im Kommentar markiert).

## Einzelbefunde

### Teil II, Kap. 1 – Basic Results on Spaces C₀(X) (`part-b/chap-b1.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 137 | 57 | ○ | `C_{0}(X\backslash F)` | `C_{0}(X\setminus F)` | LaTeX | **Umgesetzt.** \backslash setzt einen großen Backslash ohne Abstände wie bei einem binären Operator; für Mengendifferenz \setminus (im Buch überwiegend, 34 vs. 12 Stellen). Einzige Stelle im Kapitel. |
| 137 | 57 | ◐ | `via the map $f + J \to f\vert_{F}$` | `via the map $f + J \mapsto f\vert_{F}$` | Notation | **Umgesetzt.** Zuordnung von Elementen: \mapsto (im Buch durchgehend so, z. B. t ↦ T(t)f); ebenso Z. 110 `$t \to \delta_{t}$` → `$t \mapsto \delta_{t}$`. |

### Teil II, Kap. 2 – Characterization of Positive Semigroups on C₀(X) (`part-b/chap-b2.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 142 | 58 | ○ | `(n/tR(n/t,A))^{n}` | `((n/t)R(n/t,A))^{n}` | Notation | **Umgesetzt.** „n/tR“ ist mehrdeutig (liest sich wie n/(tR…)); n/t klammern. |
| 142 | 101 | ○ | `\mleft( (\eu^{tA}f(x) - f(x)) \mright)` | `\bigl( (\eu^{tA}f)(x) - f(x) \bigr)` | Klammern | **Umgesetzt.** Doppelte Klammer; gemeint ist (\eu^{tA}f)(x), vgl. Z. 102. |
| 142 | 102 | ● | `\mleft( (\eu^{tA}f(x) \mright)` | `(\eu^{tA}f)(x)` | Klammern | **Umgesetzt.** Innere öffnende Klammer ohne Gegenstück; gedruckt „((e^{tA}f(x))“. |
| 142 | 146 | ◐ | `This shows~\ref{thm:b2-1.3-2} to hold.` | `This shows~\ref{thm:b2-1.3-3} to hold.` | Verweis | **Umgesetzt.** Im Beweisschritt (b) ⇒ (c) wird A + ‖A‖Id ≥ 0, also (c), gezeigt; bitte prüfen. |
| 142 | 152 | ◐ | `\qedhere \qedhere` | `\qedhere` | LaTeX | **Umgesetzt.** \qedhere steht doppelt (Z. 152/153). |
| 144 | 225 | ◐ | `0 \leq  u \in C(K)` | `0 \ll u \in C(K)` | Tippfehler | **Umgesetzt.** Alle genannten Stellen. Z. 733 (`0 \leq q`) bewusst nicht geändert, dort genügt q ≥ 0. Gemeint ist ein strikt positives u (vgl. Z. 246, 461, 629, 638: „strictly positive“ bzw. u ≫ 0); vermutlich ≪ bei der Konvertierung zu ≤ geworden. Ebenso Z. 251, 423, 474, 561, 605, 732, 823 (jeweils u), 1861 (p, vgl. Satz: „strictly positive p“) und 2260 (p mit inf p > 0). Bitte prüfen. |
| 144 | 247 | ○ | `\{u \in C(K): u \gg 0\}` | `\{u \in C(K) \colon u \gg 0\}` | Notation | **Umgesetzt.** Sonst \colon in Mengenklammern (anderer Abstand); ebenso Z. 2455, 2463, 2664, 2669. |
| 144 | 263 | ◐ | `\sup_{\lambda \geq \omega}` | `\sup_{\lambda \geq w}` | Tippfehler | **Umgesetzt.** Im selben Ausdruck und in Theorem~\ref{thm:b2-1.8} heißt die Konstante w, nicht ω. |
| 146 | 389 | ● | `\textcite{greinervoigtwolff:1981}` + Zeilenumbruch + `)` | `\textcite{greinervoigtwolff:1981})` | Abstand | **Umgesetzt.** Schon in der Arbeitsliste. Der Zeilenumbruch erzeugt ein Leerzeichen vor „)“. |
| 147 | 434 | ○ | `(f \in C(K)\,)` | `(f \in C(K))` | Abstand | **Umgesetzt.** Überzähliger Abstand vor „)“; ebenso Z. 902 `\,($f \in C[-1,0]$\,)`. |
| 148 | 568 | ● | `$\lambda > \lambda_{0}$ ,` | `$\lambda > \lambda_{0}$,` | Abstand | **Umgesetzt.** Leerzeichen vor Komma. |
| 148 | 588 | ◐ | `(see Eq.~\myeqpageref{eq:a3-1.3})` | `(see Part-I, Eq.~\myeqpageref{eq:a3-1.3})` | Verweis | **Umgesetzt.** Verweis auf Part I ohne „Part-I“; gedruckt „(3.1.3)“, kollidiert mit der Gleichungsnummerierung in Part II, Kap. 3. |
| 149 | 636 | ○ | `Au = \lambda u - 1` | `Au = \lambda u - \1` | Notation | **Umgesetzt.** Konstante Funktion sonst \1 (vgl. u = R(λ,A)\1 in derselben Zeile). |
| 150 | 696 | ● | `0 & \text{if } x+t > 0` | `0 & \text{if } x+t > 1` | Tippfehler | **Umgesetzt.** Gegenfall zu „x+t ≤ 1“; bitte prüfen (wegen X = [0,1) ggf. „< 1“ / „≥ 1“). |
| 150 | 730 | ◐ | `also generates a positive semigroup).` | `also generates a positive semigroup.` | Klammern | **Umgesetzt.** Schon in der Arbeitsliste. Schließende Klammer ohne öffnende. |
| 151 | 754 | ○ | `&\text{ then } q \cdot B` | `&\text{then } q \cdot B` | Abstand | **Umgesetzt.** Führendes Leerzeichen in \text rückt die Zeile gegenüber Z. 752/753 ein; ebenso Z. 2995/2996 im array (`\text{ and there exists …}`, `\text{ such that …}`). |
| 151 | 770 | ◐ | `$(I - q \cdot B)$` | `$(\Id - q \cdot B)$` | Notation | **Umgesetzt.** Identität sonst \Id (Z. 775, 779); ebenso Z. 793 und 812 `(R(1,B) - I)`. |
| 151 | 803 | ● | `\sup\nolimits_{\|f\|_{u} \leq 1}\{ \,` | `\sup\nolimits_{\|f\|_{u} \leq 1}` | Klammern | **Umgesetzt.** Die hier geöffnete Mengenklammer \{ wird nie geschlossen (Z. 804 schließt nur das innere \{…\}). |
| 151 | 820 | ◐ | `B = m^{1/k} \cdot A` | `B = m^{l/k} \cdot A` | Tippfehler | **Umgesetzt.** Zusätzlich Laufbereich l = 0, …, k−1 (der erste Schritt geht von B = A aus). Der Laufindex l (l = 1, …, k−1) kommt sonst nicht vor; gemeint m^{l/k}; bitte prüfen. |
| 152 | 854 | ○ | `(P') \quad $f \in C(K)_{+}$` | `$(\mathrm{P}')$ \quad $f \in C(K)_{+}$` | Notation | **Umgesetzt.** Im Textmodus wird ' zum Apostroph statt Strich; ebenso Z. 846 und 876. Zudem überzähliges `\,` vor „implies“. |
| 153 | 916 | ● | `\eu^{\lambda x} d\mu(x)` | `\eu^{\lambda x} \diff{\mu(x)}` | Notation | **Umgesetzt.** Kursives d, sonst aufrechtes \diff (vgl. Z. 913); ebenso Z. 1499 `- d\phi` und Z. 1832 `h(\phi(s,x))ds` (→ `\ds`). |
| 153 | 958 | ○ | `L_{11}u_{1} + \ldots + L_{1n}u_{n}` | `L_{11}u_{1} + \dots + L_{1n}u_{n}` | LaTeX | **Umgesetzt.** Zwischen Operatoren zentrierte Punkte; ebenso Z. 960. |
| 154 | 1026 | ○ | `g \in C([0,1])` | `g \in C[0,1]` | Notation | **Umgesetzt.** Im ganzen Beispiel C[0,1] bzw. C^{2}[0,1]. Im selben Beispiel C[0,1] (Z. 992) neben C([0,1]) und C^{2}([0,1]) (Z. 995, 1032, 1034); im Kapitel sonst meist C[−1,0], C^{1}[−1,0]. Vereinheitlichen. |
| 154 | 1029 | ◐ | `k = \frac{1}{2}\lambda\mleft(` | `k = \frac{1}{2\lambda}\mleft(` | Tippfehler | **Umgesetzt.** Mit Faktor λ/2 gilt λ²k − k'' = g nicht, mit 1/(2λ) schon (Original vermutlich „1/2λ“); bitte prüfen. |
| 154 | 1041 | ○ | `\exp(\lambda^{2})` | `\exp(2\lambda)` | Tippfehler | **Umgesetzt.** Die Determinante des Randwertsystems für h = a e^{λx} + b e^{−λx} enthält e^{2λ}; bitte prüfen. |
| 155 | 1112 | ◐ | `\lim_{t \to 0} 1/t(\Theta(f+tu) - \Theta(f))` | `\lim_{t \downarrow 0} \frac{1}{t}(\Theta(f+tu) - \Theta(f))` | Notation | **Umgesetzt.** Rechtsseitige Ableitung, also t ↓ 0 (wie Z. 1138); „1/t(…)“ zudem mehrdeutig. |
| 156 | 1122 | ○ | `\label{prop:b2-2.3}` … `(chain rule). Let` | `\begin{proposition}[Chain rule]\label{prop:b2-2.3}` | LaTeX | **Umgesetzt.** Titel steht als Text im Rumpf statt als optionales Argument (vgl. [Hille-Yosida] in Part I). |
| 156 | 1140 | ◐ | `- \Theta(k(a)) - D_{k'(a)}\Theta(k(a))\bigr]` | `- \Theta(k(a))\bigr] - D_{k'(a)}\Theta(k(a))` | Klammern | **Umgesetzt.** Der D-Term gehört nicht unter 1/t (vgl. Z. 1138); bitte prüfen. |
| 156 | 1172 | ◐ | `z = (x_{0} + iy_{0})` | `z = (x_{0} + \iu y_{0})` | Notation | **Umgesetzt.** Kursives i, sonst \iu (Z. 1417, 1541); ebenso Z. 1179 und 1183 (`iy_{0}`, `iu_{2}`). |
| 156 | 1177 | ◐ | `(\Theta(x_{0},y_{0})\vert u)` | `(\nabla\Theta(x_{0},y_{0})\vert u)` | Tippfehler | **Umgesetzt.** Gemeint ist das Skalarprodukt mit dem Gradienten; Θ(x0,y0) ist ein Skalar; bitte prüfen. |
| 158 | 1254 | ◐ | `= \left\langle \Re\left[\left(\widehat{\sign} \bar{f}\right)(Af)\right],\phi \right\rangle` | `= \Re\bigl[(\widehat{\sign} \bar{f})(Af)\bigr](x)` | Tippfehler | **Umgesetzt.** Die linke Seite ist punktweise in x; rechts gehört der Wert an der Stelle x (so die auskommentierte Z. 1255), nicht die Paarung mit φ. |
| 158 | 1317 | ◐ | `\overline{\lim}_{h \downarrow 0}` | `\limsup_{h \downarrow 0}` | Notation | **Umgesetzt.** Sonst \limsup (Z. 1139–1141). |
| 159 | 1338 | ● | `\lim_{t \downarrow 0}  \frac{1}{h}` | `\lim_{h \downarrow 0}  \frac{1}{h}` | Tippfehler | **Umgesetzt.** Grenzübergang in h (vgl. Z. 1336/1337). |
| 159 | 1338 | ● | `\langle (\vert T(s+h)f\vert -  \vert T(s)f\vert ,` | `\langle \vert T(s+h)f\vert - \vert T(s)f\vert,` | Klammern | **Umgesetzt.** Öffnende Klammer ohne Gegenstück. |
| 161 | 1482 | ◐ | `for $(f \in D(A_{\max})$ and $ \phi \in D(A'_{\max}))$.` | `for $f \in D(A_{\max})$ and $\phi \in D(A'_{\max})$.` | Klammern | **Umgesetzt.** Klammerpaar über zwei Formeln verteilt; Klammern überflüssig. |
| 161 | 1527 | ● | `D(A'_{max})` | `D(A'_{\max})` | Notation | **Umgesetzt.** Kursives „max“, sonst \max. |
| 161 | 1548 | ◐ | `\int_{0}^{1} \phi(x)\, \diff{\vert f(x)\vert}` | `\int_{-1}^{0} \phi(x)\, \diff{\vert f(x)\vert}` | Tippfehler | **Umgesetzt.** Integrationsgrenzen; das Intervall ist [−1,0]; bitte prüfen. |
| 161 | 1548 | ○ | `= \\` + `&= \phi(0)` | `\\` + `&= \phi(0)` | LaTeX | **Umgesetzt.** Gleichheitszeichen am Zeilenende und am nächsten Zeilenanfang (doppelt); sonst im Kapitel nicht so gesetzt. |
| 162 | 1588 | ● | `\Re[\widehat{(\sign} f)(Af)]` | `\Re[(\widehat{\sign} \bar{f})(Af)]` | Klammern | **Umgesetzt.** Klammer im \widehat-Argument, Hut über „(sign“. Zusätzlich \bar{f} wie in (2.2.9) (ebenso Z. 1587); bitte prüfen. |
| 162 | 1601 | ● | `$f~\in~C_{0}[-1,0)$` | `$f \in C_{0}[-1,0)$` | LaTeX | **Umgesetzt.** Tilden im Mathemodus erzeugen zusätzliche Abstände; ebenso Z. 2678 `=~x` und Z. 2967 `M^{-1}~+~h`. |
| 164 | 1692 | ◐ | `C([0,1]) \times K` | `C([0,1] \times K)` | Tippfehler | **Umgesetzt.** Identifikation C([0,1],C(K)) mit C([0,1] × K); bitte prüfen. |
| 164 | 1702 | ○ | `f,g \in D(\delta). \label{eq:b2-3.4} \\` | `f,g \in D(\delta), \label{eq:b2-3.4} \\` | Satzzeichen | **Umgesetzt.** Punkt ans Ende von Z. 1703 gesetzt. Punkt nach der ersten von zwei Bedingungen; ggf. Punkt ans Ende von Z. 1703. |
| 166 | 1811 | ◐ | `by Eq.~\myeqpageref{eq:a2-1.8}` | `by Part-I, Eq.~\myeqpageref{eq:a2-1.8}` | Verweis | **Umgesetzt.** Schon in der Arbeitsliste (S. 166, „Verweis prüfen“). Das Ziel liegt jetzt in Part I, gedruckt wird aber „(2.1.8)“, identisch mit Eq. (2.1.8) dieses Kapitels; „Part-I,“ ergänzen. |
| 166 | 1817 | ◐ | `for all $t \geq 0$, $f \in C(K)$` | `for all $t \geq 0$, $f \in C(K)$.` | Satzzeichen | **Umgesetzt.** Satzpunkt fehlt (Absatzende nach abgesetzter Formel). |
| 166 | 1838 | ● | `$f \in D(\delta)$ ,` | `$f \in D(\delta)$,` | Abstand | **Umgesetzt.** Leerzeichen vor Komma. |
| 166 | 1841 | ○ | `\frac{\diff{}}{\dt}\vert_{t = 0}` | `\left.\frac{\diff{}}{\dt}\right\vert_{t = 0}` | Notation | **Umgesetzt.** Strich nicht skaliert; sonst \left. … \right\vert (z. B. Z. 1744). |
| 167 | 1895 | ○ | `$A$ is \text{local}` | `$A$ is \emph{local}` | LaTeX | **Umgesetzt.** \text im Textmodus wirkungslos; vermutlich Hervorhebung des definierten Begriffs gemeint. |
| 167 | 1913 | ◐ | `non-com\-mutative C*-algebras` | `non-com\-mutative \CA-algebras` | Notation | **Umgesetzt.** In der Überschrift (Z. 1912) \CA (C mit hochgestelltem *), im Text „C*“ mit Sternchen auf der Grundlinie; ebenso Z. 1914 (2x). |
| 167 | 1922 | ● | `(\pm\1 - A)(D(A)) = \mathcal{A}_{h}.` | `(\pm\1 - A)(D(A)) = \mathcal{A}_{h}` | Satzzeichen | **Umgesetzt.** Der Satz geht nach der Formel weiter („and A is local …“). |
| 167 | 1934 | ● | `T(t)_{t \in \R}` | `(T(t))_{t \in \R}` | Klammern | **Umgesetzt.** Sonst durchgehend (T(t))_{t ∈ R}. |
| 168 | 2003 | ◐ | `T(.)f` | `T(\cdot)f` | Notation | **Umgesetzt.** Platzhalter sonst \cdot (z. B. Z. 2560). |
| 171 | 2151 | ◐ | `\eu^{-ws}k_{s}(x)` | `\eu^{-\omega s}k_{s}(x)` | Notation | **Umgesetzt.** Im ganzen Beweis ω. In (2.3.16)/(2.3.17) heißt die Konstante ω, im weiteren Beweis w; ebenso Z. 2153, 2158, 2160, 2169, 2170, 2177, 2183. |
| 171 | 2183 | ● | `k_{t}(t)\,p(x)^{-1}` | `k_{t}(x)\,p(x)^{-1}` | Tippfehler | **Umgesetzt.** Argument ist x (vgl. Z. 2177). |
| 172 | 2211 | ○ | `for all \\` | `for all` | LaTeX | **Umgesetzt.** Manueller Zeilenumbruch im Fließtext; ebenso Z. 2764 (`\\is contained`) und 2767 (`$\delta_{m}$\\`). |
| 173 | 2241 | ● | `p(\phi_{t}(x)^{-1}` | `p(\phi_{t}(x))^{-1}` | Klammern | **Umgesetzt.** Schließende Klammer fehlt (vgl. (2.3.15)). |
| 173 | 2258 | ◐ | `$V^{-1}\delta V$ generates a positive group` | `$V\delta V^{-1}$ generates a positive group` | Tippfehler | **Umgesetzt.** Passend zu (2.3.18) A = VδV^{-1} + h und Z. 2270; bitte prüfen. |
| 173 | 2299 | ○ | `denotes the scalar product in $\R^{n}$` | `denotes the scalar product in $\R^{n}$.` | Satzzeichen | **Umgesetzt.** Satzpunkt am Ende des Beispiels fehlt. |
| 173 | 2308 | ● | `f(\phi(x,t))` | `f(\phi(t,x))` | Tippfehler | **Umgesetzt.** Argumentreihenfolge; sonst φ(t,x). |
| 173 | 2309 | ● | `\big(\mathrm{grad}\: f)(\phi(t,x)) \big\vert F(\phi(t,x))\big)` | `\big((\mathrm{grad}\: f)(\phi(t,x)) \big\vert F(\phi(t,x))\big)` | Klammern | **Umgesetzt.** Öffnende Klammer vor grad fehlt (vgl. (2.3.21)). |
| 173 | 2347 | ◐ | `\nabla(f \circ \phi_{t})(x) = (\nabla f)(\phi_{t}(x))` | `[\mathrm{grad}\:(f \circ \phi_{t})](x) = (\mathrm{grad}\: f)(\phi_{t}(x))` | Notation | **Umgesetzt.** Im selben Beispiel sonst „grad“ (Z. 2289–2315); ebenso Z. 2349, 2352, 2353 (überarbeitete Passage). |
| 175 | 2405 | ◐ | `-\infty \leq c \text{ and } m(c) = 0` | `-\infty < c \text{ and } m(c) = 0` | Tippfehler | **Umgesetzt.** Analog zu „d < ∞“ in Z. 2413; der Fall c = −∞ ist die Alternative „a = c = −∞“. |
| 175 | 2508 | ● | `Bg = V^{-1}\delta_{m}V = V^{-1}(m(g \circ q)')` | `Bg = V^{-1}\delta_{m}Vg = V^{-1}(m(g \circ q)')` | Tippfehler | **Umgesetzt.** g fehlt. |
| 176 | 2532 | ● | `C^{1}(a',b)` | `C^{1}(a',b')` | Tippfehler | **Umgesetzt.** Strich fehlt. |
| 176 | 2546 | ○ | `B_{1}u(t) \quad u(0) = f.` | `B_{1}u(t), \quad u(0) = f.` | Satzzeichen | **Umgesetzt.** Komma vor \quad. |
| 176 | 2576 | ○ | `\quad x \in (a,b).` | `\quad (x \in (a,b)).` | Notation | **Umgesetzt.** Laufbereich sonst in Klammern (z. B. Z. 2569); ebenso Z. 2621. |
| 176 | 2588 | ◐ | `g(q_{n}^{-1}(q_{n}(x) + t))` | `g(g_{n}^{-1}(g_{n}(x) + t))` | Notation | **Umgesetzt.** Die Funktionen heißen in Remark~\ref{rem:b2-3.17} bzw. in (2.3.22) g_n; q_n wird in Theorem~\ref{thm:b2-3.24} anders verwendet; ebenso rechte Seite. |
| 178 | 2758 | ◐ | `then $D(\delta)$ contains` | `then $D(\delta_{m})$ contains` | Tippfehler | **Umgesetzt.** Gemeint ist der Definitionsbereich von δ_m. |
| 178 | 2767 | ◐ | `differentiable functions in $D_{0}(\delta_{m})$` | `differentiable functions in $D(\delta_{m})$` | Tippfehler | **Umgesetzt.** Zirkuläre Definition; vgl. Theorem~\ref{thm:b2-3.17}. |
| 180 | 2865 | ◐ | `constructed from $m$ in Theorem~\ref{thm:b2-3.17}` | `constructed from $m$ in Remark~\ref{rem:b2-3.17}` | Verweis | **Umgesetzt.** Die Konstruktion des Flusses (2.3.22) steht nach der Aufteilung jetzt in der Remark; ebenso Z. 2931. |
| 182 | 2970 | ○ | `$A = V\delta_{m}V^{-1} + h$` | `$A = V^{-1}\delta_{m}V + h$` | Notation | **Umgesetzt.** Die Aussage (2.3.24) lautet A = V^{-1}δ_mV + h; mit V = MU passt die Form im Beweis nicht dazu (dann V = (MU)^{-1}); bitte prüfen. |
| 182 | 2975 | ● | `\phi(a,t) = a` … `\phi(b,t) = b` | `\phi(t,a) = a` … `\phi(t,b) = b` | Tippfehler | **Umgesetzt.** Argumentreihenfolge (vgl. Z. 2978). |
| 182 | 2981 | ◐ | `\widetilde{\delta}_{m}` | `\tilde{\delta}_{m}` | Notation | **Umgesetzt.** Sonst \tilde{\delta}_m (Z. 2992–3037); sichtbar verschiedene Akzentbreite (2x in der Zeile). |
| 183 | 3050 | ◐ | `A = V^{-1}\delta_{m}V + h` | `A = V^{-1}\tilde{\delta}_{m}V + h` | Notation | **Umgesetzt.** Auf C[a,b] ist der Operator δ̃_m (vgl. Theorem~\ref{thm:b2-3.27}); bitte prüfen. |
| 184 | 3077 | ● | `(Theorem~\ref{thm:b2-3.14} )` | `(Theorem~\ref{thm:b2-3.14})` | Abstand | **Umgesetzt.** Schon in der Arbeitsliste. Leerzeichen vor „)“. |

### Teil II, Kap. 3 – Spectral Theory of Positive Semigroups on C₀(X) (`part-b/chap-b3.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 188 | 64 | ◐ | `\geq \vert\lambda_{0} - \mu_{0}\vert^{-1}` | `\geq \vert\lambda_{0} - \mu_{0}\vert^{-1}.` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Abgesetzte Formel beendet den Satz, der Punkt fehlt (der nächste Satz beginnt groß); ebenso Z. 74, 166, 250, 518, 636, 722, 812, 1486, 1972, 2212. |
| 189 | 115 | ○ | `(Af)(x) = f'(x) - xf(x), D(A) = \{` | `(Af)(x) = f'(x) - xf(x), \quad D(A) = \{` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Z. 1611 steht im Fließtext; dort zwei Formeln `$C(G)$, $G \coloneq …$` statt `\quad`. Komma zwischen zwei Formelteilen im Mathemodus ohne Abstand, wirkt gequetscht; ebenso Z. 449, 464, 1474, 1611, 1746, 1839, 2261. |
| 190 | 197 | ◐ | `by Example~\ref{ex:a3-3.6}` | `by Part-I, Example~\ref{ex:a3-3.6}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Das Ziel liegt in Part-I. Ohne den Zusatz liest man „Example 3.3.6“ als Beispiel aus Part-II (vgl. Z. 799, 945, 969, 1199 mit „Part-I,“). |
| 190 | 230 | ◐ | `\phi \in D(A^*)$ such that $A^*\phi = \alpha\phi` | `\phi \in D(A')$ such that $A'\phi = \alpha\phi` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Adjungierte steht sonst im ganzen Kapitel mit Strich (A', T(t)'), nur hier als A^*. |
| 192 | 307 | ○ | `equation Eq.~\myeqpageref{eq:b3-1.16}` | `Eq.~\myeqpageref{eq:b3-1.16}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste. Doppelte Bezeichnung „equation Eq.“. |
| 192 | 312 | ○ | `\langle \phi,1 \rangle = 1` | `\langle \phi,\1_{K} \rangle = 1` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die konstante Funktion steht sonst als \1 bzw. \1_{K} (fett), hier als normale 1. |
| 192 | 334 | ○ | `\exp(-(x-y)^{2}/4t)` | `\exp(-\vert x-y\vert^{2}/(4t))` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). x, y ∈ R^n: Das Quadrat eines Vektors und „/4t“ sind mehrdeutig; bitte prüfen. |
| 192 | 344 | ◐ | `\langle \phi,f \rangle = \lim_{t \to \infty}\langle T(t)f,\phi \rangle` | `\langle f,\phi \rangle = \lim_{t \to \infty}\langle T(t)f,\phi \rangle` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Argumente der Dualpaarung sind innerhalb derselben Formel vertauscht. Im Kapitel steht sonst meist ⟨f,φ⟩ (Z. 749, 1190, 1202), umgekehrt nur noch in Z. 312. |
| 194 | 479 | ◐ | `we have for all $f$.` | `we have for all $f$` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Punkt vor der abgesetzten Formel (3.2.9) unterbricht den Satz. |
| 195 | 536 | ○ | `\text{ and \ }` | `\text{ and }` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Das überzählige „\ “ erzeugt einen doppelten Wortabstand. |
| 196 | 567 | ○ | `Eq.~\myeqpageref{eq:b3-2.12})` | `Eq.~\myeqpageref{eq:b3-2.13})` | Verweis | **Nicht geändert** (20.10.2026, Entscheidung G. Greiner). Die Rechnung davor benutzt die iterierte Form (3.2.13), nicht (3.2.12); bitte prüfen. |
| 196 | 594 | ◐ | `\eu^{-\alpha t}\eu^{\im\beta  t}S_{h}^{-1}T(t)S_{h}` | `\eu^{-\alpha t}\eu^{-\im\beta t}S_{h}^{-1}T(t)S_{h}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Vorzeichen: Aus (i) mit λ = e^{iβt} folgt e^{iβt}T(t) = S_h^{-1}T(t)S_h, also der Faktor e^{-iβt}. Das passt auch zu iβ + A = S_h^{-1}AS_h (Z. 536); bitte prüfen. |
| 196 | 610 | ◐ | `for every $k \in \Z$\,` | `for every $k \in \Z$.` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Definition endet mit \, statt mit einem Punkt; ebenso Z. 2315 (`\ds\,` am Formelende in Prop. 3.4.8 (iv), dort Komma). |
| 196 | 623 | ● | `of\/ $\im \R$ ,` | `of\/ $\im \R$,` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Leerzeichen vor dem Komma; ebenso Z. 789, 2298, 2301 („values ,“), 2304. |
| 196 | 635 | ◐ | `M_{6} &= \cup_{n=0}^{\infty}\{` | `M_{6} &= \bigcup_{n=0}^{\infty}\{` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). In einer abgesetzten Formel gehört hier das große \bigcup (wie in Z. 626); \cup ist das binäre Zeichen. |
| 197 | 674 | ◐ | `semigroup on $C(D)$ (which is given by` | `semigroup on $C(D)$ which is given by` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die öffnende Klammer wird nie geschlossen (die Formel in Z. 677 endet mit einem Punkt). |
| 197 | 691 | ○ | `(\eg $S = M$)` | `(\eg $S = -\im M$)` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). S ⊆ R, aber M ⊆ iR, also kann S = M nicht stimmen; bitte prüfen. |
| 198 | 744 | ○ | `T(t)\vert h\vert - \vert h\vert \geq 0` | `T(t)\vert h\vert - \vert h\vert \geq 0,` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Komma und „and“ zwischen (3.2.14) und (3.2.15) eingefügt. Die abgesetzten Formeln (3.2.14) und (3.2.15) folgen ohne Satzzeichen und Bindewort aufeinander; Vorschlag: Komma und „and“ einfügen. |
| 198 | 767 | ◐ | `C_{0}(X\backslash M)` | `C_{0}(X\setminus M)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). \backslash statt der Mengendifferenz \setminus (sonst \setminus, z. B. Z. 2041, 2468); ebenso Z. 768 (`M\backslash N`). |
| 199 | 781 | ○ | `I_{1} \subsetneq \ldots \subsetneq I_{k}` | `I_{1} \subsetneq \cdots \subsetneq I_{k}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Zwischen Relationszeichen gehören \cdots auf die Mittelachse; ebenso Z. 812 (`= \ldots =`). |
| 199 | 803 | ● | `\frac{1}{2\pi i}` | `\frac{1}{2\pi\im}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Kursives i statt \im (aufrechtes i). |
| 199 | 827 | ◐ | `Q_{m/} = \lim_{z \to 0}z^{m}R(z,A_{k})` | `Q_{m/I_{k-1}} = \lim_{z \to 0}z^{m}R(z,A_{k})` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Index ist abgeschnitten (vgl. Z. 842 `Q_{1/I_{k-1}}`); ebenso Z. 835. |
| 199 | 841 | ○ | `{Q_{1}}_{/I_{k-1}}` | `Q_{1/I_{k-1}}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Dasselbe Objekt steht in Z. 842 als `Q_{1/I_{k-1}}` und sieht im Druck anders aus; vereinheitlichen. |
| 201 | 893 | ● | `$\ I_0$ & $I_2$ & $I_2$ & $I_3$` | `$I_0$ & $I_1$ & $I_2$ & $I_3$` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Im Tabellenkopf steht I_2 doppelt, I_1 fehlt; außerdem steht ein überflüssiges \ vor I_0. |
| 201 | 945 | ◐ | `AQ = QA = s(A)A = 0` | `AQ = QA = s(A)Q = 0` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Für das Residuum Q eines Pols 1. Ordnung gilt AQ = s(A)Q; bitte prüfen. |
| 202 | 1016 | ○ | `r_{\text{ess}}(T(t)) < r(T(t))` | `r_{\text{ess}}(T(t_{0})) < r(T(t_{0}))` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Ebenso $\sigma(T(t_{0}))$ in Z. 1015. Die Voraussetzung in Kor. 3.2.11 ist für t_0 formuliert; ebenso Z. 1015 (`\exp(s(A)t) = r(T(t))`); bitte prüfen. |
| 203 | 1070 | ○ | `all $\im k$, $k \in \Z$, $k \neq 0$` | `all $\im n$, $n \in \Z$, $n \neq 0$` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). k ist in diesem Beispiel schon die Funktion k ∈ C_0(R) (Z. 1046, 1052), also doppelt belegt; dann auch e_k → e_n; bitte prüfen. |
| 204 | 1146 | ◐ | `Eq.~\myeqpageref{eq:b3-2.25} and Eq.~\myeqpageref{eq:b3-2.26}` | `Eq.~\myeqpageref{eq:b3-2.27} and Eq.~\myeqpageref{eq:b3-2.28}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste. Die Abschätzung folgt aus (3.2.27) und (3.2.28). |
| 204 | 1162 | ● | `\{\alpha e_{\lambda} \colon a \in \C\}` | `\{\alpha e_{\lambda} \colon \alpha \in \C\}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Laufvariable heißt einmal α, einmal a. |
| 204 | 1170 | ○ | `\langle e_{\lambda},\phi \rangle` | `\phi(e_{\lambda})` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Im selben Satz und in (3.2.30) steht φ(e_λ), hier ⟨e_λ,φ⟩; vereinheitlichen. |
| 206 | 1293 | ◐ | `satisfy $T \neq \{0\}$  and  $T \subseteq` | `satisfies $I \neq \{0\}$ and $I \subseteq` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste. Zweimal T statt I. |
| 206 | 1302 | ◐ | `\langle f_{0},T(t)'\delta_{y} \rangle > 0` | `\langle f_{0},T(t)'\delta_{y} \rangle = 0` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Träger sind disjunkt (Z. 1301), also = 0; nur so folgt „y ∉ …“; bitte prüfen. |
| 206 | 1306 | ● | `(T(t_{0})(f)(y)` | `(T(t_{0})f)(y)` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Klammern unausgeglichen (4 öffnende, 3 schließende). |
| 206 | 1315 | ◐ | `\ref{item:b3-3.1-v} $\implies$~\ref{item:b3-3.1-vi}` | `\ref{item:b3-3.1-v} $\implies$~\ref{item:b3-3.1-iv}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste. Gedruckt steht „(e) ⇒ (f)“, gezeigt wird (e) ⇒ (d). |
| 206 | 1320 | ◐ | `Part-I, Example~\ref{subsec:a1-3.3}` | `Part-I, Section~\ref{subsec:a1-3.3}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Ziel ist der Unterabschnitt „The Subspace Semigroup“ in „Standard Constructions“. Unterabschnitte werden sonst mit „Section“ zitiert (Z. 329, 1857). |
| 207 | 1352 | ○ | `(1 - R(\lambda,A)M_{h})^{-1}` | `(\Id - R(\lambda,A)M_{h})^{-1}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Identität steht sonst als \Id (Z. 1135–1143); ebenso Z. 1354, 2058. |
| 208 | 1388 | ◐ | `\bigcup_{t>0}\text{supp}\{k(t,x,.)\}` | `\bigcup_{t>0}\supp k(t,x,\cdot)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Makro \supp statt \text{supp} verwenden; Platzhalter als \cdot (vgl. Z. 1708); die Mengenklammern um die Funktion sind überflüssig. |
| 208 | 1404 | ○ | `C([0,1])` | `C[0,1]` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst C[0,1] bzw. C[-1,0] (Z. 673, 1104); ebenso Z. 127 (`C(\left[0,1\right])`). |
| 209 | 1435 | ● | `\dim(\Kern{s(A) - A} \leq 1` | `\dim(\Kern{s(A) - A}) \leq 1` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Nach \Kern{…} fehlt die schließende Klammer. |
| 209 | 1435 | ◐ | `(\cf Theorem~\ref{thm:b3-1.6}), then` | `(\cf Theorem~\ref{thm:b3-1.6})), then` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste. Die Klammer „(\eg if …“ wird nicht geschlossen. |
| 211 | 1558 | ● | `A + i(\beta - \alpha)` | `A + \im(\beta - \alpha)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Kursives i statt \im; ebenso Z. 1562. |
| 211 | 1564 | ○ | `\im (\beta - \alpha) \in P\sigma(A)` | `\im (\alpha - \beta) \in P\sigma(A)` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Aus Kern(A + i(β−α)) ≠ {0} folgt der Eigenwert −i(β−α) = i(α−β); bitte prüfen. |
| 211 | 1590 | ◐ | `$h\cdot p_{n}(h)$` | `$h\cdot p_{n}(\tilde{h})$` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Das Polynom wird auf h̃ angewandt (Z. 1587); ebenso Z. 1598, 1600. |
| 211 | 1595 | ○ | `k=0,1,2,\ldots` | `k=1,2,3,\ldots` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). h^{[k]} (k ≥ 1) liegt in Kern(ikα − A). Mit k = 0 verschwindet φ nicht auf dem Span (vgl. Z. 1597); bitte prüfen. |
| 212 | 1666 | ○ | `\|j(f)\| > \epsilon\|f\|` | `\|j(f)\| \geq \epsilon\|f\|` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die strikte Ungleichung ist für f = 0 falsch; bitte prüfen. |
| 213 | 1726 | ◐ | `P\sigma(A)\cap(s(A) + \im\R) = \{s(A)\}` | `P\sigma(L)\cap(s(L) + \im\R) = \{s(L)\}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Operator heißt in (ii) L (vgl. Z. 1742 s(L)); ebenso Z. 1773 (A in Teil (iii)), bitte prüfen. |
| 213 | 1729 | ◐ | `0 < f \in C_{0}(X)` | `0 < f \in C_{0}(\Omega)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Grundraum ist hier Ω. |
| 213 | 1739 | ◐ | `(see Definition~\ref{def:b3-3.1}\,(e))` | `(see Definition~\ref{def:b3-3.1}\,(e)).` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Am Absatzende fehlt der Satzpunkt. |
| 214 | 1746 | ● | `L_{0}h = i \alpha h` | `L_{0}h = \im\alpha h` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Kursives i statt \im. |
| 214 | 1757 | ◐ | `w_{i}'~,\\` | `w_{i}',\\` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Tilde im Mathemodus erzeugt Leerraum vor dem Komma; ebenso Z. 1758, 1765 (`~.`). |
| 214 | 1765 | ○ | `\sum_{ij} a_{ij}w_{i}'w_{j}'` | `\sum_{i,j} a_{ij}w_{i}'w_{j}'` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). In (3.3.14) steht \sum_{i,j}; ebenso Z. 1768. |
| 215 | 1820 | ● | `\lambda \in \{ \sigma(A) \colon \Re(\lambda) < s(A)\}` | `\{\lambda \in \sigma(A) \colon \Re(\lambda) < s(A)\}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Mengenschreibweise ist verdreht. |
| 215 | 1835 | ◐ | `[$1^{st}$ part of the proof]` | `[First part of the proof]` | Mathemodus | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). „st“ steht kursiv im Mathemodus; alternativ `1\textsuperscript{st}`. |
| 215 | 1866 | ○ | `Example~\ref{ex:b3-2.6}(vi)` | `Example~\ref{ex:b3-2.6}\,(vi)` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst steht \, vor der Teilnummer; ebenso Z. 2249 (`\ref{prop:b3-4.8}(i)`). |
| 216 | 1879 | ○ | `\phi = (\phi_{t}): \R_{+} \times K \to K` | `\phi = (\phi_{t}) \colon \R_{+} \times K \to K` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Abbildungsdoppelpunkt ist sonst \colon (z. B. Z. 1366); ebenso Z. 2207, 2278, 2282. |
| 218 | 2029 | ◐ | `By the definition given in Eq.~\myeqpageref{eq:b3-4.1}` | `By the definition given in Eq.~\myeqpageref{eq:b3-4.4}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste. c_t(h,φ) ist in (3.4.4) definiert. |
| 219 | 2058 | ○ | `(A - \lambda)g_{n} = (1 - \eu^{-\lambda(n+1)}T(n+1))f_{n}` | `(\lambda - A)g_{n} = (\Id - \eu^{-\lambda(n+1)}T(n+1))f_{n}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Vorzeichen: (λ − A)∫_0^s e^{-λt}T(t)f dt = (Id − e^{-λs}T(s))f; bitte prüfen. |
| 219 | 2063 | ○ | `\dt \right\vert \geq\]` | `\begin{multline*} … \end{multline*}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Als `multline*`. Die Abschätzungskette ist auf vier getrennte \[…\] verteilt (Z. 2063–2071), die erste Zeile endet mit „\geq“; besser eine mehrzeilige Umgebung. |
| 219 | 2065 | ◐ | `\left\vert \eu^{-\lambda t}\vert h_{t}(y_{n})f_{n}(\phi(t,y_{n}))\right\vert` | `\left\vert \eu^{-\lambda t}h_{t}(y_{n})f_{n}(\phi(t,y_{n}))\right\vert` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Überzähliger Betragsstrich nach e^{-λt}. |
| 219 | 2075 | ● | `1/2\epsilon \cdot\left(\eu^{\epsilon n} - \eu^{\epsilon(n-1)})\right)` | `1/(2\epsilon)\cdot\left(\eu^{\epsilon n} - \eu^{\epsilon(n-1)}\right)` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Vor \right) steht eine überzählige „)“; außerdem ist „1/2ε“ mehrdeutig (vgl. 1/ε in Z. 2070). |
| 219 | 2093 | ◐ | `R{\sigma}(A_{/})` | `R\sigma(A_{/I_{\infty}})` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Index ist abgeschnitten (vgl. Z. 2097 `A_{/I_{\infty}}`); ebenso Z. 2094. |
| 219 | 2102 | ● | `\lambda = a + \im\beta$, $\alpha,\beta \in \R` | `\lambda = a + \im\beta$, $a,\beta \in \R` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). α statt a (vgl. Z. 2036). |
| 219 | 2102 | ◐ | `\|f\| = \|f(\phi(\tau,x_{f}))\|` | `\|f\| = \vert f(\phi(\tau,x_{f}))\vert` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Gemeint ist der Betrag einer Zahl, nicht eine Norm. |
| 220 | 2115 | ● | `\underbar{c}(h,\phi)` | `\underline{c}(h,\phi)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). \underbar (Textbefehl) statt \underline wie sonst; der Strich sitzt im Druck sichtbar anders. |
| 220 | 2115 | ◐ | `\exp(\underbar{c}(h,\phi)-2\epsilon)` | `\exp((\underline{c}(h,\phi)-2\epsilon)\tau)` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Für λ ∈ H_{2ε} hat e^{λτ} den Betrag e^{aτ}, der Faktor τ fehlt vermutlich; bitte prüfen. |
| 220 | 2147 | ◐ | `$(a)\implies(b)$` | `(a)~$\implies$~(b)` | Mathemodus | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Teilbezeichnungen (a), (b) stehen kursiv im Mathemodus, sonst aufrecht (vgl. Z. 1292); ebenso Z. 2149. |
| 220 | 2153 | ○ | `\phi\vert_{K_{\infty}}` | `\phi_{\vert K_{\infty}}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Einschränkung von φ steht sonst als `\phi_{\vert K_{\infty}}` (Z. 2018, 2021, 2091, 2215). |
| 221 | 2254 | ○ | `(see Proposition~\ref{prop:b3-4.8}\,(i))` | `(see Proposition~\ref{prop:b3-4.8}\,(ii)–(v))` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Teil (i) betrifft die rechte Halbebene (so schon in Z. 2249); die Teilantwort für den Mittelstreifen liefern (ii)–(v); bitte prüfen. |
| 222 | 2276 | ◐ | `\eu^{\mathcal{\im\omega}}` | `\eu^{\im\omega}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Überflüssiges \mathcal. |
| 222 | 2283 | ◐ | `corresponding to $\phi$ and $h$` | `corresponding to $\tilde{\phi}$ and $h$` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Fluss wurde in Z. 2280 als \tilde{\phi} eingeführt. |
| 223 | 2352 | ◐ | `\exp(-(h^{\star}+\im\beta )t)` | `\exp(-(\hat{h}+\im\beta )t)` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). h^⋆ statt ĥ (vgl. Z. 2348, 2371). |
| 224 | 2371 | ◐ | `& {= \frac{1}{n}\int_{0}^{n}` | `&= \frac{1}{n}\int_{0}^{n}` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die geschweifte Klammer um „= …“ unterdrückt den Abstand vor dem Gleichheitszeichen; ebenso Z. 2372. |
| 225 | 2424 | ◐ | `f(\phi(t,x)) \dt = \\` | `f(\phi(t,x)) \dt \\` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Das Gleichheitszeichen steht doppelt (am Zeilenende und am Anfang der nächsten Zeile); ebenso Z. 2425. |
| 226 | 2484 | ○ | `\im\cdot 2\pi k/\tau_{x} \colon x \in X, 0 < \tau_{x} < \infty` | `\im\cdot 2\pi k/\tau_{x} \colon k \in \Z, x \in X, 0 < \tau_{x} < \infty` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Der Laufbereich von k fehlt (vgl. Z. 2449). |
| 226 | 2537 | ◐ | `Example~\ref{ex:b3-3.4}\,(iii)` | `Example~\ref{ex:b3-2.14}\,(ii)` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Section 4.3 behandelt retardierte Gleichungen, 3.3.4 (iii) ist dagegen die erste Ableitung. Gemeint ist vermutlich Beispiel 3.2.14 (ii) (Notes zu Section 2, vgl. Remark 3.2.15 (iv)) oder 3.3.4 (iv); bitte prüfen. |
| 226 | 2541 | ◐ | `as defined in~\ref{def:b3-3.1}` | `as defined in Definition~\ref{def:b3-3.1}` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Die Bezeichnung fehlt, gedruckt wird nur „3.3.1“. |
| 226 | 2547 | ○ | `(more general than Example~\ref{ex:b3-3.4}\,(ii))` | `(more general than Example~\ref{ex:b3-3.4}\,(v))` | Verweis | **Umgesetzt, abweichend** (20.10.2026, Entscheidung G. Greiner): Verweis auf Example~3.3.10\,(ii) (`ex:b3-3.10`). 3.3.4 (ii) behandelt Kernoperatoren, elliptische Operatoren stehen in (v)/(vi) bzw. in Beispiel 3.3.10 (ii); bitte prüfen. |

### Teil II, Kap. 4 – Asymptotics of Positive Semigroups on C₀(X) (`part-b/chap-b4.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 231 | 14 | ◐ | `Part-I, Chapter~\ref{chap:a1} and Chapter~\ref{chap:b2}` | `Part-I, Chapter~\ref{chap:a3} and Chapter~\ref{chap:b3}` | Verweis | „results … on the spectrum of the generator“: die Spektraltheorie steht in Kap. 3 (a3/b3), nicht in a1 (Basic Results) bzw. b2 (Characterization); bitte prüfen. |
| 232 | 65 | ● | `P\sigma(A')$ , and` | `P\sigma(A')$, and` | Abstand | Leerzeichen vor Komma nach Formel; ebenso Z. 270 (`C_{0}(X)''$ ,`), 1462 und 1464 (`\lambda$ , then`). |
| 232 | 76 | ◐ | `from Section~\ref{subsec:a3-4.4}` | `from Part-I, Section~\ref{subsec:a3-4.4}` | Verweis | Schon in der Arbeitsliste. Ziel ist der Part-I-Unterabschnitt „Spectrum of the adjoint semigroup“; Präfix „Part-I,“ fehlt, Ziel bitte prüfen. |
| 232 | 77 | ◐ | `$(c) \Rightarrow (a)$` | `(c)~$\Rightarrow$~(a)` | Notation | **Teilweise umgesetzt** (20.10.2026, Freigabe G. Greiner für Abschnitt 4.2): Stellen in Abschnitt 4.2 erledigt (Z. 622, 632, 652, 663, 667, 815, 817, 819, 824, 940); Z. 77, 1569, 1571 offen. Aufzählungslabels sind aufrecht (\upshape), im Mathemodus erscheinen sie kursiv; im Fließtext sonst aufrecht („condition (c)“, Z. 647). Ebenso Z. 622, 632, 652, 663, 667, 815, 817, 819, 824, 940 (`$(i)$`, `$(ii)$`), 1569, 1571. |
| 232 | 133 | ◐ | `\C\backslash\{0\}` | `\C\setminus\{0\}` | Notation | **Teilweise umgesetzt** (20.10.2026, Freigabe G. Greiner für Abschnitt 4.2): Z. 757, 758 erledigt; Z. 133, 140 offen. Mengendifferenz uneinheitlich: \backslash hier, \setminus (= \smallsetminus) in Z. 1667; ebenso Z. 140, 757, 758. |
| 232 | 151 | ● | `\dot{r} &= 1 - r~,` | `\dot{r} &= 1 - r,` | LaTeX | Tilde im Mathemodus erzeugt sichtbaren Zwischenraum; ebenso Z. 1284 (`(0)~\in~F`), 1408 (`\lambda~>~\|\Phi\|+w`), 1466 (`B~+~\Phi_{\lambda'})~\neq~\emptyset`). |
| 232 | 204 | ◐ | `\langle f,\mu \rangle \,=\, \eu^{\im\alpha t}\langle f,T(t)'\mu \rangle` | `\langle f,\mu \rangle \,=\, \eu^{-\im\alpha t}\langle f,T(t)'\mu \rangle` | Tippfehler | Aus $T(t)'\mu = \eu^{\im\alpha t}\mu$ folgt der Faktor $\eu^{-\im\alpha t}$ (so auch Z. 210); betrifft beide Faktoren der Zeile; bitte prüfen. |
| 232 | 240 | ○ | `thus \,$R(\lambda,A)'^2E'` | `thus $R(\lambda,A)'^2E'` | Abstand | \, vor der Formel vergrößert den Wortabstand sichtbar. |
| 234 | 263 | ◐ | `Part-I, Definition~\ref{def:a2-1.11}` | `Part-I, Proposition~\ref{prop:a1-1.11}` | Verweis | Definition 2.1.11 definiert holomorphe Halbgruppen; die benutzte Darstellung von $R(1,A^*)^{n+1}$ als Integral steht in Prop. 1.1.11, Eq. (1.1.7) (eq:a1-1.7); bitte prüfen. |
| 235 | 273 | ◐ | `\int_0^{\infty} \langle T(t)^*\phi,\rho \rangle \dt` | `\int_0^{\infty} \langle T(t)^*\phi,\rho \rangle \dt .` | Satzzeichen | Satzende nach abgesetzter Formel, Punkt fehlt (nächster Satz beginnt mit „Since“); ebenso Z. 541 (`\lambda_1 = r` → `\lambda_1 = r .`, danach „Now …“). |
| 235 | 313 | ● | `for r  >  0.` | `for $r > 0$.` | Mathemodus | Variable und Relation ohne Mathemodus. |
| 235 | 318 | ◐ | `\int_0^{\infty} \|T(t)\mu\| \dt` | `\int_0^{\infty} \|T(t)^*\mu\| \dt` | Tippfehler | Stern fehlt, vgl. Z. 311 und linke Seite derselben Formel. |
| 235 | 345 | ○ | `\|T(t)'\mu_n\|` | `\|T(t)^*\mu_n\|` | Notation | In Z. 331 und 337 steht $T(t)^*\mu_n$, hier und Z. 346 $T(t)'\mu_n$; vereinheitlichen. |
| 235 | 352 | ◐ | `t \to \|T(t)'\mu\|` | `t \mapsto \|T(t)'\mu\|` | Notation | Abbildungsvorschrift, sonst \mapsto (z. B. Z. 864). |
| 235 | 354 | ◐ | `Part-I, Proposition~\ref{prop:a3-4.4}\,(iii)` | `Part-I, Section~\ref{subsec:a3-4.4}\,(iii)` | Verweis | Prop. 3.4.4 (F-Produkt) hat nur (i), (ii); $\omega_0(A)=\omega_0(A^*)$ steht als (iii) im Unterabschnitt „Spectrum of the adjoint semigroup“ (subsec:a3-4.4); bitte prüfen. |
| 237 | 412 | ● | `\exp((\epsilon +\Re(\lambda_m))t) \text{ for }  t \geq 0, \epsilon >0\\` | `\exp((\epsilon +\Re(\lambda_m))t)\\` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). „for t ≥ 0, ε > 0“ steht doppelt (Z. 412 und 413). |
| 237 | 434 | ○ | `\{z \in \sigma(T(t_{0})) :` | `\{z \in \sigma(T(t_{0})) \colon` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst \colon in Mengenschreibweise (z. B. Z. 423); „:“ ergibt anderen Abstand. |
| 237 | 439 | ● | `\sigma(T(t_{0})_{\vert \Kern{P}} \subseteq` | `\sigma(T(t_{0})_{\vert \Kern{P}}) \subseteq` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schließende Klammer zu $\sigma($ fehlt. |
| 237 | 455 | ◐ | `f \in P_n E` | `f \in P_n G` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Theorem 4.2.1 spricht vom Banachraum $G$, der Beweis benutzt $E$; ebenso Z. 456 (`E = P_n E`). |
| 237 | 455 | ○ | `P_n E = \ker(\lambda_n-A)` | `P_n E = \ker(\lambda_n-A)^{k(n)}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Bild des Residuums ist der verallgemeinerte Eigenraum (vgl. Z. 458: $(\lambda-A)^k=0$); bitte prüfen. |
| 237 | 482 | ● | `follows from Eq.~\myeqpageref{eq:a2-1.3}` | `follows from Part-I, Eq.~\myeqpageref{eq:a2-1.3}.` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Satzpunkt am Beweisende fehlt; zudem Part-I-Gleichung ohne „Part-I,“ (vgl. auskommentierte Fassung Z. 501). |
| 238 | 529 | ○ | `Proposition~\ref{prop:b3-3.5}(i)` | `Proposition~\ref{prop:b3-3.5}\,(i)` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst überall `\,(i)` nach \ref. |
| 239 | 589 | ◐ | `C(K) \not\subseteq B(K) \not\subseteq C(K)''` | `C(K) \subsetneq B(K) \subsetneq C(K)''` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). $B(K)$ wird unmittelbar davor als Teilraum von $C(K)''$ identifiziert; gemeint sind wohl echte Inklusionen; bitte prüfen. |
| 239 | 605 | ○ | `R''(\1_C) \in G$,` | `R''(\1_C) \in G$.` | Satzzeichen | **Bereits erledigt** (der Punkt stand schon im Quelltext). Letzter Punkt der Aufzählung endet mit Komma, danach beginnt ein neuer Satz („In case …“). |
| 239 | 647 | ○ | `$\{R'y' \colon y' \in G'$, $\|y'\| \leq 1\}$` | `$\{R'y' \colon y' \in G',\ \|y'\| \leq 1\}$` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Mengenklammer auf zwei Formeln verteilt (\{ und \} in getrennten $…$, über Z. 647/648); ebenso Z. 662. |
| 241 | 713 | ◐ | `P_t(x,.)` | `P_t(x,\cdot)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Punkt als Platzhalter; sonst \cdot (z. B. Z. 555 `T(\cdot)f`); ebenso Z. 716 (`P_t(.,C)`), 770. |
| 242 | 807 | ○ | `\omega_{\text{ess}}(\TT)` | `\omega_{\mathrm{ess}}(\TT)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). In der kursiven Proposition wird \text{ess} kursiv gesetzt, im Fließtext (Z. 797, 821) aufrecht. |
| 242 | 846 | ○ | `\text{exp}(-\omega_{0}(\TT)t)` | `\exp(-\omega_{0}(\TT)t)` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst \exp (z. B. Z. 937). |
| 243 | 893 | ○ | `nonneg<U+00AD>ative` | `nonnegative` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Unsichtbares weiches Trennzeichen (U+00AD) im Quelltext. |
| 243 | 895 | ◐ | `k_1, \dots, k_m` | `k(1), \dots, k(m)` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Polordnungen in Eq. (4.2.1) als $k(n)$, in Theorem 4.2.10 als $k_n$; ebenso Z. 899 (`k_n - 1`). |
| 244 | 899 | ● | `e^{\lambda_n t}` | `\eu^{\lambda_n t}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Kursives e; im Kapitel sonst \eu bzw. \exp. |
| 244 | 910 | ● | `\omega_{ess}(\TT) < 0$, hence $r_{ess}(T(1))` | `\omega_{\text{ess}}(\TT) < 0$, hence $r_{\text{ess}}(T(1))` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). „ess“ als kursives Produkt gesetzt; sonst \text{ess}. |
| 244 | 914 | ○ | `P = P_1+P_2+ \ldots +P_m` | `P = P_1 + P_2 + \dots + P_m` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Grundlinienpunkte zwischen Operationszeichen; sonst \cdots bzw. \dots (Z. 409, 898). |
| 245 | 1008 | ◐ | `\alpha g(0)` | `\alpha g_r(0)` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Index $r$ fehlt. |
| 245 | 1018 | ● | `m(z) \, dz` | `m(z) \,\diff{z}` | Notation | **Teilweise umgesetzt** (20.10.2026, Freigabe G. Greiner für Abschnitt 4.2): Z. 1018 erledigt; Z. 1292 und 1758 (außerhalb von Abschnitt 4.2) offen. Kursives d; sonst \diff (vgl. Z. 1014). Ebenso Z. 1292 (`\frac{d}{ds}`) und 1758 (`\frac{d}{dt}`) → `\frac{\mathrm{d}}{\mathrm{d}s}` usw. |
| 246 | 1039 | ● | `\begin{equation*}\label{eq:b4-2.12}` | `\begin{equation}\label{eq:b4-2.12}` | Verweis | **Umgesetzt, Alternative** (20.10.2026, Entscheidung G. Greiner): Z. 1818 verweist jetzt auf Proposition~\ref{prop:b4-2.13}; Z. 1039 unverändert. \label in equation* ohne \tag übernimmt die Nummer der Proposition (4.2.13); der Verweis Z. 1818 „Eq. (4.2.13)“ zeigt auf keine Gleichung. Alternativ in Z. 1818 auf Proposition~\ref{prop:b4-2.13} verweisen. |
| 247 | 1143 | ◐ | `\textit{if }` | `\text{if }` | Notation | In (T) (Z. 1126) und Z. 1221 aufrechtes „if“; ebenso Z. 1144. |
| 247 | 1145 | ● | `\end{cases}\quad, \quad` | `\end{cases}, \quad` | Abstand | Geviert vor dem Komma; vgl. Z. 1128. |
| 249 | 1257 | ◐ | `\dot{w}(0) = \dot{w}(t)` | `\dot{w}_t(0) = \dot{w}(t)` | Tippfehler | Für $x(t)\in D(A)$ wird die Ableitung von $w_t$ an der Stelle 0 gebraucht; bitte prüfen. |
| 251 | 1355 | ◐ | `\Phi(e_\lambda \otimes x)` | `\Phi(\epsilon_\lambda \otimes x)` | Notation | Die Funktion $s\mapsto\eu^{\lambda s}$ ist in Z. 1157 als $\epsilon_\lambda$ eingeführt und wird so verwendet (Z. 1391, 1408, 1592); ebenso Z. 1380 (`e_\mu`), 1789 (`e_{\lambda}`). |
| 251 | 1355 | ◐ | `\Phi(e_\lambda \otimes x) \, , \, x \in F \, .` | `\Phi(e_\lambda \otimes x), \quad x \in F .` | Abstand | Schmaler Abstand vor Komma und Punkt; ebenso Z. 1605 und 1606 (`\, , \ &&`), 1619 (`0\, ,`). |
| 252 | 1422 | ● | `supp$(f) \subseteq [-\delta,0])$` | `$\operatorname{supp}(f) \subseteq [-\delta,0]$)` | Mathemodus | „supp“ außerhalb des Mathemodus; die schließende Textklammer steht im Mathemodus. |
| 253 | 1441 | ● | `0 \leq R(t, B +\Phi_\mu) \leq R(t,B+\Phi_\mu)` | `0 \leq R(t, B +\Phi_\mu) \leq R(t,B+\Phi_\lambda)` | Tippfehler | Beide Seiten identisch; aus $\Phi_\mu \leq \Phi_\lambda$ folgt die Abschätzung durch die von $B+\Phi_\lambda$ erzeugte Halbgruppe (vgl. Z. 1444f.); bitte prüfen. |
| 253 | 1482 | ● | `Theorem~\ref{thm:c3-1.1}.\,(i)` | `Theorem~\ref{thm:c3-1.1}\,(i)` | Satzzeichen | Schon in der Arbeitsliste. Überzähliger Punkt vor (i). |
| 256 | 1645 | ○ | `-\tau \leq t \leq 0 , \Psi \in C[-\tau,0]` | `-\tau \leq t \leq 0 ,\ \Psi \in C[-\tau,0]` | Abstand | Zu knapper Abstand nach dem Komma, vgl. Z. 1606 (`, \ \psi \in E`). |
| 256 | 1665 | ● | `$Eq.~\eqref{eq:b4-3.9}$` | `Eq.~\eqref{eq:b4-3.9}` | Mathemodus | „Eq.“ im Mathemodus (kursiv, Tilde in der Formel). |
| 257 | 1705 | ○ | `\begin{equation}\label{eq:b4-3.11}` | `Label auf die Gleichung Z. 1698–1701 setzen` | Verweis | Das Label sitzt auf der Randbedingung; „solution (semigroup) of Eq. (4.3.11)“ in Z. 1727, 1735, 1740 meint aber das ganze Problem; bitte prüfen. |
| 258 | 1753 | ○ | `F = L^1([a,1])` | `F = L^1[a,1]` | Notation | Gleich danach (Z. 1763) $L^1[a,1]$, $AC[a,1]$, $C[a,1]$. |
| 258 | 1759 | ◐ | `u &= \Psi \in E.` | `u_0 &= \Psi \in E.` | Tippfehler | Anfangsbedingung betrifft das Historiensegment, vgl. Z. 1090, 1722. |
| 258 | 1768 | ○ | `[a,1/2(r+1)]` | `[a,(r+1)/2]` | Notation | Mehrdeutig (lesbar als $1/(2(r+1))$); ebenso Z. 1769. |
| 258 | 1805 | ◐ | `C*-algebras` | `\CA-algebras` | Notation | Sonst \CA ($\mathrm{C}^{*}$), vgl. Z. 367. |
| 258 | 1807 | ● | `\textcite[V.8.8]{schaefer:1974}.` | `\textcite[V.8.8]{schaefer:1974}).` | Klammern | Schließende Klammer zu „(see“ (Z. 1806) fehlt. |
| 258 | 1811 | ◐ | `Theorem~\ref{thm:b4-1.1} seems to be folklore` | `Theorem~\ref{thm:b4-2.1} seems to be folklore` | Verweis | Schon in der Arbeitsliste. Notes zu Section 2; gemeint ist wohl Theorem 4.2.1. |

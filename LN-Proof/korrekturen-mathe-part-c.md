# Formelprüfung Part C (Teil III): Satz und Notation

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184). Geprüft am 14.10.2026; Stand der Umsetzung: 20.10.2026.

**Umfang:** Teil III, Kap. 1–4, geprüft im LaTeX-Quelltext (Branch `fahnenkorrektur`). Geprüft wurden nur Satz und Notation in Formeln: Tippfehler, Klammern, Indizes, uneinheitliche Schreibweisen, Mathemodus, Satzzeichen an Formeln, Verweise. Beweise wurden **nicht** nachgerechnet; wo ein Befund inhaltlich wirkt, steht „bitte prüfen“.

**Stand 20.10.2026:** **Kap. 1 und Kap. 2 sind erledigt** (Kap. 1 nach Durchsicht durch Rainer Nagel; in der Spalte Kommentar mit **Umgesetzt** markiert, Abweichungen ebenda). Kap. 3–4 sind noch offen. Die Zeilenangaben beziehen sich auf den Stand vom 14.10.2026.

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

**Spalten:** S. = gedruckte Buchseite, ermittelt über das nächstgelegene Label (kann um eine Seite abweichen). Z. = Zeile in der .tex-Datei. Sicherheit: ● eindeutig · ◐ sehr wahrscheinlich · ○ Hinweis/Ermessen.

Insgesamt **222 Punkte**: 47 ●, 99 ◐, 76 ○. Davon stehen 26 bereits in der Arbeitsliste `Fahnenkorrektur_Springer_LNM1184.md` (im Kommentar markiert).

## Einzelbefunde

### Teil III, Kap. 1 – Basic Results on Banach Lattices and Positive Operators (`part-c/chap-c1.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 265 | 35 | ◐ | `\mathrm{(LO1)} \quad` | `\text{(LO$_{1}$)} \quad` | Notation | **Umgesetzt.** In der Definition „(LO1)“/„(LO2)“ ohne Index, im Fließtext Z. 45, 46, 49 „(LO$_{1}$)“/„(LO$_{2}$)“ mit tiefgestellter Ziffer, im Druck sichtbar verschieden; ebenso Z. 37 `\mathrm{(LO2)}`. Alternativ Z. 45–49 auf (LO1)/(LO2) umstellen. |
| 265 | 71 | ● | `\inf   \sup_{\alpha} f_{\alpha},h  )` | `\inf(\sup_{\alpha} f_{\alpha},h)` | Klammern | **Umgesetzt.** Öffnende Klammer nach \inf fehlt (vgl. die Parallelformel Z. 72 `\sup(\inf_{\alpha}f_{\alpha},h)`). |
| 266 | 79 | ○ | `\begin{equation*}\label{eq:c1-1}` | `\begin{equation*}` | LaTeX | **Umgesetzt.** \label in einer unnummerierten Umgebung; das Label wird nirgends referenziert (ein \ref würde die Abschnittsnummer liefern). Ebenso Z. 267 (eq:c1-2) und Z. 275 (eq:c1-3). Im Druck unsichtbar, nur Bereinigung. |
| 269 | 206 | ○ | `\{u\}^{d} = 0` | `\{u\}^{d} = \{0\}` | Notation | **Umgesetzt.** Gleichheit von Mengen; sonst im Kapitel `= \{0\}` (Z. 180, 368). |
| 270 | 245 | ◐ | `\sup\{\phi(h) \colon \vert h\vert \leq f \text{ for $ f \in E_{+} $}\}` | `\sup\{\phi(h) \colon \vert h\vert \leq f\} \quad \text{for $ f \in E_{+} $}` | Notation | **Umgesetzt.** Die Bedingung „for f ∈ E₊“ steht innerhalb der Mengenklammer, betrifft aber die feste Variable f, nicht die Laufvariable h; gehört hinter die Menge. Ebenso Z. 384 (`\vert h\vert \leq f , \text{ $ f \in E_{+} $} \}`) und Z. 529 (`\text{ for $ h \geq 0 $} \}`). |
| 271 | 276 | ○ | `g \in E_{+}'` | `g \in E'_{+}` | Notation | **Umgesetzt.** Strich hinter dem Index gesetzt; in Teil III sonst durchweg E'_{+} (z. B. chap-c2 Z. 61, 415, 488, 568). |
| 271 | 302 | ◐ | `which we denote by $ (E,x') $` | `which we denote by $ (E,f') $` | Tippfehler | **Umgesetzt.** Das Funktional heißt im Kontext f' (q_{f'}), ein x' kommt nicht vor; vgl. Z. 305 `(E,\mu)`. Bitte prüfen. |
| 273 | 371 | ◐ | `\mathcal{L}^{r}(E;F)` | `\mathcal{L}^{r}(E,F)` | Notation | **Umgesetzt.** Semikolon als Trenner, während im selben Absatz `\L{E,F}` mit Komma steht (Z. 369, 372, 373, 475); sichtbar uneinheitlich. Ebenso Z. 372, 373, 374, 381. |
| 273 | 435 | ● | `$ h = f + ig $` | `$ h = f + \iu g $` | Notation | **Umgesetzt.** Kursives i für die imaginäre Einheit; sonst \iu/\im (aufrecht), z. B. Z. 428, 438, 446, 450, 461. Ebenso Z. 474 `T_{1} + iT_{2}` und Z. 533 `+ i(S_{3} - S_{4})`. |
| 273 | 476 | ◐ | `if\/ $ T_{2} $ is $ = 0 $` | `if\/ $ T_{2} = 0 $` | Mathemodus | **Umgesetzt** (stand schon so im Text). Schon in der Arbeitsliste. Relationszeichen allein im Mathemodus nach „is“. Ähnlich Z. 524 `one has necessarily the values $ = 0 $ for $ S_{f} $` (besser: „one has necessarily $ S_{f} = 0 $“). |
| 275 | 508 | ○ | `\text{sign } f = f\cdot\vert f\vert^{-1}` | `\sign f = f\cdot\vert f\vert^{-1}` | Notation | **Umgesetzt.** In Z. 485 mit dem Operator \sign gesetzt; \text{sign } übernimmt die Umgebungsschrift und hat anderen Abstand. |
| 275 | 520 | ◐ | `the band $ \{x\}^{dd} $` | `the band $ \{f\}^{dd} $` | Tippfehler | **Umgesetzt** (vorgezogen zusammen mit math-error Z. 529; Rainer ohne Einwand). Ein Element x kommt im Kontext nicht vor, gemeint ist das Band zu f. Ebenso Z. 524 `\{x\}^{d}` und Z. 527 `\{x\}^{dd}`. Bitte prüfen. |
| 275 | 529 | ○ | `S_{f}h = \sup \{ S_{f}g \colon` | `S_{f}h = \sup \{ S_{0}g \colon` | Tippfehler | **Umgesetzt** (stand schon so im Text). S_f wird hier erst definiert; rechts ist wohl S_0 gemeint (g ∈ E_{\vert f\vert}). Bitte prüfen. |
| 276 | 579 | ● | `then $ Z(E) $ is isomorphic` | `then $ \mathcal{Z}(E) $ is isomorphic` | Notation | **Umgesetzt.** Zentrum sonst kalligraphisch \mathcal{Z}(E) (Z. 572, 573, 575, 582). |

### Teil III, Kap. 2 – Characterization of Positive Semigroups on Banach Lattices (`part-c/chap-c2.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 280 | 57 | ○ | `(see Eq.~\myeqpageref{eq:a2-2.12})` | `(see Part-I, Eq.~\myeqpageref{eq:a2-2.12})` | Verweis | **Umgesetzt.** Formel aus Teil I ohne „Part-I,“ zitiert; das Kapitel hat eigene Formeln (2.2.x), die Nummer ist nur über die Seitenangabe eindeutig. Ebenso Z. 64 (eq:a2-2.5). |
| 280 | 61 | ◐ | `\partial N^{+}(f)` | `\diff{N^{+}}(f)` | Notation | **Umgesetzt.** Subdifferential uneinheitlich: ∂N⁺(f) in Z. 61, 76, 95, 215, dagegen dN⁺(f) mit aufrechtem d (\diff) in Z. 91, 106, 181, 227, 250, 253, 487 und \ddp(f) in Z. 1094, 1106, 1596. Teil I schreibt \ddp, daher Vereinheitlichung auf d vorgeschlagen; ebenso Z. 76, 95, 215. |
| 280 | 64 | ◐ | `see Eq.~\myeqpageref{eq:a2-2.5}.` | `see Eq.~\myeqpageref{eq:a2-2.5}).` | Klammern | **Umgesetzt.** Schon in der Arbeitsliste. Die mit „(this follows …“ geöffnete Klammer wird nicht geschlossen. |
| 281 | 190 | ◐ | `C^{2}[0,1]` | `C^{2}([0,1])` | Notation | **Umgesetzt.** Sonst im Kapitel C^{2}([0,1]), L^{p}([0,1]), AC([0,1]); ebenso Z. 1287 (`L^{q}[0,1]`) und Z. 2074, 2123, 2136 (`C[-1,0]`, `C^{1}[-1,0]` gegenüber `C^{1}([-1,0],\C)` in Z. 2046, 2055). |
| 281 | 216 | ● | `\ref{ex:c2-1.1},~\ref{ex:c2-1.1-2} )` | `\ref{ex:c2-1.1}\,\ref{ex:c2-1.1-2})` | Abstand | **Umgesetzt.** Leerzeichen vor der schließenden Klammer; außerdem sonst „Example~\ref{…}\,\ref{…}“ ohne Komma (Z. 1786, 1792, 2243). |
| 281 | 252 | ◐ | `f(x) = \|f\|_{\infty}` | `f(x) = \|f^{+}\|_{\infty}` | Tippfehler | **Umgesetzt.** bitte prüfen: Das Maximum von f ist ‖f⁺‖∞ (vgl. Z. 75, 179), nicht ‖f‖∞. |
| 283 | 264 | ● | `(1 + \sum_{i=1}^{n} y_{i}^{2})g(y), g \in \mathcal{S}(\R^{n})) .` | `(1 + \sum_{i=1}^{n} y_{i}^{2})g(y) \quad (g \in \mathcal{S}(\R^{n})) .` | Klammern | **Umgesetzt.** Überzählige schließende Klammer; die Nebenbedingung gehört offenbar in Klammern. |
| 283 | 308 | ◐ | `\,$C_{c}^{\infty}(\R^{n})$\, is dense in \,$\mathcal{S}$\,` | `$C_{c}^{\infty}(\R^{n})$ is dense in $\mathcal{S}$` | Abstand | **Umgesetzt.** Die manuellen \, um die Inline-Formeln vergrößern die Wortabstände sichtbar. |
| 283 | 317 | ● | `\phi \in S` | `\phi \in \mathcal{S}` | Notation | **Umgesetzt.** Der Schwartz-Raum heißt sonst \mathcal{S} (Z. 286, 314). |
| 284 | 340 | ○ | `u(x) - \Delta u(x) &= 0 \quad &(x \in \Omega)` | `\begin{array}{r@{\;}l@{\quad}l}` | Abstand | **Umgesetzt.** Mit `aligned` gelöst (ebenso Z. 1286). Im array steht vor dem „=“ der Spaltenabstand 2\arraycolsep (10 pt), dahinter nur der normale Relationsabstand. Alternativ aligned mit &=. Ebenso Z. 1286 ({rl}, `D(A') &= …`). |
| 284 | 381 | ◐ | `f \in C^{2}(\Omega) \cap C(\Omega)` | `f \in C^{2}(\Omega) \cap C(\overline{\Omega})` | Tippfehler | **Umgesetzt.** bitte prüfen: C(Ω) ist in C²(Ω) bereits enthalten; aus f̄ ∈ 𝒮 und u ∈ C(Ω̄) folgt f ∈ C(Ω̄) (vgl. Z. 376). |
| 284 | 399 | ◐ | `We know from~\ref{ex:c2-1.5-4}` | `We know from~\ref{ex:c2-1.5-5}` | Verweis | **Umgesetzt.** Schon in der Arbeitsliste. Die Aussage wird im Beweis von (v) gezeigt. |
| 285 | 426 | ● | `$E = C(K)$ (K compact)` | `$E = C(K)$ ($K$ compact)` | Mathemodus | **Umgesetzt.** K steht nicht im Mathemodus; ebenso Z. 2024 (`(X locally compact)`), Z. 2399 (`Assume that E is`), Z. 2885 (`(K compact)`). |
| 286 | 518 | ◐ | `\lim_{n \to \infty} \|u - (n u \wedge g)\| = 0` | `\lim_{n \to \infty} \|g - (n u \wedge g)\| = 0` | Tippfehler | **Umgesetzt.** bitte prüfen: g liegt genau dann im Abschluss von E_u, wenn nu ∧ g gegen g konvergiert. |
| 286 | 525 | ◐ | `(Au)^{-} \in E_{u}` | `(Au)^{-} \in \overline{E_{u}}` | Tippfehler | **Umgesetzt.** bitte prüfen: Der Beweis (Z. 532, 536) und Theorem 2.1.11 (c) (Z. 571) verwenden den Abschluss. |
| 286 | 532 | ○ | `\overline{E}_{u}` | `\overline{E_{u}}` | Notation | **Umgesetzt.** Z. 532, 533, 536 (3 Stellen). Querstrich hier nur über E, sonst über E_u bzw. E_f (Z. 518, 571, 1378); ebenso Z. 533 (2×) und 536. |
| 286 | 533 | ○ | `0 \leq \phi \in E_{+}'` | `0 \leq \phi \in E'_{+}` | Notation | **Umgesetzt.** Sonst durchgehend E'_{+}; im Druck steht der Strich hier hinter dem Index. |
| 287 | 571 | ○ | `\overline{E_{f}}$ \ for all` | `\overline{E_{f}}$ for all` | Abstand | **Umgesetzt.** Leerzeichen plus „\ “ ergibt doppelten Wortabstand; ebenso Z. 1848 (`\text{for }\ 0`). |
| 287 | 610 | ◐ | `Pg = g^{-} < 0` | `Pg = -g^{-} < 0` | Tippfehler | **Umgesetzt.** bitte prüfen: g⁻ ≥ 0; P projiziert auf das von g⁻ erzeugte Band, also Pg = −g⁻. |
| 288 | 653 | ● | `the $n^{th}$ unit vector` | `the $n$th unit vector` | Mathemodus | **Umgesetzt.** „th“ wird als kursives Variablenprodukt im Exponenten gesetzt. |
| 288 | 671 | ◐ | `linear operator (sign $f$) on $E$` | `linear operator $(\sign f)$ on $E$` | Notation | **Umgesetzt.** Im kursiven Satztext erscheint „sign“ kursiv, sonst überall aufrecht als \sign. |
| 289 | 720 | ◐ | `(\sign f)g = m \cdot g \quad (g \in E), ` | `(\sign f)g = m \cdot g \quad (g \in E).` | Satzzeichen | **Umgesetzt.** Nach der Formel beginnt ein neuer Satz („Moreover,“). |
| 289 | 750 | ○ | `\Re\left(\widehat{\sign} \bar{f}\right)g` | `\Re\left((\widehat{\sign} \bar{f})g\right)` | Klammern | **Umgesetzt.** So steht der Realteil des Operators statt des Elements; in Z. 2450 dieselbe Formel als \Re((ŝign f̄)g). Ebenso Z. 2491, 2526, 2564, 2566. |
| 290 | 799 | ○ | `\begin{equation*}\label{eq:c2-K-2}` | `\begin{equation*}` | LaTeX | **Umgesetzt.** \label in unnummerierter Formel ohne \tag, nirgends referenziert; ebenso Z. 1355 (eq:c2-3-KGK). Im Druck unsichtbar, nur Bereinigung. |
| 291 | 848 | ● | `\langle \phi,\Delta\vert f\vert \rangle (= \langle \Delta \phi,\vert f\vert \rangle` | `\langle \phi,\Delta\vert f\vert \rangle \;(= \langle \Delta \phi,\vert f\vert \rangle)` | Klammern | **Umgesetzt.** Die mit „(=“ geöffnete Klammer wird nicht geschlossen. |
| 291 | 851 | ● | `$(1~\leq~p <~\infty)$` | `$(1 \leq p < \infty)$` | Abstand | **Umgesetzt.** Tilden im Mathemodus erzeugen zusätzliche Wortabstände; ebenso Z. 1412 (`-\phi^{(3)}(x)~\leq~\phi(x)`) und Z. 1422 (`f~\in~D(B)`). |
| 291 | 884 | ○ | `C_{c}^{\infty} \subseteq D_{0}` | `C_{c}^{\infty}(\R^n) \subseteq D_{0}` | Notation | **Umgesetzt.** Im übrigen Absatz C_c^∞(R^n); die Kurzform C_c^∞ wird erst in Z. 1792 eingeführt. |
| 291 | 893 | ● | `\Re\langle(\sign \bar{f})Af),\phi \rangle` | `\Re\langle(\sign \bar{f})Af,\phi \rangle` | Klammern | **Umgesetzt.** Überzählige „)“. |
| 291 | 894 | ◐ | `\leq \langle \vert f\vert,A'\phi \rangle & = \langle` | `&\leq \langle \vert f\vert,A'\phi \rangle = \langle` | LaTeX | **Umgesetzt.** Das & der zweiten Zeile steht an der falschen Stelle; das „≤“ wird nicht unter dem „=“ der ersten Zeile ausgerichtet. |
| 292 | 901 | ◐ | `\sum_{i,j=1}^{2} b_{ij}` | `\sum_{i,j=1}^{n} b_{ij}` | Tippfehler | **Umgesetzt.** bitte prüfen: Der Operator wirkt auf dem R^n; die obere Grenze 2 ist vermutlich mit der Ordnung m ≤ 2 verwechselt. |
| 294 | 1032 | ◐ | `Definition~\ref{def:b3-3.1}` | `Definition~\ref{def:c3-3.1}` | Verweis | **Umgesetzt.** bitte prüfen: def:b3-3.1 ist die Irreduzibilität auf C_0(X) in Teil II (hier ohne „Part-II,“); für Banachverbände gibt es Definition 3.3.1 in Teil III (def:c3-3.1). Gedruckte Nummer gleich, Link und Seitenbezug führen aber nach Teil II. |
| 294 | 1053 | ◐ | `f \in D_{0} \, ,  \phi \in M'` | `f \in D_{0}, \phi \in M'` | Abstand | **Umgesetzt.** Sichtbarer Abstand vor dem Komma (vgl. die gleiche Formel in Z. 1205). |
| 295 | 1087 | ○ | `P_{+} \coloneq P_{f^{+}}` | `P_{+} \coloneq P_{(f^{+})}` | Notation | **Umgesetzt.** Bandprojektion teils P_{(f^{+})} (Z. 700, 1182, 1187, 1740, 1823), teils P_{f^{+}} (Z. 1087, 1932, 2658); einheitlich setzen. |
| 295 | 1089 | ◐ | `Q \coloneq P_{+} + 1/2` | `Q \coloneq P_{+} + 1/2\,P` | Tippfehler | **Umgesetzt.** bitte prüfen: Nach Z. 1104 ist Qf = P₊f + ½Pf; „+ 1/2“ allein ergäbe auch nicht Q ≤ Id. |
| 295 | 1139 | ● | `\text{ and } t\geq 0) .` | `\text{ and } t\geq 0 .` | Klammern | **Umgesetzt.** Überzählige „)“. |
| 297 | 1260 | ● | `f(1) = \diff{}f(0)` | `f(1) = d f(0)` | Tippfehler | **Umgesetzt.** \diff{} setzt das aufrechte Differential-d; gemeint ist die Konstante d ∈ R aus Z. 1256 (vgl. φ(0) = dφ(1) in Z. 1287). |
| 297 | 1266 | ○ | `(n \in \N )` | `(n \in \N_{0})` | Tippfehler | **Umgesetzt.** bitte prüfen: Für 0 ≤ x+t < 1 wird n = 0 gebraucht; \N_0 ist in Z. 872 eingeführt. |
| 298 | 1288 | ◐ | `\text{for all } \phi \in D(A').` | `\text{for all } \phi \in D(A'),` | Satzzeichen | **Umgesetzt.** Nach dem Punkt geht der Satz mit „where 1/p + 1/q = 1“ weiter. |
| 298 | 1324 | ○ | `\text{has codimension one in } D(A_{\max})` | `\text{has codimension one in } D(A_{\max}).` | Satzzeichen | **Umgesetzt.** Die übrigen Zeilen dieser Aufzählung enden mit Punkt. |
| 299 | 1366 | ● | `\phi \in D(B')_{+}) .` | `\phi \in D(B')_{+} .` | Klammern | **Umgesetzt.** Überzählige „)“. |
| 300 | 1439 | ● | `\left(-\phi^{(3)}(x)\right)) \dx` | `\left(-\phi^{(3)}(x)\right) \dx` | Klammern | **Umgesetzt.** Überzählige „)“. |
| 301 | 1511 | ● | `Section~\ref{sec:c3-1}` | `Section~\ref{sec:c2-3}` | Verweis | **Umgesetzt.** Schon in der Arbeitsliste. Die Charakterisierung positiver Halbgruppen steht in Abschnitt 2.3, nicht in 3.1. |
| 301 | 1531 | ◐ | `\Re\mleft\langle(\sign  \bar{f}) S(t)f\mright\rangle` | `\Re\mleft[(\sign \bar{f}) S(t)f\mright]` | Klammern | **Umgesetzt.** bitte prüfen: Spitze Klammern mit nur einem Argument; gemeint ist der Realteil des Elements (vgl. Z. 1719 \Re[…]). |
| 301 | 1537 | ○ | `\max\{\omega (A),\omega (B)\}` | `\max\{\omega_{0}(A),\omega_{0}(B)\}` | Notation | **Umgesetzt.** Wachstumsschranke sonst ω_0 (Z. 407, 1677, 2218). |
| 302 | 1552 | ○ | `= \langle R(\lambda,A)\vert g\vert,\psi\rangle` | `= \langle R(\lambda,A)\vert g\vert,\psi\rangle .` | Satzzeichen | **Umgesetzt.** Abgesetzte Formel ohne Satzende, danach beginnt ein neuer Satz; ebenso Z. 1600 (vor „Thus“) und Z. 1642 (vor „Assume“). |
| 303 | 1651 | ◐ | `\vert f_{n} - f_{m}\vert \leq R(\lambda,A)\vert g_{n} - g_{m}\vert` | `\vert f_{n} - f_{m}\vert \leq R(\mu,A)\vert g_{n} - g_{m}\vert` | Tippfehler | **Umgesetzt.** bitte prüfen: g_n = (μ − B)f_n, also ist R(μ,A) gemeint. |
| 304 | 1694 | ◐ | `(the center of\/ $E$ (see Section~\ref{sec:c1-9}).` | `(the center of\/ $E$, see Section~\ref{sec:c1-9}).` | Klammern | **Umgesetzt.** Schon in der Arbeitsliste. Klammern nicht ausgeglichen. |
| 304 | 1695 | ○ | `$E =$ $L^{p}(X,\mu)$` | `$E = L^{p}(X,\mu)$` | LaTeX | **Umgesetzt.** Formel unnötig geteilt (Umbruch nach „=“ möglich, Abstand nach „=“ ist Wortabstand); ebenso Z. 2218 (`$\lambda \geq$ $\omega_{0}(A)+1$`). |
| 304 | 1711 | ◐ | `B_{0} \in \mathcal{L}(E^{r})` | `B_{0} \in \mathcal{L}^{r}(E)` | Notation | **Umgesetzt.** bitte prüfen: Reguläre Operatoren sonst \mathcal{L}^{r}(E) (Z. 2207, 2280, 2294); in Z. 2207 genauer B_0 ∈ \mathcal{Z}(E)^{d}. |
| 307 | 1924 | ◐ | `\lambda R(\lambda,A)u = \lambda R(\lambda,A)u+u` | `\lambda R(\lambda,A)u = AR(\lambda,A)u+u` | Tippfehler | **Umgesetzt.** bitte prüfen: So unterscheiden sich beide Seiten um u; gemeint ist λR(λ,A)u = AR(λ,A)u + u. |
| 309 | 2071 | ○ | `\alpha \coloneq \Re(\beta)` | `\alpha = \Re(\beta)` | Notation | **Umgesetzt.** α ist vorgegeben; formuliert wird eine Annahme, keine Definition (parallel dazu „\mu = \vert\nu\vert“). |
| 309 | 2086 | ● | `\leq \langle\vert f\vert,A'\phi\rangle .` | `\leq \langle\vert f\vert,A'\phi\rangle` | Satzzeichen | **Umgesetzt.** Punkt am Formelende, obwohl der Satz mit „holds for all …“ weitergeht. |
| 310 | 2129 | ● | `1/t \, ((T(t)\vert f\vert)(0)` | `1/t \, (T(t)\vert f\vert)(0)` | Klammern | **Umgesetzt.** Eine öffnende Klammer zu viel. |
| 310 | 2134 | ○ | `\mu\{0\} = \nu\{0\} = 0` | `\mu(\{0\}) = \nu(\{0\}) = 0` | Notation | **Umgesetzt.** In Z. 2041 μ({0}); ebenso Z. 2144. |
| 311 | 2181 | ◐ | `- \langle\Re(V)\vert f\vert,\phi\rangle &= \Re\langle` | `- \langle\Re(V)\vert f\vert,\phi\rangle = \Re\langle` | LaTeX | **Umgesetzt.** Das zweite & öffnet eine neue align-Spaltengruppe; „= Re⟨…Af…⟩“ rückt mit großem Abstand nach rechts. |
| 312 | 2234 | ○ | `Mc/\lambda(\|g^{+}\| + \|g^{-}\|)` | `(Mc/\lambda)(\|g^{+}\| + \|g^{-}\|)` | Klammern | **Umgesetzt.** Ohne Klammern liest sich λ(…) als Nenner; vgl. Z. 2229 und rechts (2Mc/λ). |
| 314 | 2354 | ◐ | `Then by Eq.~\myeqpageref{eq:c2-5.1},` | `Then by Eq.~\myeqpageref{eq:c2-5.3},` | Verweis | **Umgesetzt.** bitte prüfen: Benutzt wird die Definition von T(s) als Modulus von S(s), also (2.5.3), nicht die Verbandshomomorphismus-Gleichung (2.5.1). |
| 315 | 2489 | ○ | `$\displaystyle D_{g}\Theta(f) = \lim_{t \downarrow 0} k(t)/t$` | `$D_{g}\Theta(f) = \lim_{t \downarrow 0} k(t)/t$` | LaTeX | **Umgesetzt.** \displaystyle im Fließtext vergrößert den Zeilenabstand; ggf. als abgesetzte Formel. |
| 316 | 2505 | ◐ | `Part-II, Chapter~\ref{chap:b2}, ⏎ Lemma 2.4` | `Part-II, Lemma~\ref{lem:b2-2.4}` | Verweis | **Umgesetzt.** Schon in der Arbeitsliste. Hartkodierte Nummer und abweichende Zitierweise (Z. 737: Part-II, Lemma~\ref{lem:b2-2.4}). |
| 316 | 2512 | ○ | `regular Borel measure $\mu$ on $C(K)$` | `regular Borel measure $\mu$ on $K$` | Tippfehler | **Umgesetzt.** bitte prüfen: Das Maß lebt auf K (integriert wird in Z. 2517 über K). |
| 316 | 2517 | ● | `\Re\mleft(\sign (\bar{f}(x))\mright)h(x))` | `\Re\mleft(\sign(\overline{f(x)})h(x)\mright)` | Klammern | **Umgesetzt.** Klammern unausgeglichen: \mright) steht zu früh, am Ende eine „)“ zu viel; vgl. Z. 2509. |
| 316 | 2524 | ○ | `(see Section~\ref{sec:c1-8})\,).` | `(see Section~\ref{sec:c1-8})).` | Abstand | **Umgesetzt.** Schon in der Arbeitsliste. Abstand vor der schließenden Klammer. |
| 317 | 2539 | ○ | `\Re((\sign  \overline{f})g)` | `\Re((\sign  \bar{f})g)` | Notation | **Umgesetzt.** Sonst durchgehend \bar{f}; \overline{f} ist im Druck breiter. |
| 317 | 2542 | ◐ | `D^{-}_{g}\Theta(f) = \lim_{t \to 0}` | `D^{-}_{g}\Theta(f) = \lim_{t \uparrow 0}` | Tippfehler | **Umgesetzt.** bitte prüfen: Linksseitige Ableitung; die rechtsseitige ist mit t ↓ 0 notiert (Z. 2489). |
| 317 | 2578 | ● | `\text{ for } t \in [0,s]) .` | `\text{ for } t \in [0,s] .` | Klammern | **Umgesetzt.** War im Quelltext schon korrekt. Überzählige „)“. |
| 318 | 2664 | ◐ | `(P_{+} - P_{-})(Af^{+} + Af^{-})` | `(P_{+} - P_{-})(Af^{+} - Af^{-})` | Tippfehler | **Umgesetzt.** bitte prüfen: Af = Af⁺ − Af⁻; die folgende Zeile setzt das Minuszeichen voraus. |
| 320 | 2747 | ○ | `is a multiplication operator for all $\lambda \in \rho(A)$` | `is a multiplication operator for all $\lambda \in \rho(A)$.` | Satzzeichen | **Umgesetzt.** In der Aufzählung enden (a), (b), (e) mit Punkt, (c) und (d) (Z. 2750) nicht; ebenso Prop. 2.5.15 (a), (b) (Z. 2833, 2836). |
| 321 | 2846 | ● | `\ref{sec:c1-9})⏎, it is clear` | `\ref{sec:c1-9}), it is clear` | Abstand | **Umgesetzt.** Schon in der Arbeitsliste. Der Zeilenumbruch vor dem Komma ergibt im Druck ein Leerzeichen. |
| 321 | 2849 | ◐ | `Hence $A \in \mathcal{Z}(E)$` | `Hence $A \in \mathcal{Z}(E)$.` | Satzzeichen | **Umgesetzt.** Schon in der Arbeitsliste. Am Satzende fehlt der Punkt. |
| 322 | 2898 | ● | `\phi \in E^*` | `\phi \in E'` | Notation | **Umgesetzt.** Dualraum sonst durchgehend E'; ebenso Z. 2922 (`E_{+}^*` → `E'_{+}`). |
| 322 | 2899 | ◐ | `Af \in (f)^{dd}` | `Af \in \{f\}^{dd}` | Notation | **Umgesetzt.** Sonst \{f\}^{dd} (Z. 1378, 2492, 2633). |
| 322 | 2906 | ◐ | `(this follows from Eq.~\myeqpageref{eq:a2-1.8})` | `(this follows from Part-I, Eq.~\myeqpageref{eq:a2-1.8})` | Verweis | **Umgesetzt.** Schon in der Arbeitsliste. Formel aus Teil I ohne Teilangabe; die gedruckte Nummer kommt auch in diesem Kapitel vor. |
| 322 | 2944 | ○ | `C*-algebras` | `\CA-algebras` | Notation | **Umgesetzt.** In Z. 2975 mit \CA (C mit hochgestelltem Stern), hier mit Text-Sternchen. |
| 322 | 2951 | ○ | `C^{\infty}_0(\R^n)` | `C^{\infty}_{c}(\R^n)` | Notation | **Umgesetzt.** Testfunktionen sonst C_c^∞ (z. B. Z. 1785, 2166). |

### Teil III, Kap. 3 – Spectral Theory of Positive Semigroups on Banach Lattices (`part-c/chap-c3.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 327 | 52 | ○ | `If \ $T(1)'\phi_{0} = \phi_{0}$ \ for some \ $\phi_{0} \in E'_{+}$` | `If $T(1)'\phi_{0} = \phi_{0}$ for some $\phi_{0} \in E'_{+}$` | Abstand | Erzwungene Leerzeichen „\ “ zusätzlich zum normalen Wortabstand ergeben sichtbar doppelte Lücken. |
| 328 | 115 | ○ | `T(s)\vert f\vert \ds \right\| \` | `T(s)\vert f\vert \ds \right\| .` | LaTeX | Überzähliger Backslash am Zeilenende (wirkt als Leerzeichen), Satzzeichen fehlt; ebenso Z. 684 (`= 0\ `). |
| 328 | 121 | ◐ | `\left(\int_{0}^t \exp(-\mu s)T(s) \ds \right)_{t\geq 0}` | `\left(\int_{0}^t \eu^{-\lambda s}T(s) \ds \right)_{t\geq 0}` | Tippfehler | Bitte prüfen: Zu zeigen ist die Normkonvergenz für λ (vgl. Aussage Z. 76 und Schluss Z. 138); μ wird erst in Z. 122 fixiert. |
| 329 | 134 | ◐ | `\exp(-(\Re(\lambda)-\mu)s)\eu^{-\lambda s}\vert\langle T(s)f,\phi\rangle\vert` | `\exp(-(\Re(\lambda)-\mu)s)\eu^{-\mu s}\vert\langle T(s)f,\phi\rangle\vert` | Tippfehler | Bitte prüfen: Für die Abschätzung mit Eq. (3.1.4) muss der Faktor e^{-μs} stehen; ebenso Z. 135 (`\int_{t}^r \eu^{-\lambda s}\vert\langle` → `\eu^{-\mu s}`). |
| 331 | 223 | ◐ | `\index{spectrum!boundary\vert)} … \section{The Boundary Spectrum}` | `\index{spectrum!boundary\vert)} \section{Irreducible Semigroups}` | LaTeX | Kein Formelbefund: Indexbereich wird in Z. 223 geschlossen, aber erst in Z. 227 geöffnet und danach nie geschlossen (makeindex-Warnung, falscher Seitenbereich). |
| 331 | 262 | ○ | `\vert f^{[n]}\vert = \vert f\vert \quad (n \in \Z)` | `\vert f^{[n]}\vert = \vert f\vert \quad (n \in \Z);` | Satzzeichen | In der Aufzählung Eq. (3.2.3)–(3.2.5) endet (3.2.4) mit „;“, (3.2.5) mit „.“; bei (3.2.3) fehlt das Semikolon. |
| 332 | 305 | ◐ | `\overline{T}(t)\overline{h}^{[n]} = \eu^{\im\beta  t}\overline{h}^{[n]}` | `\overline{T}(t)\overline{h}^{[n]} = \eu^{\im n\beta t}\overline{h}^{[n]}` | Tippfehler | Bitte prüfen: Es fehlt der Faktor n im Exponenten (vgl. Z. 306 und Eq. (3.2.7)). |
| 332 | 306 | ◐ | `T(t)h^{[n]} = \eu^{\im n\beta}h^{[n]}` | `T(t)h^{[n]} = \eu^{\im n\beta t}h^{[n]}` | Tippfehler | Bitte prüfen: Im Exponenten fehlt t. |
| 333 | 373 | ○ | `0 \in P\sigma(R_{\F}(\lambda,A))` | `0 \in P\sigma(R_{\F}(\lambda))` | Notation | Die Pseudoresolvente R_F hat ein Argument (Z. 372: „R(λ,A)_F“ bzw. „R_F“); bitte prüfen. |
| 333 | 397 | ○ | `R(\lambda_{0})^{n+1}$ } .` | `R(\lambda_{0})^{n+1}$} .` | Abstand | Das Leerzeichen vor „}“ steht innerhalb von \text und ist im Druck als Lücke vor dem Punkt sichtbar. |
| 334 | 420 | ○ | `S = (\mu-\lambda_{0})^{-1}(1 - (1-(\lambda_{0}-\mu)R(\lambda_{0}))^{-1})` | `S = (\mu-\lambda_{0})^{-1}(\Id - (\Id-(\lambda_{0}-\mu)R(\lambda_{0}))^{-1})` | Notation | Unmittelbar davor (Z. 413 f.) steht \Id für dieselbe Identität; ebenso Z. 1635 (vgl. Z. 1627/1630 mit \Id) und Z. 1680; außerdem 1 statt \Id in Z. 357, 658, 661. |
| 334 | 435 | ◐ | `\overline{D}\backslash D` | `\overline{D}\setminus D` | Notation | \backslash ist sichtbar größer als \setminus (\smallsetminus), das sonst im Kapitel verwendet wird (Z. 1085, 1166, 1336); ebenso Z. 1775, 1902. |
| 335 | 508 | ◐ | `S_{h}^{n}\vert h\vert = S_{h}^{-n}z\tilde{R}(z) \vert h\vert` | `S_{h}^{n}\vert h\vert = S_{h}^{n}z\tilde{R}(z) \vert h\vert` | Tippfehler | Bitte prüfen: Nach Eq. (3.2.14) muss links S_h^{n} stehen, sonst passt der Folgeschritt nicht. |
| 336 | 547 | ○ | `Eq.~\myeqpageref{eq:c3-2.15}~(a)` | `condition (a) of Eq.~\myeqpageref{eq:c3-2.15}` | Verweis | \myeqpageref hängt ggf. „on the … page“ an, dann steht „(a)“ hinter der Seitenangabe; ebenso Z. 554 und 564. |
| 336 | 602 | ◐ | `r\lambda \eu^{-r}` | `r\lambda \eu^{-\lambda r}` | Tippfehler | Bitte prüfen: Aus Z. 598 folgt der Faktor e^{-λr}, nur dann ergibt sich (1 - e^{-λr}) in Z. 603. |
| 336 | 606 | ◐ | `hence $\|\lambda R(\lambda,A)\| \leq M$` | `hence $\|\lambda R(\lambda,A)\| \leq M$.` | Satzzeichen | Der Satz am Beweisende hat keinen Punkt. |
| 337 | 625 | ◐ | `in Corollary~\ref{cor:c3-2.12}` | `in Corollary~\ref{cor:c3-2.12}.` | Satzzeichen | Nach dem Verweis fehlt der Schlusspunkt. |
| 338 | 655 | ◐ | `for $r > 0$, $\epsilon > 0$` | `for $\tau > 0$, $\epsilon > 0$` | Tippfehler | Die folgende Formel und Z. 661 verwenden τ, nicht r. |
| 338 | 688 | ● | `r > 0) .` | `r > 0 .` | Klammern | Schließende Klammer ohne öffnende Klammer. |
| 338 | 690 | ● | `\{(R_{1}(\lambda)\}_{\Re(\lambda)>0}` | `\{R_{1}(\lambda)\}_{\Re(\lambda)>0}` | Klammern | Öffnende Klammer ohne schließende Klammer. |
| 338 | 691 | ● | `(by Eq.~\myeqpageref{eq:c3-2.19}.` | `(by Eq.~\myeqpageref{eq:c3-2.19}).` | Klammern | Schon in der Arbeitsliste. Ebenso Z. 692: `(by Eq.~\myeqpageref{eq:c3-2.16} and` → `(by Eq.~\myeqpageref{eq:c3-2.16}) and`. |
| 338 | 694 | ◐ | `Proposition~\ref{prop:c3-2.7}(b)` | `Proposition~\ref{prop:c3-2.7}` | Verweis | Schon in der Arbeitsliste. Proposition 3.2.7 hat keinen Teil (b). |
| 339 | 716 | ○ | `\subsetneq ... \subsetneq` | `\subsetneq \dots \subsetneq` | LaTeX | „...“ im Mathemodus ergibt schlecht gesetzte Punkte; sonst \ldots. |
| 339 | 722 | ◐ | `$s(A_{0}) < s(A)$ ,` | `$s(A_{0}) < s(A)$,` | Abstand | Sichtbares Leerzeichen vor dem Komma; ebenso Z. 2056 (`(R(\mu,A)g)^+$ ,`) und Z. 2071 (`R(\mu,A)h \geq 0$ ,`). |
| 339 | 753 | ○ | `(\cf Eq.~\myeqpageref{eq:b3-2.19})` | `(\cf Part-II, Eq.~\myeqpageref{eq:b3-2.19})` | Verweis | Schon in der Arbeitsliste. Gleiche Nummer (3.2.19) existiert auch in diesem Kapitel. |
| 340 | 782 | ● | `L_{p,o}` | `L_{p,0}` | Tippfehler | Buchstabe o statt Ziffer 0 (vgl. Eq. (3.2.23)). |
| 340 | 802 | ○ | `$s(A)$ is strictly dominant provided that $\sigma(A) \neq \emptyset$` | `$s(L_{p})$ is strictly dominant provided that $\sigma(L_{p}) \neq \emptyset$` | Notation | Im Beispiel heißt der Generator L_p, A ist nicht eingeführt; ebenso Z. 803; bitte prüfen. |
| 340 | 814 | ○ | `R(\lambda,A) : s(A) < \lambda` | `R(\lambda,A) \colon s(A) < \lambda` | Notation | Sonst steht in Mengenklammern durchgehend \colon (andere Abstände); ebenso Z. 1163 (`\{\xi\in\C :\vert\xi\vert=1\}`). |
| 342 | 967 | ◐ | `$(b)\Rightarrow (a)$.` | `(b) $\Rightarrow$ (a).` | Notation | Im Mathemodus werden a, b kursiv gesetzt, anders als in Z. 575/593 und den Aufzählungslabels; ebenso Z. 974, 2079, 2089, 2284, 2291. |
| 344 | 1033 | ○ | `\begin{align*}\label{eq:c3-D0}` | `\begin{align*}` | LaTeX | \label in einer unnummerierten Umgebung, nirgends referenziert; ebenso Z. 1056 (`\begin{equation*}\label{eq:c3-r_lambda}`). |
| 345 | 1115 | ◐ | `Theorem~\ref{thm:b2-3.5}` | `Part-II, Proposition~\ref{prop:b3-3.5}` | Verweis | Schon in der Arbeitsliste. Gemeint ist laut „latter proposition“ und Beweis Z. 1140 Part-II, Proposition 3.3.5. |
| 345 | 1142 | ○ | `by assertion (i) there exists` | `by assertion (ii) there exists` | Verweis | Schon in der Arbeitsliste. Strikte Positivität des Funktionals folgt aus (ii). |
| 346 | 1166 | ◐ | `\Gamma\times\Gamma\setminus(1,1)` | `\Gamma\times\Gamma\setminus\{(1,1)\}` | Notation | Mengendifferenz mit einem Punkt braucht Mengenklammern. |
| 346 | 1215 | ○ | `Eq.~\myeqpageref{eq:a1-3.1}` | `Part-I, Eq.~\myeqpageref{eq:a1-3.1}` | Verweis | Gleichung aus Part I ohne Teilangabe, die Nummer (1.3.1) gibt es auch in Part III; ebenso Z. 1642 (eq:a2-1.9), 1717 (eq:a1-3.1), 2081 (eq:a1-3.2); vgl. Arbeitsliste zu Z. 753. |
| 348 | 1309 | ◐ | `C(K) \cong E_{h}` | `C(K) \cong E_{\vert h\vert}` | Tippfehler | h ist nicht positiv; in Z. 1306 wird E_{\vert h\vert} mit C(K) identifiziert. |
| 348 | 1309 | ○ | `We define $j \colon C(\Gamma) \to E$` | `We define $i \colon C(\Gamma) \to E$` | Notation | Schon in der Arbeitsliste. In der Aussage (Z. 1283) heißen die Abbildungen i und j, im Beweis j und \tilde{j}; ebenso Z. 1310, 1313, 1315, 1317, 1318. |
| 348 | 1313 | ○ | `\int_{0}^{2\pi} e_{n}(\eu^{\im t})\dt  =2\pi\cdot\delta_{n0}` | `\frac{1}{2\pi}\int_{0}^{2\pi} e_{n}(\eu^{\im t})\dt = \delta_{n0}` | Tippfehler | Bitte prüfen: Wegen ⟨\vert h\vert,φ⟩ = 1 (Z. 1305) müsste ⟨h^{[0]},φ⟩ = 1 sein, nicht 2π; ebenso Z. 1315. |
| 348 | 1342 | ◐ | `\alpha \notin P\sigma(A)` | `\alpha \notin P\sigma(R)` | Tippfehler | Im Lemma kommt nur der Operator R vor (vgl. Z. 1336). |
| 349 | 1356 | ○ | `\mathcal{F}\text{-}\lim\sup` | `\mathcal{F}\text{-}\limsup` | Notation | \lim\sup setzt zwei getrennte Operatoren; üblich ist \limsup. |
| 350 | 1436 | ◐ | `\vert\hat{f}\vert = \gamma R(\gamma+\im\beta,A)_{\mathcal{U}}\vert\hat{f}\vert` | `\vert\hat{f}\vert = \vert\gamma R(\gamma+\im\beta,A)_{\mathcal{U}}\hat{f}\vert` | Klammern | Bitte prüfen: Die Betragsstriche müssen um den ganzen Ausdruck stehen (Eigenvektor \hat{f} ∈ M), erst dann folgt die Abschätzung. |
| 350 | 1443 | ○ | `\hat{\phi}(\vert\hat{f}\vert) = P_{\mathcal{U}}\vert\hat{f}\vert` | `\hat{\phi}(\vert\hat{f}\vert)\hat{u} = P_{\mathcal{U}}\vert\hat{f}\vert` | Tippfehler | Bitte prüfen: Links steht ein Skalar, rechts ein Vektor (P_U = \hat{φ}⊗\hat{u}). |
| 350 | 1449 | ◐ | `\tilde{\phi}(\vert\hat{f}\vert) - \vert\hat{f}\vert \in I` | `\hat{\phi}(\vert\hat{f}\vert)\hat{u} - \vert\hat{f}\vert \in I` | Tippfehler | \tilde{φ} ist nicht definiert (gemeint \hat{φ}); zudem fehlt \hat{u} (vgl. Z. 1443 und 1455); bitte prüfen. |
| 350 | 1453 | ◐ | `E_{\mathcal{U}/{I}}` | `E_{\mathcal{U}}/I` | Notation | Der Quotient wird im Index gesetzt; vgl. E_1/I in Z. 690. |
| 350 | 1467 | ● | `J_{1},J_{2}, .. J_{m}` | `J_{1},J_{2},\ldots,J_{m}` | Tippfehler | Zwei statt drei Punkte; ebenso Z. 1473 (`J_{2}\oplus .. \oplus J_{m} .$` → `J_{2}\oplus \cdots \oplus J_{m}$.`). |
| 351 | 1504 | ◐ | `To show that $T_{k}$ is irreducible` | `To show that $\TT_{k}$ is irreducible` | Notation | Die eingeschränkte Halbgruppe heißt \TT_k (Z. 1468, 1472). |
| 351 | 1533 | ◐ | `Moreover, $\sigma_{b}$ contains` | `Moreover, $\sigma_{b}(A)$ contains` | Notation | Argument fehlt. |
| 352 | 1545 | ○ | `\gamma_{1} \coloneq  \pi/v_{1}$, $\gamma_{2} \coloneq  \pi/v_{2}` | `\gamma_{1} \coloneq \pi v_{1}$, $\gamma_{2} \coloneq \pi v_{2}` | Tippfehler | Bitte prüfen: Wegen v_1 < v_2 ist so γ_1 > γ_2 und die Bedingung nγ_1 ≤ \vert γ\vert ≤ nγ_2 in Z. 1543 für n ≥ 1 leer. |
| 352 | 1552 | ○ | `\textit{\small $ (T(t)f)(x,v) = \begin{cases} … $}` | `(T(t)f)(x,v) = \begin{cases} … \end{cases}` | LaTeX | Die Formel wird als kleine Inline-Formel in kursivem Text gesetzt, „if“ ist kursiv (anders als Eq. (3.3.3)); außerdem `k \textit{ even}` neben `k \text{ odd}`; ebenso Z. 1649. |
| 352 | 1570 | ● | `R(.,A)` | `R(\cdot,A)` | Notation | Sonst \cdot, z. B. Z. 1576 und 1577. |
| 354 | 1664 | ● | `\dim(\ker((\eu^{\tau\cdot s(B)} - S(\tau))) > 1` | `\dim(\ker(\eu^{\tau\cdot s(B)} - S(\tau))) > 1` | Klammern | Eine öffnende Klammer zu viel. |
| 354 | 1675 | ● | `\dx'dv'` | `\dx'\diff{v'}` | Notation | Das zweite Differential hat ein kursives d. |
| 354 | 1678 | ◐ | `(\cf Eq.~\eqref{eq:c3-3.5} and Eq.~\myeqpageref{eq:c3-3.7})` | `(\cf Eq.~\eqref{eq:c3-3.5} and Eq.~\myeqpageref{eq:c3-3.6})` | Verweis | Bitte prüfen: κ wird in Eq. (3.3.6) eingeführt, Eq. (3.3.7) ist das Irreduzibilitätskriterium. |
| 354 | 1679 | ● | `$K$ is A-compact` | `$K$ is $A$-compact` | Mathemodus | A steht ohne Mathemodus (vgl. Z. 1608, 1680). |
| 355 | 1717 | ◐ | `(\eu^{rt} - T(r))R(r,A) \geq 0` | `(\eu^{rt} - T(t))R(r,A) \geq 0` | Tippfehler | Bitte prüfen: Die folgende Abschätzung betrifft T(t). |
| 355 | 1749 | ◐ | `A^*(q_{\psi}'(x)) = q_{\psi}'(x)` | `A^*(q_{\psi}'(x)) = \lambda q_{\psi}'(x)` | Tippfehler | Bitte prüfen: Der Eigenwert λ fehlt (vgl. vorangehende Gleichungen). |
| 357 | 1834 | ● | `P\sigma(A)\cap i\R` | `P\sigma(A)\cap \im\R` | Notation | Kursives i statt \im; ebenso Z. 1869 (`iF\cap E_{\R }`), 1902 (zweimal `i\R`), 2107 (`\mu+i\R`). |
| 357 | 1836 | ● | `\item E is weakly sequentially complete` | `\item $E$ is weakly sequentially complete` | Mathemodus | E ohne Mathemodus. |
| 357 | 1848 | ● | `\im\alpha\Z \in P\sigma(A_{\vert F})` | `\im\alpha\Z \subseteq P\sigma(A_{\vert F})` | Tippfehler | Inklusion von Mengen. |
| 357 | 1853 | ○ | `$T(t)'\phi = \phi$ and $\phi \gg 0 ,  (t \geq 0)$` | `$T(t)'\phi = \phi$ $(t \geq 0)$ and $\phi \gg 0$` | Satzzeichen | Komma und Bedingung (t ≥ 0) stehen falsch innerhalb der Formel. |
| 358 | 1870 | ● | `F\cap\mathbb{E}_{\R }` | `F\cap E_{\R }` | Tippfehler | \mathbb{E} statt E (vgl. Z. 1869). |
| 358 | 1897 | ○ | `\int_{0}^{2\pi} f(z \cdot \eu^{\im s}) \ds` | `\int_{0}^{2\pi} f(\eu^{\im s}) \ds` | Tippfehler | Bitte prüfen: In der Definition von g_t(x) ist z frei. |
| 358 | 1928 | ● | `r \in R(\sigma(T(t)))` | `r \in R\sigma(T(t))` | Notation | Residualspektrum, sonst als R\sigma geschrieben (Z. 1930). |
| 360 | 2008 | ◐ | `\text{ for every } \ f \in D(A) ,` | `\text{ for every } \ f \in D(A) .` | Satzzeichen | Nach der Formel beginnt ein neuer Satz („For real μ …“). |
| 362 | 2204 | ◐ | `r(T(-t)_{\vert J_{\mu}}) < \eu^{\mu t}` | `r(T(-t)_{\vert J_{\mu}}) < \eu^{-\mu t}` | Tippfehler | Bitte prüfen: Nur so folgt Z. 2213 (\vert λ\vert > e^{μt} nach Inversion). |
| 363 | 2260 | ◐ | `\begin{enumerate} [(a)]` | `\begin{enumerate}[\upshape (a)]` | LaTeX | In der Proposition werden die Labels sonst kursiv gesetzt; alle anderen Aufzählungen verwenden \upshape. |
| 363 | 2286 | ◐ | `(\sup\{\|T(t)\| \colon 0 \leq t \leq t_0\})^{1/p}` | `(\sup\{\|T(t)\| \colon 0 \leq t \leq t_0\})^{p}` | Tippfehler | Bitte prüfen: Z. 2289 braucht \|T(t)\|^p ≤ M und Z. 2303/2304 \|T(t)\| ≤ M^{1/p}. |
| 364 | 2356 | ● | `on $L(\R ^n)$ $(1 \leq p < \infty)$` | `on $L^p(\R ^n)$ $(1 \leq p < \infty)$` | Tippfehler | Exponent p fehlt. |
| 365 | 2369 | ● | `n$\times$n-matrix` | `$n\times n$-matrix` | Mathemodus | n steht aufrecht außerhalb des Mathemodus. |
| 365 | 2411 | ○ | `Part-III, Section~\ref{sec:c4-3}` | `Section~\ref{sec:c4-3}` | Verweis | Innerhalb von Part III sonst ohne Teilangabe zitiert (vgl. Arbeitsliste Kap. 4, S. 372). |

### Teil III, Kap. 4 – Asymptotics of Positive Semigroups on Banach Lattices (`part-c/chap-c4.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 369 | 27 | ● | `Part-III, Chapter~\ref{chap:b3}` | `Chapter~\ref{chap:c3}` | Verweis | Label zeigt auf Part-II, Kap. 3 (Hyperlink falsch, gedruckte Nummer zufällig gleich); gemeint ist Part-III, Kap. 3. |
| 369 | 55 | ◐ | `Remark~\ref{rem:b4-1.5}.)` | `Remark~\ref{rem:b4-1.5})` | Satzzeichen | Schon in der Arbeitsliste. Überflüssiger Punkt vor der Klammer. |
| 369 | 100 | ○ | `L^{\,p}(\mu)` | `L^{p}(\mu)` | Abstand | Zusätzlicher Abstand im Exponenten; sonst überall `L^{p}`. |
| 371 | 154 | ◐ | `k \cdot \log [r(R(k,A_{1/u}))]^{-1}` | `k \cdot \log [r(R(k,A_{1/u}))]` | Tippfehler | Wegen r(R(k,A_u)) = (k−s(u))^{-1} (Z. 141) ist [k−s(1/u)]^{-1} = r(R(k,A_{1/u})); Exponent −1 überzählig – bitte prüfen. |
| 371 | 176 | ◐ | `Part-III, Theorems~\ref{thm:c3-1.2}` | `Theorem~\ref{thm:c3-1.2}` | Verweis | Schon in der Arbeitsliste. Plural bei nur einem Satz. |
| 373 | 243 | ◐ | `0 \notin \text{P}\sigma(A)` | `0 \notin P\sigma(A)` | Notation | \text{P} setzt P im (im Theorem kursiven) Textfont; sonst überall mathematisches P\sigma bzw. P{\sigma}. |
| 373 | 252 | ○ | `\ref{thm:c4-1.5-1} In case` | `\ref{thm:c4-1.5-1}: In case` | Satzzeichen | Doppelpunkt nach der Implikation „(b) ⇒ (a)“ fehlt (vgl. Z. 274). |
| 373 | 277 | ○ | `R{\sigma}(A^*) = P{\sigma}(A^{**})` | `R{\sigma}(A') = P{\sigma}(A'')` | Notation | Adjungierte sonst mit Strich (A', T(t)', Z. 234, 689, 969, 1251); ebenso Z. 278 `(T(t)^*)`, Z. 279 `A^*`. |
| 374 | 309 | ◐ | `E_{+} \subseteq \Image{A(D(A)_{-})}` | `E_{+} \subseteq A(D(A)_{-})` | Notation | \Image setzt „im(…)“ um eine Menge, die bereits das Bild ist – bitte prüfen; ebenso Z. 316. |
| 374 | 341 | ◐ | `(\image{A})_{+}` | `(\Image{A})_{+}` | Notation | \image ergibt „im A“, \Image „im(A)“ – im selben Absatz gemischt; ebenso Z. 344, 355, 357 (\image) gegenüber Z. 343, 348, 446 (\Image). |
| 374 | 356 | ○ | `T(t)f \, \dt` | `T(t)f \dt` | Abstand | \dt/\diff bringen den Abstand schon mit, mit \, doppelt (Kapitel sonst meist ohne); ebenso u. a. Z. 343, 394, 452, 684, 897, 921, 925, 1214, 1229, 1241, 1248, 1260, 1794, 1801, 1884. |
| 374 | 357 | ◐ | `$\sigma(E',E)$-$\lim` | `$\sigma(E,E')$-$\lim` | Tippfehler | Schwache Topologie auf E ist σ(E,E') (vgl. Z. 382) – bitte prüfen. |
| 375 | 379 | ○ | `\lim_{\lambda \downarrow 0}` | `\lim_{\lambda \to 0+}` | Notation | Sonst im Kapitel λ → 0+ (Z. 362, 368, 389). |
| 376 | 435 | ◐ | `g_{0} \in \Image{A_{+}}` | `g_{0} \in (\Image{A})_{+}` | Notation | „im(A_+)“ ergibt keinen Sinn; gemeint ist der positive Teil des Bildes (vgl. Z. 341, 452). |
| 376 | 435 | ◐ | `\lim_{t \to \infty} u(t) = -h` | `\lim_{t \to \infty} u(t) = h` | Tippfehler | Im Beweis (Z. 446) konvergiert u(t) gegen h mit Ah = −f_0 (vgl. Prop. 1.12: −A^{-1}f_0) – Vorzeichen bitte prüfen. |
| 379 | 545 | ○ | `Example~\ref{ex:a3-1.3} \&~\ref{ex:a3-1.4}` | `Examples~\ref{ex:a3-1.3} and~\ref{ex:a3-1.4}` | Verweis | Schon in der Arbeitsliste. |
| 379 | 560 | ◐ | `Section~\ref{sec:b4-2}` | `Part-II, Section~\ref{sec:b4-2}` | Verweis | Schon in der Arbeitsliste. Ohne Part-Angabe liest sich „Section 4.2“ als der aktuelle Abschnitt. |
| 379 | 577 | ◐ | `Eq.~\myeqpageref{eq:b4-2.5}` | `Part-II, Eq.~\myeqpageref{eq:b4-2.5}` | Verweis | Gleichung aus Part-II trägt dieselbe Nummer (4.2.5) wie Eq. (4.2.5) dieses Kapitels (Z. 752); Part-Angabe fehlt. |
| 380 | 597 | ○ | `\omega_{ess}(\TT)` | `\omega_{\mathrm{ess}}(\TT)` | Mathemodus | „ess“ kursiv wie ein Produkt gesetzt; ebenso Z. 645, 669, 1178 (`r_{ess}`). Buchweit so – nur global ändern. |
| 381 | 661 | ○ | `Af &:= -f' - \mu f` | `Af &\coloneq -f' - \mu f` | Notation | Sonst durchgehend \coloneq (zentrierter Doppelpunkt); ebenso Z. 662, 1339, 1881. |
| 383 | 830 | ● | `assertion~\ref{thm:c4-2.6-1} , then` | `assertion~\ref{thm:c4-2.6-1}, then` | Satzzeichen | Leerzeichen vor Komma nach \ref; ebenso Z. 911 (`\ref{ex:c4-2.7-1} ,`). |
| 384 | 867 | ● | `$t > 0$ ,` | `$t > 0$,` | Satzzeichen | Leerzeichen vor Komma; ebenso Z. 871 (`$t > 0$\, ,`), 1017 (`$L^p(\mu)$ ,`), 1494 (`$h \colon \R \to \R_{+}$ ,`). |
| 384 | 875 | ◐ | `\int_{K} P_{s}(y,C)P_{t}(x,dy)` | `\int_{X} P_{s}(y,C)P_{t}(x,\diff{y})` | Tippfehler | Grundmenge heißt X (Z. 861), K ist nicht definiert; ebenso `x \in K` → `x \in X` in derselben Zeile; dazu kursives d – bitte prüfen. |
| 384 | 883 | ◐ | `\, d\mu(x)` | `\, \diff{\mu(x)}` | Notation | Kursives d; sonst \diff (Z. 897, 921, 925); ebenso Z. 906 (zweimal). |
| 384 | 892 | ◐ | `= 1_{C}(x)` | `= \1_{C}(x)` | Notation | Indikatorfunktion sonst fett \1 (Z. 787, 917, 925). |
| 384 | 892 | ◐ | `\mu\text{-a.e.}.$` | `\mu\text{-a.e.}$` | Satzzeichen | Doppelter Punkt „a.e..“. |
| 385 | 917 | ◐ | `\quad\mu-\text{a.e.}.` | `\quad\mu\text{-a.e.}` | Mathemodus | Bindestrich im Mathemodus wird zum Minuszeichen; dazu doppelter Punkt. |
| 385 | 970 | ● | `Since Pe = e, hence` | `Since $Pe = e$, hence` | Mathemodus | Formel ohne $…$. |
| 386 | 1003 | ○ | `T^n \wedge T^m > 0` | `\inf\{T^n,T^m\} > 0` | Notation | Infimum von Operatoren sonst als \inf\{\cdot,\cdot\} (Z. 957, 961). |
| 386 | 1021 | ● | `\cap \im\R = {0}` | `\cap \im\R = \{0\}` | Klammern | Unmaskierte Mengenklammern: gedruckt wird „= 0“. |
| 388 | 1088 | ○ | `$T = T_{1} \oplus T_{2}$` | `$\TT = \TT_{1} \oplus \TT_{2}$` | Notation | T ohne Argument nicht definiert; vorher (Z. 1067) \TT_1, \TT_2. |
| 389 | 1151 | ◐ | `Mh \coloneq h\cdot f` | `Mf \coloneq h\cdot f` | Tippfehler | M wirkt auf f ∈ L^p(ν), h ist die feste Dichte – bitte prüfen. |
| 389 | 1159 | ◐ | `P = h \otimes l` | `P = h \otimes \1` | Tippfehler | Nach der Normierung T(t)𝟙 = 𝟙 ist 𝟙 der Fixvektor; „l“ vermutlich verlesene 1 – bitte prüfen. |
| 389 | 1172 | ◐ | `\|R(1,A)^{n} - P\|^{2/p}\|\cdots\|^{1-2/p}` | `\|R(1,A)^{n} - P\|^{p/2}\|\cdots\|^{1-p/2}` | Tippfehler | Für p < 2 wäre 1−2/p negativ; Riesz-Konvexität (vgl. Z. 1155: Exponent p/q) liefert p/2 und 1−p/2 – bitte prüfen; ebenso Z. 1173. |
| 389 | 1176 | ◐ | `R(1,A)(1-P)` | `R(1,A)(\Id-P)` | Notation | Identität unmittelbar vorher (Z. 1165) als \Id. |
| 390 | 1202 | ○ | `f(\frac{1}{2}) = 0` | `f(\frac{1}{4}) = 0` | Tippfehler | Intervall ist [1/4,1]; Halbgruppe (Z. 1223–1226) und Resolvente (Z. 1229) passen zur Randbedingung bei 1/4 – bitte prüfen. |
| 390 | 1240 | ◐ | `\text{\sfrac{1}{x}}` | `\mfrac{1}{x}` | Notation | \sfrac ist das Textmakro, x erscheint aufrecht statt kursiv; ebenso Z. 1241. |
| 392 | 1298 | ◐ | `\Phi(u_t),  t \geq 0` | `\Phi(u_t), \quad t \geq 0` | Abstand | Leerzeichen im Mathemodus wirkungslos, „t ≥ 0“ klebt am Komma; ebenso Z. 1315, 1794 (`t \geq 0, f_{0}`). |
| 393 | 1349 | ◐ | `Example~\ref{subsec:a1-2.4}.\,(ii)` | `Example~\ref{subsec:a1-2.4}\,(ii)` | Satzzeichen | Schon in der Arbeitsliste. Überflüssiger Punkt. |
| 393 | 1381 | ○ | `Formula Eq.~\myeqpageref{eq:c4-3.2}` | `Eq.~\myeqpageref{eq:c4-3.2}` | Verweis | Doppelte Bezeichnung „Formula Eq. (…)“; ebenso Z. 1456 („formula Eq.“), 1473 („equation Eq.“), 1533, 1672. |
| 393 | 1384 | ○ | `\|\sum_{n=0}^{\infty} S_{\lambda}^n\|` | `\Bigl\|\sum_{n=0}^{\infty} S_{\lambda}^n\Bigr\|` | Klammern | Normstriche in der abgesetzten Formel nicht an die Summe angepasst. |
| 394 | 1433 | ○ | `supp $g \subseteq [-1,-t]$` | `$\supp g \subseteq [-1,-t]$` | Mathemodus | „supp“ im Fließtext; Makro \supp vorhanden. |
| 394 | 1463 | ● | `\|w_{t}(s)\_{F}\|` | `\|w_{t}(s)\|_{F}` | LaTeX | `\_` druckt einen Unterstrich; Normindex falsch platziert. |
| 394 | 1474 | ○ | `(use \myeqpageref{eq:c4-re})` | `(use Eq.~\myeqpageref{eq:c4-3.1})` | Verweis | Schon in der Arbeitsliste. Positivität folgt aus (4.3.1) – bitte prüfen. |
| 394 | 1475 | ● | `Proposition~\ref{prop:c2-4.1} )` | `Proposition~\ref{prop:c2-4.1})` | Satzzeichen | Schon in der Arbeitsliste (●-Punkt S. 370, „ebenso“-Fälle), im Quelltext aber noch nicht korrigiert; ebenso Z. 1502 (`\ref{cor:c3-2.12} )`). |
| 395 | 1484 | ○ | `\Phi(\epsilon_{\lambda} \cdot x)` | `\Phi(\epsilon_{\lambda} \otimes x)` | Notation | Z. 1360–1363 definiert ε_λ ⊗ x; so auch Z. 1522 und 1539. |
| 396 | 1549 | ○ | `If \, $\lambda \in \sigma(A)$` | `If\/ $\lambda \in \sigma(A)$` | Abstand | Wortabstand plus \, sichtbar zu breit; sonst `If\/`; ebenso Z. 1552. |
| 396 | 1574 | ○ | `$\Phi(D(A_{0}))$ $= F$` | `$\Phi(D(A_{0})) = F$` | LaTeX | Formel in zwei Mathe-Stücke zerrissen, Abstand vor „=“ falsch; ebenso Z. 1693. |
| 396 | 1574 | ○ | `x - \Phi_{\lambda}(x) = 0` | `x - \Phi_{\lambda}(x) = \Phi R(\lambda,A_{0})g` | Tippfehler | Rechte Seite hängt nicht von g ab („for every g ∈ E“); gemeint vermutlich die Gleichung aus Z. 1540 – bitte prüfen. |
| 396 | 1576 | ○ | `the proof of~\ref{lem:c4-3.5}` | `the proof of Lemma~\ref{lem:c4-3.5}` | Verweis | Schon in der Arbeitsliste. |
| 396 | 1576 | ◐ | `equivalent to $\lambda \in \sigma(A)$` | `equivalent to $\lambda \in \rho(A)$` | Tippfehler | Eindeutige Lösbarkeit ⇔ 1 ∈ ρ(Φ_λ) ⇔ λ ∈ ρ(A) (Lemma 3.5) – bitte prüfen. |
| 396 | 1578 | ◐ | `\sigma(\Phi_{\lambda})\backslash\{0\}` | `\sigma(\Phi_{\lambda})\setminus\{0\}` | Notation | Sonst \setminus (Z. 1078, 1088); \backslash ist ein anderes Zeichen ohne Operatorabstand. |
| 396 | 1586 | ○ | `A \coloneq \frac{\diff{}}{\dt}` | `A \coloneq \frac{\diff{}}{\dx}` | Notation | Derselbe Operator heißt in Z. 1336 d/dx – bitte vereinheitlichen. |
| 396 | 1611 | ● | `s(\Phi_{r)} \geq 1` | `s(\Phi_{r}) \geq 1` | Klammern | Schließende Klammer im Index. |
| 397 | 1633 | ◐ | `$h: \mu \mapsto s(\Phi_{\mu})$` | `$h \colon \mu \mapsto s(\Phi_{\mu})$` | Notation | Sonst \colon (Z. 1494, 1744, 1815, 1901); „:“ als Relation mit falschem Abstand. |
| 398 | 1681 | ● | `$E = (L^{1}[-1,0],F)$` | `$E = L^{1}([-1,0],F)$` | Tippfehler | „L^1“ fehlt vor der Klammer (vgl. Z. 1303, 1722). |
| 398 | 1712 | ◐ | `\psi(e_{\lambda})` | `\psi(\epsilon_{\lambda})` | Notation | Die Funktion heißt sonst ε_λ (Z. 1360, 1696). |
| 398 | 1732 | ○ | `Corollary~\ref{cor:c4-3.2}, \ Eq.` | `Corollary~\ref{cor:c4-3.2}, Eq.` | Abstand | Doppelter Wortabstand nach dem Komma. |
| 398 | 1775 | ◐ | `of\/ $K(s)$) ,` | `of\/ $K(s)$),` | Satzzeichen | Schon in der Arbeitsliste. |
| 398 | 1776 | ○ | `Hence \ $\langle x_{\lambda},x_{\mu}'\rangle \neq 0$ \ and` | `Hence $\langle x_{\lambda},x_{\mu}'\rangle \neq 0$ and` | Abstand | Doppelte Wortabstände um die Formel. |
| 399 | 1801 | ◐ | `\dx' \ ,` | `\dx',` | Satzzeichen | Sichtbarer Abstand vor dem Komma in der abgesetzten Formel. |
| 399 | 1824 | ◐ | `\Phi_{\mu}(x) =` | `\Phi_{\mu}f(x) =` | Tippfehler | f fehlt (vgl. rechte Seite Φ_λ f(x), Z. 1827). |
| 401 | 1899 | ○ | `{bellmancooke:1963}\,)` | `{bellmancooke:1963})` | Abstand | Schon in der Arbeitsliste (●, S. 401); nach der Korrektur bleibt mit \, ein kleiner Abstand vor „)“. |
| 401 | 1909 | ◐ | `(i=1,...,n)` | `(i=1,\ldots,n)` | LaTeX | „...“ im Mathemodus statt \ldots (Abstände falsch); ebenso Z. 1913, 1917; Z. 2070 korrekt. |
| 402 | 2067 | ◐ | `\frac{\partial u_i}{\partial t}(t,a)` | `\frac{\partial u}{\partial t}(t,a,x)` | Tippfehler | System scheint aus Bsp. 3.12 (Z. 1909–1917) kopiert: n und β_ij sind in Bsp. 3.13 nicht definiert, die Interpretation (Z. 2097) spricht von u(t,a,x), β und Ω. Ganze align-Umgebung Z. 2067–2079 bitte am Original prüfen. |

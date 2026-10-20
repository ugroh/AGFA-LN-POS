# Formelprüfung Part A (Teil I): Satz und Notation

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184). Geprüft am 14.10.2026; Stand der Umsetzung: 20.10.2026.

**Umfang:** Teil I, Kap. 1–4, geprüft im LaTeX-Quelltext (Branch `fahnenkorrektur`). Geprüft wurden nur Satz und Notation in Formeln: Tippfehler, Klammern, Indizes, uneinheitliche Schreibweisen, Mathemodus, Satzzeichen an Formeln, Gleichungsverweise. Beweise wurden **nicht** nachgerechnet; wo ein Befund inhaltlich wirkt, steht „bitte prüfen“.

**Stand 20.10.2026:** **Kap. 1, 2 und 3 sind erledigt** (Kap. 1 nach Durchsicht durch Rainer Nagel, Kap. 3 nach Freigabe durch Günther Greiner; in der Spalte Kommentar mit **Umgesetzt** markiert, Abweichungen ebenda). Kap. 4 ist noch offen. Die Zeilenangaben beziehen sich auf den Stand vom 14.10.2026.

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

**Spalten:** S. = gedruckte Buchseite, ermittelt über das nächstgelegene Label (kann um eine Seite abweichen). Z. = Zeile in der .tex-Datei. Sicherheit: ● eindeutig · ◐ sehr wahrscheinlich · ○ Hinweis/Ermessen.

Insgesamt **141 Punkte**: 34 ●, 58 ◐, 49 ○. Davon stehen 9 bereits in der Arbeitsliste `Fahnenkorrektur_Springer_LNM1184.md` (als „Schon in der Arbeitsliste“ markiert).

## Auffälligste Punkte

- **S. 73, Example 3.1.4:** Das optionale Argument steht hinter `\label`; „[Hilbert space, Zabczyk]“ wird deshalb als Fließtext gedruckt statt im Kopf des Beispiels.
- **Mehrere Klammerfehler in Formeln** (Kap. 2: Z. 657, 1645, 1675, 1679; Kap. 1: Z. 767).
- **Vertauschte oder falsche Variablen/Indizes**, z. B. `1/2` statt `s/2` (Kap. 1, Z. 470), `f_f'` statt `\xi_f'` (Kap. 1, Z. 1332/1337), `\lim_{t\to0}` statt `\lim_{n\to\infty}` (Kap. 2, Z. 2031), `t\to\infty` statt `t\to0` (Kap. 3, Z. 1155), fehlendes Minus in der Laplace-Transformation (Kap. 4, Z. 205).
- **Tilden `~` im Mathemodus** erzeugen sichtbaren Leerraum (Kap. 2, Z. 1473, 1914, 1951).

## Einzelbefunde

### Teil I, Kap. 1 – Basic Results on Semigroups on Banach Spaces (`part-a/chap-a1.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 4 | 69 | ◐ | `$ T(t)_{t\geq0} $` | `$ (T(t))_{t\geq0} $` | Klammern | **Umgesetzt.** Sonst überall `(T(t))_{t\geq0}`; ebenso Z. 78. |
| 4 | 104 | ◐ | `$ -\infty \leq \omega < +\infty$` | `$ -\infty \leq \omega_{0} < +\infty$` | Tippfehler | **Umgesetzt.** Im Satz geht es um ω₀. |
| 6 | 220 | ◐ | `\frac{d}{\dt}\xi(t)` | `\frac{\diff{}}{\dt}\xi(t)` | Notation | **Umgesetzt.** Kursives d; in Z. 187, 321, 648 aufrecht. Ebenso Z. 785 `\frac{d}{\dx}`. |
| 7 | 285 | ◐ | `\text{ for $ n \geq 2 $, }` | `\text{ for $ n \geq 2 $.}` | Satzzeichen | **Umgesetzt.** Danach beginnt ein neuer Satz („Then“, Z. 288). |
| 9 | 380 | ◐ | `= \colon  \eu^{tA}` | `\eqqcolon \eu^{tA}` | LaTeX | **Umgesetzt.** `= \colon` ergibt „= :“ mit falschem Abstand; ebenso Z. 561 und 818. |
| 9 | 448 | ◐ | `for all $ (k \geq 2)$` | `for all $ k \geq 2 $` | Klammern | **Umgesetzt.** Überflüssige Klammern. |
| 9 | 470 | ● | `\eu^{t( A - 1/2  \cdot \Id )}` | `\eu^{t( A - s/2  \cdot \Id )}` | Tippfehler | **Umgesetzt.** In Z. 451 und 471 steht s/2. |
| 9 | 472 | ◐ | `\sum_{ \text{k even} }` | `\sum_{k \text{ even}}` | Mathemodus | **Umgesetzt.** k aufrecht in Textschrift; ebenso `\text{k odd}`. |
| 14 | 767 | ● | `…$Af \coloneq f'$}. \}` | `…, f' \in E\}, \quad Af \coloneq f'.` | Klammern | **Umgesetzt** (stand schon so im Text). Punkt vor `\}`, und „Af := f′“ steht innerhalb der Mengenklammer. |
| 15 | 814 | ○ | `\cos \pi nx` | `\cos(\pi nx)` | Notation | **Umgesetzt.** Z. 851 mit Klammern, Z. 814 und 858 ohne. |
| 15 | 871 | ● | `k_{t}(x,y)dy` | `k_{t}(x,y)\dy` | Notation | **Umgesetzt.** Kursives d ohne Abstand; sonst `\dy`. Ebenso Z. 884 `f(y)dy`. |
| 16 | 878 | ◐ | `\subsection{n-dimensional …}` | `\subsection{\texorpdfstring{$n$}{n}-dimensional …}` | Mathemodus | **Umgesetzt.** n nicht im Mathemodus (im Index steht `$n$`). |
| 16 | 881 | ○ | `$1 \leq p \leq \infty$` | `$1 \leq p < \infty$` | Tippfehler | **Umgesetzt** (stand schon so im Text). Auf L^∞ nicht stark stetig, 𝒮 dort nicht dicht (Z. 906); inhaltlich bitte prüfen. |
| 16 | 916 | ● | `T(t)\vert_{ S(\R^{n})}` | `T(t)\vert_{\mathcal{S}(\R^{n})}` | Notation | **Umgesetzt.** Schwartz-Raum sonst `\mathcal{S}`. |
| 16 | 952 | ○ | `$L^{p}\interval{0,1}$` | `$L^{p}(\interval{0,1})$` | Notation | **Umgesetzt.** Z. 755 und 1176: `L^p([0,1])`. |
| 19 | 1047 | ◐ | `$(T(t)_{\vert})$` | `$(T_{\vert}(t))_{t \geq 0}$` | Notation | **Umgesetzt.** Z. 1035 definiert `T_{\vert}(t)`; Einschränkungen insgesamt uneinheitlich notiert (Z. 1167, 1251, 1379). |
| 20 | 1109 | ○ | `\hat{g} \, \ds` | `\hat{g} \ds` | Abstand | **Umgesetzt.** Zusätzliches `\,` nur in Z. 1109–1111. |
| 20 | 1115 | ○ | `$\lambda > \omega$` | `$\lambda > \omega_{0}$` | Notation | **Umgesetzt.** ω ohne Index hier nicht definiert. |
| 20 | 1159 | ◐ | `(see Example~\ref{subsec:a1-2.4})` | `(see Section~\ref{subsec:a1-2.4})` | Verweis | **Umgesetzt** (stand schon so im Text). Schon in der Arbeitsliste (S. 20). |
| 20 | 1173 | ◐ | `f \in AC` | `f \in \mathrm{AC}` | Notation | **Umgesetzt.** Z. 1187 `\mathrm{AC}`; ebenso Z. 1362. |
| 20 | 1177 | ○ | `quotient space \mfrac{F}{I}, where` | `quotient space $\mfrac{F}{I}$, where` | Mathemodus | **Umgesetzt.** `\mfrac` ist für den Mathemodus gedacht (vgl. Z. 1088). |
| 21 | 1265 | ◐ | `\lim\sup_{t \to 0}` | `\limsup_{t \to 0}` | LaTeX | **Umgesetzt.** Index hängt sonst nur am sup; ebenso Z. 1512. |
| 22 | 1332 | ● | `\vert f_f'(0) - f_f'(s)\vert` | `\vert \xi_f'(0) - \xi_f'(s)\vert` | Tippfehler | **Umgesetzt.** Gemeint sind die Funktionen ξ_f (Z. 1295, 1328); ebenso Z. 1337 `f'_f(0)`. |
| 22 | 1347 | ○ | `$0 \leq s \leq t_{0}$` | `$0 < s \leq t_{0}$` | Tippfehler | **Umgesetzt.** Bei s = 0 ist 1/s nicht definiert; Z. 1332: 0 < s < t₀. |
| 23 | 1398 | ● | `\emph{n-th Sobolev space}` | `\emph{$n$-th Sobolev space}` | Mathemodus | **Umgesetzt.** Zweimal in der Zeile (auch „n-th Sobolev semigroup“). |
| 26 | 1500 | ○ | `E_{\mathcal{F}}^{T}` | `E_{\mathcal{F}}^{\TT}` | Notation | **Umgesetzt.** Daneben `m^{\TT}(E)`; ebenso Z. 1506, 1507, 1526, 1542 – bitte prüfen, ob gewollt. |
| 26 | 1522 | ◐ | `T(t)_{F}` | `T(t)_{\mathcal{F}}` | Notation | **Umgesetzt.** Gemeint ist der Filter 𝓕, nicht der Raum F; ebenso Z. 1523. |
| 27 | 1583 | ○ | `let $X$,$Y$ be` | `let $X$, $Y$ be` | Abstand | **Umgesetzt.** Leerzeichen nach dem Komma fehlt. |
| 27 | 1605 | ● | `on $E \times F$` | `on $E \otimes F$` | Tippfehler | **Umgesetzt.** Gemeint ist die Norm auf dem Tensorprodukt (Z. 1601, 1609). |
| 27 | 1628 | ○ | `L^{1}(\mu \otimes \nu)` | `L^{1}(\mu \times \nu)` | Notation | **Umgesetzt.** Z. 1574, 1580: `\mu \times \nu`; ebenso Z. 1630. |
| 28 | 1683 | ◐ | `(T(h) \otimes S(h))(f \otimes g)` | `(S(h) \otimes T(h))(f \otimes g)` | Tippfehler | **Umgesetzt.** Im Satz heißt das Produkt S(t)⊗T(t); im Beweis vertauscht, auch Z. 1686. |

### Teil I, Kap. 2 – Characterization of Semigroups on Banach Spaces (`part-a/chap-a2.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 32 | 92 | ◐ | `u'(t) = Au(t)` | `\dot{u}(t) = Au(t)` | Notation | **Umgesetzt.** Sonst durchgehend `\dot{u}` (z. B. Z. 86). |
| 33 | 148 | ● | `\tilde{v}(s) = v(s) & \text{$0 \leq s \leq t$.}` | `v(s) & \text{for $0 \leq s \leq t$.}` | Tippfehler | **Umgesetzt.** „ṽ(s) =“ im zweiten cases-Zweig doppelt; „for“ fehlt. |
| 36 | 388 | ○ | `Then $ \overline{A} $ satisfies` | `Then $ A $ satisfies` | Tippfehler | **Umgesetzt.** Eingeführt wird die Einschränkung A, nicht ihr Abschluss; bitte prüfen. |
| 36 | 417 | ○ | `u(t) = (f + tBg,g)` | `u(t) = (f - tBg,g)` | Tippfehler | **Umgesetzt.** Gelöst mit f − tBg (passend zur Matrix in Z. 398). math-error-part-a, Z. 409, ist damit mit λf + Bg zu lösen, nicht durch Änderung der Matrix. Mit A = (0 −B; 0 0) wäre u̇ = (−Bg, 0); nur Hinweis. |
| 38 | 528 | ● | `is dense in E and` | `is dense in $E$ and` | Mathemodus | **Umgesetzt.** E ohne Mathemodus. |
| 39 | 552 | ○ | `~\ref{cor:a2-1.8.2} implies~\ref{cor:a2-1.8.1}` | `~\ref{thm:a2-1.7.2} implies~\ref{thm:a2-1.7.1}` | Verweis | **Umgesetzt.** Gedruckt gleich, aber der Hyperlink führt ins Korollar statt ins Theorem. |
| 40 | 657 | ● | `(\lambda \in S(\alpha_{1} + \pi/2).` | `(\lambda \in S(\alpha_{1} + \pi/2)).` | Klammern | **Umgesetzt.** Äußere Klammer nicht geschlossen. |
| 40 | 686 | ◐ | `$\lambda \in \rho(A)$` | `$\lambda \in \rho(A^{2})$` | Tippfehler | **Umgesetzt.** Gemeint ist die Resolventenmenge von A² (vgl. Z. 957). |
| 41 | 744 | ◐ | `$(U_{i})_{t \geq 0}$ the group` | `$(U_{i}(t))_{t \in \R}$ the group` | Tippfehler | **Umgesetzt.** (t) fehlt; Gruppe, daher t ∈ ℝ (vgl. Z. 747). |
| 42 | 853 | ◐ | `\alpha \in \left]0,\pi/2\right]` | `\alpha \in (0,\pi/2]` | Notation | **Umgesetzt.** Sonst `(0,\pi/2]` (Z. 604, 647, 798); ebenso Z. 1417 `\left]0,1\right]`. |
| 43 | 940 | ◐ | `\Im\{z(t)\}^2/\Re\{z(t)\}^2` | `\Im(z(t)^2)/\Re(z(t)^2)` | Klammern | **Umgesetzt.** Geschweifte Klammern werden gedruckt und lesen sich als (Im z)²; gemeint Im(z²) (Z. 934). |
| 43 | 949 | ● | `(r\eu^{\im\theta}+\omega)^2` | `(r\eu^{\im\theta}+w)^2` | Tippfehler | **Umgesetzt.** Im Beweis heißt es sonst w (Z. 902, 954). |
| 45 | 1020 | ○ | `c\eu^{-b\Re(\lambda)}` | `c\eu^{-b\cdot\Re(\lambda)}` | Notation | **Umgesetzt.** Theorem 1.17 und 1.18 (Z. 1036, 1043) einmal mit, einmal ohne `\cdot`. |
| 46 | 1108 | ○ | `[Proof of Theorem~\ref{thm:a2-1.20}  ]` | `[Proof of Theorem~\ref{thm:a2-1.20}]` | LaTeX | **Umgesetzt.** Schon in der Arbeitsliste (S. 46); ebenso Z. 2502. |
| 46 | 1126 | ● | `T(t) \dt (n \in \N).` | `T(t) \dt \quad (n \in \N).` | Abstand | **Umgesetzt.** Gedruckt „dt(n ∈ ℕ)“. |
| 46 | 1152 | ○ | `\right\lVert` | `\right\rVert` | LaTeX | **Umgesetzt.** Falsches schließendes Normzeichen (optisch gleich). |
| 46 | 1173 | ○ | `T(t)\,\dt` | `T(t)\dt` | Abstand | **Umgesetzt.** Zusätzliches `\,` nur in Z. 1173–1180, 1544, 1551, 1638, 1644–1647. |
| 50 | 1370 | ◐ | `[\text{ess}]\text{-}\text{image}(m)` | wie Z. 1455 (`\Image{m}`) | Notation | **Umgesetzt.** Dasselbe Objekt einmal „image“, einmal „im“. |
| 50 | 1411 | ◐ | `H \coloneq \{m(x) \colon \Re(\lambda) \geq b …` | `H \coloneq \{\lambda \in \C \colon \Re(\lambda) \geq b …` | Tippfehler | **Umgesetzt.** Bedingung über λ, im Mengenterm steht m(x). |
| 50 | 1420 | ● | `[\text{ess}]\text{-}\esssup\left\{` | `[\text{ess}]\text{-}\sup\left\{` | Notation | **Umgesetzt.** Gedruckt „[ess]-ess sup“; vgl. Z. 1427. |
| 50 | 1473 | ● | `S(\theta + \pi/2) \subset~\rho(A)` | `S(\theta + \pi/2) \subseteq \rho(A)` | LaTeX | **Umgesetzt.** Tilde im Mathemodus erzeugt Leerraum; sonst `\subseteq`. |
| 50 | 1509 | ○ | `\iu \cdot \exp(n^{2})` | `\iu\,\eu^{n^{2}}` | Notation | **Umgesetzt.** Z. 1509, 1513, 1517 einheitlich `\iu\,…`. Die drei Beispiele (Z. 1509, 1513, 1517) uneinheitlich. |
| 53 | 1628 | ◐ | `(T(t+s-h) - T(t-s))` | `(T(t+h-s) - T(t-s))` | Tippfehler | **Umgesetzt.** Z. 1647 hat t+h−s; ebenso Z. 1634, 1638. |
| 54 | 1645 | ● | `\int_{0}^{t} (T(t-s)BS(s)\, \ds` | `\int_{0}^{t} T(t-s)BS(s)\, \ds` | Klammern | **Umgesetzt.** Öffnende Klammer ohne schließende. |
| 54 | 1646 | ○ | `\leq \|T(t+h) - T(t)\| &+ …` | `&\leq \|T(t+h) - T(t)\| + …` | LaTeX | **Umgesetzt.** ≤ links vom Ausrichtungspunkt, Ausrichtung verschoben. |
| 54 | 1675 | ● | `= (\Id - SR(\lambda,A)` | `= (\Id - SR(\lambda,A))` | Klammern | **Umgesetzt.** Schließende Klammer fehlt. |
| 54 | 1679 | ● | `$(\Id -BR(\lambda,A))^{-1})$` | `$(\Id -BR(\lambda,A))^{-1}$` | Klammern | **Umgesetzt.** Überzählige schließende Klammer. |
| 57 | 1819 | ○ | `\emph{p-contractive}`, `p-dissipative` | `$p$-contractive`, `$p$-dissipative` | Mathemodus | **Umgesetzt.** Außer in `\index`-Einträgen. p steht aufrecht, `$N$-`, `$p$-` (Z. 2248) dagegen kursiv; ca. 30 Stellen in Z. 1819–2272. |
| 58 | 1914 | ● | `$\phi~\in~\ddp(f)$` | `$\phi \in \ddp(f)$` | LaTeX | **Umgesetzt.** Tilden im Mathemodus erzeugen Leerraum. |
| 58 | 1947 | ○ | `for all $t > 0$, \\` | `for all $t > 0$,` | LaTeX | **Umgesetzt.** `\\` vor abgesetzter Formel. |
| 58 | 1951 | ● | `p(f)~& \leq~p(f-tAf)` | `p(f) &\leq p(f-tAf)` | LaTeX | **Umgesetzt.** Tilden im Mathemodus. |
| 59 | 2031 | ● | `T(t) = \lim_{t\to 0} \left( \frac{n}{t} …` | `T(t) = \lim_{n\to\infty} \left( \frac{n}{t} …` | Tippfehler | **Umgesetzt.** Grenzübergang über n (vgl. Z. 584). |
| 60 | 2116 | ○ | `(this is equivalent … {schaefer:1966}).` | `… {schaefer:1966})).` | Klammern | **Umgesetzt.** Schon in der Arbeitsliste (S. 61). |
| 62 | 2235 | ◐ | `from~\ref{thm:a2-2.6} it follows` | `from Theorem~\ref{thm:a2-2.6} it follows` | Verweis | **Umgesetzt.** Schon in der Arbeitsliste (S. 62). |
| 63 | 2274 | ◐ | `p((1-tA)f) \geq p(f)` | `p((\Id-tA)f) \geq p(f)` | Notation | **Umgesetzt.** Identität sonst `\Id`. |
| 63 | 2281 | ● | `if it is N-dissipative` | `if it is $N$-dissipative` | Mathemodus | **Umgesetzt.** Z. 1861 schreibt `$N$-dissipative`. |
| 64 | 2311 | ◐ | `\lim\sup_{t\to 0}` | `\limsup_{t\to 0}` | Notation | **Umgesetzt.** Z. 2014 `\limsup`; ebenso Z. 2322, 2323, 2341, 2431. |
| 64 | 2341 | ○ | `< 1\ ,` | `< 1 ,` | Satzzeichen | **Umgesetzt.** Leerzeichen vor dem Komma. |
| 66 | 2513 | ◐ | `and $H^{\infty}$ does not only contain` | `and $H^{\infty}(O)$ does not only contain` | Tippfehler | **Umgesetzt.** Im selben Satz `H^{\infty}(O)`. |

### Teil I, Kap. 3 – Spectral Theory (`part-a/chap-a3.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 73 | 182 | ● | `\begin{example}\label{ex:a3-1.4}[Hilbert space, \textcite{zabczyk:1975}]` | `\begin{example}[Hilbert space, \textcite{zabczyk:1975}]\label{ex:a3-1.4}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Optionales Argument hinter `\label`: „[Hilbert space, …]“ erscheint als Fließtext statt im Kopf des Beispiels (vgl. Z. 127). |
| 73 | 207 | ○ | `$n \in \N$ ,` | `$n \in \N$,` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Leerzeichen vor dem Komma; dasselbe Muster in Z. 210, 712, 1050, 1053, 1056, 1162, 1163, 1166, 1215, 1383, 1386, 1432, 1490, 1493, 1713, 1733, 1736, 2206. |
| 73 | 234 | ◐ | `continuous on each component $E_{n}$` | `$H_{n}$` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Komponenten heißen H_n (Z. 184, 220). |
| 76 | 355 | ● | `(\text{dist}(x,\sigma(A)))^{-1}` | `(\mathrm{dist}(\lambda_{n},\sigma(A)))^{-1}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). x statt λ_n; sonst `\mathrm{dist}` (Z. 537). |
| 76 | 358 | ◐ | `Proposition~\ref{prop:a3-2.5}\,(ii)` | `…\,(i)` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste (S. 76). |
| 76 | 392 | ◐ | `q \colon X \mapsto \C` | `q \colon X \to \C` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst `\to` (Z. 1933, 1948). |
| 76 | 402 | ○ | `\eu^{tq} \cdot f \, , \, f \in E .` | `\eu^{tq} \cdot f, \quad f \in E .` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst `, \quad`; ebenso Z. 2141, 2293. |
| 76 | 431 | ○ | `spectral value of\/ $A$` … | `$M_{q}$` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Ebenso Z. 434 ($\sigma(M_{q}) = A\sigma(M_{q})$). Im Beispiel heißt der Generator sonst M_q (Z. 431–434). |
| 77 | 467 | ○ | `\epsilon_{\lambda}` (vs. `e_{\lambda}` Z. 160) | einheitlich `\epsilon_{\lambda}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst ε_λ (Z. 520, 708, 1515). |
| 78 | 603 | ◐ | `\diff{z} = \\ &= …` | `\diff{z} \\ &= …` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Doppeltes Gleichheitszeichen am Zeilenende und -anfang. |
| 82 | 757 | ◐ | `$T_{1} = (T(t)P)_{t \geq 0}$` | `$\TT_{1} = …$` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Halbgruppen sonst 𝒯_i (Z. 669, 685, 727); ebenso Z. 774 (T₃), 801 (ω₀(T₁)). |
| 82 | 808 | ● | `Theorem~~\ref{thm:a3-3.3}` | `Theorem~\ref{thm:a3-3.3}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Doppelte Tilde, sichtbar doppelter Abstand. |
| 83 | 817 | ◐ | `(see~\ref{prop:a3-6.2})` | `(see Proposition~\ref{prop:a3-6.2})` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste (S. 83). |
| 86 | 1070 | ◐ | `D(A)\backslash N` | `D(A) \setminus N` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst `\setminus` (Z. 537, 1446). |
| 86 | 1071 | ○ | `E_{/}` | `E/N` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Fehlender Schlusspunkt (Arbeitsliste S. 87) ebenfalls ergänzt. Z. 1018: E/N; ebenso Z. 1077, 1084. (Fehlender Schlusspunkt schon in der Arbeitsliste, S. 87.) |
| 87 | 1134 | ○ | `we have \quad $…$, $\quad R… = \sum U_{n\vert}…$` | abgesetzte Formel, einheitlich `\sum_{n}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Als abgesetzte Formel (`gather*`, wegen der Breite zweizeilig). `\quad` im Fließtext, Tilde am Ende, Summe teils ohne Index (Z. 1134–1135). |
| 88 | 1155 | ● | `\lim_{t \to \infty} \|T(t)'\phi-\phi\| = 0` | `\lim_{t \to 0} …` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Definition des Halbgruppen-Duals über t → 0 (vgl. chap-a1 Z. 1245). |
| 88 | 1173 | ◐ | `\ref{prop:a3-2.2}(ii)` | `Proposition~\ref{prop:a3-2.2}\,(ii)` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste (S. 88). |
| 89 | 1233 | ● | `({\hat{f}^{m}})_{n \in \N}` | `(\hat{f}^{m})_{m \in \N}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Folge läuft über m. |
| 91 | 1351 | ● | `the n-th Fourier coefficient` | `the $n$-th Fourier coefficient` | Mathemodus | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). n nicht im Mathemodus. |
| 93 | 1511 | ○ | `generator\quad $Af(z) = …$\quad is …` | ohne `\quad` | Abstand | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). `\quad` im Fließtext (Z. 1511–1514). |
| 93 | 1525 | ○ | `Q_{m} \coloneq \sum_{-m}^{+m} P_{n}$ in $L^{p}(\Gamma,m)` | anderer Index, z. B. `Q_{N}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). m zugleich Summationsgrenze und Maß. |
| 94 | 1574 | ○ | `$\sigma(T(t)) = \Gamma$` | `$\sigma(R_{\tau}(t)) = \Gamma$` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). In (ii) heißt die Gruppe R_τ(t) (Z. 1572). |
| 96 | 1702 | ◐ | `(see Proposition~\ref{prop:a3-4.4})` | `(see Section~\ref{subsec:a3-4.4})` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste (S. 96). |
| 97 | 1736 | ◐ | `\overline{\text{span}_{n \in \Z} \{P_{n}E\}}` | `\overline{\mathrm{span}_{n \in \Z} …}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). `\text{span}` wird im kursiven Korollar kursiv; Z. 1716 `\mathrm{span}`. |
| 97 | 1772 | ○ | `\label{eq:a3-6.6)}` | `\label{eq:a3-6.6}` | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Überzählige Klammer im Label (derzeit nicht referenziert). |
| 97 | 1815 | ◐ | `(see~\ref{cor:a3-1.2})` | `(see Corollary~\ref{cor:a3-1.2})` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Bezeichnung fehlt, gedruckt nur die Nummer. |
| 98 | 1898 | ○ | `Theorem~\ref{thm:a2-1.20} )` | `Theorem~\ref{thm:a2-1.20})` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Schon in der Arbeitsliste (S. 99). |
| 102 | 2099 | ◐ | `\widehat{\left(\eu^{\im 2k}\check{\phi_{0}}\right)}` | `\widehat{\left(\eu^{\im 2k\cdot}\check{\phi_{0}}\right)}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Variable fehlt im Exponenten (vgl. Z. 2161 `\eu^{\im\pi\cdot}`). |
| 103 | 2150 | ○ | `\eu^{-\im n0}` | `\eu^{-\im n\cdot 0}` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). „n0“ liest sich wie ein Symbol. |
| 105 | 2194 | ● | `C_{1}\text{-}\sum_{k\in\Z} \xi_{n}` | `C_{1}\text{-}\sum_{k\in\Z} \xi_{k}` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Summationsindex k, Summand mit n. |
| 106 | 2269 | ◐ | `< \infty$~, then\quad $…$\quad is summable` | `< \infty$, then $…$ is summable` | Satzzeichen | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Geschütztes Leerzeichen vor Komma, `\quad` im Fließtext. |
| 106 | 2270 | ○ | Leerzeile in Item (ii) | Leerzeile entfernen | LaTeX | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Absatzumbruch mitten im Satz. |
| 106 | 2286 | ◐ | `(use Eq.~\myeqpageref{eq:a3-7.5})` | `eq:a3-7.7` | Verweis | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Benötigt wird die Definition von Q_k (7.7), nicht (7.5). |
| 106 | 2311 | ● | `\eu^{-\im ks}g_{k}\right\|^{2} \dx` | `… \ds` | Tippfehler | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Integrationsvariable ist s. |
| 106 | 2313 | ○ | `c(\sum_{k\in N} \|g_{k}\|^{2})^{1/2}` | `c\left(\sum … \right)^{1/2}` | Klammern | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Klammern zu klein; daneben mit `\left(…\right)`. |
| 107 | 2335 | ○ | `\not\in` (2×) | `\notin` | Notation | **Umgesetzt** (20.10.2026, Freigabe G. Greiner). Sonst `\notin`. |

### Teil I, Kap. 4 – Asymptotics of Semigroups on Banach Spaces (`part-a/chap-a4.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 111 | 54 | ● | `$ f \in \C^{n} $ ,` | `$ f \in \C^{n} $,` | Satzzeichen | Leerzeichen vor dem Komma; ebenso Z. 693. |
| 111 | 71 | ◐ | `Chapter~\ref{chap:c3}` | `Chapter~\ref{chap:a3}` | Verweis | Gemeint ist wohl Kap. 3 (Spektraltheorie) dieses Teils; Verweise in andere Teile haben sonst „Part-…“. |
| 112 | 79 | ◐ | `($1^{st}$ part)` | `(1\textsuperscript{st} part)` | Mathemodus | „st“ kursiv; ebenso Z. 111 `$2^{nd}$`. |
| 113 | 176 | ● | `$\Im(\Delta) \not= C_0(\R^{n})$` | `$\Image{\Delta} \not= C_0(\R^{n})$` | Notation | `\Im` ist der Imaginärteil; Bild sonst `\Image` (Z. 888). |
| 113 | 205 | ● | `\int_{0}^{\infty} \eu^{\lambda t} T(t)f \dt` | `\int_{0}^{\infty} \eu^{-\lambda t} T(t)f \dt` | Tippfehler | Minus im Exponenten fehlt (vgl. Z. 528). |
| 113 | 219 | ○ | `\|T(t)f\| \leq M\eu^{\lambda t}` | `\|T(t)f\| \leq M\eu^{\Re(\lambda) t}` | Notation | λ ist komplex (Z. 205). |
| 115 | 255 | ◐ | `\int_{0}^{t} \eu^{\mu s} f(s) \ds` | `\int_{0}^{t} \eu^{-\mu s} f(s) \ds` | Tippfehler | Ebenso Z. 256 `\eu^{\mu r}`; passt dann zu Z. 262. |
| 115 | 292 | ◐ | `\begin{enumerate}[(i)]` | `\begin{enumerate}[\upshape (i)]` | Notation | Labels werden sonst kursiv; ebenso Z. 300, 910. |
| 115 | 295 | ○ | `\inf\{\Re(\lambda)\colon\int_{0}^{\infty} …\}` | `\inf\left\{…\right\}` | Klammern | Kleine Mengenklammern um Integral; ebenso Z. 303, 357 (Z. 339, 465, 470 skalieren). |
| 116 | 339 | ● | `\|^{-\lambda t} T(t)f\|` | `\|\eu^{-\lambda t} T(t)f\|` | Tippfehler | `\eu` fehlt. |
| 116 | 361 | ◐ | `from Eq.~\myeqpageref{eq:a4-1}` | `from Eq.~\myeqpageref{eq:a4-1.1}` | Verweis | eq:a4-1 ist (*); gemeint (1.1); ebenso Z. 457. |
| 116 | 362 | ○ | `that \[g \coloneqq\lim_{r \to \infty} T(r)f\] exists.` | `that $g \coloneq \lim_{r \to \infty} T(r)f$ exists.` | LaTeX | Abgesetzte Formel mitten im Satz; sonst `\coloneq`. |
| 118 | 474 | ○ | `\eu^{\lambda t} \left\{ f - \int … \right\}` | `\eu^{\lambda t} \left( f - \int … \right)` | Notation | Z. 209 mit runden Klammern. |
| 119 | 552 | ◐ | `x^n \in \C^n\colon\sum_{j=1}^{\infty} …` | `x^n \in \C^n,\ \sum_{j=1}^{\infty} …` | Notation | Zwei `\colon` in einer Mengenklammer; `...` statt `\dots` (auch Z. 569, 588). |
| 119 | 554 | ◐ | `\eu^{2\pi i n t}` | `\eu^{2\pi \im n t}` | Notation | Kursives i; sonst `\im`; ebenso Z. 567, 1167. |
| 119 | 574 | ● | `\|\exp(&t A_n) \cdot e_n\|^2 = \\ &= …` | `… \|^2 \\ &= …` | Tippfehler | Doppeltes Gleichheitszeichen. |
| 119 | 588 | ○ | `x_q :=  (q e_1, …)` | `x_q \coloneq (q e_1, …)` | Notation | Sonst `\coloneq`. |
| 119 | 593 | ◐ | `\| \exp(t A) e_n \|^2` | `\| \exp(t A_n) e_n \|^2` | Tippfehler | e_n ∈ ℂⁿ, gemeint ist A_n (Z. 574). |
| 121 | 633 | ◐ | `\ref{cor:a3-6.7} ).` | `\ref{cor:a3-6.7}).` | LaTeX | Teilweise schon in der Arbeitsliste (S. 121–125); ebenso Z. 638, 792, 837, 879. |
| 121 | 634 | ○ | `$\dot{u}(t) = A u(t), u(0) = x$` | `$\dot{u}(t) = A u(t),\ u(0) = f$` | Notation | Anfangswert sonst f (Z. 41). |
| 121 | 682 | ◐ | `\sup \{ \omega(f),  f \in D(A^n) \}` | `\sup \{ \omega(f) \colon f \in D(A^n) \}` | Notation | Sonst `\colon`. |
| 121 | 690 | ○ | `\max(\omega_{0}(A), q)` | `\max\{\omega_{0}(A), q\}` | Notation | Z. 692, 613, 797: `\max\{…\}`. |
| 122 | 695 | ◐ | `\frac{1}{2\pi i} … f \, d\lambda` | `\frac{1}{2\pi\im} … f \diff{\lambda}` | Notation | Kursives i und d; ebenso Z. 707, 709, 718, 1271. |
| 122 | 711 | ◐ | Leerzeile nach `\end{equation}` | Leerzeile löschen | LaTeX | Fortsetzungssatz bekommt sonst Absatzeinzug. |
| 123 | 755 | ◐ | `$(a)  \Rightarrow  (b)  \Rightarrow  (c) $` | `(a)~$\Rightarrow$ (b)~$\Rightarrow$ (c)` | Notation | Labels im Mathemodus kursiv; ebenso Z. 766, 923, 928, 930, 935, 937. |
| 124 | 840 | ◐ | `T(t)^* \phi = \exp(\lambda t) \phi` | `T(t)' \phi = \eu^{\lambda t} \phi` | Notation | Adjungierte sonst mit ′ (Z. 839); Z. 837 `\eu^{\lambda t}`. |
| 127 | 1015 | ◐ | `F(t) \quad , \quad u(0) = f,` | `F(t), \quad u(0) = f,` | Satzzeichen | Großer Abstand vor dem Komma. |
| 127 | 1050 | ◐ | `$t\to T(t)g$` | `$t\mapsto T(t)g$` | Notation | Abbildungsvorschrift (vgl. Z. 1044). |
| 128 | 1095 | ◐ | `Theorem~\ref{prop:a1-1.6}` | `Proposition~\ref{prop:a1-1.6}` | Verweis | Label gehört zu einer Proposition. |
| 130 | 1202 | ◐ | `\{f \in E: f' \in C^{1} \text{ and } f' \in E\}` | `\{f \in E\colon f \in C^{1} \text{ and } f' \in E\}` | Tippfehler | Gemeint f ∈ C¹; `:` statt `\colon`. |
| 130 | 1208 | ○ | `\tag{*}` | anderes Tag, z. B. `\tag{$\ast\ast\ast$}` | Verweis | (*) schon in Z. 24 vergeben; Bezug in Z. 1212/1234 mehrdeutig. Kursives d in `\frac{d}{dx}` (Z. 1202, 1208). |
| 130 | 1254 | ○ | `Example~\ref{ex:a4-1.2}(ii)` | `Example~\ref{ex:a4-1.2}\,(ii)` | Abstand | Sonst mit `\,`. |
| 131 | 1277 | ○ | `statements Eq.~\myeqpageref{eq:a4-1.12}, Eq.~\myeqpageref{eq:a4-1.13}` | prüfen | Verweis | (1.12), (1.13) sind Inversionsformeln; vermutlich Nummerierung der 1. Auflage. |
| 131 | 1279 | ○ | `\textcite{datko:1970}` | prüfen | Verweis | Z. 802 nennt `datko:1972`. |

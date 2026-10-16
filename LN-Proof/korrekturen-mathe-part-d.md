# Formelprüfung Part D (Teil IV): Satz und Notation

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184). Stand: 14.10.2026.

**Umfang:** Teil IV, Kap. 1–4, geprüft im LaTeX-Quelltext (Branch `fahnenkorrektur`). Geprüft wurden nur Satz und Notation in Formeln: Tippfehler, Klammern, Indizes, uneinheitliche Schreibweisen, Mathemodus, Satzzeichen an Formeln, Verweise. Beweise wurden **nicht** nachgerechnet; wo ein Befund inhaltlich wirkt, steht „bitte prüfen“.

**Noch nichts geändert.** Die Liste dient zur Besprechung; umgesetzt wird erst nach Rücksprache.

**Spalten:** S. = gedruckte Buchseite, ermittelt über das nächstgelegene Label (kann um eine Seite abweichen). Z. = Zeile in der .tex-Datei. Sicherheit: ● eindeutig · ◐ sehr wahrscheinlich · ○ Hinweis/Ermessen.

Insgesamt **122 Punkte**: 40 ●, 55 ◐, 27 ○. Davon stehen 9 bereits in der Arbeitsliste `Fahnenkorrektur_Springer_LNM1184.md` (im Kommentar markiert).

## Einzelbefunde

### Teil IV, Kap. 1 – Basic Results on Semigroups and Operator Algebras (`part-d/chap-d1.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 409 | 52 | ◐ | `\phi \in M'_{+}: \phi(\1) = 1` | `\phi \in M'_{+} \colon \phi(\1) = 1` | Notation | Sonst \colon in Mengenklammern (Z. 32, 38, 46); „:“ ergibt sichtbar anderen Abstand. |
| 409 | 67 | ● | `every n-positive map` | `every $n$-positive map` | Mathemodus | n ohne Mathemodus; in Z. 66 korrekt `$n$-positive`. |
| 410 | 116 | ◐ | `on a\, \CA-algebra` | `on a \CA-algebra` | Abstand | \, plus folgender Wortzwischenraum ergibt sichtbar zu großen Abstand. |
| 410 | 127 | ○ | `\mu R(\mu,A)xx^{*}` | `\mu R(\mu,A)(xx^{*})` | Notation | Uneinheitlich: Z. 120 `T(t)(xx^{*})` und Z. 184 `R(\mu,A)(xx^{*})` mit Klammern, hier und Z. 142, 150, 162, 164 f., 178, 231 ohne; ohne Klammern als (Rx)x^{*} lesbar. |
| 410 | 132 | ◐ | `If\/ $ \,\TT $` | `If\/ $ \TT $` | Abstand | Überzähliger Abstand \, vor \TT. |
| 410 | 140 | ○ | `\left( S(r)x)(S(r)x \right)^{*}` | `(S(r)x)(S(r)x)^{*}` | LaTeX | \left( … \right) über „)(“ hinweg falsch gepaart; optisch unauffällig, aber unsauber; ebenso zweiter Term in Z. 140. |
| 410 | 161 | ● | `(S(t)x)(S(r)x)^{*}  \dr \dt \right)` | `(S(t)x)(S(r)x)^{*}) \dr \dt \right)` | Klammern | Die in Z. 160 mit `((S(r)x)…` geöffnete runde Klammer wird nicht geschlossen (vgl. Z. 162). |
| 410 | 163 | ● | `\eu^{-\mu s} ds` | `\eu^{-\mu s} \ds` | Notation | Kursives d; sonst \dr, \dt mit aufrechtem d. |
| 411 | 178 | ◐ | `xx^{*} \, , \, x \in M .` | `xx^{*}, \quad x \in M.` | Abstand | Dünnes Leerzeichen vor dem Komma sichtbar; vgl. Z. 206 `x, \quad x \in M`. |
| 411 | 194 | ◐ | `\eu^{- \im  \lambda t }T(t)` | `\eu^{- \im \Im(\lambda) t}T(t)` | Tippfehler | Bitte prüfen: Mit \lambda statt \Im(\lambda) gilt R(\lambda,A) = R(\Re(\lambda),B) nicht; ebenso Z. 197 `B \coloneq A - \im \lambda` → `B \coloneq A - \im \Im(\lambda)`. |
| 412 | 213 | ◐ | `Part-III, Section~\ref{sec:c3-3}` | `Part-III, Section~\ref{sec:c3-2}` | Verweis | Schon in der Arbeitsliste. Pseudo-Resolventen stehen in chap-c3.tex Abschnitt sec:c3-2 (dort auch ex:c3-2.5), sec:c3-3 ist „Irreducible Semigroups“. |
| 412 | 218 | ● | `\mathcal{R} \colon D \mapsto \LE` | `\mathcal{R} \colon D \to \LE` | Notation | Abbildungspfeil zwischen Mengen ist \to (so Z. 304 und Part III, chap-c3 Z. 383). |
| 412 | 262 | ● | `\Fix{ (\lambda R(\lambda,A) }` | `\Fix{\lambda R(\lambda,A)}` | Klammern | \Fix setzt selbst Klammern; gedruckt „Fix((λR(λ,A))“ mit unausgeglichener Klammer. |
| 413 | 312 | ◐ | `\TT_p = (T(t)p)_{t \geq 0}` | `\TT_p = (T(t)_{p})_{t \geq 0}` | Tippfehler | Induzierte Abbildung heißt S_{p} (Z. 304); T(t)p liest sich als Produkt. Bitte prüfen. |
| 413 | 339 | ◐ | `\eqref{item:d1-3.2} above` | `\ref{item:d1-3.2} above` | Verweis | \eqref auf einen Aufzählungspunkt ergibt „(2.) above“; mit \ref „2. above“. |
| 413 | 347 | ○ | `M_{s(\phi)}` | `s(\phi)Ms(\phi)` | Notation | M_{s(\phi)} nirgends eingeführt und leicht mit M_\phi = s(\phi)^\perp M s(\phi)^\perp (Z. 327, 334) zu verwechseln; ebenso Z. 368. Bitte prüfen. |
| 413 | 360 | ● | `s(\phi)M_s(\phi)` | `s(\phi)M_{*}s(\phi)` | Tippfehler | Stern fehlt; gedruckt M mit Index s, danach (φ). |
| 413 | 368 | ◐ | `T_{*_{\vert}}` | `(T_{*})_{\vert s(\phi)M_{*}s(\phi)}` | Notation | Im Quelltext senkrechter Strich als Unter-Index ohne Bezugsraum; sonst `_{\vert F}` mit Raum (Z. 281, 370, 377). |
| 413 | 370 | ◐ | `\phi \in \text{Fix}(T)` | `\phi \in \Fix{\TT}` | Notation | Sonst Makro \Fix (Z. 261 f.); die Halbgruppe heißt hier \TT, nicht T. |

### Teil IV, Kap. 2 – Characterization of Positive Semigroups on W*-Algebras (`part-d/chap-d2.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 418 | 43 | ● | `\TT = (T(t)_{t \geq 0})` | `\TT = (T(t))_{t \geq 0}` | Klammern | Index steht innerhalb der Klammer; sonst im ganzen Buch (T(t))_{t \geq 0}. |
| 418 | 57 | ○ | `\|(T_n - \Id)(u_n)\| \leq n^{-1}` | `\|(T_n - \Id)u_n\| \leq n^{-1}` | Notation | Dieselbe Aussage in Z. 66 ohne Klammern um u_n; einheitlich setzen. |
| 418 | 80 | ◐ | `\in \mathcal{L}(\widehat{M})$` | `\in \mathcal{L}(\widehat{M})$,` | Satzzeichen | Punkte (i)' und (ii)' enden mit Komma, (iii)' vor „and let …“ nicht. |
| 418 | 90 | ◐ | `follows from \upshape(i)', … follows from \upshape(iii)'` | `follows from (i), … follows from (iii)` | Verweis | Bitte prüfen: T(pxp)=pxp folgt aus (i) (gleichmäßige Konvergenz), T(u)=u aus (iii) (Abschätzung für u_n) der ersten Liste; (i)'/(iii)' sind nur die Definitionen von \widehat{M} bzw. T. \upshape im Fließtext ist zudem überflüssig. |

### Teil IV, Kap. 3 – Spectral Theory on W*-Algebras and their Preduals (`part-d/chap-d3.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 421 | 61 | ○ | `\vert\phi(x)\vert^{2} &\leq \vert\phi\vert(xx^{*})` | `\vert\phi(x)\vert^{2} &\leq \|\phi\|\,\vert\phi\vert(xx^{*})` | Tippfehler | Faktor ‖φ‖ fehlt vermutlich; in Z. 299–301 wird (*) mit ‖ψ‖ angewandt. Bitte prüfen. |
| 422 | 110 | ◐ | `0 \leq \psi \in M^{*}` | `0 \leq \psi \in M'` | Notation | Dualraum sonst M' bzw. E' (Z. 34, 389 ff.); ebenso Z. 113 `M^{*}_{+}` → `M'_{+}`. |
| 423 | 142 | ○ | `S(x)(Sx)^{*} \leq T(xx^{*})` | `S(x)S(x)^{*} \leq T(xx^{*})` | Notation | Im selben Ausdruck S(x) und Sx gemischt; Z. 162 und 186 schreiben S(x)S(x)^*. |
| 423 | 151 | ● | `is T-invariant` | `is $T$-invariant` | Mathemodus | T ohne Mathemodus; vgl. Z. 181 „$T$-invariant“. |
| 423 | 159 | ◐ | `b: M\times M \mapsto M` | `b \colon M\times M \to M` | Notation | \mapsto statt \to; Doppelpunkt sonst \colon (Z. 100). Doppelpunkt ebenso Z. 706 `D(A): A\psi`, 767 `\kappa:\R`, 963 `): D \to`, 1158 `J: (M_{*})^{\wedge}`. |
| 423 | 204 | ◐ | `& = 2\vert\phi\vert(uu^{*}) - \phi(u^{*})^{*}` | `& = 2\vert\phi\vert(u^{*}u) - \phi(u^{*})^{*}` | Tippfehler | Z. 203 und 205 haben u^*u; bitte prüfen. |
| 423 | 208 | ◐ | `(Su^{*} - u^{*})(Su^{*} - u^{*}) \in F` | `(Su^{*} - u^{*})(Su^{*} - u^{*})^{*} \in F` | Tippfehler | Stern am zweiten Faktor fehlt (vgl. Z. 195, 202); bitte prüfen. |
| 425 | 299 | ◐ | `\vert^2 \leq \\ &\leq \|\psi\|` | `\vert^2 \\ &\leq \|\psi\|` | LaTeX | Relationszeichen am Zeilenende und am Anfang der Folgezeile doppelt gesetzt; sonst im Kapitel nicht (Z. 338–341). Ebenso Z. 308 `= \\ &=`. |
| 425 | 300 | ◐ | `\dualp{(\mu R(\mu+\im\alpha)'x)(\ldots)^{*},\psi}` | `\dualp{(\mu R(\mu+\im\alpha)'x)(\ldots)^{*},\vert\psi\vert}` | Tippfehler | Nach (*) muss hier der Betrag von ψ stehen (wie Z. 301); bitte prüfen. |
| 425 | 340 | ○ | `\dualp{R(\phi^{+}), \1}` | `\dualp{\1, R(\phi^{+})}` | Notation | Reihenfolge der dualen Paarung sonst ⟨x, ψ⟩ (Z. 299, 309, 517); ebenso `\dualp{R(\phi^{-}), \1}`. |
| 426 | 408 | ◐ | `0 \neq \psi_{0} \in \Fix{S}` | `0 \neq \psi_{0} \in \Fix{S'}` | Tippfehler | ψ_0 liegt in Fix(S') (Z. 399); danach „Fix(S') separates the points“. |
| 428 | 537 | ○ | `A'u_{\alpha} = \im\alpha u_{\alpha}` | `A'u_{\alpha}^{*} = \im\alpha u_{\alpha}^{*}` | Tippfehler | Im Beweis (Z. 485) gilt die Gleichung für u_α^*; bitte prüfen. |
| 428 | 561 | ○ | `\{0, \lambda, \lambda^{*}\}` | `\{0, \lambda, \overline{\lambda}\}` | Notation | Stern steht sonst für Involution/Adjungierte; wegen λ ∈ iR ggf. einfach −λ. Bitte prüfen. |
| 429 | 582 | ◐ | `\im \, \R` | `\im\R` | Abstand | Sonst überall \im\R ohne Zwischenraum. |
| 429 | 640 | ○ | `\circ V_{\alpha}^{-1} \quad (1)` | `\circ V_{\alpha}^{-1} \tag{1}` | LaTeX | Handgesetzte Nummern stehen nicht am rechten Rand wie (*) in Z. 62; ebenso Z. 648 (dort zusätzlich Punkt vor (2), bei (1) und (3) nicht) und Z. 654. |
| 429 | 645 | ● | `$i\beta \in P\sigma(A)$` | `$\im\beta \in P\sigma(A)$` | Notation | Kursives i statt \im. |
| 429 | 645 | ◐ | `\1 = u_{\beta}u_{\beta}^{*} = u_{\beta}u_{\beta}^{*}` | `\1 = u_{\beta}u_{\beta}^{*} = u_{\beta}^{*}u_{\beta}` | Tippfehler | Zweimal derselbe Ausdruck; vgl. Z. 620. |
| 429 | 662 | ○ | `\sigma(R(\mu+\im\alpha))` | `\sigma(R(\mu+\im\alpha,A))` | Notation | Im selben Ausdruck R(\mu,A); Argument A fehlt. |
| 430 | 695 | ○ | `G \coloneq (\TT_{0})^{-}` | `G \coloneq \overline{\TT_{0}}` | Notation | Abschluss uneinheitlich: ^{-} (Z. 695, 710 \closure) neben \overline (Z. 698, 743, 789). |
| 430 | 709 | ◐ | `U = \{U(\eta) \colon \eta \in \Omega\}` | `U \coloneq \bigcup_{\eta \in \Omega} U(\eta)` | Tippfehler | Mengensystem statt Vereinigung; danach „ψ ∈ U“ und Abschluss von U = N_*. Bitte prüfen. |
| 430 | 715 | ◐ | `\{\eu^{-\eta t}\psi \colon t \in \R_{+}\}` | `\{\eu^{\eta t}\psi \colon t \in \R_{+}\}` | Tippfehler | Wegen Aψ = ηψ; Z. 725 ohne Minuszeichen. Bitte prüfen. |
| 430 | 721 | ◐ | `\psi_{1}, ..., \psi_{n}` | `\psi_{1}, \dots, \psi_{n}` | LaTeX | „...“ im Mathemodus ergibt eng gesetzte Punkte; ebenso Z. 732 (zweimal), 1067, 1068. |
| 430 | 743 | ● | `\subseteq L_{s}(N_{*})` | `\subseteq \mathcal{L}_{s}(N_{*})` | Notation | Sonst kalligraphisches L (Z. 695, 698, 718, 963); ebenso Z. 1137 `L(\widehat{E})` → `\mathcal{L}(\widehat{E})`. |
| 430 | 752 | ◐ | `S \coloneq \lim_{\mathfrak{U}}T(t-s)` | `S \coloneq \lim_{\mathfrak{U}}T_{0}(t-s)` | Notation | Im Beweis sonst T_0 (Z. 748, 758). |
| 431 | 783 | ◐ | `fulfils the assertions of Theorem 1.10` | `fulfils the assertions of Theorem~\ref{thm:d3-1.11}` | Verweis | Schon in der Arbeitsliste. Hart codierte Altnummer. |
| 432 | 820 | ● | `\{p_{1}, .., p_{n}\}` | `\{p_{1}, \ldots, p_{n}\}` | Tippfehler | Nur zwei Punkte; ebenso Z. 957 `(x, x, ..)` → `(x, x, \dots)`. |
| 432 | 824 | ◐ | `from Lemma 1.1.b that` | `from Lemma~\ref{lem:d3-1.1}\,\ref{item:d3-1.1-ii} that` | Verweis | Schon in der Arbeitsliste. Hart codierte Altnummer. |
| 432 | 827 | ◐ | `x(\mu \RR'(\mu)y)` | `x(\mu R(\mu)'y)` | Notation | Links R(\mu)', rechts kalligraphisches \RR'(\mu). |
| 432 | 843 | ● | `\leq (\1-s(\vert\psi_{\alpha}\vert) , \mu` | `\leq \1-s(\vert\psi_{\alpha}\vert) , \mu` | Klammern | Öffnende Klammer ohne Gegenstück (vgl. Z. 461 f.). |
| 432 | 895 | ◐ | `\mu R(\mu)'(x u_{\alpha})u_{\alpha}^{*}` | `\mu R(\mu)'(x u_{\alpha}^{*})u_{\alpha}` | Tippfehler | Z. 889 und 903 haben (xu_α^*)u_α; bitte prüfen. |
| 432 | 912 | ● | `\Fix  {\lambda R(\lambda)')\vert M(u_{\alpha}u_{\alpha}^{*}}` | `\Fix{\lambda R(\lambda)'\vert M(u_{\alpha}u_{\alpha}^{*})}` | Klammern | Schließende Klammer steht hinter R(λ)' statt hinter u_α u_α^* (vgl. Z. 911). |
| 432 | 927 | ◐ | `\dim \Fix{\lambda R(\lambda)'} , \\` | `\dim \Fix{\lambda R(\lambda)'} \\` | Satzzeichen | Komma mitten in der Gleichungskette. |
| 435 | 1058 | ◐ | `= \lim \|z - x_{n}\| = 0` | `= \lim_{n} \|z - x_{n}\| = 0 .` | Satzzeichen | Schlusspunkt fehlt (nächster Satz „Consequently“); \lim ohne Index, sonst \lim_{n}. |
| 435 | 1075 | ◐ | `R(\lambda)} \bigoplus \bigcap_{j=1}^{n}` | `R(\lambda)} \oplus \bigcap_{j=1}^{n}` | LaTeX | \bigoplus ist ein großer Operator; als binäres Zeichen \oplus. |
| 435 | 1088 | ○ | `\bigcap_{j=1}^{n} \ker\phi_{j}` | `\bigcap_{j=1}^{n} \Kern{\phi_{j}}` | Notation | Z. 1075 und 1090 ker(φ_j) mit Klammern; ebenso Z. 1099. |
| 437 | 1161 | ○ | `\dualp{x,J(\widehat{\phi})}` | `\dualp{\hat{x},J(\widehat{\phi})}` | Tippfehler | Definiert wird für \hat{x} ∈ \widehat{M}; bitte prüfen. |
|      |      |      |                                                              |                                                              |             |                                                              |
|  |      |      |                                                              |                                                              |             |                                                              |
| 438 | 1206 | ● | `(Proposition~\ref{prop:d3-2.1} ).` | `(Proposition~\ref{prop:d3-2.1}).` | Abstand | Schon in der Arbeitsliste. Leerzeichen vor der Klammer. |

### Teil IV, Kap. 4 – Asymptotics on C*- and W*-Algebras (`part-d/chap-d4.tex`)

| S. | Z. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|---|
| 441 | 57 | ◐ | `\exp(\omega_{0} t) \in \rho(T(t)')` | `\exp(\omega_{0} t) \in \sigma(T(t)')` | Tippfehler | exp(ω₀t) ist nach Z. 52 Eigenwert von T(t)', liegt also nicht in der Resolventenmenge ρ; vermutlich σ bzw. Pσ gemeint, bitte prüfen. |
| 442 | 83 | ● | `\eu^{-\lambda t}T(s)\phi \ds` | `\eu^{-\lambda s}T(s)\phi \ds` | Tippfehler | Integrationsvariable gemischt (t im Exponenten, s im Integranden und Differential). |
| 442 | 90 | ◐ | `\eu^{\lambda t}\|T(s)\phi\| \ds` | `\eu^{-\lambda s}\|T(s)\phi\| \ds` | Tippfehler | Integrationsvariable gemischt wie Z. 83; außerdem fehlt das Minuszeichen im Exponenten (für λ > s(A) ist e^{-λs} gemeint), bitte prüfen. |
| 442 | 128 | ● | `C*-algebras` | `\CA-algebras` | Notation | Schon in der Arbeitsliste. Hier (und Z. 131 „C*-algebra“) normales Sternchen ohne Mathemodus statt \CA wie sonst im Kapitel. |
| 443 | 151 | ◐ | `by Theorem~\ref{thm:d4-1.3}` | `by Theorem~\ref{thm:d4-1.1}` | Verweis | Schon in der Arbeitsliste. Theorem 4.1.7 betrifft C*-Algebren mit Eins (Theorem 4.1.1), nicht Prädualräume (4.1.3). |
| 443 | 171 | ◐ | `hence $s(A) = 1$` | `hence $\omega_{0} = 0$` | Tippfehler | Aus ‖T(t)‖ = 1 folgt ω₀ = 0 (bzw. s(A) = 0), nicht s(A) = 1; bitte prüfen. |
| 443 | 182 | ● | `\UG(t)^{*}MU(t)` | `U(t)^{*}MU(t)` | Notation | \UG ist die Halbgruppe 𝒰; gemeint ist der Operator U(t) (vgl. Z. 186). |
| 444 | 223 | ○ | `(\xi \mapsto x(B\xi)+B^{*}(x\xi)): D(B) \to H` | `(\xi \mapsto x(B\xi)+B^{*}(x\xi))\colon D(B) \to H` | Abstand | Doppelpunkt bei Abbildungen als Relation gesetzt (zu viel Abstand davor); ebenso Z. 733 (`(S \mapsto S'): K \to`), Z. 878 (`\kappa_{t}: \N \to \N`). |
| 444 | 231 | ● | `\ie  $Ax = xB + B^{*}x$ for $ x \in D(A) $` | `\ie $Ax = xB + B^{*}x$ for $x \in D(A)$.` | Satzzeichen | Satzende-Punkt fehlt. |
| 444 | 271 | ● | `\vert(T(s)x)\xi\vert\eta) \ds` | `\abs{((T(s)x)\xi \,\vert\, \eta)} \ds` | Klammern | Öffnende Klammer des Skalarprodukts fehlt, Betrag/Trennstrich vermischt (vgl. Z. 342: `((T(s)x)\xi \,\vert\, \eta)`). |
| 444 | 327 | ● | `\int_{0}^{\infty}\|U(s)\|^2ds` | `\int_{0}^{\infty}\|U(s)\xi\|^2 \ds` | Tippfehler | ξ fehlt (vgl. Theorem 4.2.2 (g), Z. 268); außerdem kursives „ds“ statt \ds. |
| 446 | 367 | ● | `\frac{1}{s}\int_{0}^{s} T(t)dt` | `\frac{1}{s}\int_{0}^{s} T(t) \dt` | Notation | Kursives d und fehlender Abstand; sonst im Kapitel aufrechtes \dt (z. B. Z. 386, 473). |
| 446 | 389 | ◐ | `exists for every $x$ in $M$` | `exists for every $\phi$ in $M_{*}$` | Notation | 𝒯 wirkt auf M_* (Z. 381, Beweis mit Orbits T(t)φ); dann in Z. 386 entsprechend `T(t)\phi \dt`; bitte prüfen. |
| 446 | 401 | ○ | `(T(t)p_{n})^2 \leq T(t)p_{n}` | `(T(t)'p_{n})^2 \leq T(t)'p_{n}` | Notation | 𝒯 wirkt auf M_*, p_n ∈ M; sonst wird die Adjungierte mit Strich geschrieben (vgl. Z. 432 T(t)'p_r); ebenso Z. 407, 413, 418; bitte prüfen. |
| 447 | 463 | ◐ | `It follows as in (b) that` | `It follows as in (ii) that` | Verweis | Schon in der Arbeitsliste. Remark 4.3.2 hat nur die Teile (i)–(iii). |
| 447 | 473 | ○ | `(x \in M, 0 \leq s \in \R)` | `(x \in M, 0 < s \in \R)` | Tippfehler | Wegen 1/s muss s > 0 sein; bitte prüfen. |
| 448 | 522 | ● | `\mleft( C(s)'((\1-p_{r})x))(C(s)'((\1-p_{r})x)^{*} \mright)` | `C(s)'((\1-p_{r})x)\,\bigl(C(s)'((\1-p_{r})x)\bigr)^{*}` | Klammern | Klammern unausgeglichen: nach dem ersten Faktor eine Klammer zu viel, beim zweiten fehlt die schließende vor ^{*}; \mleft/\mright umschließen hier nichts Sinnvolles. |
| 448 | 539 | ◐ | `for $0 \neq x \in \Fix{\TT}$` | `for $0 \neq x \in \Fix{\TT'}$` | Notation | x ∈ M, vorher (Z. 533) x ∈ Fix(𝒯'); bitte prüfen. |
| 449 | 575 | ● | `$\Fix{T'}$` | `$\Fix{\TT'}$` | Notation | T' statt 𝒯' (sonst durchgehend \TT'); ebenso Z. 576 (`\Fix{T'} = \C.\1`). |
| 449 | 576 | ◐ | `\C.\1` | `\C \cdot \1` | Notation | Punkt auf Grundlinie statt \cdot; vgl. Z. 569 `\C \cdot \phi` (Z. 573 dagegen `\phi\C`). |
| 449 | 593 | ◐ | `(\TT)^{-} \subseteq L_{w}(M_{*})` | `\closure{\TT} \subseteq L_{w}(M_{*})` | Notation | Abschluss von 𝒯 uneinheitlich: (𝒯)^- hier, \closure{\TT} Z. 641, \overline{\TT} Z. 648, \TT^{-} Z. 730. |
| 450 | 641 | ● | `\mathcal{L}_{w}{(M_{*})}` | `L_{w}(M_{*})` | Notation | Sonst steht L_w(M_*) (Z. 593, 648, 730); hier kalligraphisches 𝓛. |
| 450 | 646 | ● | `\TT_{0}(t)' \coloneqq T(t)'_{\vert N}` | `T_{0}(t)' \coloneqq T(t)'_{\vert N}` | Notation | Einzeloperator, nicht Halbgruppe; später T_{0}(t)' (Z. 699, 726, 727). |
| 450 | 659 | ● | `(\lim_{\mathfrak{U}} \eu^{\eta})` | `(\lim_{\mathfrak{U}} \eu^{\eta t})` | Tippfehler | t im Exponenten fehlt (vgl. Z. 662). |
| 450 | 666 | ● | `\langle\psi,Q'(u_{n})\rangle` | `\langle\psi,Q'(u_{\eta})\rangle` | Tippfehler | Index n statt η (rechts u_η). |
| 450 | 668 | ● | `(\lim_{\mathfrak{U}} \eu^{\eta t})\langle\psi,u_{\eta}\rangle \langle\psi,u_{\eta}\rangle.` | `(\lim_{\mathfrak{U}} \eu^{\eta t})\langle\psi,u_{\eta}\rangle = \langle\psi,u_{\eta}\rangle.` | Tippfehler | Gleichheitszeichen fehlt zwischen den beiden Termen. |
| 450 | 677 | ◐ | `\overline{\langle S,\eta \rangle}` | `\overline{\langle S,\gamma \rangle}` | Notation | x_γ wird mit γ definiert (Z. 673, 676, 680), im Integranden steht η; Z. 682–687 dann x_η mit „η ∈ K“ (gemeint: η aus der dualen Gruppe von K); Bezeichnung bitte vereinheitlichen. |
| 450 | 695 | ● | `let $\UG$ be a family of unitary eigenvectors` | `let $U$ be a family of unitary eigenvectors` | Notation | Z. 696 heißt die Familie U (kursiv); \UG ist sonst die implementierende Halbgruppe 𝒰. |
| 450 | 699 | ○ | `\eu^{(n_{1}-n_{2})t}` | `\eu^{(\eta_{1}-\eta_{2})t}` | Notation | n_1, n_2 werden nicht eingeführt (Eigenwerte heißen sonst η ∈ Ω); ebenso Z. 707–708; bitte prüfen. |
| 451 | 733 | ● | `\mathcal{L}( (N,\sigma(N,N_{*}) )` | `\mathcal{L}(N,\sigma(N,N_{*}))` | Klammern | Drei öffnende, zwei schließende Klammern. |
| 451 | 740 | ○ | `\begin{enumerate}[\upshape(i), wide, labelindent=.25em]` | `\begin{enumerate}[\upshape(a), wide, labelindent=.25em]` | LaTeX | Innere Aufzählung in Remarks 4.3.6 (iv) nummeriert wieder (i)–(iii) wie die äußere; „as in (ii)“ in Z. 755 dadurch mehrdeutig. |
| 452 | 782 | ◐ | `\lim_{\mathfrak{U}} T(t) = P` | `\lim_{\mathfrak{U}} T(t)_{*} = P_{*}` | Notation | Sonst im Beweis T(t)_*, P_* (Z. 774, 781, 801); bitte prüfen. |
| 452 | 812 | ○ | `\{p_{i}: i \in A\}` | `\{p_{i} \colon i \in I\}` | Notation | Indexmenge A kollidiert mit dem Generator A (ebenso Z. 814 `i_{0} \in A`); außerdem „:“ statt \colon wie sonst in Mengenschreibweise, ebenso Z. 814, 924, 981, 1148, 1321. |
| 452 | 842 | ● | `\|(\phi_{t} - \phi_{0})\vert_{p \BH p} \| \leq \delta .` | `\|(\phi_{t} - \phi_{0})\vert_{p \BH p} \| \leq \delta` | Satzzeichen | Punkt in der abgesetzten Formel, der Satz geht mit „for all t ∈ U.“ weiter. |
| 453 | 871 | ◐ | `(Proposition~\ref{prop:d4-3.7})` | `(Theorem~\ref{thm:d4-3.5})` | Verweis | Schon in der Arbeitsliste. Die bedingte Erwartung stammt aus Theorem 4.3.5 (i). |
| 453 | 885 | ◐ | `m = \kappa_{t}\eta` | `m = \kappa_{t}n` | Tippfehler | κ_t : ℕ → ℕ wird auf n angewandt (δ_n ∘ S(t) = δ_m); η ist hier nicht definiert; bitte prüfen. |
| 453 | 890 | ● | `N = B(H_{n})` | `N = \mathcal{B}(H_{n})` | Notation | Sonst \BH = 𝓑(H) kalligraphisch. |
| 454 | 899 | ◐ | `\lim_{s \to \infty} T(s) = \1 \otimes \phi` | `\lim_{s \to \infty} T(s)_{*} = \1 \otimes \phi` | Notation | Konvergenz in 𝓛(𝓑(H)_*), also Prädualoperatoren (vgl. Prop. 4.3.7 (b)); ebenso Z. 902 `T_{*}` statt `\TT_{*}`; bitte prüfen. |
| 454 | 978 | ◐ | `\Re(\lambda) \leq \delta` | `\Re(\lambda) \leq -\delta` | Tippfehler | Mit δ > 0 wäre die Aussage trivial; gemeint ist eine Spektrallücke; bitte prüfen. |
| 454 | 983 | ● | `hence $ T_{\vert \Image{Q}} $` | `hence $ \TT_{\vert \Image{Q}} $` | Notation | Einschränkung der Halbgruppe, vgl. Z. 984 `\TT_{\vert \Image{Q}}`; außerdem `T(\tau)u_{\gamma}^{k}` evtl. `T(\tau)'u_{\gamma}^{k}` (u ∈ M), bitte prüfen. |
| 455 | 1014 | ● | `$ \beta \in \R $ :` | `$ \beta \in \R $:` | Abstand | Leerzeichen vor dem Doppelpunkt nach $…$. |
| 455 | 1017 | ● | `\|R(\eta + \im\beta A_{0})\| \leq c` | `\|R(\eta + \im\beta, A_{0})\| \leq c` | Tippfehler | Komma zwischen Argument und Operator der Resolvente fehlt. |
| 456 | 1084 | ● | `\Fix{ R_{1}' }` | `\Fix{\RR_{1}'}` | Notation | R_1 statt 𝓡_1 (vgl. Z. 1076). |
| 456 | 1097 | ● | `\rangle = \\` | `\rangle \\` | LaTeX | In aligned endet jede Zeile mit „=“ und die nächste beginnt mit „&=“: doppeltes Gleichheitszeichen im Druck; ebenso Z. 1098, 1099, 1100. |
| 456 | 1098 | ○ | `\langle\mu p_{n}p(R(\mu)p'x)p_{n},\phi_{n}\rangle` | `\langle\mu p_{n}p(R(\mu)'x)p\,p_{n},\phi_{n}\rangle` | Tippfehler | Strich an p statt an R(μ); vermutlich p_n = p_n p = p p_n eingeschoben; bitte prüfen. |
| 456 | 1101 | ◐ | `\phi_{n}(p_{n})^{-1}\phi_{n}(x) = \psi_{n}(x)` | `\phi_{n}(p_{n})^{-1}\phi_{n}(p_{n}xp_{n}) = \psi_{n}(x)` | Tippfehler | Widerspricht der Definition von ψ_n in Z. 1088; bitte prüfen. |
| 457 | 1114 | ○ | `by Lemma~\ref{lem:d3-1.2}` | `by Lemma~\ref{lem:d4-4.1}` | Verweis | Schon in der Arbeitsliste. Folge von Zuständen mit orthogonalen Trägern ist Lemma 4.4.1; bitte prüfen. |
| 457 | 1162 | ◐ | `a net $ (z_{n,\eta}) $  in $ \widehat{M}_{1}^{+} $` | `a net $ (\hat{z}_{n,\eta}) $  in $ \widehat{M}_{1}^{+} $` | Notation | Im folgenden (Z. 1165, 1168, 1169) heißt das Netz \hat{z}_{n,η}. |
| 457 | 1168 | ◐ | `(p\hat{z}_{n,\eta}\widehat{p})` | `(\widehat{p}\hat{z}_{n,\eta}\widehat{p})` | Tippfehler | Links p statt \widehat{p} (Rechnung in \widehat{M}); bitte prüfen. |
| 457 | 1182 | ● | `$ {M}_{\widehat{p}} = \widehat{M_{p}} $ )` | `$ {M}_{\widehat{p}} = \widehat{M_{p}} $)` | Abstand | Leerzeichen vor schließender Klammer nach $…$; ebenso Z. 1278 (zweimal: `\1 $ )`, `\R_{+} $ )`), Z. 1323 (`\psi_{i} $ )`). |
| 457 | 1186 | ○ | `\mu R(\mu)'\widehat{\psi}_{n} = \widehat{\psi}_{n}` | `\mu \widehat{R}(\mu)\widehat{\psi}_{n} = \widehat{\psi}_{n}` | Notation | ψ̂_n liegt im Prädual-Ultrapotenz-Raum, Strich (Adjungierte) passt nicht; vgl. Z. 1198 ohne Strich; bitte prüfen. |
| 457 | 1208 | ◐ | `\lim_{n} \phi_{n}(z_{n}) = 0` | `\lim_{n} \phi(z_{n}) = 0` | Tippfehler | Widerspricht (iii'') φ_n(z_n) ≥ 1/2; gemeint ist der treue Zustand φ (vgl. (i') Z. 1195 und Z. 1217); bitte prüfen. |
| 457 | 1218 | ◐ | `Therefore condition~\ref{item:d4-4.3-iip} implies` | `Therefore condition (i$''$) implies` | Verweis | Die s*-Konvergenz z_n → 0 folgt aus φ(z_n) → 0 und der Treue von φ, also aus (i''), nicht (ii''); ebenso Z. 1225; bitte prüfen (für (i'') fehlt ein \label). |
| 459 | 1278 | ○ | `R''\1 = R\1 = \1` | `\mu R''(\mu)\1 = \mu R(\mu)\1 = \1` | Notation | R ohne Argument μ, sonst stets μR(μ); bitte prüfen. |
| 459 | 1280 | ◐ | `satisfying (i)--(ii) of Lemma~\ref{lem:d4-4.3}` | `satisfying (i)--(iii) of Lemma~\ref{lem:d4-4.3}` | Verweis | Lemma 4.4.3 hat drei Teile; im Folgenden wird auch (iii) φ_k(z_k) ≥ 1/2 gebraucht; bitte prüfen. |
| 459 | 1305 | ● | `the fixed space of\/ $ R' $` | `the fixed space of\/ $ \RR' $` | Notation | R' statt 𝓡' (vgl. Z. 1306). |
| 459 | 1314 | ○ | `\dim(\Fix{\RR'})` | `\dim \Fix{\RR'}` | Notation | Uneinheitlich mit/ohne Klammern um Fix(…): ohne Z. 1258, 1302, 1311, 1399; mit Z. 1314, 1320, 1334, 1364. |
| 461 | 1367 | ● | `\phi_{1},\ldots,\phi_{n}` | `\phi_{1},\ldots,\phi_{k}` | Tippfehler | Laufindex bis k (vgl. x_1, …, x_k und Z. 1370, 1376). |
| 461 | 1376 | ○ | `P = \sum_{i=1}^{k} \phi_{i} \otimes x_{i}` | `P = \sum_{i=1}^{k} x_{i} \otimes \phi_{i}` | Notation | In Z. 577 ist P = 𝟏 ⊗ φ mit Pψ = ψ(𝟏)φ, also erst Element von M, dann von M_*; bitte prüfen. |
| 461 | 1383 | ◐ | `\sum_{i=1}^{k} \phi_{i}(\psi)x_{i} \in M_{*}` | `\sum_{i=1}^{k} \psi(x_{i})\phi_{i} \in M_{*}` | Tippfehler | Argumente vertauscht: φ_i ∈ M_* kann nicht auf ψ ∈ M' angewandt werden, und das Ergebnis soll in M_* liegen; bitte prüfen. |

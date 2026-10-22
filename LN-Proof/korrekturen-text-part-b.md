# Fahnenkorrektur (Text): Teil II (Part B)

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184), Proof-PDF vom 14.10.2026.

Auszug aus `Fahnenkorrektur_Springer_LNM1184.md`. **Seitenangaben** = gedruckte Seitenzahl (PDF-Seite = gedruckte Seite + 18). **Sicherheit:** ● hoch · ◐ mittel · ○ niedrig.

**Stand 21.10.2026 (Branch `fahnenkorrektur`):** **Kap. 1, 2 und 3 sind erledigt** (Kap. 3 nach Freigabe durch Günther Greiner), ebenso die Updated Notes. In Kap. 4 sind alle ●-Punkte umgesetzt; die von Frank Neubrander geprüften Seiten sind komplett umgesetzt (Teil I, Kap. 4 und Updated Notes S. 468–471; Teil II, S. 231–235; Teil III, S. 369–376; Freigabe 22.10.2026); sonst sind ◐ und ○ in Kap. 4 offen, außer wo im Kommentar „Umgesetzt“ steht (einige über die Formellisten, Stand 20.10.2026). Abweichungen vom Soll stehen im Kommentar der jeweiligen Zeile.

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

Insgesamt **120 Punkte**: 36 ●, 56 ◐, 28 ○; davon umgesetzt: 83, teilweise: 1.


Übergreifende Punkte (Inhaltsverzeichnis, Kolumnentitel, Schreibweisen) und der Index stehen in `korrekturen-text-allgemein.md`.

### Teil II, Kap. 1 – Basic Results on Spaces C₀(X)

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 137 | ○ | Basic Results of Spaces 𝐶0(𝑋) | Basic Results on Spaces 𝐶0(𝑋) | Grammatik | **Umgesetzt.** Präposition; betrifft auch den Kolumnentitel. |
| 137 | ○ | 1.1 Algebraic and Order-Structure: Ideals and Quotients | 1.1 Algebraic and Order Structure: Ideals and Quotients | Satz | **Umgesetzt.** |
| 139 | ● | This identification is a topological isomorphisms with respect to the weak*-topology | This identification is a topological isomorphism with respect to the weak* topology | Tippfehler | **Umgesetzt.**  |
| 139 | ● | (i) positive (notation: 𝑇 ⩾ 0) if 𝑇 𝑓 is a positive whenever 𝑓 is positive, | if 𝑇𝑓 is positive whenever 𝑓 is positive, | Tippfehler | **Umgesetzt.**  |
| 139 | ◐ | (iii) Markov-operator if 𝑋 and 𝑌 are compact | (iii) Markov operator if 𝑋 and 𝑌 are compact | Konsistenz | **Umgesetzt.** Auf S. 140 'Markov operator' ohne Bindestrich. |

### Teil II, Kap. 2 – Characterization of Positive Semigroups on C₀(X)

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 142 | ◐ | similar to a derivation perturbated by a multiplication operator | similar to a derivation perturbed by a multiplication operator | Tippfehler | **Umgesetzt.** |
| 143 | ● | It will be essential that K is compact for all what follows | It will be essential that K is compact for all that follows | Grammatik | **Umgesetzt.**  |
| 146 | ◐ | is not positive (see Greiner et al. [16] ). | is not positive (see Greiner et al. [16]). | Satz | **Umgesetzt.** Leerzeichen vor schließender Klammer |
| 148 | ● | The next result is a strengthened form of Theorem 1.6. | The next result is a strengthened form of Theorem 2.1.6. | Querverweis | **Umgesetzt.** Nicht verlinkter Altverweis; gemeint ist Theorem 2.1.6 (S. 144) |
| 148 | ◐ | Thus (P) is not a "metric" condition | Thus (P) is not a “metric” condition | Satz | **Umgesetzt.** Gerade statt typografische Anführungszeichen (sonst “...” verwendet) |
| 150 | ◐ | then by Part-I, Section 1.3.2, the operator m · A = ∥m∥∞ B also generates a positive semigroup). | ... also generates a positive semigroup. | Satz | **Umgesetzt.** Schließende Klammer ohne öffnende (Satz geht auf S. 151 weiter) |
| 152 | ● | preceding page succesively to B = m^{1/k} · A | preceding page successively to ... | Tippfehler | **Umgesetzt.**  |
| 154 | ● | Then A is the generator of positive semigroup. | Then A is the generator of a positive semigroup. | Grammatik | **Umgesetzt.**  |
| 155 | ◐ | A semigroup (T(t))t⩾0 is called lattice semigroup if | A semigroup (T(t))t⩾0 is called a lattice semigroup if | Grammatik | **Umgesetzt.** |
| 155 | ◐ | a concrete representation of lattice-semigroups | a concrete representation of lattice semigroups | Konsistenz | **Umgesetzt.** Sonst durchgehend ohne Bindestrich |
| 156 | ◐ | right-sided Gateaux-differentiable at every point f ∈ G (vs. 'right-sided Gateaux differentiable' im selben Absatz) | einheitlich 'Gateaux differentiable' (bzw. ggf. 'Gâteaux') | Konsistenz | **Umgesetzt.** Einheitlich „Gateaux differentiable“. Auf S. 155/156 gemischt mit und ohne Bindestrich (auch in Prop. 2.2.3) |
| 159 | ○ | For A = Δ (the Laplacian) this is a version of the classical Kato’s inequality. | ... this is a version of the classical Kato inequality. | Grammatik | **Umgesetzt.** |
| 160 | ◐ | Remark Although we assume that (T(t))t⩾0 is a real semigroup, i.e., T(t)C(K,R) ⊆ C(K,R) for all t ⩾ 0. It is important for the proof | ... for all t ⩾ 0, it is important for the proof | Grammatik | **Umgesetzt.** Nebensatz mit 'Although' als eigener Satz abgetrennt |
| 161 | ● | hence T(t) is so as well (cf. Remark 2.1). | hence T(t) is so as well (cf. Remark 2.2.1). | Querverweis | **Umgesetzt.** Remark 2.1 existiert nicht; gemeint Remark 2.2.1 (S. 155) |
| 161 | ● | we denote by dφ he linear form on C[−1, 0] | we denote by dφ the linear form on C[−1, 0] | Tippfehler | **Umgesetzt.**  |
| 161 | ◐ | The operator Amax on the (real or complex space) C[−1, 0] | The operator Amax on the (real or complex) space C[−1, 0] | Grammatik | **Umgesetzt.** |
| 162 | ◐ | Let A on (the real or complex) space C[−1, 0] be given by | Let A on the (real or complex) space C[−1, 0] be given by | Grammatik | **Umgesetzt.** |
| 162 | ◐ | A satisfies Kato’s Equality Eq. (2.2.9) | A satisfies Kato’s equality Eq. (2.2.9) | Konsistenz | **Umgesetzt.** Sonst 'Kato’s equality' klein |
| 163 | ● | this will enable us, to give a detailed description | this will enable us to give a detailed description | Satz | **Umgesetzt.**  |
| 163 | ◐ | A mapping φ : [0, ∞) × K → K is called semiflow if | ... is called a semiflow if | Grammatik | **Umgesetzt.** |
| 163 | ○ | the space of all real valued continuous functions on K | the space of all real-valued continuous functions on K | Konsistenz | **Umgesetzt.** Sonst 'real-valued' |
| 164 | ◐ | An operator δ on C(K) is called derivation if | An operator δ on C(K) is called a derivation if | Grammatik | **Umgesetzt.** |
| 166 | ◐ | Theorem 2.3.6 An operator A is generator of a lattice semigroup | An operator A is the generator of a lattice semigroup | Grammatik | **Umgesetzt.** |
| 166 | ○ | In fact, by Eq. (2.1.6) T0(t)f = lim e^{−t/n·h} · T(t/n)f | Verweis prüfen (Eq. (2.1.6) ist φx ∈ dpu(f); gemeint vermutlich die Trotter-Produktformel aus Part I) | Querverweis | **Umgesetzt.** Gemeint ist die Trotter-Produktformel; jetzt „Part-I, Eq.“ (eq:a2-1.8). |
| 167 | ● | is closable (by Corollary 2.1.11 ); but | is closable (by Corollary 2.1.11); but | Satz | **Umgesetzt.** Im PDF bestätigt |
| 169 | ◐ | Given a compact neighbourhood V of x0 | neighbourhood/neighborhood vereinheitlichen | Konsistenz | **Umgesetzt.** Überall „neighborhood“ (amerikanisch, wie „behavior“). S. 169, 179: neighbourhood; S. 180 (3x): neighborhood; außerdem 'behavior' (S. 187) amerikanisch |
| 174 | ◐ | by Part I, Proposition 1.1.9 (or Part I, Corollary 2.1.33) | by Part-I, Proposition 1.1.9 (or Part-I, Corollary 2.1.33) | Konsistenz | **Umgesetzt.** Im Fließtext sonst durchgehend „Part-I“ mit Bindestrich, siehe Merkposten A.4. |
| 178 | ◐ | This does no longer hold for functions which are not admissible | This no longer holds for functions which are not admissible | Grammatik | **Umgesetzt.** |
| 179 | ● | is closed in (a, b) Thus (a, b) ∖ K is the union | is closed in (a, b). Thus (a, b) ∖ K is the union | Satz | **Umgesetzt.** Punkt fehlt, im PDF bestätigt |
| 179 | ◐ | Thus αn is strictly monotonous. | Thus αn is strictly monotone. | Tippfehler | **Umgesetzt.** 'monotonous' = eintönig; mathematisch 'monotone'/'monotonic' |
| 183 | ● | It is easy to verify, that the generator of this group is | It is easy to verify that the generator of this group is | Satz | **Umgesetzt.**  |
| 183 | ◐ | The operator δ̃m is generator of an automorphism group on C[a, b] | The operator δ̃m is the generator of an automorphism group | Grammatik | **Umgesetzt.** |
| 184 | ● | we refer to the corresponding notes in Part-III, Chapter 2, Theorem 2.1.6 and 2.1.8 are due to Arendt et al. [4] | ... in Part-III, Chapter 2. Theorems 2.1.6 and 2.1.8 are due to Arendt et al. [4] | Satz | **Umgesetzt.** Komma statt Punkt; außerdem Plural 'Theorems' |
| 184 | ● | Infinite-dimensional Systems, Retahof 1983. | Infinite-dimensional Systems, Retzhof 1983. | Literatur | **Umgesetzt.** Tagungsort Retzhof (LNM 1076) |
| 184 | ◐ | as perturbation of a derivation (Theorem 2.3.5 and 2.3.6) | (Theorems 2.3.5 and 2.3.6) | Grammatik | **Umgesetzt.** |
| 184 | ◐ | positive groups on C0(X) (Theorem 2.3.14 ) was obtained | (Theorem 2.3.14) was obtained | Satz | **Umgesetzt.** |
| 184 | ◐ | to satisfy the "generalized Osgood condition" | to satisfy the “generalized Osgood condition” | Satz | **Umgesetzt.** Gerade Anführungszeichen |
| 184 | ◐ | Uhlig [30] determined all semi-flows on an interval. | Uhlig [30] determined all semiflows on an interval. | Konsistenz | **Umgesetzt.** Im Kapitel sonst 'semiflow' |
| 184 | ◐ | has been obtained by Kurose in a series of papers Kurose [21, 22, 23]. | has been obtained by Kurose in a series of papers [21, 22, 23]. | Grammatik | **Umgesetzt.** `\cite` statt `\textcite`. Name doppelt |
| 184 | ○ | (see Part-III, Section 2.5), for general Banach spaces and C0(X) in particular the problem has been considered | (see Part-III, Section 2.5); for general Banach spaces ... | Satz | **Umgesetzt.** |
| 184 | ○ | Our approach is inspired by Laubenfels [24] | Our approach is inspired by de Laubenfels [24] | Konsistenz | **Umgesetzt.** Als „de Laubenfels~\cite{…}“, weil biblatex das „de“ im Zitat weglässt. Im Literaturverzeichnis 'R. de Laubenfels' |
| 184 | ○ | In the sequel of Batty’s work (loc.cit.) | (loc. cit.) | Satz | **Umgesetzt.** |
| 184 | ○ | [2] W. Arendt: “Generators of positive semigroups”. ... Vol. 1076. Springer 1984 pp. 1–15. / [30] H. Uhlig: “Derivationen und Verbandshalbgruppen”. | Titel ohne Anführungszeichen, Jahr in Klammern wie bei den übrigen Einträgen (z. B. Lecture Notes in Math. 1076, Springer (1984) 1–15) | Literatur | **Umgesetzt.** Anführungszeichen und Jahresformat kommen aus dem biblatex-Stil (alle Sammelband- und Thesis-Einträge), nicht geändert. Reihe „Lecture Notes in Math.“ bei arendt:1984a ergänzt. Formatierung uneinheitlich |
| 185 | ● | [11] P. Collatz: Einschließungssatz für die charakteristischen Zahlen von Matrizen. | [11] L. Collatz: Einschließungssatz ... | Literatur | **Umgesetzt.** Lothar Collatz |
| 185 | ◐ | [16] G. Greiner, J. Voigt & M. Wolff: ... J. Operator Theory (1981) 245–256. | J. Operator Theory 5 (1981) 245–256. | Literatur | **Umgesetzt.** Bandangabe fehlt |
| 185 | ◐ | [24] R. de Laubenfels: Well behaved derivation on C[0,1]. | R. de Laubenfels: Well-behaved derivations on C[0,1]. | Literatur | **Umgesetzt.** |
| 185 | ○ | [19] E. Kamke: Über die partielle Differentialgleichung. Math. Z. 41 (1932) 56–66. | Titel/Angaben prüfen (Titel wirkt unvollständig) | Literatur | **Umgesetzt.** Schon am 18.10. korrigiert (Jahr 1936, Titel vollständig). |
| 185 | ○ | [20] T. Kato: Schrödinger operators with singular potentials. Israel J. Math. 13 (1973) 135–148. | Israel J. Math. 13 (1972) 135–148 | Literatur | **Umgesetzt.** Bei der Bib-Bereinigung (18.10.) bewusst belassen. Band 13 erschien 1972 – bitte prüfen |
| 186 | ○ | [27] G. Lumer: Problème de Cauchy pour opérateurs locaux et “changement de temps”. Ann. Inst. Fourier (Grenoble) 23 (1974) 409–466. | Ann. Inst. Fourier (Grenoble) 25 (1975) 409–446 | Literatur | **Umgesetzt.** Bib seit 18.10. richtig; die Fahne beruht auf dem alten Stand. Band/Jahr/Seiten wohl aus [26] übernommen – bitte prüfen; [26] ist Bd. 23 (1973) |

### Teil II, Kap. 3 – Spectral Theory of Positive Semigroups on C₀(X)

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 187 | ◐ | Krein, Krasnoselski’i, Lotz | Krein, Krasnosel’skii, Lotz | Tippfehler | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 187 | ◐ | (see Chapt.V of Schaefer [27]) ... (Schaefer [27, V.Proposition 4.1]) | (see Chap. V of Schaefer [27]) ... (Schaefer [27, V, Proposition 4.1]) | Satz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). Leerzeichen fehlen; Abkürzung uneinheitlich (Chapt./Chap./Chapter, vgl. S. 150 'Chapter I', S. 209 'Chap.I') |
| 188 | ○ | We may assume λ0 > ω0(A) then R(λ0, A) ⩾ 0, and iterating | We may assume λ0 > ω0(A); then R(λ0, A) ⩾ 0, and iterating | Satz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 192 | ○ | equation Eq. (3.1.16) implies that | Eq. (3.1.16) implies that | Satz | **Umgesetzt** (20.10.2026, über `korrekturen-mathe-part-b`, Freigabe G. Greiner). Doppelung 'equation Eq.' |
| 202 | ● | A real spectral value λ0 of a generator A is called a dominant provided that | ... is called dominant provided that | Grammatik | **Umgesetzt.**  |
| 204 | ● | unless φ = r0δ0 for some r0 ∈ R.) | unless φ = r0δ0 for some r0 ∈ R. | Satz | **Umgesetzt.** Schließende Klammer ohne öffnende, im PDF bestätigt |
| 204 | ◐ | It follows from Eq. (3.2.25) and Eq. (3.2.26) that for λ > ∥φ∥, the resolvent R(λ, Aφ) exists | It follows from Eq. (3.2.27) and Eq. (3.2.28) that ... | Querverweis | **Umgesetzt** (20.10.2026, über `korrekturen-mathe-part-b`, Freigabe G. Greiner). Die Abschätzung folgt aus (3.2.27)/(3.2.28), nicht aus (3.2.25)/(3.2.26) |
| 205 | ◐ | hence it maps the unit ball in an order interval | hence it maps the unit ball into an order interval | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 206 | ◐ | can be extended to systems of functional differential equations even the infinite dimensional case. | ... functional differential equations, even to the infinite-dimensional case. | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). Wort fehlt |
| 206 | ◐ | Then the ideal I generated by {T(t)f : t ⩾ 0} satisfy T ≠ {0} | Then the ideal I generated by {T(t)f : t ⩾ 0} satisfies I ≠ {0} | Grammatik | **Umgesetzt** (20.10.2026, über `korrekturen-mathe-part-b`, Freigabe G. Greiner). Verbform; zudem T statt I (auch in der Folgezeile) |
| 207 | ◐ | (e) =⇒ (f): If I is a R(λ, A)-invariant ideal | (e) =⇒ (d): If I is an R(λ, A)-invariant ideal | Querverweis | **Umgesetzt** (21.10.2026, Freigabe G. Greiner): jetzt auch „an R(λ, A)-invariant ideal“. **Teilweise umgesetzt** (20.10.2026, über `korrekturen-mathe-part-b`, Freigabe G. Greiner): Verweis jetzt (e) ⇒ (d); „a R(λ, A)“ → „an“ offen. Beweiskette a⇒b⇒c⇒f⇒e⇒d⇒a; '(e) ⇒ (f)' doppelt bzw. falsch |
| 207 | ○ | The rotation semigroup (see Part-I, Example 1.2.5) | Verweis vereinheitlichen (S. 190, 197, 202: 'Part-I, Example 3.5.6') | Konsistenz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner): S. 207 und S. 212 verweisen jetzt auf Part-I, Example 3.5.6 (`ex:a3-5.6`); vorher stand dort ein Abschnittslabel. Auch S. 212 'Part-I, Example 1.2.5'; einer der Verweise ist vermutlich falsch |
| 209 | ◐ | (iv) If ker(s(A) − A′) contains a positive element (e.g., if X is compact (cf. Theorem 3.1.6), then | (e.g., if X is compact (cf. Theorem 3.1.6)), then | Satz | **Umgesetzt** (20.10.2026, über `korrekturen-mathe-part-b`, Freigabe G. Greiner). Klammer nicht geschlossen |
| 209 | ◐ | Protter & Weinberger [20, Chap.I, Theorem 3] | Protter & Weinberger [20, Chap. I, Theorem 3] | Satz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 210 | ○ | a φ ⩾ 0 satisfying A′φ = 0 always exists (see Theorem 3.1.6) | ... always exists (see Theorem 3.1.6). | Satz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). Satzpunkt fehlt |
| 210 | ○ | (i) Pσ(A) ∩ iR is a (additive) subgroup of iR. | (i) Pσ(A) ∩ iR is an (additive) subgroup of iR. | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 212 | ● | such that Pσ(A) = H). Here (H_d)ˆ denotes | such that Pσ(A) = H. Here (H_d)ˆ denotes | Satz | **Umgesetzt.** Überzählige Klammer, im PDF bestätigt |
| 212 | ◐ | For details see Greiner [15, p.62]. | For details see Greiner [15, p. 62]. | Satz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 215 | ● | A complete proof of this results requires | A complete proof of this result requires | Grammatik | **Umgesetzt.**  |
| 216 | ◐ | described explicitly by a semi-flow φ (S. 216); semi-flows associated with ordinary differential equations (S. 222); dagegen sonst durchgehend 'semiflow' | semiflow / semiflows (einheitlich) | Konsistenz | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). auch S. 226 'construct semi-flows associated with (T(t))' |
| 218 | ◐ | it is enough to prove assertion (i), (ii) and (iii) respectively | it is enough to prove assertions (i), (ii) and (iii) respectively | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 219 | ◐ | (i) By the definition given in Eq. (3.4.1) on page 216 there exists a τ > 0 such that c_t(h,φ) ⩾ ... | (i) By the definition given in Eq. (3.4.4) on page 217 ... | Querverweis | **Umgesetzt** (20.10.2026, über `korrekturen-mathe-part-b`, Freigabe G. Greiner). c(h,φ) ist in (3.4.4) definiert, nicht in (3.4.1) |
| 220 | ● | by Part-I, Proposition 3.6.2 Since every boundary point | by Part-I, Proposition 3.6.2. Since every boundary point | Satz | **Umgesetzt.** Punkt fehlt |
| 220 | ◐ | there is a x_f ∈ K such that | there is an x_f ∈ K such that | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 221 | ● | by Lemma 3.4.2 (b) there exists y ∈ K∞ | by Lemma 3.4.2 (ii) there exists y ∈ K∞ | Querverweis | **Umgesetzt.** Lemma 3.4.2 hat Teile (i)-(iii), kein (b) |
| 221 | ● | For details see Sect.18.2 of Dieudonné [11]. | For details see Section 18.2 of Dieudonné [11]. | Satz | **Umgesetzt.** Leerzeichen fehlt; sonst wird 'Section' ausgeschrieben (im PDF geprüft) |
| 221 | ◐ | φ0 and φ̃0 satisfy condition Theorem 3.4.4 (iii). | φ0 and φ̃0 satisfy condition (iii) of Theorem 3.4.4. | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 222 | ● | (iii) We consider Ω as in (b) and assume | (iii) We consider Ω as in (ii) and assume | Querverweis | **Umgesetzt.** Teile des Beispiels 3.4.6 sind (i)-(iii) nummeriert |
| 222 | ● | by remarking that the ideas of (b) and (c) can be combined | by remarking that the ideas of (ii) and (iii) can be combined | Querverweis | **Umgesetzt.**  |
| 225 | ◐ | for every x ∈ K there exists a r = r_x with | for every x ∈ K there exists an r = r_x with | Grammatik | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). |
| 227 | ● | The dichotomy stated in (Eq.(3.2.19) on page 202) is probably | The dichotomy stated in Eq. (3.2.19) on page 202 is probably | Satz | **Umgesetzt.** Leerzeichen fehlt, überflüssige Klammern (im PDF geprüft) |
| 227 | ○ | introduced by Derndinger [8] (and Schaefer (1980) respectively) | Zitat im Literaturformat, z. B. 'Schaefer [n]', oder Eintrag ergänzen | Literatur | **Umgesetzt** (G. Greiner, 21.10.2026): „(and Schaefer (1980) respectively)“ ersatzlos gestrichen. Schaefer (1980) steht nicht im Literaturverzeichnis des Kapitels |
| 228 | ◐ | [3] J.-M. Bony, P. Courrège & P. Priouret: Semi-groups de Feller sur une variété à bord compact | Semi-groupes de Feller sur une variété à bord compact | Literatur | **Umgesetzt** (21.10.2026, Freigabe G. Greiner; wie vorgeschlagen). französischer Originaltitel |
| 229 | ● | [22] J. P. Roth: “Les operateurs elliptiques comme générateurs infinitésimaux de semigroups de Feller”. Séminaire de Théorie du Potential | “Les opérateurs elliptiques comme générateurs infinitésimaux de semi-groupes de Feller”. Séminaire de Théorie du Potentiel | Literatur | **Umgesetzt.** Akzent fehlt, 'semigroups' englisch, 'Potential' statt 'Potentiel' |
| 229 | ◐ | [28] H. H. Schaefer: “Some recent results on positive groups and semi-groups. Proceedings of the Symposium in Honour of A.C. Zaanen”. From A to Z. ... Vol. 149. Mathematical Centre 1982 | “Some recent results on positive groups and semi-groups”. From A to Z: Proceedings of a Symposium in Honour of A.C. Zaanen. Ed. by ... Mathematical Centre Tracts 149. Mathematisch Centrum, Amsterdam (1982) pp. 69–79. | Literatur | **Umgesetzt** (21.10.2026, Freigabe G. Greiner): Bib-Eintrag `schaefer:1982`: Tagungsangabe als `booksubtitle`, Reihe „Mathematical Centre Tracts“ Nr. 149, Mathematisch Centrum, Amsterdam. Tagungsbandtitel steckt im Aufsatztitel; Reihe fehlt |
| 229 | ○ | [18] K. Kuhn: ... Semesterbericht Funktionalanalysis. 1984 pp. 125–142. | Semesterbericht Funktionalanalysis. Universität Tübingen, 1984 pp. 125–142. | Literatur | **Umgesetzt** (21.10.2026, Freigabe G. Greiner): Bib-Eintrag `kuhn:1984` als Techreport mit „Universität Tübingen“ (wie `greiner:1985`). im Literaturverzeichnis von Kap. 4 (Greiner [13]) mit 'Universität Tübingen' |

### Teil II, Kap. 4 – Asymptotics of Positive Semigroups on C₀(X)

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 232 | ◐ | Proof. Eq. (4.1.2) follows directly from Section 3.4.1 and the results from Chapter 2 | vermutlich: Theorem 3.4.1 (oder ein anderer gemeinter Verweis) | Querverweis | **Umgesetzt** (22.10.2026, Freigabe F. Neubrander): Gemeint ist Part-I, Section 3.4.1 (Spectrum of the adjoint semigroup); „Part-I,“ ergänzt. Einen Abschnitt 3.4.1 gibt es nicht |
| 233 | ○ | Γ\{1} is a homoclinic orbit i.e., | Γ\{1} is a homoclinic orbit, i.e., | Satz | **Umgesetzt** (22.10.2026, Freigabe F. Neubrander; wie vorgeschlagen). |
| 234 | ◐ | (2) Assume, that T(t)f = e^{iαt}f | (2) Assume that T(t)f = e^{iαt}f | Grammatik | **Umgesetzt** (22.10.2026, Freigabe F. Neubrander; wie vorgeschlagen). kein Komma vor 'that' |
| 234 | ◐ | (T(t)f)(z) → 0 μ-a.e.. Lebesgue’s | (T(t)f)(z) → 0 μ-a.e. Lebesgue’s | Satz | **Bereits erledigt** (21.10.2026, globale Korrektur „a.e..“). doppelter Punkt |
| 235 | ○ | (see Schaefer [29, II.Theorem 5.9]) | (see Schaefer [29, II. Theorem 5.9]) | Satz | **Umgesetzt** (22.10.2026, Freigabe F. Neubrander; wie vorgeschlagen). vgl. S. 240 'II. Proposition 9.4' |
| 236 | ○ | (see Asimow & Ellis [1], p.39) | (see Asimow & Ellis [1], p. 39) | Satz |  |
| 240 | ● | is a countable additive set function | is a countably additive set function | Grammatik | **Umgesetzt.**  |
| 240 | ○ | (see e.g., Schaefer [29, II. Proposition 9.4 ]) | (see e.g., Schaefer [29, II. Proposition 9.4]) | Satz | Leerzeichen vor schließender Klammer |
| 242 | ● | Then ω_ess(T) < 0 by Eq. (3.3.10) on page 85). | Then ω_ess(T) < 0 by Eq. (3.3.10) on page 85. | Satz | **Umgesetzt.** überzählige schließende Klammer |
| 245 | ◐ | the asymptotic behavior as t → ∞ of certain semigroups if only its generator is known | ... of certain semigroups if only their generator is known | Grammatik |  |
| 251 | ● | as developed in Part-I, Section 4.1, Section 4.1 | as developed in Part-I, Section 4.1. | Tippfehler | **Umgesetzt, abweichend:** „Part-I, Section 4.1, Section 4.1 and Part-III, Section 4.1“ (gemeint sind die Abschnitte 4.1 aus Teil I, II und III; Labels `sec:a4-1`, `sec:b4-1`, `sec:c4-1`). Verweis doppelt, Satzpunkt fehlt |
| 251 | ◐ | Again we use the assertion that dim F < ∞ | Again we use the assumption that dim F < ∞ | Tippfehler |  |
| 251 | ◐ | by the Theorem of Arzela-Ascoli | by the Theorem of Arzelà–Ascoli | Tippfehler |  |
| 252 | ○ | Proof. By Formula Eq. (4.3.2) on page 248 | Proof. By Eq. (4.3.2) on page 248 | Satz | ebenso S. 258: 'see Formula Eq. (4.3.3)' |
| 253 | ● | then σ(A) = ∅ by Proposition 3.4. | then σ(A) = ∅ by Proposition 4.3.4. | Querverweis | **Umgesetzt.**  |
| 253 | ◐ | by Part-III, Theorem 3.1.1. (i), we obtain | by Part-III, Theorem 3.1.1 (i), we obtain | Satz |  |
| 256 | ○ | since, even a scalar valued delay differential equation may be stable | since even a scalar-valued delay differential equation may be stable | Satz |  |
| 257 | ● | Then (3.11) takes the abstract form | Then Eq. (4.3.10) takes the abstract form | Querverweis | **Umgesetzt, abweichend:** „Then the problem in Example 4.3.11 takes …“ (das Label zeigt nur auf die Randbedingung; gemeint ist das ganze System des Beispiels). Alter Gleichungsverweis '(3.11)'; gemeint ist die Gleichung aus Example 4.3.11 (bitte Nummer prüfen) |
| 257 | ○ | It is well-known that B̃ generates | It is well known that B̃ generates | Konsistenz | sonst 'well known' (S. 247, 259) |
| 259 | ● | showed the translation property (T)for the solution semigroup | showed the translation property (T) for the solution semigroup | Satz | **Umgesetzt.** im PDF geprüft |
| 259 | ● | (see Part-III, Section 3.4 can be used to derive | (see Part-III, Section 3.4) can be used to derive | Satz | **Umgesetzt.** schließende Klammer fehlt |
| 259 | ◐ | Section 2: ... Theorem 4.1.1 seems to be folklore. | Theorem 4.2.1 seems to be folklore. | Querverweis | In den Notizen zu Abschnitt 2 ist wohl Theorem 4.2.1 (eventuell kompakte Halbgruppen) gemeint; 4.1.1 wird schon in Section 1 genannt |
| 259 | ◐ | This relation more detailed than in Example 4.2.6, can be found | This relation, in more detail than in Example 4.2.6, can be found | Grammatik |  |
| 259 | ○ | in Chapter 2 of Casteren [3] | in Chapter 2 of van Casteren [3] | Literatur | Literatureintrag lautet 'J. van Casteren'; ebenso S. 241 |

### Updated Notes, Part II

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 474 | ● | As examples for the rich litterature we mention | the rich literature | Tippfehler | **Umgesetzt.**  |
| 474 | ◐ | by the work of I. Mezic [36] in the context of numerical problems using the dynamical mode decomposition | I. Mezić [36] ... dynamic mode decomposition | Konsistenz | **Umgesetzt.** Im Literaturverzeichnis 'Mezić'; der übliche Fachbegriff lautet 'dynamic mode decomposition' |
| 475 | ● | persistent irreducibilty implies that the generator | persistent irreducibility | Tippfehler | **Umgesetzt.**  |
| 475 | ● | In Gerlach [21] strong convergence of Feller semigoups is studied. | Feller semigroups | Tippfehler | **Umgesetzt.**  |
| 475 | ○ | whose positive cone has non empty interior | non-empty interior | Konsistenz | **Umgesetzt.** sonst 'non-empty' |
| 477 | ◐ | [29] N. Jacob: Pseudo Differential Operators and Markov Processes. Vol. 1: ... [30] N. Jacob: Pseudo Differential Operators and Markov Processes. Vol III: | Pseudo-Differential Operators and Markov Processes. Vol. I: ... / Vol. III: | Literatur | **Umgesetzt.** Uneinheitlich gegenüber [28] 'Pseudo-Differential ... Vol. II'; Punkt nach 'Vol' fehlt bei [30] |

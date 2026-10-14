# Umgesetzte Korrekturen: *One-parameter Semigroups of Positive Operators* (2. Aufl.)

Springer LNM 1184, Fahnenkorrektur zum Proof-PDF vom 14.10.2026. Stand: 14.10.2026.

Die Seitenangaben beziehen sich auf die gedruckten Buchseiten (PDF-Seite = Buchseite + 18).

## Überblick

- Umgesetzt sind alle **122 Punkte mit hoher Sicherheit (●)** aus der Arbeitsliste `Fahnenkorrektur_Springer_LNM1184.md`, in den TeX- und Bib-Dateien unter `LN-Book-Springer`.
- Die Punkte mit mittlerer (◐) und niedriger (○) Sicherheit sind **noch offen**.
- **Merkposten A.4 („Part-I“):** Variante 1 umgesetzt. Die zwei Stellen auf S. 174 lauten jetzt „Part-I“ wie im übrigen Fließtext.
- **Greiner/Voigt/Wolff (J. Operator Theory):** Der gemeinsame Bib-Eintrag hat jetzt Band 5. Damit sind auch die gleichlautenden ◐-Punkte auf S. 109, 132, 185, 367 und 463 erledigt.
- Formeln wurden nicht verändert.
- Die Änderungen liegen im Git-Branch `fahnenkorrektur`; `main` enthält weiterhin den Stand vor den Korrekturen.

## Abweichungen von der Arbeitsliste

Bei diesen Punkten hat der Quelltext (Label-Namen) das gemeinte Verweisziel gezeigt; umgesetzt wurde daher etwas anderes als in der Spalte „Soll“ der Arbeitsliste:

| S. | Arbeitsliste | Umgesetzt | Begründung |
|---|---|---|---|
| 107 | Corollary 3.1.2 (?) | Part-III, Corollary 3.1.3 | Label `cor:c3-1.3` verweist nach Teil III; „Part-III,“ fehlte. |
| 114 | Example 3.2.3/3.2.4 prüfen | Part-II, Example 3.1.7 | Label `ex:b3-1.7` verweist nach Teil II; „Part-II,“ fehlte. |
| 251 | Part-I, Section 4.1. | Part-I, Section 4.1, Section 4.1 and Part-III, Section 4.1 | Gemeint sind die Abschnitte 4.1 aus Teil I, II und III (Labels `sec:a4-1`, `sec:b4-1`, `sec:c4-1`). |
| 257 | Eq. (4.3.10) | the problem in Example 4.3.11 | Das Label zeigt nur auf die Randbedingung; gemeint ist das ganze System des Beispiels. |
| 461 | Theorem 4.4.5 (iv) | Verweis auf Label `thm:d4-4.4` | Der Verweis geht jetzt auf den Satz, dessen Beweis an dieser Stelle steht. |
| 468 | Part-I, Section 3.6.6 | the proof of Part-I, Theorem 3.6.6 | Einen Abschnitt 3.6.6 gibt es nicht; im Beweis von Theorem 3.6.6 werden über das F-Produkt Näherungseigenvektoren zu Eigenvektoren gemacht. |

## Einzelkorrekturen

### Teil I, Kap. 1 – Basic Results on Semigroups on Banach Spaces

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 12 | Let E to be one of the following function spaces | Let E be one of the following function spaces |  |
| 17 | generator on a core of its domain (see Proposition 1.1.9 (ii). In particular | (see Proposition 1.1.9 (ii)). In particular |  |
| 23 | form a strongly-continuos semigroup with respect to the sup-norm | form a strongly continuous semigroup with respect to the sup-norm |  |
| 26 | In most cases F will be either the Frechét filter or some free ultra filter | In most cases F will be either the Fréchet filter or some free ultrafilter | Nur Fréchet/ultrafilter; die Klammerstellung (◐) ist noch offen. |

### Teil I, Kap. 2 – Characterization of Semigroups on Banach Spaces

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 32 | (which might not be known explicitely) | (which might not be known explicitly) |  |
| 36 | So by Theorem 1.1.9 (ii) D(A) is a core of B. | So by Proposition 1.1.9 (ii) D(A) is a core of B. |  |
| 38 | it follows that T(·)f is measureable. | it follows that T(·)f is measurable. |  |
| 45 | (this follows from Theorem 1.1.6 (ii)) | (this follows from Proposition 1.1.6 (ii)) |  |
| 47 | All together we obtain for \ | r\ | Doppelter Satz im Quelltext auskommentiert. |
| 51 | if and only if the following equivalent assertions holds. | if and only if the following equivalent assertions hold. |  |
| 58 | Consequently it posseses a σ(E′,E)-limit point | Consequently it possesses a σ(E′,E)-limit point |  |
| 59 | p(λR(λ,A)g) ⩽ p(g)for all g ∈ E | p(λR(λ,A)g) ⩽ p(g) for all g ∈ E |  |
| 60 | (2t c∥g − Af∥ + t² c∥Ag∥) (by (2.3)) | (by Eq. (2.2.2)) |  |
| 70 | [30] J. J. Moreau: Fonctionelles convexes. Séminaire sur les équations aux derivées partielles. | [30] J. J. Moreau: Fonctionnelles convexes. Séminaire sur les équations aux dérivées partielles. |  |

### Teil I, Kap. 3 – Spectral Theory

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 79 | we recall the well known resolvent equation . | we recall the well-known resolvent equation. |  |
| 82 | the spectral mapping theorem for the resolvent (Theorem 3.2.5) | (Proposition 3.2.5) |  |
| 100 | a "multiplication operator" | a “multiplication operator” |  |
| 104 | (cf. Formula Eq. (1.3.1) on page 19) | (cf. Eq. (1.3.1) on page 19) |  |
| 107 | for some 𝑘 ∈ Z otherwise if (∥𝑅(𝜇𝑘, 𝐴)∥)𝑘∈Z is unbounded. | for some 𝑘 ∈ Z or if (∥𝑅(𝜇𝑘, 𝐴)∥)𝑘∈Z is unbounded. |  |
| 107 | The Example 3.1.3 above in combination with Corollary 3.1.3 shows | Example 3.1.3 above in combination with Corollary 3.1.2 (?) shows | Umgesetzt als „Part-III, Corollary 3.1.3“ (siehe Abweichungen). |
| 108 | The spectral mapping theorem for the resolvent (Theorem 3.2.5) is well known | (Proposition 3.2.5) |  |
| 108 | can be found in Kato [16], Chap.III,§ 6.4]. | can be found in Kato [16, Chap. III, § 6.4]. |  |
| 108 | Applications to isolated singularities like Example 3.6 are discussed | like Example 3.3.6 are discussed |  |

### Teil I, Kap. 4 – Asymptotics of Semigroups on Banach Spaces

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 114 | for all 𝑓 ∈ 𝐶0(R𝑛); see also Example 3.1.7. | Verweisziel prüfen (z. B. Example 3.2.3/3.2.4) | Umgesetzt als „Part-II, Example 3.1.7“ (siehe Abweichungen). |
| 119 | Example 4.1.2(c) shows that uniform exponential stability is not equivalent to | Example 4.1.2 (ii) shows |  |
| 121 | On the other hand, Example 4.1.2(c) produces a semigroup | Example 4.1.2 (ii) produces a semigroup |  |
| 125 | The Laplacian Δ generates a bounded holomorphic semigroups on 𝐿𝑝(R𝑛) | generates a bounded holomorphic semigroup on |  |

### Teil II, Kap. 1 – Basic Results on Spaces C₀(X)

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 139 | This identification is a topological isomorphisms with respect to the weak*-topology | This identification is a topological isomorphism with respect to the weak* topology |  |
| 139 | (i) positive (notation: 𝑇 ⩾ 0) if 𝑇 𝑓 is a positive whenever 𝑓 is positive, | if 𝑇𝑓 is positive whenever 𝑓 is positive, |  |

### Teil II, Kap. 2 – Characterization of Positive Semigroups on C₀(X)

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 143 | It will be essential that K is compact for all what follows | It will be essential that K is compact for all that follows |  |
| 148 | The next result is a strengthened form of Theorem 1.6. | The next result is a strengthened form of Theorem 2.1.6. |  |
| 152 | preceding page succesively to B = m^{1/k} · A | preceding page successively to ... |  |
| 154 | Then A is the generator of positive semigroup. | Then A is the generator of a positive semigroup. |  |
| 161 | hence T(t) is so as well (cf. Remark 2.1). | hence T(t) is so as well (cf. Remark 2.2.1). |  |
| 161 | we denote by dφ he linear form on C[−1, 0] | we denote by dφ the linear form on C[−1, 0] |  |
| 163 | this will enable us, to give a detailed description | this will enable us to give a detailed description |  |
| 167 | is closable (by Corollary 2.1.11 ); but | is closable (by Corollary 2.1.11); but |  |
| 179 | is closed in (a, b) Thus (a, b) ∖ K is the union | is closed in (a, b). Thus (a, b) ∖ K is the union |  |
| 183 | It is easy to verify, that the generator of this group is | It is easy to verify that the generator of this group is |  |
| 184 | we refer to the corresponding notes in Part-III, Chapter 2, Theorem 2.1.6 and 2.1.8 are due to Arendt et al. [4] | ... in Part-III, Chapter 2. Theorems 2.1.6 and 2.1.8 are due to Arendt et al. [4] |  |
| 184 | Infinite-dimensional Systems, Retahof 1983. | Infinite-dimensional Systems, Retzhof 1983. |  |
| 185 | [11] P. Collatz: Einschließungssatz für die charakteristischen Zahlen von Matrizen. | [11] L. Collatz: Einschließungssatz ... |  |

### Teil II, Kap. 3 – Spectral Theory of Positive Semigroups on C₀(X)

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 202 | A real spectral value λ0 of a generator A is called a dominant provided that | ... is called dominant provided that |  |
| 204 | unless φ = r0δ0 for some r0 ∈ R.) | unless φ = r0δ0 for some r0 ∈ R. |  |
| 212 | such that Pσ(A) = H). Here (H_d)ˆ denotes | such that Pσ(A) = H. Here (H_d)ˆ denotes |  |
| 215 | A complete proof of this results requires | A complete proof of this result requires |  |
| 220 | by Part-I, Proposition 3.6.2 Since every boundary point | by Part-I, Proposition 3.6.2. Since every boundary point |  |
| 221 | by Lemma 3.4.2 (b) there exists y ∈ K∞ | by Lemma 3.4.2 (ii) there exists y ∈ K∞ |  |
| 221 | For details see Sect.18.2 of Dieudonné [11]. | For details see Section 18.2 of Dieudonné [11]. |  |
| 222 | (iii) We consider Ω as in (b) and assume | (iii) We consider Ω as in (ii) and assume |  |
| 222 | by remarking that the ideas of (b) and (c) can be combined | by remarking that the ideas of (ii) and (iii) can be combined |  |
| 227 | The dichotomy stated in (Eq.(3.2.19) on page 202) is probably | The dichotomy stated in Eq. (3.2.19) on page 202 is probably |  |
| 229 | [22] J. P. Roth: “Les operateurs elliptiques comme générateurs infinitésimaux de semigroups de Feller”. Séminaire de Théorie du Potential | “Les opérateurs elliptiques comme générateurs infinitésimaux de semi-groupes de Feller”. Séminaire de Théorie du Potentiel |  |

### Teil II, Kap. 4 – Asymptotics of Positive Semigroups on C₀(X)

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 240 | is a countable additive set function | is a countably additive set function |  |
| 242 | Then ω_ess(T) < 0 by Eq. (3.3.10) on page 85). | Then ω_ess(T) < 0 by Eq. (3.3.10) on page 85. |  |
| 251 | as developed in Part-I, Section 4.1, Section 4.1 | as developed in Part-I, Section 4.1. | Umgesetzt als „Part-I, Section 4.1, Section 4.1 and Part-III, Section 4.1“ (siehe Abweichungen). |
| 253 | then σ(A) = ∅ by Proposition 3.4. | then σ(A) = ∅ by Proposition 4.3.4. |  |
| 257 | Then (3.11) takes the abstract form | Then Eq. (4.3.10) takes the abstract form | Umgesetzt als „Then the problem in Example 4.3.11 takes …“ (siehe Abweichungen). |
| 259 | showed the translation property (T)for the solution semigroup | showed the translation property (T) for the solution semigroup |  |
| 259 | (see Part-III, Section 3.4 can be used to derive | (see Part-III, Section 3.4) can be used to derive |  |

### Teil III, Kap. 1 – Basic Results on Banach Lattices and Positive Operators

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 265 | Rainer Nagel und Ulf Schlotterbeck | Rainer Nagel and Ulf Schlotterbeck |  |
| 267 | contains x1, ..., xn (see Section. 1.4). | contains x1, ..., xn (see Section 1.4). |  |

### Teil III, Kap. 2 – Characterization of Positive Semigroups on Banach Lattices

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 284 | of all infinitely differentiabele functions on Ω | of all infinitely differentiable functions on Ω |  |
| 292 | It has been proved by Miyajima & Okazawa [23]] that | It has been proved by Miyajima & Okazawa [23] that |  |
| 294 | In the proof of the "only if" - part of Proposition 2.3.6 | In the proof of the “only if” part of Proposition 2.3.6 |  |
| 303 | which finally implies that B is closable Now let λ > λ0 | which finally implies that B is closable. |  |
| 315 | is right-sided Gateaux differerentiable and | is right-sided Gateaux differentiable and |  |
| 325 | [27] J. Peetre: Une charactérisation abstraite des opérateurs différentiels. | [27] J. Peetre: Une caractérisation abstraite des opérateurs différentiels. |  |

### Teil III, Kap. 3 – Spectral Theory of Positive Semigroups on Banach Lattices

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 341 | then T(t)f is a quasi-interior pointof E+ whenever | then T(t)f is a quasi-interior point of E+ whenever |  |
| 348 | which is finer than the Frechet filter | which is finer than the Fréchet filter |  |
| 350 | ultrafilter U on N which is finer than the Frechet filter | ultrafilter U on N which is finer than the Fréchet filter |  |
| 352 | by calculating the resolvent explicitely | by calculating the resolvent explicitly |  |
| 354 | appearing in the the representation Eq. (3.3.21) | appearing in the representation Eq. (3.3.21) |  |
| 357 | the Césaro means | the Cesàro means |  |
| 366 | or “quasi-strictly positive” in Karlin [21]). Sawashima [30] | or “quasi-strictly positive” in Karlin [21]. Sawashima [30] |  |
| 368 | [34] J. Voigt: On the abszissa of convergence for the Laplace transform | On the abscissa of convergence for the Laplace transform |  |

### Teil III, Kap. 4 – Asymptotics of Positive Semigroups on Banach Lattices

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 370 | 𝑠(𝐴) ∈ 𝜎(𝐴) (see Corollary 3.1.4 ). | (see Corollary 3.1.4). |  |
| 385 | a Markov transition function satisfying all the assumptions of 4.2.7 induces | a Markov transition function satisfying all the assumptions of Example 4.2.8 induces |  |
| 402 | (see Schaefer [36, Section II.5] and thus compactness of 𝐵2 | (see Schaefer [36, Section II.5]) and thus compactness of 𝐵2 |  |
| 402 | As in Example 4.3.13 the first equation in (4.3.14) corresponds to the aging process. | As in Example 4.3.12 the first equation in (4.3.14) corresponds to the aging process. |  |

### Teil IV, Kap. 1 – Basic Results on Semigroups and Operator Algebras

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 413 | R𝑝 has both the Schwarz type property and is identity preservation. | R𝑝 has the Schwarz type property and is identity preserving. |  |
| 414 | the following equalities holds | the following equalities hold |  |

### Teil IV, Kap. 2 – Characterization of Positive Semigroups on W*-Algebras

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 418 | Using the Schwarz, inequality we obtain | Using the Schwarz inequality, we obtain |  |

### Teil IV, Kap. 3 – Spectral Theory on W*-Algebras and their Preduals

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 422 | subinvariant for a positive map 𝑇 ∈ L(𝑀) (resp.. positive semigroup T) | (resp. positive semigroup T) |  |
| 425 | by the uniqueness theorem (*) on p. 422 for the absolut value | for the absolute value |  |
| 426 | we obtain that 𝜑+ and 𝜑− in Fix(R). | we obtain that 𝜑+ and 𝜑− are in Fix(R). |  |
| 432 | 3.2 Spectral Properties of Uniformly Ergodic Semigoups | 3.2 Spectral Properties of Uniformly Ergodic Semigroups |  |
| 432 | the discret group 𝑃𝜎(𝐴) ∩ iR | the discrete group |  |
| 434 | and the assertion follows from Lemma 3.1.6). | and the assertion follows from Lemma 3.1.6. |  |
| 437 | and the assocciated ergodic projection | and the associated ergodic projection |  |
| 438 | Our main result Theorem 3.1.10 on extends Part-II, Theorem 3.3.6 | Our main result Theorem 3.1.10 extends Part-II, Theorem 3.3.6 |  |
| 439 | G. Greiner, J. Voigt & M. Wolff: On the spectral bound ... J. Operator Theory (1981) 245–256. | J. Operator Theory 5 (1981) 245–256. | Band 5 im gemeinsamen Bib-Eintrag ergänzt; wirkt in allen Kapiteln. |

### Teil IV, Kap. 4 – Asymptotics on C*- and W*-Algebras

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 442 | characterizes uniform exponentially stability of the semigroup | characterizes uniform exponential stability |  |
| 443 | Then the following assertion are equivalent. | Then the following assertions are equivalent. |  |
| 445 | whereas (c) and (d)), resp. (e) and (f) are equivalent by the Remark 4.2.1 (iii). | whereas (c) and (d), resp. (e) and (f), are equivalent by Remark 4.2.1 (iii). |  |
| 446 | (see Propositions 4.3.7, 4.3.8 &. 4.3.9) | (see Propositions 4.3.7, 4.3.8 & 4.3.9) | Umgesetzt als „Proposition 4.3.7, Theorem 4.3.8 and Corollary 4.3.9“. |
| 446 | Therefore the following compactness criterium is quite useful. | compactness criterion |  |
| 446 | the orbit {𝑇(𝑡)𝜑 : 𝑡 ∈ R+} is relatively weak compact | is relatively weakly compact |  |
| 448 | (see Krengel [14, Chap.2, Theorem1.4]) | (see Krengel [14, Chap. 2, Theorem 1.4]) |  |
| 449 | By Proposition 3.1 the semigroup T is strongly ergodic. | By Proposition 4.3.1 the semigroup T is strongly ergodic. |  |
| 451 | If 𝑢1 and 𝑢2 in 𝑈, then | If 𝑢1 and 𝑢2 are in 𝑈, then |  |
| 451 | the fact that 𝑇0(𝑡)′ is a *-automorphismus on 𝑁. | is a *-automorphism on 𝑁. |  |
| 452 | as group of *-automorphism such that the fixed space | as a group of *-automorphisms |  |
| 452 | We apply now these results to weak*-semigroup on B(𝐻). | We now apply these results to weak*-semigroups on B(𝐻). |  |
| 452 | and 𝜑 is a faithful T-invariant normal states. | a faithful T-invariant normal state. |  |
| 452 | irreducible (equvalently, if the fixed space | (equivalently, if |  |
| 454 | a predual 𝑀∗ of a von Neumann-algebra 𝑀 | of a von Neumann algebra 𝑀 |  |
| 459 | Without further comments, we will now use following facts. | we will now use the following facts. |  |
| 461 | hence Theorem 4.4.2 (iv) is proved. | hence Theorem 4.4.5 (iv) is proved. | Verweis auf den Satz, dessen Beweis hier steht (siehe Abweichungen). |
| 461 | exists in the strong operator topology with 𝐴′ is the generator of T′. | where 𝐴′ is the generator of T′. |  |
| 463 | U. Groh & B. Kümmerer: Bibounded operators 𝑊∗-algebras. | Bibounded operators on W∗-algebras. |  |

### Updated Notes

| S. | Ist | Soll | Hinweis |
|---|---|---|---|
| 468 | to the spectral theory of 𝐶0-semigroups, as in Chapter 3.6.6, was started | as in Part-I, Section 3.6.6 | Umgesetzt als „the proof of Part-I, Theorem 3.6.6“ (siehe Abweichungen). |
| 468 | Using this, El-Mennaoui & Engel [30] gives a characterization | El-Mennaoui & Engel [30] give a characterization |  |
| 470 | Quantative estimates of the decay of the semigroup | Quantitative estimates |  |
| 471 | [16] J. Diestel: A survey of results related to the Dunford-Pettis property. ... Contemp. Math. 2, 15-60 (1980). 1980. | ... Contemp. Math. 2 (1980) 15–60. | Bib-Eintrag auf @InCollection umgestellt. |
| 474 | As examples for the rich litterature we mention | the rich literature |  |
| 475 | persistent irreducibilty implies that the generator | persistent irreducibility |  |
| 475 | In Gerlach [21] strong convergence of Feller semigoups is studied. | Feller semigroups |  |
| 481 | Even the spectrum of the generator is independent on p in this case | independent of p |  |
| 481 | The domain of its generator can be described explicitely | explicitly |  |
| 489 | This also follows from the example given above above and the fact | from the example given above and the fact |  |
| 490 | By Greiner et al. [12, Theorem 5.3.1]] one has | By Greiner et al. [12, Theorem 5.3.1] one has |  |

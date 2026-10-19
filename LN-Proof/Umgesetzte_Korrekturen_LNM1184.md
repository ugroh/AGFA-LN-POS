# Umgesetzte Korrekturen: *One-parameter Semigroups of Positive Operators* (2. Aufl.)

Springer LNM 1184, Fahnenkorrektur zum Proof-PDF vom 14.10.2026. Stand: 18.10.2026.

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

Prüfpunkte Updated Notes (aus `updated-notes-pruefpunkte.md`, von Ulrich am Original geprüft, umgesetzt 19.10.2026):

- Part III, Kap. 2 (Edeko–Gerlach–Kühner, `un-part-c.tex`): „continuous flow on a compact Borel probability space“ → „continuous flow on a compact space equipped with a Borel probability measure“; dazu „measure-preserving“ mit Bindestrich.
- Part III, Kap. 2 (Domination, zbmath00417080): Text richtig, keine Änderung.
- Part I, Kap. 2 (Lumer–Phillips-Variante, zbmath07950102): Text richtig, keine Änderung.

## Formelkorrekturen Kap. 1, Teil I–III (18.10.2026)

Umgesetzt sind alle Punkte zu Kap. 1 aus den Formellisten `korrekturen-mathe-part-a/b/c.md`, nachdem Rainer Nagel sie durchgesehen hat (seine Anmerkungen in `rana/korrekturen-mathe-part-*.pdf` betreffen nur spätere Kapitel). In den Listen sind die Zeilen mit **Umgesetzt** markiert; Einzelheiten stehen dort.

| Teil | Datei | Punkte | davon schon vorher erledigt |
|---|---|---|---|
| I | `part-a/chap-a1.tex` | 31 | 3 (Z. 767, 881, 1159) |
| II | `part-b/chap-b1.tex` | 2 | – |
| III | `part-c/chap-c1.tex` | 14 | 3 (Z. 476, 520, 529) |

Inhaltlich relevant sind vor allem:

- **Teil I, Abschnitt 1.2.2 (Matrixhalbgruppen, S. 9):** `1/2` → `s/2` im Exponenten.
- **Teil I, Abschnitt 1.3.5 (adjungierte Halbgruppe, S. 22):** `f_f'` → `\xi_f'` und `0 < s \leq t_0` statt `0 \leq s`.
- **Teil I, Tensorprodukte:** „least cross norm on E ⊗ F“ statt „E × F“; im Beweis der Proposition in Abschnitt 1.3.8 sind S und T jetzt richtig zugeordnet (`S(h)f ⊗ (T(h)g − g) + (S(h)f − f) ⊗ g`).
- **Teil I, 𝓕-Produkt:** `E_𝓕^T` → `E_𝓕^𝒯` wie in Teil II/III; `T(t)_F` → `T(t)_𝓕`.
- **Teil III, Kap. 1:** `\inf(\sup_α f_α, h)` (fehlende Klammer), AL-Raum `(E, f')` statt `(E, x')`, Bedingung „for f ∈ E₊“ hinter die Mengenklammer, `\mathcal{L}^r(E,F)` einheitlich mit Komma, aufrechtes i, Zentrum `𝒵(E)`.

Der Rest sind Satz- und Notationsfragen: Klammern, `\eqqcolon`, `\limsup`, `\mapsto`, `\setminus`, aufrechtes d, Mathemodus.

## Kap. 2, Teil I–III (19.10.2026)

Alle offenen Punkte aus `korrekturen-text-part-a/b/c.md` und `korrekturen-mathe-part-a/b/c.md` zu Kap. 2 sind umgesetzt (`chap-a2.tex`, `chap-b2.tex`, `chap-c2.tex`, `bib/ln-references.bib`) und in den Listen mit **Umgesetzt** markiert. Die Punkte aus `math-error-part-a/b/c.md` zu Kap. 2 sind davon nicht betroffen und weiter offen.

Abweichungen und Ergänzungen:

- **Teil I, Example 2.1.4:** Lösung als u(t) = (f − tBg, g), passend zur Matrix. Der Vorzeichenfehler in Z. 409 (math-error-part-a) ist damit mit (λf + Bg, λg) zu beheben, nicht durch Änderung der Matrix.
- **Teil I:** `$p$-contractive`/`$p$-dissipative` überall außer in `\index`-Einträgen. Notes-Aufzählung jetzt „Section 2.1/2.2/2.3“, ebenso in Kap. 2 von Teil II und III. Kap. 3 und 4 (auch Teil IV) haben noch „Section 1:“.
- **Teil II, Theorem 2.1.16:** Neben m^{l/k} auch der Laufbereich l = 0, …, k−1 (der erste Schritt geht von B = A aus).
- **Teil II, 0 ≪ u:** An allen genannten Stellen; Z. 733 (`0 \leq q`) bewusst nicht, dort genügt q ≥ 0.
- **Teil II:** „neighbourhood“ → „neighborhood“ (amerikanisch, wie „behavior“). de Laubenfels als „de Laubenfels~\cite{…}“, Kurose mit `\cite`, weil biblatex sonst Präfix bzw. Namen doppelt setzt.
- **Teil III:** van Casteren (1984) jetzt als vancasteren:1984 (Integral Equations Operator Theory 7) zitiert – von Ulrich bestätigt. Ebenfalls mit „van Casteren~\cite{…}“.
- **Teil III:** Die Felder in (2.1.7) und (2.3.11) mit `aligned` statt `array`.
- **Bib:** Bénilan–Picard „linéaires“, Picard „accrétifs“, „Special Year in Analysis“, „North-Holland“ in allen Einträgen, Wolff „M. P. H.“ in allen Einträgen, Reihe „Lecture Notes in Math.“ bei arendt:1984a und greiner:1984a, `note = {Preprint}` bei lotz:1982 (veröffentlicht als Math. Z. 190 (1985), steht als lotz:1985 schon im Verzeichnis); miyajimaokazawa:1984 auf die veröffentlichte Fassung umgestellt: Pacific J. Math. 125 (1986) 161–176, Schlüssel beibehalten.
- **Nicht geändert:** Anführungszeichen um Titel, Jahresformat und „Vol.“ in den Literaturlisten kommen aus dem biblatex-Stil und betreffen alle Einträge.

## Bereinigung der Bib-Dateien (18.10.2026)

Beide Literaturdateien unter `LN-Book-Springer/bib/` sind durchgesehen und bereinigt.

### `ln-references.bib` (Literatur der ersten Auflage)

Alle zitierten Zeitschriften- und Sammelbandbeiträge wurden einzeln mit zbMATH Open abgeglichen. Nicht abgeglichen sind die 53 Bücher sowie 14 Dissertationen, Reports und unveröffentlichte Arbeiten.

| Eintrag | Korrektur |
|---|---|
| akemann:1972 | Band 16 → 10; Titel „W*-algebra“ → „C*-algebra“ |
| albeverio:1978 | Titel „maps on“ → „maps of von Neumann algebras“ |
| bart:1977 | Jahr 1977 → 1978 |
| battyrobinson:1984 | Titel „ordered spaces“ → „ordered Banach spaces“ |
| benchimol:1978b | Seiten 223–248 → 225–248 |
| benilanpicard:1979 | Seiten 1–37 ergänzt |
| bourgain:1982 | Jahr 1982 → 1983; Seiten 192–226 → 193–216 |
| combesdelaroche:1978 | alle fünf Autoren; Titel mit „Séminaire d’Orléans 1973–1974“ |
| cookeferreira:1983 | Titel „retarded functional differential equations“ |
| davies:1982 | Titel „mean ergodic Markov semigroups“ |
| davies:1986 | Seiten 41–48 ergänzt |
| delaubenfels:1984 | Titel „Well-behaved derivations on C[0,1]“ |
| deleeuw:1961 | Titel „Applications of …“ |
| depagter:1984 | Seiten 543–550 → 543–549 |
| derndinger:1983 | Jahr 1984 |
| derndingernagel:1979 | Titel „stark stetiger“ |
| diblasioetal:1984 | Titel „linear functional differential equations“ |
| eberlein:1948 | Jahr 1948 → 1949 |
| elliot:1972 | Autor Elliott; Titel „Convergence of automorphisms in certain C*-algebras“ |
| feller:1952 | Titel „parabolic differential equations“ |
| gearhart:1978 | Titel „on Hilbert space“ |
| greinernagel:1982 | Band 9 → 61 (die 9 war die Serie) |
| grohkuemmerer:1982 | Seitenangabe vereinheitlicht |
| hadeler:1978 | Jahr 1978 → 1979 |
| kamke:1932 | Jahr 1932 → 1936; Gleichung im Titel ergänzt |
| kato:1986 | Seiten 63–78 ergänzt |
| kurose:1981 | Titel „derivation in C(I)“ |
| lotz:1984 | Herausgeber Fuchssteiner, B.; Seiten 117–133 ergänzt |
| lotz:1986 | Seiten 137–156 ergänzt |
| lumer:1974, lumer:1974a | Jahr 1973; Titel „Perturbation“ (Singular, 19.10.) |
| lumer:1974b, lumer:1975 | Band 25, Jahr 1975, Seiten 409–446; Titel „opérateurs locaux et …“ ohne Komma (19.10., nach Original-PDF der Annales) |
| luxemburg:1979 | Verlag und Reihe University of Arkansas |
| miyajima:1986 | Seiten 241–246 ergänzt |
| nagel:1984 | Seiten 145–154 ergänzt |
| neubrander:1985a | Jahr 1985 → 1986 |
| oseledets:1984 | Titel „linear mappings“ |
| picard:1972 | Zeitschrift „C. R. Acad. Sci. Paris Sér. A“ (Sér. I erst ab 1981) |
| plant:1977 | Titel falsch, jetzt „Nonlinear semigroups of translations in Banach space generated by functional differential equations“ |
| slemrod:1976 | Seiten 783–892 → 783–792 |
| stormer:1972 | Titel „maps of von Neumann algebras“; Seiten 42–50 → 46–50 |
| triggiani:1975a | Titel „… of control systems in Banach space“ |
| triggiani:1975b | Titel „in Banach space“ |
| villellabressan:1985 | Titel „Functional equations of delay type in L¹ spaces“ |
| voigt:1984b | Titel „neutron transport equation“ |
| voigt:1985 | Titel „Interpolation for (positive) C₀-semigroups …“ |
| webb:1984 | Titel „A semigroup proof of the Sharpe-Lotka theorem“; Buchtitel „Infinite-Dimensional Systems“ |
| winkler:1972 | Titel „continuous parameter zero-two law“ |
| wolff:1981 | Titel „… of semigroups of positive operators with applications …“ |
| yosida:1948 | Titel „On the differentiability and the representation of one-parameter semi-group …“ |
| zabczyk:1979 | Seiten 321–332, Reihe Lect. Notes Control Inf. Sci. 14 ergänzt |

Abweichung von zbMATH bewusst belassen: greiner:1982 (zbMATH: 3. Abh., 30 S.), kato:1973 (Jahr 1972/1973 uneinheitlich), kipnis:1974 (zbMATH 1975, Numdam 1974), milstein:1975 (Seiten der russischen Ausgabe).

### `ln-references-EN.bib` (Literatur der Updated Notes)

- Jacob: Titel der Bände I–III vereinheitlicht („Pseudo-Differential Operators and Markov Processes. Vol. I …“).
- Derndinger: Seiten 281–293 ergänzt.
- Diestel (zbmath03911038): auf @InCollection umgestellt (Contemp. Math. 2, 15–60).
- mr4176382: Artikelnummer 20190611 als Seitenangabe.
- Krupa: Seiten 159–166.
- Chill–Tomilov: URL mit https://.
- Ouhabaz: Vorname „El Maati“; Rhandi: Vorname „Abdelaziz“; Henson–Moore: „jun.“ entfernt.

### Stil

In `preamble/ln-biblatex.sty` steht vor dem Zeilenumbruch in den Literatureinträgen jetzt ein Punkt (`\setunit{\addperiod\par\nobreak}`).

### Nachprüfung (19.10.2026)

Alle oben aufgeführten Korrekturen sind in den aktuellen Dateien `ln-references.bib` und `ln-references-EN.bib` vorhanden; nichts wurde überschrieben. Die Springer-Fahne beruht bei Lumer [26]/[27] (Part II, Kap. 2) noch auf dem Stand vor dem 18.10.; die richtigen Angaben sind dort als Fahnenkorrektur zu melden.

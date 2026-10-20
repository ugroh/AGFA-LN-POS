# Fahnenkorrektur (Text): Teil IV (Part D)

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184), Proof-PDF vom 14.10.2026.

Auszug aus `Fahnenkorrektur_Springer_LNM1184.md`. **Seitenangaben** = gedruckte Seitenzahl (PDF-Seite = gedruckte Seite + 18). **Sicherheit:** ● hoch · ◐ mittel · ○ niedrig.

**Stand der Umsetzung (Branch `fahnenkorrektur`):** Alle Punkte dieser Liste sind umgesetzt und im Kommentar mit „Umgesetzt“ markiert (Stand 18.10.2026; Abweichungen stehen im Kommentar der jeweiligen Zeile).

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

Insgesamt **72 Punkte**: 33 ●, 25 ◐, 14 ○; davon umgesetzt: alle.


Übergreifende Punkte (Inhaltsverzeichnis, Kolumnentitel, Schreibweisen) und der Index stehen in `korrekturen-text-allgemein.md`.

### Teil IV, Kap. 1 – Basic Results on Semigroups and Operator Algebras

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 409 | ◐ | if 𝑇 ⊗ Id𝑛 is positive from 𝑀 ⊗ 𝑀𝑛 in 𝑀 ⊗ 𝑀𝑛 | if 𝑇 ⊗ Id𝑛 is positive from 𝑀 ⊗ 𝑀𝑛 into 𝑀 ⊗ 𝑀𝑛 | Grammatik | **Umgesetzt.** |
| 409 | ○ | satisfies the so called Schwarz-inequality | satisfies the so-called Schwarz inequality | Konsistenz | **Umgesetzt.** Auf S. 410 'Schwarz inequality' ohne Bindestrich |
| 410 | ◐ | on a commutative C∗-algebra is a Schwarz map. (Takesaki [7, Chapter IV]). | on a commutative C∗-algebra is a Schwarz map (Takesaki [7, Chapter IV]). | Satz | **Umgesetzt.** Punkt vor der Quellenklammer |
| 410 | ◐ | If (𝑆(𝑡)𝑥)(𝑆(𝑡)𝑥)∗ ⩽ 𝑇(𝑡)(𝑥𝑥∗) for all 𝑥 ∈ 𝑀 and 𝑡 ∈ R+. Then | If (𝑆(𝑡)𝑥)(𝑆(𝑡)𝑥)∗ ⩽ 𝑇(𝑡)(𝑥𝑥∗) for all 𝑥 ∈ 𝑀 and 𝑡 ∈ R+, then | Grammatik | **Umgesetzt.** If-Satz durch Punkt abgetrennt (Theorem 1.2.1) |
| 410 | ○ | we recommend to compare the results of this section | we recommend comparing the results of this section | Grammatik | **Umgesetzt.** |
| 412 | ◐ | As in Part-III, Section 3.3 the following notion will be an important tool | As in Part-III, Section 3.2 the following notion will be an important tool | Querverweis | **Umgesetzt.** Pseudo-Resolventen werden in Part III, Abschnitt 3.2 behandelt (vgl. 'Part-III, Example 3.2.5' wenige Zeilen später) |
| 412 | ○ | T is a semigroup of Schwarz-type, if and only if 𝜇𝑅(𝜇, 𝐴) is a Schwarz-operator | T is a semigroup of Schwarz type if and only if 𝜇𝑅(𝜇, 𝐴) is a Schwarz operator | Konsistenz | **Umgesetzt.** Sonst 'Schwarz type' ohne Bindestrich; Komma vor 'if and only if' überflüssig |
| 413 | ● | R𝑝 has both the Schwarz type property and is identity preservation. | R𝑝 has the Schwarz type property and is identity preserving. | Grammatik | **Umgesetzt.**  |
| 414 | ● | the following equalities holds | the following equalities hold | Grammatik | **Umgesetzt.**  |
|      |      |                                                              |                                                              |             |                                                              |
|      |      |                                                              |                                                              |             |  |

### Teil IV, Kap. 2 – Characterization of Positive Semigroups on W*-Algebras

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 417 | ○ | which derivations) commuting with certain automorphism groups are automatically generators of strongly continuous positive semigroups. | ... generators of strongly continuous positive semigroups? | Satz | **Umgesetzt.** Formulierung als Frage ('Which maps ...'), endet mit Punkt |
| 418 | ● | Using the Schwarz, inequality we obtain | Using the Schwarz inequality, we obtain | Satz | **Umgesetzt.** Komma an falscher Stelle (im PDF sichtbar) |
| 418 | ◐ | (compare Elliot [1], Lemma 2.). | (compare Elliott [1, Lemma 2]). | Literatur | **Umgesetzt.** Name korrekt 'Elliott' (auch in der Literaturliste S. 419 'G. Elliot'); überflüssiger Punkt; Zitierformat sonst '[n, ...]' |
|      |      |                                                              |                                                            |           |                                                              |

### Teil IV, Kap. 3 – Spectral Theory on W*-Algebras and their Preduals

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 422 | ● | subinvariant for a positive map 𝑇 ∈ L(𝑀) (resp.. positive semigroup T) | (resp. positive semigroup T) | Satz | **Umgesetzt.** Doppelter Punkt |
|      |      |                                                              |                                                              |             |                                                              |
| 423 | ◐ | Hence Fix(𝑇) is a self adjoint subspace of 𝑀 | selfadjoint (bzw. einheitlich self-adjoint) | Konsistenz | **Umgesetzt.** Uneinheitlich: 'self adjoint' (S. 423, 425, 457) neben 'selfadjoint' (S. 425, 426) |
| 425 | ● | by the uniqueness theorem (*) on p. 422 for the absolut value | for the absolute value | Tippfehler | **Umgesetzt.**  |
| 426 | ● | we obtain that 𝜑+ and 𝜑− in Fix(R). | we obtain that 𝜑+ and 𝜑− are in Fix(R). | Grammatik | **Umgesetzt.** Verb fehlt |
| 428 | ◐ | This is no longer true in the non commutative case. | noncommutative (einheitlich) | Konsistenz | **Umgesetzt.** 'non commutative' (S. 428, 429, 454) neben 'noncommutative' (S. 438, 489, 490) |
| 429 | ◐ | (i) The fixed space of T is one dimensional ... (iii) The fixed space of the adjoint weak*-semigroup T′ is one-dimensional. | einheitlich 'one-dimensional' | Konsistenz | **Umgesetzt.** Im selben Theorem uneinheitlich; 'one dimensional' auch S. 430, 452, 455 |
| 431 | ◐ | (see, Jacobs [11, Satz 6.1., p.77]) | (see Jacobs [11, Satz 6.1, p. 77]) | Satz | **Umgesetzt.** überflüssiges Komma nach 'see', Leerzeichen in 'p. 77' fehlt |
| 432 | ● | 3.2 Spectral Properties of Uniformly Ergodic Semigoups | 3.2 Spectral Properties of Uniformly Ergodic Semigroups | Tippfehler | **Umgesetzt.** Abschnittstitel; der Fehler steht auch in den Kolumnentiteln S. 433, 435, 437, 439 (und vermutlich im Inhaltsverzeichnis) |
| 432 | ● | the discret group 𝑃𝜎(𝐴) ∩ iR | the discrete group | Tippfehler | **Umgesetzt.**  |
| 432 | ◐ | fulfils the assertions of Theorem 1.10 | fulfils the assertions of Theorem 3.1.10 | Querverweis | **Umgesetzt.** Gemeint ist sicher Theorem 3.1.10 (Altnummerierung) |
| 433 | ◐ | we obtain from Lemma 1.1.b that for all 𝑥 ∈ 𝑁 | we obtain from Lemma 3.1.1 (ii) that | Querverweis | **Umgesetzt.** Altnummerierung 'Lemma 1.1.b'; inhaltlich passt Lemma 3.1.1 (ii) |
| 434 | ● | and the assertion follows from Lemma 3.1.6). | and the assertion follows from Lemma 3.1.6. | Satz | **Umgesetzt.** überzählige schließende Klammer |
| 437 | ● | and the assocciated ergodic projection | and the associated ergodic projection | Tippfehler | **Umgesetzt.**  |
| 437 | ◐ | one part of the corollary is proved | one part of the proposition is proved | Querverweis | **Umgesetzt.** Die Aussage ist als Proposition 3.2.3 nummeriert |
| 438 | ● | Our main result Theorem 3.1.10 on extends Part-II, Theorem 3.3.6 | Our main result Theorem 3.1.10 extends Part-II, Theorem 3.3.6 | Tippfehler | **Umgesetzt.** überflüssiges 'on' |
| 438 | ○ | for all 𝛼 ∈ R (Proposition 3.2.1 ). | (Proposition 3.2.1). | Satz | **Umgesetzt.** Leerzeichen vor der Klammer |
| 439 | ● | G. Greiner, J. Voigt & M. Wolff: On the spectral bound ... J. Operator Theory (1981) 245–256. | J. Operator Theory 5 (1981) 245–256. | Literatur | **Umgesetzt.** Bandnummer fehlt (in den Updated Notes Part IV korrekt mit 5); gilt ebenso für Ref. [8] auf S. 463 |

### Teil IV, Kap. 4 – Asymptotics on C*- and W*-Algebras

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 442 | ● | characterizes uniform exponentially stability of the semigroup | characterizes uniform exponential stability | Grammatik | **Umgesetzt.**  |
| 442 | ◐ | From this the assumption follows by Part-I, Theorem 4.1.11. | From this the assertion follows | Tippfehler | **Umgesetzt.** |
| 443 | ● | Then the following assertion are equivalent. | Then the following assertions are equivalent. | Grammatik | **Umgesetzt.**  |
| 443 | ◐ | Proof. Since 𝑠(𝐴) = 𝜔0 by Theorem 4.1.3 | by Theorem 4.1.1 | Querverweis | **Umgesetzt.** Theorem 4.1.7 betrifft C*-Algebren mit Eins, dafür gilt Theorem 4.1.1; 4.1.3 behandelt Prädualräume |
| 443 | ○ | positive semigroups on C*-algebras with unit. Theorem 4.1.7 Let 𝑀 be a C*-algebra | C∗-algebras (gleicher Stern wie sonst) | Konsistenz | **Umgesetzt.** Hier ein normales Sternchen statt des sonst verwendeten hochgestellten ∗; bitte im PDF prüfen |
| 443 | ○ | but (𝑇(𝑡))𝑡⩾0 is strongly stable | is uniformly stable (Terminologie aus Definition 4.1.6 (ii)) | Konsistenz | **Umgesetzt.** In Definition 4.1.6 heißt die starke Konvergenz gegen 0 'uniformly stable'; 'strongly stable' kommt dort nicht vor |
| 445 | ● | whereas (c) and (d)), resp. (e) and (f) are equivalent by the Remark 4.2.1 (iii). | whereas (c) and (d), resp. (e) and (f), are equivalent by Remark 4.2.1 (iii). | Satz | **Umgesetzt.** überzählige Klammer, überflüssiger Artikel 'the' |
| 446 | ● | (see Propositions 4.3.7, 4.3.8 &. 4.3.9) | (see Propositions 4.3.7, 4.3.8 & 4.3.9) | Satz | **Umgesetzt** als „Proposition 4.3.7, Theorem 4.3.8 and Corollary 4.3.9“. Punkt nach '&' streichen; 4.3.8 ist außerdem ein Theorem und 4.3.9 ein Corollary |
| 446 | ● | Therefore the following compactness criterium is quite useful. | compactness criterion | Tippfehler | **Umgesetzt.**  |
| 446 | ● | the orbit {𝑇(𝑡)𝜑 : 𝑡 ∈ R+} is relatively weak compact | is relatively weakly compact | Grammatik | **Umgesetzt.**  |
| 447 | ◐ | which is of Schwarz type. It follows as in (b) that | It follows as in (ii) that | Querverweis | **Umgesetzt.** Remark 4.3.2 hat die Teile (i)–(iii), ein Teil (b) existiert nicht |
| 448 | ● | (see Krengel [14, Chap.2, Theorem1.4]) | (see Krengel [14, Chap. 2, Theorem 1.4]) | Satz | **Umgesetzt.** Leerzeichen fehlen; auf S. 461 fehlt ebenso das Leerzeichen in 'Chap.2' |
| 449 | ● | By Proposition 3.1 the semigroup T is strongly ergodic. | By Proposition 4.3.1 the semigroup T is strongly ergodic. | Querverweis | **Umgesetzt.**  |
| 449 | ◐ | (Leeuw & Glicksberg [15], Junghenn [13] & Krengel [14, § 2.4]) | (de Leeuw & Glicksberg [15], ...) | Konsistenz | **Umgesetzt.** Im Literaturverzeichnis steht 'K. de Leeuw' |
| 450 | ◐ | which is not empty by assumptions. | which is not empty by assumption. | Grammatik | **Umgesetzt.** |
| 450 | ○ | Halmos-von Neumann Theorem in commutative ergodic theory | Halmos–von Neumann theorem (einheitlich mit S. 455) | Konsistenz | **Umgesetzt.** S. 450 'Theorem', S. 455 'theorem' |
| 451 | ● | If 𝑢1 and 𝑢2 in 𝑈, then | If 𝑢1 and 𝑢2 are in 𝑈, then | Grammatik | **Umgesetzt.**  |
| 451 | ● | the fact that 𝑇0(𝑡)′ is a *-automorphismus on 𝑁. | is a *-automorphism on 𝑁. | Tippfehler | **Umgesetzt.** deutsches Wort |
| 452 | ● | as group of *-automorphism such that the fixed space | as a group of *-automorphisms | Grammatik | **Umgesetzt.**  |
| 452 | ● | We apply now these results to weak*-semigroup on B(𝐻). | We now apply these results to weak*-semigroups on B(𝐻). | Grammatik | **Umgesetzt.**  |
| 452 | ● | and 𝜑 is a faithful T-invariant normal states. | a faithful T-invariant normal state. | Grammatik | **Umgesetzt.**  |
| 452 | ● | irreducible (equvalently, if the fixed space | (equivalently, if | Tippfehler | **Umgesetzt.**  |
| 453 | ◐ | We show next, that for irreducible W∗-dynamical systems | We show next that for irreducible | Satz | **Umgesetzt.** Komma nach deutscher Regel, im Englischen falsch |
| 453 | ◐ | pertaining to the eigenvalues on iR and let 𝑄 be the faithful normal conditional expectation from 𝑀 onto 𝑁 (Proposition 4.3.7) | eigenvalues in iR ... (Theorem 4.3.5) | Querverweis | **Umgesetzt.** Die bedingte Erwartung stammt aus Theorem 4.3.5 (i), nicht aus Prop. 4.3.7; sonst steht 'eigenvalues in iR' |
| 454 | ● | a predual 𝑀∗ of a von Neumann-algebra 𝑀 | of a von Neumann algebra 𝑀 | Satz | **Umgesetzt.**  |
| 454 | ◐ | 0 is a pole of the resolvent of its generator 𝐵 with residuum 𝑃 = 1 ⊗ 1 | with residue 𝑃 = 1 ⊗ 1 | Konsistenz | **Umgesetzt.** Sonst immer 'residue' |
| 454 | ◐ | forms a strongly continuous one parameter semigroup | one-parameter semigroup | Konsistenz | **Umgesetzt.** |
| 456 | ○ | 𝐻0 is invariant under the extension to 𝐻𝜑 and for the multiplication maps we defined in Remark 3.1.3. | 𝐻0 is invariant under the extensions to 𝐻𝜑 and under the multiplication maps defined in Remark 3.1.3. | Grammatik | **Umgesetzt.** Satz grammatisch verunglückt |
| 457 | ○ | then by Lemma 3.1.2, there exists a sequence of normal states in Fix(R′) with orthogonal supports | then by Lemma 4.4.1, there exists ... | Querverweis | **Umgesetzt.** Die Existenz einer Folge von Zuständen mit orthogonalen Trägern ist Lemma 4.4.1; bitte prüfen |
| 459 | ● | Without further comments, we will now use following facts. | we will now use the following facts. | Grammatik | **Umgesetzt.**  |
| 459 | ◐ | if and only if it converges in 𝜎(𝑀′, 𝑀′′)-topology | converges in the 𝜎(𝑀′, 𝑀′′)-topology | Grammatik | **Umgesetzt.** |
| 461 | ● | hence Theorem 4.4.2 (iv) is proved. | hence Theorem 4.4.5 (iv) is proved. | Querverweis | **Umgesetzt, abweichend:** Verweis jetzt auf den Satz, dessen Beweis an dieser Stelle steht (Label `thm:d4-4.4`). 4.4.2 ist eine Remark; gemeint ist Theorem 4.4.5 |
| 461 | ● | exists in the strong operator topology with 𝐴′ is the generator of T′. | where 𝐴′ is the generator of T′. | Grammatik | **Umgesetzt.**  |
| 463 | ● | U. Groh & B. Kümmerer: Bibounded operators 𝑊∗-algebras. | Bibounded operators on W∗-algebras. | Literatur | **Umgesetzt.** 'on' fehlt im Titel |
|      |      |                                                              |                                                              |             |                                                              |

### Updated Notes, Part IV

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 489 | ● | This also follows from the example given above above and the fact | from the example given above and the fact | Tippfehler | **Umgesetzt.** Wort doppelt |
| 490 | ● | By Greiner et al. [12, Theorem 5.3.1]] one has | By Greiner et al. [12, Theorem 5.3.1] one has | Satz | **Umgesetzt.** doppelte schließende Klammer |
| 490 | ◐ | Chapter 4 As in Part-IV, Chapter 4, results from Glück & Mironchenko [10] | As in Part-II, Chapter 4, results from Glück & Mironchenko ... | Querverweis | **Umgesetzt.** Der Abschnitt gehört selbst zu Part IV, Chapter 4; Glück & Mironchenko wird in den Updated Notes zu Part II, Chapter 4 zitiert |
|      |      |                                                              |                                                              |             |                                                              |

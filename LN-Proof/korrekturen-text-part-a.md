# Fahnenkorrektur (Text): Teil I (Part A)

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184), Proof-PDF vom 14.10.2026.

Auszug aus `Fahnenkorrektur_Springer_LNM1184.md`. **Seitenangaben** = gedruckte Seitenzahl (PDF-Seite = gedruckte Seite + 18). **Sicherheit:** ● hoch · ◐ mittel · ○ niedrig.

**Stand 20.10.2026 (Branch `fahnenkorrektur`):** **Kap. 1 und Kap. 2 sind erledigt**, ebenso die Updated Notes. In Kap. 3–4 sind alle ●-Punkte umgesetzt; ◐ und ○ sind dort offen, außer wo im Kommentar „Umgesetzt“ steht. Abweichungen vom Soll stehen im Kommentar der jeweiligen Zeile.

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

Insgesamt **121 Punkte**: 31 ●, 39 ◐, 51 ○; davon umgesetzt: 82, teilweise: 1.


Übergreifende Punkte (Inhaltsverzeichnis, Kolumnentitel, Schreibweisen) und der Index stehen in `korrekturen-text-allgemein.md`.

### Teil I, Kap. 1 – Basic Results on Semigroups on Banach Spaces

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 4 | ◐ | is continuous for the strong operator topology on L(E), e.g., lim ∥T(t)f − T(t0)f∥ = 0 | is continuous for the strong operator topology on L(E), i.e., lim ... | Grammatik | **Umgesetzt.** Definition, kein Beispiel: 'i.e.' statt 'e.g.'. |
| 5 | ○ | the generator is everywhere defined and therefore bounded (use Proposition 1.1.9 (ii)) | (use Proposition 1.1.9 (i)) | Querverweis | **Umgesetzt.** Beschränktheit folgt aus Abgeschlossenheit = 1.1.9 (i); bitte prüfen. |
| 10 | ◐ | As summary we obtain | In summary we obtain | Grammatik | **Umgesetzt.** |
| 12 | ● | Let E to be one of the following function spaces | Let E be one of the following function spaces | Grammatik | **Umgesetzt.**  |
| 17 | ● | generator on a core of its domain (see Proposition 1.1.9 (ii). In particular | (see Proposition 1.1.9 (ii)). In particular | Satz | **Umgesetzt.** Schließende Klammer fehlt. |
| 17 | ○ | (Reed & Simon [10, p.28]) | (Reed & Simon [10, p. 28]) | Satz | **Umgesetzt.** Ebenso S. 42 'p.252', S. 66 'pp.18-22 ... p.55', S. 67 'p.77'; sonst 'p. 6'. |
| 18 | ○ | There is an easy way how to obtain different (but isomorphic) semigroups | There is an easy way to obtain different (but isomorphic) semigroups | Grammatik | **Umgesetzt.** |
| 20 | ◐ | the translation semigroup (T(t))t⩾0 where T(t)f(x) := f(x+t) (see Example 1.2.4) | (see Section 1.2.4) | Querverweis | **Umgesetzt.** 1.2.4 ist ein Abschnitt, kein Beispiel. |
| 20 | ○ | By Sections 1.2.4 and 1.3.2, the generator A\|F acts as | By Sections 1.2.4 and 1.3.3, the generator A\|F acts as | Querverweis | **Umgesetzt.** Restriktion auf Unterraum = Abschnitt 1.3.3 (Subspace Semigroup), nicht 1.3.2 (Rescaled). Bitte prüfen. |
| 21 | ◐ | it is natural to associate (T(t)′)t⩾0 its weak*-generator | it is natural to associate with (T(t)′)t⩾0 its weak*-generator | Grammatik | **Umgesetzt.** |
| 23 | ● | form a strongly-continuos semigroup with respect to the sup-norm | form a strongly continuous semigroup with respect to the sup-norm | Tippfehler | **Umgesetzt.** 'continuos' -> 'continuous'; außerdem kein Bindestrich (sonst überall 'strongly continuous'). |
| 26 | ● | In most cases F will be either the Frechét filter or some free ultra filter | In most cases F will be either the Fréchet filter or some free ultrafilter | Tippfehler | **Umgesetzt.** Eine Zeile vorher richtig 'Fréchet filter'. |
| 26 | ◐ | (i.e., the filter of sets with finite complement. In most cases F will be ... ultra filter). | (i.e., the filter of sets with finite complement). In most cases F will be ... ultrafilter. | Satz | **Umgesetzt.** Klammer schließt an falscher Stelle. |
| 26 | ○ | For the proof we refer to Lemma 1.4. of Derndinger [2]. | For the proof we refer to Lemma 1.4 of Derndinger [2]. | Satz | **Umgesetzt.** |

### Teil I, Kap. 2 – Characterization of Semigroups on Banach Spaces

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 32 | ● | (which might not be known explicitely) | (which might not be known explicitly) | Tippfehler | **Umgesetzt.**  |
| 32 | ◐ | 2.1.1 The abstract Cauchy problem / 2.1.2 One-parameter groups / 2.1.4 Holomorphic semigroups ... vs. 2.1.3 The Hille-Yosida Theorem, 2.1.8 Perturbation of Generators, 2.1.9 Domains of Uniqueness | Einheitliche Groß-/Kleinschreibung der Unterabschnittsüberschriften (wie in Kap. 1 Title Case, z.B. 'The Abstract Cauchy Problem') | Konsistenz | **Umgesetzt.** Betroffen: 2.1.1, 2.1.2, 2.1.4, 2.1.5 (Differentiable semigroups), 2.1.6 (Norm continuous semigroups), 2.1.7 (Compact semigroups). |
| 35 | ◐ | (continuous dependence from the initial value) | (continuous dependence on the initial value) | Grammatik | **Umgesetzt.** S. 37 korrekt 'dependence on the initial values'. |
| 36 | ● | So by Theorem 1.1.9 (ii) D(A) is a core of B. | So by Proposition 1.1.9 (ii) D(A) is a core of B. | Querverweis | **Umgesetzt.** 1.1.9 ist eine Proposition. |
| 36 | ◐ | It is surprising that from condition (b) and (c) in the corollary | It is surprising that from conditions (b) and (c) in the corollary | Grammatik | **Umgesetzt.** |
| 38 | ● | it follows that T(·)f is measureable. | it follows that T(·)f is measurable. | Tippfehler | **Umgesetzt.**  |
| 39 | ◐ | (see Davies [11], Goldstein [15] or Pazy [31]) | (see Davies [11], Goldstein [16] or Pazy [31]) | Literatur | **Umgesetzt.** [15] ist die Bibliographie, das Lehrbuch ist [16] (so auch S. 32, 53, 68). |
| 40 | ◐ | if and only if it is weakly holomorphic Yosida [40, V.3]. | if and only if it is weakly holomorphic (Yosida [40, V.3]). | Satz | **Umgesetzt.** |
| 40 | ○ | There exists r > 0 and β ∈ (−β1, β1) | There exist r > 0 and β ∈ (−β1, β1) | Grammatik | **Umgesetzt.** |
| 43 | ○ | We now prove the following extension of Corollary 2.1.12 | We now prove the following extension of Corollary 2.1.12. | Satz | **Umgesetzt.** |
| 45 | ● | (this follows from Theorem 1.1.6 (ii)) | (this follows from Proposition 1.1.6 (ii)) | Querverweis | **Umgesetzt.** 1.1.6 ist eine Proposition. |
| 45 | ○ | Pazy [31, Chapter 3, Theorem 4.7 and 4.8] | Pazy [31, Chapter 3, Theorems 4.7 and 4.8] | Grammatik | **Umgesetzt.** Kapitelangabe (Chapter 3 oder 2) bleibt offener Punkt in math-error-part-a. |
| 45 | ○ | the function t ↦ T(t)f is right sided differentiable at t0 | the function t ↦ T(t)f is right-sided differentiable at t0 | Konsistenz | **Umgesetzt.** S. 48 und 51: 'right-sided'. |
| 46 | ○ | Proof of Theorem 2.1.19 . It is enough | Proof of Theorem 2.1.19. It is enough | Satz | **Umgesetzt.** Leerzeichen vor Punkt, im PDF sichtbar. |
| 47 | ● | All together we obtain for \|r\| ⩾ r0, All together we obtain for \|r\| ⩾ r0, | All together we obtain for \|r\| ⩾ r0, | Satz | **Umgesetzt.** Satz doppelt gesetzt (im PDF bestätigt). |
| 50 | ○ | (see e.g., Part-II, Corollary 3.2.12) | (see, e.g., Part-II, Corollary 3.2.12) | Satz | **Umgesetzt.** Komma nach 'see' fehlt. |
| 51 | ● | if and only if the following equivalent assertions holds. | if and only if the following equivalent assertions hold. | Grammatik | **Umgesetzt.**  |
| 54 | ◐ | Let λ > s(A) be so large such that ∥SR(λ,A)∥ < 1. | Let λ > s(A) be so large that ∥SR(λ,A)∥ < 1. | Grammatik | **Umgesetzt.** |
| 57 | ○ | Moreover, it follows from Eq. (2.2.1) on the preceding page p(f) + p(−f) ⩾ p(0) = 0 | Moreover, it follows from Eq. (2.2.1) on the preceding page that p(f) + p(−f) ⩾ p(0) = 0 | Grammatik | **Umgesetzt.** |
| 58 | ● | Consequently it posseses a σ(E′,E)-limit point | Consequently it possesses a σ(E′,E)-limit point | Tippfehler | **Umgesetzt.**  |
| 59 | ● | p(λR(λ,A)g) ⩽ p(g)for all g ∈ E | p(λR(λ,A)g) ⩽ p(g) for all g ∈ E | Satz | **Umgesetzt.** Fehlendes Leerzeichen, im PDF sichtbar. |
| 60 | ● | (2t c∥g − Af∥ + t² c∥Ag∥) (by (2.3)) | (by Eq. (2.2.2)) | Querverweis | Verweis '(2.3)' existiert nicht; gemeint ist offenbar die Abschätzung \|p(f)\| **Umgesetzt.** ⩽ c∥f∥ (2.2.2). |
| 60 | ○ | A continuous sublinear function p : E → R is called half-norm if | is called a half-norm if | Grammatik | **Umgesetzt.** Analog folgt 'is called a strict half-norm'. |
| 60 | ○ | (by Eq. (2.2.5) on page 58 ) | (by Eq. (2.2.5) on page 58) | Satz | **Umgesetzt.** Leerzeichen vor Klammer, im PDF sichtbar. |
| 61 | ◐ | (this is equivalent to the fact that ... such that φ = φ1 − φ2 (see Batty & Robinson [3] or Schaefer [37, Chapter V]). | (this is equivalent to the fact that ... such that φ = φ1 − φ2; see Batty & Robinson [3] or Schaefer [37, Chapter V]). | Satz | **Umgesetzt.** Klammern nicht ausgeglichen. |
| 62 | ◐ | Finally, from 2.2.6 it follows that (T(t)) is p-contractive. | Finally, from Theorem 2.2.6 it follows that (T(t)) is p-contractive. | Querverweis | **Umgesetzt.** |
| 63 | ○ | We conclude this section indicating the results for the complex case. | We conclude this section by indicating the results for the complex case. | Grammatik | **Umgesetzt.** |
| 64 | ◐ | Therefore T is not uniformly continuous however, (T(t) − Id)² = 0 | Therefore T is not uniformly continuous; however, (T(t) − Id)² = 0 | Satz | **Umgesetzt.** |
| 65 | ○ | Then there exists a bounded sequence (xn) in E and a bounded sequence (x′n) in E′ | Then there exist a bounded sequence (xn) in E and a bounded sequence (x′n) in E′ | Grammatik | **Umgesetzt.** |
| 67 | ◐ | Notes ... Section 1: The abstract Cauchy problem is treated ... | Section 2.1: ... | Konsistenz | **Umgesetzt.** In den Notes zu Kap. 2 heißen die Abschnitte 'Section 1/2/3' (S. 67/68), im Buch sonst 2.1, 2.2, 2.3. |
| 67 | ○ | is a Cauchy-sequence for this norm | is a Cauchy sequence for this norm | Tippfehler | **Umgesetzt.** |
| 67 | ○ | In Bourgain [7] it is shown, that H∞(D) is a Grothendieck space | In Bourgain [7] it is shown that H∞(D) is a Grothendieck space | Grammatik | **Umgesetzt.** |
| 68 | ◐ | The observation that eventually norm continuity is preserved | The observation that eventual norm continuity is preserved | Grammatik | **Umgesetzt.** |
| 68 | ○ | in the book of Pazy [31] who discovered Theorem 2.1.16 and 2.1.17. | who discovered Theorems 2.1.16 and 2.1.17. | Grammatik | **Umgesetzt.** |
| 68 | ○ | has the advantage to yield the same permanence | has the advantage of yielding the same permanence | Grammatik | **Umgesetzt.** |
| 68 | ○ | A complete information on the general theory can be obtained | Complete information on the general theory can be obtained | Grammatik | **Umgesetzt.** |
| 68 | ○ | Bénilan & Picard [5] and Picard [34], where the two last consider non-linear semigroups | where the last two consider non-linear semigroups | Grammatik | **Umgesetzt.** |
| 69 | ◐ | [5] P. Bénilan & C. Picard: “Quelques aspects non lineaires du principe du maximum”. Séminaire de Théorie du Potentiel. Vol. 713. Springer 1979. | ... “Quelques aspects non linéaires du principe du maximum”. ... Springer (1979). | Literatur | **Umgesetzt.** Akzent korrigiert. Jahr ohne Klammern und „Vol.“ kommen aus dem biblatex-Stil, nicht geändert. Akzent fehlt; Jahr ohne Klammern (sonst '(Jahr)'); ggf. 'Lecture Notes in Math.' statt 'Vol.'. |
| 69 | ○ | [7] J. Bourgain: H∞ is a Grothendieck space. Studia Math. 75 (1982) 192–226. | [7] J. Bourgain: H∞ is a Grothendieck space. Studia Math. 75 (1983) 193–216. | Literatur | **Umgesetzt.** Schon bei der Bib-Bereinigung (18.10.) korrigiert. Jahr/Seiten nach meiner Kenntnis 1983, 193–216; bitte prüfen. |
| 69 | ○ | Proceedings of the Special year in analysis. Springer (1983). | Proceedings of the Special Year in Analysis. Springer (1983). | Literatur | **Umgesetzt.** |
| 70 | ● | [30] J. J. Moreau: Fonctionelles convexes. Séminaire sur les équations aux derivées partielles. | [30] J. J. Moreau: Fonctionnelles convexes. Séminaire sur les équations aux dérivées partielles. | Literatur | **Umgesetzt.**  |
| 70 | ◐ | [34] C. Picard: Opérateurs φ-accretifs et génération des semi-groupes non linéaires. | [34] C. Picard: Opérateurs φ-accrétifs et génération des semi-groupes non linéaires. | Literatur | **Umgesetzt.** |
| 70 | ◐ | Ed. by K. D. Bierstedt & E. Fuchssteiner. North Holland 1984. | Ed. by K. D. Bierstedt & B. Fuchssteiner. North-Holland (1984). | Literatur | **Umgesetzt.** Herausgeber schon am 18.10. korrigiert; „North-Holland“ jetzt in allen Einträgen. Jahresformat = biblatex-Stil. Herausgeber ist Benno Fuchssteiner; Jahresangabe sonst in Klammern. |
| 70 | ○ | [25] H. P. Lotz: “Uniform convergence of operators on L∞”. 1982. | Unvollständiger Eintrag (z.B. 'Preprint (1982)' ergänzen) | Literatur | **Umgesetzt;** offen: Soll der Preprint bleiben oder durch lotz:1985 ersetzt werden? `note = {Preprint}` ergänzt. Veröffentlicht als Math. Z. 190 (1985), steht als lotz:1985 schon im Verzeichnis. |

### Teil I, Kap. 3 – Spectral Theory

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 71 | ○ | called spectral mapping theorem. | called the spectral mapping theorem. | Grammatik |  |
| 71 | ○ | These — or similar — relations will be of great use | These—or similar—relations will be of great use | Konsistenz | Sonst Geviertstrich ohne Leerzeichen (S. 9 'are—at least in many aspects—', S. 28, S. 72). |
| 76 | ◐ | = (dist(𝑥, 𝜎(𝐴)))^−1 (see Proposition 3.2.5 (ii)) | (see Proposition 3.2.5 (i)) | Querverweis | Die Formel r(R(λ0)) = dist^−1 steht in 3.2.5 (i), nicht (ii). |
| 77 | ◐ | using the notion essential range, see Goldstein [8] | using the notion of essential range | Grammatik |  |
| 79 | ● | we recall the well known resolvent equation . | we recall the well-known resolvent equation. | Satz | **Umgesetzt.** Leerzeichen vor dem Punkt (im PDF sichtbar). |
| 82 | ● | the spectral mapping theorem for the resolvent (Theorem 3.2.5) | (Proposition 3.2.5) | Querverweis | **Umgesetzt.** 3.2.5 ist eine Proposition; ebenso in den Notes S. 108 'Theorem 3.2.5'. |
| 83 | ◐ | Only by adding appropriate hypotheses we will achieve spectral decompositions | Only by adding appropriate hypotheses will we achieve spectral decompositions | Grammatik | Inversion nach 'Only by ...'. |
| 83 | ○ | follows from the Spectral Inclusion Theorem (see 3.6.2) below. | follows from the Spectral Inclusion Theorem (see Proposition 3.6.2 below). | Querverweis |  |
| 86 | ◐ | We review these constructions under the spectral theoretical point of view | from the spectral theoretical point of view | Grammatik |  |
| 87 | ◐ | it follows that (𝜆 − 𝐴/) 𝑓ˆ = 𝑔ˆ = 0, i.e., 𝜆 ∈ 𝜎(𝐴/) | …, i.e., 𝜆 ∈ 𝜎(𝐴/). | Satz | Schlusspunkt fehlt (im PDF geprüft). |
| 88 | ○ | either well known or has been stated in 3.2.2(ii). | stated in Proposition 3.2.2 (ii). | Querverweis |  |
| 92 | ○ | the representations Eq. (3.5.3) on the previous page and Eq. (3.5.4) on the preceding page | the representations (3.5.3) and (3.5.4) on the previous page | Satz | Automatische varioref-Zusätze wirken doppelt/unbeholfen; tritt im Bereich häufig auf (z. B. S. 128 sechsmal 'Eq. (4.2.1) on the previous/preceding page'). |
| 96 | ◐ | Since 𝑅𝜎(𝐴) = 𝑃𝜎(𝐴∗) and 𝑅𝜎(𝑇(𝑡)) = 𝑃𝜎(𝑇(𝑡)∗) (see Proposition 3.4.4) | (see Section 3.4.1) | Querverweis | Proposition 3.4.4 behandelt das F-Produkt; die Aussage über den adjungierten Halbgruppen steht in 3.4.1. |
| 98 | ◐ | on Banach spaces 𝐸1, 𝐸2 with generator 𝐴1, 𝐴2. | with generators 𝐴1, 𝐴2. | Grammatik |  |
| 99 | ◐ | (see Theorem 2.1.19 ). By taking | (see Theorem 2.1.19). By taking | Satz | Leerzeichen vor ')' bzw. ','; gleiches Muster im PDF bestätigt auf S. 121 ('Corollary 3.6.7 )', 'Theorem 2.1.6 )'), außerdem S. 123 'Theorem 3.6.3 )', S. 124 'Corollary 3.6.4 ,', S. 125 'Corollary 2.1.12 )'. |
| 100 | ● | a "multiplication operator" | a “multiplication operator” | Satz | **Umgesetzt.** Gerade Anführungszeichen statt typografischer (sonst überall “…”). |
| 102 | ○ | That 𝑇(𝜑) is well-defined follows | well defined (einheitlich) | Konsistenz | Wechsel zwischen 'well defined' (S. 85, 87) und 'well-defined' (S. 102, 128) bzw. 'well known' / 'well-known' (S. 84, 138). |
| 104 | ● | (cf. Formula Eq. (1.3.1) on page 19) | (cf. Eq. (1.3.1) on page 19) | Tippfehler | **Umgesetzt.** 'Formula' und 'Eq.' doppelt. |
| 104 | ◐ | By the rescaling procedure Section 1.3.2 we may assume | By the rescaling procedure (see Section 1.3.2) we may assume | Grammatik | Ebenso S. 107: 'use the rescaling procedure Section 1.3.2'. |
| 105 | ○ | is Cesàro-summable … Fourier series is Cesàro summable | einheitlich 'Cesàro summable' (oder durchgehend mit Bindestrich) | Konsistenz | S. 104/105 wechseln 'Cesàro summable' und 'Cesàro-summable'; ebenso 'Fejér’s Theorem' (S. 104) vs. 'Fejér’s theorem' (S. 105) und 'Hahn-Banach theorem' (S. 76, 91) vs. 'Hahn-Banach Theorem' (S. 93). |
| 107 | ● | for some 𝑘 ∈ Z otherwise if (∥𝑅(𝜇𝑘, 𝐴)∥)𝑘∈Z is unbounded. | for some 𝑘 ∈ Z or if (∥𝑅(𝜇𝑘, 𝐴)∥)𝑘∈Z is unbounded. | Grammatik | **Umgesetzt.** 'either … or' statt 'either … otherwise'. |
| 107 | ● | The Example 3.1.3 above in combination with Corollary 3.1.3 shows | Example 3.1.3 above in combination with Corollary 3.1.2 (?) shows | Querverweis | **Umgesetzt, abweichend:** „Part-III, Corollary 3.1.3“ (Label `cor:c3-1.3` verweist nach Teil III; „Part-III,“ fehlte). Ein 'Corollary 3.1.3' gibt es nicht (3.1.3 ist das Example). Bitte richtiges Ziel prüfen. |
| 107 | ◐ | (use the rescaling procedure Section 1.3.2) | (use the rescaling procedure, see Section 1.3.2) | Grammatik |  |
| 108 | ● | The spectral mapping theorem for the resolvent (Theorem 3.2.5) is well known | (Proposition 3.2.5) | Querverweis | **Umgesetzt.**  |
| 108 | ● | can be found in Kato [16], Chap.III,§ 6.4]. | can be found in Kato [16, Chap. III, § 6.4]. | Satz | **Umgesetzt.** Klammer falsch gesetzt (öffnende eckige Klammer fehlt), Leerzeichen fehlen. |
| 108 | ● | Applications to isolated singularities like Example 3.6 are discussed | like Example 3.3.6 are discussed | Querverweis | **Umgesetzt.** Example 3.6 existiert nicht; gemeint ist Example 3.3.6 (Isolated singularities and poles). |
| 108 | ○ | may be violated in various ways [l.c.,Sec.23.16] | [l.c., Sec. 23.16] | Satz | Fehlende Leerzeichen; ähnlich 'Chap.VII' (S. 108), 'Chap.I' (S. 83), 'Chap.8.1' (S. 93), 'Sec.23.16' (S. 101), 'Sec.8' (S. 108) – uneinheitlich zu 'Chap. III, §6.5'. |
| 108 | ○ | Matrix valued multiplication semigroups appear as solution, via Fourier transformation, of systems | appear as solutions, via Fourier transformation, of systems | Grammatik |  |
| 109 | ◐ | F. Combes & C. Delaroche: Representations des groupes localement compacts | Représentations des groupes localement compacts | Literatur | **Umgesetzt** (in der Bib-Datei, 18./19.10.2026). Akzent fehlt im französischen Titel. |
| 109 | ◐ | G. Greiner: Some applications of Fejer’s theorem to one-parameter semigroups | Some applications of Fejér’s theorem | Literatur | Im Text 'Fejér' mit Akzent. |
| 109 | ◐ | G. Greiner, J. Voigt & M. Wolff: On the spectral bound … J. Operator Theory (1981) 245–256. | J. Operator Theory 5 (1981) 245–256. | Literatur | **Umgesetzt.** Bandnummer fehlt; gleicher Eintrag in Kap. 4, Ref. [10] (S. 132). |
| 109 | ○ | Semesterbericht Funktionalanalysis. Universität Tübingen, 1985 pp. 33–49. | Semesterbericht Funktionalanalysis. Universität Tübingen, 1985, pp. 33–49. | Literatur |  |
| 110 | ◐ | M. P. H. Wolff: “A remark on the spectral bound … Proceedings of the Conference in Oberwolfach 1980”. Functional Analysis and Approximation. … Birkhäuser 1981 pp. 39–50. | M. P. H. Wolff: A remark on the spectral bound … In: Functional Analysis and Approximation (Proc. Conf. Oberwolfach 1980), ed. by P. L. Butzer, B. Sz.-Nagy & E. Görlich. Birkhäuser (1981) 39–50. | Literatur | **Teilweise umgesetzt** (in der Bib-Datei, 18./19.10.2026): Initialen „M. P. H.“; das Format des Eintrags ist offen. Anführungszeichen umschließen Titel samt Tagungsangabe; Format weicht von den übrigen Einträgen ab. Gleicher Eintrag Kap. 4, Ref. [26] (S. 133). |

### Teil I, Kap. 4 – Asymptotics of Semigroups on Banach Spaces

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 114 | ● | for all 𝑓 ∈ 𝐶0(R𝑛); see also Example 3.1.7. | Verweisziel prüfen (z. B. Example 3.2.3/3.2.4) | Querverweis | **Umgesetzt, abweichend:** „Part-II, Example 3.1.7“ (Label `ex:b3-1.7` verweist nach Teil II; „Part-II,“ fehlte). In Abschnitt 3.1 gibt es nur 3.1.1–3.1.4; 'Example 3.1.7' existiert nicht. |
| 114 | ○ | beyond the class of eventually norm-continuous semigroups | eventually norm continuous semigroups | Konsistenz | Kap. 3 schreibt durchgehend 'norm continuous' ohne Bindestrich; Kap. 4 mit (auch S. 121). |
| 114 | ○ | (ii) Note that the condition … (iii) Rescaling this semigroup | (ii) Note that … / (iii) Rescaling … (ohne Einzug) | Satz | Unbeabsichtigter Einzug vor den Aufzählungspunkten (im PDF sichtbar); ähnlich S. 79, 87, 121 ('Due to the difficulty'). |
| 117 | ○ | which implies that 𝑔 ∈ ker(𝐴) = {0} or 𝑔 = 0. | which implies that 𝑔 ∈ ker(𝐴) = {0}, i.e., 𝑔 = 0. | Grammatik | 'or' im Sinne von 'bzw./d.h.' (Germanismus); ähnlich S. 126: 'Therefore, 𝐷 ⊆ 𝐺 or 𝐺 = 𝐸'. |
| 118 | ○ | Proof. (Proof of Theorem 4.1.4) The equality | Proof of Theorem 4.1.4. The equality | Satz | Doppeltes 'Proof'. |
| 119 | ● | Example 4.1.2(c) shows that uniform exponential stability is not equivalent to | Example 4.1.2 (ii) shows | Querverweis | **Umgesetzt.** Example 4.1.2 hat die Teile (i)–(iii); gemeint ist (ii). Ebenso S. 121: 'Example 4.1.2(c) produces a semigroup'. |
| 121 | ● | On the other hand, Example 4.1.2(c) produces a semigroup | Example 4.1.2 (ii) produces a semigroup | Querverweis | **Umgesetzt.**  |
| 121 | ◐ | holomorphic, or nilpotent ones— the spectral mapping theorem | holomorphic, or nilpotent ones—the spectral mapping theorem | Satz | Leerzeichen nach Geviertstrich, davor keins (im PDF sichtbar). |
| 122 | ○ | see Widder [24, p.66]; see also the notes in this section. | see also the notes at the end of this chapter. | Querverweis |  |
| 124 | ○ | By a classical theorem of Laplace transform theory, (for a proof of the vector-valued version one may follow Widder [25, p.196]), we conclude | By a classical theorem of Laplace transform theory (for a proof … Widder [25, p. 196]), we conclude | Satz | Überzähliges Komma vor der Klammer. |
| 125 | ● | The Laplacian Δ generates a bounded holomorphic semigroups on 𝐿𝑝(R𝑛) | generates a bounded holomorphic semigroup on | Tippfehler | **Umgesetzt.**  |
| 125 | ○ | Furthermore the following statements are equivalent, | Furthermore, the following statements are equivalent. | Satz |  |
| 126 | ○ | Therefore, 𝐷 ⊆ 𝐺 or 𝐺 = 𝐸 since 𝐷 is dense in 𝐸. | Therefore, 𝐷 ⊆ 𝐺, and hence 𝐺 = 𝐸 since 𝐷 is dense in 𝐸. | Grammatik |  |
| 127 | ○ | to be weakly stable if … or as weakly uniformly stable if the above holds | to be weakly stable if … or weakly uniformly stable if the above holds | Grammatik |  |
| 128 | ○ | (see Pazy [17, Chapter 4,2.4]) | (see Pazy [17, Chapter 4, 2.4]) | Satz |  |
| 131 | ◐ | Theorem 4.1.3 (ii) is a semigroup version of Theorem 1.2.7 and 1.2.8 in Doetsch [7]. | of Theorems 1.2.7 and 1.2.8 in Doetsch [7]. | Grammatik |  |
| 131 | ○ | was observed by many authors, see for example, Balakrishnan [1, p.178], or Benchimol [2]. | see, for example, Balakrishnan [1, p. 178] or Benchimol [2]. | Satz |  |
| 132 | ◐ | A. Balakrishnan: Applied Functional Analysis. Application of Mathematics. Springer (1976). | A. V. Balakrishnan: Applied Functional Analysis. Applications of Mathematics. Springer (1976). | Literatur | Reihenname lautet 'Applications of Mathematics'. |
| 132 | ◐ | G. Doetsch: Handbuch der Laplace Transformation, Band I. | Handbuch der Laplace-Transformation, Band I. | Literatur |  |
| 132 | ○ | R. Datko: Extending a theorem of A.M. Liapunov to Hilbert space. | Extending a theorem of A. M. Liapunov to Hilbert space. | Literatur |  |
| 132 | ○ | Exponential stability of positive semigroups in a linear topological space I,II. | … in a linear topological space I, II. | Literatur |  |
| 132 | ○ | F. Neubrander: Laplace transform and asymptotic behavior of strongly continuous semigroups. Houston J. Math. 12 (1985) 549–561. | Houston J. Math. 12 (1986) 549–561. | Literatur | **Umgesetzt** (in der Bib-Datei, 18./19.10.2026). Band 12 der Houston J. Math. ist meines Wissens von 1986 – bitte prüfen. |
| 133 | ◐ | M. Slemrod: Asymptotic behavior of 𝐶0-semigroups … Indiana Univ. Math. J. 25 (1976) 783–892. | Indiana Univ. Math. J. 25 (1976) 783–792. | Literatur | **Umgesetzt** (in der Bib-Datei, 18./19.10.2026). Seitenumfang 110 Seiten unplausibel; der Artikel umfasst 783–792. |

### Updated Notes, Part I

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 468 | ● | to the spectral theory of 𝐶0-semigroups, as in Chapter 3.6.6, was started | as in Part-I, Section 3.6.6 | Querverweis | **Umgesetzt, abweichend:** „the proof of Part-I, Theorem 3.6.6“ (einen Abschnitt 3.6.6 gibt es nicht; im Beweis von Theorem 3.6.6 werden über das F-Produkt Näherungseigenvektoren zu Eigenvektoren gemacht). 'Chapter' statt 'Section' |
| 468 | ● | Using this, El-Mennaoui & Engel [30] gives a characterization | El-Mennaoui & Engel [30] give a characterization | Grammatik | **Umgesetzt.**  |
| 469 | ◐ | (i.e., stability of the semigroup induced on an ultra power of the underlying Banach space) | ultrapower | Konsistenz | **Umgesetzt.** Sonst immer 'ultrapower' |
| 470 | ● | Quantative estimates of the decay of the semigroup | Quantitative estimates | Tippfehler | **Umgesetzt.**  |
| 471 | ● | [16] J. Diestel: A survey of results related to the Dunford-Pettis property. ... Contemp. Math. 2, 15-60 (1980). 1980. | ... Contemp. Math. 2 (1980) 15–60. | Literatur | **Umgesetzt.** Jahr doppelt, Format weicht ab, Bindestrich statt Halbgeviertstrich |
| 471 | ○ | [15] R. Derndinger: Über das Spektrum positiver Generatoren. Math. Z. 172 (1980). | Math. Z. 172 (1980) 281–293. | Literatur | **Umgesetzt.** Seitenangaben fehlen (bitte prüfen) |
| 471 | ○ | Institute of Mathematics 2007 pp. 71–109 Available from: | ... 2007 pp. 71–109. Available from: | Literatur | **Umgesetzt.** Punkt fehlt; ebenso bei Groh [13] S. 491 ('C∗-Algebras. 2026 Available from') |

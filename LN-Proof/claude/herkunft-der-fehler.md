# Herkunft der Fehler: Original 1986 oder TeX-Umsetzung?

Stichprobe vom 18.10.2026. 31 Befunde aus den Listen `math-error-part-*.md` und `korrekturen-mathe-part-*.md` wurden am Original (LNM 1184, 1986, Scan `ln-pos-1184.pdf`) nachgeschlagen. Seitenangaben beziehen sich auf das Original.

## Ergebnis

| Herkunft | Anzahl |
|---|---|
| Schon im Original | 18 |
| Bei der TeX-Umsetzung entstanden | 10 |
| Falsche Abschnittsverweise durch Umnummerierung | 2 |
| Neuer Text der 2. Auflage | 1 |

**Muster:** Inhaltliche Fehler stehen fast alle schon im Original. Dazu gehören fehlende Voraussetzungen, falsche Aussagen und Vorzeichenfehler. Bei der Umsetzung kamen Abschreibfehler in Formeln hinzu: verlorene Faktoren oder Exponenten, vertauschte Symbole, falsche Grenzen und Klammern.

## Hochrechnung auf das ganze Buch

Die Beweis-Listen `math-error-part-a…d` enthalten 212 Befunde (94 ●, 56 ◐, 62 ○). Rechnet man ● und ◐ voll und ○ zur Hälfte, ergeben sich **etwa 165 echte mathematische Fehler**. Mit den Anteilen aus der Stichprobe (rund 60 % Original, 30 % Umsetzung, 10 % sonstige) folgt:

| Herkunft | ungefähr |
|---|---|
| Schon in der 1. Auflage | **100** |
| Bei der TeX-Umsetzung entstanden | **50** |
| Umnummerierung, neuer Text | 15 |

Die Unsicherheit liegt bei etwa ±30 %. Die Stichprobe war nicht zufällig: Sie enthält überwiegend ●-Punkte, Teil I ist überrepräsentiert und Teil IV kaum vertreten. Die Übertragungsfehler sind eher unterschätzt, weil nur auffällt, was beim Lesen stört. Die 691 Punkte der Formellisten (überwiegend Satz und Notation) sind nicht eingerechnet.

**Einordnung:** Das sind bei rund 460 Seiten etwa ein Fehler auf vier bis fünf Seiten. Für eine Forschungsmonographie mit mehreren Autoren, 1986 mit der Schreibmaschine gesetzt, ist das ein normaler Wert. Die meisten Fehler sind lokal: eine fehlende Voraussetzung, ein falscher Faktor oder Verweis, ein Vorzeichen. Die Hauptresultate bleiben richtig, und das Buch ist seit Jahrzehnten ein Standardwerk. Die betroffenen Beweise ließen sich jeweils mit kleinen Änderungen reparieren.

## Schon im Original (Auswahl)

- I, Ex. 1.10 (S. 6): „D(B²) = {0}“; B ist nicht abgeschlossen, wenn q Nullstellen hat.
- I, 2.3 (S. 8): sup statt wesentlichem Supremum.
- I, 2.5 (S. 11): Periodizitätsbedingung f(0) = f(1) fehlt bei L^p.
- I, 2.7 (S. 12): (e_n ⊗ e_n)(e_m ⊗ e_m) = δ_{n,m} e_n ⊗ e_n.
- I, 3.3 (S. 15): „λ > ω (see 1.6)“.
- I, 3.4 (S. 18): „0 ≤ s ≤ t₀“.
- I, 3.7 (S. 22 f.): „least cross norm on E × F“; Hilbert-Skalarprodukt „defined as in (ii)“; S und T im Beweis vertauscht.
- II, B-I 3 (i) (S. 120 f.): h ohne Positivität.
- II, Thm. 1.3 (S. 124): „for all f ∈ C₀(X)“.
- II, Cor. 1.17 (S. 131): „f ≫ 0 iff p_u(−f) < 0“; Gl. (1.10) gilt nur für ω₀ ≥ 0.
- II, Ex. 1.22 (S. 133): λ > α + ‖μ‖.
- II, Ex. 2.13 (S. 142): α ≥ 0.
- III, Cor. 3.9 (S. 313): α = 2π/(nτ).
- III, Thm. 3.12 (S. 315): Vorzeichen in (3.15).
- III, Transportgleichung (S. 320): R(λ, A−M) = R(λ,A)(1 − MR(λ,A))⁻¹.
- IV, Lemma 4.3 (S. 420): φ = Σ 2^{−(n+k+1)} ψ_{n,k} ist kein Zustand.

Notationsbefunde wie `E_𝓕^T`, „𝓕-lim sup“ und `f ∈ AC` stammen ebenfalls aus dem Original.

## Bei der TeX-Umsetzung entstanden (Original richtig)

| Stelle | TeX | Original |
|---|---|---|
| I, nach Def. 1.5 (S. 4) | Prop. 1.9 (ii) | Prop. 1.9 (i) |
| I, 2.8 (S. 12) | 1 ≤ p ≤ ∞ | 1 ≤ p < ∞ |
| I, 3.4 (S. 18) | `f_f'` | ξ_f' |
| II, Prop. 1.10 (S. 128) | −u(x)(Af)(x) | −u(x)⁻¹(Af)(x) |
| II, Rem. 1.18 (S. 131) | x + t > 0 | x + t > 1 |
| III, C-I (S. 234) | `\inf \sup_α f_α, h)` | inf(sup_α f_α, h) |
| III, C-II Ex. 1.5 (S. 249) | ∫₀¹ | ∫ₓ¹ |
| III, Thm. 1.2 (S. 293) | ohne Faktor sⁿ | ((λ₀−μ)s)ⁿ |
| III, Prop. 2.6 (S. 299) | (μ−α) | (λ−α) |
| III, Thm. 2.10 (S. 302) | ohne Faktor r | rR₁(r)\|h₁\| |

## Umnummerierung

Im Original beginnt A-I, Abschnitt 3 mit **3.0** (Similar Semigroups), in der 2. Auflage mit 1.3.1. Verweise wie „by 2.4 and 3.2“ oder „3.4 will help“ wurden mit der alten Nummer übernommen und zeigten dadurch auf den Nachbarabschnitt. Beide Fälle sind korrigiert. Alle übrigen 37 Verweise auf I.3.x im Buch stimmen. Weitere Abschnitte „x.0“ gibt es im Original nicht.

## Neuer Text

`1/2` statt s/2 bei den Matrixhalbgruppen (I, 1.2.2): Diese Herleitung steht im Original nicht.

## Folgerung

- Weitere unentdeckte Abschreibfehler in Formeln sind wahrscheinlich, weil sie nur auffallen, wenn sie stören. Für Kap. 2–4 wäre ein Abgleich der abgesetzten Formeln mit dem Original sinnvoll.
- Für das Vorwort (Diskussionspunkt VW-1) genügt ein sachlicher Hinweis, dass neben Druckfehlern auch einige, meist kleinere mathematische Ungenauigkeiten korrigiert wurden.

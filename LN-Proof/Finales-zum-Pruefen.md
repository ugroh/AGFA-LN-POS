# Finales zum Prüfen

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184). Angelegt am 19.10.2026.

Hier stehen Punkte, die vor der Abgabe noch eine Entscheidung oder eine Kontrolle brauchen: bewusste Abweichungen von den Korrekturlisten, Literaturfragen und Konsistenz. Erledigtes bitte abhaken und mit Datum versehen; Einzelheiten zu den umgesetzten Korrekturen stehen in `Umgesetzte_Korrekturen_LNM1184.md`.

## 1. Inhaltlich prüfen (bewusste Entscheidungen im Text)

- [ ] **Teil I, Example 2.1.4:** Die Lösung lautet jetzt u(t) = (f − tBg, g), passend zur Matrix A = (0 −B; 0 0). Offen bleibt der Vorzeichenfehler in Z. 409 (`math-error-part-a`): Er ist dann mit (λf + Bg, λg) zu beheben, **nicht** durch Änderung der Matrix, wie dort vorgeschlagen.
- [ ] **Teil I, Notes zu 2.1 (Pazy):** „Chapter 3, Theorems 4.7 and 4.8“ – ob es Chapter 2 heißen muss, ist offener Punkt in `math-error-part-a` (S. 45, Z. 1047).
- [ ] **Teil II, Beweis des Satzes zu m · A (Z. 820):** Neben m^{l/k} habe ich auch den Laufbereich auf l = 0, …, k−1 geändert (der erste Schritt geht von B = A aus).
- [ ] **Teil II, 0 ≪ u:** An allen Stellen der Liste von `0 \leq u` auf `0 \ll u` geändert. Z. 733 (`0 \leq q \in C(K)`) bewusst nicht, dort genügt q ≥ 0.

## 2. Literatur

- [ ] **lotz:1982** („Uniform convergence of operators on L∞“, Teil I) steht jetzt als „Preprint (1982)“. Die veröffentlichte Fassung Math. Z. 190 (1985) steht als lotz:1985 schon im Verzeichnis. Soll der Preprint bleiben?
- [ ] **Format der Literaturlisten:** Anführungszeichen um Sammelband- und Thesis-Titel, Jahr ohne Klammern und „Vol.“ vor der Bandnummer kommen aus dem biblatex-Stil (`ln-biblatex.sty`) und betreffen alle Einträge. Bisher nicht geändert; ggf. einmal zentral im Stil entscheiden.
- [ ] **Bewusst von zbMATH abweichend belassen (18.10.):** greiner:1982, kato:1973, kipnis:1974, milstein:1975.
- [ ] **Namenspräfixe:** „de Laubenfels“ (Teil II) und „van Casteren“ (Teil III) stehen im Text von Hand vor `\cite`, weil biblatex das Präfix im Zitat weglässt. Falls der Stil auf `useprefix=true` umgestellt wird, diese Stellen anpassen.

## 3. Noch nicht bearbeitet

- [ ] `math-error-part-a/b/c.md`: Kap. 2–4 offen.
- [ ] `korrekturen-text-part-a/b/c.md` und `korrekturen-mathe-part-a/b/c.md`: Kap. 3–4 offen.

## Erledigt

- [x] **Notes-Aufzählung:** in allen Kapiteln mit Abschnitts-Notes jetzt „Section k.1:“ usw. (Kap. 2–4 in Teil I–III, Kap. 3–4 in Teil IV) – 19.10.2026.
- [x] **Lumer [26]/[27]:** in der Bib richtig (25 (1975) 409–446 bzw. 1973); die Fahne beruht auf dem alten Stand und ist durch unser PDF überholt – 19.10.2026.
- [x] **van Casteren (Teil III, Notes zu Kap. 2):** „van Casteren (1984)“ war im Original ein Autor-Jahr-Zitat; jetzt echtes Zitat von vancasteren:1984 (Integral Equations Operator Theory 7 (1984) 884–892), damit steht der Eintrag in der Literaturliste von Teil III, Kap. 2 ([10]). Belegt durch das Literaturverzeichnis der 1. Auflage (`LN-1184/LN-Book/ln-biblio.pdf`, dort Druckfehler „2“ statt 7); Bib-Eintrag aus `LN-1184/LN-References/references-c.bib` (Feb. 2025) – 19.10.2026.
- [x] **Miyajima–Okazawa:** auf die veröffentlichte Fassung umgestellt, Pacific J. Math. 125 (1986) 161–176 – 19.10.2026.
- [x] **Updated Notes, Prüfpunkte:** Edeko–Gerlach–Kühner umformuliert; Domination und Lumer–Phillips-Variante bleiben – 19.10.2026.

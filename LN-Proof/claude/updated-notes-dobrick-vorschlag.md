# Updated Notes Part III, Kap. 3: Soll Dobricks Preprint zur Zyklizität erwähnt werden?

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184), Stand: 17.10.2026.

## Ausgangslage

In den Updated Notes steht zur Zyklizität:

- **Part II, Kap. 3:** „The question whether the boundary spectrum of a positive semigroup is additively cyclic is still open, even on the space $C(K)$.“
- **Part III, Kap. 3:** „The question whether the generator of a positive semigroup on a Banach lattice always has additively cyclic boundary spectrum is still open. […] In the analogous case of a bounded positive operator they are relaxed in [zbmath06591946].“

Am 7.10.2026 erschien der Preprint

> A. Dobrick, *On the cyclicity conjecture*, arXiv:2610.10093 [math.FA].

Er beansprucht einen Beweis der Zyklizitätsvermutung für **einzelne** positive Operatoren auf komplexen Banachverbänden, und zwar ohne zusätzliche Wachstumsbedingungen. Die Arbeit ist noch nicht begutachtet. Laut ihrer eigenen Erklärung entstand sie unter Einsatz von KI-Werkzeugen (OpenAI GPT-5.6).

Die Aussagen der Updated Notes zu **Halbgruppen** bleiben davon unberührt und richtig. Ein Übertrag auf das Randspektrum von Generatoren scheitert am Spektralabbildungssatz; Einzelheiten stehen in der separaten Notiz *Zur Zyklizität: Dobricks Satz und positive Halbgruppen*.

## Empfehlung

Die Arbeit **erwähnen, aber ausdrücklich als ungeprüften Preprint** und in nur einem Satz.

### Gründe dafür

- **Vollständigkeit:** Die Updated Notes sollen den Stand der Forschung wiedergeben. Hält die Arbeit, ist sie für die Zyklizitätsfrage das wichtigste Ergebnis seit Jahrzehnten. Sie gar nicht zu nennen, wäre dann eine sichtbare Lücke, gerade in einem Buch aus der Tübinger Schule, in der das Problem entstanden ist.
- **Kein Risiko bei vorsichtiger Formulierung:** Mit „preprint“ und „announces“ legt man sich inhaltlich nicht fest. Erweist sich die Arbeit als fehlerhaft, schadet eine solche Erwähnung niemandem.
- **Klarstellung zum Halbgruppenfall:** Im selben Satz lässt sich festhalten, dass die Frage für Halbgruppen offen bleibt. Das schützt die Aussagen der Notes.

### Zum Einwand „Nutzung von ChatGPT“

Maßstab sollte die **mathematische Prüfung** sein, nicht das verwendete Werkzeug:

- Dobrick legt die KI-Nutzung offen und übernimmt die Verantwortung für den Inhalt.
- Auch die zweite Auflage de LN wurde unter Mitwirkung einer KI (Claude, Anthropic) korrigiert, und das soll im Vorwort offengelegt werden. Ein Einwand allein wegen der KI-Nutzung wäre deshalb schwer zu vertreten.
- Der **berechtigte** Vorbehalt ist ein anderer: Die Arbeit ist sehr neu und nicht begutachtet.

**Stand der eigenen Prüfung:** Die zentralen Schritte haben sich bei einer ersten Durchsicht als korrekt erwiesen. Das gilt für Theorem 2.3 (Vererbung des peripheren Spektrums unter Domination via Vesentini) und für den Schluss $r(S_n) = 1$ in Proposition 3.4. Die Anhänge (Torsionsoperatoren, Lotz' Satz) wurden nicht im Detail nachgerechnet.

### Vorschlag zum Vorgehen

Rainer steht in der Danksagung der Arbeit („detailed feedback on an early draft“) und kann die Belastbarkeit des Ergebnisses vermutlich am besten einschätzen. Laut Danksagung hat auch Jochen Glück eine frühere Fassung gelesen.

## Textvorschlag

**Ort:** `part-e/un-part-c.tex`, Updated Notes Part III, Chapter 3, im Absatz zur Zyklizität, direkt nach dem Satz
„In the analogous case of a bounded positive operator they are relaxed in \textcite{zbmath06591946}.“

**Einzufügender Text:**

```latex
For a single positive operator on a complex Banach lattice, a recent preprint by
\textcite{dobrick:2026} announces a proof that the peripheral spectrum is always
cyclic, without any additional growth assumptions.
This does not settle the question for the boundary spectrum of generators of
positive semigroups, since the spectral mapping theorem may fail.
```

**Bib-Eintrag** (für `bib/ln-references-EN.bib`):

```bibtex
@Misc{dobrick:2026,
  author = {Dobrick, Alexander},
  title  = {On the cyclicity conjecture},
  year   = {2026},
  note   = {Preprint, arXiv:2610.10093 [math.FA]}
}
```

## Alternativen

1. **Nicht erwähnen:** Die Notes bleiben wie sie sind. Das ist vertretbar, solange die Arbeit nicht begutachtet ist, wirkt aber später womöglich unvollständig.
2. **Nur in Part II, Kap. 3 einen Verweis ergänzen:** Hinter „see also the updated notes to Part-III, Chapter 3“ ist inhaltlich nichts weiter nötig, wenn der Satz in Part III steht.
3. **Erwähnung wie vorgeschlagen** (Empfehlung).

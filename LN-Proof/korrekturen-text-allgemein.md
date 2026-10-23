# Fahnenkorrektur (Text): Übergreifende Punkte und Index

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184), Proof-PDF vom 14.10.2026.

Auszug aus `Fahnenkorrektur_Springer_LNM1184.md`. **Seitenangaben** = gedruckte Seitenzahl (PDF-Seite = gedruckte Seite + 18). **Sicherheit:** ● hoch · ◐ mittel · ○ niedrig.

**Stand der Umsetzung (Branch `fahnenkorrektur`):** Diese Liste enthält keine ●-Punkte. Von den beiden Index-Einträgen ist der ○-Punkt (S. 495) umgesetzt, der ◐-Punkt (S. 494, Kato) ist offen. Bei den übergreifenden Punkten A.1–A.8 und den Bib-Fragen steht der Stand jeweils in der Zeile selbst. Stand 23.10.2026.

**Buchführung:** Maßgeblich für den Korrekturstand sind nur die Listen `korrekturen-text-*`, `korrekturen-mathe-*` und `math-error-*` (seit 20.10.2026). `Umgesetzte_Korrekturen_LNM1184.md`, `Finales-zum-Pruefen.md` und `Fahnenkorrektur_Springer_LNM1184.md` werden nicht mehr fortgeführt.

Insgesamt **2 Punkte**: 0 ●, 1 ◐, 1 ○; davon umgesetzt: 1.



## A. Übergreifende Punkte

1. **Einleitungsseiten der Teile (S. 2, 136, 264, 408):** Die Bezeichnung „Part A–D“ ist gewollt. Diese Seiten sind aber in einer anderen Schrift gesetzt (Computer Modern statt Times). Falls das nicht beabsichtigt ist, bitte an Springer melden.
2. **Inhaltsverzeichnis (S. xi–xiv): Umgesetzt** (Stand 23.10.2026, im Quelltext geprüft). „Uniformly Ergodic Semig**o**ups“ → „Semig**r**oups“ (Teil IV, 3.2; gleicher Fehler in Überschrift und Kolumnentitel S. 432–436). „Basic Results **of** Spaces C₀(X)“ → „**on**“ (Teil II, Kap. 1; auch Kolumnentitel).
3. **Kolumnentitel:** Teil I, Kap. 1 heißt im Kolumnentitel „Basic Results on Banach Spaces“ (Kapiteltitel: „… on Semigroups on Banach Spaces“) — als Kurztitel vertretbar, **offen**, ob das so bleiben soll (`\chaptermark` in `part-a/chap-a1.tex`, Z. 8). Teil IV, Kap. 3 („W∗-algebras“ klein): **umgesetzt**, der Kolumnentitel schreibt jetzt „\WA-Algebras“ (`part-d/chap-d3.tex`, Z. 6). Kurztitel sonst konsistent.
4. **„Part-I“ im Fließtext:** Die Bindestrich-Form ist gewollt. Gelistet sind nur Stellen, an denen sie fehlt (S. 174, zweimal).

   > **Merkposten (entschieden: Variante 1, umgesetzt):** Im Fließtext steht 357-mal „Part-I/II/III/IV“ mit Bindestrich. Ohne Bindestrich steht es nur auf S. 174 (zweimal: „Part I, Proposition 1.1.9“, „Part I, Corollary 2.1.33“). Kolumnentitel, Teil-Titelseiten, Inhaltsverzeichnis und „Updated Notes Part I–IV“ schreiben dagegen ohne Bindestrich.
   > - **Variante 1:** So lassen, nur S. 174 an „Part-I“ angleichen.
   > - **Variante 2:** Überall „Part I“ ohne Bindestrich (im Englischen üblich, passt zu Titelei und Kolumnentiteln). Das geht nur als Sammelanweisung an Springer: „im gesamten Text ‚Part-I‘ → ‚Part I‘ usw.“
5. **Britische Schreibweise** nur vereinzelt in den Updated Notes (S. 480: characterise, generalisation), sonst amerikanisch. „behaviour“ kommt nur in Literaturtiteln vor, das ist okay.
6. **Einheitlichkeit:** „quasi-compactness“ / „quasicompactness“ (S. 380), „well defined“ / „well-defined“, „Markov-operator“ / „Markov operator“ u. Ä. Siehe die Einzelpunkte unten (Kategorie „Konsistenz“).
7. **Literatur:** Alle Zitate [n] haben einen Eintrag im jeweiligen Literaturverzeichnis, und jeder Eintrag wird zitiert (automatisch geprüft). Unten aufgeführt sind nur inhaltliche Zuordnungsfehler und Formatfragen.
8. **Keine Author Queries** im PDF gefunden. Falls Springer eine separate AQ-Liste geschickt hat, bitte nachreichen.

### Literaturverzeichnisse (Bib-Dateien)

Beide Bib-Dateien unter `LN-Book-Springer/bib/` sind am 18./19.10.2026 mit zbMATH Open abgeglichen und bereinigt (Einzelliste im Archiv `Umgesetzte_Korrekturen_LNM1184.md`). Greiner/Voigt/Wolff (J. Operator Theory) hat jetzt Band 5; das wirkt in allen Kapiteln.

Stand der Entscheidungen:

- **Format der Literaturlisten:** **Umgesetzt** (21.10.2026, Entscheidung U. Groh) in `preamble/ln-biblatex.sty`: Bei Sammelbandbeiträgen, Tagungsbeiträgen, Berichten, Hochschulschriften und Preprints jetzt wie bei Artikeln und Büchern Titel kursiv ohne Anführungszeichen, Jahr in Klammern, kein „Vol.“, kein „pp.“, kein Komma vor dem Jahr (z. B. „Universität Tübingen (1985) 33–49“).
- **Bewusst von zbMATH abweichend belassen:** greiner:1982 **bestätigt** (U. Groh, 22.10.2026); kato:1973 auf Jahr **1972** geändert (U. Groh, 22.10.2026; Schlüssel unverändert); kipnis:1974 auf Jahr **1975** geändert (U. Groh, 23.10.2026; Schlüssel unverändert): im Zweifel gilt zbMATH, Numdam führt den Jahrgang als 1974.
- **Offen — milstein:1975:** `journal = {Soviet Math.}` ist die englische Übersetzung, `pages = {35--42, 51--61}` sind die Seiten der russischen Ausgabe. Vorerst unverändert (U. Groh, 23.10.2026); abschließende Klärung durch **W. Arendt**.
- **Namenspräfixe:** „de Laubenfels“ (Teil II) und „van Casteren“ (Teil III) stehen im Text von Hand vor `\cite`, weil biblatex das Präfix im Zitat weglässt. Falls der Stil auf `useprefix=true` umgestellt wird, diese Stellen anpassen.
- **lotz:1982:** steht als „Preprint (1982)“; die veröffentlichte Fassung steht als lotz:1985 schon im Verzeichnis (siehe `korrekturen-text-part-a.md`, S. 70).

### Index

| S. | | Ist | Soll | Art | Kommentar |
|---|---|---|---|---|---|
| 494 | ◐ | Kato’s equality, 157–161, 317, 318, 360 | prüfen | Begriff | **Kein Tippfehler, mathematisch zu klären** (23.10.2026): Im Text kommen beide Begriffe vor, „Kato’s equality“ 18-mal und „Kato’s inequality“ 27-mal. Der Index führt nur `\index{Kato's equality}` (Teil II, Kap. 2 zweimal als Bereich; Teil III, Kap. 2 zweimal, Kap. 3 einmal). Zu entscheiden: ein gemeinsamer Eintrag oder zwei getrennte. |
| 495 | ○ | F-Product semigroup, 25 | F-product semigroup, 25 | Konsistenz | **Umgesetzt** (23.10.2026, Entscheidung U. Groh). Eine einzige Stelle: `part-a/chap-a1.tex`, Z. 1433, `\index{standard construction!fprod@$\mathcal{F}$-Product semigroup}`. Alle übrigen Einträge schreiben „product“ klein. Sortierschlüssel `fprod` bleibt unverändert. |

---
*Hinweis:* Die Liste beruht auf dem aus dem PDF extrahierten Text. Verdächtige Stellen (zusammengeklebte Wörter, Trennungen) wurden am PDF-Bild gegengeprüft. Formeln wurden bewusst ausgelassen.

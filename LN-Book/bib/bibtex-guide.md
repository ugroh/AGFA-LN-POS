# Umfassende Anleitung zu BibTeX und natbib

## 1. Grundlagen von BibTeX

BibTeX ist ein Literaturverwaltungssystem für LaTeX, das die Verwaltung von Bibliografien und Zitaten vereinfacht. 

### 1.1 Die BibTeX-Datei (.bib)

Eine BibTeX-Datei (mit der Endung .bib) enthält alle Literatureinträge in folgendem Format:

```bibtex
@article{einstein1905,
  author  = {Einstein, Albert},
  title   = {Zur Elektrodynamik bewegter K{\"o}rper},
  journal = {Annalen der Physik},
  year    = {1905},
  volume  = {322},
  number  = {10},
  pages   = {891--921}
}

@book{latexcompanion,
  author    = {Goossens, Michel and Mittelbach, Frank and Samarin, Alexander},
  title     = {The \LaTeX\ Companion},
  publisher = {Addison-Wesley},
  year      = {1994}
}
```

### 1.2 Wichtige Eintragstypen

- `@article`: Für Zeitschriftenartikel
- `@book`: Für Bücher
- `@inproceedings`: Für Konferenzbeiträge
- `@phdthesis`: Für Dissertationen
- `@techreport`: Für technische Berichte
- `@misc`: Für sonstige Quellen

## 2. Integration in LaTeX

### 2.1 Grundlegende Einbindung

Im LaTeX-Dokument müssen Sie folgende Zeilen im Präambel-Bereich einfügen:

```latex
\usepackage[options]{natbib}
\bibliographystyle{plainnat}  % oder ein anderer Stil
```

Am Ende des Dokuments vor `\end{document}`:

```latex
\bibliography{ihre_bibliographie}  % ohne .bib-Endung
```

### 2.2 Compilation-Prozess

Um die Bibliografie korrekt zu erstellen, müssen Sie folgende Befehle in dieser Reihenfolge ausführen:

1. `pdflatex ihr_dokument`
2. `bibtex ihr_dokument`
3. `pdflatex ihr_dokument`
4. `pdflatex ihr_dokument`

## 3. Das natbib-Paket

### 3.1 Wichtige Zitierbefehle

- `\cite{key}`: Standard-Zitation
- `\citet{key}`: Textzitat (Name als Teil des Textes)
- `\citep{key}`: Klammerzitat
- `\citeauthor{key}`: Nur Autorname
- `\citeyear{key}`: Nur Jahr

Beispiele:
```latex
\citet{einstein1905} → "Einstein (1905)"
\citep{einstein1905} → "(Einstein, 1905)"
\citep[S. 42]{einstein1905} → "(Einstein, 1905, S. 42)"
```

### 3.2 natbib-Optionen

Im Präambel können verschiedene Optionen gesetzt werden:

```latex
\usepackage[
  round,       % runde Klammern
  authoryear,  % Autor-Jahr-Zitierweise
  sort        % Sortierung mehrerer Zitate
]{natbib}
```

### 3.3 Bibliografiestile

Gängige Stile für natbib:
- `plainnat`: Standard-Stil
- `abbrvnat`: Gekürzte Vornamen
- `unsrtnat`: Unsortierte Bibliografie
- `apanat`: APA-Stil

## 4. Tipps und Best Practices

1. **Konsistente Schlüssel**: Verwenden Sie ein einheitliches Schema für BibTeX-Schlüssel, z.B.:
   - `autor1999`: Erstautor + Jahr
   - `autor_et_al_1999`: Bei mehreren Autoren

2. **Sonderzeichen**:
   - Umlaute in geschweiften Klammern: `{\"a}` für ä
   - Titel in geschweiften Klammern schützen: `title = {{Ein Titel mit Großbuchstaben}}`

3. **Fehlervermeidung**:
   - Überprüfen Sie die .bib-Datei auf fehlende Pflichtfelder
   - Achten Sie auf korrekte Klammerung
   - Verwenden Sie keine Umlaute direkt in der .bib-Datei

4. **Organisation**:
   - Kommentieren Sie komplexe Einträge
   - Gruppieren Sie ähnliche Einträge
   - Führen Sie eine separate Liste der verwendeten Schlüssel

## 5. Häufige Probleme und Lösungen

### 5.1 Fehlende Zitate
Problem: Zitate erscheinen als [?]
Lösung: 
- Überprüfen Sie die Schreibweise des Schlüssels
- Führen Sie BibTeX und LaTeX mehrmals aus

### 5.2 Falsche Sortierung
Problem: Zitate erscheinen in falscher Reihenfolge
Lösung:
- Verwenden Sie die Option `sort` in natbib
- Überprüfen Sie die Datumsangaben in der .bib-Datei

### 5.3 Formatierungsprobleme
Problem: Unerwünschte Großbuchstaben im Titel
Lösung:
- Titel in zusätzliche geschweifte Klammern setzen
- BibTeX-Stil überprüfen
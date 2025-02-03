# LaTeX Guide: Kapitelweise Bibliographien mit BibTeX und chapterbib

## Inhaltsverzeichnis
- [1. Grundkonfiguration](#1-grundkonfiguration)
- [2. Kapitelweise Bibliographien](#2-kapitelweise-bibliographien)
- [3. Zusätzliche Literaturliste](#3-zusätzliche-literaturliste)
- [4. Build-Skript](#4-build-skript)
- [5. Typische Probleme und Lösungen](#5-typische-probleme-und-lösungen)

## 1. Grundkonfiguration

### Hauptdokument (LN-Book.tex)
```latex
\usepackage{chapterbib}
\usepackage[round,authoryear]{natbib}
```

### Kapitel-Dateien
Jedes Kapitel braucht am Ende:
```latex
\bibliographystyle{plainnat}
\bibliography{../bib/ln-references}  % Pfad relativ zum Kapitel
```

## 2. Kapitelweise Bibliographien

### Verzeichnisstruktur
```
.
├── LN-Book.tex
├── bib
│   └── ln-references.bib
├── part-a
│   ├── chap-a1.tex
│   └── ...
└── ...
```

### Label-Konventionen
Verwenden Sie eindeutige Präfixe:
- Theoreme: `\label{thm:a1-1.2}`
- Gleichungen: `\label{eq:a1-1.4}`
- Definitionen: `\label{def:a1-1.3}`

## 3. Zusätzliche Literaturliste

### Separate TeX-Datei (additional.tex)
```latex
\documentclass{article}
\usepackage[round,authoryear]{natbib}
\begin{document}
\nocite{*}
\bibliographystyle{plainnat}
\bibliography{bib/ln-additional}
\end{document}
```

### Einbindung im Hauptdokument
```latex
\chapter*{Weiterführende Literatur}
\input{additional.bbl}
```

## 4. Build-Skript

### Installation
```zsh
# Skript ausführbar machen
chmod +x build.zsh
```

### Verwendung
```zsh
./build.zsh build              # Kompiliert alles
./build.zsh build-additional   # Nur additional.bbl neu erzeugen
./build.zsh clean             # Aufräumen
./build.zsh watch             # Automatische Kompilierung
```

### Build-Reihenfolge
1. additional.bbl erzeugen
2. Hauptdokument erste Kompilierung
3. BibTeX für jedes Kapitel
4. Hauptdokument zweite und dritte Kompilierung

## 5. Typische Probleme und Lösungen

### Mehrfach definierte Labels
```
LaTeX Warning: Label `eq:a1-1.4' multiply defined.
```
- In .log Datei suchen: `grep "multiply defined" LN-Book.log`
- Labels im Kapitel finden: `grep -r "eq:a1-1.4" part-a/chap-a1.tex`

### Undefinierte Referenzen
```
LaTeX Warning: There were undefined references.
```
- Meist behoben durch erneute Kompilierung
- In .log Datei suchen: `grep "Reference.*undefined" LN-Book.log`

### Undefinierte Zitate
```
Package natbib Warning: Citation `autor2023' undefined
```
- In .log Datei suchen: `grep "Citation.*undefined" LN-Book.log`
- BibTeX-Eintrag prüfen: `grep -A 10 "autor2023" bib/ln-references.bib`

### Debugging-Tipps
1. .log Datei ist die beste Quelle für Fehlermeldungen
2. Bei Zitierproblemen:
   - Pfade zu .bib Dateien prüfen
   - Auf exakte Schreibweise der Keys achten
   - .aux und .bbl Dateien bei Bedarf löschen
3. Bei Label-Problemen:
   - Eindeutige Präfixe verwenden
   - Kontext mit grep -A und -B zeigen

## Alternative: bibunits
Wenn mehr Flexibilität benötigt wird:
```latex
\usepackage{bibunits}
\usepackage[round,authoryear]{natbib}
\defaultbibliographystyle{plainnat}
\defaultbibliography{references}

\begin{bibunit}
\chapter{Kapitel}
Text...
\putbib
\end{bibunit}
```

### Vorteile chapterbib vs. bibunits
- chapterbib:
  - Einfacher bei Datei-basierter Struktur
  - Weniger Markup im Text
  - Gut für Bücher mit klarer Kapitelstruktur
- bibunits:
  - Flexiblere Platzierung der Bibliographien
  - Verschiedene Stile möglich
  - Funktioniert mit \input
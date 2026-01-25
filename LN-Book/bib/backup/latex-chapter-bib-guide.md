# BibTeX Guide für Kapitelweise Bibliographien

## Inhaltsverzeichnis
- [Einführung](#einführung)
- [Grundlegende Struktur](#grundlegende-struktur)
- [Vollständiges Beispiel](#vollständiges-beispiel)
- [Kompilierung](#kompilierung)
- [Häufige Probleme](#häufige-probleme)

## Einführung

Dieses Dokument erklärt, wie man BibTeX mit kapitelweisen Bibliographien in einem LaTeX-Buch verwendet. Dies ist besonders nützlich für:
- Dissertationen
- Technische Berichte
- Bücher mit unterschiedlichen thematischen Schwerpunkten pro Kapitel

## Grundlegende Struktur

Für kapitelweise Bibliographien benötigen Sie:

1. Das chapterbib-Paket
2. Separate Tex-Dateien für jedes Kapitel
3. Eine oder mehrere BibTeX-Dateien
4. Eine Hauptdatei, die alles zusammenführt

### Pakete im Hauptdokument

```latex
\usepackage{chapterbib}
\usepackage[round,authoryear]{natbib}
```

## Vollständiges Beispiel

### Hauptdatei (main.tex)

```latex
\documentclass[a4paper,11pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[german]{babel}
\usepackage{chapterbib}
\usepackage[round,authoryear]{natbib}

\title{Beispielbuch mit kapitelweisen Bibliographien}
\author{Max Mustermann}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\include{kapitel1}
\include{kapitel2}

\end{document}
```

### Erstes Kapitel (kapitel1.tex)

```latex
\chapter{Grundlagen der Quantenmechanik}

\section{Einführung}
Die Entwicklung der Quantenmechanik begann mit Plancks Arbeiten 
zur Schwarzkörperstrahlung \citep{planck1901}. 
Einstein entwickelte diese Ideen weiter \citep{einstein1905} 
und führte das Konzept des Photons ein.

\section{Mathematische Grundlagen}
Die Schrödinger-Gleichung \citep{schroedinger1926} bildet das 
mathematische Fundament der Quantenmechanik.

\bibliographystyle{plainnat}
\bibliography{qm_literatur}
```

### Zweites Kapitel (kapitel2.tex)

```latex
\chapter{Moderne Anwendungen}

\section{Quantencomputing}
Die Grundlagen des Quantencomputings wurden von 
Feynman gelegt \citep{feynman1982}.

\section{Quantenkryptographie}
Das BB84-Protokoll \citep{bennett1984} war der erste 
praktische Vorschlag für Quantenkryptographie.

\bibliographystyle{plainnat}
\bibliography{modern_literatur}
```

### Bibliographie für Kapitel 1 (qm_literatur.bib)

```bibtex
@article{planck1901,
  author  = {Planck, Max},
  title   = {{\"U}ber das Gesetz der Energieverteilung im Normalspektrum},
  journal = {Annalen der Physik},
  volume  = {309},
  number  = {3},
  pages   = {553--563},
  year    = {1901}
}

@article{einstein1905,
  author  = {Einstein, Albert},
  title   = {{\"U}ber einen die Erzeugung und Verwandlung des Lichtes 
             betreffenden heuristischen Gesichtspunkt},
  journal = {Annalen der Physik},
  volume  = {322},
  number  = {6},
  pages   = {132--148},
  year    = {1905}
}

@article{schroedinger1926,
  author  = {Schr{\"o}dinger, Erwin},
  title   = {Quantisierung als Eigenwertproblem},
  journal = {Annalen der Physik},
  volume  = {384},
  number  = {4},
  pages   = {361--376},
  year    = {1926}
}
```

### Bibliographie für Kapitel 2 (modern_literatur.bib)

```bibtex
@article{feynman1982,
  author  = {Feynman, Richard P.},
  title   = {Simulating Physics with Computers},
  journal = {International Journal of Theoretical Physics},
  volume  = {21},
  number  = {6/7},
  pages   = {467--488},
  year    = {1982}
}

@article{bennett1984,
  author  = {Bennett, Charles H. and Brassard, Gilles},
  title   = {Quantum Cryptography: Public Key Distribution and Coin Tossing},
  journal = {Proceedings of IEEE International Conference on Computers, 
             Systems and Signal Processing},
  pages   = {175--179},
  year    = {1984}
}
```

## Kompilierung

### Makefile

```makefile
all: thesis

thesis:
	pdflatex main
	bibtex kapitel1
	bibtex kapitel2
	pdflatex main
	pdflatex main

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.pdf
```

### Manuelle Kompilierung

Wenn Sie keinen Makefile verwenden möchten, führen Sie diese Befehle der Reihe nach aus:

```bash
pdflatex main
bibtex kapitel1
bibtex kapitel2
pdflatex main
pdflatex main
```

## Häufige Probleme

### Problem: Zitate erscheinen als [?]
- **Ursache**: BibTeX wurde nicht für jedes Kapitel ausgeführt
- **Lösung**: Führen Sie `bibtex` für jedes Kapitel aus

### Problem: Bibliographie erscheint nicht am Kapitelende
- **Ursache**: Fehlendes `\bibliography{...}` am Kapitelende
- **Lösung**: Fügen Sie `\bibliography{ihre_bib_datei}` am Ende jedes Kapitels ein

### Problem: Falsche Sortierung der Referenzen
- **Ursache**: Natbib-Optionen nicht korrekt gesetzt
- **Lösung**: Überprüfen Sie die Optionen im `\usepackage[options]{natbib}` Befehl

### Problem: Umlaute werden nicht korrekt angezeigt
- **Ursache**: Falsche Kodierung oder fehlende Pakete
- **Lösung**: 
  1. Stellen Sie sicher, dass `inputenc` und `fontenc` geladen sind
  2. Verwenden Sie `{\"a}` für ä, `{\"u}` für ü, etc.
  3. Speichern Sie alle Dateien in UTF-8
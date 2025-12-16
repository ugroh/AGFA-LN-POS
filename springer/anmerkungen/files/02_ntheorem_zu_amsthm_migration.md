# Migration: ntheorem → amsthm/thmtools

**Für:** Springer Lecture Notes Projekt  
**Ziel:** Ersatz veralteter ntheorem (2011) durch modernes amsthm + thmtools  
**Aufwand:** Moderat (hauptsächlich in LN-Book.tex)

---

## Teil 1: Grundkonzepte verstehen

### Was macht ntheorem?
```latex
\usepackage[thmmarks,thref]{ntheorem}
\theoremstyle{nonumberplain}
\theoremheaderfont{\bfseries\itshape}
\theorembodyfont{\upshape}
\theoremsymbol{\ensuremath{\square}}
\newtheorem{proof}{Proof}
```

Das definiert:
- Theorem-Stile (Header, Body, Symbole)
- Custom Theorem-Umgebungen
- Markierungen und Referenzen

### Was macht amsthm + thmtools?
- **amsthm:** Basis-Theorem-System (seit 1990er, aktiv gepflegt)
- **thmtools:** Modernes Frontend für amsthm (mehr Features, cleaner API)

---

## Teil 2: Installation prüfen

**Prüfung in Ihrer TeX-Installation:**
```bash
tlmgr search --file "amsthm.sty"
tlmgr search --file "thmtools.sty"
```

**Falls nicht vorhanden:**
```bash
tlmgr install amsthm thmtools
```

Beide sollten in modernem TeX Live enthalten sein.

---

## Teil 3: Schritt-für-Schritt Migration

### Schritt 1: ntheorem entfernen, amsthm + thmtools hinzufügen

**ALT (in svmono.cls, Zeile 2038):**
```latex
\usepackage[thmmarks,thref]{ntheorem}
\theoremstyle{nonumberplain}
\theoremheaderfont{\bfseries\itshape}
\theorembodyfont{\upshape}
\theoremsymbol{\ensuremath{\square}}
\newtheorem{proof}{Proof}
```

**NEU (in LN-Book.tex, nach `\documentclass{svmono}`):**
```latex
\usepackage{amsthm}
\usepackage{thmtools}

% Proof-Umgebung mit Square
\usepackage{amssymb}  % für \square
\renewcommand\qedsymbol{\ensuremath{\square}}
\theoremstyle{plain}
\newtheorem*{proof}{Proof}
```

### Schritt 2: Ihre Theorem-Definitionen anpassen

**ALT (LN-Book.tex, Zeilen 25–37):**
```latex
\spnewtheorem{remarks}[theorem]{Remarks}{\normalfont\bfseries}{\normalfont}
\spnewtheorem{examples}[theorem]{Examples}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{example*}{Example}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{examples*}{Examples}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{remark*}{Remark}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{remarks*}{Remark}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{definition*}{Definition}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{theorem*}{Theorem}{\normalfont\bfseries}{\itshape}
\spnewtheorem*{proposition*}{Proposition}{\normalfont\bfseries}{\itshape}
\spnewtheorem*{lemma*}{Lemma}{\normalfont\bfseries}{\itshape}
\spnewtheorem*{corollary*}{Corollary}{\normalfont\bfseries}{\itshape}
```

**NEU (mit thmtools):**
```latex
% Stil für numerierte Theoreme (mit Counter)
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{definition}[theorem]{Definition}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}

% Stil für Remarks/Examples (in Upshape)
\theoremstyle{definition}
\newtheorem{remarks}[theorem]{Remarks}
\newtheorem{examples}[theorem]{Examples}

% Nicht-numerierte Versionen (mit *)
\theoremstyle{plain}
\newtheorem*{theorem*}{Theorem}
\newtheorem*{proposition*}{Proposition}
\newtheorem*{lemma*}{Lemma}
\newtheorem*{corollary*}{Corollary}

\theoremstyle{definition}
\newtheorem*{definition*}{Definition}
\newtheorem*{example*}{Example}
\newtheorem*{examples*}{Examples}
\newtheorem*{remark*}{Remark}
\newtheorem*{remarks*}{Remarks}
```

**Erklärung der Stile:**
- `plain` – Standard (Header bold + italic, Body italic) → für Theoreme
- `definition` – Alt (Header bold, Body normal) → für Definitionen, Remarks
- `remark` – Alt (Header italic, Body normal)

### Schritt 3: Counter-Verwaltung anpassen

**ALT (LN-Book.tex, Zeilen 55–65):**
```latex
\makeatletter
\let\c@definition=\c@theorem
\let\c@example=\c@theorem
\let\c@examples=\c@theorem
\let\c@lemma=\c@theorem
\let\c@corollary=\c@theorem
\let\c@proposition=\c@theorem
\let\c@remark=\c@theorem
\let\c@remarks=\c@theorem
\makeatother
```

**NEU (viel simpler mit thmtools):**
```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{definition}[theorem]{Definition}  % teilt Counter mit theorem
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{remarks}[theorem]{Remarks}
\newtheorem{examples}[theorem]{Examples}
% Das `[theorem]` nach der Umgebung teilt den Counter!
```

**Das ist viel cleaner.** Sie brauchen die `\makeatletter`-Tricks nicht mehr.

### Schritt 4: Nummerierung definieren

**ALT (LN-Book.tex, Zeilen 41–49):**
```latex
\renewcommand\thetheorem{\thesection.\arabic{theorem}}
\renewcommand\theproposition{\thesection.\arabic{proposition}}
\renewcommand\thedefinition{\thesection.\arabic{definition}}
\renewcommand\thelemma{\thesection.\arabic{lemma}}
\renewcommand\thecorollary{\thesection.\arabic{corollary}}
\renewcommand\theremark{\thesection.\arabic{remark}}
\renewcommand\theremarks{\thesection.\arabic{remarks}}
\renewcommand\theexample{\thesection.\arabic{example}}
\renewcommand\theexamples{\thesection.\arabic{examples}}
```

**NEU (da alle Counter geteilt sind):**
```latex
\renewcommand\thetheorem{\thesection.\arabic{theorem}}
% Das reicht! Alle anderen erben automatisch.
```

Viel simpler!

---

## Teil 5: Vollständiges neues Theorem-Setup

Ersetzen Sie die Zeilen 25–65 in LN-Book.tex durch:

```latex
%% ========================================
%% THEOREM ENVIRONMENTS mit amsthm + thmtools
%% ========================================

\usepackage{amsthm}
\usepackage{thmtools}
\usepackage{amssymb}

% QED-Symbol (weißes Quadrat)
\renewcommand\qedsymbol{\ensuremath{\square}}

%% ---- NUMERIERTE THEOREME ----
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remarks}[theorem]{Remarks}
\newtheorem{examples}[theorem]{Examples}

%% ---- NICHT-NUMERIERTE VERSIONEN ----
\theoremstyle{plain}
\newtheorem*{theorem*}{Theorem}
\newtheorem*{proposition*}{Proposition}
\newtheorem*{lemma*}{Lemma}
\newtheorem*{corollary*}{Corollary}

\theoremstyle{definition}
\newtheorem*{definition*}{Definition}
\newtheorem*{remark*}{Remark}
\newtheorem*{remarks*}{Remarks}
\newtheorem*{example*}{Example}
\newtheorem*{examples*}{Examples}

%% ---- PROOF (bereits in amsthm enthalten) ----
% \begin{proof} ... \end{proof}
% funktioniert automatisch mit \qedsymbol

%% ---- NUMMERIERUNG ----
\renewcommand\thetheorem{\thesection.\arabic{theorem}}

%% ---- EQUATIONS ----
\counterwithin{equation}{section}
```

Fertig! Das ersetzt die kompletten Zeilen 25–65.

---

## Teil 6: Testen und Validieren

### Minimales Test-Beispiel

```latex
\documentclass[graybox]{svmono}
\usepackage{amsthm}
\usepackage{thmtools}
\usepackage{amssymb}

\renewcommand\qedsymbol{\ensuremath{\square}}
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem*{theorem*}{Theorem*}

\begin{document}

\section{Test}

\begin{theorem}
Das ist ein Theorem mit Nummer.
\end{theorem}

\begin{theorem*}
Das ist ein Theorem ohne Nummer.
\end{theorem*}

\begin{proof}
Beweis mit QED-Symbol.
\end{proof}

\end{document}
```

**Kompilieren:**
```bash
pdflatex test.tex
```

Falls es funktioniert, können Sie zum vollständigen Dokument übergehen.

---

## Teil 7: Mögliche Probleme und Lösungen

### Problem 1: Unterschiedliche Formatierung in Headern

**ntheorem:**
```latex
\theoremheaderfont{\bfseries\itshape}
```

**amsthm:**
```latex
\theoremstyle{plain}      % Header ist automatisch bold+italic
\theoremstyle{definition} % Header ist automatisch bold
```

**Lösung:** Sie können Custom-Stile mit thmtools definieren:
```latex
\declaretheorem[
  style=definition,
  name=Remark,
  sibling=theorem
]{remark}
```

### Problem 2: Markierungen (thmmarks)

**ntheorem hatte:**
```latex
\usepackage[thmmarks]{ntheorem}
```

**In amsthm/thmtools:** Das funktioniert standardmäßig über `\qedsymbol`

Falls Sie spezielle Markierungen für verschiedene Umgebungen brauchen:
```latex
% Custom QED für Remarks
\newenvironment{remarks}
  {\begin{remarksinner}\renewcommand\qedsymbol{$\diamond$}}
  {\end{remarksinner}}
\newtheorem*{remarksinner}{Remarks}
```

### Problem 3: thref-Option

**ntheorem hatte:**
```latex
\usepackage[..., thref]{ntheorem}
```

**In amsthm:** Nicht nötig, Referenzen funktionieren standardmäßig

---

## Teil 8: Checkliste für die Migration

- [ ] `amsthm` und `thmtools` installieren
- [ ] ntheorem-Zeilen aus svmono.cls entfernen
- [ ] Neues Theorem-Setup (Schritt 5) in LN-Book.tex einfügen
- [ ] Alte Theorem-Definitionen (Zeilen 25–65) löschen
- [ ] Alte Counter-Verwaltung (Zeilen 55–65) löschen
- [ ] Test-Kompilierung durchführen
- [ ] Alle 16 Kapitel überprüfen auf Theorem-Rendering
- [ ] Bibliography und Index nochmal testen
- [ ] Finale PDF überprüfen (PDF-Größe sollte ähnlich sein)

---

## Teil 9: Fallback-Strategie

Falls die Migration zu schwierig wird:

**Option A: ntheorem manuell installieren**
```bash
# Wenn Sie TeX Live haben, aber ntheorem fehlt:
tlmgr install ntheorem
```

**Option B: ntheorem lokal verpacken**
```bash
# ntheorem.sty + ntheorem.cfg zusammen mit Ihren Dateien committen
./texmf/tex/latex/ntheorem/ntheorem.sty
./texmf/tex/latex/ntheorem/ntheorem.cfg
```

Dann Straive fragen, diese Dateien zu verwenden.

**Option C: Hybrid-Ansatz**
- Keep svmono.cls mit ntheorem (für Kompatibilität)
- In LN-Book.tex zusätzliche Theorem-Umgebungen mit amsthm definieren
- Funktioniert, ist aber nicht elegant

---

## Zusammenfassung

**Aufwand:** ~30 Minuten  
**Risiko:** Gering (alle Änderungen sind lokal in LN-Book.tex)  
**Gewinn:** 
- Moderne, gepflegte Packages
- Kompatibilität mit TeX Live 2024+
- Simpler Code ohne `\makeatletter` Tricks

Die Migration ist **sehr straight-forward** und empfohlen!

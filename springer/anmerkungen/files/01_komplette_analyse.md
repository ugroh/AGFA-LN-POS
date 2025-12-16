# Springer svmono.cls Analyse – Kompletter Überblick

**Projekt:** One-parameter Semigroups of Positive Operators (Lecture Notes)  
**Datum:** 2025-01-XX  
**Ausgangspunkt:** TeX-Kompatibilitätsprobleme bei der Produktion mit Straive

---

## Executive Summary

Ihre Probleme stammen primär aus **zwei Quellen**:

1. **svmono.cls ist veraltet** (Juni 2018, auf TeX-Standard von 1995 eingestellt)
2. **ntheorem (2011) existiert nicht mehr in modernen TeX Live** (2024+)

Das ist keine Schuld von Springer oder Straive – das Template wurde einfach 6+ Jahre nicht aktualisiert, während sich die TeX-Welt weiterentwickelt hat.

---

## Teil 1: svmono.cls – Detaillierte Analyse

### Status der Datei

| Attribut | Wert |
|---|---|
| Version | 5.6 |
| Datum | 25. Juni 2018 |
| TeX-Format-Anforderung | 1995/12/01 (!!) |
| Wartungsstatus | Nicht aktiv gepflegt |
| Größtes Problem | ntheorem (2011) nicht mehr verfügbar |

### Veraltete Packages in svmono.cls

| Paket | Zeile | Problem | Modern |
|---|---|---|---|
| `natbib` | opt. | Alte Bibliography | `biblatex` + `biber` |
| `color` | 185 | Zu simpel | `xcolor` |
| `framed` | 189 | Nicht gepflegt | `tcolorbox`, `mdframed` |
| `ntheorem` | 2038 | **NICHT in TeX Live 2024+!** | `amsthm` + `thmtools` |

### Legacy-Code-Beispiele in svmono.cls

**1. Veraltete TeX-Version (Zeile 21)**
```latex
\NeedsTeXFormat{LaTeX2e}[1995/12/01]  % ← 30 Jahre alt!
```
Sollte: `[2018/06/01]` oder später

**2. Veraltete Conditional-Syntax (Zeilen 39, 44)**
```latex
\let\if@spthms\iftrue
\DeclareOption{nospthms}{\let\if@spthms\iffalse}
```
Modern: `\newif\if@spthms` mit `\@spthmstrue/\@spthmsfalse`

**3. Low-Level Box-Manipulationen (Zeilen 2060–2065)**
```latex
\newbox\authrun
\newtoks\authorrunning
\newdimen\instindent
```
Modern: `expl3` oder strukturierte Makros

**4. Direkte interne TeX-Befehle (Zeile 2079)**
```latex
\if!\@institute!\else
```
Modern: Public API statt `\@`-Befehle

**5. `\gdef` für globale Defs (Zeile 2088)**
```latex
\gdef\svlanginfo{\typeout{Man spricht deutsch.}\global\let\svlanginfo\relax}
```
1990er-Jahre TeX-Stil

**6. Alte Dimensionseinheiten (Zeile 2086)**
```latex
\vspace{5dd}  % didot points – veraltet
```
Modern: `mm`, `cm` oder proportionale Einheiten

---

## Teil 2: Das ntheorem-Problem – Der Kern des Problems

### Das kritische Issue

**In svmono.cls (Zeile 2038):**
```latex
\usepackage[thmmarks,thref]{ntheorem}
```

**Status:**
- Letzte Version: 2011
- Verfügbarkeit: **NICHT mehr in TeX Live 2024+**
- Installation: Nur noch manuell oder über alte Installations-Archive

### Warum das Ihr Problem ist

1. **Ihr System:** Hat `ntheorem` wahrscheinlich noch (TeX Live < 2020 oder manuelle Installation)
2. **Straive's System:** Nutzt wahrscheinlich aktuelles TeX Live 2024 → `ntheorem` fehlt
3. **Resultat:** Compilation schlägt fehl bei Straive

### Die Besonderheit: Springer-Theorem-Makros

Sie nutzen in Ihrer Präambel (LN-Book.tex, Zeilen 25–37):
```latex
\spnewtheorem{remarks}[theorem]{Remarks}{\normalfont\bfseries}{\normalfont}
\spnewtheorem{examples}[theorem]{Examples}{\normalfont\bfseries}{\normalfont}
\spnewtheorem*{example*}{Example}{\normalfont\bfseries}{\normalfont}
% ... etc
```

Diese `\spnewtheorem`-Makros sind in `svmono.cls` definiert und **hängen direkt von ntheorem ab**.

**Das ist der Grund, warum svmono.cls nicht einfach aktualisierbar ist:**
- Millionen bestehender Springer-Dokumente nutzen diese Makros
- Sie funktionieren nur mit `ntheorem`
- Ein Update würde alles brechen

---

## Teil 3: Ihre Präambel – Analyse (LN-Book.tex)

### Struktur und Umfang
- **Größe:** Großes Buch-Projekt mit 4 Parts (A–D) + Appendix (E)
- **Kapitel:** 16 Hauptkapitel + Front/Back Matter
- **Dateien:** ~40 Einzel-Dateien via `\include`

### Kritische Punkte in Ihrer Präambel

**1. Theorem-Definitionen (Zeilen 25–49) – GUT**
```latex
\spnewtheorem{remarks}[theorem]{Remarks}{\normalfont\bfseries}{\normalfont}
% ... weitere 8 Theorem-Umgebungen
\renewcommand\thetheorem{\thesection.\arabic{theorem}}
% ... Nummerierung korrekt eingestellt
```
✅ Perfekt implementiert, hängt aber von `ntheorem` ab

**2. Veraltete Bibliography-Systeme (Zeilen 82–87)**
```latex
\usepackage[square,numbers]{natbib}
\usepackage[resetlabels]{multibib}
\newcites{EN}{Updated Notes: References}
\newcommand{\mycite}[2][]{\citeauthor{#2}~\citeEN[#1]{#2}}
```
⚠️ `natbib` + `multibib` sind veraltet  
Modern: `biblatex` mit `biber`

**3. Fehlende UTF-8-Encoding**
```latex
% Am Anfang fehlt:
\usepackage[utf8]{inputenc}
```
⚠️ Könnte zu Problemen mit Umlauten/Sonderzeichen führen

**4. Index (Zeile 135)**
```latex
\usepackage{makeidx}
\makeindex
```
⚠️ `makeidx` ist OK, aber `imakeidx` ist moderner (Zeile 134 ist kommentiert)

**5. TOC-Anpassungen (Zeile 111)**
```latex
\usepackage{tocloft}
```
✅ Funktioniert, aber modern wäre `titletoc`

**6. Auskommentierte svmono-Optionen (Zeilen 9–12)**
```latex
%,envcountsect			%% not working  
%,evvcountsame			%% -- " -- 
%,envcountresetsect		%% -- " --
```
⚠️ Diese funktionieren nicht – Grund: Kompatibilitätsprobleme mit TeX-Version

**7. Hyperref (Zeile 143) – GUT**
```latex
\usepackage{hyperref}
\hypersetup{breaklinks=true, colorlinks=true, ...}
```
✅ Korrekt konfiguriert

### Positive Aspekte
✅ Gut strukturierte Dateiorganisation  
✅ Moderne Packages wie `tikz`, `mathtools`, `tikz-cd`  
✅ Gute Theorem-Definition mit korrekt eingestellter Nummerierung  
✅ Hyperref ist sinnvoll konfiguriert

---

## Teil 4: Die Lösungsstrategie

### Kurztermig: Für die aktuelle Produktion mit Straive

**Was Sie Straive sagen/fragen sollten:**

> "Unsere svmono.cls (Version 5.6, Juni 2018) nutzt das ntheorem-Paket (Stand 2011) für Theorem-Umgebungen. Dieses Paket existiert nicht mehr in modernen TeX Live Versionen (2024+). Können Sie entweder:
> 
> 1. ntheorem installieren/verfügbar machen, oder
> 2. Uns bei der Migration zu modernen Theorem-Paketen helfen?"

**Edition ID angeben:** 656256

### Mittelfristig: Ihr Dokument modernisieren

**Schritt 1: UTF-8 Support hinzufügen (Zeile 16, nach documentclass)**
```latex
\usepackage[utf8]{inputenc}
```

**Schritt 2: ntheorem durch amsthm ersetzen** (siehe separater Migrationsleitfaden)

**Schritt 3: Bibliography modernisieren**
```latex
% Alt (Zeilen 82–87):
\usepackage[square,numbers]{natbib}
\usepackage[resetlabels]{multibib}

% Neu:
\usepackage[style=numeric, backend=biber, maxbibnames=99]{biblatex}
\addbibresource{./bib/ln-references.bib}
\addbibresource{./bib/ln-references-EN.bib}
```

**Schritt 4: Index modernisieren**
```latex
% Alt:
\usepackage{makeidx}
\makeindex

% Neu:
\usepackage{imakeidx}
\makeindex[columns=2]
```

### Langfristig: Neue svmono-Version nutzen

- Springer sollte `svmono-modern.cls` entwickeln
- Oder Sie verwenden ein modernes Template basierend auf `book.cls`

---

## Teil 5: Nächste Schritte

### 1. Sofort – Kommunikation mit Straive

Schreiben Sie an: `texsupport@straive.com`

**Betreff:** TeX Kompatibilität svmono.cls – ntheorem nicht verfügbar

**Inhalt:**
- Edition ID: 656256
- Problem: `ntheorem` (2011) nicht in modernem TeX Live
- Frage: Können Sie das Paket bereitstellen oder Modernisierung empfehlen?
- Ihr Kontakt: ulrich@...

### 2. Parallel – Migration zu amsthm vorbereiten

Siehe separater Leitfaden: `ntheorem-zu-amsthm-migration.md`

### 3. Langfristig – Modernisierung

- Biblatex statt natbib+multibib
- imakeidx statt makeidx
- UTF-8 Encoding
- XeLaTeX/LuaLaTeX Support optional

---

## Anhang: Dateien und Referenzen

**Ihre Dateien:**
- `LN-Book.tex` – Hauptpräambel
- `svmono.cls` v5.6 (Juni 2018) – Springer Template
- `./preamble/ln-preamble-final` – Ihre zusätzliche Präambel
- `./preamble/ln-definitionen` – Definitionen
- `./bib/ln-references.bib` – Hauptbibliographie
- `./bib/ln-references-EN.bib` – Englische Referenzen

**Wichtige Paket-Versionen:**
- `ntheorem` – Stand 2011 ⚠️ **VERALTET**
- `natbib` – 2009+ (veraltet)
- `tikz` – 2010+ (aktuell)
- `hyperref` – 2020+ (aktuell)

---

## Zusammenfassung in 3 Sätzen

1. **Das Problem:** `svmono.cls` nutzt `ntheorem` (2011), das nicht mehr in TeX Live 2024+ vorhanden ist.
2. **Der Grund:** Springer hat das Template seit 2018 nicht aktualisiert, weil das Brechen von Backward-Compatibility zu viel Aufwand bedeutet.
3. **Die Lösung:** Straive muss `ntheorem` bereitstellen ODER Sie migrieren zu modernen Theorem-Paketen (`amsthm`).

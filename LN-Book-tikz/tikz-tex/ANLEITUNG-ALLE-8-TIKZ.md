# T3-Fonts entfernen – Alle 8 tikz-Grafiken

## Übersicht der Dateien

```
tikz-chap-a1-a-standalone.tex
tikz-chap-a1-b-standalone.tex
tikz-chap-a2-standalone.tex
tikz-chap-a4-standalone.tex
tikz-chap-b3-standalone.tex
tikz-chap-c3-a-standalone.tex
tikz-chap-c3-b-standalone.tex
tikz-chap-d3-standalone.tex
```

## Schritt 1: Alle mit LuaLaTeX compilieren

Lege alle `-standalone.tex` Dateien in ein Verzeichnis und führe aus:

```bash
for file in tikz-*-standalone.tex; do
  lualatex "$file"
done
```

Das erzeugt für jede Datei eine entsprechende `.pdf` (ohne T3-Fonts!).

## Schritt 2: T3-Fonts überprüfen (optional)

```bash
pdffonts tikz-chap-a1-a-standalone.pdf | grep -i "T3\|Type 3"
```

Sollte **keine Treffer** geben ✓

## Schritt 3: Im Monograph einbinden

**Statt** (erzeugt T3-Fonts):
```latex
\input{tikz-chap-a1-a}
\input{tikz-chap-a1-b}
% etc...
```

**Nutze** (T3-frei):
```latex
\includegraphics[width=0.8\textwidth]{tikz-chap-a1-a-standalone.pdf}
\includegraphics[width=0.8\textwidth]{tikz-chap-a1-b-standalone.pdf}
% etc...
```

## Optional: Automatische Konvertierung

Falls du weitere tikz-Dateien hast, nutze das `convert_tikz.py` Skript:

```bash
python3 convert_tikz.py
```

Das konvertiert alle `tikz-*.tex` (ohne `-standalone`) automatisch.

---

**Nach diesen Schritten sollte dein Monograph T3-frei sein!** 🎉

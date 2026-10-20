#!/bin/bash
# Erzeugt aus den md-Korrekturlisten in LN-Proof die LaTeX-Fassungen mit gesetzten Formeln.
# Aufruf (aus beliebigem Verzeichnis):   LN-Proof/tex/tools/make-tex.sh
# Benötigt: python3, pdflatex (TeX Live mit newtx, wasysym, zi4).
set -e
cd "$(dirname "$0")/.."            # -> LN-Proof/tex
export KORR_OUT=.
MD="../math-error-part-?.md ../korrekturen-mathe-part-?.md"
python3 tools/md2tex.py collect $MD          # Formel-Kandidaten sammeln
python3 tools/testfrags.py 0 >/dev/null      # Probesatz jedes Kandidaten
python3 tools/testfrags.py 1 >/dev/null      # Ersatzkandidaten
python3 tools/testfrags.py 2 >/dev/null      # Text mit eingestreuten Formeln; Rest bleibt Quelltext
python3 tools/finalize.py chosen.json $MD    # .tex schreiben und übersetzen
rm -rf .probe *.aux *.out *.log fragments.json chosen.json

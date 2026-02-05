#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konvertiert alle tikz-*.tex Dateien zu Standalone-Format
"""
import os
import glob

# LaTeX-Header für Standalone
HEADER = r"""\documentclass[tikz,border=5pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,matrix}

\begin{document}
"""

FOOTER = r"""\end{document}
"""

# Finde alle tikz-*.tex Dateien
tikz_files = glob.glob("tikz-*.tex")
tikz_files.sort()

if not tikz_files:
    print("Keine tikz-*.tex Dateien gefunden!")
    exit(1)

print(f"Gefundene {len(tikz_files)} tikz-Dateien:\n")

for tikz_file in tikz_files:
    # Lese Original-Datei
    with open(tikz_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Erstelle Standalone-Datei
    standalone_name = tikz_file.replace('.tex', '-standalone.tex')
    standalone_content = HEADER + content + FOOTER
    
    with open(standalone_name, 'w', encoding='utf-8') as f:
        f.write(standalone_content)
    
    print(f"✓ {tikz_file:30} → {standalone_name}")

print(f"\n✓ {len(tikz_files)} Standalone-Dateien erstellt!")
print("\nNächster Schritt: Alle mit lualatex compilieren:")
print("\n  for file in tikz-*-standalone.tex; do lualatex \"$file\"; done")

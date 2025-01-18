#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def text_to_tex(input_path, output_path):
    """
    Konvertiert eine Textdatei in eine LaTeX-Datei
    """
    print(f"Verarbeite Textdatei: {input_path}")
    
    try:
        # Text einlesen
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Text eingelesen. Starte Konvertierung...")
        
        # Mathematische Symbole ersetzen
        replacements = {
            'ℝ': '\\mathbb{R}',
            'ℕ': '\\mathbb{N}',
            'φ': '\\phi',
            'ϕ': '\\phi',
            '≤': '\\leq',
            '≥': '\\geq',
            '∈': '\\in',
            '∗': '*',
            '→': '\\to',
            '∅': '\\emptyset',
            'σ': '\\sigma',
            'α': '\\alpha',
            'μ': '\\mu',
            'λ': '\\lambda'
        }
        
        for old, new in replacements.items():
            if old in content:
                print(f"Ersetze {old} mit {new}")
            content = content.replace(old, new)
        
        # LaTeX-Dokument erstellen
        latex_content = """\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{amsthm}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}

\\begin{document}

%s

\\end{document}
""" % content

        # In Datei speichern
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"LaTeX-Datei wurde erstellt: {output_path}")
        
    except Exception as e:
        print(f"Fehler bei der Verarbeitung: {str(e)}")

if __name__ == "__main__":
    # Feste Pfade für den Test
    text_file = "test.txt"  # Ihre Textdatei
    tex_file = "test.tex"   # Ausgabe-LaTeX-Datei
    
    text_to_tex(text_file, tex_file)

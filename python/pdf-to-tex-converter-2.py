#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdfplumber
import re
import os
import sys

def extract_text_from_pdf(pdf_path):
    """
    Extrahiert Text aus einer PDF-Datei und behält mathematische Notation bei
    """
    print(f"Starte Extraktion von: {pdf_path}")
    text_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"PDF geöffnet. Anzahl Seiten: {len(pdf.pages)}")
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"Verarbeite Seite {page_num}")
                text = page.extract_text()
                if text:
                    text_content.append(text)
                else:
                    print(f"Warnung: Keine Text auf Seite {page_num} gefunden")
    except Exception as e:
        print(f"Fehler bei der PDF-Extraktion: {str(e)}")
        raise
    
    combined_text = '\n'.join(text_content)
    print(f"Extrahierter Text (ersten 200 Zeichen):\n{combined_text[:200]}")
    return combined_text

def convert_to_tex_commands(text):
    """
    Konvertiert mathematische Ausdrücke in LaTeX-Befehle
    """
    print("Starte Konvertierung zu LaTeX")
    
    # Mathematische Symbole ersetzen
    replacements = {
        'ℝ': '\\mathbb{R}',
        'ℕ': '\\mathbb{N}',
        'φ': '\\phi',
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
    
    # Text in LaTeX-Format umwandeln
    tex_text = text
    
    # Mathematische Symbole ersetzen
    for old, new in replacements.items():
        if old in tex_text:
            print(f"Ersetze Symbol: {old} -> {new}")
        tex_text = tex_text.replace(old, new)
    
    # Inline-Mathematik markieren
    tex_text = re.sub(r'(\w+)_(\w+)', r'$\1_\2$', tex_text)  # Subscripts
    tex_text = re.sub(r'(\w+)\^(\w+)', r'$\1^\2$', tex_text)  # Superscripts
    
    print(f"Konvertierter Text (ersten 200 Zeichen):\n{tex_text[:200]}")
    return tex_text

def create_tex_document(tex_content):
    """
    Erstellt ein vollständiges LaTeX-Dokument mit Standard-Header
    """
    print("Erstelle LaTeX-Dokument")
    template = """\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{amsthm}

\\begin{document}

%s

\\end{document}
""".strip() % tex_content
    
    print("LaTeX-Dokument erstellt")
    return template

def main(pdf_path):
    """
    Hauptfunktion zur Verarbeitung einer einzelnen PDF-Datei
    """
    print(f"\nStarte Verarbeitung von: {pdf_path}")
    
    # Erstelle den Output-Pfad im gleichen Verzeichnis wie die PDF
    directory = os.path.dirname(os.path.abspath(pdf_path))
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(directory, filename + '.tex')
    
    print(f"Output wird gespeichert als: {output_path}")
    
    # Text aus PDF extrahieren
    raw_text = extract_text_from_pdf(pdf_path)
    
    if not raw_text.strip():
        print("Warnung: Kein Text extrahiert!")
        return
    
    # Text in LaTeX-Befehle umwandeln
    tex_content = convert_to_tex_commands(raw_text)
    
    # Vollständiges LaTeX-Dokument erstellen
    full_doc = create_tex_document(tex_content)
    
    # In Datei speichern
    print(f"Speichere LaTeX in: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_doc)
    
    print(f"LaTeX-Datei erfolgreich erstellt: {output_path}")

def process_directory(directory="."):
    """
    Verarbeitet alle PDF-Dateien im angegebenen Verzeichnis
    """
    print(f"Suche nach PDF-Dateien in: {directory}")
    # Alle PDF-Dateien im Verzeichnis finden
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"Keine PDF-Dateien im Verzeichnis {directory} gefunden.")
        return
    
    print(f"Gefundene PDF-Dateien: {len(pdf_files)}")
    print("Dateien:", pdf_files)
    
    # Jede PDF-Datei verarbeiten
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        print(f"\nVerarbeite: {pdf_file}")
        try:
            main(pdf_path)
        except Exception as e:
            print(f"Fehler bei der Verarbeitung von {pdf_file}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Wenn ein Argument übergeben wurde, verwende es als Verzeichnispfad
        directory = sys.argv[1]
    else:
        # Sonst verwende das aktuelle Verzeichnis
        directory = "."
    
    print(f"Starte Programm mit Verzeichnis: {directory}")
    process_directory(directory)

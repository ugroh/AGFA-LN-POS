#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_in_directory():
    # Schritt 1: Suche nach PDF-Dokumenten im aktuellen Verzeichnis
    pdf_files = glob.glob('*.pdf')
    
    # Wenn kein PDF gefunden wird, werfe eine Fehlermeldung
    if not pdf_files:
        raise FileNotFoundError("Kein PDF-Dokument im aktuellen Verzeichnis gefunden!")
    
    # Nimm das erste PDF (falls mehrere vorhanden)
    pdf_path = pdf_files[0]
    print(f"Gefundenes PDF: {pdf_path}")
    
    # Schritt 2: PDF in Einzelseiten zerlegen
    reader = PdfReader(pdf_path)
    
    # Basis-Dateiname ohne Erweiterung
    base_filename = os.path.splitext(pdf_path)[0]
    
    # Schritt 3: Einzelseiten speichern
    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        
        # Speichere jede Seite als separate Datei
        output_filename = f"{base_filename}_{page_num + 1}.pdf"
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)
        
        print(f"Seite {page_num + 1} gespeichert als {output_filename}")

if __name__ == "__main__":
    try:
        split_pdf_in_directory()
        print("PDF erfolgreich in Einzelseiten zerlegt!")
    except Exception as e:
        print(f"Fehler: {e}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def pdf_to_text(pdf_path, output_path):
    """
    Konvertiert eine gescannte PDF-Datei in Text mittels OCR
    """
    print(f"Verarbeite PDF: {pdf_path}")
    
    try:
        # PDF öffnen
        doc = fitz.open(pdf_path)
        print(f"PDF geöffnet. Anzahl Seiten: {len(doc)}")
        
        text_content = []
        for page_num, page in enumerate(doc, 1):
            print(f"Verarbeite Seite {page_num}")
            
            # Seite als Bild rendern
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x Zoom für bessere OCR
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # OCR durchführen
            print(f"Führe OCR für Seite {page_num} durch...")
            text = pytesseract.image_to_string(img, lang='eng+deu')  # eng+deu für Englisch und Deutsch
            
            if text.strip():
                print(f"Text wurde auf Seite {page_num} gefunden")
                text_content.append(f"--- Seite {page_num} ---\n{text}\n")
            else:
                print(f"WARNUNG: Kein Text auf Seite {page_num} gefunden")
        
        doc.close()
        
        if not text_content:
            print("FEHLER: Kein Text in der gesamten PDF gefunden!")
            return
        
        # Text in Datei speichern
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_content))
        
        print(f"Text wurde gespeichert in: {output_path}")
        
    except Exception as e:
        print(f"Fehler bei der Verarbeitung: {str(e)}")

if __name__ == "__main__":
    # Feste Pfade für den Test
    pdf_file = "test.pdf"
    text_file = "test.txt"
    
    pdf_to_text(pdf_file, text_file)

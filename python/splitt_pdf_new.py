# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
from PyPDF2 import PdfReader, PdfWriter


def split_pdf_in_directory():
    pdf_files = glob.glob('*.pdf')

    if not pdf_files:
        raise FileNotFoundError("Kein PDF-Dokument im aktuellen Verzeichnis gefunden!")

    pdf_path = pdf_files[0]
    print(f"Gefundenes PDF: {pdf_path}")

    reader = PdfReader(pdf_path)
    base_filename = os.path.splitext(pdf_path)[0]

    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])

        output_filename = f"{base_filename.lower()}_{str(page_num + 1).zfill(2)}.pdf"
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)

        print(f"Seite {page_num + 1} gespeichert als {output_filename}")


if __name__ == "__main__":
    try:
        split_pdf_in_directory()
        print("PDF erfolgreich in Einzelseiten zerlegt!")
    except Exception as e:
        print(f"Fehler: {e}")

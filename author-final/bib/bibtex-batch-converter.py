#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-


import re
from typing import List, Dict
import os

class BibTeXBatchConverter:
    def __init__(self):
        self.journal_names = {
            "Bull. Amer. Math. Soc.": "Bulletin of the American Mathematical Society",
            "Pacific J. Math.": "Pacific Journal of Mathematics",
            "J. Math. Soc. Japan": "Journal of the Mathematical Society of Japan",
            "Ann. Mat. Pura Appl.": "Annali di Matematica Pura ed Applicata",
            "Hiroshima Math. J.": "Hiroshima Mathematical Journal",
            "J. Funct. Anal.": "Journal of Functional Analysis",
            "SIAM Rev.": "SIAM Review",
            "Israel J. Math.": "Israel Journal of Mathematics"
        }

    def split_references(self, text: str) -> List[str]:
        """Split a text into individual references based on author patterns."""
        # Pattern für Autorenzeilen (Nachname, Vorname oder Initialen)
        author_pattern = r'(?m)^[A-Z][a-zäöüß]+(?:,\s*[A-Z]\.(?:\s*[A-Z]\.)*)?\s*$'
        
        # Finde alle Matches
        splits = list(re.finditer(author_pattern, text))
        references = []
        
        # Extrahiere die Referenzen
        for i in range(len(splits)):
            start = splits[i].start()
            end = splits[i + 1].start() if i + 1 < len(splits) else len(text)
            references.append(text[start:end].strip())
        
        return references

    def parse_reference(self, text: str) -> Dict:
        """Parse a single reference into components."""
        ref = {}
        
        # Extract authors
        first_line = text.split('\n')[0].strip()
        ref['author'] = first_line
        
        # Extract year and title
        year_match = re.search(r'\[(\d{4})(?:[a-z])?\]', text)
        if year_match:
            ref['year'] = year_match.group(1)
            # Look for title after the year
            after_year = text[year_match.end():].strip()
            title_end = after_year.find('.')
            if title_end != -1:
                ref['title'] = after_year[:title_end].strip()

        # Look for journal information
        journal_pattern = r'([^\.]+)\s+(\d+)\s*\((\d{4})\)\s*,\s*(\d+[-]\d+)'
        journal_match = re.search(journal_pattern, text)
        
        if journal_match:
            ref['type'] = 'article'
            ref['journal'] = journal_match.group(1).strip()
            ref['volume'] = journal_match.group(2)
            ref['pages'] = journal_match.group(4)
        else:
            # Check if it's a book
            publisher_match = re.search(r':\s*([^\.]+)\.?\s*(\d{4})', text)
            if publisher_match:
                ref['type'] = 'book'
                pub_info = publisher_match.group(1).strip()
                ref['publisher'] = pub_info.split()[0]
                ref['address'] = ' '.join(pub_info.split()[1:])
        
        return ref

    def generate_citation_key(self, ref: Dict, text: str) -> str:
        """Generate a citation key from reference data."""
        # Get first author's last name
        author = ref['author'].split(',')[0].split(';')[0].strip()
        year = ref['year']
        
        # Check for multiple papers in same year
        year_letter_match = re.search(r'\[(\d{4})([a-z])\]', text)
        if year_letter_match:
            year = f"{year}{year_letter_match.group(2)}"
        
        return f"{author}{year}"

    def to_bibtex(self, ref: Dict, citation_key: str) -> str:
        """Convert parsed reference to BibTeX format."""
        entry_type = ref.get('type', 'article')
        lines = [f"@{entry_type}{{{citation_key},"]
        
        # Format authors
        if 'author' in ref:
            authors = ref['author'].replace(';', ' and')
            lines.append(f"  author    = {{{authors}}},")
        
        # Add title
        if 'title' in ref:
            lines.append(f"  title     = {{{ref['title']}}},")
        
        # Add type-specific fields
        if entry_type == 'article':
            if 'journal' in ref:
                journal = self.journal_names.get(ref['journal'], ref['journal'])
                lines.append(f"  journal   = {{{journal}}},")
            if 'volume' in ref:
                lines.append(f"  volume    = {{{ref['volume']}}},")
            if 'pages' in ref:
                lines.append(f"  pages     = {{{ref['pages']}}},")
        elif entry_type == 'book':
            if 'publisher' in ref:
                lines.append(f"  publisher = {{{ref['publisher']}}},")
            if 'address' in ref:
                lines.append(f"  address   = {{{ref['address']}}},")
        
        # Add year
        if 'year' in ref:
            lines.append(f"  year      = {{{ref['year']}}}")
        
        lines.append("}")
        return '\n'.join(lines)

    def convert_file(self, input_file: str, output_file: str):
        """Convert a file containing multiple references to BibTeX format."""
        try:
            # Lese die Eingabedatei
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Teile in einzelne Referenzen
            references = self.split_references(content)
            
            # Öffne die Ausgabedatei
            with open(output_file, 'w', encoding='utf-8') as f:
                for ref_text in references:
                    if ref_text.strip():  # Ignoriere leere Referenzen
                        try:
                            # Verarbeite jede Referenz
                            parsed_ref = self.parse_reference(ref_text)
                            citation_key = self.generate_citation_key(parsed_ref, ref_text)
                            bibtex = self.to_bibtex(parsed_ref, citation_key)
                            
                            # Schreibe in die Ausgabedatei
                            f.write(bibtex + '\n\n')
                        except Exception as e:
                            print(f"Fehler bei der Verarbeitung der Referenz:\n{ref_text}\nFehler: {e}\n")
                            continue

            print(f"Konvertierung abgeschlossen. Ausgabe in: {output_file}")
            
        except Exception as e:
            print(f"Fehler beim Verarbeiten der Datei: {e}")

# Beispielverwendung
if __name__ == "__main__":
    converter = BibTeXBatchConverter()
    
    # Beispiel für die Verwendung
    input_file = "references.txt"  # Ihre Eingabedatei
    output_file = "references.bib" # Die zu erstellende BibTeX-Datei
    
    if os.path.exists(input_file):
        converter.convert_file(input_file, output_file)
    else:
        print(f"Die Eingabedatei {input_file} wurde nicht gefunden.")
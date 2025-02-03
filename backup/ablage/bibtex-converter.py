import re
from typing import Dict, List, Optional

class BibTeXConverter:
    def __init__(self):
        # Dictionary of common journal abbreviations and their full names
        self.journal_names = {
            "Bull. Amer. Math. Soc.": "Bulletin of the American Mathematical Society",
            "Pacific J. Math.": "Pacific Journal of Mathematics",
            "J. Math. Soc. Japan": "Journal of the Mathematical Society of Japan",
            "Ann. Mat. Pura Appl.": "Annali di Matematica Pura ed Applicata",
            "Hiroshima Math. J.": "Hiroshima Mathematical Journal",
            # Add more journal mappings as needed
        }

    def parse_reference(self, text: str) -> Dict:
        """Parse a reference text into components."""
        # Initialize empty reference
        ref = {}
        
        # Try to extract authors and year first
        lines = text.strip().split('\n')
        
        # First line typically contains authors
        if lines:
            ref['author'] = lines[0].strip().rstrip('.')
        
        # Look for year in square brackets
        year_match = re.search(r'\[(\d{4})(?:[a-z])?\]', text)
        if year_match:
            ref['year'] = year_match.group(1)
        
        # Try to extract title - usually after year until the next period
        title_match = re.search(r'\]\s*(.*?)\s*\.\s*', text)
        if title_match:
            ref['title'] = title_match.group(1).strip()
        
        # Try to extract journal and other details
        journal_match = re.search(r'\.\s*([\w\s\.]+)\s*(\d+)\s*\((\d{4})\)\s*,\s*(\d+[-]\d+)', text)
        if journal_match:
            journal, volume, year, pages = journal_match.groups()
            ref['journal'] = journal.strip()
            ref['volume'] = volume
            ref['pages'] = pages
        
        # Check if it's a book
        if 'journal' not in ref and ':' in text:
            # Extract publisher info
            pub_info = text.split(':')[-1].strip()
            ref['publisher'] = pub_info.split()[0]
            ref['address'] = ' '.join(pub_info.split()[1:]).rstrip('.')
            ref['type'] = 'book'
        else:
            ref['type'] = 'article'
            
        return ref

    def generate_citation_key(self, ref: Dict) -> str:
        """Generate a citation key from reference data."""
        authors = ref['author'].split(',')[0].split()[-1]  # Get last name of first author
        year = ref['year']
        
        # Add a letter if there are multiple papers by same author in same year
        if 'a' in text or 'b' in text:
            year_letter = re.search(r'\[(\d{4})([a-z])', text)
            if year_letter:
                year = f"{year}{year_letter.group(2)}"
                
        return f"{authors}{year}"

    def to_bibtex(self, text: str) -> str:
        """Convert a reference text to BibTeX format."""
        ref = self.parse_reference(text)
        citation_key = self.generate_citation_key(text)
        
        # Determine entry type
        entry_type = ref.get('type', 'article')
        
        # Start building BibTeX entry
        bibtex = [f"@{entry_type}{{{citation_key},"]
        
        # Add authors
        if 'author' in ref:
            authors = ref['author']
            # Replace 'and' with 'and' for BibTeX
            authors = authors.replace(';', ' and')
            bibtex.append(f"  author  = {{{authors}}},")
            
        # Add title
        if 'title' in ref:
            title = ref['title']
            # Capitalize important words in title
            bibtex.append(f"  title   = {{{title}}},")
            
        # Add journal/publisher specific fields
        if entry_type == 'article':
            if 'journal' in ref:
                # Use full journal name if available
                journal = self.journal_names.get(ref['journal'], ref['journal'])
                bibtex.append(f"  journal = {{{journal}}},")
            if 'volume' in ref:
                bibtex.append(f"  volume  = {{{ref['volume']}}},")
        else:
            if 'publisher' in ref:
                bibtex.append(f"  publisher = {{{ref['publisher']}}},")
            if 'address' in ref:
                bibtex.append(f"  address   = {{{ref['address']}}},")
                
        # Add common fields
        if 'year' in ref:
            bibtex.append(f"  year    = {{{ref['year']}}},")
        if 'pages' in ref:
            bibtex.append(f"  pages   = {{{ref['pages']}}}")
            
        bibtex.append("}")
        
        return '\n'.join(bibtex)

    def convert_file(self, input_file: str, output_file: str):
        """Convert a file of references to BibTeX format."""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
                
            # Split text into individual references
            references = text.split('\n\n')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                for ref in references:
                    if ref.strip():
                        bibtex = self.to_bibtex(ref)
                        f.write(bibtex + '\n\n')
                        
            print(f"Successfully converted references to {output_file}")
            
        except Exception as e:
            print(f"Error processing file: {e}")

# Example usage
if __name__ == "__main__":
    converter = BibTeXConverter()
    
    # Example reference
    reference = """Calvert, B.D.
    [1970] Nonlinear evolution equations in Banach lattice.
    Bull. Amer. Math. Soc. 76 (1970), 845-850."""
    
    bibtex = converter.to_bibtex(reference)
    print(bibtex)
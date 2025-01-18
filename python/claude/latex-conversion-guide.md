# PDF zu LaTeX Konvertierung mit Claude API

## Überblick

Dieses Python-Skript ermöglicht die automatische Konvertierung von PDF-Dokumenten in LaTeX unter Verwendung der Claude API von Anthropic.

## Voraussetzungen

- Python 3.7+
- `anthropic` Bibliothek
- `PyPDF2` Bibliothek
- Anthropic API-Schlüssel

## Bibliotheken installieren

```bash
pip install anthropic PyPDF2
```

## Skript-Komponenten

### 1. PDF-Vorverarbeitung

Die Funktion `preprocess_pdf()` extrahiert den Text aus dem PDF-Dokument:

```python
def preprocess_pdf(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text
```

#### Wichtige Aspekte:
- Verwendet `PyPDF2` zum Textextrakt
- Verarbeitet mehrseitige PDFs
- Konkateniert Text aller Seiten

### 2. LaTeX-Konvertierung

Die Funktion `convert_to_latex()` sendet den extrahierten Text an Claude:

```python
def convert_to_latex(text):
    client = anthropic.Anthropic(api_key="YOUR_API_KEY")
    
    conversion_prompt = """Detaillierte Formatierungsregeln..."""
    
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        messages=[
            {
                "role": "user",
                "content": f"{conversion_prompt}{text}"
            }
        ]
    )
    
    return response.content[0].text
```

#### Wichtige Aspekte:
- Definiert detaillierte Formatierungsregeln
- Nutzt Claude 3 Opus Modell
- Maximale Tokenlänge: 4000
- Gibt konvertierten LaTeX-Text zurück

### 3. Hauptprozess

Die `main()`-Funktion koordiniert den gesamten Konvertierungsprozess:

```python
def main(pdf_path, output_path):
    text = preprocess_pdf(pdf_path)
    latex_output = convert_to_latex(text)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_output)
    
    print(f"LaTeX-Dokument wurde in {output_path} gespeichert.")
```

#### Wichtige Aspekte:
- Extrahiert PDF-Inhalt
- Konvertiert in LaTeX
- Speichert Ausgabe-LaTeX-Datei
- Gibt Erfolgsmeldung aus

## Verwendung

```bash
python convert_pdf_to_latex.py input.pdf output.tex
```

## Einschränkungen

- Qualität hängt von PDF-Formatierung ab
- Komplexe mathematische Notationen können Herausforderungen bereiten
- Manuelles Nachbearbeiten möglicherweise erforderlich

## Empfehlungen

1. Testen Sie mit verschiedenen PDF-Dokumenten
2. Überprüfen Sie die Ausgabe
3. Passen Sie Formatierungsregeln im Prompt an

## Troubleshooting

- Überprüfen Sie API-Schlüssel
- Stellen Sie sicher, alle Bibliotheken installiert zu haben
- Bei Fehlern: Überprüfen Sie Fehlermeldungen

## Lizenz

[Ihre Lizenzinformationen]

## Autor

Ulrich Groh  
Email: ulgr@math.uni-tuebingen.de

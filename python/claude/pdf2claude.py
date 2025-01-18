import PyPDF2
import anthropic
import os
import sys


def preprocess_pdf(pdf_path):
    try:
        # Detaillierte Fehlerbehandlung
        if not os.path.exists(pdf_path):
            print(f"FEHLER: Datei {pdf_path} existiert nicht!")
            return ""

        reader = PyPDF2.PdfReader(pdf_path)
        full_text = ""

        # Prüfe Seitenanzahl
        print(f"Anzahl der Seiten: {len(reader.pages)}")

        for i, page in enumerate(reader.pages, 1):
            page_text = page.extract_text()
            print(f"Seite {i}: {len(page_text)} Zeichen")
            full_text += page_text

        # Zeige Gesamtlänge
        print(f"Gesamter extrahierter Text: {len(full_text)} Zeichen")

        return full_text
    except Exception as e:
        print(f"FEHLER bei PDF-Extraktion: {e}")
        return ""


def convert_to_latex(text, client):
    # Prüfe Textlänge vor Konvertierung
    print(f"Zu konvertierender Text: {len(text)} Zeichen")

    if not text.strip():
        print("WARNUNG: Leerer Eingabetext!")
        return ""

    conversion_prompt = """Bitte konvertiere den EXAKT vorliegenden mathematischen Text in LaTeX mit folgenden PRÄZISEN Formatierungsregeln:

1. Mathematische Formatierung:
- Hochstellungen IMMER mit {} einklammern: x{2} statt x^2
- Tiefstellungen IMMER mit {} einklammern: a{i} statt a_i
- Einzelformeln mit \[ ... \]
- Vor \[ und nach \] Zeilen mit %% --

2. Dokumentstruktur:
- Jeder Satz beginnt auf neuer Zeile
- Keine zusätzlichen Leerzeilen zwischen Sätzen
- Verwende enumitem mit [inline, shortlabel]
- Theorem und Definitionen mit amsthm
- Querverweise mit \label und \ref

3. Zusätzliche LaTeX-Konventionen:
- Mathematische Operatoren mit \operatorname{}
- Griechische Buchstaben mit \alpha, \beta etc.
- Konsistente Einrückungen und Formatierung

Bitte halte diese Regeln STRIKT ein und verändere NICHTS am Originaltext.

Zu konvertierender Text:
"""

    try:
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

        # Prüfe Antwortlänge
        latex_output = response.content[0].text
        print(f"Konvertierter LaTeX-Text: {len(latex_output)} Zeichen")
        return latex_output

    except Exception as e:
        print(f"FEHLER bei LaTeX-Konvertierung: {e}")
        return ""


def main(api_key):
    # Client initialisieren
    client = anthropic.Anthropic(api_key=api_key)

    # Pfade für Eingabe und Ausgabe
    pdf_path = 'test.pdf'
    tex_path = 'test.tex'
    original_text_path = 'test_original.txt'

    # PDF-Inhalt extrahieren
    original_text = preprocess_pdf(pdf_path)

    # Originaltext speichern
    with open(original_text_path, 'w', encoding='utf-8') as f:
        f.write(original_text)

    # In LaTeX konvertieren
    latex_output = convert_to_latex(original_text, client)

    # LaTeX-Datei speichern
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(latex_output)

    print(f"Konvertierung erfolgreich:")
    print(f"- Originaltext: {original_text_path}")
    print(f"- LaTeX-Dokument: {tex_path}")


# Direkte Verwendung
if __name__ == "__main__":
    api_key = "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"
    main(api_key)

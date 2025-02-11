import re
import os
import sys
from pathlib import Path


class LaTeXFormatter:
    @staticmethod
    def format_latex(input_text):
        # Nur Doppelpunkte AUSSERHALB mathematischer Formeln ersetzen
        def replace_colon(match):
            # Prüfe, ob der Doppelpunkt in einer mathematischen Formel ist
            text = match.group(0)
            if '$' in text or '\\[' in text or '\\(' in text:
                return text
            return text.replace(':', ' \\colon ')

        # Ersetze Doppelpunkte, aber schütze mathematische Formeln
        input_text = re.sub(r'[^$\\]*:.*', replace_colon, input_text)

        # := zu \coloneqq außerhalb mathematischer Formeln
        input_text = input_text.replace(':=', '\\coloneqq')

        # Zusätzliche Formatierungen, die mathematische Formeln nicht verändern
        input_text = re.sub(r'(\\item)([^\n]+)', r'\1\n\2', input_text)

        return input_text

    @staticmethod
    def process_file(input_path, output_path=None):
        if not output_path:
            output_path = Path(input_path).parent / f"{Path(input_path).stem}_formatted{Path(input_path).suffix}"

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            formatted_content = LaTeXFormatter.format_latex(content)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)

            print(f"Formatierte Datei gespeichert unter: {output_path}")
        except Exception as e:
            print(f"Fehler beim Formatieren: {e}")


def main():
    if len(sys.argv) < 2:
        print("Bitte geben Sie den Pfad zur LaTeX-Datei an.")
        sys.exit(1)

    input_file = sys.argv[1]
    LaTeXFormatter.process_file(input_file)


if __name__ == "__main__":
    main()
import re


def convert_citation(text):
    """
    Converts citations of formats:
    [Author (YYYY), Note] to Author \citet[Note]{author:YYYY}
    [Author-Author (YYYY)] to Author1 et all. \citet{author_author:YYYY}
    """

    def replace_citation_with_note(match):
        author = match.group(1).strip()
        year = match.group(2)
        note = match.group(3).strip()

        # Convert author to lowercase and replace 
        # spaces/hyphens with underscores/entfernt diese
        # Setzt den Namen des Authors vor \cite-Befehl
        # author_label = author.lower()
        # author_label = author_label.replace(' ', '_')
        # author_label = author_label.replace('-', '_')

        #author_name = author
        author_label = author.lower()
        author_label = author_label.replace(' ', '')
        author_label = author_label.replace('-', '')

        #return f"{author_name}~\\cite[{note}]{{{author_label}:{year}}}"
        return f"\\citet[{note}]{{{author_label}:{year}}}"



    def replace_simple_citation(match):
        author = match.group(1).strip()
        year = match.group(2)

        # Convert author to lowercase and replace 
        # spaces/hyphens with underscores/entfernt diese

        author_name = author
        author_label = author.lower()
        author_label = author_label.replace(' ', '')
        author_label = author_label.replace('-', '')

        return f"\\citet{{{author_label}:{year}}}"

    # Pattern for citations with notes
    pattern_with_note = r"\[([\w\s-]+)\s+\((\d{4})\),\s+([^\]]+)\]"
    # Pattern for simple citations
    pattern_simple = r"\[([\w\s-]+)\s+\((\d{4})\)\]"

    # First replace citations with notes
    text = re.sub(pattern_with_note, replace_citation_with_note, text)
    # Then replace simple citations
    text = re.sub(pattern_simple, replace_simple_citation, text)

    return text


# Test the function
if __name__ == "__main__":
    # Test cases
    test_texts = [
        "[Takesaki (1979), Chapter III]",
        "[von Neumann (1932), Section 2.1]",
        "[Reed Moore (1975), Theorem 1.2]",
        "[Bratteli-Robinson (1979)]",
        "[von Neumann (1932)]",
        "[Bratteli-Robinson (1979)]"
    ]

    for text in test_texts:
        converted = convert_citation(text)
        print(f"Original: {text}")
        print(f"Converted: {converted}")
        print()

# Example usage:
    with open('chap-b4.tex', 'r') as file:
        text = file.read()
        converted_text = convert_citation(text)
        with open('chap-b4-bib.tex', 'w') as file:
            file.write(converted_text)

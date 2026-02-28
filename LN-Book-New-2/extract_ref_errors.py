#!/usr/bin/env python3
"""
Extract undefined references, citations, and other LaTeX errors from .log files
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

def extract_errors(log_file):
    """Extract all reference, citation, and label errors from LaTeX log"""
    
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found")
        sys.exit(1)
    
    errors = defaultdict(list)
    
    # Pattern 1: Undefined references
    pattern_ref = r"Reference\s+['\"]?([^'\"]+)['\"]?\s+on page\s+(\d+)\s+undefined(?:\s+on input line\s+(\d+))?"
    for match in re.finditer(pattern_ref, content, re.IGNORECASE):
        ref, page, line = match.groups()
        errors['undefined_references'].append({
            'ref': ref.strip(),
            'page': page,
            'line': line,
            'type': 'Reference'
        })
    
    # Pattern 2: Undefined citations
    pattern_cite = r"Citation\s+['\"]?([^'\"]+)['\"]?\s+undefined"
    for match in re.finditer(pattern_cite, content, re.IGNORECASE):
        cite = match.group(1)
        # Find line number if available
        idx = match.start()
        line_match = re.search(r"on input line\s+(\d+)", content[max(0, idx-100):idx+100])
        line = line_match.group(1) if line_match else "?"
        errors['undefined_citations'].append({
            'cite': cite.strip(),
            'line': line,
            'type': 'Citation'
        })
    
    # Pattern 3: LaTeX Warnings about references
    pattern_warn = r"LaTeX Warning:.*?(?:Reference|Label|Citation).*?([a-zA-Z0-9\-_.:]+).*?(?:undefined|not found)"
    for match in re.finditer(pattern_warn, content, re.IGNORECASE):
        # This is less precise, only collect if not already found
        pass
    
    # Pattern 4: "There were undefined references" with preceding errors
    # Collect all lines mentioning undefined
    undefined_lines = []
    for i, line in enumerate(content.split('\n')):
        if 'undefined' in line.lower() and any(keyword in line.lower() for keyword in ['reference', 'citation', 'label']):
            undefined_lines.append((i+1, line.strip()))
    
    # Pattern 5: Check for lines with specific label/ref patterns
    pattern_label_error = r"(?:undefined on input line|at input line)\s+(\d+)"
    
    return errors, undefined_lines

def format_output(errors, undefined_lines):
    """Format and print the extracted errors"""
    
    print("=" * 80)
    print("LATEX REFERENCE/CITATION ERRORS EXTRACTION")
    print("=" * 80)
    print()
    
    # Undefined References
    if errors['undefined_references']:
        print(f"UNDEFINED REFERENCES ({len(errors['undefined_references'])})")
        print("-" * 80)
        for err in errors['undefined_references']:
            print(f"  Ref:     '{err['ref']}'")
            print(f"  Page:    {err['page']}")
            if err['line']:
                print(f"  Line:    {err['line']}")
            print()
    
    # Undefined Citations
    if errors['undefined_citations']:
        print(f"\nUNDEFINED CITATIONS ({len(errors['undefined_citations'])})")
        print("-" * 80)
        for err in errors['undefined_citations']:
            print(f"  Citation: '{err['cite']}'")
            if err['line'] and err['line'] != '?':
                print(f"  Line:      {err['line']}")
            print()
    
    # All lines mentioning undefined
    if undefined_lines:
        print(f"\nALL LINES MENTIONING 'UNDEFINED' ({len(undefined_lines)})")
        print("-" * 80)
        for line_num, line_text in undefined_lines:
            print(f"  Line {line_num}: {line_text[:100]}")
        print()
    
    # Summary
    print("=" * 80)
    total_errors = len(errors['undefined_references']) + len(errors['undefined_citations'])
    if total_errors == 0:
        print("✓ No undefined references or citations found!")
    else:
        print(f"Total Errors Found: {total_errors}")
        print("\nNext steps:")
        print("  1. Check each undefined reference/citation above")
        print("  2. Verify \\label{...} definitions exist for \\ref{...} calls")
        print("  3. Check bibliography keys in .bib file for citations")
        print("  4. Ensure biber was run (if using biblatex)")
        print("  5. Try: pdflatex → biber → pdflatex → pdflatex")
    print("=" * 80)

def main():
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        # Try to find .log files in current directory
        log_files = list(Path('.').glob('*.log'))
        if not log_files:
            print("Usage: python extract_ref_errors.py <logfile.log>")
            print("No .log files found in current directory")
            sys.exit(1)
        log_file = str(log_files[0])
        print(f"Processing: {log_file}\n")
    
    errors, undefined_lines = extract_errors(log_file)
    format_output(errors, undefined_lines)

if __name__ == '__main__':
    main()

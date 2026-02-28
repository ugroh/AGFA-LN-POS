#!/usr/bin/env python3
"""
Find label definitions in .tex files and identify missing labels
Shows WHERE each undefined reference is used
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

def find_all_labels(directory='.'):
    """Scan all .tex files for \\label{...} definitions"""
    labels = defaultdict(list)
    tex_files = list(Path(directory).rglob('*.tex'))
    
    if not tex_files:
        print(f"No .tex files found in {directory}")
        return labels
    
    for tex_file in sorted(tex_files):
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Find all \label{...}
                for match in re.finditer(r'\\label\s*\{\s*([^}]+)\s*\}', content):
                    label = match.group(1).strip()
                    line_num = content[:match.start()].count('\n') + 1
                    labels[label].append({
                        'file': str(tex_file),
                        'line': line_num,
                        'rel_path': str(tex_file).replace('./','')
                    })
        except Exception as e:
            pass
    
    return labels

def find_ref_usage(ref, directory='.'):
    """Find where a \\ref{...} is used in .tex files"""
    usages = []
    tex_files = list(Path(directory).rglob('*.tex'))
    
    # Escape special regex chars in ref
    ref_escaped = re.escape(ref)
    pattern = r'\\ref\s*\{\s*' + ref_escaped + r'\s*\}'
    
    for tex_file in sorted(tex_files):
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for match in re.finditer(pattern, content):
                    line_num = content[:match.start()].count('\n') + 1
                    # Get context (the line content)
                    lines = content.split('\n')
                    line_text = lines[line_num - 1].strip()[:80]
                    usages.append({
                        'file': str(tex_file),
                        'line': line_num,
                        'rel_path': str(tex_file).replace('./',''),
                        'context': line_text
                    })
        except Exception as e:
            pass
    
    return usages

def check_undefined_refs(log_file, directory='.'):
    """Compare undefined refs from log with actual labels"""
    
    # Parse log file for undefined references
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
        return
    
    undefined_refs_list = []
    pattern_ref = r"Reference\s+['\"`]?([^'\">`]+)['\"`]?\s+on page\s+(\d+)\s+undefined(?:\s+on input line\s+(\d+))?"
    for match in re.finditer(pattern_ref, content, re.IGNORECASE):
        ref = match.group(1).strip()
        page = match.group(2)
        # Remove backticks if present
        ref = ref.strip('`')
        undefined_refs_list.append({
            'ref': ref,
            'page': page
        })
    
    # Remove duplicates while preserving info
    seen = set()
    undefined_refs = []
    for item in undefined_refs_list:
        if item['ref'] not in seen:
            undefined_refs.append(item)
            seen.add(item['ref'])
    
    undefined_refs = sorted(undefined_refs, key=lambda x: x['ref'])
    
    # Find all labels
    labels = find_all_labels(directory)
    
    # Compare and find usages
    missing_labels = []
    found_refs = []
    
    for item in undefined_refs:
        ref = item['ref']
        if ref in labels:
            # Find where it's used
            usages = find_ref_usage(ref, directory)
            found_refs.append((ref, labels[ref], usages))
        else:
            # Try to find where it's used
            usages = find_ref_usage(ref, directory)
            missing_labels.append((ref, usages))
    
    # Print results
    print("=" * 100)
    print("LABEL ANALYSIS - WHERE ARE THE ERRORS?")
    print("=" * 100)
    print()
    
    print(f"Total Undefined References in Log: {len(undefined_refs)}")
    print(f"Labels Found in .tex Files: {len(labels)}")
    print()
    
    if missing_labels:
        print(f"MISSING LABELS ({len(missing_labels)}) - THESE DON'T EXIST ANYWHERE:")
        print("-" * 100)
        for ref, usages in missing_labels:
            print(f"\n  ✗ {ref}")
            if usages:
                print(f"    Referenced in:")
                for usage in usages:
                    print(f"      • {usage['rel_path']}: line {usage['line']}")
                    print(f"        {usage['context']}")
            else:
                print(f"    Not found in any .tex file (typo?)")
        print()
    
    if found_refs:
        print(f"LABELS FOUND ({len(found_refs)}) - BUT SHOWING AS UNDEFINED:")
        print("-" * 100)
        for ref, locations, usages in found_refs:
            print(f"\n  ✓ {ref}")
            print(f"    DEFINED in:")
            for loc in locations:
                print(f"      • {loc['rel_path']}: line {loc['line']}")
            print(f"    REFERENCED in:")
            for usage in usages:
                print(f"      • {usage['rel_path']}: line {usage['line']}")
                print(f"        {usage['context']}")
        print()
        print("  NOTE: These might be in different refsections or need recompilation")
        print()
    
    # Print summary
    print("=" * 100)
    print("DIAGNOSIS & SOLUTIONS")
    print("=" * 100)
    print()
    
    if missing_labels:
        print(f"1. MISSING LABELS: {len(missing_labels)} labels are referenced but never defined")
        print("   ACTION ITEMS:")
        for ref, usages in missing_labels:
            if usages:
                print(f"     • Add \\label{{{ref}}} near {usages[0]['rel_path']} line {usages[0]['line']}")
            else:
                print(f"     • Check spelling of '{ref}' (case-sensitive!)")
        print()
    
    if found_refs:
        print(f"2. CROSS-REFSECTION ISSUES: {len(found_refs)} labels exist but show as undefined")
        print("   Solutions:")
        print("   a) Run full recompilation cycle: pdflatex → biber → pdflatex → pdflatex")
        print("   b) Check if labels are in different refsections (biblatex issue)")
        print()
    
    print("3. GENERAL FIXES:")
    print("   $ rm *.aux *.auxlock part-*/*.aux 2>/dev/null")
    print("   $ pdflatex -interaction=nonstopmode LN-Book-New.tex")
    print("   $ biber LN-Book-New")
    print("   $ pdflatex -interaction=nonstopmode LN-Book-New.tex")
    print("   $ pdflatex -interaction=nonstopmode LN-Book-New.tex")
    print()
    print("=" * 100)

def main():
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = 'LN-Book-New.log'
    
    if len(sys.argv) > 2:
        directory = sys.argv[2]
    else:
        directory = '.'
    
    check_undefined_refs(log_file, directory)

if __name__ == '__main__':
    main()

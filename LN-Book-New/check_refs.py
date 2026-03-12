#!/usr/bin/env python3
import re, sys
from pathlib import Path

# Alle .tex-Dateien sammeln
dirs = ['part-a', 'part-b', 'part-c', 'part-d', 'part-e']
files = []
for d in dirs:
    files.extend(Path(d).rglob('*.tex'))
# Hauptdateien im Wurzelverzeichnis
files.extend(Path('.').glob('*.tex'))

labels  = set()
refs    = {}  # label -> [(datei, zeile)]

for f in files:
    text = f.read_text(errors='ignore')
    for m in re.finditer(r'\\label\{([^}]+)\}', text):
        labels.add(m.group(1))
    for m in re.finditer(r'\\(?:eq)?ref\{([^}]+)\}', text):
        lnum = text[:m.start()].count('\n') + 1
        refs.setdefault(m.group(1), []).append((str(f), lnum))

# Fehlende Labels ausgeben
missing = {k: v for k, v in refs.items() if k not in labels}

if not missing:
    print("Alles ok – alle \\ref/\\eqref haben ein entsprechendes \\label.")
else:
    print(f"{len(missing)} fehlende Labels:\n")
    for label, locations in sorted(missing.items()):
        for datei, zeile in locations:
            print(f"  {datei}:{zeile}  ->  {label}")
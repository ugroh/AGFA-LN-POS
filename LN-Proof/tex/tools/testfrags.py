#!/usr/bin/env python3
"""Jeden Formel-Kandidaten probeweise setzen (pdflatex); Ergebnis -> chosen.json.

Aufruf: testfrags.py 0   (erste Kandidaten)
        testfrags.py 1   (Ersatzkandidaten für die fehlerhaften)
"""
import json, subprocess, os, re, sys

frags = json.load(open('fragments.json'))
level = int(sys.argv[1]) if len(sys.argv) > 1 else 0
prev = json.load(open('chosen.json')) if level else {}
items = [(k, v[level]) for k, v in frags.items()
         if len(v) > level and (level == 0 or prev.get(k) is None)]
OUT = os.environ.get('KORR_OUT', 'out')
TMP = os.path.join(OUT, '.probe')
os.makedirs(TMP, exist_ok=True)
pre = open(os.path.join(OUT, 'korr-preamble.tex')).read()


def run(batch, tag):
    body = []
    for idx, (k, tex) in batch:
        body.append('\\typeout{@@B%d}\\setbox0\\vbox{\\hsize=6cm\\RaggedRight %s\\par}\\typeout{@@E%d}' % (idx, tex, idx))
    doc = ('\\documentclass[10pt]{article}\n' + pre + '\n\\tracinglostchars=3\n\\begin{document}\n'
           + '\n'.join(body) + '\n\\typeout{@@DONE}\\end{document}\n')
    fn = os.path.join(TMP, '%s.tex' % tag)
    open(fn, 'w').write(doc)
    try:
      subprocess.run(['pdflatex', '-interaction=nonstopmode',
                    '-output-directory', TMP, fn], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    except subprocess.TimeoutExpired:
      pass
    log = open(os.path.join(TMP, '%s.log' % tag), encoding='latin-1').read()
    return log


def analyse(batch, log):
    bad, missing = set(), []
    for idx, _ in batch:
        m = re.search(r'@@B%d\n(.*?)@@E%d\n' % (idx, idx), log, re.S)
        if not m:
            missing.append(idx); continue
        seg = m.group(1)
        if re.search(r'^! ', seg, re.M) or 'Missing character' in seg:
            bad.add(idx)
    return bad, missing


indexed = list(enumerate(items))
fails = set()
B = 60
todo = [indexed[i:i + B] for i in range(0, len(indexed), B)]
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(8) as ex:
    logs = list(ex.map(lambda a: run(a[1], 'p%d' % a[0]), enumerate(todo)))
retry = []
for batch, log in zip(todo, logs):
    bad, missing = analyse(batch, log)
    fails |= bad
    if missing:
        retry.append([x for x in batch if x[0] in missing])
todo = retry
print('erster Durchgang fertig, Wiederholungen:', len(todo))
n = 0
while todo:
    batch = todo.pop(0)
    n += 1
    log = run(batch, 'b%d' % n)
    bad, missing = analyse(batch, log)
    fails |= bad
    if missing:
        if len(batch) == 1:
            fails.add(batch[0][0])
        else:
            # Lauf abgebrochen: Rest einzeln/halbiert erneut
            rest = [x for x in batch if x[0] in missing]
            h = max(1, len(rest) // 2)
            todo[:0] = [rest[:h], rest[h:]] if len(rest) > 1 else [rest]
fail_keys = [items[i][0] for i in sorted(fails)]
chosen = prev if level else {k: None for k in frags}
for i, (k, tex) in enumerate(items):
    if i not in fails:
        chosen[k] = tex
json.dump(chosen, open('chosen.json', 'w'), ensure_ascii=False, indent=1)
print('getestet', len(items), 'fehlerhaft', len(fail_keys), 'Läufe', n)
for k in fail_keys:
    print('  ', k[:140])

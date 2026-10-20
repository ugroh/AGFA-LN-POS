#!/usr/bin/env python3
"""Dokumente übersetzen; Formeln, die im Tabellenkontext doch Fehler machen, als Code zeigen.

Aufruf: finalize.py chosen.json <md...>   (im Ausgabeverzeichnis, KORR_OUT=.)
"""
import json, os, re, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
chosen_file, mds = sys.argv[1], sys.argv[2:]
OUT = os.environ.get('KORR_OUT', '.')


def build():
    subprocess.run([sys.executable, os.path.join(here, 'md2tex.py'), 'build', chosen_file] + mds,
                   check=True, stdout=subprocess.DEVNULL)


def compile_doc(name):
    for _ in range(2):
        subprocess.run(['pdflatex', '-interaction=nonstopmode', name + '.tex'], cwd=OUT,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return open(os.path.join(OUT, name + '.log'), encoding='latin-1').read()


for runde in range(6):
    build()
    chosen = json.load(open(chosen_file))
    demoted = 0
    for md in mds:
        name = os.path.splitext(os.path.basename(md))[0]
        log = compile_doc(name)
        if not re.search(r'^! ', log, re.M):
            continue
        src = open(os.path.join(OUT, name + '.tex'), encoding='utf-8').read().splitlines()
        lines = {int(n) for n in re.findall(r'^l\.(\d+) ', log, re.M)}
        for n in lines:
            line = src[n - 1] if n - 1 < len(src) else ''
            for k, tex in chosen.items():
                if tex and len(tex) > 2 and tex in line:
                    chosen[k] = None
                    demoted += 1
    if not demoted:
        break
    json.dump(chosen, open(chosen_file, 'w'), ensure_ascii=False, indent=1)
    print('Runde %d: %d Formel(n) im Kontext nicht setzbar -> als Code' % (runde + 1, demoted))

for md in mds:
    name = os.path.splitext(os.path.basename(md))[0]
    log = open(os.path.join(OUT, name + '.log'), encoding='latin-1').read()
    pages = re.search(r'Output written on \S+ \((\d+) pages', log)
    print('%s: %d Fehler, %s Seiten' % (name, len(re.findall(r'^! ', log, re.M)), pages.group(1) if pages else '?'))

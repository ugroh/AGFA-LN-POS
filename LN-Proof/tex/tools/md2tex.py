#!/usr/bin/env python3
"""Korrekturlisten (Markdown mit TeX-Code) -> LaTeX mit gesetzten Formeln.

TeX-Code in `...`, in $...$ und im Fließtext (z. B. E_{\vert f\vert}) wird als Formel
gesetzt. Was sich nicht setzen lässt (Labels, Makronamen, Dateinamen), erscheint grau
in Schreibmaschinenschrift. Ablauf siehe make-tex.sh.

Aufruf:  md2tex.py collect <md...>              -> fragments.json (alle Kandidaten)
         md2tex.py build   chosen.json <md...>  -> <name>.tex je Datei (in $KORR_OUT)
"""
import re, sys, json, os, unicodedata

OUT = os.environ.get('KORR_OUT', 'out')

# ---------------------------------------------------------------- Unicode
UMATH = {
    'Γ': r'\Gamma', 'Θ': r'\Theta', 'Φ': r'\Phi', 'Ψ': r'\Psi', 'Ω': r'\Omega',
    'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta', 'ε': r'\varepsilon',
    'η': r'\eta', 'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu', 'ν': r'\nu', 'ξ': r'\xi',
    'π': r'\pi', 'ρ': r'\varrho', 'σ': r'\sigma', 'τ': r'\tau', 'φ': r'\varphi',
    'ψ': r'\psi', 'ω': r'\omega',
    '‖': r'\|', '′': r"{}'", '⁺': r'^{+}', '⁻': r'^{-}', 'ⁿ': r'^{n}', '²': r'^{2}', '¹': r'^{1}',
    '₀': r'_{0}', '₁': r'_{1}', '₃': r'_{3}', '₊': r'_{+}',
    'ℂ': r'\mathbb{C}', 'ℕ': r'\mathbb{N}', 'ℝ': r'\mathbb{R}',
    '→': r'\to', '↓': r'\downarrow', '↦': r'\mapsto', '⇒': r'\Rightarrow', '⇔': r'\Leftrightarrow',
    '∂': r'\partial', '∅': r'\emptyset', '∈': r'\in', '∉': r'\notin', '−': r'-',
    '∖': r'\setminus', '∘': r'\circ', '∞': r'\infty', '∧': r'\wedge', '∩': r'\cap',
    '∫': r'\int', '≈': r'\approx', '≠': r'\neq', '≡': r'\equiv', '≤': r'\leq', '≥': r'\geq',
    '≪': r'\ll', '≫': r'\gg', '⊆': r'\subseteq', '⊗': r'\otimes', '⋆': r'\star',
    '⟨': r'\langle', '⟩': r'\rangle', '±': r'\pm', '×': r'\times', '·': r'\cdot',
    '𝒮': r'\mathcal{S}', '𝒯': r'\mathcal{T}', '𝒰': r'\mathcal{U}', '𝓑': r'\mathcal{B}',
    '𝓕': r'\mathcal{F}', '𝓛': r'\mathcal{L}', '𝓡': r'\mathcal{R}', '𝟏': r'\mathbf{1}',
    '𝟙': r'\mathbf{1}', '⏎': r'\hookleftarrow', '½': r'\tfrac{1}{2}',
}
COMB = {'\u0302': r'\hat', '\u0303': r'\tilde', '\u0304': r'\bar', '\u0307': r'\dot'}
TEXTSYM = {'●': r'\sichA{}', '◐': r'\sichB{}', '○': r'\sichC{}', '½': r'\textonehalf{}',
           '…': r'\dots{}', 'ṽ': r'\ensuremath{\tilde{v}}', '\u00ad': r'\-'}


def uni_math(s):
    """Unicode in einem Formel-Fragment durch Makros ersetzen."""
    out = []
    for ch in unicodedata.normalize('NFD', s) if any(c in s for c in 'ṽĥŝ') else s:
        if ch in COMB and out:
            out[-1] = r'\ensuremath{' + COMB[ch] + '{' + out[-1] + '}}'
        elif ch in UMATH:
            out.append(r'\ensuremath{' + UMATH[ch] + '}')
        elif ch == '…':
            out.append(r'\dots ')
        elif ch == '\u00ad':
            pass
        elif ch == '’':
            out.append("'")
        else:
            out.append(ch)
    return ''.join(out)


TEX_SPECIAL = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '$': r'\$', '&': r'\&',
               '%': r'\%', '#': r'\#', '_': r'\_', '^': r'\textasciicircum{}', '~': r'\textasciitilde{}'}


def esc_prose(s):
    """Fließtext (Deutsch) escapen; mathematische Unicode-Zeichen als Formel."""
    s = unicodedata.normalize('NFC', s)
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        nxt = s[i + 1] if i + 1 < len(s) else ''
        if nxt in COMB:
            out.append(r'\ensuremath{' + COMB[nxt] + '{' + UMATH.get(ch, ch) + '}}'); i += 2; continue
        if ch == '~' and i > 0 and not s[i - 1].isspace() and nxt and not nxt.isspace():
            out.append('~')                      # TeX-Leerzeichen wie in „Eq.~(7.4)“
        elif ch in TEX_SPECIAL:
            out.append(TEX_SPECIAL[ch])
        elif ch in TEXTSYM:
            out.append(TEXTSYM[ch])
        elif ch in UMATH:
            # zusammenhängende Formelzeichen zu einem Mathe-Block bündeln
            j = i
            buf = []
            while j < len(s) and s[j] in UMATH:
                m = UMATH[s[j]]
                buf.append(m + (' ' if re.match(r'\\[A-Za-z]+$', m) else ''))
                j += 1
            out.append(r'\ensuremath{' + ''.join(buf).strip() + '}')
            i = j; continue
        else:
            out.append(ch)
        i += 1
    return ''.join(out)


def esc_code(s):
    """Quelltext wörtlich (Schreibmaschine)."""
    r = []
    for ch in s:
        if ch in TEX_SPECIAL:
            r.append(TEX_SPECIAL[ch])
        elif ch in TEXTSYM:
            r.append(TEXTSYM[ch])
        elif ch in UMATH:
            r.append(r'\ensuremath{' + UMATH[ch] + '}')
        else:
            r.append(ch)
    t = ''.join(r)
    # Umbruch nach Komma, Leerzeichen, Backslash erlauben
    t = t.replace(' ', r' \allowbreak{}').replace(r'\textbackslash{}', r'\allowbreak{}\textbackslash{}')
    if t.startswith(r'\allowbreak{}'):
        t = t[len(r'\allowbreak{}'):]
    return r'\code{' + t + '}'


# ---------------------------------------------------------------- Klassifikation
STRUCT = re.compile(r'\\(label|'
                    r'part|chapter|section|subsection|subsubsection|paragraph|index|item|footnote|'
                    r'texorpdfstring|newcommand|renewcommand|spnewtheorem|usepackage|bibitem|'
                    r'begin\{(theorem|proposition|lemma|corollary|definition|example|examples|remark|'
                    r'remarks|proof|enumerate|itemize|equation|align|empheq)\*?\}|end\{(theorem|'
                    r'proposition|lemma|corollary|definition|example|examples|remark|remarks|proof|'
                    r'enumerate|itemize)\*?\}|noindent|hspace|vspace|smallskip|medskip|bigskip|'
                    r'newline|linebreak|qed|qedhere|url|href|xspace)\b')
TEXTCMDS = {'eg', 'ie', 'cf', 'resp', 'etc', 'vs', 'CA', 'WA', 'AW', 'lnm', 'sfrac'}
FILE_RE = re.compile(r'^[\w./+-]+\.(tex|md|bib|pdf|sty|cls|py)$')


def classify(frag):
    f = frag.strip()
    if not f:
        return 'code'
    if FILE_RE.match(f) or f in ('fahnenkorrektur', 'main') or re.fullmatch(r'\{?[a-zA-Z-]+:\d{4}[a-z]?\}?\)*\.?', f):
        return 'code'
    if re.fullmatch(r'[a-z]+:[\w.-]+', f):          # Label-Name wie thm:a1-2.3
        return 'code'
    if STRUCT.search(f):
        return 'code'
    if re.fullmatch(r'\\(label|ref|eqref|cite|emph)', f):
        return 'code'
    m = re.fullmatch(r'\\([A-Za-z]+)\*?', f)
    if m and m.group(1) in TEXTCMDS:
        return 'code'
    if f in ('~', '\\,', '\\;', '\\!', '\\:', '\\ ', '$', '$$', '{}', '='):
        return 'code'
    if re.fullmatch(r'(\\(begin|end)\{[^{}]*\}(\s*\[[^\]]*\]|\{[^{}]*\})*\s*)+', f) or f.startswith('\\\\') \
            or re.fullmatch(r'\\begin\{(multline|align|equation|gather)\*?\}.*', f):
        return 'code'
    if '$' in f:
        if f.startswith('$') and f.endswith('$') and f.count('$') == 2:
            return 'math'
        if f.startswith('\\text'):
            return 'math'
        return 'text'
    if re.search(r'\\(v?ref|eqref|myeqpageref|vpageref|cite[a-z]*|emph|textit|textbf|enquote)\b', f):
        return 'text'
    # Text ohne $ : englische Wörter außerhalb von \text{..} etc.
    g = re.sub(r'\\(text|mathrm|operatorname|textup|mbox|textnormal|mathit|textrm|textit|begin|end)\{[^{}]*\}', ' ', f)
    g = re.sub(r'\\[A-Za-z]+', ' ', g)
    if re.search(r'(?<![\\{_^])\b[A-Za-z]{3,}\s+[A-Za-z]{2,}\b', g) and not re.search(r'[\^_]', g):
        return 'text'
    if re.search(r'(?<![\\A-Za-z])[A-Za-z]{5,}', g):
        return 'text'
    if re.search(r'\b(and|or|for|if|the|with|on|of|is|in)\s+[A-Za-z]', g) and re.search(r'[A-Za-z]{3,}\s', g):
        return 'text'
    return 'math'


def balanced(f):
    g = f.replace('\\{', '').replace('\\}', '').replace('\\$', '')
    d = 0
    for ch in g:
        d += ch == '{'
        d -= ch == '}'
        if d < 0:
            return False
    if d != 0:
        return False
    if g.count('$') % 2:
        return False
    if len(re.findall(r'\\left\b', g)) != len(re.findall(r'\\right\b', g)):
        return False
    if len(re.findall(r'\\begin\{', g)) != len(re.findall(r'\\end\{', g)):
        return False
    return True


def render(frag):
    """LaTeX-Kandidat für ein Fragment (None = als Code zeigen)."""
    kind = classify(frag)
    if kind == 'code' or not balanced(frag):
        return None, kind
    f = uni_math(frag.strip())
    # Verweise: Label-Namen sichtbar machen statt ??
    f = re.sub(r'\\(?:myeqpageref|eqref)\{([^{}]*)\}', r'(\\lbl{\1})', f)
    f = re.sub(r'\\(?:v?ref|vpageref|pageref)\{([^{}]*)\}', r'\\lbl{\1}', f)
    f = re.sub(r'\\(?:text|paren|auto)?cite[a-z]*(\[[^\]]*\])?\{([^{}]*)\}', r'[\\lbl{\2}]', f)
    if kind == 'math':
        if f.startswith('$') and f.endswith('$'):
            f = f[1:-1]
        f = f.replace('\\\\', ' ')        # keine Zeilenumbrüche in Inline-Formeln
        f = re.sub(r'(?<!\\)&', ' ', f) if not re.search(r'\\begin\{', f) else f
        return '$' + safe_end(f.strip()) + '$', kind
    # Textmodus: wie im Buch gesetzt (gruppiert, damit nichts nach außen wirkt);
    # ein Zeilenumbruch \\ würde die Tabellenzeile beenden -> sichtbar als Code
    f = re.sub(r'(?<!\\)\\\\(?![A-Za-z])', r'\\code{\\textbackslash\\textbackslash}', f)
    return '{' + safe_end(f) + '}', kind


def safe_end(f):
    """Ein abschließendes '\\' (Kontroll-Leerzeichen) darf nicht mit $ oder } verschmelzen."""
    m = re.search(r'(\\+)$', f)
    if m and len(m.group(1)) % 2:
        f += ' '
    return f


def alternatives(frag):
    """Weitere Kandidaten, falls der erste nicht setzbar ist."""
    tex, kind = render(frag)
    if tex is None:
        return []
    alts = [tex]
    if kind == 'text' and re.match(r'\{(\\|[A-Za-z]([_^ ]|$))', tex):
        alts.append('$' + tex[1:-1] + '$')
    elif kind == 'math':
        alts.append(tex[1:-1])
    return alts


# ---------------------------------------------------------------- Registry
REG = {}      # Schlüssel -> Liste von LaTeX-Kandidaten (werden probegesetzt)
CHOSEN = {}   # Schlüssel -> gewählter Kandidat oder None (= als Code zeigen)


DIRECT = [False]   # True: Kandidaten direkt einsetzen (für den Ersatz ganzer Textfragmente)


def resolve(key, alts, fallback):
    if DIRECT[0]:
        return alts[0] if alts else fallback
    if key not in REG:
        REG[key] = alts
    tex = CHOSEN.get(key)
    return tex if tex is not None else fallback


# ---------------------------------------------------------------- Fließtext mit TeX
GREEK = {'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'varepsilon', 'eta', 'theta', 'kappa', 'lambda',
         'mu', 'nu', 'xi', 'pi', 'rho', 'sigma', 'tau', 'phi', 'varphi', 'psi', 'omega', 'Gamma',
         'Delta', 'Theta', 'Lambda', 'Phi', 'Psi', 'Omega', 'Sigma', 'chi', 'zeta', 'iota'}
OPS = set('=<>+-−/·≤≥→↦∈∉⊆≠≈≡⊗∘×⇒⇔↓≫≪∧') | {'\\leq', '\\geq', '\\to', '\\in'}
MARKUP_CMDS = {'text', 'diff', 'ddp', 'dt', 'ds', 'dx', 'dy', 'Kern', 'Fix', 'closure', 'Image', 'image', 'iu',
               'im', 'upshape', 'mleft', 'mright', 'smallsetminus', 'setminus', 'backslash', 'lim', 'limsup',
               'sign', 'supp', 'label', 'qedhere', 'displaystyle', 'underbar', 'underline', 'sfrac', 'mfrac',
               'Id', 'eu', 'exp', 'cdots', 'ldots', 'dots', 'colon', 'mapsto', 'quad', 'bigoplus', 'oplus',
               'bigcup', 'cup', 'max', 'inf', 'left', 'right', 'coloneq', 'coloneqq', 'eqqcolon', 'mathrm',
               'operatorname', 'widehat', 'hat', 'overline', 'bar', 'textit', 'mathit', 'cdot', 'Re', 'Im'}
MATHCHARS = set(UMATH) | {'∫'}
OPMAP = {'Id': r'\Id ', 'Ker': r'\operatorname{Ker}', 'Kern': r'\operatorname{Kern}', 'ker': r'\ker ',
         'Fix': r'\operatorname{Fix}', 'dim': r'\dim ', 'Re': r'\Re ', 'Im': r'\Im ', 'exp': r'\exp ',
         'sign': r'\sign ', 'max': r'\max ', 'min': r'\min ', 'sup': r'\sup ', 'inf': r'\inf ',
         'lim': r'\lim ', 'supp': r'\operatorname{supp}', 'grad': r'\operatorname{grad}', 'im': r'\operatorname{im}'}
OPNAMES = re.compile(r'(?<![\\A-Za-z])(' + '|'.join(sorted(OPMAP, key=len, reverse=True)) + r')(?![A-Za-z])')
TEXTMACROS = re.compile(r'\\(eg|ie|cf|resp|etc|vs|CA|WA|AW)\b')


STOP2 = {'an', 'in', 'im', 'zu', 'ob', 'so', 'da', 'es', 'um', 'am', 'er', 'wo', 'is', 'of', 'on', 'to',
         'if', 'or', 'as', 'at', 'be', 'by', 'we', 'it', 'no', 'Z', 'S', 'z', 'B', 'd', 'h', 'vgl', 'bzw', 'ca'}


def is_mathy(tok):
    if '\x00' in tok:
        return False
    return ('\\' in tok or '_' in tok or '^' in tok or any(c in MATHCHARS for c in tok)
            or tok in ('=', '<', '>', '<=', '>=', '+'))


def is_conn(tok):
    if tok in OPS:
        return True
    if tok in STOP2 or re.search(r'[a-zäöüß]{3,}', tok) or re.search(r'[ÄÖÜäöüß„“]', tok):
        return False
    if re.fullmatch(r"\d+(,\d+)?|[A-Za-z]", tok):
        return True
    return bool(re.fullmatch(r"[A-Za-z0-9()+\-−/'′’=<>.]{1,10}", tok)) and not tok.endswith('.')


def tokens_balanced(text):
    """In Wörter zerlegen; Leerzeichen innerhalb {..} gehören zum Wort."""
    out, cur, depth = [], '', 0
    for ch in text:
        if ch == '{' and not cur.endswith('\\'):
            depth += 1
        elif ch == '}' and not cur.endswith('\\') and depth:
            depth -= 1
        if ch.isspace() and depth == 0:
            if cur:
                out.append(cur); cur = ''
            out.append(ch)
        else:
            cur += ch
    if cur:
        out.append(cur)
    # Leerzeichen zusammenfassen
    res = []
    for t in out:
        if t.isspace() and res and res[-1].isspace():
            res[-1] += t
        else:
            res.append(t)
    return res


def split_punct(w):
    pre, suf = '', ''
    while w and (w[0] in '„“"' or (w[0] == '(' and w.count('(') > w.count(')'))
                 or (w[0] == '[' and w.count('[') > w.count(']'))):
        pre += w[0]; w = w[1:]
    while w and (w[-1] in '.,;:!?“”"' or (w[-1] == ')' and w.count(')') > w.count('('))
                 or (w[-1] == ']' and w.count(']') > w.count('['))):
        suf = w[-1] + suf; w = w[:-1]
    return pre, w, suf


def prose_math_run(run, latex_row, markup_table=False):
    """Ein Stück TeX im Fließtext setzen (Kandidat) oder als Code lassen."""
    if TEXTMACROS.fullmatch(run):
        return resolve('P:' + run, ['{' + run + '{}}'], esc_code(run))
    m = re.fullmatch(r'\\([A-Za-z]+)', run)
    if m and m.group(1) not in GREEK:
        return esc_code(run)                       # es geht um das Makro selbst
    if latex_row and '\\' in run:
        return esc_code(run)
    if markup_table and set(re.findall(r'\\([A-Za-z]+)', run)) & MARKUP_CMDS:
        return esc_code(run)
    if not balanced(run):
        return esc_code(run)
    if TEXTMACROS.search(run):
        alts = ['{' + safe_end(uni_math(run)) + '}']
    else:
        m_run = OPNAMES.sub(lambda m: OPMAP[m.group(1)], uni_math(run))
        alts = ['$' + safe_end(m_run) + '$']
    return resolve('P:' + run, alts, esc_code(run))


def prose(text, latex_row=False, markup_table=False):
    """Markdown-Fließtext (ohne Code-Spans) -> LaTeX."""
    ph = []

    def keep(tex):
        ph.append(tex)
        return '\x00%d\x00' % (len(ph) - 1)

    # $...$ im Fließtext
    def dollar(m):
        inner = m.group(1)
        if not balanced(inner):
            return keep(esc_code(m.group(0)))
        return keep(resolve('D:' + inner, ['$' + safe_end(uni_math(inner)) + '$'], esc_code(m.group(0))))
    text = re.sub(r'(?<!\\)\$([^$]+)\$', dollar, text)
    # Querverweise, Zitate
    text = re.sub(r'(~?)\\(?:myeqpageref|eqref)\{([^{}]*)\}',
                  lambda m: keep(('~' if m.group(1) else '') + r'(\lbl{' + m.group(2) + '})'), text)
    text = re.sub(r'(~?)\\(?:v?ref|vpageref|pageref)\{([^{}]*)\}',
                  lambda m: keep(('~' if m.group(1) else '') + r'\lbl{' + m.group(2) + '}'), text)
    text = re.sub(r'\\(?:text|paren|auto)?cite[a-z]*(?:\[([^\]]*)\])?\{([^{}]*)\}',
                  lambda m: keep('[' + r'\lbl{' + m.group(2) + '}' + (', ' + m.group(1) if m.group(1) else '') + ']'),
                  text)
    # \hat x  ->  \hat{x}
    text = re.sub(r'\\(hat|tilde|bar|widehat|widetilde|overline|dot|vec|mathfrak|mathcal|mathbb|mathbf)\s+([A-Za-z])\b',
                  r'\\\1{\2}', text)
    # TeX-Stücke im Fließtext
    toks = tokens_balanced(text)
    words = []          # (pre, core, suf, ws)
    for t in toks:
        if t.isspace():
            if words:
                words[-1][3] += t
            else:
                words.append(['', '', '', t])
        else:
            pre, core, suf = split_punct(t)
            m = re.match(r'^(.+?)(-[A-Za-zÄÖÜäöüß]{3,}.*)$', core)
            if m and is_mathy(m.group(1)) and '{' not in m.group(2):
                core, suf = m.group(1), m.group(2) + suf
            words.append([pre, core, suf, ''])
    out = []
    i = 0
    while i < len(words):
        pre, core, suf, ws = words[i]
        if core and is_mathy(core):
            # Lauf nach links: Verbinder mit Operator (z. B. "h =") einbeziehen
            j = i
            while j > 0 and not words[j - 1][2] and not words[j][0] and words[j - 1][1] \
                    and is_conn(words[j - 1][1]) and not out_locked(out, j - 1):
                j -= 1
            left = [w[1] for w in words[j:i]]
            if left and not any(x in OPS for x in left) and not (core[0] in OPS or core in OPS):
                j = i
            elif left:
                # nur den Verbinder direkt vor dem Operator mitnehmen (z. B. "m ≡ 1", nicht "a b = c")
                j = max(j, i - 1) if not any(x in OPS for x in left) else j
            # Lauf nach rechts
            k = i
            while not words[k][2] and k + 1 < len(words) and not words[k + 1][0] and words[k + 1][1] \
                    and (is_mathy(words[k + 1][1]) or is_conn(words[k + 1][1])):
                k += 1
            # rechts: Verbinder nur behalten, wenn direkt davor ein Operator steht (z. B. "≥ 1")
            while k > i and not is_mathy(words[k][1]):
                prev = words[k - 1][1]
                if prev in OPS or (prev and prev[-1] in OPS):
                    break
                k -= 1
            # bereits ausgegebene linke Wörter zurücknehmen
            for _ in range(i - j):
                out.pop()
            run = ''.join(words[x][1] + (words[x][3] if x < k else '') for x in range(j, k + 1))
            out.append(words[j][0] + keep(prose_math_run(run, latex_row, markup_table)) + words[k][2] + words[k][3])
            i = k + 1
            continue
        out.append(pre + core + suf + ws)
        i += 1
    text = ''.join(out)
    q = esc_prose(text)
    q = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', q)
    q = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\\emph{\1}', q)
    return _fill(q, ph)


def out_locked(out, idx):
    return False


def _fill(q, ph):
    while '\x00' in q:
        q = re.sub('\x00(\\d+)\x00', lambda m: ph[int(m.group(1))], q)
    return q


# ---------------------------------------------------------------- Markdown
CODE_SPAN = re.compile(r'`([^`]*)`')


def code_span(frag):
    tex, kind = render(frag)
    alts = alternatives(frag)
    if kind == 'text' and balanced(frag):
        # letzter Versuch: Text mit eingestreutem TeX wie Fließtext behandeln
        # (z. B. "Define, for f \in E, g \coloneq ...")
        DIRECT[0] = True
        try:
            alts.append('{' + prose(frag) + '}')
        finally:
            DIRECT[0] = False
    return resolve('C:' + frag, alts, esc_code(frag))


def inline(text, latex_row=False, markup_table=False):
    """Markdown-Inline (Code-Spans, **fett**, *kursiv*, TeX im Text) -> LaTeX."""
    parts = CODE_SPAN.split(text)
    res = []
    for k, p in enumerate(parts):
        res.append(code_span(p) if k % 2 else prose(p, latex_row, markup_table))
    s = ''.join(res)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    return s


def split_row(line):
    return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]]


COLSPEC = {
    # math-error: S. | Z. | ● | Stelle | Befund | Vorschlag
    6: [('S.', 'r', None), ('Z.', 'r', None), ('', 'c', None),
        ('Stelle', 'p', 3.0), ('Befund', 'p', 11.4), ('Vorschlag', 'p', 7.4)],
    # korrekturen-mathe: S. | Z. | ● | Ist | Soll | Art | Kommentar
    7: [('S.', 'r', None), ('Z.', 'r', None), ('', 'c', None),
        ('Ist', 'p', 5.8), ('Soll', 'p', 5.8), ('Art', 'p', 1.9), ('Kommentar', 'p', 7.3)],
}


def table_tex(rows):
    ncol = len(rows[0])
    spec = COLSPEC[ncol]
    cols = []
    for name, kind, w in spec:
        cols.append(r'>{\RaggedRight\arraybackslash}p{%.1fcm}' % w if kind == 'p' else kind)
    head = ' & '.join(r'\textbf{%s}' % h for h, _, _ in spec) + r' \\'
    out = [r'\begin{longtable}{@{}' + ''.join(cols) + '@{}}', r'\toprule', head, r'\midrule', r'\endfirsthead',
           r'\toprule', head, r'\midrule', r'\endhead', r'\bottomrule', r'\endlastfoot']
    body = rows[2:]
    for i, r in enumerate(body):
        latex_row = ncol == 7 and r[5].strip() in ('LaTeX', 'Abstand')
        cells = [inline(c, latex_row, ncol == 7) for c in r]
        line = ' & '.join(cells) + r' \\'
        if i < len(body) - 1:
            line += r'[2pt]'
        out.append(line)
    out.append(r'\end{longtable}')
    return '\n'.join(out)


def convert(md_path):
    lines = open(md_path, encoding='utf-8').read().splitlines()
    out = []
    i = 0
    title = None
    in_list = False
    while i < len(lines):
        l = lines[i]
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append(split_row(lines[i])); i += 1
            out.append(table_tex(rows))
            continue
        if in_list and not l.startswith('- '):
            out.append(r'\end{itemize}'); in_list = False
        if l.startswith('# '):
            title = inline(l[2:])
        elif l.startswith('## '):
            out.append(r'\section*{' + inline(l[3:]) + '}')
        elif l.startswith('### '):
            out.append(r'\subsection*{' + inline(l[4:]) + '}')
        elif l.startswith('- '):
            if not in_list:
                out.append(r'\begin{itemize}'); in_list = True
            out.append(r'\item ' + inline(l[2:]))
        elif l.strip() == '---':
            out.append(r'\medskip\hrule\medskip')
        elif l.strip():
            out.append(inline(l) + '\n')
        i += 1
    if in_list:
        out.append(r'\end{itemize}')
    name = os.path.basename(md_path)
    plain_title = re.sub(r'\\[a-zA-Z]+\{|[{}$\\]', '', title or name)
    doc = [r'\documentclass[10pt]{article}',
           r'\input{korr-preamble}',
           r'\hypersetup{pdftitle={' + plain_title + '}}',
           r'\pagestyle{plain}',
           r'\begin{document}',
           '% Erzeugt aus ' + name + ': Formeln gesetzt statt Quelltext.',
           '% Grau/Schreibmaschine = Quelltext, der sich nicht als Formel setzen laesst (Makronamen, Labels).',
           r'{\Large\bfseries ' + (title or name) + r'\par}',
           r'\smallskip',
           '\n'.join(out),
           r'\end{document}', '']
    return '\n'.join(doc)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'collect':
        for p in sys.argv[2:]:
            convert(p)
        json.dump(REG, open('fragments.json', 'w'), ensure_ascii=False, indent=1)
        from collections import Counter
        print(len(REG), Counter(k[:2] for k in REG), 'ohne Kandidat', sum(not v for v in REG.values()))
    elif mode == 'build':
        CHOSEN.update(json.load(open(sys.argv[2])))
        for p in sys.argv[3:]:
            name = os.path.splitext(os.path.basename(p))[0]
            open(os.path.join(OUT, name + '.tex'), 'w', encoding='utf-8').write(convert(p))
            print('wrote', name)

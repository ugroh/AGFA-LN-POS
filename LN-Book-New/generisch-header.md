```

\makeatletter
\newcommand{%\specialchapheader}[2]{%
  % #1 = Befehl (z.B. \chapter*, \printindex)
  % #2 = Header-Text (z.B. "List of Symbols")
  \def\ps@headings{%
    \let\@oddfoot\@empty\let\@evenfoot\@empty%
    \def\@evenhead{\runheadsize\rmfamily\upshape\rlap{\thepage}\hfil #2}%
    \def\@oddhead{\runheadsize\rmfamily\upshape #2\hfil\llap{\thepage}}%
  }%
  \pagestyle{headings}%
  #1%
}
\makeatother

```

```
%\specialchapheader{\chapter*{Preface}}{Preface}
%\specialchapheader{\chapter*{Contents}}{Contents}
%\specialchapheader{\chapter*{List of Symbols}}{List of Symbols}
%\specialchapheader{\chapter*{Updated Notes}}{Updated Notes}
%\specialchapheader{\printindex}{Index}
```

```
\makeatletter
\newcommand{\restoreheadings}{%
  \def\@evenhead{\runheadsize\rmfamily\upshape
                  \rlap{\thepage}\hfil
                  Part~\thepart\hspace{.75em}\leftmark}%
  \def\@oddhead{\runheadsize\rmfamily\upshape
                 \rightmark\hfil\llap{\thepage}}%
  \pagestyle{headings}%
}
\makeatother
```

### Final?

```
\makeatletter

% NORMALE HEADINGS (für Part/Chapter/Section)
\def\ps@headings{%
  \let\@oddfoot\@empty\let\@evenfoot\@empty
  \def\@evenhead{\runheadsize\rmfamily\upshape
                  \rlap{\thepage}\hfil
                  Part~\thepart\hspace{.75em}\leftmark}%
  \def\@oddhead{\runheadsize\rmfamily\upshape
                 \rightmark\hfil\llap{\thepage}}%
}

% Spezial-Header: Preface
\newcommand{\prefaceheader}{%
  \def\@evenhead{\runheadsize\rmfamily\upshape\rlap{\thepage}\hfil Preface}%
  \def\@oddhead{\runheadsize\rmfamily\upshape Preface\hfil\llap{\thepage}}%
}

% Spezial-Header: Contents
\newcommand{\contentsheader}{%
  \def\@evenhead{\runheadsize\rmfamily\upshape\rlap{\thepage}\hfil Contents}%
  \def\@oddhead{\runheadsize\rmfamily\upshape Contents\hfil\llap{\thepage}}%
}

% Spezial-Header: List of Symbols
\newcommand{\symbolsheader}{%
  \def\@evenhead{\runheadsize\rmfamily\upshape\rlap{\thepage}\hfil List of Symbols}%
  \def\@oddhead{\runheadsize\rmfamily\upshape List of Symbols\hfil\llap{\thepage}}%
}

% Spezial-Header: Updated Notes
\newcommand{\notesheader}{%
  \def\@evenhead{\runheadsize\rmfamily\upshape\rlap{\thepage}\hfil Updated Notes}%
  \def\@oddhead{\runheadsize\rmfamily\upshape Updated Notes\hfil\llap{\thepage}}%
}

% Spezial-Header: Index
\newcommand{\indexheader}{%
  \def\@evenhead{\runheadsize\rmfamily\upshape\rlap{\thepage}\hfil Index}%
  \def\@oddhead{\runheadsize\rmfamily\upshape Index\hfil\llap{\thepage}}%
}

\pagestyle{headings}

\makeatother
```
Im Dokument dann

```
\prefaceheader
\chapter*{Preface}

\contentsheader
\chapter*{Contents}
\tableofcontents

\symbolsheader
\include{./part-0/ln-symbols}

\pagestyle{headings}
\mainmatter
\include{./part-a/part-a}
...

\notesheader
\chapter*{Updated Notes}

\indexheader
\printindex
```
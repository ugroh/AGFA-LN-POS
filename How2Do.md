##### How2Do (Stand: 2024/01/31)

Grundsätzlich bietet sich [Overleaf](https://www.overleaf.com/) als System zur Erstellung von `LaTeX`-Dokumenten an. Auch hat dieses System ein sehr gutes Hilfesystem. Also bei Fragen kann man dieses konsultieren.

Nun zu meinen Vorschlägen zur einheitlichen Erstellung unserer `LaTeX`- Texte, wobei `Claude` mithilfe der Regeln schon sehr gut arbeitet. Gern können wir alles im Rahmen eines Zoom-Meetings besprechen. 

- Die  `LaTeX`-Testdateien werde ich noch etwas anpassen, damit das Erstellen, das Lesen und der Vergleich mit dem Originalen besser wird. Alles dazu werde ich in das Verzeichnis [author-test/peamble](https://github.com/ugroh/AGFA-LN-POS/tree/main/author-test) stellen und euch informieren. 

- *Aufzählungen:* Hier versenden wir das Paket [enumitem](https://ctan.org/pkg/translation-enumitem-de) in der folgenden Form:

  * Nummerierte Aufzählungen mit römischen Zahlen (i), (ii) ...
  * Äquivalenzen mit den Buchstaben (a), (b), ..

  Also etwa:

  ```latex
  begin{enumerate}[(i)]
  \item
  Text
  \item
  ...`
  \end{enumerate}
  ```
  
  Wer die Abstände enger haben will – `nossep` in `[...]` eintragen.
  
- Kursiv bitte mittels `\emph{..}` eingeben und nicht `\textit` verwenden. Letzteres ist für Sätze zuständig.

- *Label:* `\label{was:wo}` ist in der [Anleitung für Claude](https://github.com/ugroh/AGFA-LN-POS/blob/main/anleitung-claude.md) beschrieben. Verweise darauf erfolgen mittels `\ref{label}` und der Verweis auf die zugehörige Seite mittels `Prop.~\ref{a1:prop-1.2}, p.~\pageref{a1:prop-1.2}`. 

- Reelle Zahlen etc. stehen mit `\mathbb{R}` im System, gern auch mittels `\R`, `\N` etc. eingeben.

- Den Punkt nach `e.g.` interpretiert `TeX` als Satzende. Daher `\eg`, oder `ie` oder `\resp` eingeben. 

- Beim Integral `ds` oder `dt` etc. als `\ds` oder `\dt` eingeben, damit das `d` aufrecht ist. 

Diese Definitionen finden sich alle in [`ln-definitionen.tex`](https://github.com/ugroh/AGFA-LN-POS/tree/main/author-test/preamble), die man mittels `\input` in der Präambel einbinden muss (eventuell vorher in das Arbeitsverzeichnis kopieren). Die Datei auf `GitHub` auswählen (anklicken) und man dann diese sich auf den eignen rechner herunterladen (rechts oben gibt es ein Symbol dazu).  Wichtig: Das Paket `xspace` mittels `\input{xspace}` noch in die Präambel des eigenen `TeX`-Dokuments aufnehmen. 

- Hochkommata bzw. 'Text' mittels `\enquote{Text}` oder `\enquote*{Text}` eingeben (siehe auch die Anweisung für Claude)

- Mathematikmodus: Inline via `$ Formel $` , abgesetzte Formel mit `\[ ..\]` und mehrzeilige Formeln mit der `align*`-Umgebung (können wir gern vertiefen, damit es gut wird)

##### Noch einige Tipps

- Beginnt jeden Satz auf einer neuen Zeile - macht den Text lesbarer im Source-Code.

- Leerzeilen nach % und vor % entfernen (siehe Claude-Anleitung)

- Den Text nach einem `\item` auf einer neuen Zeile beginnen.

- Mathematische Formeln strukturiert eingeben – wegen der Fehlersuche.

- Unterscheidung zwischen `-` Bindestrich, `--` von-bis-Strich, em-dash `---` für eingefügte Sätze (gibt es im Deutschen so nicht, macht hier `--`) und de´m Minuszeichen $-$ – einfach mal ausprobieren und beherzigen. 

- Unter dem Verzeichnis `springer` findet sich das Verzeichnis `springer-manuals` – dort mal [hineinsehen](https://github.com/ugroh/AGFA-LN-POS/tree/main/springer/springer-manuals)

[ulgr](ulgr@math.uni-tuebingen.de)






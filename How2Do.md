##### How2Do (Stand: 2024/02/11)

##### Struktur der Dateien

- Unter `author-test` finden sich die Unterverzeichnisse `part-a`bis `part-b`und darunter jeweils `chap-x1` bis `chap-x4`, `x=1/2/3/4`. In den letzteren sind die eizelnen `PDF` Seiten des jeweiligen Kapitels des Buches, die mithilfe von Claude in ein `LaTeX` dokument umgesetzt werden soll. Zum Testen findet man dann dort `chap-xy-test.tex` und `chap-xy.tex` zum Testen bzw. zum Speichern der umgewandelten Dateien. Bitte ausshließlich diese Struktur nutzen und nicht eigene Varianten anlegen, was nur das Leben erschwert.
- In `author-test/preamble` findet sich die jeweils aktuelle Version des Literaturverzeichnisses (was sicherlich noch zu überarbeiten ist) und die beiden Dateien, die für die Testphase erforderlich sind. Das `ln-definitionen.tex` bschreibe ich weiter unten. 
- Wer `Overleaf` nutzt: Das jewilige Unterverzeichnis inkl. der Dateien aus `author-test/preamble` zusammen als `ZIP`-File als neues Projekt hochladen und auf Overleaf weiter bearbeiten. Wer da Probleme hat: da kann ich gern helfen. 

##### Gemeinsames `LaTeX`

Damit es bei der bearbeitung einigermaßnen einheitlich zugeht bitte ich folgendes zu beachten: 

- `$$ ... $$` für abgesetzte Formeln ist verboten. Bitte `\[...\]` stattdessen nutzen.
- `eqnarray` ist verboten. Bitte die `align*` Umgebung nutzen.
- `\it`, `\bf` u.ä. Befehle für Schriftvariationen sind seit einigen Jahren nicht mehr üblich, da dies zu Problemen führen kann. Stattdesssen bitte `\textit`, `textbf` etc. nutzen.
- Ein neuer Satz beginnt auf einer neuen Zeile und Absätzte werden mittels einer Leerzeile erzeugt (und nicht durch `\\`, `\newline`o.ä. )
- Aufzählungen machen wir mithilfe des Pakes `enumitem` durch 
		``\begin{enumerate}[(i)] oder [(a)]`
		`\item`
		`Text`
		`\end{enumerate}`
	wobei `[(a)]` bei äquivalenten Bedingungen genommen wird (ausschließlich). Mithilfe des Pakes kann man noch mehr erreichen, etwa `\begin{enumerate}[(i), wide]` gibt eine Aufzählung, wobei den die gesamte textbreite genutzt wird, was sicherlich manchmal sinnvoll ist.
- Claude hat die Angewohnheit, unsere abgestzten Formeln zeilwenweise mithilfe von `\[ ...\]` zu erzeugen. Bitte dies mittels der `align*`-Umgebung ändern.
- In der `ln-definitionen.tex` Datei habe ich einige Makros erfasst, die für die Erstellung der `LaTeX` Dateien sinnvoll sind. Dazu gehört `\TT`, damit `if T is a simgroup`  das `T` in `\mathcal` erscheint., oder `\RR` oder `\ds` oder .. . Bitte die Definitionen in [`ln-definitionen.tex`]()
- 
Grundsätzlich bietet sich [Overleaf](https://www.overleaf.com/) als System zur Erstellung von `LaTeX`-Dokumenten an. Auch hat dieses System ein sehr gutes Hilfesystem. Also bei Fragen kann man dieses konsultieren. Wichtig ist aber, dass man **nur** seinen Teil dort bearbeitet und nicht das ganze System in Overleaf einstellt.

Nun zu meinen Vorschlägen zur einheitlichen Erstellung unserer `LaTeX`- Texte.

- Mithilfe von `Claude` und den regeln, die sich unter xxx finden, seitenweise von einem PDF in ein LaTeX-Dokument umwandeln. Die umgewandeltten Seiten anschließend einem testlauf unterziehen. Dazu habe ich zwei Dateien zur Verfügung gestellt. 
	
- 

- Die  `LaTeX`-Testdateien werde ich noch etwas anpassen, damit das Erstellen, das Lesen und der Vergleich mit dem Originalen besser wird. Alles dazu werde ich in das Verzeichnis [author-test/preamble](https://github.com/ugroh/AGFA-LN-POS/tree/main/author-test) stellen und euch informieren. 

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






##### How2Do (Stand: 2024/02/11)

##### Struktur der Dateien

- Unter `author-test` finden sich die Unterverzeichnisse `part-a`bis `part-b`und darunter jeweils `chap-x1` bis `chap-x4`, `x=1/2/3/4`. In den letzteren sind die einzelnen `PDF` Seiten des jeweiligen Kapitels des Buches, die mithilfe von Claude in ein `LaTeX` Dokument umgesetzt werden sollen. Zum Testen findet man dann dort `chap-xy-test.tex` und `chap-xy.tex` zum Testen bzw. zum Speichern der umgewandelten Dateien. Bitte ausschließlich diese Struktur nutzen und nicht eigene Varianten anlegen, was nur das Leben erschwert.
- In `author-test/preamble` findet sich die jeweils aktuelle Version des Literaturverzeichnisses (was sicherlich noch zu überarbeiten ist) und die beiden Dateien, die für die Testphase erforderlich sind. Das `ln-definitionen.tex` beschreibe ich weiter unten. 
- Wer `Overleaf` nutzt: Das jeweilige Unterverzeichnis inkl. der Dateien aus `author-test/preamble` zusammen als `ZIP`-File als neues Projekt hochladen und auf Overleaf weiter bearbeiten. Wer da Probleme hat: da kann ich gern helfen. 
- Und mal in die Anleitung für Claude reinsehen – da hat es noch einige Tipps. 

##### Gemeinsames `LaTeX`

Damit es bei der Bearbeitung einigermaßen einheitlich zugeht, bitte ich folgendes zu beachten: 

- `$$ ... $$` für abgesetzte Formeln ist verboten. Bitte `\[...\]` stattdessen nutzen.

- `eqnarray` ist verboten (stammt aus der Urzeit des `TeX`). Bitte die `align*` Umgebung nutzen.

- `\it`, `\bf` u.ä. Befehle für Schriftvariationen sind seit einigen Jahren nicht mehr üblich, da dies zu Problemen führen kann. Stattdessen bitte `\textit`, `textbf` etc. nutzen.

- Ein neuer Satz beginnt auf einer neuen Zeile und Absätze werden mittels einer Leerzeile erzeugt (und nicht durch `\\`, `\newline`o.ä. )

- Aufzählungen machen wir mithilfe des Pakets `enumitem` durch 
	```latex
  begin{enumerate}[(i)]
  \item
  Text
  \item
  ...
  \end{enumerate}
  ```
	wobei `[(a)]` bei äquivalenten Bedingungen genommen wird (ausschließlich). Mithilfe des Pakets kann man noch mehr erreichen, etwa `\begin{enumerate}[(i), wide]` gibt eine Aufzählung, wobei die gesamte Textbreite genutzt wird, was sicherlich manchmal sinnvoll ist. Einfach mal in die Beschreibung des Paketes [`enumiten`](https://ctan.org/pkg/translation-enumitem-de)
	
- Claude hat die Angewohnheit, unsere abgesetzten Formeln zeilenweise mithilfe von `\[ ...\]` zu erzeugen. Bitte dies mittels der `align*`-Umgebung ändern.

- In der `ln-definitionen.tex` Datei sind einige Makros erfasst, die für die Erstellung der `LaTeX` Dateien sinnvoll sind. Dazu gehört `\TT`, damit `if T is a simgroup`  das `T` in `\mathcal` erscheint. Oder `\RR` oder `\ds` oder... Bitte die Definitionen in [`ln-definitionen.tex`](https://github.com/ugroh/AGFA-LN-POS/tree/main/author-test/preamble) ansehen und nutzen. Macht den Text lesbarer.

- So gibt `\1_{A}` die charakteristische Funktion einer Menge `A`. Oder `\dt` das Differenzial etc.

- Um Querverweise richtig machen zu können, bitte Folgendes bei `\label{marke}` eingeben:

  - `\chapter{Text}\label{chap:xy}`, also etwa `\label{chap:a1}`
  - `\section{Text}\label{sec:xy-z}`, also etwa `\label{sec:a1-1}`
  - `\begin{theorem}\label{thm:xy-a.b}`, also etwa `\label{thm:a1-1.3`
  - etc.

  Dabei stehen `thm, prop, lem, cor, rem, ex`als Abkürzungen für `Theorem, Proposition, .., Example`. Dann kann via `\ref{thm:a1-1.12}` einfach verwiesen werden. 

  Bitte unbedingt noch Folgendes machen: Prüfen, ob die Nummerierungen `xy-a.b` mit denen im Buch übereinstimmen. Hier kann es Verwerfungen geben. 

- Kursiv bitte mittels `\emph{..}` eingeben und nicht `\textit` verwenden. Letzteres ist für Sätze zuständig.

- Die amerikanischen Hochkommata als `\enquote{Text}` umsetzen. Wir müssen dieses dann nach `\emph{Text}` einheitlich umwandeln. 

- Beim Integral `ds` oder `dt` etc. als `\ds` oder `\dt` eingeben, damit das `d` aufrecht ist. 

- Reelle Zahlen etc. stehen mit `\mathbb{R}` im System, gern auch mittels `\R`, `\N` etc. eingeben – mach alles lesbarer.

- Bitte prüfen, ob die Klammern dir rihtige Größe haben oder angepasst werden müssen (etwa bei Summenzeichen `\sum`). Dies bitte mittels `\left( ... \right)` machen. Gilt auch für Intervalle, etwa `[0,1]` sollte man als `\left[ 0,1 \right]`eingeben. 

- Bitte momentan die Literaturzitate belassen und diese mit `[ ]` einklammern. Umwandeln kann man es dann via `\citet{engelnagel:2006}`oder `\citet[Thm. III.4.6.]{takesaki:1979}`. Wir besprechen dies separat, da hier `BibTeX `zuschlägt.

##### `Overleaf`

- Grundsätzlich bietet sich [Overleaf](https://www.overleaf.com/) als System zur Erstellung von `LaTeX`-Dokumenten an. Auch hat dieses System ein sehr gutes Hilfesystem. Also bei Fragen kann man dieses konsultieren. Wichtig ist aber, dass man **nur** seinen Teil dort bearbeitet und nicht das ganze System in Overleaf einstellt. Dabei lädt man das Kapitel, für das man zuständig ist, als `ZIP`-Datei und als neues Projekt hoch. 

##### Noch einige Tipps

- Beginnt jeden Satz auf einer neuen Zeile - macht den Text lesbarer im Source-Code.

- Leerzeilen nach % und vor % entfernen (siehe Claude-Anleitung), sonst wird ein neuer Absatz erzeugt.

- Den Text nach einem `\item` auf einer neuen Zeile beginnen.

- Mathematische Formeln strukturiert eingeben – wegen der Fehlersuche.

- Unterscheidung zwischen `-` Bindestrich, `--` von-bis-Strich, em-dash `---` für eingefügte Sätze (gibt es im Deutschen so nicht) und dem Minuszeichen $-$ – einfach mal ausprobieren

- Unter dem Verzeichnis `springer` findet sich das Verzeichnis `springer-manuals` – dort mal [hineinsehen](https://github.com/ugroh/AGFA-LN-POS/tree/main/springer/springer-manuals)

[ulgr](ulgr@math.uni-tuebingen.de)






### Zehn+ Tipps für die Bearbeitung 


#### `LaTeX`


  - Jeder Satz beginnt auf einer neuen Zeile. Das macht die Fehlersuche einfacher und das Lesen leichter.

  - Einen neuen Absatz erreicht man mithilfe einer Leerzeile. Bitte nicht `\\`, `\newline` oder ähnliche Konstruktionen nutzen – eine Leerzeile genügt.

  - Die richtigen US-Anführungszeichen bekommt man mit `\enquote{Text}` bzw. \enquote*{Text}
  
  - Hervorhebungen im Text (kursiv) nicht mit `\textit{kursiv}`, sondern stets mit `\emph{kursiv}` – der erste Befehl ist für längere Textstellen.

  - Ein Gedankenstrich ist etwas anderes als ein Bindestrich oder ein Minuszeichen (--, - , $-$) 

  - Die  Eingabe von Aufzählungen erfolgt mittels `\begin{enumerate}[label]` `\item` `\end{enumerate}` wobei `label` etwa `(i)` für eine nummerierte Aufzählung und `(a)` für Äquivalenzen ist. 

  - Die Eingabe mathematischen Textes: `$ -- $` für inline Ausdrücke und `\[ ... \]` für abgesetzte Formeln. Bitte sich auch `align` ansehen, etwa in AMS 

  - Querverweise: bitte `\ref{link}` nutzen. 

  - Zitieren von Literatur: `\cite[wo-steht-etwas]{link}` oder `\cite{link}`. 
  
  - Beim Verwenden von URL-Links bitte ich darum, diese abzukürzen. Dazu nutzen wir einheitlich [https://tinyurl.com](https://tinyurl.com) – dies gilt auch für die URL-Links für Referenzen (Literaturzitate).
  
Details dazu in `How2Do.pdf` (kommt noch)

#### Vom `PDF` zur `LaTeX`-Datei (wird ergänzt)

 - Einen User auf [Claude][https://console.anthropic.com] anlegen
 
 - Mal Claude etwas ausprobieren.
 
 - Für die Konvertierung:
 	- Anleitung zur Konvertierung an Claude schicken
 	- PDF-Datei mittels Copy&Paste Claude zur Verfügung stellen
 	- Das Ergebnis mittels Copy&Paste in die TeX-Datei kopieren
 	- Unbedingt testen
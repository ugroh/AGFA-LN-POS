### AGFA-LN-POS: Neuauflage das Buches LN1184

[LN 1184 als PDF](https://github.com/ugroh/AGFA-LN-POS/blob/main/ablage-orig/ln-orig/ln-pos-1184.pdf) ist vorhanden. Des weiteren sind die einzelnen Kapitel parallel heruntergeladen worden und als `LN-chap-xx.pdf` abgespeichert (siehe unten für weitere Erläuterungen dazu). Alles auf Gihub kann man sich herunterladen (grüner Knopf `Code` und dort als `zip`-Datei herunterladen).

__Achtung__: Bitte nichts an der Datei `LN-Book.tex` ändern, höchstens mal reinschauen. 

#### Die Struktur

* `AGFA-LN-POS` ist das Masterverzeichnis unter dem sich die weiteren Verzeichnisse befinden. Im Einzelnen:

	* `ablage-final:` Dies ist das Verzeichnis, in dem die finalen Beiträge abgelegt sind. 
	* `ablage-test:` Dies ist das Verzeichnis, das die noch nicht fertigen `TeX`-Dateien enthält. 
	* `springer:` Hier finden sich die Dateien des Pakets von Springer. Für Erstellung der einzelnen Beiträge sind diese nicht erforderlich. Wer dennoch die Dateien nutzen will (`svmono`), muss die in `springer/springer-style` sich befindlichen in auf seinen PC installieren (oder `Overleaf` nutzen).
	
#### Der Aufbau von `author-test`

Der Aufbau ist wie folgt (analog dann auch für die anderen Teile):

*  Das Unterverzeichnis `part-a` enthält die zugehörigen Kapitel, d.h. `chap-a1 ` bis `chap-a4`. In diesem befinden sich dann die jeweiligen Kapitel, in der Form `LN-chap-a1.pdf` und die einzelnen Seiten dieses Kapitels, also `ln-chap-a1_1.pdf` etc. 
* Des weiteren die beiden `TeX`-Dateien `chap-a1-test.tex` und `chap-a1.tex` die zum Testen des jeweiligen Kapitels genutzt werden. 
* Ist ein solches Kapile vollständig fertig, dann wird es nach `author-final/part-a/chap-a1.tex` kopiert. 

Das Verzeichnis `author-final` ist analog aufgebaut, wobei aber auf eine nochmalige Verfeinerung verzichtet wurde. 

#### Vom `PDF` zum `LaTeX`-Dokument

Dazu habe ich  die KI [Claude](http://claude.ai) genutzt. Das Vorgehen:

* Anmelden bei Claude und eine Session starten.
* Claude mitteilen, dass man ein `PDF`in `LaTeX` umsetzen will.
* Im dabei die unten stehen Anleitung mitgeben.
* Dann in das Unterverzeichnis unter `author-test/part-a/chap-a1` gehen, für das man zuständig ist und eine der Seiten des Kapitels mit Copy&Paste bei Claude einsetzen. 
* Nachdem Claude fertig ist, dieses umgesetzte Dokument via Copy&Paste in das `TeX` File `chap-a1.tex` kopieren (analog bei den anderen).

Wenn man dieses systematisch macht, also bei `\_1`anfängt, hat man nach x-Stunden das Kapitel fertig und kann sich nun um die redaktionelle Arbeit kümmern. 


#### Anleitung für Claude

1. Leerzeilen bleiben erhalten
2. Jeder neue Satz auf eine neue Zeile aber ohne eine Leerzeile dazwischen
3. Vor \[ und nach \] eine neue Zeile einfügen mit %% -- 
4. ^a und \_a stest in {} einklammern
5. Listen mit \begin{enumerate}[(i)] oder [(a)] setzen (je nach Fall
6. Theoreme etc mit \label versehen, etwa \label{thm:nummer}; entsprechend bei Definitionen etc.
7. Hochkommata mit \enquote{text} schreiben
8. den Text nach \item auf eine neue Zeile setzen
9. Eventuelle Leerzeilen nach bzw. vor %% -- wegmachen
10. Diagramme mit `Tikz` setzen



[U. Groh](ulgr@math.uni-tuebingen.de)


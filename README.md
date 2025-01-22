### AGFA-LN-POS: Neuauflage das Buches LN1184 (Stand: 2024/01/20)

[LN 1184 als PDF](https://github.com/ugroh/AGFA-LN-POS/blob/main/ablage-orig/ln-orig/ln-pos-1184.pdf) ist vorhanden. Des weiteren sind die einzelnen Kapitel parallel heruntergeladen worden und als `LN-chap-xx.pdf` abgespeichert (siehe unten für weitere Erläuterungen dazu). Alles auf Gihub kann man sich herunterladen (grüner Knopf `Code` und dort als `zip`-Datei herunterladen).

__Achtung__: Bitte nichts an der Datei `LN-Book.tex` ändern, höchstens mal reinschauen. 

Die Vorlagen und weitere Erläuterungen finden sich auf der [Springer-Webseite](https://www.springernature.com/gp/authors/campaigns/latex-author-support) bzw. im Unterverzeichnis `springer`. 

#### Die Struktur

* `AGFA-LN-POS` ist das Masterverzeichnis unter dem sich die weiteren Verzeichnisse befinden. Im Einzelnen:

	* `ablage-final:` Dies ist das Verzeichnis, in dem die finalen Beiträge abgelegt sind. Dies sollte momentan nicht benutzt werden. 
	* `ablage-test:` Dies ist das Verzeichnis, das die noch nicht fertigen `TeX`-Dateien enthält. In diesem sind alle Kapitel enthalten (Reihenfolge wie im Buch) und man sich eines dieser Verzeichnisse herunterladen und bearbeiten.
	* `springer:` Hier finden sich die Dateien des Pakets `svmono` und `svmult`von Springer. Für Erstellung der einzelnen Beiträge sind diese nicht erforderlich. Wichtiger wäre es, mal in die Dokumente reinzusehen, die sich unter `springer-manuals`finden. 
	
#### Der Aufbau von `author-test`

Der Aufbau ist wie folgt (analog dann auch für die anderen Teile):

*  Das Unterverzeichnis `part-a` enthält die zugehörigen Kapitel, d.h. `chap-a1 ` bis `chap-a4`. In diesem befinden sich dann die jeweiligen Kapitel, in der Form `LN-chap-a1.pdf` und die einzelnen Seiten dieses Kapitels, also `ln-chap-a1_1.pdf` etc. 
* Des weiteren die beiden `TeX`-Dateien `chap-a1-test.tex` und `chap-a1.tex` die zum Testen des jeweiligen Kapitels genutzt werden. 
* Ist ein solches Kapitelvollständig fertig, dann wird es nach `author-final/part-a/chap-a1.tex` kopiert. 

Das Verzeichnis `author-final` ist analog aufgebaut, wobei aber auf eine nochmalige Verfeinerung verzichtet wurde. 

#### Literatur zu `LaTeX`

Wer Literatur benötigt – bitte mich anschreiben. Bitte auch das Dokument (*muss noch erstellt werden*) `LaTeX-HowDo` beachten, in der einige Regeln festgehalten sind, damit die Dokumente einheitlich werden.

#### Vom `PDF` zum `LaTeX`-Dokument

Dazu habe ich  die KI [Claude](http://claude.ai) genutzt. Das Vorgehen:

* Anmelden bei Claude und eine Session starten.
* Claude mitteilen, dass man ein `PDF`in `LaTeX` umsetzen will und ihm dabei die unten stehen Anleitung mitgeben.
* Dann in das Unterverzeichnis unter `author-test/part-a/chap-a1` gehen, für das man zuständig ist und eine der Seiten des Kapitels mit Copy&Paste bei Claude einsetzen.
* Nachdem Claude fertig ist, dieses umgesetzte Dokument via Copy&Paste in das `TeX` File `chap-a1.tex` kopieren (analog bei den anderen).
* Wenn man alle Seiten umgesetzt hat, dan kann man das `LaTeX`-Dokument überarbeiten.
* Ist man der Meinung, alles final zu haben, dann kommt dieses Dokument in das entsprechende Kapitel unter `author-final`.
* Alle bearbeiteten `pdf`-Seiten kommen in das Unterverzeichnis `bearbeitet`. 
+ Kleiner Tipp: In der zugehörigen `LaTeX`-Datei ist es sinnvoll, einen Kommentar wie `%% -- a1_1` einzufügen und danach dann die erste umgewandelte Seite zu speichern. Dann ein `%% -- a1_2` und danach dann die zweite umgewandelte Seite zu speichern. Macht die Fehlerkorrekturen beim Verleich zum `pdf` einfacher.

Wenn man dieses systematisch macht, also bei `a1_1`anfängt, hat man nach x-Stunden das Kapitel fertig und kann sich nun um die redaktionelle Arbeit kümmern. Natürlich kann man sich auch ein anderes Kapitel vornehmen – der Ablauf ist immer der gleiche.

*Zur Beachtung:* Bei dieser Methode kann es sein, dass Fehlermeldungen auftauchen, dass irgendwelche Umgebungen nicht beendet wurden. Dies kann man aber einfach klären, wenn man regelmäßig das Hauptdokument `chap-a1-test.tex` aufruft (am besten, nachdem man in `cahap-a1.tex` kopiert hat.)


#### Anleitung für Claude

Damit die label eindeutig werden, bitte bei Punkt 6 angeben, um welches Kapitel es sich handelt. Also `\\label{thm:a2-nummer}` etwa angeben (sollte klar sein, was gemeint ist)

1. Leerzeilen bleiben erhalten
2. Jeder neue Satz auf eine neue Zeile aber ohne eine Leerzeile dazwischen
3. Vor \\[ und nach \\] eine neue Zeile einfügen mit %% -- 
4. Bei Subskripts: \_a wird zu \_{a}
	Bei Superskripts: ^a wird zu ^{a}
	Dies gilt auch für zusammengesetzte Ausdrücke und griechische Buchstaben
5. Listen mit \\begin{enumerate}[(i)] oder [(a)] setzen (je nach Fall
6. Theoreme etc mit \\label versehen, etwa \\label{thm:d3-nummer}; entsprechend bei Definitionen, Corollary, Proposition, Remark, Example etc.
7. Hochkommata mit \\enquote{text} schreiben
8. den Text nach \\item auf eine neue Zeile setzen
9. Eventuelle Leerzeilen nach bzw. vor %% -- wegmachen
10. Diagramme mit `Tikz` setzen
11. Alle griechischen Buchstaben oder mathematische Zeichen in LaTeX-Code umsetzen.
12. Vor und nach einer mathematischen Bezeichnung bitte eine Leerstelle einfügen, also NICHT a\\tob sondern a \\to b .
13. Mehrzeilige mathematische Formeln bitte mit \\begin{align\*} .. \\end{align\*} setzen, einzeilige aber weiterhin mit \\[ .. \\] wie oben beschrieben. 
13. Aufzählungen, die mit Zahlen nummeriert sind, bitte mit [(i)] in der enumerate-Umgebung setzen. Listen, die mit Buchstaben nummeriert sind, bitte mit [(a)] in der  enumerate-Umgebung setzen. 

#### Einige Tools

##### Literaturzitate

In `author-test/bib` findet sich ein Pythonprogramm `convert2bib_ref.py`, mithilfe dessen man Literaturzitate der Form `[Bratteli-Robinson (1979)]` oder `[Takesaki (1979), Chapter III]` in `\cite{bratelli_robinson:1979}` oder `\cite[Chapter III]{takesaki:1979}` umwandeln kann. Daher bitte die Zitate im LN so belassen (auch nach der Umsetzung) aber eventuell mit `[ ]` einklammern, falls dies nicht der Fall sein sollte.

Unter `author-test/bib` findet sich die Literaturdatenbank `ln-references-bib`. Diese und die `bst`-Datei (um es einfach zu machen) zur `TeX`-Datei kopieren (s.u.). Die Testdateien sind angepasst. 

##### Installation

* Die `bst`-Datei `spmpsci.bst` muss in einem Verzeichnis liegen, das TeX finden kann. Das bedeutet:

1. Entweder im gleichen Verzeichnis wie die `TeX`-Datei
2. Oder im lokalen texmf-Baum,:
   - Windows: `C:\Users\IhrName\texmf\bibtex\bst\`
   - macOS: `~/Library/texmf/bibtex/bst/`
   - Linux: `~/texmf/bibtex/bst/`

Um herauszufinden, ob TeX die Datei findet, auf der Kommandozeile `kpsewhich spmpsci.bst` eingeben. Dies zeigt an wo TeX nach der Datei sucht.

Die sauberste Lösung ist, die Datei im lokalen texmf-Baum zu installieren. 

##### Nützlich

Nützlich ist noch das Programm `bibtool`, das man sich mit `brew install bib-tool` installieren kann. Möglichkeit: Auslesen der verwendeten Literatur (wird ergänzt).

Dies erfolgt mittels (Muster)

`bibtool -x chap-d1-test.aux -i ln-references.bib -o new-references.bib`

mit Pfad zur `bib`-Datei (bei mir `/Users/ugroh/Library/texmf/bibtex/bib/ln-references.bib`)

Literatur: [bibtool-manual](https://ctan.org/pkg/bibtool)





[U. Groh](ulgr@math.uni-tuebingen.de)


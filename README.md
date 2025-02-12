#### AGFA-LN-POS: Neuauflage das Buches LN1184 (Stand: 2024/02/11)

Das Projekt ist es, das Buch [LN 1184](https://github.com/ugroh/AGFA-LN-POS/blob/main/ablage-orig/ln-orig/ln-pos-1184.pdf), das im `PDF`-Format vorhanden ist, in das `LaTeX` umzuwandeln. Um dieses strukturiert anzugehen, ist auf `GitHub` das Repository [AGFA-LN-POS](https://github.com/ugroh/AGFA-LN-POS) angelegt worden, in dem sich alles findet, was dazu erforderlich ist. Man kann sich dieses herunterladen (grüner Knopf `Code` und dort als `zip`-Datei herunterladen) oder auch einzelne Dateien (Datei anklicken und dann findet sich rechts oben das Symbol dazu). Dann kann man alles löschen, was für die persönliche Bearbeitung unerheblich ist, d.h. alles außer `author-test` (aber siehe unten).

Die Vorlagen und weitere Erläuterungen finden sich auf der [Springer-Webseite](https://www.springer.com/gp/authors-editors/book-authors-editors/your-publication-journey/manuscript-preparation) bzw. im Unterverzeichnis `springer`. Weiteres für eine einheitliche Eingabe findet sich im [How2Do](https://github.com/ugroh/AGFA-LN-POS/blob/main/How2Do.pdf).

##### Die Struktur

* `AGFA-LN-POS` ist das Masterverzeichnis, unter dem sich die weiteren Verzeichnisse befinden. Im Einzelnen:
	* `ablage-test:` Dies ist das Verzeichnis, das die noch nicht fertigen `TeX`-Dateien enthält. In diesem sind alle Kapitel enthalten (Reihenfolge wie im Buch) .
	
	* Das Unterverzeichnis `preamble` enthält die folgenden `TeX`-Dateien:
	
	  * `ln-defintionen.tex`enthält die Abkürzungen, die für die richtige Erstellung der Vorlagen erforderlich sind (beschrieben im `How2Do`).
	  * `ln-preamble.tex`: Hier ist alles zusammengefasst, was wir für die Testphase nutzen. 
	  * `ln-references.bib`: Die Literaturdatenbank.

​		Dies drei Dateien in das jeweilge Arbeitsverzecinis kopieren, da diese genutzt werden.  Besser: In den lokalen `TeX`Datenbaum kopieren, üblicherweise nach `texmf/tex/latex` bzw. `bibtex/bib`	

* `springer:` Hier finden sich die Dateien des Pakets `svmono` und `svmult`von Springer. Für die Erstellung der einzelnen Beiträge sind diese nicht erforderlich. Wichtiger wäre es, mal in die Dokumente hereinzusehen, die sich unter `springer-manuals`finden. 
	
* `literatur:` Wie der Name sagt – ergänzende Literatur zum Hineinschauen, insbesondere in den `Grätzer`.

#### Der Aufbau von `author-test`

Der Aufbau ist wie folgt (analog dann auch für die anderen Teile):

* Es findet sich  in `part-a` die Kapitel `chap-a1` bis `chap-a4`– analog geht es dann weiter.
	* In etwa `chap-a4` finden sich dann das `PDF` dieses Kapitels, `LN-chap-a4.pdf` als Gesamtübersicht und die einzelnen Seiten `ln-chap-a4_01.pdf` bis (hier) `ln-chap-a4_14.pdf`. 
	* Diese Seiten werden - einzeln - mithilfe von `Claude` in `LaTeX` übersetzt und die umgewandelte Seite in die `TeX`-Datei `chap-a4.tex` einkopiert, überarbeitet und mittels `chap-a4-test.tex` getestet.

Ist ein solches Kapitel vollständig fertig und bereinigt, so bitte als  `chap-a1.tex` an mich schicken. 

Noch ein Hinweis: Da einzelne Seiten konvertiert werden, ist es sinnvoll, in der `TeX`-Datei dies mittels

	\newpage
	%% -- a4-n

zu strukturieren, wobei `n` die Seitennummer des PDFs ist, das man umgewandelt hat. Dann kann man relativ einfach das neue PDF mit dem Original vergleichen und Fehler finden.

##### Literatur zu `LaTeX`

Nützlich:
- [lshort](https://ctan.org/pkg/lshort-german) Eine kurze Einführung in die wesentlichen Aspekte von `LaTeX`
- [AMS-Math](https://ctan.org/pkg/short-math-guide): Die wichtigen Punkte für die Eingabe mathematischer Texte

Wer weitergehende Literatur benötigt – bitte mich anschreiben – und bitte das Dokument [How2Do](https://github.com/ugroh/AGFA-LN-POS/blob/main/How2Do.pdf) beachten

#### Vom `PDF` zum `LaTeX`-Dokument

Dazu die KI [Claude](http://claude.ai) nutzen: 

* Anmelden bei Claude und eine Session starten und am Anfang mal mit dem System etwas »spielen«
* Claude mitteilen, dass man ein `PDF`in `LaTeX` umsetzen will und ihm dabei die [Anleitung mitgeben](https://github.com/ugroh/AGFA-LN-POS/blob/main/anleitung-claude.md), etwa mit `Copy&Paste`. Ihn aber fragen, ob er alles verstanden hat (kann man mehrmals machen)
* Dann in das Unterverzeichnis unter `author-test/part-a/chap-ax` gehen, für das man zuständig ist und die Seiten des Kapitels mit `Copy&Paste` bei Claude einsetze`:
	* Die jeweilige Seite via `Copy & Paste` in die Claude-Chatseite einkopieren
	* Abwarten, was Claude damit macht und ihm eventuell Hinweise geben, was er besser machen soll
	* Die umgesetzte Seite in `chap-ax.tex`kopieren und einen Testlauf mit `LaTeX` machen. Eventuelle Fehler werden so seitenweise schnell erkannt und können korrigiert werden. Manchmal fehlen eventuell `\end{}` Befehle. Die kann man zwischenzeitlich am Ende der jeweiligen Seite einfügen und beim nächsten Mal, wenn diese entbehrlich sind, entfernen.
* Wenn man alle Seiten umgesetzt hat, dann kann man das `LaTeX`-Dokument überarbeiten und zur weiteren Korrektur weitergeben. 
* Man sollte regelmäßig einen neuen Chat mit Claude starten, da er sonst sehr langsam wird und auch eventuell das Arbeiten einstellt.

Wenn man dieses systematisch macht, also bei `ax_01`anfängt, hat man nach z-Stunden das Kapitel fertig und kann sich nun um die redaktionelle Arbeit kümmern. Natürlich kann man sich auch ein anderes Kapitel vornehmen – der Ablauf ist immer der gleiche.

##### Literaturzitate, Referenzen und Index

* Bitte momentan die Literaturzitate belassen und diese mit `[ ]` einklammern - siehe `How2Do`
* Bei der Überarbeitung der `LaTeX` Datei bitte die Querverweise setzen – in  `How2Do` finden sich Informationen dazu.
* Claude baut bereits jetzt bei den Abschnitten den `\index{}` Befehl ein (siehe die Anleitung für Claude). Bitte dies momentan so stehen lassen. Wir müssen dies dann noch gemeinsam überarbeiten.


[U. Groh](ulgr@math.uni-tuebingen.de)


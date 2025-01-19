### AGFA-LN-POS: Neuauflage das Buches LN1184


[LN 1184 als PDF](https://github.com/ugroh/AGFA-LN-POS/blob/main/ablage-orig/ln-orig/ln-pos-1184.pdf)

#### Struktur

* AGFA-LN-POS ist das Masterverzeichnis. Darunter befinden sich
	* ablage-orig: Hier finden sich die PDF's der einzelnen Kapitel einmal als Gesamt-PDF als auch aufgeteilt in die einzelnen Seiten. Also aus `foo.pdf` werden dann `foo\_1.pdf` bis `foo\_n.pdf`, wenn es n Seiten gibt.
	* author: Hier finden sich die finalen `TeX` Dateien.
	* python: nur relevant für mich
	etc. 


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

#### Nützlich

Erzeugen von vielen Dateien auf einmal:

`for i in {1..21}; do touch ln-part-d3_$i.tex; done`


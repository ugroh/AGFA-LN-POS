### AGFA-LN-POS: Neuauflage das Buches LN1184


[Link zu Springer](https://www.springer.com/gp/authors-editors/book-authors-editors/your-publication-journey)

#### Struktur



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


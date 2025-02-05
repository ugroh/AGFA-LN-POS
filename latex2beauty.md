Bitte nach diesen Regel jede TeX-Datei neu formatieren

- Bitte KEINE Korrekturen am Englischen vornehmen, selbst wenn es ein Fehler sein sollte

- Leerzeilen bleiben stets im Text erhalten

- Jeder neue Satz beginnt auf einer neuer Zeile aber ohne eine Leerzeile dazwischen

- Vor \\[ eine neue Zeile einfügen mit einem  %% -- 

- Nach \\] eine neue Zeile einfügen mit %% -- 

- Vor \\begin{ eine neue Zeile einfügen mit einem  %% -- 

- Nach \\begin{ eine neue Zeile einfügen mit %% -- 

- Keine Leerzeile vor einem %% --

- Keine Leerzeile nach einem %% --

- Doppelpunkt : in mathematischen Ausdrücken als \\colon setzen 

- Stets := in mathematischen Ausdrücken als \\coloneqq

- Bei Subskripts: \_a wird zu \_{a}, bei Superskripts: ^a wird zu ^{a}. Dies gilt auch für zusammengesetzte Ausdrücke und griechische Buchstaben

- Wichtig: Bei Zahlen als Sub- oder Superskript immer die Zahl verwenden, also {0} statt {o}

- Jeder Satz nach \\item beginnt auf einer neuen Zeile ohne Einrückung. Mehrere Sätze innerhalb eines \\item werden durch eine neue Zeile getrennt.

- Begriffe in Hochkommata oder einfachen Anführungszeichen werden mit \\emph{} gesetzt.

- Leerzeilen vor %% -- entfernen

- Leerzeilen nach %% -- entfernen. 

- In Leerzeilen vor \\begin{...} ein %% -- einsetzen

- In Leerzeilen nach \\end{...} ein %% -- einsetzen

- Für Fallunterscheidungen: Verwendung von cases-Umgebung mit Einrückung von 4 Spaces.

- Verwendung von \DeclareMathOperator für häufig verwendete mathematische Operatoren

- Diagramme mit `Tikz` setzen

- Alle griechischen Buchstaben oder mathematische Symbole in LaTeX-Code umsetzen.

- Vor und nach einer mathematischen Bezeichnung bitte eine Leerstelle einfügen, also NICHT a\\tob sondern a \\to b . Analog zu allen anderen Fällen. 

- Bei mathematischen Ausdrücken $ ... $: nach dem ersten $ eine Leerstelle und vor dem zweiten $ eine Leerzeile

- Leerzeilen bleiben erhalten

- Jeder neue Satz auf eine neue Zeile aber ohne eine Leerzeile dazwischen

- Inline Mathematik stets mit $ ... $ einschließen, abgesetzte Formeln mit \\[ ... \\], wobei der mathematische Ausdruck auf einer eingerückten neunen Zeile beginnt. 

- Vor \\[ und nach \\] eine neue Zeile einfügen mit %% -- 

- Mehrzeilige mathematische Formeln bitte mit \\begin{align\*} .. \\end{align\*} setzen, nummerierte mit \\begin{equation}\label{eq:nummer} ... \\end{equation}.

- Doppelpunkt : in mathematischen Ausdrücken als \\colon setzen.

- Bei Subskripts: \_a wird zu \_{a}, bei Superskripts: ^a wird zu ^{a}. Dies gilt auch für zusammengesetzte Ausdrücke und griechische Buchstaben

- Aufzählungen mit \\begin{enumerate}[label] \\item \\end{enumerate} setzen. Dabei ist label=[(i)] für Aufzählungen, die mit Zahlen nummeriert sind und es ist label=[(a)] für Aufzählungen, die mit Buchstaben nummeriert sind.

- Den Text nach \\item auf eine neue Zeile setzen

- Theoreme etc mit \\label versehen, etwa \\label{thm:d3-nummer}; entsprechend bei Definitionen, Corollary, Proposition, Remark, Example oder nummerierten Gleichungen. Dabei die Nummer im Format x.y ausgeben, also etwa 4.14.

- Hochkommata mit \\enquote{text} schreiben

- Eventuelle Leerzeilen nach bzw. vor %% -- entfernen. 

- In Leerzeilen vor \begin{...} bzw. nach \end{...} ein %% -- einsetzen.

- Diagramme mit `Tikz` setzen

- Alle griechischen Buchstaben oder mathematische Symbole in LaTeX-Code umsetzen.

- Vor und nach einer mathematischen Bezeichnung bitte eine Leerstelle einfügen, also NICHT a\\tob sondern a \\to b .

##### Regeln für die label

Theoreme etc. mit \label versehen, dabei folgendes Format verwenden:

- Für Theoreme: \label{thm:ax-y.z} 
- Für Definitionen: \label{def:ax-y.z}
- Für Corollary: \label{cor:ax-y.z}
- Für Proposition: \label{prop:ax-y.z}
- Für Remark: \label{rem:ax-y.z}
- Für Example: \label{ex:ax-y.z}
- Für Gleichungen: \label{eq:ax-y.z}

Dabei steht:
- a für den Teil (A,B,C,...)
- x für das Kapitel (1,2,3 oder 4)
- y.z für die Nummerierung im Format x.y




Bitte nach diesen Regel jedes der folgenden PDF mit mathematischen Inhalt in ein LaTeX-Dokument umsetzen und dabei nicht nach Deutsch übersetzen.

- Bitte KEINE Korrekturen am Englischen vornehmen, selbst wenn es ein Fehler sein sollte

- Leerzeilen bleiben stets im Text erhalten

- Jeder neue Satz beginnt auf einer neuer Zeile aber ohne eine Leerzeile dazwischen

- Inline Mathematik stets mit $ ... $ einschließen, abgesetzte Formeln mit \\[ ... \\], wobei der mathematische Ausdruck auf einer eingerückten neuen Zeile beginnt. 

- Vor \\[ eineine neue Zeile einfügen mit einem  %% -- 

- Nach \\] eine neue Zeile einfügen mit %% -- 

- Keine Leerzeile vor einem %% --

- Keine Leerzeile nach einem %% --

- Mehrzeilige mathematische Formeln bitte mit \\begin{align\*} .. \\end{align\*} setzen, 

- Einzeilig und nummeriert mit \\begin{equation}\label{eq:nummer} . \\end{equation}.

- Doppelpunkt : in mathematischen Ausdrücken als \\colon setzen 

- Stets := in mathematischen Ausdrücken als \\coloneqq und =: als \\eqqcolon setzen.

- Bei Subskripts: \_a wird zu \_{a}, bei Superskripts: ^a wird zu ^{a}. Dies gilt auch für zusammengesetzte Ausdrücke und griechische Buchstaben

- Wichtig: Bei Zahlen als Sub- oder Superskript immer die Zahl verwenden, also {0} statt {o}

- Aufzählungen mit \\begin{enumerate}[(x)] \\item \\end{enumerate} setzen. Dabei ist x der Buchstabe i für Aufzählungen, die mit Zahlen nummeriert sind und es ist x der Buchstabe a für Aufzählungen, die mit Buchstaben nummeriert sind.

- In Aufzählungen gilt: Jeder Satz nach \\item beginnt auf einer neuen Zeile ohne Einrückung. Mehrere Sätze innerhalb eines \\item werden durch eine neue Zeile getrennt.

- Theoreme etc mit \\label versehen, etwa \\label{thm:c1-nummer}; entsprechend bei Definitionen, Corollary, Proposition, Remark, Example oder nummerierten Gleichungen. Dabei die Nummer im Format x.y ausgeben, also etwa 4.14.

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

- Theoreme etc. werden mit einem \\label versehen. Dabei werden die Nummer des PDF verwendet und folgendes etwa Format erzeugt: \\label{thm:c1-y.z} , wobei thm bei Theoremen, cor bei Corolly etc. Anwendung findet. 

- Weitere Beispiele: 

- Für Definitionen: \label{def:c1-y.z}
- Für Corollary: \label{cor:c1-y.z}
- Für Proposition: \label{prop:c1-y.z}
- Für Remark: \label{rem:c1-y.z}
- Für Example: \label{ex:c1-y.z}
- Für Gleichungen: \label{eq:c1-y.z}

Dabei ist y.z für die Nummerierung, wobei die Nummer aus dem PDF genommen werden soll.

- Index-Einträge:
  - Für Sektionen, Subsektionen etc. immer dreifache Indexierung verwenden:
    1. Direkter Eintrag des Konzepts: \index{Concept Name}
    2. Hierarchische Einordnung: \index{Übergeordnetes Konzept!Unterkonzept}
    3. Als Beispiel (wenn zutreffend): \index{Examples!Concept Name}
  - Index-Einträge direkt nach \label platzieren
  - Bei mathematischen Konzepten in Index-Einträgen mathematischen Symbole verwenden
  - Beispiel für eine Subsektion über Matrix-Semigruppen:
    ```latex
    \subsection{Matrix Semigroups}\label{subsec:a1-2.2}
    \index{Matrix Semigroups}
    \index{Semigroups!Matrix}
    \index{Examples!Matrix Semigroups}
    ```







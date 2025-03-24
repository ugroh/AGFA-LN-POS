## Anleitung zur Umwandlung von PDF-Dokumenten mit mathematischem Inhalt in LaTeX

Bitte nach diesen Regel jedes der folgenden PDF mit mathematischen Inhalt in ein LaTeX-Dokument umsetzen und dabei nicht nach Deutsch übersetzen.

### 1. Grundlegende Textformatierung

- Originaltext genau übernehmen, KEINE Korrekturen am Englischen vornehmen, selbst bei erkennbaren Fehlern
- Keine Übersetzung ins Deutsche durchführen
- Jeder neue Satz beginnt auf einer neuen Zeile ohne Leerzeile dazwischen
- Leerzeilen aus dem Original bleiben im Text erhalten
- Begriffe in Hochkommata oder einfachen Anführungszeichen mit `\emph{}` setzen

### 2. Mathematische Notation

#### 2.1 Grundformate
- Inline-Mathematik stets mit `$ ... $` einschließen
- Abgesetzte Formeln mit `\[ ... \]` umschließen, wobei:
  - Vor `\[` eine neue Zeile mit `%% --` einfügen (ohne Leerzeile davor oder danach)
  - Nach `\]` eine neue Zeile mit `%% --` einfügen (ohne Leerzeile davor oder danach)
  - Der mathematische Ausdruck beginnt auf einer eingerückten neuen Zeile
  - Keine Leerzeilen vor oder nach den `%% --` Markierungen

#### 2.2 Spezielle Formeln
- Mehrzeilige mathematische Formeln mit `\begin{align*} .. \end{align*}` setzen
- Einzeilige nummerierte Formeln mit `\begin{equation}\label{eq:c1-y.z} ... \end{equation}` setzen
- Für Fallunterscheidungen: `cases`-Umgebung mit Einrückung von 4 Spaces verwenden

#### 2.3 Mathematische Symbole und Notation
- Doppelpunkt `:` in mathematischen Ausdrücken als `\colon` setzen
- Definitionszeichen `:=` als `\coloneqq` und `=:` als `\eqqcolon` setzen
- Bei Subskripts: `_a` wird zu `_{a}`, bei Superskripts: `^a` wird zu `^{a}`
  - Dies gilt auch für zusammengesetzte Ausdrücke und griechische Buchstaben
  - Bei Zahlen als Sub- oder Superskript immer die Zahl verwenden, also `{0}` statt `{o}`
- Vor und nach einem mathematischen Operator eine Leerstelle einfügen (z.B. `a \to b` statt `a\to b`)
- Häufig verwendete mathematische Operatoren mit `\DeclareMathOperator` definieren

### 3. Strukturelemente

#### 3.1 Umgebungen
- In Leerzeilen vor `\begin{...}` ein `%% --` einsetzen (ohne Leerzeile danach oder davor)
- In Leerzeilen nach `\end{...}` ein `%% --` einsetzen (ohne Leerzeile danach oder davor)

#### 3.2 Aufzählungen
- Aufzählungen mit `\begin{enumerate}[(x)] \item ... \end{enumerate}` setzen
  - `x` ist `i` für numerische Aufzählungen
  - `x` ist `a` für alphabetische Aufzählungen
- In Aufzählungen:
  - Jeder Satz nach `\item` beginnt auf einer neuen Zeile ohne Einrückung
  - Mehrere Sätze innerhalb eines `\item` werden durch eine neue Zeile getrennt

#### 3.3 Theoreme und spezielle Umgebungen
- Theoreme und ähnliche Umgebungen stets mit `\label` versehen
- Folgende Konvention für Label-Namen verwenden:
  - Theorem: `\label{thm:c1-y.z}`
  - Definition: `\label{def:c1-y.z}`
  - Corollary: `\label{cor:c1-y.z}`
  - Proposition: `\label{prop:c1-y.z}`
  - Remark oder Remarks: `\label{rem:c1-y.z}`
  - Example oder Examples: `\label{ex:c1-y.z}`
  - Equation: `\label{eq:c1-y.z}`
- Dabei ist `c1` der Dokumentbezeichner und `y.z` die Nummerierung aus dem PDF

### 4. Spezielle Elemente

#### 4.1 Diagramme
- Diagramme mit `TikZ` setzen

#### 4.2 Indexeinträge
- Für Sektionen, Subsektionen etc. immer dreifache Indexierung verwenden:
  1. Direkter Eintrag des Konzepts: `\index{Concept Name}`
  2. Hierarchische Einordnung: `\index{Übergeordnetes Konzept!Unterkonzept}`
  3. Bei Beispielen: `\index{Examples!Concept Name}`
- Index-Einträge direkt nach `\label` platzieren
- Bei mathematischen Konzepten in Index-Einträgen mathematische Symbole verwenden






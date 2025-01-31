##### Reminder für Literatur-db


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
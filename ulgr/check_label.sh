#!/bin/zsh

# Prüfe ob Dateiname als Parameter übergeben wurde
if [[ $# -ne 1 ]]; then
    print "Usage: $0 filename.tex"
    exit 1
fi

# Temporäre Dateien
TMPDIR=$(mktemp -d)
LABELS=$TMPDIR/labels.txt
REFS=$TMPDIR/refs.txt

# Output-Datei erstellen (mit Datum im Namen)
OUTFILE="label_check_$(date '+%Y%m%d_%H%M%S').txt"

{
    print "Label-Check für $1 am $(date '+%Y-%m-%d %H:%M:%S')\n"
    
    # Alle Labels finden
    print "Alle Labels:"
    grep -n "\\label{" $1 | sed -E 's/.*\\label\{([^}]*)\}.*/\1/' | sort > $LABELS
    cat $LABELS
    
    # Alle Referenzen finden (ref und eqref)
    print "\nAlle Referenzen:"
    grep -n "\\\\[eq]*ref{" $1 | sed -E 's/.*\\[eq]*ref\{([^}]*)\}.*/\1/' | sort > $REFS
    cat $REFS
    
    # Genutzte Labels finden
    print "\nGenutzte Labels:"
    comm -12 $LABELS $REFS
    
    # Ungenutzte Labels finden
    print "\nUngenutzte Labels:"
    comm -23 $LABELS $REFS

} | tee $OUTFILE

# Aufräumen
rm -rf $TMPDIR

print "\nErgebnisse wurden in $OUTFILE gespeichert."
#!/bin/zsh

# Farben für Ausgaben
autoload -U colors && colors

# Hauptdatei
MAIN_FILE="LN-Book.tex"

# Funktion für farbige Ausgabe
print_status() {
    echo "$fg[blue]>>> $1$reset_color"
}

print_success() {
    echo "$fg[green]✓ $1$reset_color"
}

print_error() {
    echo "$fg[red]✗ $1$reset_color"
}

# Build-Funktion
build() {
    print_status "Starte LaTeX-Kompilierung..."
    
    # Erster pdflatex Durchlauf
    print_status "Erster pdflatex Durchlauf..."
    pdflatex $MAIN_FILE || { print_error "pdflatex fehlgeschlagen"; return 1 }
    
    # BibTeX für Hauptdokument und alle Kapitel
    print_status "Führe bibtex für Hauptdokument aus..."
    if [[ -f "LN-Book.aux" ]]; then
        bibtex "LN-Book" || print_error "bibtex fehlgeschlagen für Hauptdokument"
    fi
    
    print_status "Führe bibtex für alle Kapitel aus..."
    # Kapitel
    for part in {a,b,c,d}; do
        for chap in {1,2,3,4}; do
            if [[ -f "part-${part}/chap-${part}${chap}.aux" ]]; then
                print_status "Bearbeite Kapitel ${part}${chap}..."
                bibtex "part-${part}/chap-${part}${chap}" || print_error "bibtex fehlgeschlagen für Kapitel ${part}${chap}"
            fi
        done
        # Appendix für jeden Teil
        if [[ -f "part-${part}/appendix-${part}.aux" ]]; then
            print_status "Bearbeite Appendix ${part}..."
            bibtex "part-${part}/appendix-${part}" || print_error "bibtex fehlgeschlagen für Appendix ${part}"
        fi
    done
    # Part-0 spezielle Dateien
    for file in part-0/*.aux; do
        if [[ -f "$file" ]]; then
            base=${file:r}  # Entfernt die .aux-Endung
            print_status "Bearbeite $base..."
            bibtex "$base" || print_error "bibtex fehlgeschlagen für $base"
        fi
    done
    
    # Zwei weitere pdflatex Durchläufe
    print_status "Zweiter pdflatex Durchlauf..."
    pdflatex $MAIN_FILE || { print_error "pdflatex fehlgeschlagen"; return 1 }
    
    print_status "Dritter pdflatex Durchlauf..."
    pdflatex $MAIN_FILE || { print_error "pdflatex fehlgeschlagen"; return 1 }
    
    print_success "Kompilierung abgeschlossen!"
}

# Clean-Funktion
clean() {
    print_status "Räume auf..."
    
    # Liste der zu löschenden Dateitypen
    local extensions=(.aux .bbl .blg .log .out .toc .lof .lot "synctex.gz" .fls .fdb_latexmk)
    
    # Lösche im Hauptverzeichnis und allen part-* Verzeichnissen
    for ext in $extensions; do
        # Hauptverzeichnis
        rm -f *$ext
        # Unterverzeichnisse
        for part in part-{0,a,b,c,d}; do
            if [[ -d $part ]]; then
                rm -f $part/*$ext
            fi
        done
    done
    
    print_success "Aufräumen abgeschlossen!"
}

# Watch-Funktion mit fswatch (muss installiert sein)
watch() {
    if ! command -v fswatch > /dev/null; then
        print_error "fswatch ist nicht installiert. Installiere es mit:"
        echo "brew install fswatch"
        return 1
    fi
    
    print_status "Überwache Änderungen... (Strg+C zum Beenden)"
    
    # Erste Kompilierung
    build
    
    # Überwache alle .tex und .bib Dateien
    fswatch -o . part-* | while read f; do
        if [[ $f == *.tex ]] || [[ $f == *.bib ]]; then
            print_status "Änderung erkannt in $f"
            build
        fi
    done
}

# Hilfe-Funktion
show_help() {
    echo "Verwendung: $0 <command>"
    echo "Commands:"
    echo "  build   - Kompiliert das Dokument"
    echo "  clean   - Löscht temporäre Dateien"
    echo "  watch   - Überwacht Änderungen und kompiliert automatisch"
    echo "  help    - Zeigt diese Hilfe"
}

# Hauptlogik
case "$1" in
    build)
        build
        ;;
    clean)
        clean
        ;;
    watch)
        watch
        ;;
    help)
        show_help
        ;;
    *)
        print_error "Unbekannter Befehl: $1"
        show_help
        exit 1
        ;;
esac

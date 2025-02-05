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
    print_status "Starte LaTeX-Kompilierung mit latexmk..."
    latexmk -pdf -interaction=nonstopmode $MAIN_FILE || { 
        print_error "Kompilierung fehlgeschlagen"
        return 1 
    }
    print_success "Kompilierung abgeschlossen!"
}

clean() {
    print_status "Räume auf..."
    # Erst normales Aufräumen durch latexmk
    latexmk -c
    # Dann zusätzlich .thm Dateien löschen
    find . -name "*.thm" -type f -delete
    print_success "Aufräumen abgeschlossen!"
}

# Watch-Funktion 
watch() {
    if ! command -v latexmk > /dev/null; then
        print_error "latexmk ist nicht installiert."
        return 1
    fi
    
    print_status "Überwache Änderungen... (Strg+C zum Beenden)"
    latexmk -pdf -pvc $MAIN_FILE
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
#!/bin/zsh
# --
# -- Version 2025-01-21
# --

# Colors for output
autoload -U colors && colors

# Main file
MAIN_FILE="LN-Book.tex"

# Functions
print_status() {
    echo "$fg[blue]>>> $1$reset_color"
}

print_success() {
    echo "$fg[green]✓ $1$reset_color"
}

print_error() {
    echo "$fg[red]✗ $1$reset_color"
}

# Build function
build() {
    if [[ ! -f "$MAIN_FILE" ]]; then
        print_error "Missing: $MAIN_FILE"
        return 1
    fi
    print_status "Starting LaTeX compilation with latexmk..."
    latexmk -pdf -interaction=nonstopmode $MAIN_FILE || { 
        print_error "Compilation failed"
        return 1 
    }
    print_success "Finished!"
}

# Clean function
clean() {
    print_status "Cleaning temporary files..."
    latexmk -c
    find . -name "*.thm" -type f -delete
    find . -name "*.idx" -type f -delete
    find . -name "*.ind" -type f -delete
    find . -name "*.ilg" -type f -delete
    find . -name "*.aux" -type f -delete
    print_success "Cleanup finished!"
}

# Watch function
watch() {
    if ! command -v latexmk > /dev/null; then
        print_error "latexmk not installed"
        return 1
    fi    
    print_status "Monitoring changes... (Ctrl+C to stop)"
    latexmk -pdf -pvc $MAIN_FILE
}

# Help function
show_help() {
    echo "Usage: $0 <command>"
    echo "Commands:"
    echo "  build   - Compiles the document"
    echo "  clean   - Deletes temporary files"
    echo "  watch   - Monitors changes and compiles automatically"
    echo "  help    - Shows this help"
}

# Main part
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
        print_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac

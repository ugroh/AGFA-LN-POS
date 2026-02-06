#!/bin/zsh
# --
# -- Version 2025-02-06 (biblatex/biber)
# --

# Colors for output
autoload -U colors && colors

# Main file
MAIN_FILE="LN-Book-New.tex"
MAIN_BASE="LN-Book-New"

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
    
    # First LaTeX run
    print_status "First LaTeX compilation..."
    pdflatex -interaction=nonstopmode $MAIN_FILE || { 
        print_error "First compilation failed"
        return 1 
    }
    print_success "First LaTeX run finished!"
    
    # Run biber (without .tex extension!)
    print_status "Running biber..."
    biber $MAIN_BASE || {
        print_error "biber failed"
        return 1
    }
    print_success "biber finished!"
    
    # Final LaTeX runs
    print_status "Final LaTeX compilation..."
    pdflatex -interaction=nonstopmode $MAIN_FILE || { 
        print_error "Final compilation failed"
        return 1 
    }
    pdflatex -interaction=nonstopmode $MAIN_FILE || { 
        print_error "Final compilation failed"
        return 1 
    }
    print_success "Build completed successfully!"
}

# Clean function
clean() {
    print_status "Cleaning temporary files..."
    find . -name "*.thm" -type f -delete
    find . -name "*.idx" -type f -delete
    find . -name "*.ind" -type f -delete
    find . -name "*.ilg" -type f -delete
    find . -name "*.aux" -type f -delete
    find . -name "*.bcf" -type f -delete
    find . -name "*.sync*" -type f -delete
    find . -name "*.log" -type f -delete
    find . -name "*.out" -type f -delete
    find . -name "*.fls" -type f -delete
    find . -name "*.run.xml" -type f -delete
    find . -name "*.toc" -type f -delete
    find . -name "*.fdb_latexmk" -type f -delete
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
    echo "  build   - First run → biber → final runs"
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_tex_document(content):
    """
    Creates a LaTeX document from the mathematical content
    """
    tex_content = []
    
    # Document header
    tex_content.extend([
        "\\documentclass{article}",
        "\\usepackage{amsmath}",
        "\\usepackage{amssymb}",
        "\\usepackage{amsthm}",
        "",
        "\\begin{document}",
        "",
        "\\section{D-IV Asymptotics}",
        ""
    ])
    
    # Main content
    tex_content.extend([
        "Let $(P_n)_{n\\in\\mathbb{N}}$ be a decreasing sequence of projections in $M$ such",
        "that $\\inf_n P_n = 0$. Then $\\lim_{n\\phi}(P_n) = 0$ for every $\\phi\\in\\phi$. Since",
        "",
        "\\[(T(t)P_n)^2 \\leq T(t)P_n, t\\in\\mathbb{R}_+,\\]",
        "",
        "we obtain by a classical inequality of Kadison that",
        "",
        "\\[0 \\leq \\phi((T(t)P_n)^2) \\leq \\phi(T(t)P_n) \\leq \\phi(P_n),\\]",
        "",
        "hence $\\lim_{n\\phi}(T(t)P_n) = 0$ uniformly in $t\\in\\mathbb{R}_+$. Since the family $\\phi$",
        "is faithful on $M$, it follows from [Takesaki (1979), Proposition",
        "III.5.3] that $(T(t)P_n)$ converges to zero in the $\\sigma(M,M_*)$-topology",
        "uniformly in $t\\in\\mathbb{R}_+$. Since this topology is finer than the weak*-topo-",
        "logy on $M$ we obtain the relative compactness of $T$ which implies",
        "the strong ergodicity.",
        "",
        "Let $T$ be an identity preserving semigroup of Schwarz type on the",
        "predual of a W*-algebra $M$. We call",
        "",
        "\\[P_r := \\sup\\{s(|\\phi|) : \\phi\\in\\text{Fix}(T)\\}\\]",
        "",
        "the recurrent projection associated with $T$. For a motivation of",
        "this definition compare, e.g., [Davies (1976), Section 6.3].",
        "",
        "Since $T(t)|\\phi| = |\\phi|$ for all $\\phi\\in\\text{Fix}(T)$ (D-III, Cor. 1.5) we obtain",
        "$T(t)'P_r \\geq P_r$ (see D-I,Sec.3.(c)). Let $T^{(r)}$ be the reduced semi-",
        "group on $P_rM_*P_r$ with generator $A^{(r)}$. Then $T^{(r)}$ is identity",
        "preserving and of Schwarz type. Similarly, if $R$ is a pseudo-resol-",
        "vent on $D = \\{\\lambda\\in\\mathbb{C} : \\text{Re}(\\lambda) > 0\\}$ with values in $M_*$ such that $R$ is",
        "identity preserving and of Schwarz type, then the recurrent projecton",
        "associated with $R$ is defined using $\\text{Fix}(R)$.",
        "",
        "\\begin{remark}[3.2]",
        "\\begin{enumerate}[(a)]",
        "\\item Let $\\phi\\in M_*$ and $\\alpha\\in\\mathbb{R}$ such that",
        "      \\[\\mu - i\\alpha)R(\\mu)\\phi = \\phi \\text{ for some } \\mu\\in\\mathbb{R}_+.\\]",
        "Since $s(|\\phi|)$ and $s(|\\phi^*|)$ are majorized by $P_r$ (D-III,Prop.1.4)",
        "it follows that $\\phi$ and $\\phi^*$ are in $P_rM_*P_r$.",
        "",
        "\\item From (a) and the observation that the family $\\{|\\phi| : \\phi\\in\\text{Fix}(T)\\}$ is",
        "\\end{enumerate}",
        "\\end{remark}",
        "",
        "\\end{document}"
    ])
    
    return "\n".join(tex_content)

def save_tex_file(filename, content):
    """
    Saves the LaTeX content to a file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Generate the TeX content
    tex_content = create_tex_document(None)
    
    # Save to file
    output_filename = 'test.tex'
    save_tex_file(output_filename, tex_content)
    print(f"LaTeX file has been created: {output_filename}")

if __name__ == "__main__":
    main()

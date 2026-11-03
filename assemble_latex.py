import os
import re

def assemble_latex():
    # 1. Read files
    with open("jalon-105/Jalon-105.md", "r") as f:
        cours_md = f.read()

    exos_md = []
    for i in range(1, 11):
        with open(f"jalon-105/exos/Exo-{i:02d}.md", "r") as f:
            exos_md.append(f.read())

    tps_md = []
    for i in range(1, 6):
        with open(f"jalon-105/tp/TP-{i:02d}.md", "r") as f:
            tps_md.append(f.read())

    # Remove YAML block from cours
    cours_md = re.sub(r'^---.*?---\n', '', cours_md, flags=re.DOTALL)

    # 2. Convert markdown to LaTeX using strict rules
    def md_to_latex(text, is_exo_or_tp=False):
        # Temporarily protect math blocks and tikz
        placeholders = []

        def replace_and_store(match):
            placeholders.append(match.group(0))
            return f"PLACEHOLDERBLOCK{len(placeholders)-1}ZZZ"

        # Protect TikZ
        text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', replace_and_store, text, flags=re.DOTALL)

        # Protect Display Math
        text = re.sub(r'\$\$.*?\$\$', replace_and_store, text, flags=re.DOTALL)

        # Protect Inline Math
        text = re.sub(r'\$.*?\$', replace_and_store, text, flags=re.DOTALL)

        # Protect lstlisting
        text = re.sub(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}', replace_and_store, text, flags=re.DOTALL)

        # Now apply markdown replacements on plain text

        # Formatting
        text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)

        # Remove * C* * style matches
        text = text.replace('C*', 'C-star')

        # Italic replacement
        text = re.sub(r'(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)', r'\\textit{\1}', text)

        # Headers (no manual numbering!)
        # Course headers
        if not is_exo_or_tp:
            # Replace # Jalon 105 : ... with nothing, handled by \title
            text = re.sub(r'^#\s+Jalon.*?\n', '', text, flags=re.MULTILINE)
            # Replace ## 1. Title -> \section{Title}
            text = re.sub(r'^##\s+(?:\d+\.\s+)?(.*?)$', r'\\section{\1}', text, flags=re.MULTILINE)
            # Replace ### A. Title -> \subsection{Title}
            text = re.sub(r'^###\s+(?:[A-Z]\.\s+)?(.*?)$', r'\\subsection{\1}', text, flags=re.MULTILINE)
        else:
            # For exos and TPs, # Title becomes \subsection*{Title}
            text = re.sub(r'^#\s+(.*?)$', r'\\subsection*{\1}', text, flags=re.MULTILINE)
            text = re.sub(r'^##\s+(.*?)$', r'\\subsubsection*{\1}', text, flags=re.MULTILINE)

        # Fix ampersands (escape them)
        text = text.replace('&', r'\&')

        # Fix unescaped underscores in plain text
        text = re.sub(r'([a-zA-Z])_([a-zA-Z0-9])', r'$\1_\2$', text)

        # Fix unescaped carets in plain text
        text = re.sub(r'([a-zA-Z])\^([a-zA-Z0-9])', r'$\1^\2$', text)

        # Quotes
        text = re.sub(r'^>\s+(.*?)$', r'\\begin{quote}\n\1\n\\end{quote}', text, flags=re.MULTILINE)

        # Restore placeholders (in reverse order!)
        for i in reversed(range(len(placeholders))):
            text = text.replace(f"PLACEHOLDERBLOCK{i}ZZZ", placeholders[i])

        return text

    latex_cours = md_to_latex(cours_md)
    latex_exos = "\n\n".join([md_to_latex(exo, is_exo_or_tp=True) for exo in exos_md])
    latex_tps = "\n\n".join([md_to_latex(tp, is_exo_or_tp=True) for tp in tps_md])

    # Strip French accents in Python blocks to prevent compilation errors
    def clean_lstlisting(match):
        code = match.group(0)
        code = code.replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('à', 'a').replace('ç', 'c').replace('ù', 'u')
        return code

    latex_tps = re.sub(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}', clean_lstlisting, latex_tps, flags=re.DOTALL)


    master_latex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\geometry{hmargin=2.5cm,vmargin=3cm}
\usepackage{tikz}
\usetikzlibrary{cd,positioning,shapes}
\usepackage{listings}
\usepackage{xcolor}

\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue}\bfseries,
    stringstyle=\color{red},
    commentstyle=\color{gray}\itshape,
    numbers=left,
    numberstyle=\tiny\color{gray},
    breaklines=true,
    frame=single,
    showstringspaces=false
}

\title{\Huge Opérateurs adjoints \\ \large Cours magistral, exercices corrigés et travaux pratiques}
\author{\Large Charles EDOU NZE}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\part{Cours Magistral}
""" + latex_cours + r"""

\part{Exercices d'Application et de Concours}
""" + latex_exos + r"""

\part{Travaux Pratiques et Simulations Algorithmiques}
""" + latex_tps + r"""

\end{document}
"""

    with open("jalon-105.tex", "w") as f:
        f.write(master_latex)

if __name__ == "__main__":
    assemble_latex()

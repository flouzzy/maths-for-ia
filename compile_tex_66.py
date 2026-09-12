import os
import re

def clean_markdown_headers(text):
    # Matches "# Title", "## Title", etc.
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('#'):
            # count hashes
            hashes = len(line) - len(line.lstrip('#'))
            title = line.strip('#').strip()

            # Anti-double numbering: remove leading numbers/letters from title
            # e.g. "1. Genèse" -> "Genèse", "A. Concept" -> "Concept"
            title = re.sub(r'^[A-Z0-9]+\.\s+', '', title)

            if hashes == 1:
                pass # Usually the main title, handled by maketitle
            elif hashes == 2:
                lines[i] = f"\\section{{{title}}}"
            elif hashes == 3:
                # Need to check if it's Exercice or TP
                if title.startswith("Exercice") or title.startswith("TP"):
                    lines[i] = f"\\subsection*{{{title}}}"
                else:
                    lines[i] = f"\\subsection{{{title}}}"
            elif hashes == 4:
                lines[i] = f"\\subsubsection{{{title}}}"
    return '\n'.join(lines)

def process_markdown_text(text):
    # Escape ampersands not in math/alignment (simplified, just escape them)
    # Be careful not to replace \& if already escaped, or ampersands in math.
    # For this jalon, we just escape free ampersands:
    text = re.sub(r'(?<!\\)&', r'\&', text)

    # Process text formatting outside of code blocks
    parts = re.split(r'(\\begin\{lstlisting\}.*?\\end\{lstlisting\})', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith(r'\begin{lstlisting}'):
            # convert bold
            parts[i] = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', parts[i])
            # convert italic (be careful not to match math like x^* by requiring spaces/boundaries or just avoiding math)
            # a safer way: only match if no math is around, but simpler:
            parts[i] = re.sub(r'(?<!\*)\*(?!\*)([^*\$]+?)(?<!\*)\*(?!\*)', r'\\textit{\1}', parts[i])

            # lists -> itemize (simple line-by-line state machine)
            lines = parts[i].split('\n')
            in_itemize = False
            for j in range(len(lines)):
                if re.match(r'^\s*-\s+', lines[j]):
                    if not in_itemize:
                        lines.insert(j, r'\begin{itemize}')
                        in_itemize = True
                        j += 1
                    lines[j] = re.sub(r'^\s*-\s+', r'\\item ', lines[j])
                else:
                    if in_itemize and lines[j].strip() == '':
                        pass
                    elif in_itemize and not re.match(r'^\s*-\s+', lines[j]):
                        lines.insert(j, r'\end{itemize}')
                        in_itemize = False
                        j += 1
            if in_itemize:
                lines.append(r'\end{itemize}')
            parts[i] = '\n'.join(lines)

    return ''.join(parts)

# 1. Read files
with open("jalon-66/Jalon-66.md", "r", encoding="utf-8") as f:
    cours_md = f.read()

# strip frontmatter
cours_md = re.sub(r'^---.*?---\n', '', cours_md, flags=re.DOTALL)

exos_content = ""
for i in range(1, 11):
    with open(f"jalon-66/exos/Exo-{i:02d}.md", "r", encoding="utf-8") as f:
        exos_content += f.read() + "\n\n"

tps_content = ""
for i in range(1, 6):
    with open(f"jalon-66/tp/TP-{i:02d}.md", "r", encoding="utf-8") as f:
        tps_content += f.read() + "\n\n"

# 2. Process contents
cours_processed = process_markdown_text(clean_markdown_headers(cours_md))
exos_processed = process_markdown_text(clean_markdown_headers(exos_content))
tps_processed = process_markdown_text(clean_markdown_headers(tps_content))

# 3. Assemble Master LaTeX
template = r"""\documentclass[11pt,a4paper]{article}
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
    showstringspaces=false,
    literate={é}{{\'e}}1 {è}{{\`e}}1 {à}{{\`a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ç}{{\c{c}}}1 {ï}{{\"i}}1 {É}{{\'E}}1
}

\title{\Huge INTÉGRALE DE LEBESGUE POUR LES FONCTIONS POSITIVES \\ \large Cours magistral, exercices corrigés et travaux pratiques}
\author{\Large Charles EDOU NZE}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\part{Cours Magistral}
""" + cours_processed + r"""

\newpage
\part{Exercices d'Application et de Concours}
""" + exos_processed + r"""

\newpage
\part{Travaux Pratiques et Simulations Algorithmiques}
""" + tps_processed + r"""

\end{document}
"""

with open("jalon-66.tex", "w", encoding="utf-8") as f:
    f.write(template)

print("Generated jalon-66.tex successfully.")

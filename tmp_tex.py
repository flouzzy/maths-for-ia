import re
import os

with open("jalon-88/Jalon-88.md", "r", encoding="utf-8") as f:
    course = f.read()

# Strip frontmatter
course = re.sub(r"^---\n.*?\n---\n", "", course, flags=re.DOTALL)

# Convert Markdown to LaTeX course
# Strip Jalon Title entirely
course = re.sub(r"^# Jalon .*?\n", "", course)
course = re.sub(r"^# .*\n", "", course) # Just in case

def clean_section(match):
    title = match.group(1).strip()
    title = re.sub(r"^(?:[0-9]+|[A-Z])\.\s*", "", title)
    return fr"\section{{{title}}}"

def clean_subsection(match):
    title = match.group(1).strip()
    title = re.sub(r"^(?:[0-9]+|[A-Z])\.\s*", "", title)
    return fr"\subsection{{{title}}}"

def process_text_blocks(text):
    # Escape &
    text = re.sub(r'(?<!\\)&', r'\&', text)

    lines = text.split('\n')
    out_lines = []
    in_quote = False
    in_code = False
    in_itemize = False
    in_enumerate = False

    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
            continue

        if in_code:
            out_lines.append(line)
            continue

        # Lists handling
        is_itemize_item = line.startswith("- ")
        is_enumerate_item = re.match(r"^[0-9]+\.\s", line) is not None

        if is_itemize_item:
            if not in_itemize:
                out_lines.append(r"\begin{itemize}")
                in_itemize = True
            line = line.replace("- ", r"\item ", 1)
        else:
            if in_itemize and not line.strip():
                out_lines.append(r"\end{itemize}")
                in_itemize = False

        if is_enumerate_item:
            if not in_enumerate:
                out_lines.append(r"\begin{enumerate}")
                in_enumerate = True
            line = re.sub(r"^[0-9]+\.\s", r"\\item ", line)
        else:
            if in_enumerate and not line.strip():
                out_lines.append(r"\end{enumerate}")
                in_enumerate = False

        if line.startswith(">"):
            if not in_quote:
                out_lines.append(r"\begin{quote}")
                in_quote = True
            line = line.replace(">", "").strip()
            line = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", line)
            if line:
                out_lines.append(line)
            continue
        else:
            if in_quote:
                out_lines.append(r"\end{quote}")
                in_quote = False

        if line.startswith("## "):
            out_lines.append(clean_section(re.match(r"## (.*)", line)))
        elif line.startswith("### "):
            out_lines.append(clean_subsection(re.match(r"### (.*)", line)))
        else:
            # Bold and italic (basic)
            line = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", line)
            line = re.sub(r"(?<!\\)\*(.*?)\*", r"\\textit{\1}", line)
            out_lines.append(line)

    if in_quote:
        out_lines.append(r"\end{quote}")
    if in_itemize:
        out_lines.append(r"\end{itemize}")
    if in_enumerate:
        out_lines.append(r"\end{enumerate}")

    return "\n".join(out_lines)

course_processed = process_text_blocks(course)

latex_template = r"""\documentclass[11pt,a4paper]{article}
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

\title{\Huge INDÉPENDANCE D'ÉVÉNEMENTS ET DE VARIABLES ALÉATOIRES \\ \large Cours magistral, exercices corrigés et travaux pratiques}
\author{\Large Charles EDOU NZE}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\part{Cours Magistral}
""" + course_processed + r"""

\newpage
\part{Exercices d'Application et de Concours}
"""

for i in range(1, 11):
    with open(f"jalon-88/exos/Exo-{i:02d}.md", "r", encoding="utf-8") as f:
        exo_content = f.read()
        exo_content = re.sub(r"^# Exercice \d+\n+", "", exo_content)
        exo_content = exo_content.replace("**Énoncé :**", r"\textbf{Énoncé :}")
        exo_content = exo_content.replace("**Correction :**", r"\textbf{Correction :}")
        exo_content = process_text_blocks(exo_content)
        latex_template += "\n" + exo_content + "\n"

latex_template += r"""
\newpage
\part{Travaux Pratiques et Simulations Algorithmiques}
"""

for i in range(1, 6):
    with open(f"jalon-88/tp/TP-{i:02d}.md", "r", encoding="utf-8") as f:
        tp_content = f.read()
        tp_content = re.sub(r"^# TP \d+\n+", "", tp_content)
        # Process TP text content, avoiding running process_text_blocks on the lstlisting environment
        # We can just append it directly as it's simple text + code block
        tp_content = tp_content.replace(r"&", r"\&")
        latex_template += "\n" + tp_content + "\n"

latex_template += "\n\\end{document}\n"

with open("jalon-88.tex", "w", encoding="utf-8") as f:
    f.write(latex_template)

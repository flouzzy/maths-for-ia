import os
import re
import unicodedata

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def sanitize_python(code_block):
    lines = code_block.split('\n')
    out = []
    for line in lines:
        if line.strip().startswith('#'):
            out.append(strip_accents(line))
        elif '"""' in line or "'''" in line:
            out.append(strip_accents(line))
        else:
            out.append(line)
    return '\n'.join(out)

def convert_to_latex():
    with open('jalon-11/Jalon-11.md', 'r', encoding='utf-8') as f:
        md_cours = f.read()

    md_cours = re.sub(r'^---[\s\S]*?^---\n', '', md_cours, flags=re.MULTILINE)
    md_cours = re.sub(r'^# (.*)', r'\\chapter{\1}', md_cours, flags=re.MULTILINE)
    md_cours = re.sub(r'^## (.*)', r'\\section{\1}', md_cours, flags=re.MULTILINE)
    md_cours = re.sub(r'^### (.*)', r'\\subsection{\1}', md_cours, flags=re.MULTILINE)
    md_cours = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', md_cours)

    latex_doc = r"""\documentclass[11pt,a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{tikz}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{geometry}
\geometry{margin=2.5cm}

\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    stringstyle=\color{red},
    commentstyle=\color{green!60!black},
    numbers=left,
    numberstyle=\tiny,
    stepnumber=1,
    numbersep=5pt,
    backgroundcolor=\color{gray!10},
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    frame=single,
    tabsize=4,
    captionpos=b,
    breaklines=true,
    breakatwhitespace=false,
    extendedchars=true,
    literate={é}{{\'e}}1 {è}{{\`e}}1 {à}{{\`a}}1 {ç}{{\c{c}}}1 {œ}{{\oe}}1 {ù}{{\`u}}1
}

\title{Formes lineaires, hyperplans, espace dual et orthogonalite en dimension finie}
\author{Charles EDOU NZE}
\date{\today}

\begin{document}

\maketitle
\tableofcontents

\chapter{Formes lineaires, hyperplans, espace dual et orthogonalite en dimension finie}

\section{Visualisation Geometrique (TikZ)}

\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1.5]
  % Espace 3D simulé
  \draw[thick,->] (0,0,0) -- (3,0,0) node[anchor=north east]{$x_1$};
  \draw[thick,->] (0,0,0) -- (0,3,0) node[anchor=north west]{$x_2$};
  \draw[thick,->] (0,0,0) -- (0,0,3) node[anchor=south]{$x_3$};

  % Hyperplan
  \filldraw[fill=blue!20, draw=blue!50!black, opacity=0.7] (-1,2,-1) -- (2,-1,-1) -- (3,0,2) -- (0,3,2) -- cycle;
  \node[blue!80!black] at (1,2,0) {$H = \ker \phi$};

  % Vecteur normal
  \draw[thick, red, ->] (1,1,0.5) -- (2,2,1.5) node[anchor=west]{$\phi$ (Vecteur Normal)};

  % Vecteur dans H
  \draw[thick, green!60!black, ->] (0.5,1,0.5) -- (1.5,0,0.5) node[anchor=west]{$v \in H$};
\end{tikzpicture}
\caption{Hyperplan vectoriel comme noyau d'une forme lineaire}
\end{figure}

"""
    # Replace math mode asterisks safely
    md_cours = md_cours.replace('E^{**}', 'E^{\star\star}')
    latex_doc += md_cours

    latex_doc += "\n\\chapter{Exercices d'application}\n"
    for i in range(1, 11):
        try:
            with open(f'jalon-11/exos/Exo-{i:02d}.md', 'r', encoding='utf-8') as f:
                exo_md = f.read()
                exo_md = re.sub(r'^---[\s\S]*?^---\n', '', exo_md, flags=re.MULTILINE)
                exo_md = re.sub(r'^# (.*)', r'\\section{\1}', exo_md, flags=re.MULTILINE)
                exo_md = re.sub(r'^## (.*)', r'\\subsection{\1}', exo_md, flags=re.MULTILINE)
                exo_md = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', exo_md)
                latex_doc += exo_md + "\n"
        except FileNotFoundError:
            pass

    latex_doc += "\n\\chapter{Travaux Pratiques en Python}\n"
    for i in range(1, 6):
        try:
            with open(f'jalon-11/tp/TP-{i:02d}.md', 'r', encoding='utf-8') as f:
                tp_md = f.read()

                parts = tp_md.split('```python')
                if len(parts) > 1:
                    pre_code = parts[0]
                    code_part = parts[1].split('```')[0]

                    pre_code = re.sub(r'^# (.*)', r'\\section{\1}', pre_code, flags=re.MULTILINE)
                    pre_code = re.sub(r'^## (.*)', r'\\subsection{\1}', pre_code, flags=re.MULTILINE)

                    latex_doc += pre_code
                    latex_doc += "\\begin{lstlisting}\n"
                    latex_doc += sanitize_python(code_part)
                    latex_doc += "\\end{lstlisting}\n"
                else:
                    tp_md = re.sub(r'^# (.*)', r'\\section{\1}', tp_md, flags=re.MULTILINE)
                    tp_md = re.sub(r'^## (.*)', r'\\subsection{\1}', tp_md, flags=re.MULTILINE)
                    latex_doc += tp_md + "\n"

        except FileNotFoundError:
            pass

    latex_doc += "\n\\end{document}"

    # Fix the bidual star issue from before
    latex_doc = latex_doc.replace('E^{\star\star}', 'E^{**}')
    latex_doc = latex_doc.replace(r'ev_x', r'\text{ev}_x')

    with open('jalon-11.tex', 'w', encoding='utf-8') as f:
        f.write(latex_doc)

convert_to_latex()

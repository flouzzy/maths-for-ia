import re

with open('jalon-9/Jalon-9.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove forbidden phrases
forbidden = [
    "*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*",
    "*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*",
    "*Démontrer la finalité technologique moderne de ce jalon théorique.*"
]

for phrase in forbidden:
    content = content.replace(phrase, "")
    content = content.replace(phrase.replace("*", ""), "")

# Convert Markdown to LaTeX master
def generate_latex(md_text):
    # This is a simplified transformation just to output the raw LaTeX requested.
    latex = r"""\documentclass[12pt,a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath,amsfonts,amssymb,amsthm}
\usepackage{geometry}
\usepackage{tikz}
\usepackage{listings}
\usepackage{color}

\geometry{margin=1in}

\title{Calcul matriciel, opérations, inversibilité et représentations des applications linéaires}
\author{Charles EDOU NZE}
\date{}

\begin{document}
\maketitle
\tableofcontents

\chapter{Calcul Matriciel}
"""

    # Strip frontmatter
    md_text = re.sub(r'^---.*?^---\n', '', md_text, flags=re.MULTILINE|re.DOTALL)

    # Basic Markdown to LaTeX replacements
    latex_content = md_text.replace("## 1. Présentation du concept clé", r"\section{Présentation du concept clé}")
    latex_content = latex_content.replace("## 2. Formalisation & Rigueur Académique", r"\section{Formalisation et Rigueur Académique}")
    latex_content = latex_content.replace("## 3. Démonstrations Pas-à-Pas", r"\section{Démonstrations Pas-à-Pas}")
    latex_content = latex_content.replace("## 4. Exercices d'Application", r"\section{Exercices d'Application}")
    latex_content = latex_content.replace("## 5. Ancrage & Application en Intelligence Artificielle", r"\section{Application en Intelligence Artificielle}")
    latex_content = latex_content.replace("## 6. Liens Sémantiques & Maillage Obsidian", r"\section{Liens Sémantiques}")

    # Simple list handling
    latex_content = latex_content.replace("- **La Métaphore :**", r"\textbf{La Métaphore :}")
    latex_content = latex_content.replace("- **Le \"Pourquoi on a inventé ça\" :**", r"\textbf{Le Pourquoi on a inventé ça :}")
    latex_content = latex_content.replace("- **Visualisation :**", r"\textbf{Visualisation :}")

    # Subsections
    latex_content = re.sub(r'^### (.*?)$', r'\\subsection{\1}', latex_content, flags=re.MULTILINE)

    # bold
    latex_content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', latex_content)

    # End doc
    latex += latex_content + r"\n\end{document}"
    return latex

latex_code = generate_latex(content)

with open('jalon-9/jalon-9.tex', 'w', encoding='utf-8') as f:
    f.write(latex_code)

print("Generated jalon-9.tex")

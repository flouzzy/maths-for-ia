import os
import re

def process_markdown_text(text):
    # Escape ampersands but protect TikZ and pmatrix
    def replace_ampersand(match):
        content = match.group(0)
        return content

    # Protect TikZ environments
    text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', replace_ampersand, text, flags=re.DOTALL)
    # Protect pmatrix environments
    text = re.sub(r'\\begin\{pmatrix\}.*?\\end\{pmatrix\}', replace_ampersand, text, flags=re.DOTALL)

    parts = []
    # Simple split by code blocks first
    code_blocks = re.split(r'(```.*?```)', text, flags=re.DOTALL)
    for code_part in code_blocks:
        if code_part.startswith('```'):
            parts.append(code_part)
        else:
            # Simple split by inline/block math
            math_parts = re.split(r'(\$\$.*?\$\$|\$.*?\$)', code_part, flags=re.DOTALL)
            for m_part in math_parts:
                if m_part.startswith('$'):
                    parts.append(m_part)
                else:
                    # In text, escape &
                    m_part = re.sub(r'(?<!\\)&', r'\&', m_part)

                    # Convert markdown bold and italic
                    m_part = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', m_part)

                    # Protect latex commands from italic replace
                    m_part = re.sub(r'(?<!\\)\*(?!\s)(.*?)(?<!\s)\*', r'\\textit{\1}', m_part)

                    parts.append(m_part)

    text = "".join(parts)

    # Handle quotes and lists
    text = re.sub(r'^> (.*)$', r'\\begin{quote}\1\\end{quote}', text, flags=re.MULTILINE)

    return text

def convert_headers(text, is_exo=False, is_tp=False):
    # Remove # Jalon...
    text = re.sub(r'^# Jalon.*?\n', '', text, flags=re.MULTILINE)

    if is_exo:
         # Exo headers: # Exercice ...
         # Convert to \subsection*{Exercice ...}
         text = re.sub(r'^# (Exercice .*?)$', r'\\subsection*{\1}', text, flags=re.MULTILINE)
         # In exos, ## becomes \subsubsection*
         text = re.sub(r'^## (.*?)$', r'\\subsubsection*{\1}', text, flags=re.MULTILINE)
    elif is_tp:
         # TP headers: # TP ...
         text = re.sub(r'^# (TP .*?)$', r'\\subsection*{\1}', text, flags=re.MULTILINE)
         text = re.sub(r'^## (.*?)$', r'\\subsubsection*{\1}', text, flags=re.MULTILINE)
    else:
         # Course headers
         # Remove prefixes like A. or 1.
         text = re.sub(r'^##\s+(?:[A-Z]\.\s+|\d+\.\s+)?(.*?)$', r'\\section{\1}', text, flags=re.MULTILINE)
         text = re.sub(r'^###\s+(?:[A-Z]\.\s+|\d+\.\s+)?(.*?)$', r'\\subsection{\1}', text, flags=re.MULTILINE)

    # Clean remaining standalone '#' if any, except escaped \#, but ONLY outside code blocks
    # To do this safely, we will split by ```...``` again
    parts = []
    code_blocks = re.split(r'(```.*?```)', text, flags=re.DOTALL)
    for code_part in code_blocks:
        if code_part.startswith('```'):
            parts.append(code_part)
        else:
            cleaned = re.sub(r'(?<!\\)#', '', code_part)
            parts.append(cleaned)
    text = "".join(parts)

    # Finally convert code blocks to lstlisting
    text = re.sub(r'```(?:python)?(.*?)```', r'\\begin{lstlisting}\1\\end{lstlisting}', text, flags=re.DOTALL)

    return text

def main():
    course_path = "Jalon-104.md"
    with open(course_path, 'r', encoding='utf-8') as f:
        course_content = f.read()

    # Remove YAML frontmatter
    course_content = re.sub(r'^---.*?---\n', '', course_content, flags=re.DOTALL)
    course_content = process_markdown_text(course_content)
    course_content = convert_headers(course_content, is_exo=False)

    # Read Exos
    exos_content = []
    for i in range(1, 11):
        with open(f"exos/Exo-{i:02d}.md", 'r', encoding='utf-8') as f:
            c = f.read()
            c = process_markdown_text(c)
            c = convert_headers(c, is_exo=True)
            exos_content.append(c)

    # Read TPs
    tps_content = []
    for i in range(1, 6):
        with open(f"tp/TP-{i:02d}.md", 'r', encoding='utf-8') as f:
            c = f.read()
            c = process_markdown_text(c)
            c = convert_headers(c, is_exo=False, is_tp=True)
            # In TPs, remove French accents in code blocks to avoid utf8 inputenc issues
            def remove_accents_in_code(match):
                code = match.group(1)
                code = code.replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('à', 'a').replace('ç', 'c')
                return '\\begin{lstlisting}' + code + '\\end{lstlisting}'
            c = re.sub(r'\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}', remove_accents_in_code, c, flags=re.DOTALL)
            tps_content.append(c)

    tex_template = r"""\documentclass[11pt,a4paper]{article}
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

\title{\Huge Bases Hilbertiennes \\ \large Cours magistral, exercices corrigés et travaux pratiques}
\author{\Large Charles EDOU NZE}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\part{Cours Magistral}
COURSE_CONTENT

\part{Exercices d'Application et de Concours}
EXOS_CONTENT

\part{Travaux Pratiques et Simulations Algorithmiques}
TPS_CONTENT

\end{document}
"""

    tex_content = tex_template.replace("COURSE_CONTENT", course_content)
    tex_content = tex_content.replace("EXOS_CONTENT", "\n\n".join(exos_content))
    tex_content = tex_content.replace("TPS_CONTENT", "\n\n".join(tps_content))

    # Make sure difficulty stars are correctly converted
    tex_content = re.sub(r'\\\\bigstar\\\\star\\\\star\\\\star\\\\star', r'\$\\\\bigstar\\\\star\\\\star\\\\star\\\\star\$', tex_content)
    tex_content = re.sub(r'\\\\bigstar\\\\bigstar\\\\star\\\\star\\\\star', r'\$\\\\bigstar\\\\bigstar\\\\star\\\\star\\\\star\$', tex_content)
    tex_content = re.sub(r'\\\\bigstar\\\\bigstar\\\\bigstar\\\\star\\\\star', r'\$\\\\bigstar\\\\bigstar\\\\bigstar\\\\star\\\\star\$', tex_content)
    tex_content = re.sub(r'\\\\bigstar\\\\bigstar\\\\bigstar\\\\bigstar\\\\star', r'\$\\\\bigstar\\\\bigstar\\\\bigstar\\\\bigstar\\\\star\$', tex_content)
    tex_content = re.sub(r'\\\\bigstar\\\\bigstar\\\\bigstar\\\\bigstar\\\\bigstar', r'\$\\\\bigstar\\\\bigstar\\\\bigstar\\\\bigstar\\\\bigstar\$', tex_content)

    # Some manual fixes for the edge cases
    tex_content = tex_content.replace('L^2(R^2)', 'L\\textsuperscript{2}(R\\textsuperscript{2})')
    tex_content = tex_content.replace('dans ^2', 'dans $l^2$')

    tex_content = re.sub(r'\$\$\\\\bigstar', r'$\\\\bigstar', tex_content)
    tex_content = re.sub(r'\\\\star\$\$', r'\\\\star$', tex_content)
    tex_content = re.sub(r'\\\\bigstar\$\$', r'\\\\bigstar$', tex_content)

    with open("jalon-104.tex", "w", encoding="utf-8") as f:
        f.write(tex_content)

if __name__ == "__main__":
    main()

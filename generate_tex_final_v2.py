import os
import re

def process_markdown_to_latex(content):
    # 1. Clean up frontmatter
    content = re.sub(r'^---.*?^---', '', content, flags=re.DOTALL | re.MULTILINE)

    # We will temporarily mask code blocks to prevent headers and italics from messing them up.
    code_blocks = []
    def mask_code_block(match):
        code = match.group(1)
        code_blocks.append(f"\\begin{{lstlisting}}[language=Python]\n{code}\n\\end{{lstlisting}}")
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"

    content = re.sub(r'```python\n(.*?)\n```', mask_code_block, content, flags=re.DOTALL)
    content = re.sub(r'```\n(.*?)\n```', mask_code_block, content, flags=re.DOTALL)

    # We will also temporarily mask inline code `...`
    inline_codes = []
    def mask_inline_code(match):
        code = match.group(1)
        # Escape _ and & inside inline code for safety, or use \texttt. Let's use \texttt and escape them.
        code = code.replace('_', '\\_').replace('&', '\\&')
        inline_codes.append(f"\\texttt{{{code}}}")
        return f"__INLINE_CODE_{len(inline_codes)-1}__"

    content = re.sub(r'`(.*?)`', mask_inline_code, content)

    # We will also temporarily mask math blocks
    math_blocks = []
    def mask_math_block(match):
        math_blocks.append(match.group(0))
        return f"__MATH_BLOCK_{len(math_blocks)-1}__"

    content = re.sub(r'\$\$.*?\$\$', mask_math_block, content, flags=re.DOTALL)
    content = re.sub(r'\$.*?\$', mask_math_block, content)

    # 3. Replace headers
    content = re.sub(r'^# (.*?)$', r'\\chapter*{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.*?)$', r'\\section*{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.*?)$', r'\\subsection*{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^#### (.*?)$', r'\\subsubsection*{\1}', content, flags=re.MULTILINE)

    # 4. Bold and Italic
    content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)
    content = re.sub(r'(?<!\\)\*(.*?)(?<!\\)\*', r'\\textit{\1}', content)

    # Fix unicode stars
    content = content.replace("⭐", "$\\star$")

    # Cleanup % and &, _
    content = content.replace("%", "\\%")
    content = content.replace("&", "\\&")
    # Only replace _ that are not part of our temporary markers.
    # To do this safely, we will use a temporary marker for _ too.
    # Actually, if we just replace it, our markers __MATH_BLOCK_ etc will break.
    # So we replace _ with \_ ONLY if it's not preceded by __
    # Better: split by markers, replace in text.
    parts = re.split(r'(__(?:MATH|CODE|INLINE_CODE)_BLOCK_\d+__)', content)
    for i in range(len(parts)):
        if not re.match(r'__(?:MATH|CODE|INLINE_CODE)_BLOCK_\d+__', parts[i]):
            parts[i] = parts[i].replace('_', '\\_')
    content = ''.join(parts)


    # Links
    content = re.sub(r'\[\[.*?\|(.*?)\]\]', r'\1', content)
    content = re.sub(r'\[\[(.*?)\]\]', r'\1', content)

    # Unmask math blocks
    for i, block in enumerate(math_blocks):
        content = content.replace(f"__MATH_BLOCK_{i}__", block)

    # Unmask inline code
    for i, block in enumerate(inline_codes):
        content = content.replace(f"__INLINE_CODE_{i}__", block)

    # Unmask code blocks
    for i, block in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_{i}__", block)

    return content

def main():
    tex_header = r"""\documentclass{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{tikz}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{a4paper, margin=2cm}

\title{Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps)}
\author{Charles EDOU NZE}
\date{2026-06-26}

\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    stringstyle=\color{red},
    commentstyle=\color{green!60!black},
    showstringspaces=false,
    frame=single,
    breaklines=true,
    literate={é}{{\'e}}1 {è}{{\`e}}1 {à}{{\`a}}1 {ç}{{\c c}}1 {ù}{{\`u}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1 {â}{{\^a}}1 {É}{{\'E}}1 {È}{{\`E}}1 {À}{{\`A}}1 {Ç}{{\c C}}1 {Ù}{{\`U}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1 {Â}{{\^A}}1
}

\begin{document}
\maketitle
\tableofcontents
\newpage
"""

    tex_footer = r"""\end{document}"""

    with open('jalon-6/jalon-6.tex', 'w', encoding='utf-8') as outfile:
        outfile.write(tex_header)

        # 1. Jalon-6.md
        with open('jalon-6/Jalon-6.md', 'r', encoding='utf-8') as f:
            content = f.read()

        latex_content = process_markdown_to_latex(content)

        # Insert TikZ for this jalon
        tikz_figure = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}
  % Partition / Equivalence classes
  \draw[thick] (0,0) ellipse (4cm and 2.5cm);
  \draw[thick] (-2, -2.16) to[out=60,in=240] (-1, 2.4);
  \draw[thick] (1, -2.4) to[out=120,in=300] (0.5, 2.48);
  \node at (-2, 0) {$\dot{x}$};
  \node at (0, 0) {$\dot{y}$};
  \node at (2, 0) {$\dot{z}$};
  \node at (0, -3) {Ensemble quotient $E/\mathcal{R}$};
\end{tikzpicture}
\caption{Partition d'un ensemble par des classes d'équivalence}
\end{figure}
"""
        latex_content = latex_content.replace(r'\section*{1. Présentation du concept clé}', r'\section*{1. Présentation du concept clé}' + '\n' + tikz_figure)
        outfile.write(latex_content + '\n\\newpage\n')

        # 2. Exos
        outfile.write(r'\chapter*{Exercices d\'Application}' + '\n\\addcontentsline{toc}{chapter}{Exercices d\'Application}\n')
        for i in range(1, 11):
            filename = f'jalon-6/exos/Exo-{i:02d}.md'
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            latex_content = process_markdown_to_latex(content)
            outfile.write(latex_content + '\n\\newpage\n')

        # 3. TP
        outfile.write(r'\chapter*{Travaux Pratiques}' + '\n\\addcontentsline{toc}{chapter}{Travaux Pratiques}\n')
        for i in range(1, 6):
            filename = f'jalon-6/tp/TP-{i:02d}.md'
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            latex_content = process_markdown_to_latex(content)
            outfile.write(latex_content + '\n\\newpage\n')

        outfile.write(tex_footer)

if __name__ == '__main__':
    main()

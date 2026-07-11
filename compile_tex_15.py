import re
import os

with open('generate_tex_final_v2.py', 'r') as f:
    content = f.read()

content = content.replace('jalon-6', 'jalon-15')
content = content.replace('Jalon-6', 'Jalon-15')
content = content.replace('Charles EDOU NZE', 'Charles EDOU NZE')

# Fix title
title_orig = r"Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps)"
title_new = r"Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass"
content = content.replace(title_orig, title_new)

# Fix TPs count
content = content.replace('for i in range(1, 6):', 'for i in [1,2,3,5]:')

part1 = content.split('tikz_figure = r"""')[0]
part2 = content.split('\\end{figure}\n"""')[1]

tikz_block = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}
  \draw[->] (0,0) -- (10,0) node[right] {$n$};
  \draw[->] (0,-2) -- (0,2) node[above] {$u_n$};

  \foreach \x in {1, 2, 3, 4, 5, 6, 7, 8, 9} {
    \pgfmathsetmacro\y{sin(\x*50) + 0.2*cos(\x*150)}
    \filldraw[gray!50] (\x, \y) circle (1.5pt);
  }

  \foreach \x/\y in {1/-0.5, 3/0.2, 5/0.8, 7/0.95, 9/0.99} {
    \filldraw[red] (\x, \y) circle (2.5pt);
    \draw[red, dashed] (\x, \y) -- (\x, 0);
  }

  \draw[blue, dashed] (0, 1) -- (10, 1) node[right] {Valeur d'adherence $a=1$};
  \node[red] at (5, -1) {Sous-suite convergente};
\end{tikzpicture}
\caption{Extraction d'une sous-suite convergente à partir d'une suite bornée}
\end{figure}
"""

with open('compile_15.py', 'w') as f:
    f.write(part1 + 'tikz_figure = r"""' + tikz_block + '"""' + part2)

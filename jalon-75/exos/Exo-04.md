# Exercice 4 : Séries absolument convergentes dans $L^p$
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(f_n)_{n \ge 1}$ une suite de fonctions de $L^1(\mathbb{R})$ telle que $\sum_{n=1}^{+\infty} \|f_n\|_1 < +\infty$.
Montrer rigoureusement (sans utiliser directement la complétude) que la série $\sum f_n(x)$ converge absolument pour presque tout $x \in \mathbb{R}$.

**Correction :**
Posons $g(x) = \sum_{n=1}^{+\infty} |f_n(x)| \in [0, +\infty]$. Cette fonction est mesurable car limite de sommes partielles mesurables $S_N = \sum_{n=1}^N |f_n|$.
Puisque les termes sont positifs, par le théorème de convergence monotone (Beppo-Levi) :
$\int_\mathbb{R} g(x) dx = \lim_{N \to +\infty} \int_\mathbb{R} \sum_{n=1}^N |f_n(x)| dx$
Par linéarité de l'intégrale (sur une somme finie) :
$\int_\mathbb{R} g(x) dx = \lim_{N \to +\infty} \sum_{n=1}^N \|f_n\|_1 = \sum_{n=1}^{+\infty} \|f_n\|_1$
Or, par hypothèse, $\sum_{n=1}^{+\infty} \|f_n\|_1 = M < +\infty$.
Donc $g \in L^1(\mathbb{R})$.
Une fonction intégrable est finie presque partout, ce qui signifie que $\lambda(\{x \in \mathbb{R} \mid g(x) = +\infty\}) = 0$.
Ainsi, pour presque tout $x \in \mathbb{R}$, $g(x) < +\infty$, ce qui signifie exactement que la série numérique $\sum f_n(x)$ est absolument convergente.

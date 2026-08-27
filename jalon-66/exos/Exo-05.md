# Exercice 5 : Égalité des intégrales et limite
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $f, g \in \mathcal{M}^+(X)$ telles que $f \le g$ presque partout, c'est-à-dire que $\mu(\{x \in X \mid f(x) > g(x)\}) = 0$.
Démontrer que $\int_X f \, d\mu \le \int_X g \, d\mu$.
*(Note: cet exercice étend la croissance aux inégalités presque partout)*

**Correction :**
1. Soit $N = \{x \in X \mid f(x) > g(x)\}$. Par hypothèse, $\mu(N) = 0$.
2. Nous voulons décomposer l'espace en deux parties : $N$ (où l'inégalité est violée, mais de masse nulle) et $N^c$ (où l'inégalité $f \le g$ est respectée).
3. Écrivons $f = f \mathbf{1}_N + f \mathbf{1}_{N^c}$ et $g = g \mathbf{1}_N + g \mathbf{1}_{N^c}$.
4. Évaluons l'intégrale de $f \mathbf{1}_N$.
   $f \mathbf{1}_N \le +\infty \mathbf{1}_N$. Par croissance de l'intégrale :
   $\int_X f \mathbf{1}_N \, d\mu \le \int_X (+\infty \mathbf{1}_N) \, d\mu = (+\infty) \cdot \mu(N) = 0$.
   Donc $\int_X f \mathbf{1}_N \, d\mu = 0$. De même $\int_X g \mathbf{1}_N \, d\mu = 0$.
5. Sur $N^c$, on a $f(x) \le g(x)$, donc ponctuellement sur $X$ : $f \mathbf{1}_{N^c} \le g \mathbf{1}_{N^c}$.
   Par croissance de l'intégrale :
   $\int_X f \mathbf{1}_{N^c} \, d\mu \le \int_X g \mathbf{1}_{N^c} \, d\mu$.
6. Utilisons l'additivité de l'intégrale (qui sera formellement établie par Beppo-Levi pour les fonctions mesurables, mais qu'on admet pour la décomposition sur partition) :
   $$\int_X f \, d\mu = \int_X f \mathbf{1}_N \, d\mu + \int_X f \mathbf{1}_{N^c} \, d\mu = 0 + \int_X f \mathbf{1}_{N^c} \, d\mu \le 0 + \int_X g \mathbf{1}_{N^c} \, d\mu = \int_X g \, d\mu$$
   L'inégalité est prouvée.

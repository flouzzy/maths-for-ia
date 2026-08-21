## Mesurabilité de la limite simple \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur un espace $(X, \mathcal{F})$ à valeurs dans $\mathbb{R}$.
On suppose que la suite converge simplement vers une fonction $f : X \to \mathbb{R}$, c'est-à-dire que pour tout $x \in X$, $\lim_{n \to \infty} f_n(x) = f(x)$.
Démontrez que la limite $f$ est une fonction mesurable.

### Correction Détaillée

L'idée est d'exprimer la limite simple à l'aide des opérateurs $\limsup$ et $\liminf$, qui se construisent par des infimums et suprémums dénombrables.

1. Puisque la suite $(f_n)$ converge simplement, on sait que pour tout $x \in X$ :
   $$ f(x) = \lim_{n \to \infty} f_n(x) = \limsup_{n \to \infty} f_n(x) $$

2. Par définition géométrique et analytique de la limite supérieure :
   $$ \limsup_{n \to \infty} f_n(x) = \inf_{k \geq 0} \left( \sup_{n \geq k} f_n(x) \right) $$

3. Considérons d'abord la suite de fonctions $g_k(x) = \sup_{n \geq k} f_n(x)$.
   Le supremum d'une suite (finie ou dénombrable) de fonctions mesurables est mesurable. En effet :
   $$ g_k^{-1}(]a, +\infty]) = \bigcup_{n \ge k} f_n^{-1}(]a, +\infty]) $$
   L'union dénombrable d'ensembles mesurables étant mesurable, $g_k$ est mesurable pour tout $k$.

4. Ensuite, on considère l'infimum infini $f(x) = \inf_{k \geq 0} g_k(x)$.
   L'infimum d'une suite de fonctions mesurables est également mesurable. La preuve est symétrique :
   $$ f^{-1}([-\infty, a[) = \bigcup_{k \geq 0} g_k^{-1}([-\infty, a[) $$
   L'union dénombrable d'ensembles mesurables étant mesurable, $f$ est mesurable.

Conclusion : Toute limite simple d'une suite de fonctions mesurables reste mesurable, ce qui est une propriété fondamentale et puissante (non vraie pour la continuité).

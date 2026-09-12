# Exercice 8 : Un lemme de Fatou ponctuel
$\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $f_n$ une suite de fonctions positives intégrables sur $(X, \mathcal{A}, \mu)$.
On suppose que $\lim_{n \to \infty} \int_X f_n d\mu = 0$.
Montrer que la suite $(f_n)$ ne converge pas nécessairement ponctuellement vers $0$, mais qu'il existe une sous-suite $(f_{n_k})$ qui converge vers $0$ presque partout.

## Correction
**1. Contre-exemple pour la convergence ponctuelle :**
Prenons l'espace $[0, 1]$ avec la mesure de Lebesgue.
Construisons la suite des "blocs baladeurs" :
$f_1 = \mathbf{1}_{[0, 1]}$
$f_2 = \mathbf{1}_{[0, 1/2]}, \quad f_3 = \mathbf{1}_{[1/2, 1]}$
$f_4 = \mathbf{1}_{[0, 1/4]}, \quad f_5 = \mathbf{1}_{[1/4, 2/4]}, \quad f_6 = \mathbf{1}_{[2/4, 3/4]}, \quad f_7 = \mathbf{1}_{[3/4, 1]}$
... et ainsi de suite.
L'intégrale de la $n$-ième fonction tend vers $0$ (la largeur des blocs tend vers $0$).
Cependant, pour tout $x \in [0, 1]$, $f_n(x)$ prend la valeur $1$ une infinité de fois et la valeur $0$ une infinité de fois. La suite $f_n(x)$ ne converge en aucun point.

**2. Extraction de sous-suite par Borel-Cantelli analytique :**
L'hypothèse est $\int_X f_n d\mu \to 0$.
Par définition de la limite, on peut extraire une sous-suite $(n_k)$ telle que pour tout $k$, $\int_X f_{n_k} d\mu \leq \frac{1}{2^k}$.
Considérons la série de fonctions à termes positifs $g = \sum_{k=1}^\infty f_{n_k}$.
Par le théorème de convergence monotone (ou le corollaire d'intégration terme à terme de Beppo-Levi pour les séries à termes positifs) :
$$\int_X g d\mu = \int_X \left( \sum_{k=1}^\infty f_{n_k} \right) d\mu = \sum_{k=1}^\infty \int_X f_{n_k} d\mu$$
Ainsi, $\int_X g d\mu \leq \sum_{k=1}^\infty \frac{1}{2^k} = 1 < +\infty$.

Puisque l'intégrale de $g$ est finie, la fonction $g(x)$ doit être finie presqu'absolument partout.
Donc, il existe un ensemble de mesure pleine $A \subset X$ (tel que $\mu(X \setminus A) = 0$) sur lequel $g(x) = \sum_{k=1}^\infty f_{n_k}(x) < +\infty$.
Pour que cette série numérique à termes positifs converge en un point $x \in A$, il est nécessaire que le terme général tende vers $0$.
Donc pour tout $x \in A$, $\lim_{k \to \infty} f_{n_k}(x) = 0$.
On a bien extrait une sous-suite qui converge vers $0$ presque partout.

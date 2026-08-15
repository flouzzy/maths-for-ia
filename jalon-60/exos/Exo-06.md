# Exercice 6 : Non-linéarité stricte $\bigstar\bigstar\bigstar\bigstar\star$
Si la fonction d'activation est $\sigma(t) = at + b$, le théorème d'approximation universelle est-il valable ?

\textbf{Correction détaillée}
Non. L'ensemble $S$ des réseaux s'écrit $G(x) = \sum_{j=1}^N \alpha_j (a(w_j^T x) + b_j + b) = (\sum \alpha_j a w_j)^T x + \sum \alpha_j(b_j+b)$.
C'est-à-dire $G(x) = W^T x + B$ où $W \in \mathbb{R}^n$ et $B \in \mathbb{R}$.
$S$ est exactement l'espace des fonctions affines sur $\mathbb{R}^n$.
L'espace des fonctions affines est un sous-espace vectoriel de dimension finie $n+1$.
Dans l'espace $\mathcal{C}(I_n)$ qui est de dimension infinie, un sous-espace de dimension finie est toujours fermé (et complet), et ne peut donc pas être dense.
Il est impossible d'approcher uniformément une fonction non-affine, par exemple $f(x) = x^2$ sur $[0,1]$.
Si $\sup_{x \in [0,1]} |x^2 - (Wx+B)| < \epsilon$, alors les dérivées secondes devraient être proches, ce qui n'est pas le cas.

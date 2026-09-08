# Exercice 3 : Série de fonctions et interversion

**Difficulté :** $\bigstar\bigstar\☆☆\☆☆$

## Énoncé

Soit $f(x) = \sum_{n=1}^\infty \frac{\sin^2(nx)}{n^3}$. Montrer que l'intégrale sur $[0, \pi]$ de $f$ se calcule terme à terme, et évaluer cette intégrale.

## Démonstration rigoureuse pas à pas

Posons $u_n(x) = \frac{\sin^2(nx)}{n^3}$. Pour tout $x \in [0, \pi]$, $u_n(x) \ge 0$. Par le corollaire du théorème de Beppo-Levi (pour les séries à termes positifs), on peut intervertir la série et l'intégrale de Lebesgue : $\int_0^\pi \left( \sum_{n=1}^\infty \frac{\sin^2(nx)}{n^3} \right) dx = \sum_{n=1}^\infty \int_0^\pi \frac{\sin^2(nx)}{n^3} dx$. On calcule $\int_0^\pi \sin^2(nx) dx = \int_0^\pi \frac{1 - \cos(2nx)}{2} dx = \frac{\pi}{2}$. L'intégrale vaut donc $\sum_{n=1}^\infty \frac{\pi}{2n^3} = \frac{\pi}{2} \zeta(3)$, où $\zeta$ est la fonction zêta de Riemann.

# Exercice 6 : Convergence de la somme de Dirichlet

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\☆$

## Énoncé

Prouver rigoureusement l'égalité $\int_0^\infty \frac{x}{e^x - 1} dx = \sum_{n=1}^\infty \frac{1}{n^2}$ (fonction Zeta de Riemann) en utilisant Beppo-Levi.

## Démonstration rigoureuse pas à pas

Sur $]0, \infty[$, $\frac{x}{e^x - 1} = \frac{x e^{-x}}{1 - e^{-x}}$. Comme $0 < e^{-x} < 1$, on développe en série géométrique : $\frac{x e^{-x}}{1 - e^{-x}} = \sum_{n=1}^\infty x e^{-nx}$. Posons $g_n(x) = x e^{-nx}$. Les $g_n$ sont mesurables et strictement positives sur $]0, \infty[$. Par le corollaire du théorème de Beppo-Levi, on intervertit série et intégrale : $\int_0^\infty \left( \sum_{n=1}^\infty x e^{-nx} \right) dx = \sum_{n=1}^\infty \int_0^\infty x e^{-nx} dx$. Avec le changement de variable $u = nx$, $du = n dx$, on a $\int_0^\infty x e^{-nx} dx = \frac{1}{n^2} \int_0^\infty u e^{-u} du = \frac{1}{n^2} \Gamma(2) = \frac{1}{n^2}$. Ainsi, l'intégrale vaut $\sum_{n=1}^\infty \frac{1}{n^2} = \zeta(2) = \frac{\pi^2}{6}$.

# Exercice 4 : Séries de Dirichlet \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Justifier que $\int_0^\infty \frac{x^{s-1}}{e^x - 1} dx = \Gamma(s) \zeta(s)$ pour $s > 1$.

## Correction Détaillée
On écrit $\frac{1}{e^x - 1} = \frac{e^{-x}}{1 - e^{-x}} = \sum_{n=1}^\infty e^{-nx}$.
Donc $\frac{x^{s-1}}{e^x - 1} = \sum_{n=1}^\infty x^{s-1} e^{-nx}$.
Les termes de la série sont des fonctions mesurables et positives sur $]0, +\infty[$.
Par le corollaire du Théorème de Convergence Monotone :
$$\int_0^\infty \sum_{n=1}^\infty x^{s-1} e^{-nx} dx = \sum_{n=1}^\infty \int_0^\infty x^{s-1} e^{-nx} dx$$
Dans l'intégrale, on effectue le changement de variable $u = nx$, $du = n dx$, $x = u/n$.
L'intégrale devient $\int_0^\infty (u/n)^{s-1} e^{-u} \frac{du}{n} = \frac{1}{n^s} \int_0^\infty u^{s-1} e^{-u} du = \frac{\Gamma(s)}{n^s}$.
Ainsi, la somme devient $\sum_{n=1}^\infty \frac{\Gamma(s)}{n^s} = \Gamma(s) \sum_{n=1}^\infty \frac{1}{n^s} = \Gamma(s) \zeta(s)$.

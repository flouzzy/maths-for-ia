# Exercice 1 : Décomposition basique d'une fonction signée
$\bigstar\star\star\star\star$

## Énoncé
Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x^2 - 4$.
Explicitez rigoureusement ses parties positive $f^+$ et négative $f^-$, et tracez brièvement leur comportement sur $\mathbb{R}$. Calculez ensuite l'intégrale de Lebesgue de $f$ sur le segment $[0, 3]$.

## Correction
**1. Identification des parties positive et négative :**
La fonction s'annule en $x = -2$ et $x = 2$.
- Sur $]-\infty, -2] \cup [2, +\infty[$, $f(x) \geq 0$. Donc $f^+(x) = x^2 - 4$ et $f^-(x) = 0$.
- Sur $[-2, 2]$, $f(x) \leq 0$. Donc $f^+(x) = 0$ et $f^-(x) = -(x^2 - 4) = 4 - x^2$.

**2. Calcul de l'intégrale sur $X = [0, 3]$ :**
Sur $[0, 3]$, l'intégrale de Lebesgue coïncide avec l'intégrale de Riemann car les fonctions sont continues.
On a $f = f^+ - f^-$.
$\int_{[0,3]} f d\lambda = \int_{[0,3]} f^+ d\lambda - \int_{[0,3]} f^- d\lambda$.
- $\int_{[0,3]} f^+ d\lambda = \int_2^3 (x^2 - 4) dx = \left[ \frac{x^3}{3} - 4x \right]_2^3 = \left( \frac{27}{3} - 12 \right) - \left( \frac{8}{3} - 8 \right) = -3 - \left( -\frac{16}{3} \right) = \frac{7}{3}$.
- $\int_{[0,3]} f^- d\lambda = \int_0^2 (4 - x^2) dx = \left[ 4x - \frac{x^3}{3} \right]_0^2 = 8 - \frac{8}{3} = \frac{16}{3}$.

L'intégrale totale est :
$\int_{[0,3]} f d\lambda = \frac{7}{3} - \frac{16}{3} = -\frac{9}{3} = -3$.
On vérifie avec le calcul direct : $\int_0^3 (x^2 - 4) dx = \left[ \frac{x^3}{3} - 4x \right]_0^3 = 9 - 12 = -3$.
La décomposition de Lebesgue est donc parfaitement consistante.

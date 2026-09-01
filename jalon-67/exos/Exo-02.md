---
title: "Exercice 2 : Série de fonctions et mesure de Lebesgue"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 2 : Série de fonctions et mesure de Lebesgue

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Montrer que $\int_0^{+\infty} \frac{x}{e^x - 1} dx = \sum_{n=1}^\infty \frac{1}{n^2}$ (sans calculer la valeur finale de la série).

## Correction Détaillée

1. La fonction à intégrer est positive sur $]0, +\infty[$. Écrivons-la sous forme d'une série :
   $$\frac{x}{e^x - 1} = \frac{x e^{-x}}{1 - e^{-x}}$$
2. Pour tout $x > 0$, $0 < e^{-x} < 1$. On peut utiliser le développement en série géométrique : $\frac{1}{1 - e^{-x}} = \sum_{n=0}^\infty e^{-nx}$.
3. Ainsi, $\frac{x}{e^x - 1} = x e^{-x} \sum_{n=0}^\infty e^{-nx} = \sum_{n=0}^\infty x e^{-(n+1)x} = \sum_{k=1}^\infty x e^{-kx}$ (en posant $k = n+1$).
4. Posons $u_k(x) = x e^{-kx}$. Chaque fonction $u_k$ est mesurable (car continue) et positive sur $]0, +\infty[$.
5. Par le théorème de Beppo Levi (corollaire pour les séries), on a :
   $$\int_0^{+\infty} \left( \sum_{k=1}^\infty x e^{-kx} \right) dx = \sum_{k=1}^\infty \int_0^{+\infty} x e^{-kx} dx$$
6. Calculons l'intégrale $\int_0^{+\infty} x e^{-kx} dx$ par intégration par parties.
   Posons $u = x \implies u' = 1$ et $v' = e^{-kx} \implies v = -\frac{1}{k} e^{-kx}$.
   $$\int_0^{+\infty} x e^{-kx} dx = \left[ -\frac{x}{k} e^{-kx} \right]_0^{+\infty} + \int_0^{+\infty} \frac{1}{k} e^{-kx} dx$$
7. Le terme de bord est nul (car $\lim_{x\to+\infty} x e^{-kx} = 0$). L'intégrale restante donne :
   $$\left[ -\frac{1}{k^2} e^{-kx} \right]_0^{+\infty} = 0 - \left( -\frac{1}{k^2} \right) = \frac{1}{k^2}$$
8. En réinjectant dans la somme, on trouve bien :
   $$\int_0^{+\infty} \frac{x}{e^x - 1} dx = \sum_{k=1}^\infty \frac{1}{k^2}$$

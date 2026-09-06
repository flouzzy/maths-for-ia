---
uuid: "exo-67-02"
title: "Exercice 02 : Intégrale de la série géométrique"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 02 : Intégrale de la série géométrique ($\bigstar\star\star\star\star$)

## Énoncé

On pose $f_n(x) = 1 + x + x^2 + \dots + x^n$ sur $]0, 1[$. Justifier que $\int_0^1 \frac{1}{1-x} dx = \sum_{k=0}^\infty \frac{1}{k+1}$.

## Corrigé Rigoureux

1. **Fonctions :** $u_n(x) = x^n$. Sur $]0, 1[$, $u_n$ est mesurable et positive.
2. **Sommation terme à terme :** D'après le corollaire du théorème de convergence monotone, on peut intervertir la somme infinie et l'intégrale pour des fonctions positives.
$$\int_0^1 \left(\sum_{k=0}^\infty x^k\right) dx = \sum_{k=0}^\infty \int_0^1 x^k dx$$
3. **Calcul :** $\int_0^1 x^k dx = \left[ \frac{x^{k+1}}{k+1} \right]_0^1 = \frac{1}{k+1}$.
La série de gauche vaut $\int_0^1 \frac{1}{1-x} dx$, qui diverge vers $+\infty$, tout comme la série harmonique.

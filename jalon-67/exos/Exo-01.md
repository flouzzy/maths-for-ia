# Exercice 1 : Intégrale de la série géométrique \quad $\bigstar\star\star\star\star$

## Énoncé
Calculer rigoureusement $\int_0^1 \sum_{n=1}^\infty x^n dx$.

## Correction Détaillée
On pose $u_n(x) = x^n$. Chaque $u_n$ est mesurable et positive sur $[0,1]$.
Par le corollaire de Beppo Levi, on peut intervertir la somme et l'intégrale.
$$\int_0^1 \sum_{n=1}^\infty x^n dx = \sum_{n=1}^\infty \int_0^1 x^n dx = \sum_{n=1}^\infty \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \sum_{n=1}^\infty \frac{1}{n+1}$$
Ceci correspond à la série harmonique privée de son premier terme, qui diverge. La valeur de l'intégrale est donc $+\infty$.

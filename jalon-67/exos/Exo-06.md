# Exercice 6 : Linéarité de l'intégrale pour des séries \quad $\bigstar\star\star\star\star$

## Énoncé
Calculer l'intégrale de $\sum_{n=0}^\infty 2^{-n} x^2$ sur $[0, 1]$.

## Correction Détaillée
Les fonctions $u_n(x) = 2^{-n} x^2$ sont positives. Le théorème de sommation terme à terme donne :
$$\int_0^1 \sum_{n=0}^\infty 2^{-n} x^2 dx = \sum_{n=0}^\infty \int_0^1 2^{-n} x^2 dx = \sum_{n=0}^\infty 2^{-n} \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3} \sum_{n=0}^\infty 2^{-n}$$
La somme de la série géométrique est $\frac{1}{1-1/2} = 2$. Le résultat final est donc $2/3$.

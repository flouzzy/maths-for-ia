# Exercice 1 : Intégrale d'une série géométrique $\bigstar\star\star\star\star$

## Énoncé
Calculer $\int_0^1 \sum_{n=1}^\infty x^n dx$ en justifiant rigoureusement toutes les étapes.

## Correction Détaillée
1. Les fonctions $u_n(x) = x^n$ sont mesurables et positives sur l'intervalle $[0, 1]$.
2. Par le corollaire du Théorème de Convergence Monotone (sommation terme à terme de fonctions mesurables positives), on peut intervertir la série et l'intégrale :
   $$ \int_0^1 \left( \sum_{n=1}^\infty x^n \right) dx = \sum_{n=1}^\infty \int_0^1 x^n dx $$
3. Calculons l'intégrale de chaque terme :
   $$ \int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1} $$
4. La somme devient donc la série harmonique tronquée de son premier terme :
   $$ \sum_{n=1}^\infty \frac{1}{n+1} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \ldots $$
5. On sait que la série harmonique diverge vers $+\infty$. Par conséquent, l'intégrale de départ vaut $+\infty$.

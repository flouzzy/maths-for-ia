# Exercice 1 : Application directe du théorème

**Difficulté :** $\bigstar\☆☆\☆☆$

## Énoncé

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $(f_n)$ une suite de fonctions mesurables positives. Montrer que si $f_n$ décroît vers $f$ avec $\int f_1 d\mu < \infty$, alors $\lim \int f_n = \int f$. (Indice : appliquer Beppo-Levi à $g_n = f_1 - f_n$)

## Démonstration rigoureuse pas à pas

On pose $g_n = f_1 - f_n$. Puisque $(f_n)$ est décroissante, la suite $(g_n)$ est une suite croissante de fonctions mesurables positives. De plus, $g_n$ converge simplement vers $f_1 - f$. Par le théorème de Beppo-Levi appliqué à $(g_n)$, on a : $\lim_{n \to \infty} \int_X (f_1 - f_n) d\mu = \int_X (f_1 - f) d\mu$. Comme $\int f_1 d\mu < \infty$, la linéarité de l'intégrale permet d'écrire $\int f_1 d\mu - \lim_{n \to \infty} \int_X f_n d\mu = \int_X f_1 d\mu - \int_X f d\mu$. Les termes finis se simplifient, donnant le résultat : $\lim \int f_n = \int f$.

# Exercice 10

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Construction d'une variable aléatoire singulière (L'Escalier du Diable de Cantor) : On considère $\Omega = [0, 1]$ muni de la tribu borélienne et de la mesure de Lebesgue. Décrire brièvement pourquoi la fonction de répartition de Cantor, bien que continue, définit une variable aléatoire (loi de Cantor) dont le support est de mesure de Lebesgue nulle.

## Correction Détaillée

**Correction de l'exercice 10 :**

1. L'ensemble triadique de Cantor $C$ s'obtient en retirant itérativement le tiers central ouvert de chaque intervalle, à partir de $[0,1]$.
2. La mesure de Lebesgue de l'ensemble de Cantor est $\lambda(C) = 1 - \sum_{n=1}^\infty \frac{2^{n-1}}{3^n} = 1 - \frac{1/3}{1 - 2/3} = 0$.
3. La fonction de Cantor (escalier du diable) $F_C(x)$ est définie en attribuant des valeurs constantes sur les intervalles retirés (ex: $1/2$ sur $]1/3, 2/3[$). Elle est prolongée de manière continue sur $C$.
4. $F_C(x)$ est une fonction croissante, continue, avec $F_C(0)=0$ et $F_C(1)=1$. Elle satisfait donc toutes les propriétés d'une fonction de répartition d'une variable aléatoire réelle $X$.
5. La loi de cette variable aléatoire, $\mathbb{P}_X$, est caractérisée par cette fonction.
6. La dérivée $F_C'(x)$ est nulle sur les intervalles retirés. Comme $C$ est de mesure nulle, $F_C'(x) = 0$ presque partout.
7. Cependant, $\int_0^1 F_C'(x) dx = 0 \neq F_C(1) - F_C(0) = 1$. Cette variable n'est donc pas absolument continue.
8. Tout l'accroissement de la fonction (la probabilité) est concentré sur l'ensemble de Cantor $C$. On a $\mathbb{P}_X(C) = 1$, alors que la mesure de Lebesgue $\lambda(C) = 0$.
9. C'est le prototype d'une variable aléatoire à loi diffuse mais singulière (étrangère) par rapport à la mesure de Lebesgue.
$\blacksquare$

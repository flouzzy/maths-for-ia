# Exercice 7 : Hyperplans d'appui
$\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $E$ un espace normé et $B$ sa boule unité fermée. Soit $x_0 \in E$ tel que $\|x_0\| = 1$.
Montrer qu'il existe un hyperplan fermé $H$ tel que $x_0 \in H$ et $B$ est entièrement contenue dans un des demi-espaces fermés délimités par $H$. (Hyperplan d'appui).

## Correction Détaillée
1. On applique le corollaire de Hahn-Banach : il existe $f \in E^*$ telle que $\|f\| = 1$ et $f(x_0) = \|x_0\| = 1$.
2. Posons $H = \{ x \in E \mid f(x) = 1 \}$. C'est le noyau de $f(\cdot) - 1$, qui est un hyperplan fermé (car $f$ est continue).
3. On a bien $x_0 \in H$ car $f(x_0) = 1$.
4. Pour tout $x \in B$, $\|x\| \le 1$.
5. Puisque $\|f\| = 1$, on a pour tout $x \in B$, $f(x) \le |f(x)| \le \|f\|\|x\| \le 1 \times 1 = 1$.
6. L'ensemble $B$ est donc inclus dans le demi-espace $\{ x \in E \mid f(x) \le 1 \}$.
L'hyperplan $H$ est l'hyperplan d'appui recherché. $\blacksquare$

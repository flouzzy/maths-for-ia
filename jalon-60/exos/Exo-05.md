---
title: "Exercice 5 : La cassure de la fonction ReLU et les dérivées"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 5 : La cassure de la fonction ReLU et les dérivées

## Énoncé

Soit $f(x) = x^2$ sur $[0, 1]$. On approche $f$ par une combinaison linéaire de fonctions ReLU : $G(x) = \sum_{i=1}^N \alpha_i \max(0, x - t_i)$.
Est-il possible que l'approximation de la dérivée, $G'(x)$, converge uniformément vers la dérivée de la fonction cible, $f'(x) = 2x$ ? Expliquez les conditions pathologiques de cette dérivation au sens classique.

## Correction Rigoureuse

**Étape 1 : Examen de la dérivabilité de $G$**
La fonction $x \mapsto \max(0, x - t_i)$ est continue partout mais non dérivable en $x = t_i$.
Sur tout intervalle ne contenant pas de point de "cassure" $t_i$, la dérivée de $\max(0, x - t_i)$ vaut soit 0 (si $x < t_i$) soit 1 (si $x > t_i$).
Ainsi, $G'(x)$ est une fonction en escalier qui prend un nombre fini de valeurs constantes.

**Étape 2 : Comparaison avec $f'(x)$**
La fonction cible $f'(x) = 2x$ est continue et strictement croissante.
L'approximation $G'(x)$ est constante par morceaux.
Bien que $G'(x)$ puisse être proche de $f'(x)$ (une fonction en escalier peut approcher une droite en norme $L^p$ ou $L^\infty$), l'erreur $\|f' - G'\|_\infty$ ne convergera pas uniformément vers zéro à proximité des sauts des échelons, à cause du phénomène de Gibbs.

**Étape 3 : Convergence au sens des distributions**
Dans le cadre de l'analyse classique, la limite uniforme des dérivées nécessiterait des fonctions d'activation au moins $\mathcal{C}^1$ (comme la sigmoïde, la tangente hyperbolique, ou l'activation GELU). Avec ReLU, la convergence des dérivées a lieu faiblement (au sens des espaces de Sobolev $W^{1, \infty}$), mais $G$ ne sera jamais de classe $\mathcal{C}^1$. C'est une limitation géométrique intrinsèque de ReLU. $\blacksquare$

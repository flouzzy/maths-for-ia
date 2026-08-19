# Exercice 8 : Contre-exemple sans la condition finie

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Trouver un exemple de suite décroissante d'ensembles mesurables $(A_n)$ pour laquelle la conclusion de l'exercice 7 est fausse. Expliquer pourquoi la condition $\lambda(A_1) < \infty$ est cruciale.

## Correction Détaillée

1. Prenons les intervalles $A_n = [n, \infty[$.
2. La suite est bien décroissante : $[1, \infty[ \supset [2, \infty[ \supset \dots$
3. Pour tout $n$, $A_n$ a une longueur infinie, donc $\lambda(A_n) = \infty$. La limite de la suite des mesures est $\infty$.
4. Quelle est l'intersection $A = \bigcap_{n=1}^\infty A_n$ ? Il s'agit des réels qui sont supérieurs à $n$ pour TOUT entier $n$. Par la propriété d'Archimède, aucun réel ne vérifie cela. Donc $A = \emptyset$.
5. La mesure de l'intersection est $\lambda(\emptyset) = 0$.
6. On a donc $\lambda(A) = 0 \neq \infty = \lim \lambda(A_n)$.
La condition que l'un des ensembles (par exemple $A_1$) ait une mesure finie évite l'indétermination "$\infty - \infty$" à l'étape 5 de la démonstration précédente.

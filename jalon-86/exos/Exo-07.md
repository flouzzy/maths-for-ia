# Exercice 7

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $X$ une variable aléatoire réelle de loi symétrique par rapport à 0, c'est-à-dire que $X$ et $-X$ ont la même loi. Montrer que si $F_X$ est sa fonction de répartition, on a pour tout $x \in \mathbb{R}$, $F_X(x) = 1 - F_X(-x) + P(X = -x)$.

## Correction Détaillée

**Correction de l'exercice 7 :**

1. Par définition, $F_X(x) = P(X \leq x)$.
2. Puisque $X$ et $-X$ ont la même loi, $P(-X \leq x) = P(X \leq x) = F_X(x)$.
3. L'événement $\{-X \leq x\}$ équivaut à $\{X \geq -x\}$.
4. On peut réécrire cet événement comme l'union disjointe $\{X > -x\} \cup \{X = -x\}$.
5. La probabilité de l'événement strictement supérieur est $P(X > -x) = 1 - P(X \leq -x) = 1 - F_X(-x)$.
6. Donc $P(X \geq -x) = 1 - F_X(-x) + P(X = -x)$.
7. En combinant l'étape 2 et l'étape 6, on obtient l'égalité demandée : $F_X(x) = 1 - F_X(-x) + P(X = -x)$.
8. (Remarque : Si $X$ est à densité, la probabilité ponctuelle est nulle, donc $F_X(x) = 1 - F_X(-x)$).
$\blacksquare$

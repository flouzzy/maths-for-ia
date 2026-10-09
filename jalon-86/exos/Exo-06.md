# Exercice 6

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $X$ une variable aléatoire réelle dont la loi est diffuse (sans atomes, i.e., $P(X=x)=0$ pour tout $x$). Soit $F_X(x) = P(X \leq x)$ sa fonction de répartition. Montrer que la variable aléatoire $Y = F_X(X)$ suit une loi uniforme sur $[0, 1]$.

## Correction Détaillée

**Correction de l'exercice 6 :**

1. L'application $F_X$ est continue, croissante, avec des valeurs dans $[0, 1]$, car la loi de $X$ est diffuse.
2. Pour tout $y \in [0, 1]$, on veut calculer $P(Y \leq y) = P(F_X(X) \leq y)$.
3. Définissons le pseudo-inverse $F_X^{-1}(y) = \inf \{x \in \mathbb{R} \mid F_X(x) \geq y\}$.
4. Grâce à la croissance et la continuité de $F_X$, l'événement $\{F_X(X) \leq y\}$ est équivalent (à probabilité 1 près) à l'événement $\{X \leq F_X^{-1}(y)\}$.
5. Donc $P(Y \leq y) = P(X \leq F_X^{-1}(y))$.
6. Par définition de la fonction de répartition de $X$, $P(X \leq F_X^{-1}(y)) = F_X(F_X^{-1}(y))$.
7. Comme $F_X$ est continue, $F_X(F_X^{-1}(y)) = y$.
8. Ainsi, pour tout $y \in [0, 1]$, $P(Y \leq y) = y$. C'est précisément la fonction de répartition de la loi uniforme $\mathcal{U}([0,1])$.
$\blacksquare$

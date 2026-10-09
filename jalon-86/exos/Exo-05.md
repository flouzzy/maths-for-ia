# Exercice 5 : Minimum de deux lois exponentielles \quad $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soient $X_1$ et $X_2$ deux variables aléatoires indépendantes suivant des lois exponentielles de paramètres respectifs $\lambda_1 > 0$ et $\lambda_2 > 0$.
Soit $Y = \min(X_1, X_2)$.
Démontrer que $Y$ suit une loi exponentielle dont on précisera le paramètre.

## Correction

Pour étudier le minimum de deux variables aléatoires, il est plus pertinent de calculer la probabilité complémentaire $\mathbb{P}(Y > y)$, qui correspond à $1 - F_Y(y)$, où $F_Y$ est la fonction de répartition de $Y$.
La variable aléatoire $Y$ prend ses valeurs dans $[0, +\infty[$, donc pour tout $y < 0$, $\mathbb{P}(Y > y) = 1$.

Soit $y \geq 0$. L'événement $\{Y > y\}$ signifie que le minimum de $X_1$ et $X_2$ est strictement supérieur à $y$. Cela implique nécessairement que *chacune* des variables est strictement supérieure à $y$.
$$ \mathbb{P}(Y > y) = \mathbb{P}(\min(X_1, X_2) > y) = \mathbb{P}(X_1 > y \text{ et } X_2 > y) $$
Puisque les variables aléatoires $X_1$ et $X_2$ sont indépendantes, la probabilité de l'intersection des événements est le produit des probabilités :
$$ \mathbb{P}(Y > y) = \mathbb{P}(X_1 > y) \times \mathbb{P}(X_2 > y) $$

Pour une variable $X \sim \mathcal{E}(\lambda)$, on sait que sa fonction de répartition est $F_X(x) = 1 - e^{-\lambda x}$ pour $x \geq 0$. Donc la probabilité d'excéder un seuil $y$ est $\mathbb{P}(X > y) = 1 - F_X(y) = e^{-\lambda y}$.
En appliquant ceci à $X_1$ (paramètre $\lambda_1$) et à $X_2$ (paramètre $\lambda_2$), on obtient :
$$ \mathbb{P}(X_1 > y) = e^{-\lambda_1 y} \quad \text{et} \quad \mathbb{P}(X_2 > y) = e^{-\lambda_2 y} $$
D'où :
$$ \mathbb{P}(Y > y) = e^{-\lambda_1 y} \times e^{-\lambda_2 y} = e^{-(\lambda_1 + \lambda_2)y} $$

La fonction de répartition de $Y$ est donc :
$$ F_Y(y) = 1 - \mathbb{P}(Y > y) = 1 - e^{-(\lambda_1 + \lambda_2)y} $$
pour $y \geq 0$. C'est l'expression exacte de la fonction de répartition d'une loi exponentielle de paramètre $\lambda = \lambda_1 + \lambda_2$.
Conclusion : Le minimum de variables aléatoires exponentielles indépendantes suit une loi exponentielle dont le paramètre est la somme des paramètres. $\blacksquare$

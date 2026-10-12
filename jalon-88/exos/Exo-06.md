# Exercice 6 : Indépendance et espérance (Covariance nulle)

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires discrètes admettant des moments d'ordre 2.
L'énoncé stipule que $X$ prend les valeurs $\{-1, 0, 1\}$ avec les probabilités respectives $1/4, 1/2, 1/4$.
Soit la variable aléatoire $Y = X^2$.
1. Déterminer la loi de la variable aléatoire $Y$.
2. Calculer l'espérance de $X$, $\mathbb{E}[X]$, et l'espérance de $Y$, $\mathbb{E}[Y]$.
3. Calculer l'espérance du produit, $\mathbb{E}[XY]$.
4. Démontrer que la covariance entre $X$ et $Y$ est nulle.
5. $X$ et $Y$ sont-elles indépendantes ? Expliquez pourquoi.

---
**Correction détaillée :**

**Question 1 : Loi de $Y$**
Puisque $Y = X^2$, les valeurs possibles de $Y$ sont $0^2 = 0$ et $(\pm 1)^2 = 1$.
- $\mathbb{P}(Y = 0) = \mathbb{P}(X^2 = 0) = \mathbb{P}(X = 0) = \frac{1}{2}$.
- $\mathbb{P}(Y = 1) = \mathbb{P}(X^2 = 1) = \mathbb{P}(X = 1) + \mathbb{P}(X = -1) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$.
La loi de $Y$ est donc une loi de Bernoulli de paramètre $p = \frac{1}{2}$.

**Question 2 : Calcul des espérances simples**
- $\mathbb{E}[X] = (-1) \times \frac{1}{4} + 0 \times \frac{1}{2} + 1 \times \frac{1}{4} = -\frac{1}{4} + \frac{1}{4} = 0$.
- $\mathbb{E}[Y] = 0 \times \frac{1}{2} + 1 \times \frac{1}{2} = \frac{1}{2}$.

**Question 3 : Espérance du produit**
On a le produit $XY = X \times X^2 = X^3$.
Les valeurs possibles de $X^3$ sont $(-1)^3 = -1$, $0^3 = 0$, et $1^3 = 1$, avec les mêmes probabilités que $X$.
- $\mathbb{E}[XY] = \mathbb{E}[X^3] = (-1) \times \frac{1}{4} + 0 \times \frac{1}{2} + 1 \times \frac{1}{4} = 0$.

**Question 4 : Calcul de la covariance**
Par définition, la covariance est donnée par :
$$ \text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] $$
En remplaçant par les valeurs calculées :
$$ \text{Cov}(X, Y) = 0 - (0 \times \frac{1}{2}) = 0 $$
La covariance entre $X$ et $Y$ est donc strictement nulle. Les variables sont non-corrélées.

**Question 5 : Étude de l'indépendance**
Pour vérifier l'indépendance, il faut que pour toutes les valeurs, $\mathbb{P}(X=x, Y=y) = \mathbb{P}(X=x)\mathbb{P}(Y=y)$.
Prenons un point de test, par exemple $x=0$ et $y=1$.
- D'un côté, le produit des probabilités marginales est : $\mathbb{P}(X=0) \times \mathbb{P}(Y=1) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.
- De l'autre côté, la probabilité conjointe : $\mathbb{P}(X=0 \text{ et } Y=1)$. Puisque $Y = X^2$, si $X=0$, on a obligatoirement $Y=0$. Il est donc absolument impossible d'avoir simultanément $X=0$ et $Y=1$.
Donc $\mathbb{P}(X=0, Y=1) = 0$.
Puisque $0 \neq \frac{1}{4}$, l'égalité fondamentale de l'indépendance est rompue.
**Conclusion :** Les variables $X$ et $Y$ **ne sont pas indépendantes**, bien que leur covariance soit nulle. Cela démontre que si l'indépendance implique la non-corrélation, la réciproque est globalement fausse. $\blacksquare$

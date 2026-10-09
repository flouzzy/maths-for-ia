# Exercice 4 : Loi d'un produit de variables de Bernoulli \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**

Soient $X_1$ et $X_2$ deux variables aléatoires de Bernoulli indépendantes, avec pour paramètres respectifs $p_1$ et $p_2$.
Déterminer la loi de la variable aléatoire $Y = X_1 X_2$ et calculer son espérance.

**Correction Détaillée :**

1. Les variables $X_1$ et $X_2$ suivent des lois de Bernoulli, elles prennent donc leurs valeurs dans $\{0, 1\}$.
2. Par conséquent, leur produit $Y = X_1 X_2$ ne peut prendre des valeurs que dans $\{0, 1\}$.
   - En effet, $1 \times 1 = 1$, $1 \times 0 = 0$, $0 \times 1 = 0$, $0 \times 0 = 0$.
3. $Y$ est donc également une variable aléatoire suivant une loi de Bernoulli. Il nous reste à trouver son paramètre, c'est-à-dire la probabilité de succès $\mathbb{P}(Y = 1)$.
4. L'événement $\{Y = 1\}$ équivaut à $\{X_1 X_2 = 1\}$, ce qui ne se produit que si et seulement si $X_1 = 1$ ET $X_2 = 1$.
   Donc, $\mathbb{P}(Y = 1) = \mathbb{P}(X_1 = 1 \text{ et } X_2 = 1)$.
5. Puisque $X_1$ et $X_2$ sont indépendantes, la probabilité de l'intersection est le produit des probabilités :
   $\mathbb{P}(X_1 = 1 \text{ et } X_2 = 1) = \mathbb{P}(X_1 = 1) \cdot \mathbb{P}(X_2 = 1)$.
6. Par définition des lois de Bernoulli marginales, $\mathbb{P}(X_1 = 1) = p_1$ et $\mathbb{P}(X_2 = 1) = p_2$.
7. Ainsi, $\mathbb{P}(Y = 1) = p_1 p_2$.
8. On conclut que $Y$ suit une loi de Bernoulli de paramètre $p = p_1 p_2$, notée $Y \sim \mathcal{B}(p_1 p_2)$.
9. L'espérance d'une loi de Bernoulli de paramètre $p$ est égale à $p$. Par conséquent, $\mathbb{E}[Y] = p_1 p_2$.
10. Remarque de cohérence : Puisque $X_1$ et $X_2$ sont indépendantes, on savait déjà par théorème que $\mathbb{E}[X_1 X_2] = \mathbb{E}[X_1]\mathbb{E}[X_2] = p_1 p_2$, ce qui confirme notre résultat.

# Exercice 8

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Lemme de Doob-Dynkin : Soient $X, Y$ deux variables aléatoires de $(\Omega, \mathcal{F})$ vers $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. Montrer que $Y$ est mesurable par rapport à la tribu engendrée par $X$, notée $\sigma(X)$, si et seulement si il existe une fonction borélienne $g : \mathbb{R} \to \mathbb{R}$ telle que $Y = g(X)$. (Démontrer le cas où $Y$ est une fonction étagée).

## Correction Détaillée

**Correction de l'exercice 8 :**

1. Si $Y = g(X)$ avec $g$ borélienne, alors $Y$ est mesurable vis-à-vis de $\sigma(X)$ car $Y^{-1}(B) = X^{-1}(g^{-1}(B)) \in \sigma(X)$ pour tout borélien $B$ (car $g^{-1}(B) \in \mathcal{B}(\mathbb{R})$).
2. Sens inverse, cas où $Y$ est étagée : $Y$ prend un nombre fini de valeurs $y_1, ..., y_n$.
3. On peut écrire $Y = \sum_{i=1}^n y_i \mathbf{1}_{A_i}$ où $A_i = \{Y = y_i\}$ forment une partition de $\Omega$.
4. Comme $Y$ est $\sigma(X)$-mesurable, chaque événement $A_i \in \sigma(X)$.
5. Par définition de $\sigma(X)$, il existe des boréliens $B_i \in \mathcal{B}(\mathbb{R})$ tels que $A_i = X^{-1}(B_i)$.
6. Sans perte de généralité, comme les $A_i$ partitionnent $\Omega$, on peut rendre les $B_i$ disjoints (en prenant $B_i' = B_i \setminus \cup_{j<i} B_j$).
7. Posons la fonction $g(x) = \sum_{i=1}^n y_i \mathbf{1}_{B_i}(x)$. C'est une fonction borélienne de $\mathbb{R}$ dans $\mathbb{R}$.
8. Évaluons $g(X(\omega)) = \sum_{i=1}^n y_i \mathbf{1}_{B_i}(X(\omega))$. Or $X(\omega) \in B_i$ ssi $\omega \in X^{-1}(B_i) = A_i$.
9. Ainsi, $g(X(\omega)) = \sum_{i=1}^n y_i \mathbf{1}_{A_i}(\omega) = Y(\omega)$. La propriété est donc prouvée pour les fonctions étagées.
$\blacksquare$

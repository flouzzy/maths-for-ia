# Exercice 2

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soient $X$ et $Y$ deux variables aléatoires réelles sur $(\Omega, \mathcal{F}, \mathbb{P})$. Montrer que $Z = \max(X, Y)$ est une variable aléatoire.

## Correction Détaillée

**Correction de l'exercice 2 :**

1. On utilise le critère de mesurabilité avec les intervalles de la forme $]-\infty, a]$.
2. Il faut montrer que pour tout $a \in \mathbb{R}$, l'ensemble $\{\omega \in \Omega \mid Z(\omega) \leq a\} \in \mathcal{F}$.
3. Or, $\max(X(\omega), Y(\omega)) \leq a$ équivaut à la conjonction : $X(\omega) \leq a$ ET $Y(\omega) \leq a$.
4. Donc, $Z^{-1}(]-\infty, a]) = \{\omega \mid X(\omega) \leq a\} \cap \{\omega \mid Y(\omega) \leq a\}$.
5. Puisque $X$ et $Y$ sont des variables aléatoires, $A_a = \{\omega \mid X(\omega) \leq a\} \in \mathcal{F}$ et $B_a = \{\omega \mid Y(\omega) \leq a\} \in \mathcal{F}$.
6. La tribu $\mathcal{F}$ étant stable par intersection finie, $A_a \cap B_a \in \mathcal{F}$.
7. Ainsi, $Z$ est bien une variable aléatoire.
$\blacksquare$

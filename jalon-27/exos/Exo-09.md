---
uuid: "jalon-27-exo-09"
title: "Exercice 09 : Valeurs propres d'une matrice orthogonale"
---
# Exercice 09 : Valeurs propres d'une matrice orthogonale

**Difficulté :** ★★★★★

## Énoncé

Montrer que les valeurs propres réelles d'une matrice orthogonale sont dans $\{-1, 1\}$.

## Démonstration sans ellipse

Soit $A$ une matrice orthogonale et $\lambda \in \mathbb{R}$ une valeur propre associée à un vecteur propre $x \neq 0$.
Par définition, $Ax = \lambda x$.
On a $\|Ax\|^2 = (Ax)^T (Ax) = x^T A^T A x$.
Puisque $A$ est orthogonale, $A^T A = I_n$.
Donc $\|Ax\|^2 = x^T I_n x = x^T x = \|x\|^2$.
D'autre part, $\|Ax\|^2 = \|\lambda x\|^2 = \lambda^2 \|x\|^2$.
En égalant, on obtient $\lambda^2 \|x\|^2 = \|x\|^2$.
Comme $x \neq 0$, $\|x\|^2 \neq 0$, donc on peut diviser par $\|x\|^2$ :
$$ \lambda^2 = 1 $$
Ainsi, $\lambda \in \{-1, 1\}$. $\blacksquare$

---
uuid: "jalon-27-exo-09"
title: "Exercice 09 : Valeurs propres d'une matrice orthogonale"
---
# Exercice 09 : Matrices orthogonales et isométrie

**Difficulté :** ★★☆☆☆

## Énoncé

Montrer qu'une matrice carrée $A \in \mathcal{M}_n(\mathbb{R})$ est orthogonale si et seulement si l'endomorphisme canoniquement associé conserve la norme (c'est une isométrie).

## Démonstration sans ellipse

Soit $f$ l'endomorphisme associé à la matrice $A$ dans la base canonique, qui est orthonormée pour le produit scalaire standard $\langle X, Y \rangle = X^T Y$.
Dire que $A$ est orthogonale signifie que $A^T A = I_n$.
Dire que $f$ conserve la norme signifie que pour tout $X \in \mathbb{R}^n$, $\|AX\| = \|X\|$.

**Sens direct :** Supposons $A^T A = I_n$.
Pour tout $X \in \mathbb{R}^n$, la norme au carré est :
$$ \|AX\|^2 = \langle AX, AX \rangle = (AX)^T (AX) = X^T A^T A X $$
Puisque $A^T A = I_n$, cela devient :
$$ X^T I_n X = X^T X = \|X\|^2 $$
Ainsi, $\|AX\| = \|X\|$, l'endomorphisme conserve la norme.

**Sens réciproque :** Supposons que pour tout $X \in \mathbb{R}^n$, $\|AX\| = \|X\|$.
Alors pour tout $X$, $X^T A^T A X = X^T X$, ce qui s'écrit $X^T (A^T A - I_n) X = 0$.
Posons $M = A^T A - I_n$. La matrice $M$ est symétrique car $M^T = (A^T A - I_n)^T = A^T A - I_n = M$.
La forme quadratique associée à $M$ est nulle : pour tout $X$, $X^T M X = 0$.
Pour une matrice symétrique, si la forme quadratique est identiquement nulle, alors la matrice est nulle (cela se prouve par polarisation : $2 X^T M Y = (X+Y)^T M (X+Y) - X^T M X - Y^T M Y = 0 - 0 - 0 = 0$).
Donc $M = 0$, c'est-à-dire $A^T A = I_n$. La matrice $A$ est orthogonale. $\blacksquare$

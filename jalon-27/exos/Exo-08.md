---
uuid: "jalon-27-exo-08"
title: "Exercice 08 : Matrice de passage entre bases orthonormées"
---
# Exercice 08 : Matrice de passage entre bases orthonormées

**Difficulté :** ★★★★☆

## Énoncé

Montrer que la matrice de passage d'une base orthonormée à une autre base orthonormée est orthogonale.

## Démonstration sans ellipse

Soient $\mathcal{B} = (e_1, \dots, e_n)$ et $\mathcal{B}' = (e'_1, \dots, e'_n)$ deux bases orthonormées.
Soit $P$ la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$. Le coefficient $p_{i,j}$ de $P$ est la coordonnée de $e'_j$ sur $e_i$, c'est-à-dire $p_{i,j} = \langle e'_j, e_i \rangle$.
Calculons le coefficient $(i,j)$ de $P^T P$ :
$$ (P^T P)_{i,j} = \sum_{k=1}^n (P^T)_{i,k} P_{k,j} = \sum_{k=1}^n P_{k,i} P_{k,j} = \sum_{k=1}^n \langle e'_i, e_k \rangle \langle e'_j, e_k \rangle $$
Or, $e'_i = \sum_{k=1}^n \langle e'_i, e_k \rangle e_k$.
Donc $\sum_{k=1}^n \langle e'_i, e_k \rangle \langle e'_j, e_k \rangle = \langle e'_i, e'_j \rangle$.
Puisque $\mathcal{B}'$ est orthonormée, $\langle e'_i, e'_j \rangle = \delta_{i,j}$.
Ainsi, $P^T P = I_n$, la matrice est orthogonale. $\blacksquare$

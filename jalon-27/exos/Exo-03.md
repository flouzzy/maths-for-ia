---
title: "Exercice 3 : Opérateur symétrique et trace"
difficulty: "★★☆☆☆"
---
# Exercice 3 : Opérateur symétrique et trace

## Énoncé
Soit $E$ un espace euclidien et $f \in \mathcal{L}(E)$.
Montrer que $f \circ f^* = 0 \implies f = 0$.
En déduire que si la trace $\text{Tr}(f \circ f^*) = 0$, alors $f = 0$.

## Correction Zéro Ellipse
**Partie 1 : $f \circ f^* = 0 \implies f = 0$**
Supposons que l'endomorphisme composé $f \circ f^*$ soit l'endomorphisme nul.
Cela signifie que $\forall x \in E, (f \circ f^*)(x) = 0_E$.
Soit $x \in E$. Évaluons le produit scalaire de $f^*(x)$ avec lui-même pour relier à la norme :
$\| f^*(x) \|^2 = \langle f^*(x), f^*(x) \rangle$.
Par définition de l'adjoint $f^*$, on peut transférer le premier $f^*$ à gauche vers la droite, où il devient $(f^*)^* = f$ :
$\langle f^*(x), f^*(x) \rangle = \langle x, f(f^*(x)) \rangle = \langle x, (f \circ f^*)(x) \rangle$.
Or par hypothèse, $(f \circ f^*)(x) = 0_E$.
Donc $\langle x, 0_E \rangle = 0$.
Ainsi, $\| f^*(x) \|^2 = 0$.
Par séparation de la norme, cela implique $f^*(x) = 0_E$.
Puisque ceci est vrai pour tout $x \in E$, on en déduit que l'opérateur adjoint $f^*$ est nul.
Or, $f = (f^*)^* = 0^* = 0$. Donc $f$ est l'endomorphisme nul.

**Partie 2 : $\text{Tr}(f \circ f^*) = 0 \implies f = 0$**
L'espace $E$ étant euclidien, il possède une base orthonormée $\mathcal{B} = (e_1, e_2, \dots, e_n)$.
Soit $A = \text{Mat}_{\mathcal{B}}(f)$. Puisque la base est orthonormée, la matrice de $f^*$ est $A^T$.
L'endomorphisme $f \circ f^*$ est représenté par la matrice $A A^T$.
Exprimons la trace de $A A^T$ en fonction des coefficients $(a_{i,j})$ de $A$.
Le coefficient $(i, i)$ de $A A^T$ est le produit de la ligne $i$ de $A$ par la colonne $i$ de $A^T$ (qui est la ligne $i$ de $A$ transposée).
Donc $(A A^T)_{i,i} = \sum_{j=1}^n a_{i,j} a_{i,j} = \sum_{j=1}^n a_{i,j}^2$.
La trace de $A A^T$ est la somme de ses éléments diagonaux :
$\text{Tr}(A A^T) = \sum_{i=1}^n \sum_{j=1}^n a_{i,j}^2$.
C'est la somme des carrés de tous les coefficients de la matrice $A$.
Si $\text{Tr}(f \circ f^*) = 0$, alors $\sum_{i,j} a_{i,j}^2 = 0$.
Puisque c'est une somme de termes positifs ou nuls ($a_{i,j}^2 \geq 0$), la seule possibilité pour que la somme soit nulle est que chaque terme soit nul.
Donc $\forall i, j, a_{i,j} = 0$.
La matrice $A$ est donc la matrice nulle, ce qui implique que l'endomorphisme $f$ est nul.

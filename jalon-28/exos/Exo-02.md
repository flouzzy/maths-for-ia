---
title: "Exercice 2 : Inversion d'une matrice via Cayley-Hamilton"
difficulty: 2
---

# Exercice 2 : Inversion d'une matrice via Cayley-Hamilton (★★☆☆☆)

## Énoncé

Soit $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
1. Calculer le polynôme caractéristique $\chi_A(X)$.
2. En utilisant le théorème de Cayley-Hamilton, montrer que $A$ est inversible et exprimer $A^{-1}$ sous forme d'un polynôme en $A$.
3. Calculer explicitement $A^{-1}$ avec cette formule.

## Solution Rigoureuse

### 1. Calcul du polynôme caractéristique
Par définition, $\chi_A(X) = \det(X I_2 - A)$.
$$\chi_A(X) = \begin{vmatrix} X - 1 & -2 \\ -3 & X - 4 \end{vmatrix} = (X - 1)(X - 4) - (-2)(-3) = (X^2 - 4X - X + 4) - 6 = X^2 - 5X - 2$$

### 2. Expression de $A^{-1}$
D'après le théorème de Cayley-Hamilton, $\chi_A(A) = 0_2$.
Donc, on a l'égalité matricielle :
$$A^2 - 5A - 2I_2 = 0_2$$
Isolons $2I_2$ :
$$2I_2 = A^2 - 5A$$
Factorisons par $A$ à gauche et à droite (rappelons que $A$ commute avec $A$ et avec $5I_2$) :
$$2I_2 = A(A - 5I_2) = (A - 5I_2)A$$
Divisons par 2 :
$$I_2 = A \left( \frac{1}{2}(A - 5I_2) \right) = \left( \frac{1}{2}(A - 5I_2) \right) A$$
Par définition de l'inverse, cela prouve que $A$ est inversible (son inverse à droite et à gauche coïncident) et que :
$$A^{-1} = \frac{1}{2}(A - 5I_2)$$

### 3. Calcul explicite
Appliquons la formule :
$$A^{-1} = \frac{1}{2} \left[ \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} - \begin{pmatrix} 5 & 0 \\ 0 & 5 \end{pmatrix} \right] = \frac{1}{2} \begin{pmatrix} 1 - 5 & 2 - 0 \\ 3 - 0 & 4 - 5 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} -4 & 2 \\ 3 & -1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}$$
*(Vérification explicite et systématique : $\det(A) = 4 - 6 = -2 \neq 0$. La formule de l'inverse en dimension 2 donne $\frac{1}{-2} \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}$, ce qui correspond exactement).*

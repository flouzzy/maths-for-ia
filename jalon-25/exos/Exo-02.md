---
title: "Exercice 2 : Forme bilinéaire symétrique et matrice associée"
difficulty: 1
---

## Énoncé
Soit $E = \mathbb{R}^2$. On définit l'application $B : E \times E \to \mathbb{R}$ par :
$B(X, Y) = 2x_1y_1 - x_1y_2 - x_2y_1 + 3x_2y_2$, où $X = (x_1, x_2)$ et $Y = (y_1, y_2)$.
1. Montrer que $B$ est une forme bilinéaire symétrique.
2. Écrire la matrice $A$ associée à $B$ dans la base canonique de $\mathbb{R}^2$.
3. $B$ est-elle un produit scalaire ?

## Correction Détaillée
1. **Symétrie :**
   Soient $X = (x_1, x_2)$ et $Y = (y_1, y_2)$ dans $\mathbb{R}^2$.
   $B(Y, X) = 2y_1x_1 - y_1x_2 - y_2x_1 + 3y_2x_2$
   Par commutativité de la multiplication dans $\mathbb{R}$ :
   $B(Y, X) = 2x_1y_1 - x_2y_1 - x_1y_2 + 3x_2y_2 = B(X, Y)$.
   Donc $B$ est symétrique.
   **Bilinéarité :**
   Puisque $B$ est symétrique, il suffit de prouver la linéarité par rapport à la première variable.
   Soient $X = (x_1, x_2)$, $X' = (x'_1, x'_2)$, $Y = (y_1, y_2)$ et $\lambda \in \mathbb{R}$.
   $B(\lambda X + X', Y) = 2(\lambda x_1 + x'_1)y_1 - (\lambda x_1 + x'_1)y_2 - (\lambda x_2 + x'_2)y_1 + 3(\lambda x_2 + x'_2)y_2$
   $B(\lambda X + X', Y) = \lambda(2x_1y_1 - x_1y_2 - x_2y_1 + 3x_2y_2) + (2x'_1y_1 - x'_1y_2 - x'_2y_1 + 3x'_2y_2)$
   $B(\lambda X + X', Y) = \lambda B(X, Y) + B(X', Y)$.
   $B$ est bien une forme bilinéaire.

2. **Matrice associée :**
   Soit $\mathcal{B} = (e_1, e_2)$ la base canonique, avec $e_1 = (1, 0)$ et $e_2 = (0, 1)$.
   La matrice $A = (a_{i,j})$ est définie par $a_{i,j} = B(e_i, e_j)$.
   $B(e_1, e_1) = 2(1)(1) - 0 - 0 + 0 = 2$
   $B(e_1, e_2) = 0 - 1(1) - 0 + 0 = -1$
   $B(e_2, e_1) = 0 - 0 - 1(1) + 0 = -1$ (cohérent avec la symétrie)
   $B(e_2, e_2) = 0 - 0 - 0 + 3(1)(1) = 3$
   Ainsi, $A = \begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}$.
   On vérifie bien que $B(X, Y) = X^T A Y$.

3. **Caractère défini positif (Produit scalaire) :**
   $B$ est un produit scalaire si elle est définie positive. Evaluons $B(X, X)$ pour tout $X \in \mathbb{R}^2$ :
   $B(X, X) = 2x_1^2 - 2x_1x_2 + 3x_2^2$
   Utilisons la méthode de Gauss (complétion du carré) :
   $B(X, X) = 2(x_1^2 - x_1x_2) + 3x_2^2$
   $B(X, X) = 2( (x_1 - \frac{1}{2}x_2)^2 - \frac{1}{4}x_2^2 ) + 3x_2^2$
   $B(X, X) = 2(x_1 - \frac{1}{2}x_2)^2 - \frac{1}{2}x_2^2 + 3x_2^2$
   $B(X, X) = 2(x_1 - \frac{1}{2}x_2)^2 + \frac{5}{2}x_2^2$
   - **Positivité :** C'est une somme de carrés pondérés par des coefficients strictement positifs (2 et 5/2), donc $B(X, X) \ge 0$ pour tout $X$.
   - **Caractère défini :** Si $B(X, X) = 0$, alors chaque terme de la somme doit être nul car ils sont tous positifs ou nuls.
     Donc $2(x_1 - \frac{1}{2}x_2)^2 = 0$ et $\frac{5}{2}x_2^2 = 0$.
     La deuxième équation donne $x_2 = 0$.
     En remplaçant dans la première, on obtient $2(x_1 - 0)^2 = 0 \implies x_1 = 0$.
     Ainsi, $X = (0, 0) = 0_{\mathbb{R}^2}$.
   $B$ est définie positive. C'est donc un produit scalaire sur $\mathbb{R}^2$.

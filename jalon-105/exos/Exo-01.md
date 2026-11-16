# Exercice 1 : Calcul direct en dimension finie $\bigstar\star\star\star\star$
## Énoncé
Soit $H = \mathbb{R}^2$ muni du produit scalaire usuel. On définit l'opérateur linéaire $T : H \to H$ par sa matrice $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ dans la base canonique.
1. Calculer explicitement l'opérateur adjoint $T^*$ par définition, en évaluant $\langle Tx, y \rangle$.
2. Vérifier que la matrice de $T^*$ dans la base canonique correspond bien à la transposée de la matrice $A$.

## Correction
1. Soient $x = (x_1, x_2)$ et $y = (y_1, y_2)$ dans $\mathbb{R}^2$.
On a $Tx = (x_1 + 2x_2, 3x_1 + 4x_2)$.
Le produit scalaire donne :
$$ \langle Tx, y \rangle = (x_1 + 2x_2)y_1 + (3x_1 + 4x_2)y_2 $$
$$ = x_1 y_1 + 2 x_2 y_1 + 3 x_1 y_2 + 4 x_2 y_2 $$
Pour identifier $T^*y$, on doit réorganiser l'expression pour mettre $x_1$ et $x_2$ en facteur, afin d'obtenir la forme $x_1 (T^*y)_1 + x_2 (T^*y)_2$ :
$$ = x_1 (y_1 + 3y_2) + x_2 (2y_1 + 4y_2) $$
$$ = \langle x, T^*y \rangle $$
On déduit donc que l'opérateur adjoint $T^*$ agit sur $y$ de la manière suivante :
$$ T^*y = (y_1 + 3y_2, 2y_1 + 4y_2) $$

2. Exprimons $T^*y$ sous forme matricielle. En posant $y$ comme vecteur colonne :
$$ T^*y = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} $$
La matrice de $T^*$ dans la base canonique est donc $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
On constate que cette matrice est exactement $A^T$, la transposée de la matrice $A$.

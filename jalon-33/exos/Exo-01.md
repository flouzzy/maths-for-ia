# Exercice 1 : Forme polaire et matrice

## Énoncé
Soit la forme quadratique $q$ définie sur $\mathbb{R}^3$ par :
$$ q(x,y,z) = x^2 + 3y^2 + 2z^2 - 4xy + 2xz - 6yz $$
1. Déterminer la forme polaire $b$ associée à $q$.
2. Écrire la matrice $A$ de $q$ dans la base canonique de $\mathbb{R}^3$.

## Correction Détaillée (Zéro Ellipse)

### 1. Forme polaire
Par définition, la forme polaire $b$ est l'unique forme bilinéaire symétrique telle que $q(X) = b(X,X)$.
Soient $X = (x,y,z)$ et $X' = (x',y',z')$.
Les termes carrés $x^2$, $y^2$, $z^2$ donnent respectivement $xx'$, $yy'$, $zz'$.
Les termes croisés, par exemple $-4xy$, doivent être partagés de manière symétrique pour que $b(X, X') = b(X', X)$. Ainsi, $-4xy$ correspond à $-2xy' - 2x'y$.
On applique cette méthode à tous les termes croisés :
- $2xz$ devient $xz' + x'z$.
- $-6yz$ devient $-3yz' - 3y'z$.
Ainsi, la forme polaire $b$ s'écrit :
$$ b(X, X') = xx' + 3yy' + 2zz' - 2xy' - 2x'y + xz' + x'z - 3yz' - 3y'z $$

### 2. Matrice de la forme quadratique
La matrice $A = (a_{ij})$ de la forme quadratique dans une base est définie par $a_{ij} = b(e_i, e_j)$, où $(e_1, e_2, e_3)$ est la base canonique.
Pour une matrice symétrique de forme quadratique, les éléments de la diagonale sont les coefficients des termes carrés :
- $a_{11} = 1$ (coefficient de $x^2$)
- $a_{22} = 3$ (coefficient de $y^2$)
- $a_{33} = 2$ (coefficient de $z^2$)
Les éléments hors diagonale s'obtiennent en divisant par 2 les coefficients des termes croisés :
- $a_{12} = a_{21} = -4 / 2 = -2$ (pour $xy$)
- $a_{13} = a_{31} = 2 / 2 = 1$ (pour $xz$)
- $a_{23} = a_{32} = -6 / 2 = -3$ (pour $yz$)

La matrice $A$ s'écrit donc :
$$ A = \begin{pmatrix} 1 & -2 & 1 \\ -2 & 3 & -3 \\ 1 & -3 & 2 \end{pmatrix} $$
$\blacksquare$

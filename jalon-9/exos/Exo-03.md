# Exercice 3 : Produit Matriciel et Propriété de Transposition
**Difficulté :** ★★☆☆☆

## Énoncé
Soient $\mathbb{R}$ le corps des nombres réels, et $\mathcal{M}_{m,n}(\mathbb{R})$ l'espace vectoriel des matrices à $m$ lignes et $n$ colonnes à coefficients dans $\mathbb{R}$.
Considérons les matrices $A \in \mathcal{M}_{2,3}(\mathbb{R})$ et $B \in \mathcal{M}_{3,2}(\mathbb{R})$ définies par :
$$ A = \begin{pmatrix} 1 & 2 & 0 \\ -1 & 0 & 3 \end{pmatrix} $$
$$ B = \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ 3 & 0 \end{pmatrix} $$
1.  Calculer le produit matriciel $C = AB$. Préciser les dimensions de la matrice $C$.
2.  Déterminer les matrices transposées $A^T$ et $B^T$. Préciser leurs dimensions respectives.
3.  Calculer le produit matriciel $D = B^T A^T$. Préciser les dimensions de la matrice $D$.
4.  Vérifier que la matrice $D$ est égale à la matrice transposée de $C$, c'est-à-dire $D = C^T$.

## Correction Détaillée

### 1. Calcul du produit matriciel $C = AB$

La matrice $A$ est de dimension $2 \times 3$ et la matrice $B$ est de dimension $3 \times 2$. Le nombre de colonnes de $A$ (qui est 3) est égal au nombre de lignes de $B$ (qui est 3), donc le produit $AB$ est bien défini. La matrice résultante $C = AB$ sera de dimension $2 \times 2$.

Soit $C = (C_{ij})$ où $C_{ij} = \sum_{k=1}^{3} A_{ik} B_{kj}$.

Calcul des éléments de $C$:
*   $C_{11} = A_{11}B_{11} + A_{12}B_{21} + A_{13}B_{31}$
    $C_{11} = (1)(2) + (2)(0) + (0)(3)$
    $C_{11} = 2 + 0 + 0$
    $C_{11} = 2$

*   $C_{12} = A_{11}B_{12} + A_{12}B_{22} + A_{13}B_{32}$
    $C_{12} = (1)(1) + (2)(-1) + (0)(0)$
    $C_{12} = 1 - 2 + 0$
    $C_{12} = -1$

*   $C_{21} = A_{21}B_{11} + A_{22}B_{21} + A_{23}B_{31}$
    $C_{21} = (-1)(2) + (0)(0) + (3)(3)$
    $C_{21} = -2 + 0 + 9$
    $C_{21} = 7$

*   $C_{22} = A_{21}B_{12} + A_{22}B_{22} + A_{23}B_{32}$
    $C_{22} = (-1)(1) + (0)(-1) + (3)(0)$
    $C_{22} = -1 + 0 + 0$
    $C_{22} = -1$

Ainsi, la matrice $C$ est :
$$ C = \begin{pmatrix} 2 & -1 \\ 7 & -1 \end{pmatrix} $$
La matrice $C$ est de dimension $2 \times 2$.

### 2. Détermination des matrices transposées $A^T$ et $B^T$

La transposée d'une matrice $M = (M_{ij})$ est la matrice $M^T = (M_{ji})$. Les lignes de $M$ deviennent les colonnes de $M^T$, et les colonnes de $M$ deviennent les lignes de $M^T$.

Pour la matrice $A \in \mathcal{M}_{2,3}(\mathbb{R})$ :
$$ A = \begin{pmatrix} 1 & 2 & 0 \\ -1 & 0 & 3 \end{pmatrix} $$
Sa transposée $A^T$ est de dimension $3 \times 2$:
$$ A^T = \begin{pmatrix} 1 & -1 \\ 2 & 0 \\ 0 & 3 \end{pmatrix} $$

Pour la matrice $B \in \mathcal{M}_{3,2}(\mathbb{R})$ :
$$ B = \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ 3 & 0 \end{pmatrix} $$
Sa transposée $B^T$ est de dimension $2 \times 3$:
$$ B^T = \begin{pmatrix} 2 & 0 & 3 \\ 1 & -1 & 0 \end{pmatrix} $$

### 3. Calcul du produit matriciel $D = B^T A^T$

La matrice $B^T$ est de dimension $2 \times 3$ et la matrice $A^T$ est de dimension $3 \times 2$. Le nombre de colonnes de $B^T$ (qui est 3) est égal au nombre de lignes de $A^T$ (qui est 3), donc le produit $B^T A^T$ est bien défini. La matrice résultante $D = B^T A^T$ sera de dimension $2 \times 2$.

Soit $D = (D_{ij})$ où $D_{ij} = \sum_{k=1}^{3} (B^T)_{ik} (A^T)_{kj}$.

Calcul des éléments de $D$:
*   $D_{11} = (B^T)_{11}(A^T)_{11} + (B^T)_{12}(A^T)_{21} + (B^T)_{13}(A^T)_{31}$
    $D_{11} = (2)(1) + (0)(2) + (3)(0)$
    $D_{11} = 2 + 0 + 0$
    $D_{11} = 2$

*   $D_{12} = (B^T)_{11}(A^T)_{12} + (B^T)_{12}(A^T)_{22} + (B^T)_{13}(A^T)_{32}$
    $D_{12} = (2)(-1) + (0)(0) + (3)(3)$
    $D_{12} = -2 + 0 + 9$
    $D_{12} = 7$

*   $D_{21} = (B^T)_{21}(A^T)_{11} + (B^T)_{22}(A^T)_{21} + (B^T)_{23}(A^T)_{31}$
    $D_{21} = (1)(1) + (-1)(2) + (0)(0)$
    $D_{21} = 1 - 2 + 0$
    $D_{21} = -1$

*   $D_{22} = (B^T)_{21}(A^T)_{12} + (B^T)_{22}(A^T)_{22} + (B^T)_{23}(A^T)_{32}$
    $D_{22} = (1)(-1) + (-1)(0) + (0)(3)$
    $D_{22} = -1 + 0 + 0$
    $D_{22} = -1$

Ainsi, la matrice $D$ est :
$$ D = \begin{pmatrix} 2 & 7 \\ -1 & -1 \end{pmatrix} $$
La matrice $D$ est de dimension $2 \times 2$.

### 4. Vérification de l'égalité $D = C^T$

Nous avons calculé la matrice $C$:
$$ C = \begin{pmatrix} 2 & -1 \\ 7 & -1 \end{pmatrix} $$
La transposée de $C$, notée $C^T$, est obtenue en échangeant ses lignes et ses colonnes :
$$ C^T = \begin{pmatrix} 2 & 7 \\ -1 & -1 \end{pmatrix} $$

En comparant la matrice $D$ obtenue à la question 3 et la matrice $C^T$ que nous venons de calculer :
$$ D = \begin{pmatrix} 2 & 7 \\ -1 & -1 \end{pmatrix} $$
$$ C^T = \begin{pmatrix} 2 & 7 \\ -1 & -1 \end{pmatrix} $$
Nous constatons que $D_{ij} = (C^T)_{ij}$ pour tous $i,j \in \{1,2\}$.

Par conséquent, nous avons bien vérifié que $D = C^T$, ce qui illustre la propriété générale $(AB)^T = B^T A^T$.

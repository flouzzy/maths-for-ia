# Exercice 4 - Difficulté ★★★☆☆

## Énoncé
Soit la matrice $C \in \mathcal{M}_3(\mathbb{R})$ définie par :
$$C = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$$
Sans calculer directement le polynôme caractéristique complet avec la règle de Sarrus, trouver une racine évidente, factoriser, puis trouver la matrice de passage $P$.

## Solution Complète (Zéro Ellipse)

**Étape 1 : Racine évidente du polynôme caractéristique**
Notons que la somme des colonnes de $C$ donne le vecteur nul.
$\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} + \begin{pmatrix} -1 \\ 2 \\ -1 \end{pmatrix} + \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$
Cela signifie que $C \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = 0 \cdot \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$.
Ainsi, $0$ est une valeur propre de $C$ et le vecteur $v_1 = (1, 1, 1)^T$ est un vecteur propre associé.

**Étape 2 : Calcul complet de $\chi_C(X)$**
On a $\chi_C(X) = \det(X I_3 - C)$.
$$\chi_C(X) = \det\begin{pmatrix} X-1 & 1 & 0 \\ 1 & X-2 & 1 \\ 0 & 1 & X-1 \end{pmatrix}$$
Comme on sait que $0$ est racine, $\chi_C(X)$ est divisible par $X$. Développons par rapport à la première colonne :
$$\chi_C(X) = (X-1) \det\begin{pmatrix} X-2 & 1 \\ 1 & X-1 \end{pmatrix} - 1 \det\begin{pmatrix} 1 & 0 \\ 1 & X-1 \end{pmatrix} + 0$$
$$\chi_C(X) = (X-1) [ (X-2)(X-1) - 1 ] - 1 [ 1(X-1) - 0 ]$$
$$\chi_C(X) = (X-1)[(X^2 - 3X + 2 - 1) - 1]$$
$$\chi_C(X) = (X-1)[X^2 - 3X] = X(X-1)(X-3)$$
Les valeurs propres sont simples : $\text{Sp}(C) = \{0, 1, 3\}$. La matrice est diagonalisable.

**Étape 3 : Calcul des autres sous-espaces propres**
- Pour $\lambda = 1$ : on cherche $u = (x,y,z)^T$ tel que $(C-I)u = 0$.
$\begin{pmatrix} 0 & -1 & 0 \\ -1 & 1 & -1 \\ 0 & -1 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \implies y = 0 \text{ et } -x - z = 0 \implies z = -x$.
$v_2 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$.

- Pour $\lambda = 3$ : on cherche $u = (x,y,z)^T$ tel que $(C-3I)u = 0$.
$\begin{pmatrix} -2 & -1 & 0 \\ -1 & -1 & -1 \\ 0 & -1 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \implies -2x = y \text{ et } -2z = y \implies x = z$.
Si $x=1$, alors $z=1$ et $y=-2$.
$v_3 = \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}$.

**Étape 4 : Matrice de passage**
La matrice de passage, dont les colonnes sont les vecteurs propres, est :
$$P = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & -2 \\ 1 & -1 & 1 \end{pmatrix}$$
On a alors $C = P \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix} P^{-1}$.

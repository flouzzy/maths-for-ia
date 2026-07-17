# Exercice 6 - Difficulté ★★★★☆

## Énoncé
Soit la matrice $A = \begin{pmatrix} 5 & -4 \\ 2 & -1 \end{pmatrix}$.
Calculer $A^n$ pour tout $n \in \mathbb{N}$ à l'aide de sa diagonalisation.

## Solution Complète (Zéro Ellipse)

**Étape 1 : Éléments propres**
$\chi_A(X) = \det\begin{pmatrix} X-5 & 4 \\ -2 & X+1 \end{pmatrix} = (X-5)(X+1) - (-8) = X^2 - 4X - 5 + 8 = X^2 - 4X + 3$.
Les racines de $X^2 - 4X + 3 = 0$ sont $1$ et $3$. (Car $\Delta = 16 - 12 = 4$).
Valeurs propres : $\lambda_1 = 1$, $\lambda_2 = 3$. La matrice est diagonalisable.

- Vecteur propre pour $\lambda_1 = 1$ : $(A - I)u = 0 \implies \begin{pmatrix} 4 & -4 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0 \implies x = y$. $v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
- Vecteur propre pour $\lambda_2 = 3$ : $(A - 3I)u = 0 \implies \begin{pmatrix} 2 & -4 \\ 2 & -4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = 0 \implies x = 2y$. $v_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

**Étape 2 : Matrices de passage**
$P = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$.
Le déterminant de $P$ est $\det(P) = 1(1) - 2(1) = -1$.
L'inverse est $P^{-1} = \frac{1}{-1} \begin{pmatrix} 1 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$.
La matrice diagonale est $D = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$.
On a bien $A = P D P^{-1}$.

**Étape 3 : Calcul de $A^n$**
On sait par récurrence que $A^n = P D^n P^{-1}$.
$$D^n = \begin{pmatrix} 1^n & 0 \\ 0 & 3^n \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 3^n \end{pmatrix}$$
On effectue le produit matriciel :
$$A^n = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 3^n \end{pmatrix} \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$$
$$A^n = \begin{pmatrix} 1 & 2 \cdot 3^n \\ 1 & 3^n \end{pmatrix} \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$$
$$A^n = \begin{pmatrix} -1 + 2 \cdot 3^n & 2 - 2 \cdot 3^n \\ -1 + 3^n & 2 - 3^n \end{pmatrix}$$

Cette expression est valable pour tout $n \in \mathbb{N}$, donnant un accès instantané à n'importe quelle puissance de l'opérateur sans itération algorithmique coûteuse.

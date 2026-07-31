# Exercice 1 - Difficulté \quad $\bigstar$$\star$$\star$$\star$$\star$

## Énoncé
Soit la matrice $A$ définie dans $\mathcal{M}_2(\mathbb{R})$ par :
$$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$
Déterminer le polynôme caractéristique de $A$, ses valeurs propres, et en déduire si elle est diagonalisable.

## Solution Complète

**Étape 1 : Calcul du polynôme caractéristique**
Par définition, $\chi_A(X) = \det(X I_2 - A)$.
$$\chi_A(X) = \det\begin{pmatrix} X - 4 & -1 \\ -2 & X - 3 \end{pmatrix}$$
$$\chi_A(X) = (X-4)(X-3) - (-1)(-2)$$
$$\chi_A(X) = X^2 - 7X + 12 - 2 = X^2 - 7X + 10$$

**Étape 2 : Détermination des valeurs propres**
Cherchons les racines de $\chi_A(X) = 0$.
Le discriminant est $\Delta = (-7)^2 - 4 \times 1 \times 10 = 49 - 40 = 9$.
Les racines sont :
$$\lambda_1 = \frac{7 - 3}{2} = 2 \quad \text{et} \quad \lambda_2 = \frac{7 + 3}{2} = 5$$
Les valeurs propres sont donc $\text{Sp}(A) = \{2, 5\}$.

**Étape 3 : Conclusion sur la diagonalisabilité**
La matrice $A$ est de taille $2 \times 2$. Son polynôme caractéristique est scindé et possède exactement $2$ racines distinctes (les valeurs propres sont simples, de multiplicité algébrique $1$).
D'après le cours, un endomorphisme en dimension $n$ admettant $n$ valeurs propres distinctes est diagonalisable. Donc $A$ est diagonalisable.

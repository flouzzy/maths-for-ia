# Exercice 1 : Trigonalisation en dimension 2 (★)

Soit $A = \begin{pmatrix} 1 & 1 \\ -1 & 3 \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
Montrer que $A$ est trigonalisable mais non diagonalisable. Trouver une matrice $P$ inversible et une matrice $T$ triangulaire supérieure telles que $A = P T P^{-1}$.

### Solution :

**Étape 1 : Calcul du polynôme caractéristique**
$$ \chi_A(X) = \det(XI_2 - A) = \begin{vmatrix} X-1 & -1 \\ 1 & X-3 \end{vmatrix} = (X-1)(X-3) - (-1)(1) = X^2 - 4X + 3 + 1 = X^2 - 4X + 4 = (X-2)^2 $$
Le polynôme caractéristique est $\chi_A(X) = (X-2)^2$.
Il est scindé sur $\mathbb{R}$. Par le théorème de trigonalisation, $A$ est trigonalisable.

**Étape 2 : Recherche des sous-espaces propres**
L'unique valeur propre est $\lambda = 2$.
Déterminons le sous-espace propre $E_2 = \ker(A - 2I_2)$.
Soit $U = \begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2$.
$$ (A - 2I_2)U = 0 \iff \begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \iff -x + y = 0 \iff x = y $$
Donc $E_2 = \text{Vect}\left(\begin{pmatrix} 1 \\ 1 \end{pmatrix}\right)$.
La dimension du sous-espace propre est $1$.
Puisque la multiplicité algébrique de la valeur propre $\lambda=2$ est $2$ et que la dimension du sous-espace propre associé est $1 < 2$, la matrice $A$ n'est pas diagonalisable.

**Étape 3 : Construction de la base de trigonalisation**
Soit $V_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. Complétons ce vecteur pour former une base de $\mathbb{R}^2$.
Choisissons $V_2 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$. (La famille $(V_1, V_2)$ est clairement libre car les vecteurs ne sont pas colinéaires).
Soit $P$ la matrice de passage de la base canonique à la base $\mathcal{B}' = (V_1, V_2)$ :
$$ P = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} $$
On calcule l'inverse $P^{-1}$. Le déterminant est $\det(P) = 1(0) - 1(1) = -1$.
$$ P^{-1} = \frac{1}{-1} \begin{pmatrix} 0 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix} $$

**Étape 4 : Calcul de la matrice trigonalisée $T$**
On cherche $T = P^{-1} A P$.
$$ AP = \begin{pmatrix} 1 & 1 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 2 & -1 \end{pmatrix} $$
$$ T = P^{-1} (AP) = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 0 & 2 \end{pmatrix} $$
La matrice $T = \begin{pmatrix} 2 & -1 \\ 0 & 2 \end{pmatrix}$ est bien triangulaire supérieure. On a l'égalité $A = P T P^{-1}$.

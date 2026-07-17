# Exercice 2 - Difficulté ★★☆☆☆

## Énoncé
On reprend la matrice $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ de l'exercice précédent, dont le spectre est $\text{Sp}(A) = \{2, 5\}$.
Déterminer une base pour chacun des sous-espaces propres $E_2(A)$ et $E_5(A)$.

## Solution Complète (Zéro Ellipse)

**Étape 1 : Sous-espace propre associé à $\lambda = 2$**
Par définition, $E_2(A) = \ker(A - 2I_2)$.
Soit $U = \begin{pmatrix} x \\ y \end{pmatrix} \in \ker(A - 2I_2)$.
$$(A - 2I_2)U = 0 \iff \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
Ce qui donne l'unique équation (les deux lignes sont colinéaires) :
$$2x + y = 0 \iff y = -2x$$
Ainsi, les vecteurs de $E_2(A)$ s'écrivent $\begin{pmatrix} x \\ -2x \end{pmatrix} = x \begin{pmatrix} 1 \\ -2 \end{pmatrix}$.
Une base de $E_2(A)$ est donc formée par le vecteur $v_1 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$. La dimension de $E_2(A)$ est $1$.

**Étape 2 : Sous-espace propre associé à $\lambda = 5$**
Par définition, $E_5(A) = \ker(A - 5I_2)$.
Soit $U = \begin{pmatrix} x \\ y \end{pmatrix} \in \ker(A - 5I_2)$.
$$(A - 5I_2)U = 0 \iff \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
Ce qui donne l'équation (la seconde ligne est $-2$ fois la première) :
$$-x + y = 0 \iff y = x$$
Ainsi, les vecteurs de $E_5(A)$ s'écrivent $\begin{pmatrix} x \\ x \end{pmatrix} = x \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Une base de $E_5(A)$ est donc formée par le vecteur $v_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. La dimension de $E_5(A)$ est $1$.

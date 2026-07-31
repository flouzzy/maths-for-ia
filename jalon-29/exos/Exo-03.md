# Exercice 3 - Difficulté \quad $\bigstar$$\bigstar$$\star$$\star$$\star$

## Énoncé
Soit la matrice $B$ définie par :
$$B = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$
Déterminer si la matrice $B$ est diagonalisable en justifiant rigoureusement chaque étape.

## Solution Complète

**Étape 1 : Calcul du polynôme caractéristique**
Par définition, $\chi_B(X) = \det(X I_3 - B)$.
$$\chi_B(X) = \det\begin{pmatrix} X - 2 & -1 & 0 \\ 0 & X - 2 & 0 \\ 0 & 0 & X - 3 \end{pmatrix}$$
La matrice est triangulaire supérieure, le déterminant est donc égal au produit de ses éléments diagonaux :
$$\chi_B(X) = (X-2)^2(X-3)$$

**Étape 2 : Spectres et multiplicités algébriques**
Le polynôme caractéristique est scindé. Les racines sont :
- $\lambda_1 = 2$, avec une multiplicité algébrique $m(2) = 2$.
- $\lambda_2 = 3$, avec une multiplicité algébrique $m(3) = 1$.
Le spectre est $\text{Sp}(B) = \{2, 3\}$.

**Étape 3 : Dimension des sous-espaces propres**
Pour qu'une matrice soit diagonalisable, il faut que la dimension de chaque sous-espace propre soit égale à la multiplicité algébrique de la valeur propre associée.
Pour la valeur propre simple $\lambda_2 = 3$, on sait que $\dim(E_3(B)) = 1$ car $1 \leq \dim(E_3(B)) \leq m(3) = 1$.
Il faut donc vérifier la dimension de $E_2(B) = \ker(B - 2I_3)$.
Soit $U = \begin{pmatrix} x \\ y \\ z \end{pmatrix} \in \ker(B - 2I_3)$.
$$(B - 2I_3)U = 0 \iff \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
Ce qui équivaut au système :
$$\begin{cases} y = 0 \\ z = 0 \end{cases}$$
La variable $x$ est libre. Les vecteurs de $E_2(B)$ s'écrivent donc $U = \begin{pmatrix} x \\ 0 \\ 0 \end{pmatrix} = x \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.
Ainsi, $E_2(B) = \text{Vect}\left(\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\right)$.
La dimension du sous-espace propre associé à la valeur propre $2$ est $\dim(E_2(B)) = 1$.

**Étape 4 : Conclusion**
Puisque $\dim(E_2(B)) = 1 \neq 2 = m(2)$, la multiplicité géométrique est strictement inférieure à la multiplicité algébrique.
Par conséquent, la matrice $B$ **n'est pas diagonalisable**.

# Construction explicite de la base de Jordan (⭐⭐⭐⭐⭐)

## Énoncé
Considérons l'endomorphisme $u$ de $\mathbb{R}^3$ dont la matrice dans la base canonique est :
$$A = \begin{pmatrix} 2 & -1 & 2 \\ 5 & -3 & 3 \\ -1 & 0 & -2 \end{pmatrix}$$
1. Calculer le polynôme caractéristique de $A$ et vérifier qu'il s'écrit $\chi_A(X) = (X+1)^3$.
2. En déduire que la matrice $N = A + I_3$ est nilpotente.
3. Déterminer l'indice de nilpotence $p$ de $N$ et la suite des noyaux $\ker(N^k)$.
4. Construire explicitement une base de Jordan $\mathcal{B}$ pour $N$, et donner la matrice de passage $P$.

## Corrigé Détaillé

### 1. Polynôme caractéristique
Calculons $\chi_A(X) = \det(X I_3 - A)$.
$$\chi_A(X) = \det \begin{pmatrix} X - 2 & 1 & -2 \\ -5 & X + 3 & -3 \\ 1 & 0 & X + 2 \end{pmatrix}$$
Développons par rapport à la dernière ligne :
$\chi_A(X) = 1 \cdot \det \begin{pmatrix} 1 & -2 \\ X+3 & -3 \end{pmatrix} - 0 + (X+2) \cdot \det \begin{pmatrix} X-2 & 1 \\ -5 & X+3 \end{pmatrix}$
$= (-3 - (-2)(X+3)) + (X+2)((X-2)(X+3) - (-5))$
$= (-3 + 2X + 6) + (X+2)(X^2 + X - 6 + 5)$
$= (2X + 3) + (X+2)(X^2 + X - 1)$
$= 2X + 3 + (X^3 + X^2 - X + 2X^2 + 2X - 2)$
$= X^3 + 3X^2 + 3X + 1$
On reconnaît l'identité remarquable du cube : $\chi_A(X) = (X + 1)^3$.

### 2. Nilpotence de $N$
Posons $N = A - (-1)I_3 = A + I_3$.
L'unique valeur propre de $A$ est $-1$.
La matrice $N$ a pour polynôme caractéristique $\chi_N(X) = \chi_A(X - 1) = ((X-1)+1)^3 = X^3$.
D'après le théorème de Cayley-Hamilton, $N^3 = 0$. $N$ est donc nilpotente.

### 3. Indice de nilpotence et noyaux
Calculons $N$ :
$$N = A + I_3 = \begin{pmatrix} 3 & -1 & 2 \\ 5 & -2 & 3 \\ -1 & 0 & -1 \end{pmatrix}$$
Calculons $N^2$ :
$$N^2 = \begin{pmatrix} 3 & -1 & 2 \\ 5 & -2 & 3 \\ -1 & 0 & -1 \end{pmatrix} \begin{pmatrix} 3 & -1 & 2 \\ 5 & -2 & 3 \\ -1 & 0 & -1 \end{pmatrix} = \begin{pmatrix} 2 & -1 & 1 \\ 2 & -1 & 1 \\ -2 & 1 & -1 \end{pmatrix}$$
On voit que $N^2 \neq 0_3$. Comme on sait que $N^3 = 0_3$, l'indice de nilpotence de $N$ est $p=3$.
Les dimensions des noyaux successifs sont $d_1 = 1$, $d_2 = 2$, $d_3 = 3$ (car la suite est strictement croissante).

### 4. Construction de la base de Jordan
L'indice de nilpotence étant $p=3$ en dimension 3, il n'y a qu'un seul bloc de Jordan $J_3(0)$ pour $N$.
Nous devons trouver un vecteur $x$ tel que $N^2 x \neq 0$.
Au vu de $N^2$, choisissons le vecteur de la base canonique $e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.
On a $N^2 e_1 = \text{première colonne de } N^2 = \begin{pmatrix} 2 \\ 2 \\ -2 \end{pmatrix}$. Il est bien non nul.
Construisons la chaîne de Jordan ascendante (pour avoir des 1 sur la sur-diagonale) :
- $v_1 = N^2 e_1 = \begin{pmatrix} 2 \\ 2 \\ -2 \end{pmatrix}$
- $v_2 = N e_1 = \text{première colonne de } N = \begin{pmatrix} 3 \\ 5 \\ -1 \end{pmatrix}$
- $v_3 = e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$

Vérifions l'action de $N$ sur cette base $\mathcal{B} = (v_1, v_2, v_3)$ :
- $N(v_1) = N^3 e_1 = 0 = 0 v_1 + 0 v_2 + 0 v_3$
- $N(v_2) = N^2 e_1 = v_1 = 1 v_1 + 0 v_2 + 0 v_3$
- $N(v_3) = N e_1 = v_2 = 0 v_1 + 1 v_2 + 0 v_3$

Dans cette base, la matrice de $N$ est exactement le bloc de Jordan $J_3(0)$.
La matrice de passage de la base canonique vers $\mathcal{B}$ est la concaténation en colonnes :
$$P = \begin{pmatrix} 2 & 3 & 1 \\ 2 & 5 & 0 \\ -2 & -1 & 0 \end{pmatrix}$$
On conclut que $P^{-1} N P = J_3(0)$.
Par ailleurs, comme $A = -I_3 + N$, on a $P^{-1} A P = P^{-1} (-I_3 + N) P = -I_3 + P^{-1} N P = -I_3 + J_3(0)$.
La matrice $A$ est donc réductible à la forme de Jordan $J = \begin{pmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{pmatrix}$. $\blacksquare$

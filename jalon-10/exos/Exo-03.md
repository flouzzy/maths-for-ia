# Exercice 03
## Énoncé
Soit $E$ un $\mathbb{R}$-espace vectoriel de dimension 2. Soit $\mathcal{B} = (e_1, e_2)$ une base de $E$.
Soit $\mathcal{B}' = (e'_1, e'_2)$ la famille définie par :
$e'_1 = 2e_1 + e_2$
$e'_2 = 3e_1 + 2e_2$

1. Montrer que $\mathcal{B}'$ est une base de $E$.
2. Écrire la matrice de passage $P$ de $\mathcal{B}$ à $\mathcal{B}'$.
3. Calculer l'inverse de $P$.
4. Soit $u \in E$ le vecteur de coordonnées $X = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ dans $\mathcal{B}$. Calculer ses coordonnées $X'$ dans $\mathcal{B}'$.

## Correction
**1. Montrons que $\mathcal{B}'$ est une base de $E$ :**
Il suffit de montrer que la famille $(e'_1, e'_2)$ est libre, car elle contient 2 vecteurs et $\dim(E) = 2$.
Soient $\lambda_1, \lambda_2 \in \mathbb{R}$ tels que $\lambda_1 e'_1 + \lambda_2 e'_2 = 0_E$.
$\lambda_1 (2e_1 + e_2) + \lambda_2 (3e_1 + 2e_2) = 0_E$
$(2\lambda_1 + 3\lambda_2)e_1 + (\lambda_1 + 2\lambda_2)e_2 = 0_E$
Comme $\mathcal{B} = (e_1, e_2)$ est une base, c'est une famille libre. On obtient le système :
$\begin{cases} 2\lambda_1 + 3\lambda_2 = 0 \\ \lambda_1 + 2\lambda_2 = 0 \end{cases}$
De la deuxième équation, on tire $\lambda_1 = -2\lambda_2$.
En remplaçant dans la première : $2(-2\lambda_2) + 3\lambda_2 = 0 \implies -\lambda_2 = 0 \implies \lambda_2 = 0$.
Puis $\lambda_1 = -2(0) = 0$.
La famille $(e'_1, e'_2)$ est donc libre. C'est bien une base de $E$.

**2. Matrice de passage $P$ :**
Par définition, la matrice de passage $P_{\mathcal{B} \to \mathcal{B}'}$ contient en colonnes les coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ exprimés dans l'ancienne base $\mathcal{B}$.
$e'_1 = 2e_1 + 1e_2 \implies \text{colonne 1 } = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$
$e'_2 = 3e_1 + 2e_2 \implies \text{colonne 2 } = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$
Donc $P = \begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix}$.

**3. Calcul de $P^{-1}$ :**
Le déterminant de $P$ est $\det(P) = 2 \times 2 - 3 \times 1 = 4 - 3 = 1$.
Puisque $\det(P) \neq 0$, $P$ est bien inversible.
La formule de l'inverse pour une matrice $2 \times 2$ $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ est $\frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
Ici, $P^{-1} = \frac{1}{1} \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$.

**4. Coordonnées de $u$ dans $\mathcal{B}'$ :**
La formule de changement de coordonnées est $X = P X'$, ce qui équivaut à $X' = P^{-1} X$.
On a $X = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
Calculons $X'$ :
$X' = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 \times 1 + (-3) \times (-1) \\ (-1) \times 1 + 2 \times (-1) \end{pmatrix} = \begin{pmatrix} 2 + 3 \\ -1 - 2 \end{pmatrix} = \begin{pmatrix} 5 \\ -3 \end{pmatrix}$.
Les coordonnées de $u$ dans la base $\mathcal{B}'$ sont donc $\begin{pmatrix} 5 \\ -3 \end{pmatrix}$.

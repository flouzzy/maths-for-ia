# Exercice 4 : Décomposition de Dunford en dimension 3 (★★★)

Soit $M = \begin{pmatrix} 1 & 4 & -2 \\ 0 & 6 & -3 \\ -1 & 4 & 0 \end{pmatrix} \in \mathcal{M}_3(\mathbb{R})$.
Trouver la décomposition de Dunford $M = D + N$.
(Indication : On sait que $\chi_M(X) = (X-2)^2(X-3)$. On commencera par chercher les sous-espaces propres et caractéristiques).

### Solution :

**Étape 1 : Sous-espaces caractéristiques et projecteurs**
Les valeurs propres sont $2$ (multiplicité 2) et $3$ (multiplicité 1).
Par le lemme des noyaux, $\mathbb{R}^3 = \ker((M-2I)^2) \oplus \ker(M-3I)$.
Notons $E_2' = \ker((M-2I)^2)$ et $E_3 = \ker(M-3I)$.

Calculons $(M-2I)^2$ :
$$ M - 2I = \begin{pmatrix} -1 & 4 & -2 \\ 0 & 4 & -3 \\ -1 & 4 & -2 \end{pmatrix} $$
$$ (M-2I)^2 = \begin{pmatrix} -1 & 4 & -2 \\ 0 & 4 & -3 \\ -1 & 4 & -2 \end{pmatrix} \begin{pmatrix} -1 & 4 & -2 \\ 0 & 4 & -3 \\ -1 & 4 & -2 \end{pmatrix} = \begin{pmatrix} 3 & 4 & -6 \\ 3 & 4 & -6 \\ 3 & 4 & -6 \end{pmatrix} $$
Le noyau de $(M-2I)^2$ est l'ensemble des vecteurs $(x,y,z)^T$ tels que $3x+4y-6z=0$, c'est-à-dire $z = \frac{1}{2}x + \frac{2}{3}y$.
Une base de $E_2'$ est $\mathcal{B}_{E_2'} = \left( u_1 = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}, u_2 = \begin{pmatrix} 0 \\ 3 \\ 2 \end{pmatrix} \right)$.

Calculons $\ker(M-3I)$ :
$$ M - 3I = \begin{pmatrix} -2 & 4 & -2 \\ 0 & 3 & -3 \\ -1 & 4 & -3 \end{pmatrix} $$
Résolution du système :
$-2x+4y-2z = 0 \implies x = 2y-z$
$3y-3z = 0 \implies y=z$
Donc $x = 2z-z = z$.
Une base de $E_3$ est $u_3 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$.

**Étape 2 : Construction de la matrice $D$**
La matrice $D$ de la décomposition de Dunford est définie comme l'endomorphisme qui, sur chaque sous-espace caractéristique, agit comme une homothétie de rapport la valeur propre correspondante.
C'est-à-dire : $\forall v \in E_2', D(v) = 2v$, et $\forall v \in E_3, D(v) = 3v$.
Dans la base $P = (u_1, u_2, u_3)$, on a $D_P = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$.
On doit repasser dans la base canonique pour obtenir $D$.
$P = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 1 \\ 1 & 2 & 1 \end{pmatrix}$. L'inversion de $P$ donne : $\det(P) = 2(3-2) - 0 + 1(0-3) = 2 - 3 = -1$.
$P^{-1} = -1 \begin{pmatrix} 1 & 1 & -3 \\ 2 & 1 & -4 \\ -3 & -2 & 6 \end{pmatrix}^T = \begin{pmatrix} -1 & -2 & 3 \\ -1 & -1 & 2 \\ 3 & 4 & -6 \end{pmatrix}$
$D = P D_P P^{-1} = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 1 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} -1 & -2 & 3 \\ -1 & -1 & 2 \\ 3 & 4 & -6 \end{pmatrix} = \begin{pmatrix} 4 & 0 & 3 \\ 0 & 6 & 3 \\ 2 & 4 & 3 \end{pmatrix} \begin{pmatrix} -1 & -2 & 3 \\ -1 & -1 & 2 \\ 3 & 4 & -6 \end{pmatrix}$
$D = \begin{pmatrix} 5 & 4 & -6 \\ 3 & 6 & -6 \\ 3 & 4 & -4 \end{pmatrix}$

**Étape 3 : Déduction de $N$**
Par définition de Dunford, $M = D + N \implies N = M - D$.
$$ N = \begin{pmatrix} 1 & 4 & -2 \\ 0 & 6 & -3 \\ -1 & 4 & 0 \end{pmatrix} - \begin{pmatrix} 5 & 4 & -6 \\ 3 & 6 & -6 \\ 3 & 4 & -4 \end{pmatrix} = \begin{pmatrix} -4 & 0 & 4 \\ -3 & 0 & 3 \\ -4 & 0 & 4 \end{pmatrix} $$
Vérification : $N^2 = \begin{pmatrix} -4 & 0 & 4 \\ -3 & 0 & 3 \\ -4 & 0 & 4 \end{pmatrix} \begin{pmatrix} -4 & 0 & 4 \\ -3 & 0 & 3 \\ -4 & 0 & 4 \end{pmatrix} = \begin{pmatrix} 16-16 & 0 & -16+16 \\ 12-12 & 0 & -12+12 \\ 16-16 & 0 & -16+16 \end{pmatrix} = 0_3$. $N$ est bien nilpotente.
La décomposition est bien $(D, N)$.

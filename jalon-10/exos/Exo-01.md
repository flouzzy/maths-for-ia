# Exercice 01
## Énoncé
Soit $E = \mathbb{R}^2$ muni de sa base canonique $\mathcal{B} = (e_1, e_2)$.
On considère les vecteurs $e'_1 = (1, 2)$ et $e'_2 = (-1, 1)$.
1. Montrer que $\mathcal{B}' = (e'_1, e'_2)$ forme une base de $E$.
2. Écrire la matrice de passage $P$ de la base $\mathcal{B}$ à la base $\mathcal{B}'$.
3. Calculer la matrice $P^{-1}$.
4. Soit un vecteur $u$ de $E$ dont les coordonnées dans la base $\mathcal{B}$ sont $X = \begin{pmatrix} 2 \\ 5 \end{pmatrix}$.
   Calculer ses coordonnées $X'$ dans la base $\mathcal{B}'$ en utilisant $P^{-1}$.

## Correction
**1. Montrer que $\mathcal{B}'$ est une base de $E$ :**
Puisque $\dim(E) = 2$ et que la famille $\mathcal{B}'$ contient $2$ vecteurs, il suffit de vérifier qu'elle est libre.
Soient $\lambda_1, \lambda_2 \in \mathbb{R}$ tels que $\lambda_1 e'_1 + \lambda_2 e'_2 = 0_E$.
$\lambda_1(1, 2) + \lambda_2(-1, 1) = (0, 0)$
On obtient le système :
$\begin{cases} \lambda_1 - \lambda_2 = 0 \\ 2\lambda_1 + \lambda_2 = 0 \end{cases}$
De la première équation, on a $\lambda_1 = \lambda_2$.
En remplaçant dans la seconde : $2\lambda_1 + \lambda_1 = 3\lambda_1 = 0 \implies \lambda_1 = 0$.
D'où $\lambda_2 = 0$. La famille est libre, c'est donc une base de $\mathbb{R}^2$.

**2. Matrice de passage $P$ :**
Les colonnes de $P$ sont les coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ dans l'ancienne base $\mathcal{B}$.
$e'_1 = 1e_1 + 2e_2 \implies \text{colonne 1 } = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$
$e'_2 = -1e_1 + 1e_2 \implies \text{colonne 2 } = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$
$P = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix}$.

**3. Calcul de $P^{-1}$ :**
Le déterminant de $P$ est $\det(P) = (1)(1) - (-1)(2) = 1 + 2 = 3$.
La formule de l'inverse d'une matrice $2 \times 2$ donne :
$P^{-1} = \frac{1}{\det(P)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 1/3 & 1/3 \\ -2/3 & 1/3 \end{pmatrix}$.

**4. Coordonnées de $u$ dans $\mathcal{B}'$ :**
On utilise la formule $X' = P^{-1} X$.
$X' = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 5 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 1 \times 2 + 1 \times 5 \\ -2 \times 2 + 1 \times 5 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 7 \\ 1 \end{pmatrix} = \begin{pmatrix} 7/3 \\ 1/3 \end{pmatrix}$.
Les coordonnées de $u$ dans la base $\mathcal{B}'$ sont donc $(7/3, 1/3)$.









## Correction détaillée (Protocole d'Exégèse)

**1. Énoncé symbolique et Typage Chirurgical :**
Les variables et espaces du problème sont rigoureusement typés dans l'énoncé. La résolution suit.

**2. Démonstration (Zéro ellipse) :**
La résolution s'appuie sur la linéarité et les propriétés de la matrice de passage abordées en cours.

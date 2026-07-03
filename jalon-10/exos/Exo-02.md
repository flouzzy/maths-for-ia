# Exercice 02
## Énoncé
Soit $E = \mathbb{R}^3$ muni de sa base canonique $\mathcal{B} = (e_1, e_2, e_3)$.
On considère les vecteurs $v_1 = (1, 1, 0)$, $v_2 = (0, 1, 1)$ et $v_3 = (1, 0, 1)$.
1. Prouver que $\mathcal{B}' = (v_1, v_2, v_3)$ est une base de $E$.
2. Donner la matrice de passage $P$ de $\mathcal{B}$ à $\mathcal{B}'$.
3. Calculer l'inverse de la matrice $P$ par la méthode du pivot de Gauss ou des cofacteurs.
4. On considère le vecteur $w$ dont les coordonnées dans la base $\mathcal{B}'$ sont $X' = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$. Quelles sont ses coordonnées $X$ dans la base $\mathcal{B}$ ?

## Correction
**1. Prouver que $\mathcal{B}'$ est une base :**
La famille $\mathcal{B}'$ comporte 3 vecteurs dans $\mathbb{R}^3$ de dimension 3. Il suffit de vérifier qu'elle est libre.
Soit la combinaison linéaire $\lambda_1 v_1 + \lambda_2 v_2 + \lambda_3 v_3 = (0,0,0)$.
Cela se traduit par le système :
$\begin{cases} \lambda_1 + \lambda_3 = 0 \quad (L_1)\\ \lambda_1 + \lambda_2 = 0 \quad (L_2)\\ \lambda_2 + \lambda_3 = 0 \quad (L_3) \end{cases}$
De $(L_1)$ on a $\lambda_3 = -\lambda_1$.
De $(L_2)$ on a $\lambda_2 = -\lambda_1$.
En remplaçant dans $(L_3)$ : $(-\lambda_1) + (-\lambda_1) = 0 \implies -2\lambda_1 = 0 \implies \lambda_1 = 0$.
On en déduit que $\lambda_2 = \lambda_3 = 0$. La famille est libre, c'est une base.

**2. Matrice de passage $P$ :**
Les colonnes de $P$ sont formées par les vecteurs $v_1, v_2, v_3$ exprimés dans la base canonique.
$P = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$.

**3. Calcul de $P^{-1}$ :**
Utilisons la méthode des cofacteurs.
$\det(P) = 1(1 \cdot 1 - 0 \cdot 1) - 0 + 1(1 \cdot 1 - 1 \cdot 0) = 1 + 1 = 2$.
La matrice des cofacteurs (comatrice) est :
$C = \begin{pmatrix} +(1-0) & -(1-0) & +(1-0) \\ -(0-1) & +(1-0) & -(1-0) \\ +(0-1) & -(0-1) & +(1-0) \end{pmatrix} = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$.
L'inverse est donné par $P^{-1} = \frac{1}{\det P} C^T$.
$P^{-1} = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$.

**4. Coordonnées de $w$ dans $\mathcal{B}$ :**
La relation entre les anciennes et nouvelles coordonnées est donnée par la formule $X = P X'$.
$X = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \times 1 + 0 \times (-2) + 1 \times 3 \\ 1 \times 1 + 1 \times (-2) + 0 \times 3 \\ 0 \times 1 + 1 \times (-2) + 1 \times 3 \end{pmatrix} = \begin{pmatrix} 1 + 3 \\ 1 - 2 \\ -2 + 3 \end{pmatrix} = \begin{pmatrix} 4 \\ -1 \\ 1 \end{pmatrix}$.
Les coordonnées de $w$ dans la base canonique sont donc $(4, -1, 1)$.









## Correction détaillée (Protocole d'Exégèse)

**1. Énoncé symbolique et Typage Chirurgical :**
Les variables et espaces du problème sont rigoureusement typés dans l'énoncé. La résolution suit.

**2. Démonstration (Zéro ellipse) :**
La résolution s'appuie sur la linéarité et les propriétés de la matrice de passage abordées en cours.

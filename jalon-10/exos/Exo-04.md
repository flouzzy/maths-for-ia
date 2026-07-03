# Exercice 04
## Énoncé
Dans l'espace vectoriel $E = \mathbb{R}^2$, on considère la base canonique $\mathcal{B} = (e_1, e_2)$.
On définit l'endomorphisme $f$ par sa matrice dans $\mathcal{B}$ :
$A = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix}$.
On pose $u_1 = (1, 1)$ et $u_2 = (2, -1)$.
1. Montrer que $\mathcal{B}' = (u_1, u_2)$ est une base de $E$.
2. Écrire la matrice de passage $P$ de $\mathcal{B}$ à $\mathcal{B}'$, et calculer $P^{-1}$.
3. Calculer $f(u_1)$ et $f(u_2)$ sous forme de vecteurs de la base canonique. En déduire que $u_1$ et $u_2$ sont des vecteurs propres de $f$.
4. Quelle est la matrice $A'$ de $f$ dans la base $\mathcal{B}'$ ?
5. Retrouver le résultat précédent en effectuant le produit matriciel $P^{-1} A P$.

## Correction
**1. Montrer que $\mathcal{B}'$ est une base :**
Il suffit de calculer le déterminant des vecteurs de la famille dans la base canonique :
$\det(u_1, u_2) = \begin{vmatrix} 1 & 2 \\ 1 & -1 \end{vmatrix} = 1(-1) - 1(2) = -1 - 2 = -3$.
Comme le déterminant est non nul, la famille est libre. De cardinal 2 en dimension 2, c'est une base.

**2. Matrice de passage $P$ et son inverse :**
$P = \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix}$.
$P^{-1} = \frac{1}{-3} \begin{pmatrix} -1 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1/3 & 2/3 \\ 1/3 & -1/3 \end{pmatrix}$.

**3. Calcul de $f(u_1)$ et $f(u_2)$ :**
Le vecteur coordonnée de $u_1$ est $X_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
$f(u_1)$ a pour vecteur coordonnée $AX_1 = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1+4 \\ 2+3 \end{pmatrix} = \begin{pmatrix} 5 \\ 5 \end{pmatrix} = 5 \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Donc $f(u_1) = 5u_1$. $u_1$ est un vecteur propre associé à la valeur propre $5$.

Le vecteur coordonnée de $u_2$ est $X_2 = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$.
$f(u_2)$ a pour vecteur coordonnée $AX_2 = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 2-4 \\ 4-3 \end{pmatrix} = \begin{pmatrix} -2 \\ 1 \end{pmatrix} = -1 \begin{pmatrix} 2 \\ -1 \end{pmatrix}$.
Donc $f(u_2) = -u_2$. $u_2$ est un vecteur propre associé à la valeur propre $-1$.

**4. Matrice $A'$ de $f$ dans $\mathcal{B}'$ :**
Les colonnes de $A'$ sont formées par les coordonnées de $f(u_1)$ et $f(u_2)$ dans la base $(u_1, u_2)$.
Comme $f(u_1) = 5u_1 + 0u_2$ et $f(u_2) = 0u_1 - 1u_2$, on a directement :
$A' = \begin{pmatrix} 5 & 0 \\ 0 & -1 \end{pmatrix}$.

**5. Vérification avec $P^{-1} A P$ :**
Calculons d'abord $AP$ :
$AP = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 1 \times 1 + 4 \times 1 & 1 \times 2 + 4 \times (-1) \\ 2 \times 1 + 3 \times 1 & 2 \times 2 + 3 \times (-1) \end{pmatrix} = \begin{pmatrix} 5 & -2 \\ 5 & 1 \end{pmatrix}$.
Calculons ensuite $P^{-1}(AP)$ :
$P^{-1}(AP) = \begin{pmatrix} 1/3 & 2/3 \\ 1/3 & -1/3 \end{pmatrix} \begin{pmatrix} 5 & -2 \\ 5 & 1 \end{pmatrix} = \begin{pmatrix} \frac{5}{3} + \frac{10}{3} & \frac{-2}{3} + \frac{2}{3} \\ \frac{5}{3} - \frac{5}{3} & \frac{-2}{3} - \frac{1}{3} \end{pmatrix} = \begin{pmatrix} \frac{15}{3} & 0 \\ 0 & \frac{-3}{3} \end{pmatrix} = \begin{pmatrix} 5 & 0 \\ 0 & -1 \end{pmatrix}$.
On retrouve bien la matrice diagonale $A'$.









## Correction détaillée (Protocole d'Exégèse)

**1. Énoncé symbolique et Typage Chirurgical :**
Les variables et espaces du problème sont rigoureusement typés dans l'énoncé. La résolution suit.

**2. Démonstration (Zéro ellipse) :**
La résolution s'appuie sur la linéarité et les propriétés de la matrice de passage abordées en cours.

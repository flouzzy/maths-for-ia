# Exercice 08
## Énoncé
Soient $E_1, E_2$ deux espaces vectoriels de dimensions finies $n$ et $p$. On considère l'espace vectoriel produit $E = E_1 \times E_2$.
Soit $f_1 \in \mathcal{L}(E_1)$ et $f_2 \in \mathcal{L}(E_2)$.
On définit l'application $f : E \to E$ par $f(x,y) = (f_1(x), f_2(y))$.
Soit $\mathcal{B}_1$ une base de $E_1$ et $\mathcal{B}_2$ une base de $E_2$.
1. Montrer que $f$ est un endomorphisme de $E$.
2. Construire une base $\mathcal{B}$ de $E$ à partir de $\mathcal{B}_1$ et $\mathcal{B}_2$. Quelle est la dimension de $E$ ?
3. Montrer que la matrice $M$ de $f$ dans la base $\mathcal{B}$ est une matrice diagonale par blocs.
4. En déduire une expression du polynôme caractéristique de $M$ en fonction de ceux des blocs. *(Bien que le polynôme caractéristique soit formellement abordé au Jalon 29, il s'agit ici simplement d'appliquer la définition par le déterminant d'une matrice par blocs).*

## Correction
**1. Endomorphisme :**
$E_1 \times E_2$ est un espace vectoriel. $f$ va de $E$ dans $E$.
Montrons la linéarité. Soient $(x,y) \in E$, $(x',y') \in E$ et $\lambda \in \mathbb{R}$.
$f((x,y) + \lambda(x',y')) = f(x+\lambda x', y+\lambda y') = (f_1(x+\lambda x'), f_2(y+\lambda y'))$.
Par linéarité de $f_1$ et $f_2$ :
$= (f_1(x) + \lambda f_1(x'), f_2(y) + \lambda f_2(y')) = (f_1(x), f_2(y)) + \lambda(f_1(x'), f_2(y')) = f(x,y) + \lambda f(x',y')$.
$f$ est donc linéaire, c'est un endomorphisme.

**2. Base de l'espace produit :**
Soit $\mathcal{B}_1 = (e_1, ..., e_n)$ et $\mathcal{B}_2 = (u_1, ..., u_p)$.
On forme la famille $\mathcal{B} = ((e_1, 0), ..., (e_n, 0), (0, u_1), ..., (0, u_p))$.
Montrons qu'elle est génératrice : pour tout $(x,y) \in E$, on peut décomposer $x = \sum x_i e_i$ et $y = \sum y_j u_j$.
Alors $(x,y) = (x,0) + (0,y) = \sum x_i (e_i, 0) + \sum y_j (0, u_j)$.
Montrons qu'elle est libre : $\sum \lambda_i (e_i, 0) + \sum \mu_j (0, u_j) = (0,0) \implies (\sum \lambda_i e_i, \sum \mu_j u_j) = (0,0)$.
Ceci implique $\sum \lambda_i e_i = 0$ et $\sum \mu_j u_j = 0$. Comme $\mathcal{B}_1$ et $\mathcal{B}_2$ sont libres, tous les $\lambda_i$ et $\mu_j$ sont nuls.
Donc $\mathcal{B}$ est une base de $E$, et $\dim(E) = n + p$.

**3. Matrice de $f$ dans $\mathcal{B}$ :**
Évaluons $f$ sur les vecteurs de base :
$f(e_i, 0) = (f_1(e_i), f_2(0)) = (f_1(e_i), 0)$.
Comme $f_1(e_i) \in E_1$, ses coordonnées ne s'expriment que sur la première partie de la base $\mathcal{B}$ (les $(e_k, 0)$), et les coefficients sur les $(0, u_j)$ sont nuls.
De même, $f(0, u_j) = (f_1(0), f_2(u_j)) = (0, f_2(u_j))$, dont les coordonnées ne s'expriment que sur la seconde partie de la base.
Si l'on pose $A = \text{Mat}_{\mathcal{B}_1}(f_1)$ et $B = \text{Mat}_{\mathcal{B}_2}(f_2)$, la matrice $M$ s'écrit formellement par blocs :
$M = \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}$.

**4. Déterminant et polynôme :**
Le déterminant d'une matrice diagonale par blocs est le produit des déterminants des blocs diagonaux.
Le polynôme caractéristique est $P_M(\lambda) = \det(M - \lambda I_{n+p})$.
Or, $M - \lambda I_{n+p} = \begin{pmatrix} A - \lambda I_n & 0 \\ 0 & B - \lambda I_p \end{pmatrix}$.
Donc $P_M(\lambda) = \det(A - \lambda I_n) \times \det(B - \lambda I_p) = P_A(\lambda) \times P_B(\lambda)$.









## Correction détaillée (Protocole d'Exégèse)

**1. Énoncé symbolique et Typage Chirurgical :**
Les variables et espaces du problème sont rigoureusement typés dans l'énoncé. La résolution suit.

**2. Démonstration (Zéro ellipse) :**
La résolution s'appuie sur la linéarité et les propriétés de la matrice de passage abordées en cours.

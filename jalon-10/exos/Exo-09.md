# Exercice 09
## Énoncé
Soient $A, B \in \mathcal{M}_n(\mathbb{R})$.
On considère la matrice par blocs de taille $2n \times 2n$ : $M = \begin{pmatrix} A & B \\ B & A \end{pmatrix}$.
1. En introduisant la matrice de passage par blocs $P = \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix}$, calculer l'inverse $P^{-1}$.
2. Calculer le produit $P^{-1} M P$.
3. En déduire une condition nécessaire et suffisante pour que $M$ soit inversible, exprimée à l'aide de $A+B$ et $A-B$.
4. Si cette condition est remplie, exprimer $M^{-1}$ sous forme de matrice par blocs en fonction de $(A+B)^{-1}$ et $(A-B)^{-1}$.

## Correction
**1. Inversion de $P$ :**
Cherchons $P^{-1} = \begin{pmatrix} X & Y \\ Z & W \end{pmatrix}$ telle que $P P^{-1} = \begin{pmatrix} I_n & 0 \\ 0 & I_n \end{pmatrix}$.
$\begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} \begin{pmatrix} X & Y \\ Z & W \end{pmatrix} = \begin{pmatrix} X+Z & Y+W \\ X-Z & Y-W \end{pmatrix} = \begin{pmatrix} I_n & 0 \\ 0 & I_n \end{pmatrix}$.
On résout les systèmes :
$X+Z = I_n$ et $X-Z = 0 \implies X=Z$. Donc $2X = I_n \implies X = Z = \frac{1}{2}I_n$.
$Y+W = 0 \implies W = -Y$. $Y-W = I_n \implies 2Y = I_n \implies Y = \frac{1}{2}I_n$, $W = -\frac{1}{2}I_n$.
Donc $P^{-1} = \frac{1}{2} \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} = \frac{1}{2} P$.
(On remarque que $P^2 = 2 I_{2n}$).

**2. Calcul de $P^{-1} M P$ :**
$MP = \begin{pmatrix} A & B \\ B & A \end{pmatrix} \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} = \begin{pmatrix} A+B & A-B \\ B+A & B-A \end{pmatrix}$.
$P^{-1} M P = \frac{1}{2} \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} \begin{pmatrix} A+B & A-B \\ A+B & -(A-B) \end{pmatrix} = \frac{1}{2} \begin{pmatrix} (A+B)+(A+B) & (A-B)-(A-B) \\ (A+B)-(A+B) & (A-B)-(-(A-B)) \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2(A+B) & 0 \\ 0 & 2(A-B) \end{pmatrix} = \begin{pmatrix} A+B & 0 \\ 0 & A-B \end{pmatrix}$.

**3. Condition d'inversibilité :**
On a obtenu $P^{-1} M P = \begin{pmatrix} A+B & 0 \\ 0 & A-B \end{pmatrix}$.
Soit $D$ cette matrice diagonale par blocs. Comme $P$ est inversible, $M$ est inversible si et seulement si $D$ l'est.
Or, l'inversibilité d'une matrice diagonale par blocs équivaut à l'inversibilité de chacun de ses blocs diagonaux.
Donc $M$ est inversible $\iff (A+B)$ est inversible ET $(A-B)$ est inversible.

**4. Calcul de $M^{-1}$ :**
Si la condition est remplie, $D^{-1} = \begin{pmatrix} (A+B)^{-1} & 0 \\ 0 & (A-B)^{-1} \end{pmatrix}$.
Puisque $D = P^{-1} M P$, on a $M = P D P^{-1}$, d'où $M^{-1} = P D^{-1} P^{-1}$.
$M^{-1} = \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} \begin{pmatrix} (A+B)^{-1} & 0 \\ 0 & (A-B)^{-1} \end{pmatrix} \left( \frac{1}{2} \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} \right)$
$M^{-1} = \frac{1}{2} \begin{pmatrix} (A+B)^{-1} & (A-B)^{-1} \\ (A+B)^{-1} & -(A-B)^{-1} \end{pmatrix} \begin{pmatrix} I_n & I_n \\ I_n & -I_n \end{pmatrix} = \frac{1}{2} \begin{pmatrix} (A+B)^{-1} + (A-B)^{-1} & (A+B)^{-1} - (A-B)^{-1} \\ (A+B)^{-1} - (A-B)^{-1} & (A+B)^{-1} + (A-B)^{-1} \end{pmatrix}$.
On pose $S = \frac{1}{2}((A+B)^{-1} + (A-B)^{-1})$ et $T = \frac{1}{2}((A+B)^{-1} - (A-B)^{-1})$.
Alors $M^{-1} = \begin{pmatrix} S & T \\ T & S \end{pmatrix}$. L'inverse possède la même structure de blocs que $M$.









## Correction détaillée (Protocole d'Exégèse)

**1. Énoncé symbolique et Typage Chirurgical :**
Les variables et espaces du problème sont rigoureusement typés dans l'énoncé. La résolution suit.

**2. Démonstration (Zéro ellipse) :**
La résolution s'appuie sur la linéarité et les propriétés de la matrice de passage abordées en cours.

# Exercice 10
## Énoncé
Soit $E$ un espace vectoriel de dimension $n$ et $f, g \in \mathcal{L}(E)$ tels que $E = \ker(f) \oplus \text{Im}(f)$.
1. Montrer qu'il existe une base $\mathcal{B}$ de $E$ telle que la matrice $A$ de $f$ dans $\mathcal{B}$ soit de la forme $A = \begin{pmatrix} A_1 & 0 \\ 0 & 0 \end{pmatrix}$, où $A_1$ est une matrice carrée inversible de taille $r = \text{rg}(f)$.
2. On suppose de plus que $f \circ g = g \circ f = f$. Soit $B = \begin{pmatrix} B_1 & B_2 \\ B_3 & B_4 \end{pmatrix}$ la matrice de $g$ dans cette même base $\mathcal{B}$ (avec les mêmes tailles de blocs).
Traduire la condition $f \circ g = g \circ f = f$ sur les blocs de $B$.
3. En déduire que $\ker(g) \subset \ker(f)$.

## Correction
**1. Forme bloc pour la matrice de $f$ :**
Par hypothèse, $E = \text{Im}(f) \oplus \ker(f)$.
Soit $r = \dim(\text{Im}(f))$. D'après le théorème du rang, $\dim(\ker(f)) = n - r$.
Soit $(e_1, ..., e_r)$ une base de $\text{Im}(f)$ et $(e_{r+1}, ..., e_n)$ une base de $\ker(f)$.
Puisque la somme est directe, $\mathcal{B} = (e_1, ..., e_r, e_{r+1}, ..., e_n)$ est une base de $E$.
Écrivons la matrice $A$ de $f$ dans $\mathcal{B}$.
Pour $j > r$, $e_j \in \ker(f)$, donc $f(e_j) = 0$. Les $n-r$ dernières colonnes de $A$ sont nulles.
Pour $j \le r$, $f(e_j) \in \text{Im}(f)$, car $\text{Im}(f)$ est stable par $f$. Donc $f(e_j)$ s'exprime uniquement en fonction de $(e_1, ..., e_r)$. Les coefficients correspondants à $(e_{r+1}, ..., e_n)$ sont nuls.
Ainsi, $A = \begin{pmatrix} A_1 & 0 \\ 0 & 0 \end{pmatrix}$, où $A_1 \in \mathcal{M}_r(\mathbb{R})$.
Montrons que $A_1$ est inversible. Soit $u \in \text{Im}(f)$ dont le vecteur colonne dans $(e_1, ..., e_r)$ est $X$.
Si $A_1 X = 0$, cela signifie que $f(u) = 0$, donc $u \in \ker(f)$. Or $u \in \text{Im}(f)$. Puisque la somme est directe, $u = 0$.
Le noyau de l'endomorphisme induit par $A_1$ est réduit à $0$, donc $A_1$ est inversible.

**2. Condition de commutation avec $g$ :**
On a $A = \begin{pmatrix} A_1 & 0 \\ 0 & 0 \end{pmatrix}$ et $B = \begin{pmatrix} B_1 & B_2 \\ B_3 & B_4 \end{pmatrix}$.
L'équation matricielle est $AB = BA = A$.
Calculons les produits par blocs :
$AB = \begin{pmatrix} A_1 B_1 & A_1 B_2 \\ 0 & 0 \end{pmatrix}$
$BA = \begin{pmatrix} B_1 A_1 & 0 \\ B_3 A_1 & 0 \end{pmatrix}$
On identifie les blocs avec $A$ :
- $A_1 B_1 = A_1 \implies A_1(B_1 - I_r) = 0$. Comme $A_1$ est inversible, on multiplie par $A_1^{-1}$ à gauche : $B_1 = I_r$.
- $A_1 B_2 = 0 \implies B_2 = 0$ (pour la même raison).
- $B_1 A_1 = A_1 \implies B_1 = I_r$ (cohérent).
- $B_3 A_1 = 0 \implies B_3 A_1 A_1^{-1} = 0 \implies B_3 = 0$.
Le bloc $B_4$ n'est soumis à aucune contrainte par ces équations.
Donc la matrice $B$ est de la forme $B = \begin{pmatrix} I_r & 0 \\ 0 & B_4 \end{pmatrix}$.

**3. Déduction sur le noyau :**
Soit $x \in \ker(g)$. Son vecteur coordonnée $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ vérifie $BX = 0$.
$\begin{pmatrix} I_r & 0 \\ 0 & B_4 \end{pmatrix} \begin{pmatrix} X_1 \\ X_2 \end{pmatrix} = \begin{pmatrix} X_1 \\ B_4 X_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
On en déduit que $X_1 = 0$.
Calculons l'image de $x$ par $f$ : le vecteur coordonnée est $AX$.
$AX = \begin{pmatrix} A_1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ X_2 \end{pmatrix} = \begin{pmatrix} A_1 \cdot 0 + 0 \cdot X_2 \\ 0 \cdot 0 + 0 \cdot X_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
Donc $f(x) = 0$, c'est-à-dire $x \in \ker(f)$.
On a bien $\ker(g) \subset \ker(f)$.

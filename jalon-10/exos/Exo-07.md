# Exercice 07
## Énoncé
Soit $M = \begin{pmatrix} A & B \\ 0 & C \end{pmatrix}$ une matrice par blocs, où $A \in \mathcal{M}_n(\mathbb{R})$, $C \in \mathcal{M}_p(\mathbb{R})$ et $B \in \mathcal{M}_{n,p}(\mathbb{R})$.
1. Calculer $M^2$ puis $M^3$ sous forme de matrices par blocs.
2. Démontrer par récurrence sur $k \in \mathbb{N}^*$ que $M^k = \begin{pmatrix} A^k & X_k \\ 0 & C^k \end{pmatrix}$ où on précisera une relation de récurrence pour la matrice $X_k$.
3. On pose $A = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 3 \end{pmatrix}$ et $B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. Calculer explicitement la matrice $M^k$ pour tout $k \ge 1$.

## Correction
**1. Calcul de $M^2$ et $M^3$ :**
Les produits matriciels s'effectuent sur les blocs de la même manière que sur des scalaires (à condition que les dimensions soient compatibles, ce qui est le cas ici).
$M^2 = \begin{pmatrix} A & B \\ 0 & C \end{pmatrix} \begin{pmatrix} A & B \\ 0 & C \end{pmatrix} = \begin{pmatrix} A \cdot A + B \cdot 0 & A \cdot B + B \cdot C \\ 0 \cdot A + C \cdot 0 & 0 \cdot B + C \cdot C \end{pmatrix} = \begin{pmatrix} A^2 & AB+BC \\ 0 & C^2 \end{pmatrix}$.

Pour $M^3$ :
$M^3 = M^2 M = \begin{pmatrix} A^2 & AB+BC \\ 0 & C^2 \end{pmatrix} \begin{pmatrix} A & B \\ 0 & C \end{pmatrix} = \begin{pmatrix} A^2 \cdot A + (AB+BC) \cdot 0 & A^2 \cdot B + (AB+BC)C \\ 0 \cdot A + C^2 \cdot 0 & 0 \cdot B + C^2 \cdot C \end{pmatrix} = \begin{pmatrix} A^3 & A^2B + ABC + BC^2 \\ 0 & C^3 \end{pmatrix}$.

**2. Démonstration par récurrence :**
Soit la propriété $P(k)$ : "$M^k = \begin{pmatrix} A^k & X_k \\ 0 & C^k \end{pmatrix}$".
*Initialisation :* Pour $k=1$, $M^1 = M = \begin{pmatrix} A & B \\ 0 & C \end{pmatrix}$, ce qui correspond bien à la forme avec $X_1 = B$.
*Hérédité :* Supposons la propriété vraie pour un certain entier $k \ge 1$.
Montrons-la au rang $k+1$.
$M^{k+1} = M^k M = \begin{pmatrix} A^k & X_k \\ 0 & C^k \end{pmatrix} \begin{pmatrix} A & B \\ 0 & C \end{pmatrix} = \begin{pmatrix} A^k \cdot A + X_k \cdot 0 & A^k \cdot B + X_k \cdot C \\ 0 \cdot A + C^k \cdot 0 & 0 \cdot B + C^k \cdot C \end{pmatrix} = \begin{pmatrix} A^{k+1} & A^kB + X_k C \\ 0 & C^{k+1} \end{pmatrix}$.
La propriété est donc vraie au rang $k+1$ en posant $X_{k+1} = A^k B + X_k C$.
*Conclusion :* Par le principe de récurrence, pour tout $k \ge 1$, $M^k = \begin{pmatrix} A^k & X_k \\ 0 & C^k \end{pmatrix}$.

**3. Calcul de $M^k$ pour un cas spécifique :**
On a $A = 2I_2$, $C = (3)$, et $B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Il est immédiat que $A^k = 2^k I_2$ et $C^k = (3^k)$.
Il reste à calculer $X_k$. Trouvons une formule explicite pour $X_k$.
D'après la relation de récurrence obtenue en question 2, on peut aussi l'écrire de l'autre côté :
$M^{k+1} = M M^k \implies X_{k+1} = A X_k + B C^k$.
Puisque $A = 2I_2$, on a : $X_{k+1} = 2 X_k + B 3^k$.
Calculons les premiers termes :
$X_1 = B$
$X_2 = 2B + 3B = 5B$
$X_3 = 2(5B) + 3^2 B = 10B + 9B = 19B$.
On peut résoudre cette suite arithmético-géométrique matricielle. Soit $X_k = x_k B$.
La suite scalaire $(x_k)$ vérifie $x_{k+1} = 2x_k + 3^k$ avec $x_1 = 1$.
Cherchons une solution particulière sous la forme $x_k = \lambda 3^k$.
$\lambda 3^{k+1} = 2 \lambda 3^k + 3^k \implies 3\lambda = 2\lambda + 1 \implies \lambda = 1$.
Donc $x_k = 3^k + \alpha 2^k$.
Pour $k=1$, $x_1 = 1 = 3^1 + \alpha 2^1 \implies 1 = 3 + 2\alpha \implies 2\alpha = -2 \implies \alpha = -1$.
Donc $x_k = 3^k - 2^k$.
Ainsi, $X_k = (3^k - 2^k) B = (3^k - 2^k) \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3^k - 2^k \\ 3^k - 2^k \end{pmatrix}$.
Finalement, pour tout $k \ge 1$ :
$M^k = \begin{pmatrix} 2^k & 0 & 3^k - 2^k \\ 0 & 2^k & 3^k - 2^k \\ 0 & 0 & 3^k \end{pmatrix}$.









## Correction détaillée (Protocole d'Exégèse)

**1. Énoncé symbolique et Typage Chirurgical :**
Les variables et espaces du problème sont rigoureusement typés dans l'énoncé. La résolution suit.

**2. Démonstration (Zéro ellipse) :**
La résolution s'appuie sur la linéarité et les propriétés de la matrice de passage abordées en cours.

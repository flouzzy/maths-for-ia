# Exercice 07 : Inverse d'un bloc diagonalisable + nilpotent (⭐⭐⭐⭐)

## Énoncé
Soit $A \in \mathcal{M}_n(\mathbb{R})$ inversible.
Supposons que $A = \lambda I_n - N$, où $\lambda \in \mathbb{R}^*$ et $N$ est une matrice nilpotente d'indice $p$.
1. Rappeler le développement en série entière formelle de $(1 - x)^{-1}$.
2. Utiliser ce développement pour exprimer $A^{-1}$ comme un polynôme en $N$.
3. Application : Soit le bloc de Jordan inversible $J_{\lambda} = \lambda I_3 + J$ (où $J$ est le bloc nilpotent usuel de taille 3, $\lambda \neq 0$). Calculer l'inverse exact de $J_{\lambda}$.

## Corrigé Rigoureux : Zéro Ellipse Mathématique

### 1. Développement formel
Pour un réel $x$ tel que $|x| < 1$, on a le développement géométrique classique :
$\frac{1}{1 - x} = \sum_{k=0}^{+\infty} x^k = 1 + x + x^2 + x^3 + \dots$

### 2. Expression de $A^{-1}$
Factorisons $A$ :
$A = \lambda I_n - N = \lambda (I_n - \frac{1}{\lambda} N)$.
Nous cherchons un inverse $B$ tel que $A B = I_n$, soit $\lambda (I_n - \frac{1}{\lambda} N) B = I_n$.
Cela s'écrit : $(I_n - \frac{1}{\lambda} N) B = \frac{1}{\lambda} I_n$.
Par analogie avec le développement scalaire, posons formellement :
$S = \sum_{k=0}^{+\infty} (\frac{1}{\lambda} N)^k$
Puisque $N$ est nilpotente d'indice $p$, on a $N^k = 0$ pour tout $k \ge p$.
La somme infinie est donc en réalité une somme finie :
$S = \sum_{k=0}^{p-1} \frac{1}{\lambda^k} N^k$
Vérifions que $S$ est l'inverse cherché en calculant $(I_n - \frac{1}{\lambda} N) S$ :
$(I_n - \frac{1}{\lambda} N) \sum_{k=0}^{p-1} (\frac{1}{\lambda} N)^k = \sum_{k=0}^{p-1} (\frac{1}{\lambda} N)^k - \frac{1}{\lambda} N \sum_{k=0}^{p-1} (\frac{1}{\lambda} N)^k$
$= \sum_{k=0}^{p-1} (\frac{1}{\lambda} N)^k - \sum_{k=0}^{p-1} (\frac{1}{\lambda} N)^{k+1}$
Par télescopage, presque tous les termes s'annulent. Il reste :
$= (\frac{1}{\lambda} N)^0 - (\frac{1}{\lambda} N)^p = I_n - \frac{1}{\lambda^p} N^p$
Or, par définition de l'indice de nilpotence, $N^p = 0$.
Donc le produit vaut bien $I_n$.
Ainsi, $(I_n - \frac{1}{\lambda} N)^{-1} = \sum_{k=0}^{p-1} \frac{1}{\lambda^k} N^k$.
On en déduit que $A^{-1} = \frac{1}{\lambda} (I_n - \frac{1}{\lambda} N)^{-1} = \sum_{k=0}^{p-1} \frac{1}{\lambda^{k+1}} N^k$.
L'inverse $A^{-1}$ est bien un polynôme en $N$.

### 3. Application au bloc de Jordan
Soit $J_{\lambda} = \lambda I_3 + J$, avec $J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.
Ici $A = \lambda I_3 - (-J)$. Donc on applique la formule avec $N = -J$ et $p=3$.
$A^{-1} = \frac{1}{\lambda} I_3 + \frac{1}{\lambda^2} (-J) + \frac{1}{\lambda^3} (-J)^2$.
Calculons les termes :
- $J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$
- $J^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$
Ainsi, l'inverse est :
$$J_{\lambda}^{-1} = \begin{pmatrix} \frac{1}{\lambda} & -\frac{1}{\lambda^2} & \frac{1}{\lambda^3} \\ 0 & \frac{1}{\lambda} & -\frac{1}{\lambda^2} \\ 0 & 0 & \frac{1}{\lambda} \end{pmatrix}$$
Ce résultat illustre parfaitement comment inverser explicitement des blocs diagonaux non diagonalisables.

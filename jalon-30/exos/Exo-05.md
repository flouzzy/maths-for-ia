# Exercice 5 : Dunford via la méthode de Newton (★★★)

Soit $A \in \mathcal{M}_n(\mathbb{C})$. On peut obtenir les projecteurs spectraux sans calcul de noyaux grâce à la méthode de Newton-Raphson sur les polynômes.
Soit $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$. Montrer que l'itération $X_{k+1} = X_k - \chi_A(X_k) \cdot (\chi_A'(X_k))^{-1}$ converge vers la composante diagonalisable $D$.
*(Note: on remplace la division usuelle par la multiplication par l'inverse de la matrice dérivée).*

### Solution :

Bien que la décomposition de Dunford de cette matrice soit triviale ($D=2I, N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$), illustrons l'algorithme itératif.
Le polynôme caractéristique est $\chi_A(X) = (X-2)^2$. Sa dérivée formelle est $\chi_A'(X) = 2(X-2) = 2X - 4$.
On évalue ces polynômes non pas sur des scalaires, mais sur la matrice $A$ elle-même pour les premiers termes.
L'algorithme de Newton pour trouver une racine d'un polynôme $P$ matriciellement, utilisé pour isoler la partie semi-simple, est plus subtil. La méthode de Newton sur $P(X) = X^2 - 4X + 4I$ pour trouver $D$ donne :
Initialisation : $X_0 = A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
On sait que par le théorème de Cayley-Hamilton, $P(A) = 0$. Ce n'est pas ce que l'on cherche.
L'algorithme constructif de Dunford basé sur Newton utilise un polynôme sans facteur carré (square-free) $Q$ dont les racines sont les valeurs propres de $A$.
Ici $Q(X) = X - 2$.
Soit $Q(A) = A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
L'algorithme itératif pour extraire $D$ s'écrit généralement $D_{k+1} = D_k - Q(D_k)(Q'(D_k))^{-1}$ en initialisant avec $D_0 = A$.
Ici, $Q'(X) = 1$.
Itération 1: $D_1 = D_0 - Q(D_0) = A - (A-2I) = 2I$.
On obtient immédiatement $D = 2I$.
$N = A - D = A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Cet exercice met en évidence que la composante diagonalisable $D$ est la "racine simple" associée à l'opérateur, dont la différence avec l'opérateur initial donne le résidu nilpotent.

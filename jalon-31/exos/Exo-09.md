# Exercice 09 : Matrices semblables et invariants de similitude (⭐⭐⭐⭐)

## Énoncé
Soient les deux matrices nilpotentes suivantes dans $\mathcal{M}_3(\mathbb{R})$ :
$$A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
1. Calculer les polynômes caractéristiques $\chi_A$ et $\chi_B$. Sont-ils égaux ?
2. Calculer $A^2$ et $A^3$. Déterminer l'indice de nilpotence de $A$.
3. $A$ et $B$ sont-elles semblables ? Justifier de manière formelle.

## Corrigé Rigoureux : Démonstration Complète

### 1. Polynômes caractéristiques
Les matrices $A$ et $B$ sont toutes deux des matrices triangulaires supérieures strictes.
Les éléments diagonaux sont donc les valeurs propres, et elles sont toutes nulles.
Le déterminant de $X I_3 - M$ pour une matrice triangulaire supérieure stricte $M$ est simplement le produit des termes de la diagonale $(X - 0)$.
Donc $\chi_A(X) = X^3$ et $\chi_B(X) = X^3$.
Les polynômes caractéristiques sont identiques.

### 2. Puissances et indice de nilpotence de $A$
Calculons $A^2$ :
$$A^2 = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
- Ligne 1, Col 3 : $0\times 1 + 1\times 1 + 1\times 0 = 1$.
Les autres coefficients sont nuls par les propriétés des matrices triangulaires strictes (Exercice 3).
$$A^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
$A^2 \neq 0$.
Par le théorème de Cayley-Hamilton, ou par calcul direct de $A^3 = A^2 A$, on sait que $A^3 = 0_3$.
L'indice de nilpotence de $A$ est donc $3$.

### 3. Similitude
Deux matrices sont semblables si et seulement si elles représentent le même endomorphisme dans des bases différentes. Si elles sont semblables, elles partagent les mêmes invariants de similitude : trace, déterminant, polynôme caractéristique, polynôme minimal, et indice de nilpotence.

La matrice $B$ est le bloc de Jordan canonique $J_3(0)$. Nous avons démontré dans l'exercice 4 que son indice de nilpotence est 3.
L'indice de nilpotence de $A$ est également 3.
Soit $u$ l'endomorphisme de $\mathbb{R}^3$ dont la matrice dans la base canonique est $A$.
$u$ est nilpotent d'indice $p=3$.
Comme démontré dans l'Exercice 4, tout endomorphisme nilpotent de dimension 3 et d'indice 3 admet un vecteur $x$ tel que $(u^2(x), u(x), x)$ est une base. Dans cette base, la matrice de $u$ est exactement $B = J_3(0)$.
Par conséquent, il existe une matrice de passage $P$ inversible telle que $A = P B P^{-1}$.
Les matrices $A$ et $B$ sont donc rigoureusement semblables.

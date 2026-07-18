# Exercice 7 : Exponentielle d'une matrice via Dunford (★★★★)

Soit $A = \begin{pmatrix} 4 & 1 & 1 \\ -2 & 1 & -2 \\ 1 & 1 & 4 \end{pmatrix}$.
1. Calculer le polynôme caractéristique de $A$ et justifier qu'elle admet une décomposition de Dunford $A = D + N$.
2. Trouver $D$ et $N$.
3. Calculer l'exponentielle de matrice $e^{tA}$ pour tout $t \in \mathbb{R}$.

### Solution :

**Étape 1 : Polynôme caractéristique**
$$ \chi_A(X) = \det(XI - A) = \begin{vmatrix} X-4 & -1 & -1 \\ 2 & X-1 & 2 \\ -1 & -1 & X-4 \end{vmatrix} $$
Effectuons l'opération sur les colonnes $C_1 \leftarrow C_1 - C_3$ :
$$ \begin{vmatrix} X-3 & -1 & -1 \\ 0 & X-1 & 2 \\ -(X-3) & -1 & X-4 \end{vmatrix} = (X-3) \begin{vmatrix} 1 & -1 & -1 \\ 0 & X-1 & 2 \\ -1 & -1 & X-4 \end{vmatrix} $$
Ligne $L_3 \leftarrow L_3 + L_1$ :
$$ (X-3) \begin{vmatrix} 1 & -1 & -1 \\ 0 & X-1 & 2 \\ 0 & -2 & X-5 \end{vmatrix} = (X-3) [ (X-1)(X-5) + 4 ] = (X-3)[X^2 - 6X + 9] = (X-3)^3 $$
Le polynôme caractéristique est $\chi_A(X) = (X-3)^3$. Il est scindé, Dunford s'applique.
De plus, par Cayley-Hamilton, $(A-3I)^3 = 0$.

**Étape 2 : Décomposition de Dunford**
Puisque la seule valeur propre est $3$, la partie diagonalisable $D$ doit avoir pour valeur propre uniquement $3$.
Comme $D$ est diagonalisable et n'a qu'une seule valeur propre, $D$ est semblable à la matrice scalaire $3I$, donc $D = 3I$.
Par unicité de la décomposition de Dunford, on a nécessairement :
$$ D = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix} = 3I $$
Et la partie nilpotente est $N = A - D$ :
$$ N = \begin{pmatrix} 4 & 1 & 1 \\ -2 & 1 & -2 \\ 1 & 1 & 4 \end{pmatrix} - \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ -2 & -2 & -2 \\ 1 & 1 & 1 \end{pmatrix} $$
Vérifions la nilpotence de $N$ :
$$ N^2 = \begin{pmatrix} 1 & 1 & 1 \\ -2 & -2 & -2 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ -2 & -2 & -2 \\ 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1-2+1 & 1-2+1 & 1-2+1 \\ -2+4-2 & -2+4-2 & -2+4-2 \\ 1-2+1 & 1-2+1 & 1-2+1 \end{pmatrix} = 0_3 $$
Donc $N$ est bien nilpotente d'indice 2.

**Étape 3 : Calcul de $e^{tA}$**
On écrit $tA = tD + tN$.
Puisque $D$ et $N$ commutent, $tD$ et $tN$ commutent également.
Par conséquent, on peut utiliser la propriété de morphisme exponentiel :
$$ e^{tA} = e^{tD + tN} = e^{tD} e^{tN} $$
L'exponentielle d'une matrice scalaire est immédiate :
$$ e^{tD} = e^{3tI} = e^{3t} I $$
L'exponentielle de la matrice nilpotente $tN$ donne une somme finie :
$$ e^{tN} = I + tN + \frac{(tN)^2}{2!} + \dots = I + tN \quad \text{(car } N^2 = 0 \text{)} $$
On obtient donc :
$$ e^{tA} = e^{3t} I \cdot (I + tN) = e^{3t}(I + tN) $$
En remplaçant $N$ par sa matrice :
$$ e^{tA} = e^{3t} \left[ \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + t \begin{pmatrix} 1 & 1 & 1 \\ -2 & -2 & -2 \\ 1 & 1 & 1 \end{pmatrix} \right] = e^{3t} \begin{pmatrix} 1+t & t & t \\ -2t & 1-2t & -2t \\ t & t & 1+t \end{pmatrix} $$
Cette matrice constitue la solution analytique exacte, fondamentale pour l'intégration de systèmes dynamiques linéaires $\dot{x}(t) = Ax(t)$.

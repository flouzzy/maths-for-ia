# Exercice 7 - Difficulté \quad $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\star$

## Énoncé
Soit $M = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
Vérifier le théorème de Cayley-Hamilton sur cette matrice, et en déduire l'expression de $M^{-1}$ comme combinaison linéaire de $I$ et $M$.

## Solution Complète

**Étape 1 : Calcul du polynôme caractéristique**
$\chi_M(X) = \det\begin{pmatrix} X-1 & -2 \\ -3 & X-4 \end{pmatrix} = (X-1)(X-4) - 6 = X^2 - 5X + 4 - 6 = X^2 - 5X - 2$.

**Étape 2 : Vérification du théorème de Cayley-Hamilton**
Le théorème stipule que pour toute matrice, son polynôme caractéristique est un polynôme annulateur : $\chi_M(M) = 0_{2\times2}$, c'est-à-dire $M^2 - 5M - 2I = 0$.
Calculons $M^2$ :
$$M^2 = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1+6 & 2+8 \\ 3+12 & 6+16 \end{pmatrix} = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$$
Calculons $5M$ :
$$5M = \begin{pmatrix} 5 & 10 \\ 15 & 20 \end{pmatrix}$$
Effectuons la somme $M^2 - 5M - 2I$ :
$$\begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix} - \begin{pmatrix} 5 & 10 \\ 15 & 20 \end{pmatrix} - \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 7-5-2 & 10-10-0 \\ 15-15-0 & 22-20-2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$
Le théorème de Cayley-Hamilton est bien vérifié.

**Étape 3 : Déduction de l'inverse**
Puisque $M^2 - 5M - 2I = 0$, on peut isoler $I$ :
$$2I = M^2 - 5M = M(M - 5I)$$
Donc :
$$I = M \left( \frac{1}{2}(M - 5I) \right)$$
Par définition de l'inverse, cela prouve que $M$ est inversible et que son inverse est :
$$M^{-1} = \frac{1}{2}M - \frac{5}{2}I$$
Vérifions numériquement :
$$M^{-1} = \frac{1}{2} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} - \begin{pmatrix} \frac{5}{2} & 0 \\ 0 & \frac{5}{2} \end{pmatrix} = \begin{pmatrix} \frac{1-5}{2} & 1 \\ \frac{3}{2} & \frac{4-5}{2} \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}$$
C'est bien l'inverse classique, obtenu élégamment par la théorie des polynômes d'endomorphismes.

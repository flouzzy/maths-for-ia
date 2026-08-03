# Exercice 6 - Difficulté : $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit la matrice $A = \begin{pmatrix} 6 & 1 \\ 0 & 6 \end{pmatrix}$. Calculer l'exponentielle de matrice $e^{tA}$ et en déduire la solution du système différentiel associé $Y'(t) = A Y(t)$ avec condition initiale $Y(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

## Démonstration et Résolution
Décomposons la matrice $A$ sous la forme d'une somme d'une matrice scalaire et d'une matrice nilpotente.
Posons $D = \begin{pmatrix} 6 & 0 \\ 0 & 6 \end{pmatrix} = 6 I_2$ et $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
On vérifie immédiatement que $A = D + N$.
Vérifions que $D$ et $N$ commutent :
$$ D N = (6 I_2) N = 6 N $$
$$ N D = N (6 I_2) = 6 N $$
Puisque $D$ et $N$ commutent, on peut appliquer la propriété fondamentale de l'exponentielle :
$$ e^{tA} = e^{t(D+N)} = e^{tD} e^{tN} $$
L'exponentielle de $tD$ est triviale :
$$ e^{tD} = e^{6 t I_2} = \begin{pmatrix} e^{6t} & 0 \\ 0 & e^{6t} \end{pmatrix} = e^{6t} I_2 $$
Calculons maintenant $e^{tN}$. On remarque que $N^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
Donc la série de l'exponentielle pour $tN$ s'arrête au terme d'ordre 1 :
$$ e^{tN} = I_2 + tN = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & t \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} $$
On effectue alors le produit des deux matrices :
$$ e^{tA} = (e^{6t} I_2) \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{6t} & t e^{6t} \\ 0 & e^{6t} \end{pmatrix} $$

Pour trouver la solution du système $Y'(t) = A Y(t)$, on applique le théorème fondamental :
$$ Y(t) = e^{tA} Y(0) = \begin{pmatrix} e^{6t} & t e^{6t} \\ 0 & e^{6t} \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} e^{6t} + t e^{6t} \\ e^{6t} \end{pmatrix} $$
La démonstration est ainsi complète et rigoureuse.

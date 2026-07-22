# Exercice 4 : Critère de Sylvester

## Énoncé
Soit la matrice symétrique réelle dépendante d'un paramètre $a \in \mathbb{R}$ :
$$ M_a = \begin{pmatrix} 1 & a & 0 \\ a & 2 & a \\ 0 & a & 1 \end{pmatrix} $$
Pour quelles valeurs de $a$, la forme quadratique associée est-elle définie positive ?

## Correction Détaillée (Zéro Ellipse)

Une matrice symétrique réelle est définie positive si et seulement si tous ses mineurs principaux dominants sont strictement positifs (Critère de Sylvester).
Les mineurs principaux dominants $\Delta_k$ de $M_a$ (de taille $k \times k$) sont :
1. $\Delta_1 = \det(1) = 1$
2. $\Delta_2 = \det \begin{pmatrix} 1 & a \\ a & 2 \end{pmatrix} = (1)(2) - (a)(a) = 2 - a^2$
3. $\Delta_3 = \det(M_a) = \det \begin{pmatrix} 1 & a & 0 \\ a & 2 & a \\ 0 & a & 1 \end{pmatrix}$.
On développe le déterminant par rapport à la première colonne :
$$ \Delta_3 = 1 \cdot \det \begin{pmatrix} 2 & a \\ a & 1 \end{pmatrix} - a \cdot \det \begin{pmatrix} a & 0 \\ a & 1 \end{pmatrix} + 0 $$
$$ \Delta_3 = 1 \cdot (2 - a^2) - a \cdot (a - 0) = 2 - a^2 - a^2 = 2 - 2a^2 $$

Pour que la forme quadratique soit définie positive, il faut que :
1. $\Delta_1 > 0 \iff 1 > 0$ (toujours vrai)
2. $\Delta_2 > 0 \iff 2 - a^2 > 0 \iff a^2 < 2 \iff -\sqrt{2} < a < \sqrt{2}$
3. $\Delta_3 > 0 \iff 2 - 2a^2 > 0 \iff 1 - a^2 > 0 \iff a^2 < 1 \iff -1 < a < 1$

L'intersection des conditions est $-1 < a < 1$.
Ainsi, la forme quadratique associée à $M_a$ est définie positive si et seulement si $a \in ]-1, 1[$. $\blacksquare$

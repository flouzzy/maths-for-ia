# Exercice 7: Orthogonalité dans le dual
## Énoncé
Soit $E = \mathbb{R}^3$. Soit $F = \text{Vect}(v)$ avec $v = (1, 1, 1)$.
Déterminer une base de $F^\circ$, l'orthogonal de $F$ dans l'espace dual $E^*$.


## Correction détaillée
L'espace $F$ est une droite vectorielle (dimension 1) engendrée par le vecteur $v = (1, 1, 1)$.
L'orthogonal de $F$ dans le dual est défini par :
$F^\circ = \{ \varphi \in E^* \mid \forall x \in F, \varphi(x) = 0 \}$
Puisque tout vecteur de $F$ s'écrit $\lambda v$, et que $\varphi$ est linéaire, il suffit que la condition soit vérifiée sur le générateur de $F$ :
$F^\circ = \{ \varphi \in E^* \mid \varphi(v) = 0 \}$

Toute forme linéaire $\varphi \in E^*$ s'exprime dans la base duale canonique $(e_1^*, e_2^*, e_3^*)$ :
$\varphi = x e_1^* + y e_2^* + z e_3^*$, c'est-à-dire $\varphi(a, b, c) = xa + yb + zc$.
La condition $\varphi(v) = 0$ se traduit par :
$\varphi(1, 1, 1) = x(1) + y(1) + z(1) = 0 \implies x + y + z = 0$.

L'orthogonal $F^\circ$ est donc l'ensemble des formes linéaires de coordonnées $(x, y, z)$ telles que $z = -x - y$.
$\varphi = x e_1^* + y e_2^* + (-x - y) e_3^* = x(e_1^* - e_3^*) + y(e_2^* - e_3^*)$.
Les formes $\varphi_1 = e_1^* - e_3^*$ et $\varphi_2 = e_2^* - e_3^*$ engendrent $F^\circ$.
Montrons qu'elles sont libres. Si $x(e_1^* - e_3^*) + y(e_2^* - e_3^*) = 0_{E^*}$, alors en évaluant sur $e_1$, on obtient $x = 0$, et sur $e_2$, on obtient $y = 0$. La famille est libre.

Conclusion : $(\varphi_1, \varphi_2) = (e_1^* - e_3^*, e_2^* - e_3^*)$ est une base de $F^\circ$.
On vérifie la formule des dimensions : $\dim(F) + \dim(F^\circ) = 1 + 2 = 3 = \dim(E)$.

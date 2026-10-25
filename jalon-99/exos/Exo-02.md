# Exercice 2 : Séparation large et ensembles ouverts $\bigstar\star\star\star\star$

## Énoncé
Montrez que l'on peut séparer au sens large l'ouvert $A = \{(x, y) \mid x > 0, y > 0, xy > 1\}$ et le fermé $B = \{(x, y) \mid x \leq 0 \text{ ou } y \leq 0\}$ dans $\mathbb{R}^2$.

## Correction Complète
L'ensemble $A$ est délimité par l'hyperbole $xy = 1$ dans le premier quadrant.
Soient $M_1(x_1, y_1)$ et $M_2(x_2, y_2)$ dans $A$. Soit $t \in [0, 1]$.
Posons $M = t M_1 + (1-t)M_2 = (t x_1 + (1-t)x_2, t y_1 + (1-t)y_2)$.
$M_1$ et $M_2$ sont strictement positifs, donc $M$ a ses coordonnées strictement positives.
Etudions le produit :
$(t x_1 + (1-t)x_2)(t y_1 + (1-t)y_2) = t^2 x_1 y_1 + (1-t)^2 x_2 y_2 + t(1-t)(x_1 y_2 + x_2 y_1)$.
Puisque $x_1 y_1 > 1$ et $x_2 y_2 > 1$, on a :
$x_1 y_2 + x_2 y_1 \geq 2 \sqrt{x_1 y_2 x_2 y_1} > 2 \sqrt{1} = 2$.
Ainsi le produit est strictement supérieur à $t^2 + (1-t)^2 + 2t(1-t) = (t+(1-t))^2 = 1$.
Donc $A$ est convexe. L'inégalité étant stricte, $A$ est un ouvert convexe.
L'ensemble $B$ est le complémentaire de $(0, +\infty) \times (0, +\infty)$. Il n'est pas convexe.
Toutefois, le théorème de Hahn-Banach (première forme) requiert que $A$ et $B$ soient tous deux convexes.
Ici, $A$ est séparable par rapport à l'origine $(0,0)$. Posons un convexe plus petit $C = \{(x, y) \mid x+y \leq 0\}$.
$A$ et $C$ sont disjoints, convexes, et $A$ est ouvert.
Un hyperplan (droite) séparant $A$ et $C$ est $H = \{(x, y) \mid x + y = 0\}$.
En réalité, la droite d'équation $x + y = 2$ est tangente à $A$ au point $(1,1)$.
La forme linéaire $f(x, y) = x + y$ vérifie :
Pour tout $(x, y) \in A$, par l'inégalité arithmético-géométrique, $x + y \geq 2\sqrt{xy} > 2$.
Pour tout $(x, y) \in C$, $x + y \leq 0$.
Donc $\forall a \in A, \forall c \in C, f(a) > f(c)$. La séparation est acquise. $\blacksquare$

# Exercice 9 : Endomorphismes orthogonaux et formes quadratiques

## Énoncé
Soit $E$ un espace vectoriel de dimension $n$. Soit $q$ une forme quadratique non dégénérée sur $E$, de forme polaire $b$.
Un endomorphisme $u \in \mathcal{L}(E)$ est dit orthogonal pour $q$ si $\forall x \in E, q(u(x)) = q(x)$.
1. Montrer que $u$ préserve la forme polaire $b$.
2. Montrer que si $u$ est orthogonal pour une forme quadratique non dégénérée $q$, alors $u$ est un automorphisme (inversible).

## Correction Détaillée (Zéro Ellipse)

**1. Préservation de la forme polaire**
Soit $x, y \in E$. On sait par la formule de polarisation que :
$$ b(x, y) = \frac{1}{2} (q(x+y) - q(x) - q(y)) $$
L'endomorphisme $u$ préserve $q$, donc pour le vecteur $x+y$, on a :
$$ q(u(x+y)) = q(x+y) $$
Or $u$ est linéaire, donc $u(x+y) = u(x) + u(y)$. L'égalité devient :
$$ q(u(x) + u(y)) = q(x+y) $$
Développons le membre de gauche avec la forme polaire évaluée aux images :
$$ q(u(x) + u(y)) = q(u(x)) + 2b(u(x), u(y)) + q(u(y)) $$
Comme $q(u(x)) = q(x)$ et $q(u(y)) = q(y)$, on a :
$$ q(x) + 2b(u(x), u(y)) + q(y) = q(x+y) $$
Mais l'identité de polarisation sur les variables de base nous donne :
$$ q(x+y) = q(x) + 2b(x, y) + q(y) $$
En identifiant les deux égalités, on obtient :
$$ q(x) + 2b(u(x), u(y)) + q(y) = q(x) + 2b(x, y) + q(y) $$
En simplifiant par $q(x)$ et $q(y)$ et en divisant par 2 :
$$ b(u(x), u(y)) = b(x, y) $$
L'endomorphisme préserve la forme polaire bilinéaire symétrique.

**2. Inversibilité de $u$**
Puisque $E$ est de dimension finie, il suffit de montrer que $u$ est injectif (c'est-à-dire $\ker(u) = \{0_E\}$) pour prouver qu'il est bijectif.
Soit $x \in \ker(u)$. Par définition, $u(x) = 0_E$.
Pour tout $y \in E$, appliquons la propriété démontrée à la question 1 :
$$ b(x, y) = b(u(x), u(y)) = b(0_E, u(y)) $$
Une forme bilinéaire évaluée en le vecteur nul donne toujours $0$ (par linéarité, $b(0, z) = b(0\cdot 0, z) = 0 \cdot b(0, z) = 0$).
Donc, $\forall y \in E, b(x, y) = 0$.
On en déduit que $x$ appartient au noyau de la forme polaire $b$ ($x \in \ker(b)$).
Or, l'énoncé précise que la forme quadratique $q$ est **non dégénérée**. La définition stricte de la non dégénérescence est que le noyau de la forme polaire est réduit au vecteur nul : $\ker(b) = \{0_E\}$.
Par conséquent, le vecteur $x$ doit être le vecteur nul, $x = 0_E$.
On a montré que tout élément de $\ker(u)$ est nul, donc $\ker(u) = \{0_E\}$. L'endomorphisme $u$ est injectif. En dimension finie, injectivité implique bijectivité. Donc $u \in \text{GL}(E)$. $\blacksquare$

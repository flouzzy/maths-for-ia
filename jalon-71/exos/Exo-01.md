# Exercice 1 : Intégrale double sur un rectangle $\bigstar\star\star\star\star$

## Énoncé

Soit $D = [0, 1] \times [1, 2]$. Calculer l'intégrale double suivante en utilisant le théorème de Tonelli :
$$ I = \iint_D (2x + 3y^2) \, dx \, dy $$

## Correction

La fonction $f(x, y) = 2x + 3y^2$ est continue sur le pavé fermé borné $D$, elle est donc mesurable. De plus, pour tout $(x, y) \in D$, $x \ge 0$ et $y \ge 1$, donc $f(x, y) \ge 0$. Les hypothèses du théorème de Tonelli sont vérifiées.
On peut donc intégrer par rapport à $x$ puis à $y$ (ou inversement).
$$ I = \int_1^2 \left( \int_0^1 (2x + 3y^2) \, dx \right) dy $$
Calculons l'intégrale intérieure (à $y$ fixé) :
$$ \int_0^1 (2x + 3y^2) \, dx = \left[ x^2 + 3y^2 x \right]_{x=0}^{x=1} = (1^2 + 3y^2 \cdot 1) - 0 = 1 + 3y^2 $$
Maintenant, on intègre ce résultat par rapport à $y$ :
$$ I = \int_1^2 (1 + 3y^2) \, dy = \left[ y + y^3 \right]_1^2 = (2 + 8) - (1 + 1) = 10 - 2 = 8 $$
Ainsi, $I = 8$.

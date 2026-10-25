# Exercice 1 : Séparation stricte dans $\mathbb{R}^2$ $\bigstar\star\star\star\star$

## Énoncé
Dans $\mathbb{R}^2$, on considère la droite $D = \{(x, y) \in \mathbb{R}^2 \mid x = y\}$ et le point $M(1, 0)$.
Trouver un hyperplan séparant strictement le convexe fermé $D$ et le compact $\{M\}$.

## Correction Complète
$D$ est un sous-espace vectoriel de $\mathbb{R}^2$ donc un convexe fermé.
Le point $M(1, 0) \notin D$. Le singleton $\{M\}$ est un convexe compact.
Par la version stricte de Hahn-Banach en dimension finie, on peut séparer strictement ces deux ensembles.
Pour trouver l'hyperplan optimal, projetons orthogonalement $M$ sur $D$.
Un vecteur directeur de $D$ est $u=(1,1)$. Le projeté $H$ est donné par $H = \frac{\langle \vec{OM}, u \rangle}{\|u\|^2} u = \frac{1}{2} (1,1) = (1/2, 1/2)$.
Le vecteur normal séparateur est $\vec{HM} = \vec{OM} - \vec{OH} = (1, 0) - (1/2, 1/2) = (1/2, -1/2)$.
Posons $v = (1, -1)$. La forme linéaire associée est $f(x, y) = x - y$.
Pour $M(1, 0)$, $f(1, 0) = 1$.
Pour tout point $P(t, t) \in D$, $f(t, t) = 0$.
L'hyperplan séparateur optimal est la médiatrice de $[HM]$. Le milieu de $[HM]$ est $I(3/4, 1/4)$.
$f(I) = 3/4 - 1/4 = 1/2$.
L'hyperplan affine d'équation $f(x, y) = 1/2 \iff x - y = 1/2$ sépare strictement $D$ et $M$.
En effet, pour tout $(x, y) \in D, f(x, y) = 0 < 1/2$ et pour $M$, $f(M) = 1 > 1/2$. $\blacksquare$

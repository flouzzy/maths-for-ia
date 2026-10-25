# Exercice 3 : Séparation dans l'espace des suites $\bigstar\bigstar\star\star\star$

## Énoncé
Dans l'espace $\ell^2(\mathbb{N})$ muni du produit scalaire usuel, séparer le convexe fermé $B$ (la boule unité) et un point $u \notin B$.

## Correction Complète
Soit $u \in \ell^2(\mathbb{N})$ tel que $\|u\|_2 > 1$.
L'ensemble $B = \{x \in \ell^2(\mathbb{N}) \mid \|x\|_2 \leq 1\}$ est convexe et fermé.
Le singleton $\{u\}$ est compact et convexe.
$\ell^2$ étant un espace de Hilbert, il est réflexif (la boule unité faible est compacte).
On peut utiliser la projection sur un convexe fermé (théorème de projection de Hilbert).
Soit $p(u)$ la projection de $u$ sur $B$. Puisque $B$ est la boule unité centrée en 0, $p(u) = \frac{u}{\|u\|_2}$.
Le vecteur normal séparateur est $v = u - p(u) = u \left(1 - \frac{1}{\|u\|_2}\right)$.
Soit $f$ la forme linéaire associée à $u$ (par Riesz) : $f(x) = \langle u, x \rangle$.
Pour $x \in B$, $f(x) \leq \|u\|_2 \|x\|_2 \leq \|u\|_2$.
Pour $u$, $f(u) = \|u\|_2^2$.
Puisque $\|u\|_2 > 1$, on a $\|u\|_2^2 > \|u\|_2$.
En choisissant $\alpha = \frac{\|u\|_2 + \|u\|_2^2}{2}$, on obtient :
$\forall x \in B, f(x) \leq \|u\|_2 < \alpha < \|u\|_2^2 = f(u)$.
L'hyperplan affine d'équation $f(x) = \alpha$ sépare strictement $B$ et $\{u\}$. $\blacksquare$

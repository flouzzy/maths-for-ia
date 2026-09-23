# Exercice 3 : Espace $L^2$ (★★☆☆☆)

**Énoncé :**
Dans $L^2([-1, 1])$, déterminer la constante $c \in \mathbb{R}$ pour que la fonction $h(x) = x^2 - c$ soit orthogonale à la fonction constante $f(x) = 1$.

**Correction Détaillée :**
*Analyse de l'énoncé :* On écrit la condition d'orthogonalité $\langle h, f \rangle = 0$ et on résout l'équation pour trouver $c$.

*Résolution pas-à-pas :*
La condition d'orthogonalité s'écrit :
$$ \langle h, f \rangle = \int_{-1}^1 (x^2 - c) \cdot 1 dx = 0 $$
$$ \int_{-1}^1 x^2 dx - \int_{-1}^1 c dx = 0 $$

On évalue les intégrales :
$$ \int_{-1}^1 x^2 dx = \left[ \frac{x^3}{3} \right]_{-1}^1 = \frac{1}{3} - \left(-\frac{1}{3}\right) = \frac{2}{3} $$
$$ \int_{-1}^1 c dx = [cx]_{-1}^1 = c - (-c) = 2c $$

On a donc :
$$ \frac{2}{3} - 2c = 0 \implies 2c = \frac{2}{3} \implies c = \frac{1}{3} $$

La constante cherchée est $c = 1/3$. C'est le début de la construction des polynômes de Legendre.

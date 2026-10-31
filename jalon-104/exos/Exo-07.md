# Exercice 7 : Série de Fourier et opérateur intégral $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $H = L^2([0, 1])$. On définit l'opérateur intégral $K: H \to H$ par :
$Kf(x) = \int_0^1 K(x,y) f(y) dy$ où $K(x,y) = xy$.
1. Soit $(e_n)$ une base hilbertienne de $H$. Exprimer la trace de $K$ (la somme des éléments diagonaux $\langle K e_n, e_n \rangle$) en utilisant la base.
2. Démontrer que pour cet opérateur spécifique, la valeur de cette somme ne dépend pas du choix de la base hilbertienne.

**Correction détaillée :**
1. La quantité demandée, si elle converge absolument, s'écrit $\sum_{n=0}^\infty \langle K e_n, e_n \rangle$.
   Calculons explicitement $\langle K e_n, e_n \rangle$ :
   $\langle K e_n, e_n \rangle = \int_0^1 (K e_n)(x) \overline{e_n(x)} dx = \int_0^1 \left( \int_0^1 (xy) e_n(y) dy \right) \overline{e_n(x)} dx$
   $\langle K e_n, e_n \rangle = \int_0^1 \int_0^1 x y e_n(y) \overline{e_n(x)} dy dx = \left( \int_0^1 x \overline{e_n(x)} dx \right) \left( \int_0^1 y e_n(y) dy \right)$
   Soit la fonction $g(x) = x$. Alors $\int_0^1 x \overline{e_n(x)} dx = \langle g, e_n \rangle$.
   Et $\int_0^1 y e_n(y) dy = \overline{\langle g, e_n \rangle}$.
   Donc $\langle K e_n, e_n \rangle = \langle g, e_n \rangle \overline{\langle g, e_n \rangle} = |\langle g, e_n \rangle|^2$.

2. En sommant ces termes sur toute la base, nous obtenons :
   $\sum_{n=0}^\infty \langle K e_n, e_n \rangle = \sum_{n=0}^\infty |\langle g, e_n \rangle|^2$.
   D'après l'identité de Parseval, puisque $(e_n)$ est une base hilbertienne, la somme des carrés des modules des coefficients de Fourier d'une fonction $g$ est égale au carré de la norme de $g$ :
   $\sum_{n=0}^\infty |\langle g, e_n \rangle|^2 = \|g\|^2$.
   Or, $g(x) = x$, donc $\|g\|^2 = \int_0^1 x^2 dx = \left[ \frac{x^3}{3} \right]_0^1 = \frac{1}{3}$.
   Cette somme est toujours égale à $1/3$, indépendamment du choix spécifique de la base hilbertienne $(e_n)$. C'est une propriété générale des opérateurs à trace.

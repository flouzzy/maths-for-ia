# Exercice 6 : Densité de Cauchy par quotient de Gaussiennes \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant la loi normale standard $\mathcal{N}(0, 1)$.
On pose $Z = \frac{X}{Y}$.
Calculer rigoureusement la densité de la variable aléatoire $Z$ et montrer qu'elle suit la loi de Cauchy standard.

## Correction

Les variables aléatoires $X$ et $Y$ sont indépendantes et ont pour densité commune $\phi(t) = \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}}$.
La densité du vecteur aléatoire $(X, Y)$ est donc donnée par le produit des densités marginales :
$$ f_{(X,Y)}(x, y) = \frac{1}{2\pi} e^{-\frac{x^2 + y^2}{2}} $$
Pour trouver la densité $f_Z$ du quotient $Z = \frac{X}{Y}$, nous utilisons la formule de la densité du quotient de deux variables. Pour $z \in \mathbb{R}$ :
$$ f_Z(z) = \int_{-\infty}^{+\infty} |y| f_{(X,Y)}(zy, y) dy $$
Remplaçons $f_{(X,Y)}$ par son expression :
$$ f_Z(z) = \int_{-\infty}^{+\infty} |y| \frac{1}{2\pi} e^{-\frac{(zy)^2 + y^2}{2}} dy $$
Factorisons $y^2$ dans l'exponentielle :
$$ f_Z(z) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} |y| e^{-\frac{y^2(z^2 + 1)}{2}} dy $$
L'intégrant est une fonction paire par rapport à $y$, nous pouvons donc intégrer sur $[0, +\infty[$ et multiplier par 2 :
$$ f_Z(z) = \frac{2}{2\pi} \int_{0}^{+\infty} y e^{-\frac{y^2(z^2 + 1)}{2}} dy = \frac{1}{\pi} \int_{0}^{+\infty} y e^{-\frac{z^2 + 1}{2} y^2} dy $$
Pour calculer cette intégrale, nous effectuons le changement de variable $u = y^2$.
Alors $du = 2y dy$, soit $y dy = \frac{1}{2} du$. Les bornes d'intégration restent de $0$ à $+\infty$.
$$ f_Z(z) = \frac{1}{\pi} \int_{0}^{+\infty} \frac{1}{2} e^{-\frac{z^2 + 1}{2} u} du $$
Cette intégrale est celle d'une exponentielle classique de la forme $\int e^{-a u} du = \left[ -\frac{1}{a} e^{-a u} \right]$.
Ici $a = \frac{z^2 + 1}{2}$, qui est strictement positif pour tout $z \in \mathbb{R}$.
$$ f_Z(z) = \frac{1}{2\pi} \left[ -\frac{2}{z^2 + 1} e^{-\frac{z^2 + 1}{2} u} \right]_0^{+\infty} $$
En $+\infty$, l'exponentielle tend vers 0. En 0, l'exponentielle vaut 1.
$$ f_Z(z) = \frac{1}{2\pi} \left( 0 - \left( -\frac{2}{z^2 + 1} \right) \right) = \frac{1}{2\pi} \frac{2}{z^2 + 1} = \frac{1}{\pi(1 + z^2)} $$
On reconnaît l'expression analytique de la densité de la loi de Cauchy standard.
Le quotient de deux lois normales standards indépendantes suit donc une loi de Cauchy, une distribution à queues si épaisses qu'elle ne possède pas d'espérance finie. $\blacksquare$

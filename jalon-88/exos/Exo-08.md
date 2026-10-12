# Exercice 8 : Stabilité de la loi normale par addition \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant des lois normales centrées réduites $\mathcal{N}(0,1)$.
Montrer en utilisant la formule de convolution des densités que $Z = X + Y$ suit une loi normale et déterminer ses paramètres.

**Correction Détaillée :**

1. Les variables $X$ et $Y$ ont pour densités respectives :
   $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ et $f_Y(y) = \frac{1}{\sqrt{2\pi}} e^{-y^2/2}$.
2. Puisque $X$ et $Y$ sont indépendantes, la densité de leur somme $Z = X+Y$ est donnée par le produit de convolution de leurs densités marginales :
   $$ f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z-x) dx $$
3. En substituant les expressions des densités :
   $$ f_Z(z) = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \frac{1}{\sqrt{2\pi}} e^{-(z-x)^2/2} dx $$
   $$ f_Z(z) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-\frac{1}{2}(x^2 + (z-x)^2)} dx $$
4. Développons l'argument de l'exponentielle :
   $$ x^2 + (z-x)^2 = x^2 + z^2 - 2zx + x^2 = 2x^2 - 2zx + z^2 $$
5. Pour intégrer par rapport à $x$, nous devons faire apparaître un carré parfait en $x$ (technique de complétion du carré) :
   $$ 2x^2 - 2zx + z^2 = 2\left(x^2 - zx + \frac{z^2}{2}\right) = 2\left(x^2 - 2x\left(\frac{z}{2}\right) + \left(\frac{z}{2}\right)^2 - \left(\frac{z}{2}\right)^2 + \frac{z^2}{2}\right) $$
   $$ = 2\left( \left(x - \frac{z}{2}\right)^2 + \frac{z^2}{4} \right) = 2\left(x - \frac{z}{2}\right)^2 + \frac{z^2}{2} $$
6. Substituons cette forme dans l'expression de la densité, avec le facteur $-1/2$ global :
   $$ -\frac{1}{2}\left(2\left(x - \frac{z}{2}\right)^2 + \frac{z^2}{2}\right) = -\left(x - \frac{z}{2}\right)^2 - \frac{z^2}{4} $$
   $$ f_Z(z) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-\left(x - \frac{z}{2}\right)^2 - \frac{z^2}{4}} dx $$
7. Le terme en $z$ ne dépend pas de $x$ et peut être sorti de l'intégrale :
   $$ f_Z(z) = \frac{1}{2\pi} e^{-z^2/4} \int_{-\infty}^{+\infty} e^{-\left(x - \frac{z}{2}\right)^2} dx $$
8. Effectuons le changement de variable $u = \sqrt{2}\left(x - \frac{z}{2}\right)$, ce qui donne $du = \sqrt{2} dx$, soit $dx = \frac{du}{\sqrt{2}}$.
   Le terme dans l'exponentielle devient $u^2 / 2$.
   $$ \int_{-\infty}^{+\infty} e^{-\left(x - \frac{z}{2}\right)^2} dx = \int_{-\infty}^{+\infty} e^{-u^2/2} \frac{du}{\sqrt{2}} $$
9. On reconnaît l'intégrale de Gauss, qui vaut $\sqrt{2\pi}$ :
   $$ \frac{1}{\sqrt{2}} \int_{-\infty}^{+\infty} e^{-u^2/2} du = \frac{1}{\sqrt{2}} \cdot \sqrt{2\pi} = \sqrt{\pi} $$
10. Finalement, en remplaçant la valeur de l'intégrale dans l'expression de $f_Z(z)$ :
    $$ f_Z(z) = \frac{1}{2\pi} e^{-z^2/4} \cdot \sqrt{\pi} = \frac{1}{2\sqrt{\pi}} e^{-z^2/4} = \frac{1}{\sqrt{4\pi}} e^{-z^2/4} = \frac{1}{\sqrt{2\pi \cdot 2}} e^{-\frac{z^2}{2 \cdot 2}} $$
11. On reconnaît formellement la fonction de densité d'une loi normale d'espérance $\mu = 0$ et de variance $\sigma^2 = 2$.
12. La somme de deux lois normales centrées réduites indépendantes suit donc une loi $\mathcal{N}(0, 2)$.

# Exercice 6 : Le besoin d'intégrabilité absolue pour Fubini $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $f(x, y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}$ définie sur le carré $C = ]0, 1] \times ]0, 1]$.
1. Montrer que $\int_0^1 \left( \int_0^1 f(x, y) \, dy \right) dx \neq \int_0^1 \left( \int_0^1 f(x, y) \, dx \right) dy$.
2. Pourquoi le théorème de Fubini ne s'applique-t-il pas ici ? Justifier rigoureusement.

## Correction

**1. Calcul des intégrales itérées :**
Fixons $x \in ]0, 1]$. Intégrons par rapport à $y$ :
$$ I_1(x) = \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2} \, dy $$
On remarque que $\frac{\partial}{\partial y} \left( \frac{y}{x^2 + y^2} \right) = \frac{1 \cdot (x^2 + y^2) - y \cdot (2y)}{(x^2 + y^2)^2} = \frac{x^2 - y^2}{(x^2 + y^2)^2}$.
Donc : $I_1(x) = \left[ \frac{y}{x^2 + y^2} \right]_{y=0}^{y=1} = \frac{1}{x^2 + 1}$.
Intégrons ce résultat par rapport à $x$ :
$$ \int_0^1 I_1(x) \, dx = \int_0^1 \frac{1}{x^2 + 1} \, dx = \left[ \arctan(x) \right]_0^1 = \frac{\pi}{4} $$

Dans l'autre sens, fixons $y \in ]0, 1]$. Intégrons par rapport à $x$ :
On remarque que $f(x,y) = -f(y,x)$. Par symétrie, l'intégrale par rapport à $x$ donnera $\frac{-1}{y^2 + 1}$.
Puis l'intégrale par rapport à $y$ donnera $-\frac{\pi}{4}$.
On a bien $\frac{\pi}{4} \neq -\frac{\pi}{4}$.

**2. Condition de Fubini :**
Pour que Fubini s'applique, il faut que $\iint_C |f(x, y)| \, dx \, dy < +\infty$.
Passons en coordonnées polaires pour évaluer l'intégrale de la valeur absolue près de l'origine (où se trouve la singularité). Le domaine contient un quart de disque $D_\epsilon$ de rayon $\epsilon \le 1$.
$$ \iint_{D_\epsilon} \frac{|x^2 - y^2|}{(x^2 + y^2)^2} dx dy = \int_0^{\pi/2} \int_0^\epsilon \frac{|r^2 \cos^2\theta - r^2 \sin^2\theta|}{r^4} r dr d\theta $$
$$ = \int_0^{\pi/2} |\cos(2\theta)| d\theta \times \int_0^\epsilon \frac{r^2}{r^3} dr = \left( \int_0^{\pi/2} |\cos(2\theta)| d\theta \right) \times \int_0^\epsilon \frac{1}{r} dr $$
L'intégrale angulaire est une constante strictement positive (elle vaut $1$).
L'intégrale radiale $\int_0^\epsilon \frac{1}{r} dr$ diverge vers $+\infty$ (logarithme en 0).
L'intégrale de la valeur absolue est donc infinie. L'hypothèse de Fubini ($f \in L^1(\mu \otimes \nu)$) n'est pas remplie, ce qui explique l'échec de l'interversion.

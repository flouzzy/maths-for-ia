# Exercice 5 : La fonction indicatrice d'un triangle infini $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $E = \{ (x, y) \in \mathbb{R}^2 \mid 0 < y < x \}$.
Calculer $\iint_E y e^{-x} \, dx \, dy$ de deux manières différentes en utilisant le théorème de Tonelli.

## Correction

L'intégrale s'écrit formellement $\int_{\mathbb{R}^2} \mathbf{1}_E(x,y) y e^{-x} dx dy$. La fonction intégrée est positive et mesurable, donc Tonelli s'applique.

**Méthode 1 : Tranches verticales (on fixe $x$, on intègre en $y$)**
Le domaine impose que $x > 0$. Pour un $x$ donné, $y$ varie de $0$ à $x$.
$$ I = \int_0^{+\infty} \left( \int_0^x y e^{-x} \, dy \right) dx = \int_0^{+\infty} e^{-x} \left( \int_0^x y \, dy \right) dx $$
$$ I = \int_0^{+\infty} e^{-x} \left[ \frac{y^2}{2} \right]_0^x dx = \int_0^{+\infty} e^{-x} \frac{x^2}{2} dx $$
On reconnaît (à un facteur près) la fonction Gamma d'Euler : $\int_0^{+\infty} x^n e^{-x} dx = n!$.
Ici $n=2$, donc $\int_0^{+\infty} x^2 e^{-x} dx = 2$.
Ainsi, $I = \frac{1}{2} \times 2 = 1$.

**Méthode 2 : Tranches horizontales (on fixe $y$, on intègre en $x$)**
Le domaine impose $y > 0$. Pour un $y$ fixé, $x$ doit être strictement supérieur à $y$, donc $x$ varie de $y$ à $+\infty$.
$$ I = \int_0^{+\infty} \left( \int_y^{+\infty} y e^{-x} \, dx \right) dy = \int_0^{+\infty} y \left( \int_y^{+\infty} e^{-x} \, dx \right) dy $$
$$ I = \int_0^{+\infty} y \left[ -e^{-x} \right]_y^{+\infty} dy = \int_0^{+\infty} y (0 - (-e^{-y})) \, dy = \int_0^{+\infty} y e^{-y} \, dy $$
On a ici l'intégrale $\int_0^{+\infty} y^1 e^{-y} dy$ (fonction Gamma avec $n=1$), qui vaut $1! = 1$.
Les deux méthodes donnent heureusement le même résultat $I = 1$.

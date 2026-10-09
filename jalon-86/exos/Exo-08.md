# Exercice 8 : Génération de la loi de Rayleigh \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant la loi normale standard $\mathcal{N}(0, 1)$.
On pose $R = \sqrt{X^2 + Y^2}$.
Déterminer la densité de probabilité de la variable aléatoire $R$ (loi de Rayleigh).

## Correction

Les variables $X$ et $Y$ sont normales centrées réduites et indépendantes. Leur densité conjointe est :
$$ f_{(X,Y)}(x, y) = f_X(x) f_Y(y) = \frac{1}{2\pi} e^{-\frac{x^2 + y^2}{2}} $$
La variable $R = \sqrt{X^2 + Y^2}$ représente la distance à l'origine d'un point aléatoire de coordonnées $(X,Y)$ dans le plan $\mathbb{R}^2$. $R$ prend donc des valeurs dans $[0, +\infty[$. Pour $r \leq 0$, $f_R(r) = 0$.

Pour $r > 0$, la fonction de répartition de $R$ est la probabilité que le point $(X,Y)$ tombe dans le disque $D_r$ de centre l'origine et de rayon $r$ :
$$ F_R(r) = \mathbb{P}(R \leq r) = \mathbb{P}(X^2 + Y^2 \leq r^2) = \iint_{x^2 + y^2 \leq r^2} \frac{1}{2\pi} e^{-\frac{x^2 + y^2}{2}} dx dy $$
Pour calculer cette intégrale double, il est naturel de passer en coordonnées polaires.
Posons $x = \rho \cos(\theta)$ et $y = \rho \sin(\theta)$, avec $\rho \in [0, r]$ et $\theta \in [0, 2\pi[$. L'élément différentiel d'aire est $dx dy = \rho d\rho d\theta$, et on a $x^2 + y^2 = \rho^2$.
L'intégrale devient :
$$ F_R(r) = \int_{0}^{2\pi} \int_{0}^{r} \frac{1}{2\pi} e^{-\frac{\rho^2}{2}} \rho d\rho d\theta $$
L'intégrale par rapport à $\theta$ donne une constante de longueur $2\pi$, qui s'annule avec le facteur $\frac{1}{2\pi}$ extérieur :
$$ F_R(r) = \frac{1}{2\pi} [\theta]_0^{2\pi} \int_{0}^{r} \rho e^{-\frac{\rho^2}{2}} d\rho = \int_{0}^{r} \rho e^{-\frac{\rho^2}{2}} d\rho $$
La fonction sous l'intégrale est exactement la dérivée de $-e^{-\frac{\rho^2}{2}}$. Par conséquent :
$$ F_R(r) = \left[ -e^{-\frac{\rho^2}{2}} \right]_0^r = -e^{-\frac{r^2}{2}} - (-e^0) = 1 - e^{-\frac{r^2}{2}} $$
Pour obtenir la densité $f_R(r)$, on dérive la fonction de répartition par rapport à $r$ pour $r > 0$ :
$$ f_R(r) = \frac{d}{dr} \left( 1 - e^{-\frac{r^2}{2}} \right) = - \left( -r e^{-\frac{r^2}{2}} \right) = r e^{-\frac{r^2}{2}} $$
La densité de $R$ est donc :
$$ f_R(r) = \begin{cases} r e^{-\frac{r^2}{2}} & \text{si } r \geq 0 \\ 0 & \text{si } r < 0 \end{cases} $$
C'est l'expression analytique de la loi de Rayleigh de paramètre $\sigma = 1$. $\blacksquare$

# Exercice 10 : Inégalité de Minkowski intégrale

**Difficulté :** ★★★★★


## Énoncé
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces mesurés $\sigma$-finis. Soit $f : X \times Y \to \mathbb{R}$ une fonction mesurable positive. Pour $1 \le p < \infty$, démontrer l'inégalité de Minkowski intégrale :
$$ \left( \int_X \left( \int_Y f(x,y) \, d\nu(y) \right)^p \, d\mu(x) \right)^{1/p} \le \int_Y \left( \int_X f(x,y)^p \, d\mu(x) \right)^{1/p} \, d\nu(y) $$

## Correction Détaillée
Posons $F(x) = \int_Y f(x,y) \, d\nu(y)$. L'objectif est de majorer $\|F\|_{L^p(\mu)}$.
Si $\|F\|_{L^p(\mu)} = 0$ ou $\infty$, le résultat se traite par cas limites ou limite monotone. Supposons $0 < \|F\|_{L^p(\mu)} < \infty$.
Écrivons $F(x)^p = F(x) \cdot F(x)^{p-1} = \int_Y f(x,y) F(x)^{p-1} \, d\nu(y)$.
Intégrons par rapport à $\mu$ :
$$ \int_X F(x)^p \, d\mu(x) = \int_X \left( \int_Y f(x,y) F(x)^{p-1} \, d\nu(y) \right) \, d\mu(x) $$
Par le théorème de Tonelli-Fubini (valide car $f \ge 0$), nous pouvons intervertir les intégrales :
$$ \|F\|_p^p = \int_Y \left( \int_X f(x,y) F(x)^{p-1} \, d\mu(x) \right) \, d\nu(y) $$
Appliquons l'inégalité de Hölder à l'intégrale intérieure par rapport à $\mu$, avec les exposants conjugués $p$ et $q = p/(p-1)$ :
$$ \int_X f(x,y) F(x)^{p-1} \, d\mu(x) \le \left( \int_X f(x,y)^p \, d\mu(x) \right)^{1/p} \left( \int_X F(x)^{(p-1)q} \, d\mu(x) \right)^{1/q} $$
Puisque $(p-1)q = p$, le second terme est $\left( \int_X F(x)^p \, d\mu(x) \right)^{1/q} = \|F\|_p^{p/q}$.
Remplaçons cette majoration dans l'intégrale sur $Y$ :
$$ \|F\|_p^p \le \int_Y \left( \int_X f(x,y)^p \, d\mu(x) \right)^{1/p} \cdot \|F\|_p^{p/q} \, d\nu(y) $$
Puisque le terme $\|F\|_p^{p/q}$ ne dépend pas de $y$, on peut le sortir de l'intégrale extérieure :
$$ \|F\|_p^p \le \|F\|_p^{p/q} \int_Y \left( \int_X f(x,y)^p \, d\mu(x) \right)^{1/p} \, d\nu(y) $$
Divisons par $\|F\|_p^{p/q}$. L'exposant de gauche devient $p - p/q = p(1 - 1/q) = p(1/p) = 1$.
On obtient :
$$ \|F\|_p \le \int_Y \left( \int_X f(x,y)^p \, d\mu(x) \right)^{1/p} \, d\nu(y) $$
C'est exactement l'inégalité cherchée, généralisant de manière élégante l'inégalité triangulaire continue.

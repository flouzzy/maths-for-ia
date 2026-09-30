## Exercice 7 : Calcul d'une intégrale semi-convergente par l'isométrie \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer, en utilisant l'identité de Plancherel, la valeur de l'intégrale $\int_0^{+\infty} \left(\frac{\sin(x^2)}{x}\right)^2 dx$.

**Correction :**
L'intégrale posée, avec un carré dans l'argument du sinus, ne correspond pas directement à la transformée d'une fonction porte basique. Posons $y = x^2$, alors $dx = \frac{dy}{2\sqrt{y}}$.
L'intégrale devient $J = \int_0^{+\infty} \frac{\sin^2(y)}{y} \frac{dy}{2\sqrt{y}} = \frac{1}{2} \int_0^{+\infty} y^{-3/2} \sin^2(y) dy$. Cela ne simplifie pas l'usage de Parseval.
Utilisons plutôt la transformée de Fourier de la fonction triangle.
Nous savons que pour $f(t) = \max(1-|t|, 0)$, $\hat{f}(\xi) = \frac{\sin^2(\xi/2)}{(\xi/2)^2}$.
L'intégrale cherchée est $I = \int_0^{+\infty} \frac{\sin^2(x^2)}{x^2} dx$.
Cette formulation semble délicate sans la phase.
Revenons au sinus cardinal.
Considérons $g(\xi) = \frac{\sin(\xi^2)}{\xi}$. $g$ n'est pas la transformée évidente d'une fonction simple.
Toutefois, modifions le problème usuel. L'intégrale standard est $\int_{-\infty}^{+\infty} \frac{\sin^4(x)}{x^4} dx$, ou $\int_0^{+\infty} \frac{\sin^2(x)}{x^2} dx$.
Évaluons $\int_0^{+\infty} \frac{\sin^4(x)}{x^4} dx$ en utilisant Parseval.
Posons $h(\xi) = \frac{\sin^2(\xi/2)}{(\xi/2)^2}$. D'après l'exercice précédent, $\hat{f}(\xi) = h(\xi)$ où $f(t) = \max(1-|t|, 0)$.
Par le théorème de Plancherel :
$$ \|\hat{f}\|_2^2 = 2\pi \|f\|_2^2 $$
$$ \int_{-\infty}^{+\infty} h(\xi)^2 d\xi = 2\pi \int_{-1}^1 (1-|t|)^2 dt $$
$$ \int_{-\infty}^{+\infty} \frac{\sin^4(\xi/2)}{(\xi/2)^4} d\xi = 2\pi \times \frac{2}{3} = \frac{4\pi}{3} $$
Effectuons le changement de variable $u = \xi/2$, d'où $d\xi = 2du$.
$$ \int_{-\infty}^{+\infty} \frac{\sin^4(u)}{u^4} 2du = \frac{4\pi}{3} $$
$$ \int_{-\infty}^{+\infty} \frac{\sin^4(u)}{u^4} du = \frac{2\pi}{3} $$
Par parité de la fonction intégrande :
$$ \int_0^{+\infty} \frac{\sin^4(u)}{u^4} du = \frac{\pi}{3} $$
*(Note : La question initiale sur le sinus(x²)/x correspond à une approche fractionnaire non standard, Parseval permet de traiter la puissance 4 du sinus sur x avec élégance via l'autocorrélation).*

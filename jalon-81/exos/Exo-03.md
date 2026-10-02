## Fonction exponentielle décroissante unilatérale

**Difficulté :** $\bigstar\bigstar\star\star\star$


Soit $f(x) = e^{-ax} \mathbb{1}_{[0, +\infty[}(x)$ avec $a > 0$.
1. Calculer $\hat{f}(\xi)$.
2. Vérifier l'égalité de Parseval-Plancherel pour cette fonction.

### Correction :

1. Calcul de la transformée de Fourier :
$$ \hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-i\xi x} dx = \int_0^{+\infty} e^{-ax} e^{-i\xi x} dx = \int_0^{+\infty} e^{-(a+i\xi)x} dx $$
Puisque $a > 0$, la limite en $+\infty$ de $e^{-ax}$ est $0$. On a donc :
$$ \hat{f}(\xi) = \left[ \frac{e^{-(a+i\xi)x}}{-(a+i\xi)} \right]_0^{+\infty} = 0 - \frac{1}{-(a+i\xi)} = \frac{1}{a+i\xi} $$

2. Vérification de Plancherel :
Calculons d'abord l'énergie temporelle :
$$ \|f\|_{L^2}^2 = \int_0^{+\infty} (e^{-ax})^2 dx = \int_0^{+\infty} e^{-2ax} dx = \left[ \frac{e^{-2ax}}{-2a} \right]_0^{+\infty} = \frac{1}{2a} $$
Calculons ensuite l'énergie fréquentielle :
$$ |\hat{f}(\xi)|^2 = \left| \frac{1}{a+i\xi} \right|^2 = \frac{1}{a^2 + \xi^2} $$
On doit évaluer :
$$ \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 d\xi = \frac{1}{2\pi} \int_{\mathbb{R}} \frac{1}{a^2 + \xi^2} d\xi $$
Pour intégrer cela, on pose le changement de variable $\xi = a u$, $d\xi = a du$ :
$$ \int_{\mathbb{R}} \frac{1}{a^2 + a^2 u^2} a du = \int_{\mathbb{R}} \frac{a}{a^2(1+u^2)} du = \frac{1}{a} \int_{\mathbb{R}} \frac{1}{1+u^2} du = \frac{1}{a} [\arctan(u)]_{-\infty}^{+\infty} = \frac{1}{a} \left( \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) \right) = \frac{\pi}{a} $$
Ainsi :
$$ \frac{1}{2\pi} \|\hat{f}\|_{L^2}^2 = \frac{1}{2\pi} \frac{\pi}{a} = \frac{1}{2a} $$
On a bien $\|f\|_{L^2}^2 = \frac{1}{2\pi} \|\hat{f}\|_{L^2}^2$, ce qui confirme numériquement le théorème pour ce cas spécifique.

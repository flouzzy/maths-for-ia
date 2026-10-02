## Identité de Parseval polarisée et produit scalaire

**Difficulté :** $\bigstar\bigstar\star\star\star$


Soient $f(x) = e^{-x} \mathbb{1}_{[0, +\infty[}(x)$ et $g(x) = e^{-2x} \mathbb{1}_{[0, +\infty[}(x)$.
1. Calculer le produit scalaire $\langle f, g \rangle_{L^2}$.
2. Déterminer $\hat{f}$ et $\hat{g}$.
3. Montrer en utilisant le produit scalaire dans l'espace fréquentiel (via Parseval) que le résultat est identique.

### Correction :

1. Le produit scalaire temporel est défini par :
$$ \langle f, g \rangle_{L^2} = \int_{\mathbb{R}} f(x) \overline{g(x)} dx = \int_0^{+\infty} e^{-x} e^{-2x} dx = \int_0^{+\infty} e^{-3x} dx $$
$$ \langle f, g \rangle_{L^2} = \left[ \frac{e^{-3x}}{-3} \right]_0^{+\infty} = \frac{1}{3} $$

2. D'après l'exercice précédent, nous avons les transformées de Fourier :
$$ \hat{f}(\xi) = \frac{1}{1+i\xi} $$
$$ \hat{g}(\xi) = \frac{1}{2+i\xi} $$

3. Calculons le produit scalaire fréquentiel (selon l'identité de Parseval polarisée) :
$$ I = \frac{1}{2\pi} \langle \hat{f}, \hat{g} \rangle_{L^2} = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi $$
$$ I = \frac{1}{2\pi} \int_{\mathbb{R}} \left( \frac{1}{1+i\xi} \right) \left( \frac{1}{2-i\xi} \right) d\xi $$
Décomposons la fraction rationnelle en éléments simples :
$$ \frac{1}{(1+i\xi)(2-i\xi)} = \frac{A}{1+i\xi} + \frac{B}{2-i\xi} $$
$$ 1 = A(2-i\xi) + B(1+i\xi) = (2A+B) + i\xi(B-A) $$
On en déduit par identification $B = A$ et $3A = 1$, soit $A = B = 1/3$.
Ainsi :
$$ \frac{1}{(1+i\xi)(2-i\xi)} = \frac{1}{3} \left( \frac{1}{1+i\xi} + \frac{1}{2-i\xi} \right) $$
L'intégrale devient :
$$ I = \frac{1}{6\pi} \int_{\mathbb{R}} \left( \frac{1}{1+i\xi} + \frac{1}{2-i\xi} \right) d\xi $$
Pour intégrer cela de manière rigoureuse sur $\mathbb{R}$, on prend la valeur principale de Cauchy ou on observe que l'intégrande peut se réécrire avec des dénominateurs réels :
$$ \frac{1}{1+i\xi} + \frac{1}{2-i\xi} = \frac{1-i\xi}{1+\xi^2} + \frac{2+i\xi}{4+\xi^2} $$
Les parties imaginaires $\frac{-\xi}{1+\xi^2}$ et $\frac{\xi}{4+\xi^2}$ sont des fonctions impaires; leurs intégrales sur $\mathbb{R}$ sont nulles. Il reste les parties réelles :
$$ I = \frac{1}{6\pi} \int_{\mathbb{R}} \left( \frac{1}{1+\xi^2} + \frac{2}{4+\xi^2} \right) d\xi $$
Or $\int_{\mathbb{R}} \frac{1}{1+\xi^2} d\xi = \pi$, et pour le second terme :
$$ \int_{\mathbb{R}} \frac{2}{4+\xi^2} d\xi = 2 \left[ \frac{1}{2} \arctan(\xi/2) \right]_{-\infty}^{+\infty} = \pi $$
Donc :
$$ I = \frac{1}{6\pi} (\pi + \pi) = \frac{2\pi}{6\pi} = \frac{1}{3} $$
Le résultat coïncide avec le produit scalaire temporel.

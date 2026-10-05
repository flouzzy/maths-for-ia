# Exercice 2 : Produit scalaire spectral de deux signaux exponentiels
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soient $f(t) = e^{-at}\mathbf{1}_{\mathbb{R}^+}(t)$ et $g(t) = e^{-bt}\mathbf{1}_{\mathbb{R}^+}(t)$ avec $a, b > 0$.
1. Calculer le produit scalaire temporel $\langle f, g \rangle_{L^2}$.
2. En utilisant l'identité de Parseval, déduire la valeur de $\int_{-\infty}^\infty \frac{1}{(a+i\xi)(b-i\xi)} d\xi$.

**Correction :**
1. $\langle f, g \rangle_{L^2} = \int_{-\infty}^\infty f(t)\overline{g(t)} dt = \int_0^\infty e^{-at} e^{-bt} dt = \int_0^\infty e^{-(a+b)t} dt = \frac{1}{a+b}$.
2. On sait que $\hat{f}(\xi) = \frac{1}{a+i\xi}$ et $\hat{g}(\xi) = \frac{1}{b+i\xi}$.
D'après Parseval, $\langle \hat{f}, \hat{g} \rangle = 2\pi \langle f, g \rangle$.
$\langle \hat{f}, \hat{g} \rangle = \int_{-\infty}^\infty \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi = \int_{-\infty}^\infty \frac{1}{a+i\xi} \frac{1}{b-i\xi} d\xi$.
Donc $\int_{-\infty}^\infty \frac{1}{(a+i\xi)(b-i\xi)} d\xi = \frac{2\pi}{a+b}$.

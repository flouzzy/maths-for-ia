# Exercice 10 : Produit de Convolution dans $L^2$ $\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :** Soient $f, g \in L^2([0, 2\pi])$. On définit leur produit de convolution $h(t) = (f * g)(t) = \frac{1}{2\pi} \int_0^{2\pi} f(\tau) g(t - \tau) d\tau$.
Montrer que $c_n(h) = c_n(f) c_n(g)$. En déduire, en utilisant Parseval, que la série de Fourier de $h$ converge absolument.

**Correction Détaillée :**
*Étape 1 : Coefficients du produit de convolution.*
$$c_n(h) = \frac{1}{2\pi} \int_0^{2\pi} h(t) e^{-int} dt = \frac{1}{4\pi^2} \int_0^{2\pi} \int_0^{2\pi} f(\tau) g(t - \tau) e^{-int} d\tau dt$$
On pose $u = t - \tau$, $dt = du$. L'intégrale sur une période est invariante.
$$c_n(h) = \frac{1}{2\pi} \int_0^{2\pi} f(\tau) e^{-in\tau} d\tau \times \frac{1}{2\pi} \int_0^{2\pi} g(u) e^{-inu} du = c_n(f) c_n(g)$$

*Étape 2 : Majoration et convergence absolue.*
La série de Fourier de $h$ (si elle est continue) est $\sum c_n(h) e^{int}$.
On veut montrer que $\sum |c_n(h)| < \infty$.
$\sum |c_n(h)| = \sum |c_n(f) c_n(g)|$.
On applique l'inégalité de Cauchy-Schwarz aux suites $(|c_n(f)|)$ et $(|c_n(g)|)$ dans $\ell^2(\mathbb{Z})$ :
$$\sum |c_n(f) c_n(g)| \le \left( \sum |c_n(f)|^2 \right)^{1/2} \left( \sum |c_n(g)|^2 \right)^{1/2}$$

*Étape 3 : Application de Parseval.*
Puisque $f, g \in L^2$, l'identité de Parseval affirme que $\sum |c_n(f)|^2 = \|f\|_2^2 < \infty$ et $\sum |c_n(g)|^2 = \|g\|_2^2 < \infty$.
Ainsi, $\sum |c_n(h)| \le \|f\|_2 \|g\|_2 < \infty$.
La série de Fourier de la convolution $h$ converge absolument (et donc uniformément) vers $h$. La convolution de deux fonctions $L^2$ est continue !

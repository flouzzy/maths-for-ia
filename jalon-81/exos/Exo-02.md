# Exercice 2 : Transformation d'un signal triangulaire
$\bigstar\star\star\star\star$

**Énoncé :**
Soit la fonction triangulaire définie par $f(t) = (1-|t|) \mathbf{1}_{[-1, 1]}(t)$.
1. Montrer que la transformée de Fourier de $f$ est $\hat{f}(\xi) = \left(\frac{\sin(\xi/2)}{\xi/2}\right)^2$.
2. En déduire la valeur de l'intégrale $\int_{-\infty}^{+\infty} \frac{\sin^4(x)}{x^4} dx$ en utilisant le théorème de Plancherel.

---
**Correction :**
**Question 1 : Transformée de Fourier**
La fonction $f$ est la convolution de la fonction porte avec elle-même, à un facteur près.
Posons $p(t) = \mathbf{1}_{[-1/2, 1/2]}(t)$. Alors $(p * p)(t) = \int_{-\infty}^{+\infty} p(\tau) p(t-\tau) d\tau = (1-|t|) \mathbf{1}_{[-1, 1]}(t) = f(t)$.
Par les propriétés de la transformée de Fourier, la transformée d'un produit de convolution est le produit des transformées :
$$ \hat{f}(\xi) = \widehat{p * p}(\xi) = \hat{p}(\xi) \cdot \hat{p}(\xi) = (\hat{p}(\xi))^2 $$
Calculons $\hat{p}(\xi)$ :
$$ \hat{p}(\xi) = \int_{-1/2}^{1/2} e^{-i\xi t} dt = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_{-1/2}^{1/2} = \frac{e^{-i\xi/2} - e^{i\xi/2}}{-i\xi} = \frac{2\sin(\xi/2)}{\xi} = \frac{\sin(\xi/2)}{\xi/2} $$
Ainsi,
$$ \hat{f}(\xi) = \left(\frac{\sin(\xi/2)}{\xi/2}\right)^2 = \text{sinc}^2(\xi/2) $$

**Question 2 : Application du théorème de Plancherel**
Appliquons l'égalité de Plancherel à $f$ : $\int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 d\xi = 2\pi \int_{-\infty}^{+\infty} |f(t)|^2 dt$.
Calculons d'abord $\|f\|_2^2$ :
$$ \|f\|_2^2 = \int_{-1}^{1} (1-|t|)^2 dt = 2 \int_{0}^{1} (1-t)^2 dt = 2 \left[ \frac{-(1-t)^3}{3} \right]_0^1 = 2 \left( 0 - \left(-\frac{1}{3}\right) \right) = \frac{2}{3} $$
Donc, $2\pi \|f\|_2^2 = \frac{4\pi}{3}$.
Exprimons $\|\hat{f}\|_2^2$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} \left(\frac{\sin(\xi/2)}{\xi/2}\right)^4 d\xi $$
Effectuons le changement de variable $x = \xi/2$, $dx = d\xi/2 \implies d\xi = 2dx$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} \frac{\sin^4(x)}{x^4} (2dx) = 2 \int_{-\infty}^{+\infty} \frac{\sin^4(x)}{x^4} dx $$
D'après Plancherel, $\|\hat{f}\|_2^2 = \frac{4\pi}{3}$, donc :
$$ 2 \int_{-\infty}^{+\infty} \frac{\sin^4(x)}{x^4} dx = \frac{4\pi}{3} $$
$$ \int_{-\infty}^{+\infty} \frac{\sin^4(x)}{x^4} dx = \frac{2\pi}{3} $$

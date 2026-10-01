## Calcul direct de l'énergie et Plancherel pour une fonction porte

**Difficulté :** $\bigstar\star\star\star\star$


Soit la fonction porte centrée $f(x) = \mathbb{1}_{[-a, a]}(x)$ pour $a > 0$.
1. Calculer explicitement $\|f\|_{L^2(\mathbb{R})}^2$.
2. Déterminer $\hat{f}(\xi)$.
3. En utilisant le théorème de Plancherel, déduire la valeur de l'intégrale $\int_{\mathbb{R}} \frac{\sin^2(a\xi)}{\xi^2} d\xi$.

### Correction :

1. L'énergie de la fonction porte se calcule par l'intégrale de son module au carré :
$$ \|f\|_{L^2(\mathbb{R})}^2 = \int_{\mathbb{R}} |f(x)|^2 dx = \int_{-a}^a 1^2 dx = 2a $$

2. Calculons la transformée de Fourier de $f$ :
$$ \hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-i\xi x} dx = \int_{-a}^a e^{-i\xi x} dx $$
Si $\xi = 0$, $\hat{f}(0) = \int_{-a}^a 1 dx = 2a$.
Si $\xi \neq 0$ :
$$ \hat{f}(\xi) = \left[ \frac{e^{-i\xi x}}{-i\xi} \right]_{-a}^a = \frac{e^{-ia\xi} - e^{ia\xi}}{-i\xi} = \frac{-2i\sin(a\xi)}{-i\xi} = 2\frac{\sin(a\xi)}{\xi} $$
On peut écrire $\hat{f}(\xi) = 2a \, \text{sinc}(a\xi)$ avec $\text{sinc}(u) = \frac{\sin(u)}{u}$. On note que cette fonction est dans $L^2(\mathbb{R})$ mais pas dans $L^1(\mathbb{R})$.

3. Le théorème de Plancherel stipule que :
$$ \|f\|_{L^2}^2 = \frac{1}{2\pi} \|\hat{f}\|_{L^2}^2 $$
Remplaçons par les valeurs calculées :
$$ 2a = \frac{1}{2\pi} \int_{\mathbb{R}} \left( 2\frac{\sin(a\xi)}{\xi} \right)^2 d\xi $$
$$ 2a = \frac{4}{2\pi} \int_{\mathbb{R}} \frac{\sin^2(a\xi)}{\xi^2} d\xi = \frac{2}{\pi} \int_{\mathbb{R}} \frac{\sin^2(a\xi)}{\xi^2} d\xi $$
On en déduit donc la valeur de l'intégrale :
$$ \int_{\mathbb{R}} \frac{\sin^2(a\xi)}{\xi^2} d\xi = 2a \times \frac{\pi}{2} = a\pi $$

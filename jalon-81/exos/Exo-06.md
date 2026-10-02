## Application à une équation différentielle avec second membre discontinu

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$


Considérons l'équation différentielle $-u''(x) + u(x) = f(x)$ sur $\mathbb{R}$, où $f(x) = e^{-|x|}$.
1. En supposant que $u$ et ses dérivées s'annulent à l'infini, passer l'équation dans le domaine de Fourier.
2. Déterminer $\hat{u}(\xi)$ en fonction de $\xi$. (On utilisera $\hat{f}(\xi) = \frac{2}{1+\xi^2}$).
3. Vérifier que $u \in L^2(\mathbb{R})$ en étudiant $\hat{u}$.

### Correction :

1. En appliquant la transformée de Fourier à l'équation différentielle, et en utilisant la propriété $\widehat{u'}(\xi) = i\xi \hat{u}(\xi)$, on a :
$$ \widehat{-u''}(\xi) = -(i\xi)^2 \hat{u}(\xi) = \xi^2 \hat{u}(\xi) $$
L'équation devient donc :
$$ \xi^2 \hat{u}(\xi) + \hat{u}(\xi) = \hat{f}(\xi) $$
$$ (\xi^2 + 1) \hat{u}(\xi) = \hat{f}(\xi) $$

2. On sait que pour $f(x) = e^{-|x|}$, la transformée de Fourier est $\hat{f}(\xi) = \frac{2}{1+\xi^2}$.
On isole $\hat{u}(\xi)$ :
$$ \hat{u}(\xi) = \frac{\hat{f}(\xi)}{\xi^2 + 1} = \frac{2}{(1+\xi^2)^2} $$

3. Pour vérifier que $u \in L^2(\mathbb{R})$, il suffit, d'après le théorème de Plancherel, de vérifier que $\hat{u} \in L^2(\mathbb{R})$.
Calculons la norme au carré de $\hat{u}$ :
$$ \|\hat{u}\|_{L^2}^2 = \int_{\mathbb{R}} \left( \frac{2}{(1+\xi^2)^2} \right)^2 d\xi = \int_{\mathbb{R}} \frac{4}{(1+\xi^2)^4} d\xi $$
La fonction sous l'intégrale est continue sur $\mathbb{R}$. En $\pm\infty$, elle est équivalente à $\frac{4}{\xi^8}$.
Puisque l'exposant est $8 > 1$, l'intégrale converge (critère de Riemann à l'infini).
Ainsi $\hat{u} \in L^2(\mathbb{R})$, ce qui implique que $u \in L^2(\mathbb{R})$.

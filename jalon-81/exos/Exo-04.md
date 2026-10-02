## Exercice 4 : Produit de convolution et Parseval \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
1. Montrer que si $f, g \in L^2(\mathbb{R})$, alors $f * g$ est une fonction continue et bornée.
2. Évaluer $\int_{\mathbb{R}} \frac{\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi$ pour $a > 0$ et $b > 0$.

**Correction :**
1. **Continuité de la convolution :**
Pour $f, g \in L^2$, on considère $(f * g)(x) = \int_{\mathbb{R}} f(t) g(x-t) dt$.
Soit $g_x(t) = g(x-t)$. Par l'inégalité de Cauchy-Schwarz :
$$ |(f * g)(x)| \le \int_{\mathbb{R}} |f(t)| |g(x-t)| dt \le \|f\|_2 \|g_x\|_2 $$
L'invariance par translation de la mesure de Lebesgue implique $\|g_x\|_2 = \|g\|_2$.
D'où $|(f * g)(x)| \le \|f\|_2 \|g\|_2$ pour tout $x$. La fonction est donc uniformément bornée.
Pour la continuité, considérons la différence :
$$ |(f * g)(x+h) - (f * g)(x)| = \left| \int_{\mathbb{R}} f(t) [g(x+h-t) - g(x-t)] dt \right| $$
Par Cauchy-Schwarz :
$$ |(f * g)(x+h) - (f * g)(x)| \le \|f\|_2 \|g_{x+h} - g_x\|_2 = \|f\|_2 \|g_{-h} - g\|_2 $$
La continuité en moyenne d'ordre $p$ (pour $p=2$) stipule que $\lim_{h \to 0} \|g_{-h} - g\|_2 = 0$.
Par conséquent, $\lim_{h \to 0} (f * g)(x+h) = (f * g)(x)$, ce qui démontre la continuité uniforme de $f * g$.

2. **Calcul d'intégrale via Parseval :**
Posons $f(t) = \mathbf{1}_{[-a, a]}(t)$ et $g(t) = \mathbf{1}_{[-b, b]}(t)$. Les deux fonctions sont dans $L^1 \cap L^2$.
Leurs transformées de Fourier sont $\hat{f}(\xi) = \frac{2\sin(a\xi)}{\xi}$ et $\hat{g}(\xi) = \frac{2\sin(b\xi)}{\xi}$.
L'identité de Parseval s'écrit :
$$ \langle \hat{f}, \hat{g} \rangle_{L^2} = 2\pi \langle f, g \rangle_{L^2} $$
$$ \int_{\mathbb{R}} \frac{4\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi = 2\pi \int_{\mathbb{R}} \mathbf{1}_{[-a, a]}(t) \mathbf{1}_{[-b, b]}(t) dt $$
Le produit des fonctions indicatrices est l'indicatrice de l'intersection des intervalles $[-a, a] \cap [-b, b] = [-\min(a,b), \min(a,b)]$.
$$ \int_{\mathbb{R}} \frac{4\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi = 2\pi \int_{-\min(a,b)}^{\min(a,b)} 1 dt = 2\pi (2\min(a,b)) = 4\pi\min(a,b) $$
En simplifiant par 4 :
$$ \int_{\mathbb{R}} \frac{\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi = \pi \min(a,b) $$

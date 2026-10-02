## Exercice 2 : Théorème d'inversion pour des fonctions affines par morceaux \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit la fonction "triangle" $f(t) = \max(1 - |t|, 0)$.
1. Montrer que $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
2. Calculer sa transformée de Fourier $\hat{f}(\xi)$.
3. Utiliser le théorème d'inversion de Fourier pour calculer l'intégrale $\int_{-\infty}^{+\infty} \frac{\sin^2(\xi/2)}{(\xi/2)^2} d\xi$.

**Correction :**
1. **Appartenance à $L^1$ et $L^2$ :**
La fonction est continue, à support compact $[-1, 1]$, et bornée par $1$.
Elle est trivialement dans $L^1(\mathbb{R})$ : $\|f\|_1 = \int_{-1}^1 (1-|t|) dt = 2 \int_0^1 (1-t) dt = 2 \left[ t - \frac{t^2}{2} \right]_0^1 = 1$.
Elle est aussi dans $L^2(\mathbb{R})$ : $\|f\|_2^2 = 2 \int_0^1 (1-t)^2 dt = 2 \left[ \frac{-(1-t)^3}{3} \right]_0^1 = \frac{2}{3} < \infty$.

2. **Transformée de Fourier :**
$f$ peut s'écrire comme l'auto-convolution de la fonction porte $p(t) = \mathbf{1}_{[-1/2, 1/2]}(t)$.
En effet, $(p * p)(t) = \int p(\tau) p(t-\tau) d\tau = \int_{-1/2}^{1/2} \mathbf{1}_{[-1/2, 1/2]}(t-\tau) d\tau$.
L'intégrande est non nul si $-1/2 \leq t-\tau \leq 1/2$, soit $t-1/2 \leq \tau \leq t+1/2$.
L'intersection de $[-1/2, 1/2]$ et $[t-1/2, t+1/2]$ a pour longueur $\max(1-|t|, 0)$. Donc $f = p * p$.
Par propriété de la transformée de Fourier, $\mathcal{F}(p * p)(\xi) = (\mathcal{F}(p)(\xi))^2$.
Or, $\mathcal{F}(p)(\xi) = \int_{-1/2}^{1/2} e^{-i\xi t} dt = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_{-1/2}^{1/2} = \frac{e^{i\xi/2} - e^{-i\xi/2}}{i\xi} = \frac{2\sin(\xi/2)}{\xi}$.
Donc, $\hat{f}(\xi) = \left( \frac{2\sin(\xi/2)}{\xi} \right)^2 = \left( \frac{\sin(\xi/2)}{\xi/2} \right)^2 = \text{sinc}^2(\xi/2)$.

3. **Inversion de Fourier :**
Comme $\hat{f}(\xi) \ge 0$ et $\int \hat{f}(\xi) d\xi$ est lié à $f(0)$, vérifions l'intégrabilité de $\hat{f}$.
$\hat{f}(\xi) \sim 1$ en $0$, et $\hat{f}(\xi) \le \frac{4}{\xi^2}$ à l'infini, donc $\hat{f} \in L^1(\mathbb{R})$.
On peut donc appliquer le théorème d'inversion ponctuelle pour toute fonction $f$ continue dont la transformée est dans $L^1$ :
$$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{f}(\xi) e^{i\xi t} d\xi $$
Évaluons cette identité en $t=0$ :
$$ f(0) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{f}(\xi) e^0 d\xi = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \frac{\sin^2(\xi/2)}{(\xi/2)^2} d\xi $$
Or $f(0) = \max(1-0, 0) = 1$.
On en déduit donc immédiatement :
$$ \int_{-\infty}^{+\infty} \frac{\sin^2(\xi/2)}{(\xi/2)^2} d\xi = 2\pi $$

## Exercice 1 : Calcul d'énergie via Plancherel \quad $\bigstar\star\star\star\star$

**Énoncé :**
Considérons le signal $f(t) = e^{-a|t|}$ avec $a > 0$.
1. Calculer l'énergie totale du signal dans le domaine temporel : $E = \|f\|_{L^2}^2 = \int_{-\infty}^{+\infty} |f(t)|^2 dt$.
2. Calculer la transformée de Fourier $\hat{f}(\xi)$.
3. Calculer l'énergie totale dans le domaine fréquentiel : $\frac{1}{2\pi} \|\hat{f}\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 d\xi$.
4. Vérifier l'égalité de Plancherel-Parseval.

**Correction :**
1. **Énergie temporelle :**
La fonction $f(t) = e^{-a|t|}$ est paire. Son module au carré est $|f(t)|^2 = e^{-2a|t|}$.
$$ E = \int_{-\infty}^{+\infty} e^{-2a|t|} dt = 2 \int_{0}^{+\infty} e^{-2at} dt $$
En primitivant :
$$ E = 2 \left[ \frac{e^{-2at}}{-2a} \right]_0^{+\infty} = 2 \left( 0 - \frac{1}{-2a} \right) = \frac{1}{a} $$

2. **Transformée de Fourier :**
Par définition, $\hat{f}(\xi) = \int_{-\infty}^{+\infty} e^{-a|t|} e^{-i\xi t} dt$.
En séparant l'intégrale :
$$ \hat{f}(\xi) = \int_{-\infty}^{0} e^{at} e^{-i\xi t} dt + \int_{0}^{+\infty} e^{-at} e^{-i\xi t} dt $$
$$ \hat{f}(\xi) = \int_{-\infty}^{0} e^{(a-i\xi)t} dt + \int_{0}^{+\infty} e^{-(a+i\xi)t} dt $$
$$ \hat{f}(\xi) = \left[ \frac{e^{(a-i\xi)t}}{a-i\xi} \right]_{-\infty}^0 + \left[ \frac{e^{-(a+i\xi)t}}{-(a+i\xi)} \right]_0^{+\infty} $$
Comme $a>0$, $\lim_{t \to -\infty} e^{at} = 0$ et $\lim_{t \to +\infty} e^{-at} = 0$.
$$ \hat{f}(\xi) = \frac{1}{a-i\xi} - 0 + 0 - \frac{1}{-(a+i\xi)} = \frac{1}{a-i\xi} + \frac{1}{a+i\xi} $$
En réduisant au même dénominateur :
$$ \hat{f}(\xi) = \frac{a+i\xi + a-i\xi}{(a-i\xi)(a+i\xi)} = \frac{2a}{a^2 + \xi^2} $$

3. **Énergie fréquentielle :**
Calculons l'intégrale du module au carré :
$$ I = \int_{-\infty}^{+\infty} \left( \frac{2a}{a^2 + \xi^2} \right)^2 d\xi = 4a^2 \int_{-\infty}^{+\infty} \frac{1}{(a^2 + \xi^2)^2} d\xi $$
Pour évaluer cette intégrale, posons le changement de variable $\xi = a \tan \theta$, avec $d\xi = a(1+\tan^2\theta) d\theta = \frac{a}{\cos^2\theta} d\theta$.
Les bornes $-\infty$ et $+\infty$ deviennent $-\frac{\pi}{2}$ et $\frac{\pi}{2}$.
De plus, $a^2 + \xi^2 = a^2(1+\tan^2\theta) = \frac{a^2}{\cos^2\theta}$.
Donc $\frac{1}{(a^2+\xi^2)^2} = \frac{\cos^4\theta}{a^4}$.
$$ I = 4a^2 \int_{-\pi/2}^{\pi/2} \frac{\cos^4\theta}{a^4} \frac{a}{\cos^2\theta} d\theta = \frac{4a^3}{a^4} \int_{-\pi/2}^{\pi/2} \cos^2\theta d\theta $$
$$ I = \frac{4}{a} \int_{-\pi/2}^{\pi/2} \frac{1+\cos(2\theta)}{2} d\theta = \frac{2}{a} \left[ \theta + \frac{\sin(2\theta)}{2} \right]_{-\pi/2}^{\pi/2} $$
$$ I = \frac{2}{a} \left( \left(\frac{\pi}{2} + 0\right) - \left(-\frac{\pi}{2} + 0\right) \right) = \frac{2}{a} \times \pi = \frac{2\pi}{a} $$
L'énergie fréquentielle normalisée est donc $\frac{1}{2\pi} I = \frac{1}{2\pi} \times \frac{2\pi}{a} = \frac{1}{a}$.

4. **Vérification :**
On constate bien que $\|f\|_{L^2}^2 = \frac{1}{a} = \frac{1}{2\pi} \|\hat{f}\|_{L^2}^2$, validant ainsi l'identité de Plancherel-Parseval pour ce signal.

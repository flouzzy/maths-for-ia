# Exercice 1 : Calcul direct de l'énergie et Plancherel
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit $f(t) = e^{-|t|}$.
1. Vérifier que $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ et calculer son énergie $\|f\|_2^2$.
2. Calculer $\hat{f}(\xi)$.
3. Vérifier directement l'égalité de Plancherel $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$.

**Correction :**
1. L'énergie est donnée par $\|f\|_2^2 = \int_{-\infty}^\infty (e^{-|t|})^2 dt = \int_{-\infty}^\infty e^{-2|t|} dt$.
Par parité : $\|f\|_2^2 = 2 \int_0^\infty e^{-2t} dt = 2 \left[ \frac{e^{-2t}}{-2} \right]_0^\infty = 1$.
2. $\hat{f}(\xi) = \int_{-\infty}^\infty e^{-|t|} e^{-i\xi t} dt = \int_{-\infty}^0 e^{t(1-i\xi)} dt + \int_0^\infty e^{-t(1+i\xi)} dt$.
$\hat{f}(\xi) = \frac{1}{1-i\xi} + \frac{1}{1+i\xi} = \frac{2}{1+\xi^2}$.
3. L'énergie de la transformée est $\|\hat{f}\|_2^2 = \int_{-\infty}^\infty \left(\frac{2}{1+\xi^2}\right)^2 d\xi = 4 \int_{-\infty}^\infty \frac{1}{(1+\xi^2)^2} d\xi$.
Posons $\xi = \tan(\theta)$, $d\xi = (1+\tan^2(\theta)) d\theta$. L'intégrale devient $4 \int_{-\pi/2}^{\pi/2} \cos^2(\theta) d\theta = 4 \int_{-\pi/2}^{\pi/2} \frac{1+\cos(2\theta)}{2} d\theta = 4 \cdot \frac{\pi}{2} = 2\pi$.
On a bien $2\pi = 2\pi \cdot 1$. Plancherel est vérifié.

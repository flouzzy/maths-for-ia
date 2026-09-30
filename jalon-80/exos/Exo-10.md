\subsection*{Exercice 10 : Autour du sinus cardinal et Parseval \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

On admet la formule d'inversion de Fourier (sous bonnes hypothèses d'intégrabilité) : si $f$ et $\hat{f}$ sont dans $L^1$, alors $f(t) = \frac{1}{2\pi} \int \hat{f}(\xi) e^{i\xi t} d\xi$.
Soit $h(t) = \left( \frac{\sin t}{t} \right)^2$. En exploitant les résultats des exercices 1 et 7, calculer $\int_{-\infty}^{+\infty} h(t) dt$.

---
**Correction :**

Dans l'exercice 1, la transformée de $f = \mathbf{1}_{[-1, 1]}$ (donc $a=1$) est $\hat{f}(\xi) = 2 \frac{\sin \xi}{\xi}$.
L'auto-convolution $g = f * f$ a pour transformée $\hat{g}(\xi) = \hat{f}(\xi)^2 = 4 \left( \frac{\sin \xi}{\xi} \right)^2 = 4 h(\xi)$.
On a calculé à l'exercice 7 (avec $a=1$) que $g(t) = (2 - |t|)\mathbf{1}_{[-2, 2]}(t)$.

Appliquons la formule d'inversion en $t=0$ pour la fonction $g$ :
$g(0) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{g}(\xi) e^{i\xi \cdot 0} d\xi = \frac{1}{2\pi} \int_{-\infty}^{+\infty} 4 h(\xi) d\xi$.
Donc $\int_{-\infty}^{+\infty} h(\xi) d\xi = \frac{2\pi}{4} g(0)$.
Or l'expression de $g$ nous donne directement $g(0) = 2 - |0| = 2$.
D'où :
$$ \int_{-\infty}^{+\infty} \left( \frac{\sin \xi}{\xi} \right)^2 d\xi = \frac{2\pi}{4} \times 2 = \pi $$
Cette élégante méthode de dualité (passer par la fonction dont $h$ est la transformée) évite le recours au théorème des résidus complexes pour calculer l'intégrale de ce sinus cardinal au carré.

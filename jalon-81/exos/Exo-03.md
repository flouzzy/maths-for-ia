# Exercice 3 : Produit scalaire et identité de Parseval
$\bigstar\bigstar\star\star\star$

**Énoncé :**
Soient $f(t) = \mathbf{1}_{[-a, a]}(t)$ et $g(t) = \mathbf{1}_{[-b, b]}(t)$ avec $0 < a < b$.
1. Déterminer $\hat{f}$ et $\hat{g}$.
2. Utiliser l'identité de Parseval pour évaluer l'intégrale $I = \int_{-\infty}^{+\infty} \frac{\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi$.

---
**Correction :**
**Question 1 : Transformées de Fourier**
Pour $f(t) = \mathbf{1}_{[-a, a]}(t)$,
$$ \hat{f}(\xi) = \int_{-a}^{a} e^{-i\xi t} dt = \frac{2\sin(a\xi)}{\xi} $$
De même, pour $g(t) = \mathbf{1}_{[-b, b]}(t)$,
$$ \hat{g}(\xi) = \frac{2\sin(b\xi)}{\xi} $$

**Question 2 : Évaluation de l'intégrale via Parseval**
L'identité de Parseval s'écrit :
$$ \int_{-\infty}^{+\infty} f(t) \overline{g(t)} dt = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi $$
Calculons le produit scalaire temporel $\langle f, g \rangle_{L^2}$ :
Puisque $0 < a < b$, $[-a, a] \subset [-b, b]$. Le produit $f(t)\overline{g(t)}$ est simplement $\mathbf{1}_{[-a, a]}(t) \mathbf{1}_{[-b, b]}(t) = \mathbf{1}_{[-a, a]}(t)$.
$$ \int_{-\infty}^{+\infty} f(t) \overline{g(t)} dt = \int_{-a}^{a} 1 dt = 2a $$
Écrivons maintenant le produit scalaire fréquentiel :
$$ \langle \hat{f}, \hat{g} \rangle_{L^2} = \int_{-\infty}^{+\infty} \frac{2\sin(a\xi)}{\xi} \frac{2\sin(b\xi)}{\xi} d\xi = 4 \int_{-\infty}^{+\infty} \frac{\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi = 4I $$
D'après Parseval, nous avons :
$$ 2a = \frac{1}{2\pi} \times 4I \implies 2a = \frac{2}{\pi} I \implies I = \frac{2a\pi}{2} = a\pi $$
Ainsi, la valeur de l'intégrale est :
$$ \int_{-\infty}^{+\infty} \frac{\sin(a\xi)\sin(b\xi)}{\xi^2} d\xi = a\pi $$
(Rappel : on a supposé $a < b$. Si $b < a$, le résultat serait $b\pi$. Plus généralement, c'est $\pi \min(a,b)$).

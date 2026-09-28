# Exercice 9 : Équation différentielle linéaire et Fourier $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Trouver une solution particulière $2\pi$-périodique de l'équation $y'' + \omega^2 y = f(t)$, où $\omega \notin \mathbb{Z}$ et $f(t) = |t|$ sur $]-\pi, \pi]$.

**Correction Détaillée :**
1. **Décomposition en série de l'équation :**
On cherche $y(t) = \sum_{n=-\infty}^{+\infty} c_n(y) e^{int}$.
En dérivant deux fois (licite sous convergence absolue), $y''(t) = \sum -n^2 c_n(y) e^{int}$.
L'équation devient :
$$ \sum_{n=-\infty}^{+\infty} (-n^2 + \omega^2) c_n(y) e^{int} = \sum_{n=-\infty}^{+\infty} c_n(f) e^{int} $$

2. **Identification des coefficients :**
Puisque $\omega \notin \mathbb{Z}$, $-n^2 + \omega^2 \neq 0$. Par unicité, on a :
$$ c_n(y) = \frac{c_n(f)}{\omega^2 - n^2} $$

3. **Application à $f(t) = |t|$ :**
On sait (Exo 2) que $a_0 = \pi \implies c_0(f) = \pi/2$.
Et $a_n = \frac{2}{n^2\pi}((-1)^n - 1) \implies c_n(f) = c_{-n}(f) = \frac{1}{n^2\pi}((-1)^n - 1)$ pour $n \neq 0$.
Ainsi :
$$ c_0(y) = \frac{\pi}{2\omega^2} $$
$$ c_n(y) = \frac{(-1)^n - 1}{\pi n^2 (\omega^2 - n^2)} $$
La solution est :
$$ y(t) = \frac{\pi}{2\omega^2} + \sum_{n=1}^\infty \frac{2((-1)^n - 1)}{\pi n^2 (\omega^2 - n^2)} \cos(nt) $$
La division par $n^2(\omega^2 - n^2)$ assure une décroissance en $1/n^4$, donc la série converge très rapidement, justifiant formellement la dérivation sous le signe somme.

# Exercice 8 : Limite et série de Fourier
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Montrer que la fonction $f(x) = \sum_{n=1}^\infty \frac{\sin^2(nx)}{n^2}$ est bien définie et mesurable sur $\mathbb{R}$, puis calculer son intégrale sur $[0, \pi]$.

## Correction Détaillée

Considérons les fonctions $u_n(x) = \frac{\sin^2(nx)}{n^2}$. Ces fonctions sont continues, donc mesurables, et positives ($\geq 0$).
Par le corollaire du Théorème de Convergence Monotone (sommation de séries positives) :
L'intégrale de la série est égale à la série des intégrales :
$$\int_0^\pi f(x) dx = \sum_{n=1}^\infty \int_0^\pi \frac{\sin^2(nx)}{n^2} dx$$
Calculons l'intégrale $\int_0^\pi \sin^2(nx) dx$. On utilise la formule $\sin^2(nx) = \frac{1 - \cos(2nx)}{2}$.
$$\int_0^\pi \frac{1 - \cos(2nx)}{2} dx = \left[ \frac{x}{2} - \frac{\sin(2nx)}{4n} \right]_0^\pi = \frac{\pi}{2}$$
Donc, l'intégrale devient :
$$\int_0^\pi f(x) dx = \sum_{n=1}^\infty \frac{\pi}{2n^2} = \frac{\pi}{2} \sum_{n=1}^\infty \frac{1}{n^2}$$
On sait que $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.
Donc $\int_0^\pi f(x) dx = \frac{\pi}{2} \frac{\pi^2}{6} = \frac{\pi^3}{12}$.

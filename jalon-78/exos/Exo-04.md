## Exercice 4 : Coefficients de Fourier de $f(x)=x^2$ \quad \bigstar\bigstar\bigstar\star\star

On considère $f(x)=x^2$ sur $[-\pi, \pi]$, prolongée par $2\pi$-périodicité.
1. Calculer ses coefficients de Fourier trigonométriques.
2. En déduire $\sum_{n=1}^\infty \frac{1}{n^2}$ et $\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n^2}$.

**Correction :**
1. $f$ paire, $b_n = 0$.
$a_0 = \frac{2}{\pi} \int_0^\pi x^2 dx = \frac{2\pi^2}{3}$.
$a_n = \frac{2}{\pi} \int_0^\pi x^2 \cos(nx) dx$. Double IPP :
$\int x^2\cos(nx)dx = \frac{x^2\sin(nx)}{n} - \frac{2x(-\cos(nx))}{n^2} - \frac{2\sin(nx)}{n^3}$.
$a_n = \frac{2}{\pi} \left[ \frac{2\pi\cos(n\pi)}{n^2} \right] = \frac{4(-1)^n}{n^2}$.
Série : $\frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2}\cos(nx)$.
2. Par le Th. de Dirichlet (continue, $C^1$ par morceaux) en $x=\pi$ :
$\pi^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n (-1)^n}{n^2} = \frac{\pi^2}{3} + 4 \sum \frac{1}{n^2}$.
$4\sum \frac{1}{n^2} = \frac{2\pi^2}{3} \implies \sum \frac{1}{n^2} = \frac{\pi^2}{6}$.
En $x=0$ : $0 = \frac{\pi^2}{3} + 4 \sum \frac{(-1)^n}{n^2}$, donc $\sum \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$.

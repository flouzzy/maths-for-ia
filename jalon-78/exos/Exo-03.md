# Calculs avec la fonction t carré

$\bigstar\bigstar\star\star\star$

Soit $f$ la fonction $2\pi$-périodique, définie sur $[-\pi, \pi]$ par $f(t) = t^2$.
1. Déterminer les coefficients de Fourier de $f$.
2. En appliquant le théorème de Dirichlet, retrouver $\sum_{n=1}^{+\infty} \frac{1}{n^2}$.
3. Retrouver la somme de la série harmonique alternée $\sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2}$.

**Correction détaillée :**
1. $f$ est paire, donc $b_n(f) = 0$ pour tout $n \ge 1$.
   Calculons $a_0$ : $a_0 = \frac{1}{\pi} \int_{-\pi}^\pi t^2 dt = \frac{2}{\pi} [\frac{t^3}{3}]_0^\pi = \frac{2\pi^2}{3}$.
   Pour $n \ge 1$, on intègre par parties deux fois :
   $$ a_n(f) = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt = \frac{2}{\pi} \left( [t^2 \frac{\sin(nt)}{n}]_0^\pi - \int_0^\pi 2t \frac{\sin(nt)}{n} dt \right) $$
   Le crochet est nul.
   $$ a_n(f) = -\frac{4}{n\pi} \int_0^\pi t \sin(nt) dt = -\frac{4}{n\pi} \left( [-t \frac{\cos(nt)}{n}]_0^\pi - \int_0^\pi 1 (-\frac{\cos(nt)}{n}) dt \right) $$
   $$ a_n(f) = -\frac{4}{n\pi} \left( -\pi \frac{(-1)^n}{n} + 0 \right) = \frac{4(-1)^n}{n^2} $$
2. $f$ est continue et $C^1$ par morceaux, le théorème de Dirichlet s'applique sur $\mathbb{R}$.
   En $t=\pi$, $f(\pi) = \pi^2$.
   $$ \pi^2 = \frac{\pi^2}{3} + \sum_{n=1}^{+\infty} \frac{4(-1)^n}{n^2} \cos(n\pi) = \frac{\pi^2}{3} + \sum_{n=1}^{+\infty} \frac{4(-1)^n (-1)^n}{n^2} = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{1}{n^2} $$
   Donc $4 \sum_{n=1}^{+\infty} \frac{1}{n^2} = \pi^2 - \frac{\pi^2}{3} = \frac{2\pi^2}{3}$, d'où $\sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.
3. En $t=0$, $f(0) = 0$.
   $$ 0 = \frac{\pi^2}{3} + \sum_{n=1}^{+\infty} \frac{4(-1)^n}{n^2} \cos(0) = \frac{\pi^2}{3} - 4 \sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2} $$
   D'où $\sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$.
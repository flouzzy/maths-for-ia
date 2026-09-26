# Série de Fourier d'une fonction valeur absolue

$\bigstar\star\star\star\star$

Soit $f$ la fonction $2\pi$-périodique, définie sur $[-\pi, \pi]$ par $f(t) = |t|$.
1. Calculer les coefficients de Fourier de $f$.
2. Écrire la série de Fourier de $f$.
3. En déduire la somme de la série $\sum_{n=0}^{+\infty} \frac{1}{(2n+1)^2}$.

**Correction détaillée :**
1. La fonction $f$ est paire, continue sur $\mathbb{R}$. Parité implique $b_n(f) = 0$ pour tout $n \ge 1$.
   Calculons $a_0(f)$ : $a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |t| dt = \frac{2}{\pi} \int_0^\pi t dt = \frac{2}{\pi} [\frac{t^2}{2}]_0^\pi = \pi$.
   Calculons $a_n(f)$ pour $n \ge 1$ par intégration par parties :
   $$ a_n(f) = \frac{2}{\pi} \int_0^\pi t \cos(nt) dt $$
   Posons $u=t, v'=\cos(nt) \implies u'=1, v=\frac{\sin(nt)}{n}$.
   $$ a_n(f) = \frac{2}{\pi} \left( \left[ t\frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{\sin(nt)}{n} dt \right) $$
   Le terme tout intégré est nul en $0$ et en $\pi$ ($\sin(n\pi)=0$).
   $$ a_n(f) = \frac{2}{\pi} \left[ \frac{\cos(nt)}{n^2} \right]_0^\pi = \frac{2}{\pi n^2} (\cos(n\pi) - 1) = \frac{2}{\pi n^2} ((-1)^n - 1) $$
   Si $n$ est pair ($n=2p$), $a_{2p} = 0$.
   Si $n$ est impair ($n=2p+1$), $a_{2p+1} = \frac{-4}{\pi(2p+1)^2}$.
2. La série de Fourier s'écrit :
   $$ S(f)(t) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{\cos((2p+1)t)}{(2p+1)^2} $$
3. $f$ est continue et $C^1$ par morceaux. D'après le théorème de Dirichlet, $S(f)(t) = f(t)$ pour tout $t$.
   Évaluons en $t=0$ :
   $$ f(0) = 0 = \frac{\pi}{2} - \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{\cos(0)}{(2p+1)^2} $$
   $$ \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2} = \frac{\pi}{2} \implies \sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2} = \frac{\pi^2}{8} $$
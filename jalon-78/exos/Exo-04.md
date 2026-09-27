# Exo 04 : Application au calcul de la somme de Riemann zeta(2)

**Difficulté :** \bigstar\bigstar\bigstar\star\star


Soit $f$ la fonction $2\pi$-périodique définie par $f(t) = t^2$ sur $]-\pi, \pi]$.

1. Déterminer la série de Fourier de $f$.
2. En appliquant le théorème de Dirichlet en $t=\pi$, retrouver la valeur de la somme $\sum_{n=1}^{+\infty} \frac{1}{n^2}$.

## Correction

**1. Série de Fourier de $f$ :**
La fonction $f(t) = t^2$ est paire sur $]-\pi, \pi]$.
Ses coefficients en sinus $b_n$ sont donc nuls pour tout $n$.
Calcul de $a_0$ :
$$ a_0 = \frac{1}{\pi} \int_{-\pi}^\pi t^2 dt = \frac{2}{\pi} \int_0^\pi t^2 dt = \frac{2}{\pi} \left[ \frac{t^3}{3} \right]_0^\pi = \frac{2\pi^2}{3} $$

Calcul de $a_n$ pour $n \ge 1$ :
$$ a_n = \frac{1}{\pi} \int_{-\pi}^\pi t^2 \cos(nt) dt = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt $$
On procède par une double intégration par parties.
Première IPP : $u=t^2 \implies u'=2t$ et $v'=\cos(nt) \implies v=\frac{\sin(nt)}{n}$.
$$ a_n = \frac{2}{\pi} \left( \left[ t^2 \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi 2t \frac{\sin(nt)}{n} dt \right) $$
Le crochet est nul car $\sin(n\pi) = 0$ et $0^2=0$.
$$ a_n = \frac{-4}{n\pi} \int_0^\pi t \sin(nt) dt $$
Deuxième IPP : $u=t \implies u'=1$ et $v'=\sin(nt) \implies v=\frac{-\cos(nt)}{n}$.
$$ a_n = \frac{-4}{n\pi} \left( \left[ -t \frac{\cos(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{-\cos(nt)}{n} dt \right) $$
$$ a_n = \frac{-4}{n\pi} \left( -\frac{\pi \cos(n\pi)}{n} - 0 + \left[ \frac{\sin(nt)}{n^2} \right]_0^\pi \right) $$
Le dernier crochet est nul. Avec $\cos(n\pi) = (-1)^n$ :
$$ a_n = \frac{-4}{n\pi} \left( -\frac{\pi (-1)^n}{n} \right) = \frac{4(-1)^n}{n^2} $$

La série de Fourier est :
$$ S(f)(t) = \frac{a_0}{2} + \sum_{n=1}^\infty a_n \cos(nt) = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} \cos(nt) $$

**2. Calcul de la somme :**
$f$ est continue et de classe $C^1$ par morceaux sur $\mathbb{R}$. Par le théorème de Dirichlet, la série converge vers $f(t)$ pour tout $t$.
Évaluons en $t=\pi$ :
$$ f(\pi) = \pi^2 $$
$$ S(f)(\pi) = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} \cos(n\pi) $$
Puisque $\cos(n\pi) = (-1)^n$, on a $(-1)^n \cos(n\pi) = (-1)^{2n} = 1$.
Donc :
$$ \pi^2 = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4}{n^2} $$
On isole la somme :
$$ 4 \sum_{n=1}^\infty \frac{1}{n^2} = \pi^2 - \frac{\pi^2}{3} = \frac{2\pi^2}{3} $$
$$ \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} $$
C'est la résolution du célèbre problème de Bâle.

# Exercice 3 : Série de Fourier de la fonction $t \mapsto t^2$

**Difficulté :** \bigstar\bigstar\star\star\star

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique définie sur $[-\pi, \pi]$ par $f(t) = t^2$.
1. Déterminer les coefficients de Fourier réels de $f$.
2. En appliquant le théorème de Dirichlet en $t=\pi$, en déduire la valeur de $\sum_{n=1}^{+\infty} \frac{1}{n^2}$.

**Correction :**
1. La fonction $f$ est paire, d'où $b_n = 0$ pour tout $n \ge 1$.
   Calcul de $a_0$ :
   $$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi t^2 dt = \frac{2}{\pi} \int_0^\pi t^2 dt = \frac{2}{\pi} \left[ \frac{t^3}{3} \right]_0^\pi = \frac{2\pi^2}{3}$$
   Calcul de $a_n$ pour $n \ge 1$ via deux intégrations par parties :
   $$a_n = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt$$
   Première IPP ($u=t^2, v'=\cos(nt)$) :
   $$a_n = \frac{2}{\pi} \left( \left[ t^2 \frac{\sin(nt)}{n} \right]_0^\pi - \frac{2}{n} \int_0^\pi t \sin(nt) dt \right) = -\frac{4}{\pi n} \int_0^\pi t \sin(nt) dt$$
   Seconde IPP ($u=t, v'=\sin(nt)$) :
   $$a_n = -\frac{4}{\pi n} \left( \left[ -t \frac{\cos(nt)}{n} \right]_0^\pi - \int_0^\pi \left(-\frac{\cos(nt)}{n}\right) dt \right)$$
   $$a_n = -\frac{4}{\pi n} \left( -\frac{\pi (-1)^n}{n} + 0 \right) = \frac{4(-1)^n}{n^2}$$
2. La série de Fourier de $f$ s'écrit :
   $$S(f)(t) = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} \cos(nt)$$
   La fonction $f$ est continue sur $\mathbb{R}$ et de classe $C^1$ par morceaux. D'après le théorème de Dirichlet, $S(f)(\pi) = f(\pi) = \pi^2$.
   $$\frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} \cos(n\pi) = \pi^2$$
   Puisque $\cos(n\pi) = (-1)^n$, le terme devient $\frac{(-1)^{2n}}{n^2} = \frac{1}{n^2}$.
   Ainsi, $\frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{1}{n^2} = \pi^2$, d'où :
   $$4 \sum_{n=1}^{+\infty} \frac{1}{n^2} = \pi^2 - \frac{\pi^2}{3} = \frac{2\pi^2}{3} \implies \sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$

# Exercice 4 : Application aux séries alternées

**Difficulté :** \bigstar\bigstar\star\star\star

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique, telle que $f(t) = t^2$ sur $[-\pi, \pi]$.
1. Évaluer la série de Fourier de $f$ en $t=0$.
2. En déduire la valeur de la somme de la série alternée $\sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2}$.

**Correction :**
1. La série de Fourier de $f$ a été calculée :
   $$S(f)(t) = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} \cos(nt)$$
   La fonction est continue en $0$, donc par le théorème de Dirichlet, $S(f)(0) = f(0) = 0$.
2. En évaluant à $t=0$, on obtient $\cos(0) = 1$. L'égalité s'écrit :
   $$\frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} = 0$$
   On réarrange pour isoler la somme :
   $$4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} = -\frac{\pi^2}{3}$$
   En multipliant par $-1$ de chaque côté :
   $$4 \sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{3}$$
   D'où :
   $$\sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$$

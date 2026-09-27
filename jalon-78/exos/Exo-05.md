# Exo 05 : Calcul de la somme de la série alternée zeta alternée

**Difficulté :** \bigstar\bigstar\bigstar\star\star


En utilisant la fonction et la série de Fourier de l'exercice précédent, retrouver la valeur de la somme :
$$ \sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n^2} $$

## Correction

Reprenons la série de Fourier de la fonction périodique $f(t)$ (définie par $t^2$ sur $]-\pi, \pi]$) :
$$ S(f)(t) = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} \cos(nt) $$
Le théorème de Dirichlet garantit que $S(f)(t) = f(t)$ pour tout $t$, car $f$ est continue et $C^1$ par morceaux.

Pour faire apparaître le terme $(-1)^n$ pur dans la série sans qu'il ne soit annulé par $\cos(n\pi)$, il suffit d'évaluer la fonction en $t=0$.
$$ f(0) = 0 $$
Évaluons la série en $t=0$ (sachant que $\cos(0) = 1$) :
$$ S(f)(0) = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} \cos(0) = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} $$
Ainsi, on a :
$$ 0 = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n}{n^2} $$
En isolant la somme :
$$ 4 \sum_{n=1}^\infty \frac{(-1)^n}{n^2} = -\frac{\pi^2}{3} $$
$$ \sum_{n=1}^\infty \frac{(-1)^n}{n^2} = -\frac{\pi^2}{12} $$
La somme demandée est l'opposée de celle-ci, donc en multipliant par $-1$ :
$$ \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12} $$
C'est la somme de la série de Riemann alternée de paramètre $s=2$.

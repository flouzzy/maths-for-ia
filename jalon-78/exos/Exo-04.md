# Exercice 4 : Phénomène de Gibbs analytique $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Reprenons le signal en dents de scie $f(t) = t$ sur $]-\pi, \pi]$.
On admet que $S(f)(t) = 2 \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n} \sin(nt)$.
Calculer la somme partielle $S_N(f)(t)$ sous forme d'une intégrale.

**Correction Détaillée :**
Pour étudier la forme analytique de $S_N(f)$, on utilise le noyau de Dirichlet $D_N(t) = \sum_{k=-N}^N e^{ikt}$.
La somme partielle d'une fonction s'écrit comme un produit de convolution :
$$ S_N(f)(t) = \frac{1}{2\pi} \int_{-\pi}^\pi f(u) D_N(t-u) du $$
Pour $D_N(t)$, nous avons :
$$ D_N(t) = \frac{\sin((N+\frac{1}{2})t)}{\sin(t/2)} $$
Ainsi :
$$ S_N(f)(t) = \frac{1}{2\pi} \int_{-\pi}^\pi u \frac{\sin((N+\frac{1}{2})(t-u))}{\sin((t-u)/2)} du $$
Le point d'intérêt est près de $t=\pi$, où $f$ a un saut. Le comportement de cette intégrale près du saut démontre que le dépassement (l'overshoot) ne tend pas vers zéro avec $N$, mais vers une limite stricte d'environ 9% du saut. C'est l'essence du phénomène de Gibbs.

## Exercice 4 : Croissance presque partout \quad $\bigstar\bigstar\bigstar\star\star$

Soit $f_n(x) = x^2 (1 - x^n)$ sur $[0, 1]$, modifiée pour valoir $n$ sur les nombres rationnels $\mathbb{Q} \cap [0, 1]$.
**Question :** Le théorème de Beppo Levi s'applique-t-il sur l'espace mesuré $([0, 1], \mathcal{B}, \lambda)$ où $\lambda$ est la mesure de Lebesgue ? Calculer la limite de son intégrale.

**Solution :**
1. La suite de base $g_n(x) = x^2(1 - x^n)$ est strictement croissante pour $x \in ]0, 1[$.
2. Sur $\mathbb{Q} \cap [0, 1]$, la suite $(f_n)$ vaut $n$, qui est aussi strictement croissante.
3. Donc la suite $(f_n)$ est strictement croissante partout sur $[0, 1]$. De plus, elle est à valeurs positives.
4. Elle converge vers $f(x) = x^2$ si $x \notin \mathbb{Q}$, et $f(x) = +\infty$ si $x \in \mathbb{Q}$.
5. Comme $\lambda(\mathbb{Q}) = 0$, $f$ est égale à $x \mapsto x^2$ Lebesgue-presque partout.
6. L'intégrale de $f$ vaut $\int_0^1 x^2 dx = \frac{1}{3}$.
7. D'après Beppo Levi, la limite des intégrales est égale à l'intégrale de la limite. Ainsi, $\lim \int f_n d\lambda = \frac{1}{3}$. $\blacksquare$

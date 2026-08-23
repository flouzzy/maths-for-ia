## Exercice 2 : Convergence de l'intégrale $\quad \bigstar\star\star\star\star$

**Énoncé :**
Soit $f_n = n \mathbf{1}_{(0, 1/n)}$ sur $\mathbb{R}$ avec la mesure de Lebesgue $\lambda$.
Calculer $\int f_n d\lambda$ et $\int \liminf f_n d\lambda$.

**Correction :**
Pour tout $n \ge 1$, $f_n$ est une fonction simple.
Son intégrale est $\int f_n d\lambda = n \cdot \lambda((0, 1/n)) = n \cdot \frac{1}{n} = 1$.
Fixons $x \in \mathbb{R}$. Si $x \le 0$, $f_n(x) = 0$ pour tout $n$.
Si $x > 0$, alors pour $n > 1/x$, on a $x \notin (0, 1/n)$, donc $f_n(x) = 0$.
Ainsi, pour tout $x$, $f_n(x) \to 0$ quand $n \to \infty$.
Donc $f = \liminf f_n = 0$ (et $\lim f_n = 0$).
L'intégrale de $f$ est $\int 0 d\lambda = 0$.
On a bien $\int \liminf f_n \le \liminf \int f_n$, c'est-à-dire $0 \le 1$ (Lemme de Fatou strict).

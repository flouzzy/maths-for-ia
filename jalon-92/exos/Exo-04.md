# Exercice 4 : Convergence de la variance empirique \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables I.I.D. admettant un moment d'ordre 4. On note $\mu = \mathbb{E}[X_1]$ et $\sigma^2 = \text{Var}(X_1) > 0$. On définit la variance empirique non biaisée par :
$$S_n^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}_n)^2$$
où $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.
1. Montrer que $\sum_{i=1}^n (X_i - \bar{X}_n)^2 = \sum_{i=1}^n X_i^2 - n \bar{X}_n^2$.
2. En utilisant la loi forte des grands nombres, montrer que $S_n^2 \xrightarrow{p.s.} \sigma^2$.

**Correction :**
1. Développons la somme :
$$ \sum_{i=1}^n (X_i - \bar{X}_n)^2 = \sum_{i=1}^n (X_i^2 - 2X_i\bar{X}_n + \bar{X}_n^2) = \sum_{i=1}^n X_i^2 - 2\bar{X}_n \sum_{i=1}^n X_i + n\bar{X}_n^2 $$
Comme $\sum_{i=1}^n X_i = n\bar{X}_n$, on obtient :
$$ \sum_{i=1}^n (X_i - \bar{X}_n)^2 = \sum_{i=1}^n X_i^2 - 2\bar{X}_n(n\bar{X}_n) + n\bar{X}_n^2 = \sum_{i=1}^n X_i^2 - 2n\bar{X}_n^2 + n\bar{X}_n^2 = \sum_{i=1}^n X_i^2 - n\bar{X}_n^2 $$
2. D'après la question précédente, on peut réécrire $S_n^2$ :
$$ S_n^2 = \frac{n}{n-1} \left( \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \right) $$
Puisque $(X_n)$ est une suite I.I.D. admettant un moment d'ordre 2 (et même 4), on applique la LFGN aux suites $(X_n)$ et $(X_n^2)$ :
- $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p.s.} \mu$. La fonction $x \mapsto x^2$ étant continue, on a $\bar{X}_n^2 \xrightarrow{p.s.} \mu^2$.
- $\frac{1}{n} \sum_{i=1}^n X_i^2 \xrightarrow{p.s.} \mathbb{E}[X_1^2]$.
Par linéarité de la limite, on obtient que $\left( \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \right) \xrightarrow{p.s.} \mathbb{E}[X_1^2] - \mu^2 = \text{Var}(X_1) = \sigma^2$.
Enfin, comme le facteur $\frac{n}{n-1} \xrightarrow{n \to \infty} 1$, le produit converge presque sûrement vers $1 \times \sigma^2 = \sigma^2$. Ainsi, $S_n^2 \xrightarrow{p.s.} \sigma^2$.

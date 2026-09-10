## Exercice 1 : Application directe : Intégrale d'une série entière \quad $\bigstar\star\star\star\star$

Soit la suite de fonctions $f_n(x) = \sum_{k=1}^n x^k$ définies sur $[0, 1[$.
**Question :** En utilisant le corollaire du théorème de Beppo Levi, montrer que l'intégrale de la limite est égale à la somme des intégrales, et en déduire la valeur de $\int_0^1 \frac{x}{1-x} dx$.

**Solution :**
1. Pour tout $x \in [0, 1[$, $f_{n+1}(x) - f_n(x) = x^{n+1} \ge 0$. La suite $(f_n)$ est donc croissante de fonctions mesurables positives.
2. Sa limite simple est $f(x) = \sum_{k=1}^\infty x^k = \frac{x}{1-x}$.
3. D'après Beppo Levi, $\int_0^1 f(x) dx = \lim_{n \to \infty} \int_0^1 \sum_{k=1}^n x^k dx = \sum_{k=1}^\infty \int_0^1 x^k dx$.
4. Or $\int_0^1 x^k dx = \frac{1}{k+1}$.
5. Ainsi, $\int_0^1 \frac{x}{1-x} dx = \sum_{k=1}^\infty \frac{1}{k+1} = +\infty$ car c'est le reste de la série harmonique. $\blacksquare$

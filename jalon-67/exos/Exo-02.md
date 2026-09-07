# Exercice 2 : Série de fonctions rationnelles

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Calculer l'intégrale suivante en justifiant toutes les étapes :
$$I = \int_0^\infty \sum_{n=1}^\infty \frac{1}{(1+x^2)^n} dx$$

**Solution Détaillée :**
1. Soit $u_n(x) = \frac{1}{(1+x^2)^n}$ sur $[0, +\infty[$. Ces fonctions sont continues, donc mesurables, et strictement **positives**.
2. Par le corollaire du théorème de convergence monotone, nous pouvons intervertir la série et l'intégrale, quitte à ce que le résultat vaille $+\infty$ :
$$I = \sum_{n=1}^\infty \int_0^\infty \frac{1}{(1+x^2)^n} dx$$
3. Calculons plutôt la somme dans l'intégrande, car la série géométrique $\sum_{n=1}^\infty a^n = \frac{a}{1-a}$ pour $|a|<1$ (avec $a = \frac{1}{1+x^2} < 1$ pour $x > 0$).
$$f(x) = \sum_{n=1}^\infty \left(\frac{1}{1+x^2}\right)^n = \frac{\frac{1}{1+x^2}}{1 - \frac{1}{1+x^2}} = \frac{1}{1+x^2 - 1} = \frac{1}{x^2}$$
4. La valeur de $I$ est donc :
$$I = \int_0^\infty f(x) dx = \int_0^\infty \frac{1}{x^2} dx$$
5. Cette intégrale est la somme des aires sous la courbe $1/x^2$.
$$\int_0^\infty \frac{1}{x^2} dx = \int_0^1 \frac{dx}{x^2} + \int_1^\infty \frac{dx}{x^2}$$
L'intégrale sur $[1, +\infty[$ vaut $1$, mais l'intégrale sur $]0, 1]$ diverge (c'est $\lim_{\epsilon \to 0} [-\frac{1}{x}]_\epsilon^1 = +\infty$).
6. Le théorème de Beppo Levi n'interdit pas l'infini. Le résultat final rigoureux est donc :
$$I = +\infty$$

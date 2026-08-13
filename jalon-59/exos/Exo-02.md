### Exercice 2 : Conservation de l'intégrale \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f_n(x) = n x (1-x^2)^n$ sur $[0, 1]$.
1. Montrer que $f_n \to 0$ simplement sur $[0, 1]$.
2. Calculer $\int_0^1 f_n(x) dx$ et comparer avec l'intégrale de la limite.
3. En déduire que la convergence n'est pas uniforme sur $[0, 1]$.

**Correction :**
1. Si $x=0$ ou $x=1$, $f_n(x) = 0 \to 0$. Si $x \in ]0, 1[$, $1-x^2 \in ]0, 1[$, donc par croissances comparées, la suite tend vers $0$. La limite simple est $f = 0$.
2. Intégrons : $\int_0^1 n x (1-x^2)^n dx$. Posons $u = 1-x^2$, d'où $du = -2x dx$.
L'intégrale vaut $-\frac{n}{2} \int_1^0 u^n du = \frac{n}{2} \left[ \frac{u^{n+1}}{n+1} \right]_0^1 = \frac{n}{2(n+1)} \to \frac{1}{2}$.
L'intégrale de la limite est $\int_0^1 0 dx = 0$.
3. Si la convergence était uniforme sur le segment $[0, 1]$, on pourrait intervertir limite et intégrale. Or $\frac{1}{2} \neq 0$, donc la convergence ne peut être uniforme.

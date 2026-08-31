## Exercice 6 : Intégrale de Riemann impropre et limite \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Démontrer que $\int_0^1 \frac{\ln(x)}{x-1} dx = \frac{\pi^2}{6}$. On rappelle que $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

**Correction Détaillée :**
1. Sur $]0, 1[$, on a le développement en série entière : $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
2. Donc $f(x) = \frac{-\ln(x)}{1-x} = \sum_{n=0}^\infty (-x^n \ln(x))$.
3. Posons $u_n(x) = -x^n \ln(x)$. Sur $]0, 1[$, $x^n > 0$ et $\ln(x) < 0$, donc $u_n(x) > 0$. La série est à termes positifs.
4. Par le TCM (sommation), $\int_0^1 f(x) dx = \sum_{n=0}^\infty \int_0^1 -x^n \ln(x) dx$.
5. Calculons $I_n = \int_0^1 -x^n \ln(x) dx$ par intégration par parties :
   $u = -\ln(x) \implies u' = -1/x$
   $v' = x^n \implies v = \frac{x^{n+1}}{n+1}$
   $I_n = [-\ln(x) \frac{x^{n+1}}{n+1}]_0^1 - \int_0^1 -1/x \cdot \frac{x^{n+1}}{n+1} dx$
   Le terme de bord s'annule (car $x^{n+1}\ln(x) \to 0$ en $0$).
   $I_n = \int_0^1 \frac{x^n}{n+1} dx = \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$.
6. Ainsi, $\int_0^1 \frac{-\ln(x)}{1-x} dx = \sum_{n=0}^\infty \frac{1}{(n+1)^2} = \sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$.

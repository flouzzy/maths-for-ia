# Exercice 8 : Intégrale paramétrique et fonction Beta
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

### Énoncé

En développant l'expression $\frac{1}{1-x}$ en série entière, prouver par le TCM que $\int_0^1 \frac{\ln(x)}{x-1} dx = \frac{\pi^2}{6}$.

---
### Correction détaillée

1. Exprimons l'intégrande : pour $x \in ]0, 1[$, on remarque que $\frac{\ln(x)}{x-1} = \frac{-\ln(x)}{1-x}$. Comme $x \in ]0, 1[$, on a $-\ln(x) > 0$ et $1-x > 0$. Donc la fonction est strictement positive.
2. Développons le terme $\frac{1}{1-x}$ en série géométrique : pour $|x| < 1$, $\frac{1}{1-x} = \sum_{n=0}^{+\infty} x^n$.
3. Nous obtenons donc : $\frac{-\ln(x)}{1-x} = -\ln(x) \sum_{n=0}^{+\infty} x^n = \sum_{n=0}^{+\infty} -x^n \ln(x)$.
4. Posons $u_n(x) = -x^n \ln(x)$. Sur l'intervalle $]0, 1[$, ces fonctions sont mesurables et strictement positives.
5. Le corollaire du Théorème de Convergence Monotone s'applique pour cette série à termes positifs :
   $$\int_0^1 \left( \sum_{n=0}^{+\infty} -x^n \ln(x) \right) dx = \sum_{n=0}^{+\infty} \int_0^1 -x^n \ln(x) \, dx$$
6. Évaluons l'intégrale du terme général par intégration par parties. Posons $u = -\ln(x)$, $du = -1/x dx$, et $v' = x^n$, $v = \frac{x^{n+1}}{n+1}$.
   $$\int_0^1 -x^n \ln(x) \, dx = \left[ -\ln(x) \frac{x^{n+1}}{n+1} \right]_0^1 - \int_0^1 \frac{x^{n+1}}{n+1} \left(-\frac{1}{x}\right) dx$$
   Le terme de bord s'annule en $1$ (car $\ln(1)=0$) et en $0$ (par croissance comparée $\lim_{x \to 0} x^{n+1}\ln(x)=0$).
   Reste l'intégrale : $\int_0^1 \frac{x^n}{n+1} dx = \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$.
7. La somme devient alors :
   $$\sum_{n=0}^{+\infty} \frac{1}{(n+1)^2} = \sum_{k=1}^{+\infty} \frac{1}{k^2}$$
8. Cette série de Riemann célèbre, résolue par Euler (problème de Bâle), a pour somme $\frac{\pi^2}{6}$.
   Ainsi, l'égalité est rigoureusement prouvée par l'interversion de Beppo Levi.

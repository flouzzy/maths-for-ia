# Exercice 6 : Convergence d'une norme $L^p$ vers $L^\infty$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f(x) = x$ sur l'espace $X = [0, 1]$ muni de la mesure de Lebesgue $\lambda$.
1. Calculer $\|f\|_p$ pour $1 \le p < +\infty$.
2. Déterminer $\|f\|_\infty$.
3. Montrer que $\lim_{p \to +\infty} \|f\|_p = \|f\|_\infty$.

**Correction :**
1. Pour $1 \le p < +\infty$, $\|f\|_p^p = \int_0^1 |x|^p dx = \left[ \frac{x^{p+1}}{p+1} \right]_0^1 = \frac{1}{p+1}$.
Donc $\|f\|_p = \left( \frac{1}{p+1} \right)^{1/p} = (p+1)^{-1/p}$.

2. La fonction $f(x) = x$ est continue sur $[0, 1]$, donc son supremum essentiel est égal à son supremum classique.
$\|f\|_\infty = \sup_{x \in [0,1]} |x| = 1$.

3. Étudions la limite :
$\ln(\|f\|_p) = -\frac{1}{p} \ln(p+1)$.
Par croissances comparées, lorsque $p \to +\infty$, $\frac{\ln(p+1)}{p} \to 0$.
Donc $\lim_{p \to +\infty} \ln(\|f\|_p) = 0$, ce qui implique $\lim_{p \to +\infty} \|f\|_p = e^0 = 1$.
On a bien $\lim_{p \to +\infty} \|f\|_p = \|f\|_\infty$.

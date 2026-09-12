## Exercice 7 : Non-intégrabilité de sin(x)/x \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f(x) = \frac{\sin(x)}{x}$ sur $]0, +\infty[$ muni de la mesure de Lebesgue.
Montrer que $f$ n'est pas intégrable au sens de Lebesgue (c'est-à-dire $f \notin \mathcal{L}^1(]0, +\infty[)$).

**Correction :**
1. Il faut montrer que $\int_{]0, +\infty[} \left| \frac{\sin x}{x} \right| dx = +\infty$.
2. L'intégrale peut être décomposée en une somme sur des intervalles $[k\pi, (k+1)\pi]$ :
   $I = \sum_{k=0}^{\infty} \int_{k\pi}^{(k+1)\pi} \frac{|\sin x|}{x} dx$.
3. Sur l'intervalle $[k\pi, (k+1)\pi]$, on a $x \le (k+1)\pi$, donc $\frac{1}{x} \ge \frac{1}{(k+1)\pi}$.
4. Ainsi, $\int_{k\pi}^{(k+1)\pi} \frac{|\sin x|}{x} dx \ge \frac{1}{(k+1)\pi} \int_{k\pi}^{(k+1)\pi} |\sin x| dx$.
5. L'intégrale de $|\sin x|$ sur une période demi-entière est toujours 2 :
   $\int_{k\pi}^{(k+1)\pi} |\sin x| dx = 2$.
6. On obtient donc : $I \ge \sum_{k=0}^{\infty} \frac{2}{(k+1)\pi} = \frac{2}{\pi} \sum_{n=1}^{\infty} \frac{1}{n}$.
7. La série harmonique $\sum_{n=1}^{\infty} \frac{1}{n}$ diverge vers l'infini, donc l'intégrale diverge. $f \notin \mathcal{L}^1$.

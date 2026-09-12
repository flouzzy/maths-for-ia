## Exercice 8 : Limite d'une suite définie par intégrale \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Calculer $\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n \ln(x) dx$.

**Correction :**
On réécrit l'intégrale sur $]0, +\infty[$ avec une fonction indicatrice :
$I_n = \int_0^\infty f_n(x) dx$ avec $f_n(x) = \left(1 - \frac{x}{n}\right)^n \ln(x) \mathbf{1}_{[0, n]}(x)$.
1. **Convergence simple :** On sait que $\lim_{n \to \infty} \left(1 - \frac{x}{n}\right)^n = e^{-x}$. Ainsi, la limite simple est $f(x) = e^{-x} \ln(x)$.
2. **Domination :** On utilise l'inégalité $1 - u \le e^{-u}$ pour $u \in [0, 1]$.
   Donc $\left(1 - \frac{x}{n}\right)^n \le e^{-x}$ pour $0 \le x \le n$.
   On en déduit que $|f_n(x)| \le e^{-x} |\ln(x)| \mathbf{1}_{[0, n]}(x) \le e^{-x} |\ln(x)|$.
3. La fonction $g(x) = e^{-x} |\ln(x)|$ est-elle intégrable sur $]0, +\infty[$ ?
   En 0, $g(x) \sim |\ln(x)|$, dont l'intégrale impropre converge (primitive $x \ln(x) - x$).
   En $+\infty$, $x^2 g(x) = x^2 e^{-x} |\ln(x)| \to 0$, donc $g(x) = o(1/x^2)$, et l'intégrale converge.
4. Par conséquent, par le TCD, la limite de l'intégrale est l'intégrale de la limite :
   $\lim_{n \to \infty} I_n = \int_0^\infty e^{-x} \ln(x) dx$. (Cette intégrale vaut $-\gamma$, où $\gamma$ est la constante d'Euler-Mascheroni).

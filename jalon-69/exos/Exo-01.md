## Exercice 1 : Application directe : exponentielle \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Calculer la limite suivante :
$$ \lim_{n \to \infty} \int_0^{1} \left(1 - \frac{x}{n}\right)^n e^{x/2} dx $$

**Correction :**
1. Soit $f_n(x) = (1 - x/n)^n e^{x/2} \mathbf{1}_{[0, 1]}(x)$. Pour $x \in [0, 1]$ fixé et $n$ assez grand, $\ln(1 - x/n) \sim -x/n$, donc $n \ln(1 - x/n) \to -x$. Ainsi, $\lim_{n \to \infty} f_n(x) = e^{-x} e^{x/2} = e^{-x/2}$. La fonction limite est $f(x) = e^{-x/2}$.
2. Cherchons une domination. Pour $t \ge 0$, on sait que $1 - t \le e^{-t}$. Donc $(1 - x/n)^n \le e^{-x}$ pour $0 \le x \le n$.
Ainsi, $|f_n(x)| \le e^{-x} e^{x/2} = e^{-x/2}$ sur $[0, 1]$.
3. La fonction $g(x) = e^{-x/2} \mathbf{1}_{[0, 1]}(x)$ est continue donc mesurable, et intégrable sur $[0, 1]$ (car bornée sur un compact).
4. D'après le Théorème de Convergence Dominée (TCD), on peut intervertir limite et intégrale :
$$ \lim_{n \to \infty} \int_0^1 f_n(x) dx = \int_0^1 e^{-x/2} dx = \left[ -2 e^{-x/2} \right]_0^1 = 2(1 - e^{-1/2}). $$

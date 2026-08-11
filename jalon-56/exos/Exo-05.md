## Exercice 5 : Complétude et suites de Cauchy (Intermédiaire) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Soit $X$ complet et $f: X \to X$ une contraction (constante $k < 1$). Démontrer que $f$ admet au moins un point fixe en construisant une suite.

\textbf{Correction Détaillée :}
1. Soit $x_0 \in X$ quelconque. Posons la suite récurrente $x_{n+1} = f(x_n)$.
2. Évaluons la distance entre termes consécutifs : $d(x_{n+1}, x_n) = d(f(x_n), f(x_{n-1})) \leq k d(x_n, x_{n-1})$.
3. Par récurrence, $d(x_{n+1}, x_n) \leq k^n d(x_1, x_0)$.
4. Pour $p > q$, $d(x_p, x_q) \leq \sum_{i=q}^{p-1} d(x_{i+1}, x_i) \leq d(x_1, x_0) \sum_{i=q}^{p-1} k^i$.
5. Majorons par la série géométrique : $d(x_p, x_q) \leq d(x_1, x_0) \frac{k^q}{1-k}$.
6. Comme $k < 1$, $k^q \to 0$ quand $q \to \infty$. Pour tout $\epsilon > 0$, on peut trouver $N$ tel que pour $q \ge N$, cette quantité est $< \epsilon$.
7. La suite $(x_n)$ est donc de Cauchy. Comme $X$ est complet, elle converge vers $l \in X$.
8. Comme $f$ est continue, $l = \lim x_{n+1} = \lim f(x_n) = f(\lim x_n) = f(l)$. Le point $l$ est un point fixe.

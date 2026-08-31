## Exercice 4 : Limite d'intégrale de Gaussiennes tronquées \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f_n(x) = e^{-x^2} \chi_{[-n, n]}(x)$. Calculer $\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) dx$ en utilisant le TCM.

**Correction Détaillée :**
1. Posons $f_n(x) = e^{-x^2} \chi_{[-n, n]}(x)$. Pour tout $x$, $e^{-x^2} > 0$.
2. L'intervalle $[-n, n]$ est inclus dans $[-(n+1), n+1]$. Ainsi, $\chi_{[-n, n]}(x) \le \chi_{[-(n+1), n+1]}(x)$.
3. On en déduit que pour tout $x \in \mathbb{R}$, $f_n(x) \le f_{n+1}(x)$. La suite $(f_n)$ est donc positive et croissante.
4. La limite simple de $f_n(x)$ est $f(x) = e^{-x^2}$ car pour tout $x$, il existe $N$ tel que pour tout $n \ge N$, $x \in [-n, n]$.
5. Par le théorème de convergence monotone :
   $\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) dx = \int_{\mathbb{R}} \lim_{n \to \infty} f_n(x) dx = \int_{\mathbb{R}} e^{-x^2} dx$.
6. On sait que l'intégrale de Gauss $\int_{\mathbb{R}} e^{-x^2} dx$ vaut $\sqrt{\pi}$.
7. Ainsi, la limite cherchée est $\sqrt{\pi}$.

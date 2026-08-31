---
title: "Intégrale de série entière"
difficulty: $\bigstar\bigstar\star\star\star$
---
# Intégrale de série entière
**Énoncé :**
Montrer que $\int_0^1 \left( \sum_{n=1}^\infty x^n \right) dx = \sum_{n=1}^\infty \frac{1}{n+1} = +\infty$.

**Correction :**
1. Soit $u_n(x) = x^n$. Pour $x \in [0, 1]$, $u_n(x) \ge 0$.
2. Les fonctions $u_n$ sont mesurables et positives.
3. D'après le corollaire du Théorème de Convergence Monotone (sommation terme à terme de fonctions positives) :
   $\int_0^1 \left( \sum_{n=1}^\infty x^n \right) dx = \sum_{n=1}^\infty \int_0^1 x^n dx$.
4. Calculons l'intégrale : $\int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}$.
5. On obtient la série de terme général $\frac{1}{n+1}$, qui diverge. Ainsi, l'intégrale de la somme est bien $+\infty$.

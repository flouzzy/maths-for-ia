---
title: "Exercice 1"
---
## Exercice 1 : Calcul d'une intégrale avec paramètre $\bigstar$

**Énoncé :**
Pour $n \ge 1$, on pose $f_n(x) = \frac{x^n}{1+x^n}$ sur $[0,1]$.
Calculer la limite quand $n \to +\infty$ de $I_n = \int_0^1 f_n(x) dx$.

**Correction Détaillée :**
1. Pour tout $x \in [0, 1[$, on a $\lim_{n \to \infty} x^n = 0$. Donc $f_n(x) \xrightarrow{n \to \infty} 0$.
2. Pour $x=1$, $f_n(1) = 1/2$.
3. La fonction limite simple est $f(x) = 0$ presque partout sur $[0,1]$ (la mesure du singleton $\{1\}$ est nulle).
4. La suite $f_n(x)$ n'est pas clairement croissante pour tout $x$. Cependant, la suite de fonctions $g_n(x) = 1 - f_n(x) = \frac{1}{1+x^n}$ est mesurable et positive.
5. Remarquons que pour $x \in [0,1]$, $x^n \ge x^{n+1}$, donc $1+x^n \ge 1+x^{n+1}$, soit $\frac{1}{1+x^n} \le \frac{1}{1+x^{n+1}}$.
6. Ainsi, la suite $(g_n)$ est une suite \textbf{croissante} de fonctions mesurables positives, qui converge simplement vers $1$ sur $[0, 1[$.
7. D'après le théorème de convergence monotone appliqué à $g_n$ :
   $$\lim_{n \to \infty} \int_0^1 g_n(x) dx = \int_0^1 \left(\lim_{n \to \infty} g_n(x)\right) dx = \int_0^1 1 \, dx = 1$$
8. Comme $\int_0^1 g_n = \int_0^1 (1-f_n) = 1 - I_n$, on a $\lim (1 - I_n) = 1$, d'où $\lim_{n \to \infty} I_n = 0$.

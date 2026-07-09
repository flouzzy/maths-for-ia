# Exercice 7 : Limite en l'infini et interversion

**Difficulté :** $\star\star\star\star$

**Énoncé :**
Soit $f(x) = \sum_{n=1}^\infty \frac{x}{n(1+nx^2)}$. Calculer $\lim_{x \to +\infty} f(x)$.

**Démonstration :**
1. **Convergence simple :**
   Soit $u_n(x) = \frac{x}{n(1+nx^2)}$. Pour $x > 0$ fixé, $u_n(x) \sim \frac{x}{n^2 x^2} = \frac{1}{n^2 x}$.
   Comme la série de Riemann $\sum \frac{1}{n^2}$ converge, la série converge simplement sur $]0, +\infty[$.
2. **Limite de chaque terme :**
   Pour chaque $n \ge 1$, $\lim_{x \to +\infty} u_n(x) = \lim_{x \to +\infty} \frac{x}{n(1+nx^2)} = 0$.
3. **Recherche de convergence uniforme :**
   On souhaite intervertir limite et série. Il faut montrer la convergence uniforme sur un voisinage de $+\infty$, disons sur $[1, +\infty[$.
   Pour $x \ge 1$ :
   $$ 0 \le u_n(x) = \frac{x}{n(1+nx^2)} \le \frac{x}{n(nx^2)} = \frac{1}{n^2 x} \le \frac{1}{n^2} $$
   Donc $\|u_n\|_{\infty, [1, +\infty[} \le \frac{1}{n^2}$.
   La série $\sum \frac{1}{n^2}$ converge, ce qui prouve que $\sum u_n$ converge normalement, donc uniformément, sur $[1, +\infty[$.
4. **Interversion des limites :**
   Puisque la série converge uniformément sur $[1, +\infty[$, et que chaque fonction $u_n$ admet une limite finie quand $x \to +\infty$, le théorème d'interversion des limites (ou théorème de la double limite) s'applique :
   $$ \lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} \sum_{n=1}^\infty u_n(x) = \sum_{n=1}^\infty \left( \lim_{x \to +\infty} u_n(x) \right) = \sum_{n=1}^\infty 0 = 0 $$
$\blacksquare$

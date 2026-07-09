# Exercice 3 : Série alternée de fonctions

**Difficulté :** $\star\star$

**Énoncé :**
Étudier la convergence (simple, absolue, uniforme, normale) de la série $\sum_{n \ge 1} \frac{(-1)^n}{n + x^2}$ sur $\mathbb{R}$.

**Démonstration :**
1. **Convergence simple :**
   Soit $x \in \mathbb{R}$ fixé. La série $\sum \frac{(-1)^n}{n + x^2}$ est une série alternée.
   Posons $u_n(x) = \frac{1}{n + x^2}$.
   - Pour $x$ fixé, $u_n(x) > 0$.
   - $u_n(x)$ tend vers $0$ quand $n \to \infty$.
   - La suite $(u_n(x))_{n \ge 1}$ est décroissante puisque $n+1+x^2 > n+x^2 \implies \frac{1}{n+1+x^2} < \frac{1}{n+x^2}$.
   D'après le critère spécial des séries alternées (CSSA), la série converge simplement sur $\mathbb{R}$.

2. **Convergence absolue :**
   $| \frac{(-1)^n}{n + x^2} | = \frac{1}{n + x^2}$.
   Or, $n + x^2 \sim n$ quand $n \to \infty$. Puisque la série harmonique $\sum \frac{1}{n}$ diverge, la série $\sum \frac{1}{n+x^2}$ diverge.
   La série ne converge pas absolument, donc elle ne peut pas converger normalement.

3. **Convergence uniforme :**
   Par le CSSA, le reste d'ordre $N$, noté $R_N(x) = \sum_{n=N+1}^\infty \frac{(-1)^n}{n + x^2}$, est majoré en valeur absolue par la valeur absolue du premier terme négligé :
   $$ |R_N(x)| \le |u_{N+1}(x)| = \frac{1}{N+1+x^2} $$
   Or, pour tout $x \in \mathbb{R}$, on a :
   $$ \frac{1}{N+1+x^2} \le \frac{1}{N+1} $$
   Donc $\sup_{x \in \mathbb{R}} |R_N(x)| \le \frac{1}{N+1}$.
   Puisque $\lim_{N \to \infty} \frac{1}{N+1} = 0$, la suite des restes converge uniformément vers 0 sur $\mathbb{R}$.
   La série converge donc uniformément sur $\mathbb{R}$.
$\blacksquare$

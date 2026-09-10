## Exercice 10 : Problème ENS : Continuité de la transformée de Laplace \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f : \mathbb{R}^+ \to \mathbb{R}^+$ mesurable. On définit $F(s) = \int_0^\infty f(x) e^{-sx} dx$.
**Question :** Montrer que $\lim_{s \to 0^+} F(s) = \int_0^\infty f(x) dx$.

**Solution :**
1. Considérons une suite de réels $(s_n)$ strictement positive et décroissante vers $0$.
2. Pour chaque $n$, soit $g_n(x) = f(x) e^{-s_n x}$.
3. Comme $s_n \ge s_{n+1}$, on a $-s_n x \le -s_{n+1} x$, donc $e^{-s_n x} \le e^{-s_{n+1} x}$.
4. Puisque $f(x) \ge 0$, on a $g_n(x) \le g_{n+1}(x)$. La suite $(g_n)$ est croissante et positive.
5. Sa limite simple, quand $s_n \to 0$, est $g(x) = f(x) e^0 = f(x)$.
6. Par le théorème de Beppo Levi, $\lim_{n \to \infty} \int_0^\infty g_n(x) dx = \int_0^\infty f(x) dx$.
7. Ainsi, la limite continue de $F(s)$ en $0^+$ est bien l'intégrale de $f$, même si cette intégrale vaut $+\infty$. $\blacksquare$

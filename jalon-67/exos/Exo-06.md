# Exercice 6 : Intégrale de Gauss fractionnée \quad $\bigstar\bigstar\bigstar\bigstar\star$

Évaluer $\lim_{n \to \infty} \int_{0}^{n} \left(1 - \frac{x^2}{n^2}\right)^n dx$.

**Solution Détaillée :**
1. Soit $f_n(x) = \left(1 - \frac{x^2}{n^2}\right)^n \mathbf{1}_{[0, n]}(x)$.
2. La limite simple : pour $x \ge 0$, $\lim_{n \to \infty} f_n(x) = e^{-x^2}$.
3. Par un argument de convexité, $1 - u \le e^{-u}$ pour tout $u \in [0, 1]$. En posant $u = \frac{x^2}{n^2} \le 1$, on obtient :
   $\left(1 - \frac{x^2}{n^2}\right)^n \le (e^{-x^2/n^2})^n = e^{-x^2/n}$. (Ceci ne donne pas la croissance directement).
4. La suite $n \mapsto \left(1 - \frac{x^2}{n^2}\right)^n$ est bien croissante pour $n \ge x$.
5. Comme $f_n$ est positive et croît vers $e^{-x^2}$, le théorème de convergence monotone implique :
   $$ \lim_{n \to \infty} \int_{0}^{\infty} f_n(x) dx = \int_{0}^{\infty} e^{-x^2} dx $$
6. L'intégrale de Gauss donne $\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$.
7. Donc la limite vaut $\frac{\sqrt{\pi}}{2}$.

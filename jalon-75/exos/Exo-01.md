# Exercice 1 : Convergence dans $L^1$ vs Convergence ponctuelle
**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
On se place sur l'espace mesuré $([0,1], \mathcal{B}([0,1]), \lambda)$ avec $\lambda$ la mesure de Lebesgue.
Soit $f_n = n \mathbf{1}_{[0, 1/n]}$.
1. Montrer que $f_n$ converge ponctuellement vers une fonction $f$ que l'on déterminera.
2. Calculer $\|f_n - f\|_1$.
3. La suite $(f_n)_{n \ge 1}$ est-elle une suite de Cauchy dans $L^1([0,1])$ ? Justifiez rigoureusement en lien avec le théorème de Riesz-Fischer.

**Correction :**
1. Pour $x > 0$, il existe $N \in \mathbb{N}^*$ tel que $1/N < x$. Pour tout $n \ge N$, on a $x \notin [0, 1/n]$, donc $f_n(x) = 0$. Ainsi, pour tout $x \in ]0, 1]$, $\lim_{n \to +\infty} f_n(x) = 0$. Pour $x=0$, $f_n(0) = n \to +\infty$. Donc $f_n$ converge presque partout vers $f = 0$.
2. On a $\|f_n - f\|_1 = \int_0^1 |n \mathbf{1}_{[0, 1/n]}| \, dx = n \times \frac{1}{n} = 1$.
3. Puisque $\|f_n - 0\|_1 = 1 \neq 0$, la suite $(f_n)$ ne converge pas vers $0$ dans $L^1$. D'après le théorème de Riesz-Fischer, $L^1$ est complet. Si $(f_n)$ était de Cauchy dans $L^1$, elle convergerait dans $L^1$ vers une limite $g$. Par le théorème d'extraction, une sous-suite de $f_n$ convergerait p.p. vers $g$. Or $f_n \to 0$ p.p., donc par unicité de la limite p.p., on aurait $g = 0$. Mais on vient de voir que $f_n$ ne converge pas vers $0$ dans $L^1$. Par conséquent, par contraposée, $(f_n)$ n'est pas une suite de Cauchy dans $L^1$.

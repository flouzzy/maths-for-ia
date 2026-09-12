## Exercice 2 : Fatou avec pic s'écrasant à l'origine \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X = [0, 1]$ muni de la mesure de Lebesgue $\lambda$.
Soit $f_n(x) = n \mathbf{1}_{]0, 1/n[}(x)$.
1. Calculer $\int_{0}^{1} f_n d\lambda$.
2. Trouver $\liminf_{n \to \infty} f_n(x)$.
3. Le lemme de Fatou s'applique-t-il ? Comparer les intégrales.

**Correction :**
1. L'intégrale de l'indicatrice d'un intervalle est la longueur de l'intervalle. Donc, $\int_{0}^{1} f_n d\lambda = n \times (1/n) = 1$.
2. Pour $x=0$, $f_n(0) = 0$ pour tout $n$. Pour $x > 0$, il existe $N$ tel que pour tout $n \ge N$, $1/n \le x$, donc $f_n(x) = 0$. Ainsi, $f(x) = \liminf f_n(x) = 0$ pour tout $x \in [0,1]$.
3. Le lemme de Fatou s'applique puisque les $f_n$ sont mesurables et positives. On obtient $\int_{0}^{1} (\liminf f_n) d\lambda = 0$ et $\liminf \int_{0}^{1} f_n d\lambda = 1$. L'inégalité $0 \le 1$ est vérifiée de manière stricte.

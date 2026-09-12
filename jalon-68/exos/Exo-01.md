## Exercice 1 : Fatou avec masse fuyante vers l'infini \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X = \mathbb{R}$ muni de la mesure de Lebesgue $\lambda$.
Considérons la suite de fonctions $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$.
1. Déterminer la limite simple $f(x) = \lim_{n \to \infty} f_n(x)$ pour tout $x \in \mathbb{R}$.
2. Calculer $\int_{\mathbb{R}} f_n d\lambda$.
3. Vérifier la conclusion du lemme de Fatou et commenter l'inégalité.

**Correction :**
1. Pour tout $x \in \mathbb{R}$ fixé, pour $n > x$, on a $f_n(x) = \frac{1}{n}$. Ainsi, $\lim_{n \to \infty} f_n(x) = 0$. Donc $f(x) = 0$ partout.
2. $\int_{\mathbb{R}} f_n d\lambda = \frac{1}{n} \lambda([0, n]) = \frac{1}{n} \times n = 1$.
3. On a $\int_{\mathbb{R}} (\liminf f_n) d\lambda = \int_{\mathbb{R}} 0 d\lambda = 0$.
D'autre part, $\liminf \left( \int_{\mathbb{R}} f_n d\lambda \right) = \liminf (1) = 1$.
Le lemme de Fatou donne $0 \le 1$, l'inégalité est stricte. L'intégrale (la masse) de 1 "s'échappe vers l'infini".

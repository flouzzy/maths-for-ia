## Exercice 7 : Croissance de la primitive \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f$ une fonction intégrable positive sur $\mathbb{R}$. Posons $F(x) = \int_{-\infty}^x f(t) dt$. Démontrer rigoureusement que $\lim_{x \to +\infty} F(x) = \int_{\mathbb{R}} f(t) dt$.

**Correction Détaillée :**
1. Considérons toute suite croissante $(x_n)$ tendant vers $+\infty$.
2. Posons la suite de fonctions $g_n(t) = f(t) \chi_{]-\infty, x_n]}(t)$.
3. Comme $(x_n)$ est croissante, les intervalles $]-\infty, x_n]$ s'emboîtent : $]-\infty, x_n] \subset ]-\infty, x_{n+1}]$.
4. Donc $\chi_{]-\infty, x_n]}(t) \le \chi_{]-\infty, x_{n+1}]}(t)$. Puisque $f \ge 0$, on a $g_n(t) \le g_{n+1}(t)$.
5. La limite simple de $g_n(t)$ est $f(t) \chi_{\mathbb{R}}(t) = f(t)$ car pour tout $t \in \mathbb{R}$, il existe $N$ tel que pour tout $n \ge N$, $x_n > t$, et donc $t \in ]-\infty, x_n]$.
6. On applique le Théorème de Convergence Monotone :
   $\lim_{n \to \infty} \int_{\mathbb{R}} g_n(t) dt = \int_{\mathbb{R}} f(t) dt$.
7. Or $\int_{\mathbb{R}} g_n(t) dt = \int_{-\infty}^{x_n} f(t) dt = F(x_n)$.
8. Donc pour toute suite $(x_n) \uparrow +\infty$, $F(x_n)$ tend vers $\int_{\mathbb{R}} f(t) dt$, ce qui caractérise la limite $\lim_{x \to +\infty} F(x) = \int_{\mathbb{R}} f(t) dt$.

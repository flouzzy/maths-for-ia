# Exercice 2 : Passage à la limite avec une fonction indicatrice
**Difficulté :** $\bigstar\bigstar\star\star\star$

### Énoncé

Soit $f_n(x) = n \cdot \chi_{]0, \frac{1}{n}[}(x)$ pour $x \in \mathbb{R}$. La suite $(f_n)$ est-elle croissante ? Converge-t-elle ? Le théorème de convergence monotone s'applique-t-il pour justifier le calcul de $\lim_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda$ ?

---
### Correction détaillée

1. Étudions la convergence ponctuelle de la suite $(f_n)$. Soit $x \in \mathbb{R}$.
   - Si $x \le 0$, $f_n(x) = 0$ pour tout $n$, donc $\lim_n f_n(x) = 0$.
   - Si $x > 0$, il existe un rang $N$ tel que pour tout $n \ge N$, $\frac{1}{n} \le x$. Donc pour $n \ge N$, $x \notin ]0, \frac{1}{n}[$ et $f_n(x) = 0$. Ainsi, la limite ponctuelle de $f_n(x)$ est $f(x) = 0$ pour tout $x$.
2. Calculons l'intégrale de $f_n$ :
   $$\int_{\mathbb{R}} f_n \, d\lambda = \int_0^{\frac{1}{n}} n \, dx = n \left[ x \right]_0^{\frac{1}{n}} = n \cdot \frac{1}{n} = 1$$
3. Calculons l'intégrale de la limite $f$ :
   $$\int_{\mathbb{R}} f \, d\lambda = \int_{\mathbb{R}} 0 \, d\lambda = 0$$
4. Nous constatons que $\lim_n \int f_n = 1 \neq 0 = \int \lim_n f_n$. L'interversion de la limite et de l'intégrale n'est pas possible ici.
5. Le théorème de Beppo Levi ne s'applique pas car la suite de fonctions **n'est pas croissante**. Par exemple, pour $x = 0.5$, $f_1(0.5) = 1 \cdot \chi_{]0, 1[}(0.5) = 1$, mais $f_2(0.5) = 2 \cdot \chi_{]0, 0.5[}(0.5) = 0$. La suite des valeurs chute de 1 à 0. L'hypothèse de croissance est fondamentale.

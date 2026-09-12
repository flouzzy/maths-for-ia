## Exercice 5 : Un contre-exemple (masse fuyante) \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f_n(x) = n \mathbf{1}_{]0, 1/n[}(x)$ sur l'espace $[0, 1]$ muni de la mesure de Lebesgue.
1. Calculer $\lim_{n \to \infty} \int_0^1 f_n(x) dx$.
2. Calculer $\int_0^1 \lim_{n \to \infty} f_n(x) dx$.
3. Pourquoi le Théorème de Convergence Dominée ne s'applique-t-il pas ici ?

**Correction :**
1. Pour chaque $n$, $\int_0^1 f_n(x) dx = n \times \frac{1}{n} = 1$. Donc la limite est 1.
2. Pour $x > 0$ fixé, dès que $n > 1/x$, $f_n(x) = 0$. Donc la limite simple est $f(x) = 0$. L'intégrale de la limite est 0.
3. On a interversion illégitime ($1 \neq 0$). Le TCD ne s'applique pas car il n'existe pas de fonction dominatrice $g$ intégrable telle que $f_n \le g$ pour tout $n$.
En effet, si une telle $g$ existait, on aurait $g(x) \ge \sup_n f_n(x) = 1/x$. Or $x \mapsto 1/x$ n'est pas intégrable sur $[0, 1]$.

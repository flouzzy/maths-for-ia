## Exercice 6 : Lemme de Fatou - Preuve $\quad \bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(f_n)$ une suite dans $\mathcal{M}_+$. Montrer le lemme de Fatou: $\int \liminf f_n d\mu \le \liminf \int f_n d\mu$.

**Correction :**
Posons $g_k = \inf_{n \ge k} f_n$. Par définition, $(g_k)$ est une suite croissante de fonctions mesurables positives.
Et $\lim_{k \to \infty} g_k = \liminf f_n$.
D'après le théorème de convergence monotone, $\int \liminf f_n d\mu = \lim_{k \to \infty} \int g_k d\mu$.
Or, pour tout $n \ge k$, $g_k \le f_n$, donc $\int g_k d\mu \le \int f_n d\mu$.
Par conséquent, $\int g_k d\mu \le \inf_{n \ge k} \int f_n d\mu$.
En passant à la limite quand $k \to \infty$ :
$\lim_{k \to \infty} \int g_k d\mu \le \lim_{k \to \infty} \inf_{n \ge k} \int f_n d\mu = \liminf \int f_n d\mu$.
Ce qui conclut la preuve.

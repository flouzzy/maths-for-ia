## Exercice 5 : Lemme de Fatou via Beppo Levi \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(f_n)$ une suite de fonctions mesurables positives, pas nécessairement croissante. On pose $g_n = \inf_{k \ge n} f_k$.
**Question :** Utiliser Beppo Levi sur la suite $(g_n)$ pour démontrer le Lemme de Fatou : $\int \liminf f_n \le \liminf \int f_n$.

**Solution :**
1. La suite $g_n$ est croissante car $\inf_{k \ge n+1} f_k \ge \inf_{k \ge n} f_k$. Elle est positive car les $f_n$ le sont.
2. Sa limite ponctuelle est par définition la $\liminf f_n$.
3. D'après Beppo Levi, $\int (\liminf f_n) = \lim \int g_n = \liminf \int g_n$. (car la limite existe).
4. Par ailleurs, pour tout $k \ge n$, $g_n \le f_k$, donc $\int g_n \le \int f_k$.
5. Ainsi, $\int g_n \le \inf_{k \ge n} \int f_k$.
6. En prenant la limite quand $n \to \infty$ : $\lim \int g_n \le \lim_{n \to \infty} \inf_{k \ge n} \int f_k = \liminf \int f_n$.
7. On conclut : $\int \liminf f_n \le \liminf \int f_n$. $\blacksquare$

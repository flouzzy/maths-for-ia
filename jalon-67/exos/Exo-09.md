## Exercice 9 : Preuve alternative de Lemme de Fatou (Préambule) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions mesurables positives (pas nécessairement croissante). On pose $g_n(x) = \inf_{k \ge n} f_k(x)$.
1. Montrer que $(g_n)$ est croissante et positive.
2. Montrer que $\lim g_n = \liminf f_n$.
3. En déduire, via le TCM, que $\int \liminf f_n \le \liminf \int f_n$ (C'est le Lemme de Fatou).

**Correction Détaillée :**
1. Par définition, $g_n(x)$ est l'infimum sur l'ensemble $\{k \ge n\}$.
   $g_{n+1}(x)$ est l'infimum sur l'ensemble $\{k \ge n+1\}$.
   L'ensemble sur lequel on prend l'infimum est plus petit pour $g_{n+1}$, donc l'infimum est potentiellement plus grand : $g_n(x) \le g_{n+1}(x)$. De plus, $g_n \ge 0$ car $f_k \ge 0$.
2. Par définition de la limite inférieure, $\liminf f_n(x) = \lim_{n \to \infty} (\inf_{k \ge n} f_k(x)) = \lim_{n \to \infty} g_n(x)$.
3. Appliquons le TCM à la suite croissante de fonctions positives $(g_n)$ :
   $\int (\lim g_n) d\mu = \lim \int g_n d\mu$.
   Donc $\int (\liminf f_n) d\mu = \lim_{n \to \infty} \int \inf_{k \ge n} f_k d\mu$.
   Or, pour tout $k \ge n$, $g_n \le f_k$, donc par monotonie de l'intégrale, $\int g_n \le \int f_k$.
   Ainsi, $\int g_n \le \inf_{k \ge n} \int f_k$.
   En passant à la limite quand $n \to \infty$ :
   $\lim \int g_n \le \lim \inf_{k \ge n} \int f_k = \liminf \int f_n$.
   On conclut donc que $\int \liminf f_n \le \liminf \int f_n$.

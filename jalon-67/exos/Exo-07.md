# Exercice 7 : Lien avec le Lemme de Fatou \quad $\bigstar\bigstar\bigstar\star\star$

Utiliser Beppo Levi pour démontrer que si $f_n \ge 0$, $\int (\liminf f_n) \le \liminf (\int f_n)$ (Lemme de Fatou).

**Correction :**
Posons $g_n = \inf_{k \ge n} f_k$. La suite $(g_n)$ est croissante car on prend l'infimum sur un ensemble plus petit, et $g_n \ge 0$. Par Beppo Levi, $\int \lim g_n = \lim \int g_n$. Or $g_n \le f_n$, donc $\int g_n \le \int f_n$. D'où $\lim \int g_n = \liminf \int g_n \le \liminf \int f_n$. Puisque $\lim g_n = \liminf f_n$, le résultat est prouvé.

# Exercice 10 : Equivalence avec Fatou \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Démontrer le lemme de Fatou ($\int \liminf f_n \le \liminf \int f_n$) en admettant le théorème de Beppo Levi pour des fonctions positives.

## Correction Détaillée
On pose $g_k(x) = \inf_{n \ge k} f_n(x)$.
Par construction, $(g_k)$ est une suite croissante de fonctions mesurables positives.
De plus, $\lim_{k \to \infty} g_k(x) = \sup_{k} \inf_{n \ge k} f_n(x) = \liminf_{n \to \infty} f_n(x)$.
On applique Beppo Levi à la suite $(g_k)$ : $\int \liminf f_n = \int \lim g_k = \lim \int g_k = \liminf \int g_k$.
Comme $g_k \le f_n$ pour tout $n \ge k$, on a $\int g_k \le \int f_n$ pour $n \ge k$.
Donc $\int g_k \le \inf_{n \ge k} \int f_n$.
En prenant la limite sur $k$, on obtient $\lim \int g_k \le \liminf \int f_n$.
Ainsi, $\int \liminf f_n \le \liminf \int f_n$.

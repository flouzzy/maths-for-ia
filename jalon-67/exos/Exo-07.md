# Exercice 7 : Théorème de convergence monotone décroissante ?

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions mesurables, à valeurs réelles (pas infinies), positives, et **décroissantes** ($f_n \ge f_{n+1}$).
Montrer que si $f_1$ est intégrable ($\int f_1 < +\infty$), alors :
$$\int \lim_{n\to\infty} f_n = \lim_{n\to\infty} \int f_n$$
Donner un contre-exemple si $f_1$ n'est pas intégrable.

**Solution Détaillée :**
1. **Preuve de l'assertion :**
Soit $f(x) = \lim_{n\to\infty} f_n(x)$ (limite décroissante d'une suite positive).
Posons $g_n = f_1 - f_n$.
- Comme la suite $(f_n)$ est décroissante, la suite $(g_n)$ est **croissante**.
- De plus, $g_n \ge 0$ car $f_1 \ge f_n$.
- $g_n \to f_1 - f$ simplement.
On peut appliquer Beppo Levi à la suite $(g_n)$ :
$$\int (f_1 - f) = \lim_{n\to\infty} \int (f_1 - f_n)$$
Comme $f_1$ est intégrable, les intégrales sont des nombres réels finis (linéarité de l'intégrale garantie).
$$\int f_1 - \int f = \int f_1 - \lim_{n\to\infty} \int f_n$$
En soustrayant le terme fini $\int f_1$, on obtient $\int f = \lim \int f_n$.

2. **Contre-exemple (si $f_1$ non intégrable) :**
Sur $\mathbb{R}$ muni de la mesure de Lebesgue, posons $f_n(x) = \mathbf{1}_{[n, +\infty[}(x)$.
- $f_n(x)$ est décroissante, car si $x \ge n+1$, alors $x \ge n$, donc $[n+1, +\infty[ \subset [n, +\infty[$.
- La limite est $f(x) = \lim \mathbf{1}_{[n, +\infty[}(x) = 0$ pour tout $x$. Donc $\int f = 0$.
- Cependant, $\int f_n = \int_n^{+\infty} 1 dx = +\infty$ pour tout $n$. Donc $\lim \int f_n = +\infty$.
On a donc $0 \neq +\infty$. La condition d'intégrabilité de la borne supérieure ($f_1$) est absolument capitale dans la version "décroissante".

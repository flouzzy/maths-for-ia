# Exercice 9 : Une variante du Théorème de Dini

## Énoncé
Soit $(f_n)$ une suite de fonctions continues sur un compact $K$.
On suppose que pour tout $x \in K$, la suite $(f_n(x))$ est croissante et converge vers une limite continue $f(x)$.
Montrer rigoureusement (sans citer directement Dini) que la convergence est uniforme.

## Correction Détaillée

On pose $g_n = f - f_n$. Les fonctions $g_n$ sont continues (car $f$ et $f_n$ le sont).
Pour tout $x \in K$, $(f_n(x))$ est croissante vers $f(x)$, donc $(g_n(x))$ est décroissante vers $0$.
Soit $\epsilon > 0$. Pour chaque $x \in K$, $\lim_{n \to \infty} g_n(x) = 0$, donc il existe $N_x$ tel que $0 \le g_{N_x}(x) < \epsilon/2$.
Comme $g_{N_x}$ est continue en $x$, il existe un voisinage ouvert $V_x$ de $x$ tel que pour tout $y \in V_x$, $g_{N_x}(y) < \epsilon$.
La famille $(V_x)_{x \in K}$ forme un recouvrement ouvert du compact $K$.
Il existe donc un sous-recouvrement fini $V_{x_1}, \dots, V_{x_k}$.
Soit $N = \max(N_{x_1}, \dots, N_{x_k})$.
Soit $y \in K$. Il existe $i \in \{1, \dots, k\}$ tel que $y \in V_{x_i}$.
Comme la suite $(g_n)$ est décroissante, pour $n \ge N \ge N_{x_i}$, on a :
$0 \le g_n(y) \le g_N(y) \le g_{N_{x_i}}(y) < \epsilon$.
Ainsi, pour tout $n \ge N$ et pour tout $y \in K$, $0 \le f(y) - f_n(y) < \epsilon$.
Cela prouve que $\|f - f_n\|_\infty \to 0$, donc la convergence est uniforme.

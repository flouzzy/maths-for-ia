### Exercice 6 : Théorème de Dini \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions continues sur le segment $[a, b]$, convergeant simplement vers une fonction $f$ continue. Supposons que pour tout $x \in [a, b]$, la suite $(f_n(x))$ est décroissante. Montrer que la convergence est uniforme.

**Correction :**
Ceci est le théorème de Dini. Posons $g_n = f_n - f$. Les $g_n$ sont continues, la suite $(g_n(x))$ décroît vers $0$ pour chaque $x$. Soit $\epsilon > 0$.
Pour chaque $x \in [a, b]$, il existe un rang $N(x)$ tel que $0 \le g_{N(x)}(x) < \epsilon$.
Par continuité de $g_{N(x)}$, il existe un voisinage ouvert $V_x$ de $x$ tel que pour tout $y \in V_x$, $g_{N(x)}(y) < \epsilon$.
La famille $\{V_x \mid x \in [a, b]\}$ forme un recouvrement ouvert du compact $[a, b]$. Il en existe un sous-recouvrement fini $V_{x_1}, \dots, V_{x_k}$.
Posons $N = \max(N(x_1), \dots, N(x_k))$.
Pour $n \ge N$ et $y \in [a, b]$, $y$ appartient à un certain $V_{x_i}$. Comme la suite est décroissante en $n$ :
$$ 0 \le g_n(y) \le g_N(y) \le g_{N(x_i)}(y) < \epsilon $$
Donc $\sup_{[a,b]} |f_n - f| < \epsilon$ pour $n \ge N$. La convergence est uniforme.

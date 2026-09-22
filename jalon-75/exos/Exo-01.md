\subsection*{Exercice 1 : Bosse glissante et non-convergence presque partout \quad $\bigstar$}
**Énoncé :**
On considère sur $X = [0,1]$ muni de la mesure de Lebesgue la suite de fonctions définie par $f_n = \mathbf{1}_{[n/2^k, (n+1)/2^k]}$, où $n$ parcourt les entiers et $k$ est tel que $2^k \le n < 2^{k+1}$.
1. Montrer que $f_n$ converge vers $0$ dans $L^1([0,1])$.
2. Montrer que pour tout $x \in [0,1]$, la suite $f_n(x)$ ne converge pas vers $0$.
3. Extraire une sous-suite de $f_n$ qui converge presque partout vers $0$.

**Correction détaillée :**
1. Pour $2^k \le n < 2^{k+1}$, l'intervalle a pour longueur $1/2^k$. Ainsi, $\|f_n\|_1 = \int_0^1 |f_n(t)| \, dt = 1/2^k$. Comme $k \to \infty$ lorsque $n \to \infty$, on a bien $\lim_{n \to \infty} \|f_n\|_1 = 0$. Donc $f_n$ converge vers 0 dans $L^1$.
2. Pour tout $x \in [0,1]$, pour chaque $k$, il existe un unique $n \in [2^k, 2^{k+1}-1]$ tel que $x \in [n/2^k, (n+1)/2^k]$. Donc pour ce $n$, $f_n(x) = 1$. Ainsi, $f_n(x) = 1$ pour une infinité de valeurs de $n$, et $f_n(x) = 0$ pour une infinité de valeurs de $n$. La suite $(f_n(x))$ ne converge donc en aucun point $x$.
3. On choisit la sous-suite correspondant à $n_k = 2^k$, soit $g_k = f_{2^k} = \mathbf{1}_{[1, 1+1/2^k]}$. (ou on peut extraire $g_k = f_{n_k}$ telle que l'intervalle est toujours $[0, 1/2^k]$). Prenons $g_k = \mathbf{1}_{[0, 1/2^k]}$. Pour $x > 0$, il existe $K$ tel que pour $k \ge K$, $1/2^k < x$, donc $g_k(x) = 0$. La suite $g_k(x)$ converge donc vers $0$ pour tout $x \in ]0,1]$, soit presque partout. \qed

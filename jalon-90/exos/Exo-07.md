# Exercice 07

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $W_n$ distribuée uniformément sur $[-n, n]$. Considérons la suite normée $V_n = \frac{W_n}{n}$.
Vers quelle loi la suite $V_n$ converge-t-elle ? Démontrez-le formellement à l'aide des fonctions de répartition.

**Correction :**
Déterminons d'abord la loi de $V_n$. Pour tout $x \in [-1, 1]$, on a :
$$ F_{V_n}(x) = \mathbb{P}(V_n \le x) = \mathbb{P}\left(\frac{W_n}{n} \le x\right) = \mathbb{P}(W_n \le nx) $$
Puisque $W_n$ suit $\mathcal{U}([-n, n])$, sa densité est $\frac{1}{2n}$ sur cet intervalle.
$$ \mathbb{P}(W_n \le nx) = \int_{-n}^{nx} \frac{1}{2n} dt = \frac{nx - (-n)}{2n} = \frac{n(x+1)}{2n} = \frac{x+1}{2} $$
Ainsi, pour tout $x \in [-1, 1]$, $F_{V_n}(x) = \frac{x+1}{2}$, indépendamment de $n$.
Pour $x < -1$, $F_{V_n}(x) = 0$, et pour $x > 1$, $F_{V_n}(x) = 1$.

Puisque $F_{V_n}(x)$ est constante par rapport à $n$, la limite est exactement cette même fonction :
$$ \lim_{n \to \infty} F_{V_n}(x) = \begin{cases} 0 & \text{si } x < -1 \\ \frac{x+1}{2} & \text{si } -1 \le x \le 1 \\ 1 & \text{si } x > 1 \end{cases} $$
On reconnaît la fonction de répartition d'une variable aléatoire uniforme sur $[-1, 1]$.
Ainsi, $V_n$ converge en loi vers $V \sim \mathcal{U}([-1, 1])$. En fait, toutes les $V_n$ ont exactement cette loi.

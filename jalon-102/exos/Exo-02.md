$\bigstar\bigstar\star\star\star$
**Énoncé :** Convergence faible et convergence forte en dimension finie.
Soit $E$ un espace vectoriel normé de dimension finie. Démontrer que toute suite faiblement convergente est fortement convergente.

**Correction Détaillée :**
Soit $(x_n)_{n \in \mathbb{N}}$ une suite convergeant faiblement vers $x \in E$.
Puisque $E$ est de dimension finie, disons $d$, il existe une base $e_1, \dots, e_d$ de $E$.
Les formes linéaires coordonnées $L_i : E \to \mathbb{K}$, définies par $L_i(\sum_{j=1}^d \alpha_j e_j) = \alpha_i$, sont continues.
Par hypothèse de convergence faible, pour chaque $i \in \{1, \dots, d\}$, on a $\lim_{n \to \infty} L_i(x_n) = L_i(x)$.
Écrivons $x_n = \sum_{i=1}^d x_{n,i} e_i$ et $x = \sum_{i=1}^d x_i e_i$. La limite précédente se réécrit $\lim_{n \to \infty} x_{n,i} = x_i$ pour tout $i$.
La convergence coordonnée par coordonnée implique la convergence forte dans tout espace de dimension finie (toutes les normes y étant équivalentes, on peut par exemple utiliser la norme infini ou la norme euclidienne).
Ainsi, $\|x_n - x\| \to 0$ lorsque $n \to \infty$. La suite converge fortement.

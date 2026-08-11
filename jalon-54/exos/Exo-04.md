## Exercice 4 : Compacité et distance au bord \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :** Soit $X$ un espace métrique compact, et $(U_i)_{i \in I}$ un recouvrement ouvert de $X$. Démontrer le lemme de Lebesgue : il existe un $\delta > 0$ tel que toute boule de rayon $\delta$ est entièrement contenue dans au moins l'un des ouverts $U_i$.

**Correction Détaillée :**
Par l'absurde, supposons qu'un tel $\delta$ n'existe pas.
Cela signifie que pour tout $\delta > 0$, il existe un point $x \in X$ tel que la boule ouverte $B(x, \delta)$ n'est contenue dans aucun des $U_i$.
En prenant $\delta_n = \frac{1}{n}$ pour $n \in \mathbb{N}^*$, on construit une suite $(x_n)_{n \ge 1}$ telle que pour tout $n$, $B(x_n, \frac{1}{n})$ n'est incluse dans aucun $U_i$.
L'espace $X$ étant métrique compact, il est séquentiellement compact. Il existe donc une sous-suite $(x_{\phi(n)})$ convergeant vers un point $l \in X$.
Puisque $(U_i)_{i \in I}$ recouvre $X$, il existe un $i_0 \in I$ tel que $l \in U_{i_0}$.
L'ensemble $U_{i_0}$ étant ouvert, il existe un rayon $r > 0$ tel que $B(l, r) \subset U_{i_0}$.
Puisque $x_{\phi(n)} \to l$, la distance $d(x_{\phi(n)}, l)$ tend vers 0. Soit $N$ suffisamment grand tel que pour tout $n \ge N$, on ait $d(x_{\phi(n)}, l) < \frac{r}{2}$ et $\frac{1}{\phi(n)} < \frac{r}{2}$.
Pour un tel $n$, si $y \in B\left(x_{\phi(n)}, \frac{1}{\phi(n)}\right)$, l'inégalité triangulaire donne :
$d(y, l) \le d(y, x_{\phi(n)}) + d(x_{\phi(n)}, l) < \frac{1}{\phi(n)} + \frac{r}{2} < \frac{r}{2} + \frac{r}{2} = r$.
Donc $y \in B(l, r) \subset U_{i_0}$.
On en déduit que la boule entière $B\left(x_{\phi(n)}, \frac{1}{\phi(n)}\right)$ est incluse dans $U_{i_0}$, ce qui contredit formellement la définition de la suite $(x_n)$.
L'hypothèse initiale est donc fausse, et le nombre de Lebesgue $\delta$ existe bien.
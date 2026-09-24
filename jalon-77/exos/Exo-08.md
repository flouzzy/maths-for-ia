## Exercice 8 : Approximation de fonctions caractéristiques d'ouverts \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $U$ un ouvert de mesure finie dans $\mathbb{R}$. Construire explicitement une suite de fonctions continues $g_n$ qui approxime $\mathbf{1}_U$ dans $L^1(\mathbb{R})$ en utilisant la notion géométrique de distance à la frontière.

**Correction :**
Puisque $U$ est ouvert, son complémentaire $F = \mathbb{R} \setminus U$ est fermé.
Considérons la fonction distance au fermé $F$ :
$d(x, F) = \inf_{y \in F} |x - y|$.
La fonction $d(\cdot, F)$ est continue (et même $1$-lipschitzienne). De plus, $d(x, F) = 0$ si et seulement si $x \in F$, c'est-à-dire si $x \notin U$.
Ainsi, $d(x, F) > 0$ pour tout $x \in U$.

Définissons la suite de fonctions $g_n(x) = \min(1, n \cdot d(x, F))$.
Pour tout $n$, $g_n$ est continue, car elle est le minimum de deux fonctions continues.
Si $x \notin U$ ($x \in F$), $d(x, F) = 0$, donc $g_n(x) = 0$.
Si $x \in U$, $d(x, F) > 0$. Pour $n$ suffisamment grand (dès que $n > 1/d(x, F)$), $n \cdot d(x, F) > 1$, donc $g_n(x) = 1$.
La suite $(g_n)$ converge ponctuellement vers $\mathbf{1}_U(x)$ pour tout $x \in \mathbb{R}$.

La suite est dominée : $0 \le g_n(x) \le \mathbf{1}_U(x)$ pour tout $x$.
Puisque $\mathbf{1}_U \in L^1(\mathbb{R})$ (car $U$ est de mesure finie), le Théorème de Convergence Dominée s'applique.
$\lim_{n \to \infty} \int_{\mathbb{R}} |g_n(x) - \mathbf{1}_U(x)| dx = \int_{\mathbb{R}} \lim_{n \to \infty} (\mathbf{1}_U(x) - g_n(x)) dx = \int_{\mathbb{R}} 0 \, dx = 0$.
Ainsi, $\| g_n - \mathbf{1}_U \|_1 \to 0$. Ceci démontre constructivement la densité des fonctions continues pour l'indicatrice d'un ouvert.

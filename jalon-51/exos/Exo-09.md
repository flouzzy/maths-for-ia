## Exercice 9 : Distance de Hausdorff \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique et $P, Q$ deux parties non vides bornées. On définit la distance d'un point $x$ à $P$ par $d(x, P) = \inf_{p \in P} d(x, p)$.
Montrer que l'application $x \mapsto d(x, P)$ est $1$-lipschitzienne (et donc continue).

**Correction :**
Soient $x, y \in X$. Prenons $p \in P$. Par l'inégalité triangulaire :
$$ d(x, p) \le d(x, y) + d(y, p) $$
Passons à la borne inférieure par rapport à $p \in P$. Puisque $d(x, y)$ ne dépend pas de $p$, on peut le sortir de l'infimum :
$$ \inf_{p \in P} d(x, p) \le \inf_{p \in P} [d(x, y) + d(y, p)] = d(x, y) + \inf_{p \in P} d(y, p) $$
Ce qui se réécrit :
$$ d(x, P) \le d(x, y) + d(y, P) \implies d(x, P) - d(y, P) \le d(x, y) $$
En échangeant les rôles de $x$ et $y$, on obtient symétriquement :
$$ d(y, P) - d(x, P) \le d(y, x) = d(x, y) $$
En combinant les deux, on a :
$$ |d(x, P) - d(y, P)| \le d(x, y) $$
L'application est bien $1$-lipschitzienne. $\blacksquare$

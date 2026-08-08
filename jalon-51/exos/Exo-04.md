## Exercice 4 : Continuité de la distance \quad $\bigstar\bigstar$

**Énoncé :** Soit $(X, d)$ un espace métrique. Démontrer que l'application $x \mapsto d(a, x)$ est continue sur $X$, c'est-à-dire que $|d(a, x) - d(a, y)| \le d(x, y)$.

**Correction :** Soient $a, x, y \in X$.
Par l'inégalité triangulaire appliquée aux points $a, x, y$ :
$d(a, x) \le d(a, y) + d(y, x) = d(a, y) + d(x, y)$ (par symétrie).
Donc $d(a, x) - d(a, y) \le d(x, y)$.

En intervertissant les rôles de $x$ et $y$ :
$d(a, y) \le d(a, x) + d(x, y)$, donc $d(a, y) - d(a, x) \le d(x, y)$, ce qui s'écrit $-(d(a, x) - d(a, y)) \le d(x, y)$.

En combinant les deux inégalités, on obtient la valeur absolue :
$|d(a, x) - d(a, y)| \le d(x, y)$.
Cette propriété montre que l'application distance à un point est $1$-lipschitzienne, donc uniformément continue.

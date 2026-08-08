## Exercice 6 : Distance de Hausdorff (Intro) \quad $\bigstar\bigstar\star$

**Énoncé :** Soit $X$ un espace métrique. Pour un point $x \in X$ et une partie non vide $A \subset X$, on définit $d(x, A) = \inf_{a \in A} d(x, a)$. Démontrer que $x \mapsto d(x, A)$ est $1$-lipschitzienne.

**Correction :** Soient $x, y \in X$. Pour tout $a \in A$, on a par inégalité triangulaire :
$d(x, a) \le d(x, y) + d(y, a)$.
En passant à l'infimum sur $a \in A$ du membre de gauche, tout en gardant $a$ fixé à droite, on a :
$\inf_{a \in A} d(x, a) \le d(x, y) + d(y, a)$ ce qui s'écrit $d(x, A) \le d(x, y) + d(y, a)$.
Puisque cette inégalité est vraie pour tout $a \in A$, le terme de gauche est un minorant de l'ensemble $\{ d(x, y) + d(y, a) \mid a \in A \}$.
La plus grande borne inférieure (l'infimum) de cet ensemble est donc supérieure ou égale à $d(x, A)$.
Donc : $d(x, A) \le d(x, y) + \inf_{a \in A} d(y, a) = d(x, y) + d(y, A)$.
Ce qui donne $d(x, A) - d(y, A) \le d(x, y)$.
Par symétrie en échangeant $x$ et $y$, on obtient $|d(x, A) - d(y, A)| \le d(x, y)$, démontrant la propriété de contraction de Lipschitz.

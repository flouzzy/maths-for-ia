## Exercice 2 : Inégalité triangulaire inversée \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique. Démontrer rigoureusement que pour tous $x, y, z \in X$ :
$$ |d(x, z) - d(y, z)| \le d(x, y) $$

**Correction :**
Nous devons montrer cette double inégalité. Utilisons l'inégalité triangulaire standard.
1. D'une part, évaluons $d(x, z)$. En passant par $y$, nous avons :
   $$ d(x, z) \le d(x, y) + d(y, z) $$
   En soustrayant $d(y, z)$ de chaque côté, nous obtenons :
   $$ d(x, z) - d(y, z) \le d(x, y) $$
2. D'autre part, évaluons $d(y, z)$. En passant par $x$, nous avons :
   $$ d(y, z) \le d(y, x) + d(x, z) $$
   Par symétrie, $d(y, x) = d(x, y)$. Ainsi :
   $$ d(y, z) - d(x, z) \le d(x, y) $$
   Ce qui s'écrit également :
   $$ -(d(x, z) - d(y, z)) \le d(x, y) $$
3. Les deux inégalités combinées affirment que la quantité $d(x, z) - d(y, z)$ est bornée supérieurement par $d(x, y)$ et inférieurement par $-d(x, y)$.
   Ceci équivaut exactement à la valeur absolue :
   $$ |d(x, z) - d(y, z)| \le d(x, y) $$
La démonstration est achevée. $\blacksquare$

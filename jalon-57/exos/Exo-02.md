# Exercice 2 : Unicité du point fixe sans contractance stricte sur un compact
**Niveau :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique compact, et $f : X \to X$ une application continue telle que, pour tous $x, y \in X$ avec $x \neq y$, on ait $d(f(x), f(y)) < d(x, y)$.
Démontrer, en utilisant la compacité (et non le théorème de Banach), que $f$ admet un unique point fixe.

**Démonstration pas à pas :**
Considérons la fonction $g : X \to \mathbb{R}$ définie par $g(x) = d(x, f(x))$.
1. La distance $d$ est continue sur $X \times X$, et l'application $x \mapsto (x, f(x))$ est continue de $X$ vers $X \times X$ puisque $f$ est continue. Par composition, la fonction $g$ est continue sur $X$.
2. Puisque $X$ est un espace métrique compact et $g$ est une fonction continue à valeurs réelles, le théorème des bornes atteintes (Weierstrass) affirme que $g$ atteint son minimum global sur $X$. Il existe donc un point $x^* \in X$ tel que pour tout $x \in X$, $g(x^*) \leq g(x)$.
3. Supposons par l'absurde que $f(x^*) \neq x^*$, c'est-à-dire que $g(x^*) = d(x^*, f(x^*)) > 0$.
   Appliquons alors l'hypothèse de l'énoncé aux points $x = x^*$ et $y = f(x^*)$ (qui sont distincts par hypothèse) :
   $d(f(x^*), f(f(x^*))) < d(x^*, f(x^*))$
   Ceci se réécrit en termes de la fonction $g$ :
   $g(f(x^*)) < g(x^*)$
   Mais cela contredit la définition de $x^*$ comme point minimisant la fonction $g$.
   L'hypothèse $f(x^*) \neq x^*$ est donc fausse. On conclut que $f(x^*) = x^*$, ce qui prouve l'existence d'un point fixe.
4. L'unicité est triviale : si $y^*$ est un autre point fixe distinct de $x^*$, alors $d(x^*, y^*) = d(f(x^*), f(y^*))$. Or, par hypothèse, si $x^* \neq y^*$, on devrait avoir $d(f(x^*), f(y^*)) < d(x^*, y^*)$, ce qui implique $d(x^*, y^*) < d(x^*, y^*)$, une absurdité évidente. Donc $x^* = y^*$.

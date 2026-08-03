---
title: "Exercice 2 : Preuve de non-existence de limite (Directions)"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 2 : Preuve de non-existence de limite (Directions)

## Énoncé

Prouver que la fonction $g$ n'admet pas de limite en $(0,0)$ :
$$ g(x, y) = \frac{x y^2}{x^2 + y^4} $$

## Solution détaillée

1. **Compréhension du problème** :
   Pour démontrer qu'une fonction n'admet pas de limite en un point, il suffit de trouver deux chemins différents approchant ce point pour lesquels la fonction tend vers des valeurs distinctes.

2. **Premier chemin : l'axe des abscisses ($y = 0$)** :
   Considérons la limite le long de l'axe des abscisses.
   Pour $x \neq 0$, nous avons :
   $$ g(x, 0) = \frac{x \cdot 0^2}{x^2 + 0^4} = \frac{0}{x^2} = 0 $$
   Donc, $\lim_{x \to 0} g(x, 0) = 0$.

3. **Deuxième chemin : la parabole ($x = y^2$)** :
   L'idée est de rendre les termes du dénominateur du même degré par rapport à $y$. Si on pose $x = y^2$, alors $x^2 = y^4$.
   Approchons l'origine le long de cette parabole. Pour $y \neq 0$, nous avons :
   $$ g(y^2, y) = \frac{y^2 \cdot y^2}{(y^2)^2 + y^4} = \frac{y^4}{y^4 + y^4} = \frac{y^4}{2y^4} = \frac{1}{2} $$
   Donc, $\lim_{y \to 0} g(y^2, y) = \frac{1}{2}$.

4. **Conclusion formelle** :
   Puisque nous avons trouvé deux trajectoires différentes (la droite $y=0$ et la parabole $x=y^2$) menant au point $(0,0)$ et produisant des limites différentes ($0$ et $\frac{1}{2}$), la limite globale $\lim_{(x,y) \to (0,0)} g(x, y)$ **n'existe pas**.

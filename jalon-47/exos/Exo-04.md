# Point critique avec matrice dégénérée

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f(x, y) = x^4 + y^4$.
1. Déterminez les points critiques et la hessienne en ces points.
2. Pourquoi la hessienne ne permet-elle pas de conclure directement quant à la nature du point critique ? Concluez par un autre moyen.

**Correction mathématique détaillée :**

1. **Calculs préliminaires :**
   $\nabla f(x, y) = (4x^3, 4y^3)^T$.
   L'unique point critique est $(0, 0)$.
   Les dérivées secondes sont :
   $$\frac{\partial^2 f}{\partial x^2} = 12x^2, \quad \frac{\partial^2 f}{\partial y^2} = 12y^2, \quad \frac{\partial^2 f}{\partial x \partial y} = 0$$
   En $(0, 0)$, la matrice hessienne est la matrice nulle :
   $$H_f(0, 0) = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$

2. **Analyse de la situation :**
   Le déterminant est nul, et les valeurs propres sont nulles. La matrice n'est ni définie positive, ni définie négative, ni n'admet des valeurs propres de signes opposés stricte. Le test des dérivées secondes est donc **inconclusif** (cas dégénéré).

   Cependant, il suffit d'observer directement la fonction. Pour tout $(x, y) \neq (0,0)$, on a $x^4 + y^4 > 0$. Or $f(0,0) = 0$. Ainsi, par définition élémentaire, l'origine est un **minimum global strict**.

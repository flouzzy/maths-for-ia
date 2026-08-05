# Calcul basique de gradient et hessienne d'un polynôme

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f(x, y) = x^2 + 3xy + 2y^2$.
1. Déterminez le gradient $\nabla f(x, y)$.
2. Déterminez la matrice hessienne $H_f(x, y)$.
3. Montrez que le seul point critique est l'origine et étudiez sa nature.

**Correction mathématique détaillée :**

1. **Calcul du gradient :**
   Les dérivées partielles premières sont :
   $$\frac{\partial f}{\partial x}(x, y) = 2x + 3y$$
   $$\frac{\partial f}{\partial y}(x, y) = 3x + 4y$$
   Ainsi, $\nabla f(x, y) = (2x + 3y, 3x + 4y)^T$.

2. **Calcul de la matrice hessienne :**
   On dérive une seconde fois :
   $$\frac{\partial^2 f}{\partial x^2} = 2, \quad \frac{\partial^2 f}{\partial y^2} = 4, \quad \frac{\partial^2 f}{\partial x \partial y} = 3$$
   La matrice hessienne, constante, est :
   $$H_f = \begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$$

3. **Recherche de points critiques et classification :**
   $\nabla f(x, y) = (0, 0)$ implique le système $2x+3y=0$ et $3x+4y=0$. Puisque le déterminant de ce système linéaire est $2\times 4 - 3\times 3 = -1 \neq 0$, la seule solution est $(x, y) = (0, 0)$.
   Le déterminant de la hessienne vaut $2 \times 4 - 3^2 = 8 - 9 = -1$.
   Puisque le déterminant de la hessienne est strictement négatif, la forme quadratique associée possède des valeurs propres de signes opposés.
   Le point $(0,0)$ est donc un **point selle**.

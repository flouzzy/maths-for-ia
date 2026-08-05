# Hessienne d'une fonction exponentielle

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f(x, y) = e^{-(x^2 + y^2)}$.
1. Calculez les dérivées partielles premières et secondes de $f$.
2. Écrivez la matrice hessienne à l'origine $(0,0)$ et déduisez-en la nature du point critique.

**Correction mathématique détaillée :**

1. **Calcul des dérivées partielles :**
   $$\frac{\partial f}{\partial x} = -2x e^{-(x^2 + y^2)}, \quad \frac{\partial f}{\partial y} = -2y e^{-(x^2 + y^2)}$$
   Le gradient s'annule si et seulement si $x=0$ et $y=0$.
   Les dérivées secondes :
   $$\frac{\partial^2 f}{\partial x^2} = (-2 + 4x^2) e^{-(x^2 + y^2)}$$
   $$\frac{\partial^2 f}{\partial y^2} = (-2 + 4y^2) e^{-(x^2 + y^2)}$$
   $$\frac{\partial^2 f}{\partial x \partial y} = 4xy e^{-(x^2 + y^2)}$$

2. **Évaluation à l'origine :**
   En $(0,0)$, on obtient :
   $$\frac{\partial^2 f}{\partial x^2}(0,0) = -2, \quad \frac{\partial^2 f}{\partial y^2}(0,0) = -2, \quad \frac{\partial^2 f}{\partial x \partial y}(0,0) = 0$$
   La matrice hessienne en l'origine est :
   $$H_f(0,0) = \begin{pmatrix} -2 & 0 \\ 0 & -2 \end{pmatrix}$$
   Cette matrice est diagonale et toutes ses valeurs propres sont strictement négatives ($-2$).
   La matrice hessienne est donc définie négative. L'origine $(0,0)$ est un **maximum local strict** (et même global vu la nature de la fonction exponentielle).

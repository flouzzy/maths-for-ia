# Fonction de Rosenbrock (2D)

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
La fonction de Rosenbrock est classiquement utilisée pour tester les algorithmes d'optimisation (le "ravin de Rosenbrock").
Soit $f(x, y) = (1 - x)^2 + 100(y - x^2)^2$.
1. Trouvez l'unique point critique.
2. Calculez la matrice hessienne en ce point et calculez ses valeurs propres.

**Correction mathématique détaillée :**

1. **Calcul du gradient :**
   $$\frac{\partial f}{\partial x} = -2(1 - x) - 400x(y - x^2)$$
   $$\frac{\partial f}{\partial y} = 200(y - x^2)$$
   En annulant $\frac{\partial f}{\partial y}$, on obtient $y = x^2$. En injectant dans la première, on a $-2(1-x) = 0$, donc $x=1$, puis $y=1$.
   Le seul point critique est $(1, 1)$.

2. **Matrice hessienne :**
   $$\frac{\partial^2 f}{\partial x^2} = 2 - 400y + 1200x^2$$
   $$\frac{\partial^2 f}{\partial y^2} = 200$$
   $$\frac{\partial^2 f}{\partial x \partial y} = -400x$$
   Évaluation en $(1, 1)$ :
   $$H_f(1, 1) = \begin{pmatrix} 2 - 400 + 1200 & -400 \\ -400 & 200 \end{pmatrix} = \begin{pmatrix} 802 & -400 \\ -400 & 200 \end{pmatrix}$$

3. **Analyse de courbure :**
   Le déterminant est $802 \times 200 - (-400)^2 = 160400 - 160000 = 400 > 0$.
   La trace est $1002 > 0$.
   La matrice hessienne est définie positive, le point $(1,1)$ est un **minimum local strict**.

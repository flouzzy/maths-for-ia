# Extremums avec paramètre : étude d'un polynôme symétrique

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f(x, y) = x^3 + y^3 - 3axy$ avec $a > 0$ un réel strictement positif.
Trouvez les points critiques et déterminez leur nature en fonction de $a$.

**Correction mathématique détaillée :**

1. **Gradient et points critiques :**
   $\frac{\partial f}{\partial x} = 3x^2 - 3ay = 0 \implies x^2 = ay$
   $\frac{\partial f}{\partial y} = 3y^2 - 3ax = 0 \implies y^2 = ax$
   En substituant $y = x^2/a$, la seconde équation donne $(x^2/a)^2 = ax \implies x^4 = a^3 x \implies x(x^3 - a^3) = 0$.
   Puisque $a$ est réel positif, les deux solutions réelles pour $x$ sont $0$ et $a$.
   Les points critiques sont $(0, 0)$ et $(a, a)$.

2. **Matrice hessienne :**
   $$\frac{\partial^2 f}{\partial x^2} = 6x, \quad \frac{\partial^2 f}{\partial y^2} = 6y, \quad \frac{\partial^2 f}{\partial x \partial y} = -3a$$
   $$H_f(x, y) = \begin{pmatrix} 6x & -3a \\ -3a & 6y \end{pmatrix}$$

3. **Classification :**
   - **En $(0, 0)$ :**
     $$H_f(0, 0) = \begin{pmatrix} 0 & -3a \\ -3a & 0 \end{pmatrix}$$
     Déterminant = $-9a^2 < 0$. C'est un **point selle**.
   - **En $(a, a)$ :**
     $$H_f(a, a) = \begin{pmatrix} 6a & -3a \\ -3a & 6a \end{pmatrix}$$
     Déterminant = $(6a)^2 - (-3a)^2 = 36a^2 - 9a^2 = 27a^2 > 0$.
     Le déterminant est positif, et la trace ($12a$) est positive (car $a>0$). La matrice est définie positive. C'est un **minimum local strict**.

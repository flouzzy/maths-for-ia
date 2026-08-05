# Matrice hessienne en dimension 3

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f(x, y, z) = x^2 y + y^2 z + z^2 - 2x$.
Calculez la matrice hessienne $H_f(x, y, z)$ et évaluez-la au point $P(1, 1, -1)$.
La matrice est-elle définie au sens strict en ce point ?

**Correction mathématique détaillée :**

1. **Calcul des dérivées partielles premières :**
   $$\frac{\partial f}{\partial x} = 2xy - 2$$
   $$\frac{\partial f}{\partial y} = x^2 + 2yz$$
   $$\frac{\partial f}{\partial z} = y^2 + 2z$$

2. **Calcul des dérivées partielles secondes :**
   $$\frac{\partial^2 f}{\partial x^2} = 2y, \quad \frac{\partial^2 f}{\partial y^2} = 2z, \quad \frac{\partial^2 f}{\partial z^2} = 2$$
   Croisées :
   $$\frac{\partial^2 f}{\partial x \partial y} = 2x, \quad \frac{\partial^2 f}{\partial x \partial z} = 0, \quad \frac{\partial^2 f}{\partial y \partial z} = 2y$$
   La matrice hessienne générale est :
   $$H_f(x, y, z) = \begin{pmatrix} 2y & 2x & 0 \\ 2x & 2z & 2y \\ 0 & 2y & 2 \end{pmatrix}$$

3. **Évaluation en $P(1, 1, -1)$ :**
   $$H_f(1, 1, -1) = \begin{pmatrix} 2 & 2 & 0 \\ 2 & -2 & 2 \\ 0 & 2 & 2 \end{pmatrix}$$

4. **Étude du spectre (Critère de Sylvester) :**
   - Le mineur principal d'ordre 1 est $2 > 0$.
   - Le mineur principal d'ordre 2 est $\det\begin{pmatrix} 2 & 2 \\ 2 & -2 \end{pmatrix} = -4 - 4 = -8 < 0$.
   Puisque les mineurs principaux n'alternent pas en signe selon une loi stricte et qu'il y en a un négatif, la matrice n'est pas définie positive ni définie négative. Elle est **indéfinie** (ses valeurs propres n'ont pas toutes le même signe).

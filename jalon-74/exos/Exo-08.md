### Exercice 8 : Un cas de non-équivalence stricte \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Donner un exemple dans l'espace $\mathbb{R}^2$ de vecteurs non nuls $x$ et $y$ pour lesquels l'inégalité de Minkowski pour $p=1$ est stricte : $\|x+y\|_1 < \|x\|_1 + \|y\|_1$. Quel est le cas d'égalité ?

**Correction Détaillée :**
1. Considérons les vecteurs $x = (1, 0)$ et $y = (-1, 0)$.
2. Les normes 1 sont $\|x\|_1 = |1| + |0| = 1$ et $\|y\|_1 = |-1| + |0| = 1$.
3. La somme des normes est $\|x\|_1 + \|y\|_1 = 2$.
4. Le vecteur somme est $x+y = (0, 0)$. Sa norme est $\|x+y\|_1 = 0$.
5. On a bien $0 < 2$, l'inégalité est stricte.
6. Considérons maintenant $x = (1, 0)$ et $z = (0, 1)$.
   $\|x\|_1 + \|z\|_1 = 1 + 1 = 2$.
   $x+z = (1, 1) \implies \|x+z\|_1 = |1| + |1| = 2$. On a l'égalité.
7. **Condition d'égalité pour la norme 1 :** L'égalité $\|x+y\|_1 = \|x\|_1 + \|y\|_1$ se produit si et seulement si pour chaque composante $i$, $x_i$ et $y_i$ ont le même signe (ou l'un est nul). Autrement dit, $x_i y_i \ge 0$ pour tout $i$.

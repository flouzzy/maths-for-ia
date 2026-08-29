## Exercice 3 : Linéarité positive pour les fonctions étagées \quad $$\bigstar\bigstar$$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré. Soit $s \in \mathcal{E}_+$ et $\alpha \ge 0$.
Montrer que $\int_X (\alpha s) \, d\mu = \alpha \int_X s \, d\mu$.

**Correction :**
1. Si $\alpha = 0$, $\alpha s = 0$. L'intégrale vaut 0. D'autre part, $0 \cdot \int_X s \, d\mu = 0$. L'égalité est vérifiée.
2. Si $\alpha > 0$, l'écriture canonique de $s$ est $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$, où les $A_i$ partitionnent $X$.
3. Alors la fonction $\alpha s$ s'écrit $\alpha s = \sum_{i=1}^n (\alpha a_i) \mathbf{1}_{A_i}$.
4. Puisque $\alpha > 0$, les valeurs $\alpha a_i$ sont deux à deux distinctes et les $A_i$ partitionnent toujours $X$. Il s'agit donc de l'écriture canonique de $\alpha s$.
5. Par définition de l'intégrale d'une fonction étagée :
   $$\int_X (\alpha s) \, d\mu = \sum_{i=1}^n (\alpha a_i) \mu(A_i)$$
6. Par distributivité et commutativité dans $[0, +\infty]$ :
   $$\sum_{i=1}^n (\alpha a_i) \mu(A_i) = \alpha \left( \sum_{i=1}^n a_i \mu(A_i) \right) = \alpha \int_X s \, d\mu$$
7. L'homogénéité est donc démontrée.

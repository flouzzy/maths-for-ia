## Exercice 1 : Intégrale de la fonction nulle \quad $$\bigstar$$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et la fonction nulle $f(x) = 0$ pour tout $x \in X$.
Montrer en utilisant la définition stricte par supremum que $\int_X f \, d\mu = 0$.

**Correction :**
1. Par définition, $f \in \mathcal{M}_+$.
2. Soit $s \in \mathcal{E}_+$ une fonction étagée telle que $0 \le s \le f$.
3. Puisque $f(x) = 0$ pour tout $x \in X$, la seule fonction $s$ satisfaisant cette condition est $s(x) = 0$ pour tout $x$.
4. L'écriture canonique de $s$ est $s = 0 \cdot \mathbf{1}_X$.
5. L'intégrale de cette fonction étagée est par définition : $\int_X s \, d\mu = 0 \cdot \mu(X) = 0$. (La convention $0 \cdot \infty = 0$ assure ce résultat même si $\mu(X) = \infty$).
6. Le supremum sur l'ensemble de ces intégrales (qui ne contient que la valeur 0) est donc 0.
7. Ainsi, $\int_X f \, d\mu = 0$.

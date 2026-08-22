# Intégrale d'une fonction en escalier

**Difficulté :** $\star\☆☆☆☆$

## Énoncé

Soit $(X, \mathcal{A}, \mu) = ([0, 2], \mathcal{B}([0, 2]), \lambda)$. Soit la fonction étagée $s(x) = 3 \cdot \mathbb{1}_{[0,1[}(x) + 7 \cdot \mathbb{1}_{[1,2]}(x)$. Calculez rigoureusement $\int_{[0,2]} s \, d\lambda$.

---

## Correction détaillée

Par définition de l'intégrale d'une fonction étagée positive :
$$ \int_X s \, d\lambda = \sum_{i} \alpha_i \lambda(A_i) $$
Ici, les valeurs sont $\alpha_1 = 3$ et $\alpha_2 = 7$. Les ensembles correspondants sont $A_1 = [0,1[$ et $A_2 = [1,2]$.
Leurs mesures de Lebesgue sont :
$\lambda([0,1[) = 1 - 0 = 1$
$\lambda([1,2]) = 2 - 1 = 1$
Donc, $\int_{[0,2]} s \, d\lambda = 3 \times 1 + 7 \times 1 = 10$.

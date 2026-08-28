# Convergence et intégrale de Lebesgue sur un point

**Difficulté :** $\star\star☆☆☆$

## Énoncé

Sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, on pose $A = \{0\}$. Soit $f(x) = \mathbb{1}_{A}(x)$ la fonction caractéristique du singleton $\{0\}$. Que vaut $\int_\mathbb{R} f \, d\lambda$ ?

---

## Correction détaillée

La fonction $f$ est une fonction étagée positive avec une seule valeur non nulle, $\alpha_1 = 1$, prise sur l'ensemble $A_1 = \{0\}$. La mesure de Lebesgue d'un point est nulle : $\lambda(\{0\}) = 0$.
Ainsi : $\int_\mathbb{R} f \, d\lambda = 1 \times \lambda(\{0\}) = 1 \times 0 = 0$.
Bien que la fonction ne soit pas partout nulle, son intégrale de Lebesgue l'est car l'ensemble sur lequel elle est non nulle est de mesure négligeable.

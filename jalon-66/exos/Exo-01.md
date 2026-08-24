# Exercice 1 : Calcul basique d'intégrale de fonction simple \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Calculer l'intégrale de Lebesgue de la fonction simple : $f = 2 \cdot \mathbf{1}_{[0, 3]} + 5 \cdot \mathbf{1}_{]3, 6[}$.

**Correction :**
La fonction $f$ est une fonction étagée positive (ou simple). Par définition, son intégrale de Lebesgue est la somme pondérée des mesures des ensembles où elle est constante.
1. Les ensembles sont disjoints : $A_1 = [0, 3]$ et $A_2 = ]3, 6[$.
2. Leurs mesures de Lebesgue respectives sont $\lambda(A_1) = 3 - 0 = 3$ et $\lambda(A_2) = 6 - 3 = 3$.
3. On applique la définition : $\int_\mathbb{R} f \, d\lambda = 2 \cdot \lambda(A_1) + 5 \cdot \lambda(A_2)$.
4. $\int_\mathbb{R} f \, d\lambda = 2 \cdot 3 + 5 \cdot 3 = 6 + 15 = 21$.

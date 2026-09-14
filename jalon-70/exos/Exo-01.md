## Exercice 1 : Calcul de mesure produit sur des intervalles finis \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(\mathbb{R}^2, \mathcal{B}(\mathbb{R}^2), \lambda_2)$ où $\lambda_2 = \lambda \otimes \lambda$ est la mesure de Lebesgue sur $\mathbb{R}^2$.
Calculer $\lambda_2(A)$ pour $A = [1, 3] \times [2, 5]$.

**Correction :**
Par définition de la mesure produit sur un rectangle mesurable :
1. Les intervalles $A_1 = [1, 3]$ et $A_2 = [2, 5]$ sont des boréliens de $\mathbb{R}$.
2. On applique la formule : $\lambda_2(A_1 \times A_2) = \lambda(A_1) \cdot \lambda(A_2)$.
3. Calcul des mesures 1D : $\lambda([1, 3]) = 3 - 1 = 2$ et $\lambda([2, 5]) = 5 - 2 = 3$.
4. Conclusion : $\lambda_2(A) = 2 \cdot 3 = 6$.

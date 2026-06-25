# Exercice 1: Espace dual en dimension 2 (Difficulté 1/5)
## Énoncé
Soit $E = \mathbb{R}^2$. On considère la base canonique $(e_1, e_2)$. Déterminer la base duale $(e_1^*, e_2^*)$ et calculer $e_1^*(3e_1 - 2e_2)$.

## Correction détaillée
1. **Définition de la base duale :** Par définition, la base duale $(e_1^*, e_2^*)$ d'une base $(e_1, e_2)$ vérifie $e_i^*(e_j) = \delta_{ij}$.
2. **Explicitation des formes linéaires :**
   - $e_1^*(x, y) = e_1^*(xe_1 + ye_2) = x e_1^*(e_1) + y e_1^*(e_2) = x \cdot 1 + y \cdot 0 = x$.
   - $e_2^*(x, y) = e_2^*(xe_1 + ye_2) = x e_2^*(e_1) + y e_2^*(e_2) = x \cdot 0 + y \cdot 1 = y$.
3. **Calcul de l'évaluation :** On cherche à évaluer $e_1^*$ sur le vecteur $v = 3e_1 - 2e_2$.
4. **Développement complet :**
   $$e_1^*(3e_1 - 2e_2) = 3 e_1^*(e_1) - 2 e_1^*(e_2)$$
   $$= 3 \times 1 - 2 \times 0$$
   $$= 3$$
5. **Conclusion :** La valeur de la forme linéaire $e_1^*$ sur le vecteur $3e_1 - 2e_2$ est $3$.

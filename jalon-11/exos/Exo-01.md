# Exercice 1: Espace dual en dimension 2
## Énoncé
Soit $E = \mathbb{R}^2$ muni de sa base canonique $\mathcal{B} = (e_1, e_2)$. Soit $\varphi : E \to \mathbb{R}$ l'application définie par $\varphi(x, y) = 3x - 2y$.
1. Montrer que $\varphi$ est une forme linéaire, c'est-à-dire que $\varphi \in E^*$.
2. Déterminer les coordonnées de $\varphi$ dans la base duale $\mathcal{B}^* = (e_1^*, e_2^*)$.


## Correction détaillée

1. **Définition de la base duale :**
   L'espace $E = \mathbb{R}^2$ étant de dimension 2, son dual $E^*$ est également de dimension 2. La base duale associée à $(e_1, e_2)$ est la famille $(e_1^*, e_2^*)$ d'applications linéaires de $\mathbb{R}^2$ vers $\mathbb{R}$ définie explicitement par l'action sur les vecteurs de base :
   - $e_1^*(e_1) = 1$ et $e_1^*(e_2) = 0$
   - $e_2^*(e_1) = 0$ et $e_2^*(e_2) = 1$

2. **Explicitation des formes linéaires sur un vecteur quelconque :**
   Soit un vecteur $u = xe_1 + ye_2 \in \mathbb{R}^2$. Par la stricte linéarité de l'application $e_1^*$, nous pouvons développer l'évaluation :
   $$e_1^*(u) = e_1^*(xe_1 + ye_2) = x e_1^*(e_1) + y e_1^*(e_2)$$
   En substituant les valeurs des évaluations sur la base :
   $$e_1^*(u) = x \cdot 1 + y \cdot 0 = x$$
   De manière rigoureusement symétrique pour $e_2^*$ :
   $$e_2^*(u) = e_2^*(xe_1 + ye_2) = x e_2^*(e_1) + y e_2^*(e_2) = x \cdot 0 + y \cdot 1 = y$$
   Les éléments de la base duale sont donc les applications d'extraction des coordonnées canoniques.

3. **Calcul de l'évaluation spécifique :**
   Considérons le vecteur $v = 3e_1 - 2e_2$. Nous appliquons la linéarité de $e_1^*$ :
   $$e_1^*(3e_1 - 2e_2) = 3 e_1^*(e_1) - 2 e_1^*(e_2)$$
   $$= 3 \times 1 - 2 \times 0$$
   $$= 3$$
5. **Conclusion :** La valeur de la forme linéaire $e_1^*$ sur le vecteur $3e_1 - 2e_2$ est $3$.

$\blacksquare$

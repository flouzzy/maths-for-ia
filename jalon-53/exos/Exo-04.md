---
uuid: "jalon-53-exo-4"
title: "Produit d'espaces Hausdorff"
---

## Exercice 4 : Produit d'espaces Hausdorff \quad $\bigstar\bigstar\bigstar\star\star$


**Énoncé :**
Soient $X$ et $Y$ deux espaces topologiques. Montrer que l'espace produit $X \times Y$ est Hausdorff si et seulement si $X$ et $Y$ sont Hausdorff.

**Correction Détaillée :**
1. **Sens direct ($\impliedby$) :** Supposons $X$ et $Y$ Hausdorff. Soient $(x_1, y_1)$ et $(x_2, y_2)$ deux points distincts de $X \times Y$.
   - Cas 1 : $x_1 \neq x_2$. Comme $X$ est Hausdorff, il existe $U_1, U_2$ ouverts de $X$ disjoints contenant respectivement $x_1$ et $x_2$. Alors $U_1 \times Y$ et $U_2 \times Y$ sont des ouverts de $X \times Y$, disjoints, contenant respectivement $(x_1, y_1)$ et $(x_2, y_2)$.
   - Cas 2 : $y_1 \neq y_2$. Symétriquement, il existe $V_1, V_2$ ouverts de $Y$ disjoints. $X \times V_1$ et $X \times V_2$ séparent les points.
   Dans tous les cas, $X \times Y$ est Hausdorff.
2. **Sens réciproque ($\implies$) :** Supposons $X \times Y$ Hausdorff. Soient $x_1, x_2 \in X$ avec $x_1 \neq x_2$. Fixons $y \in Y$. Les points $(x_1, y)$ et $(x_2, y)$ sont distincts dans $X \times Y$. Ils admettent des voisinages de base disjoints $U_1 \times V_1$ et $U_2 \times V_2$. L'intersection est vide si et seulement si $U_1 \cap U_2 = \emptyset$ ou $V_1 \cap V_2 = \emptyset$. Comme $y \in V_1 \cap V_2$, on a nécessairement $U_1 \cap U_2 = \emptyset$. Les ouverts $U_1$ et $U_2$ de $X$ séparent $x_1$ et $x_2$. Donc $X$ est Hausdorff (même argument pour $Y$).

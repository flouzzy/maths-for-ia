---
uuid: "jalon-53-exo-3"
title: "Sous-espaces d'un espace Hausdorff"
---

## Exercice 3 : Sous-espaces d'un espace Hausdorff \quad $\bigstar\bigstar\star\star\star$


**Énoncé :**
Soit $X$ un espace de Hausdorff et $Y \subset X$ muni de la topologie induite. Montrer que $Y$ est un espace de Hausdorff.

**Correction Détaillée :**
Soient $y_1, y_2 \in Y$ avec $y_1 \neq y_2$. Comme $Y \subset X$, on a aussi $y_1, y_2 \in X$.
Puisque $X$ est Hausdorff et $y_1 \neq y_2$, il existe des ouverts $U$ et $V$ de $X$ tels que $y_1 \in U$, $y_2 \in V$ et $U \cap V = \emptyset$.
Considérons les ensembles $U_Y = U \cap Y$ et $V_Y = V \cap Y$.
Par définition de la topologie induite, $U_Y$ et $V_Y$ sont des ouverts de $Y$.
De plus, $y_1 \in U_Y$ et $y_2 \in V_Y$.
Enfin, $U_Y \cap V_Y = (U \cap Y) \cap (V \cap Y) = (U \cap V) \cap Y = \emptyset \cap Y = \emptyset$.
Les points $y_1$ et $y_2$ sont séparés par des ouverts disjoints dans $Y$. Donc $Y$ est Hausdorff.

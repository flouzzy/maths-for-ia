---
uuid: "jalon-53-exo-5"
title: "Fermeture de la diagonale"
---

## Exercice 5 : Fermeture de la diagonale \quad $\bigstar\bigstar\bigstar\star\star$


**Énoncé :**
Soit $X$ un espace topologique. Montrer que $X$ est Hausdorff si et seulement si la diagonale $\Delta = \{(x, x) \mid x \in X\}$ est fermée dans l'espace produit $X \times X$.

**Correction Détaillée :**
1. **Sens direct ($\implies$) :** Supposons $X$ Hausdorff. Pour montrer que $\Delta$ est fermée, on montre que son complémentaire $(X \times X) \setminus \Delta$ est ouvert. Soit $(x, y) \notin \Delta$, i.e., $x \neq y$. Par hypothèse, il existe $U$ ouvert contenant $x$ et $V$ ouvert contenant $y$ tels que $U \cap V = \emptyset$. L'ensemble $U \times V$ est un ouvert de $X \times X$ contenant $(x, y)$. De plus, $(U \times V) \cap \Delta = \emptyset$ car si $(z, z) \in U \times V$, alors $z \in U \cap V$, ce qui est impossible. Ainsi $(x, y) \in U \times V \subset (X \times X) \setminus \Delta$. Le complémentaire est ouvert, $\Delta$ est fermée.
2. **Sens réciproque ($\impliedby$) :** Supposons $\Delta$ fermée. Soient $x \neq y$ dans $X$. Alors $(x, y) \in (X \times X) \setminus \Delta$, qui est ouvert. Par définition de la topologie produit, il existe un ouvert de base $U \times V$ tel que $(x, y) \in U \times V \subset (X \times X) \setminus \Delta$. On a $x \in U$, $y \in V$. Si $U \cap V$ contenait un élément $z$, alors $(z, z) \in U \times V$, ce qui contredirait l'inclusion dans le complémentaire de $\Delta$. Donc $U \cap V = \emptyset$. $X$ est Hausdorff.

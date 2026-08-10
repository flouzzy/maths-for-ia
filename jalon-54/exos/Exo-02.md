## Exercice 2 : Union finie de compacts \quad $\bigstar\bigstar\star\star\star$

**Énoncé :** Soient $K_1$ et $K_2$ deux parties compactes d'un espace topologique séparé $X$. Montrer que $K_1 \cup K_2$ est compact en utilisant la définition par recouvrement ouvert (Borel-Lebesgue).

**Correction Détaillée :**
Soit $(U_i)_{i \in I}$ un recouvrement ouvert de $K_1 \cup K_2$.
Cela signifie que $K_1 \cup K_2 \subset \bigcup_{i \in I} U_i$.
Puisque $K_1 \subset K_1 \cup K_2$, la famille $(U_i)_{i \in I}$ est a fortiori un recouvrement ouvert de $K_1$.
Comme $K_1$ est compact, il existe un sous-ensemble fini $J_1 \subset I$ tel que $K_1 \subset \bigcup_{j \in J_1} U_j$.
De même, $(U_i)_{i \in I}$ est un recouvrement ouvert de $K_2$, qui est compact. Il existe donc un sous-ensemble fini $J_2 \subset I$ tel que $K_2 \subset \bigcup_{j \in J_2} U_j$.
Soit $J = J_1 \cup J_2$. L'ensemble $J$, réunion de deux ensembles finis, est un ensemble fini.
On a alors : $K_1 \cup K_2 \subset \left( \bigcup_{j \in J_1} U_j \right) \cup \left( \bigcup_{j \in J_2} U_j \right) = \bigcup_{j \in J} U_j$.
Nous avons ainsi extrait de $(U_i)_{i \in I}$ un sous-recouvrement fini indexé par $J$, recouvrant $K_1 \cup K_2$.
L'espace $X$ étant supposé séparé, $K_1 \cup K_2$ l'est également pour la topologie induite, et vérifiant la propriété de Borel-Lebesgue, il est compact.
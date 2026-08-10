## Exercice 3 : Un sous-espace fermé d'un compact est compact \quad $\bigstar\bigstar\star\star\star$

**Énoncé :** Soit $X$ un espace topologique compact et $F$ un sous-espace fermé de $X$. Démontrer que $F$ est compact.

**Correction Détaillée :**
Soit $(U_i)_{i \in I}$ une famille d'ouverts de l'espace global $X$ recouvrant $F$, c'est-à-dire $F \subset \bigcup_{i \in I} U_i$.
Puisque $F$ est fermé dans $X$, son complémentaire $V = X \setminus F$ est un ouvert de $X$.
Considérons la famille d'ouverts formée des $U_i$ et de $V$. Cette famille recouvre l'espace entier $X$ puisque $X = F \cup (X \setminus F) \subset \left(\bigcup_{i \in I} U_i\right) \cup V$.
L'espace $X$ étant compact, on peut en extraire un sous-recouvrement fini. Ce sous-recouvrement est constitué d'un nombre fini de $U_i$, notons-les $U_{i_1}, \dots, U_{i_n}$, et éventuellement de l'ouvert $V$.
On a donc $X = U_{i_1} \cup \dots \cup U_{i_n} \cup V$.
En intersectant cette égalité avec $F$, et puisque $F \cap V = F \cap (X \setminus F) = \emptyset$, on obtient :
$F = F \cap X = F \cap (U_{i_1} \cup \dots \cup U_{i_n} \cup V) = (F \cap U_{i_1}) \cup \dots \cup (F \cap U_{i_n})$.
Ainsi, $F \subset U_{i_1} \cup \dots \cup U_{i_n}$.
Nous avons extrait un sous-recouvrement fini recouvrant $F$. $F$ est donc compact.
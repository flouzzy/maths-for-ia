---
uuid: "jalon-53-exo-8"
title: "Espaces normaux ($T_4$) et lemmes de séparation"
---

## Exercice 8 : Espaces normaux ($T_4$) et lemmes de séparation \quad $\bigstar\bigstar\bigstar\bigstar\star$


**Énoncé :**
Rappeler la définition d'un espace normal ($T_4$). Montrer que tout espace métrique est normal.

**Correction Détaillée :**
1. **Définition :** Un espace topologique $X$ est normal ($T_4$) s'il est $T_1$ (les singletons sont fermés) et si pour tout couple $(A, B)$ de fermés disjoints, il existe des ouverts $U, V$ disjoints tels que $A \subset U$ et $B \subset V$.
2. **Cas métrique :** Soit $(X, d)$ un espace métrique. Les singletons sont fermés car l'espace est Hausdorff (et même métrique). Soient $A, B$ deux fermés disjoints. Pour tout $a \in A$, $a \notin B$. $B$ étant fermé, $d(a, B) = \inf_{b \in B} d(a, b) > 0$. Posons $r_a = \frac{1}{2} d(a, B)$. L'ouvert $U = \bigcup_{a \in A} B(a, r_a)$ contient $A$. Symétriquement, pour $b \in B$, posons $r_b = \frac{1}{2} d(b, A)$ et $V = \bigcup_{b \in B} B(b, r_b)$. L'ouvert $V$ contient $B$.
Montrons $U \cap V = \emptyset$. Si $x \in U \cap V$, il existe $a \in A$ et $b \in B$ tels que $d(x, a) < r_a$ et $d(x, b) < r_b$. Par inégalité triangulaire, $d(a, b) \le d(a, x) + d(x, b) < r_a + r_b$.
Or, $d(a, B) \le d(a, b)$ et $d(b, A) \le d(a, b)$. Donc $2r_a \le d(a, b)$ et $2r_b \le d(a, b)$. Ainsi $r_a + r_b \le \max(2r_a, 2r_b) \le d(a, b)$. Contradiction avec $d(a, b) < r_a + r_b$.
Donc $U \cap V = \emptyset$. L'espace métrique est normal.

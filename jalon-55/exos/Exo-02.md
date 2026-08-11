---
uuid: "exo-55-02"
title: "Adhérence et connexité"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 2 : Adhérence et connexité

**Énoncé :**
Soit $X$ un espace topologique et $A \subset X$ une partie connexe. Soit $B$ tel que $A \subset B \subset \overline{A}$. Montrer que $B$ est connexe.

**Solution :**
1. Raisonnons par l'absurde. Supposons que $B$ n'est pas connexe. Il existe alors deux ouverts $U$ et $V$ de $X$ tels que $B \cap U \neq \emptyset$, $B \cap V \neq \emptyset$, $(B \cap U) \cap (B \cap V) = \emptyset$, et $B \subset U \cup V$.
2. Puisque $A \subset B$, on a $A \subset U \cup V$. De plus, $(A \cap U) \cap (A \cap V) = \emptyset$.
3. $A$ étant connexe, l'un des deux ensembles $A \cap U$ ou $A \cap V$ doit être vide. Sans perte de généralité, supposons $A \cap U = \emptyset$.
4. Alors $A \subset V$. Puisque $V$ est ouvert, et $V^c$ est fermé avec $A \subset V^c$, l'adhérence de $A$ satisfait $\overline{A} \subset V^c$, c'est-à-dire $\overline{A} \cap U = \emptyset$.
5. Or, par hypothèse, $B \subset \overline{A}$, ce qui implique $B \cap U = \emptyset$. Ceci contredit l'hypothèse de la partition de $B$ où $B \cap U \neq \emptyset$.
6. Conclusion : $B$ est connexe.

---
uuid: "jalon-53-exo-6"
title: "Espace de Zariski"
---

## Exercice 6 : Espace de Zariski \quad $\bigstar\bigstar\bigstar\bigstar\star$


**Énoncé :**
Soit $X$ un ensemble infini muni de la topologie cofinie (un sous-ensemble est ouvert si et seulement s'il est vide ou si son complémentaire est fini). Cet espace est-il Hausdorff ? Est-il $T_1$ (axiome de Fréchet) ?

**Correction Détaillée :**
1. **Axiome $T_1$ :** Soit $x \in X$. Le complémentaire du singleton $\{x\}$ est $X \setminus \{x\}$. Comme $\{x\}$ est fini (cardinal 1), $X \setminus \{x\}$ est ouvert, donc $\{x\}$ est fermé. Un espace dont tous les singletons sont fermés est un espace $T_1$. Donc oui, $X$ est $T_1$.
2. **Axiome $T_2$ (Hausdorff) :** Soient $x, y \in X$ avec $x \neq y$. Supposons qu'il existe des ouverts $U$ et $V$ disjoints tels que $x \in U$ et $y \in V$. Comme $U$ et $V$ sont non vides, leurs complémentaires $U^c$ et $V^c$ sont finis. Or, $U \cap V = \emptyset \implies (U \cap V)^c = X \implies U^c \cup V^c = X$. L'union de deux ensembles finis étant finie, $X$ serait fini, ce qui contredit l'hypothèse. Il est donc impossible de trouver de tels ouverts. $X$ n'est pas Hausdorff.

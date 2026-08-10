---
uuid: "jalon-53-exo-7"
title: "Graphe d'une fonction continue"
---

## Exercice 7 : Graphe d'une fonction continue \quad $\bigstar\bigstar\bigstar\bigstar\star$


**Énoncé :**
Soit $f : X \to Y$ une application continue entre deux espaces topologiques. On suppose que $Y$ est Hausdorff. Montrer que le graphe de $f$, défini par $\Gamma = \{(x, f(x)) \mid x \in X\}$, est fermé dans $X \times Y$.

**Correction Détaillée :**
On va montrer que le complémentaire de $\Gamma$ est ouvert.
Soit $(x, y) \in (X \times Y) \setminus \Gamma$. Cela signifie que $y \neq f(x)$.
Puisque $Y$ est Hausdorff, il existe des ouverts disjoints $V_1, V_2 \subset Y$ tels que $f(x) \in V_1$ et $y \in V_2$.
Comme $f$ est continue, $U = f^{-1}(V_1)$ est un ouvert de $X$ contenant $x$.
Considérons l'ouvert $U \times V_2$ de $X \times Y$. Ce voisinage contient $(x, y)$.
De plus, si $(x', y') \in U \times V_2$, alors $x' \in U \implies f(x') \in V_1$. Et $y' \in V_2$.
Puisque $V_1 \cap V_2 = \emptyset$, on a $y' \neq f(x')$, ce qui signifie que $(x', y') \notin \Gamma$.
Ainsi, $U \times V_2 \subset (X \times Y) \setminus \Gamma$. Le complémentaire est ouvert, donc $\Gamma$ est fermé.

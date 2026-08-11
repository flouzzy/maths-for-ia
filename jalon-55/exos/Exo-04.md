---
uuid: "exo-55-04"
title: "Composantes connexes d'un espace rationnel"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 4 : Composantes connexes d'un espace rationnel

**Énoncé :**
Déterminer les composantes connexes de $\mathbb{Q}$ muni de la topologie usuelle induite par $\mathbb{R}$.

**Solution :**
1. Soit $A$ une composante connexe de $\mathbb{Q}$.
2. Supposons que $A$ contienne au moins deux éléments distincts, disons $x < y$.
3. Comme $\mathbb{R}$ est complet et $\mathbb{Q}$ est dénombrable, l'ensemble des irrationnels est dense. Il existe donc un irrationnel $\alpha$ tel que $x < \alpha < y$.
4. Définissons $U = A \cap ]-\infty, \alpha[$ et $V = A \cap ]\alpha, +\infty[$.
5. $U$ et $V$ sont des ouverts de la topologie induite sur $A$.
6. $x \in U$ donc $U \neq \emptyset$. $y \in V$ donc $V \neq \emptyset$.
7. $U \cap V = \emptyset$.
8. Puisque $\alpha \notin \mathbb{Q}$, $\alpha \notin A$, d'où $A = U \cup V$.
9. L'ensemble $A$ est donc séparé par deux ouverts non vides et disjoints, ce qui contredit le fait que $A$ soit connexe.
10. Par conséquent, $A$ ne peut contenir plus d'un point. Les composantes connexes de $\mathbb{Q}$ sont donc exactement ses singletons : $\mathbb{Q}$ est totalement discontinu.

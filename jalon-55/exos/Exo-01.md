---
uuid: "exo-55-01"
title: "Connexité des intervalles de R"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Connexité des intervalles de R

**Énoncé :**
Montrer que l'intervalle $X = [0, 1] \cup [2, 3]$ n'est pas connexe dans $\mathbb{R}$ muni de sa topologie usuelle.

**Solution :**
1. Considérons les ensembles $U = [0, 1]$ et $V = [2, 3]$.
2. $U$ peut s'écrire $U = X \cap ]-1, \frac{3}{2}[$. Comme $]-1, \frac{3}{2}[$ est un ouvert de $\mathbb{R}$, $U$ est un ouvert de $X$ pour la topologie induite.
3. De même, $V = X \cap ]\frac{3}{2}, 4[$ est un ouvert de $X$.
4. On a $U \neq \emptyset$, $V \neq \emptyset$, $U \cap V = \emptyset$ et $U \cup V = X$.
5. Ainsi, $X$ admet une partition par deux ouverts non vides, donc $X$ n'est pas connexe.

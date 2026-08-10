---
uuid: "jalon-53-exo-2"
title: "La droite à deux origines"
---

## Exercice 2 : La droite à deux origines \quad $\bigstar\bigstar\star\star\star$


**Énoncé :**
On considère l'ensemble $X = (\mathbb{R} \setminus \{0\}) \cup \{0_a, 0_b\}$ muni de la topologie engendrée par la base d'ouverts suivante :
- Les intervalles ouverts de $\mathbb{R} \setminus \{0\}$.
- Les ensembles de la forme $]-\epsilon, \epsilon[ \setminus \{0\} \cup \{0_a\}$ pour $\epsilon > 0$.
- Les ensembles de la forme $]-\epsilon, \epsilon[ \setminus \{0\} \cup \{0_b\}$ pour $\epsilon > 0$.
Montrer que $X$ n'est pas un espace de Hausdorff.

**Correction Détaillée :**
Pour montrer que $X$ n'est pas Hausdorff, il suffit de trouver deux points distincts qui ne peuvent pas être séparés par des voisinages ouverts disjoints. Considérons les points $0_a$ et $0_b$.
Soit $U$ un voisinage ouvert de $0_a$ et $V$ un voisinage ouvert de $0_b$.
Par définition de la topologie sur $X$, il existe $\epsilon_1 > 0$ tel que $]-\epsilon_1, \epsilon_1[ \setminus \{0\} \cup \{0_a\} \subset U$.
De même, il existe $\epsilon_2 > 0$ tel que $]-\epsilon_2, \epsilon_2[ \setminus \{0\} \cup \{0_b\} \subset V$.
Soit $\epsilon = \min(\epsilon_1, \epsilon_2) > 0$. L'intervalle $]0, \epsilon[$ est non vide.
Soit $x \in ]0, \epsilon[$. On a $x \in ]-\epsilon_1, \epsilon_1[ \setminus \{0\} \subset U$ et $x \in ]-\epsilon_2, \epsilon_2[ \setminus \{0\} \subset V$.
Donc $x \in U \cap V$, ce qui prouve que $U \cap V \neq \emptyset$.
Les points $0_a$ et $0_b$ ne peuvent être séparés, donc $X$ n'est pas $T_2$.

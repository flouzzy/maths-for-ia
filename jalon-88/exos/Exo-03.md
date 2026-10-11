# Indépendance des passages au complémentaire

**Difficulté :** $\bigstar\bigstar\star\star\star$

Soient $A$ et $B$ deux événements indépendants.
Démontrer, en utilisant uniquement les axiomes des probabilités et la définition de l'indépendance, que :
1. $A$ et $B^c$ sont indépendants.
2. $A^c$ et $B^c$ sont indépendants.

### Correction

Soient $A$ et $B$ deux événements indépendants, on a $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$.

**Démonstration 1 : Indépendance de $A$ et $B^c$**
1. On peut écrire $A$ comme la réunion disjointe de deux sous-ensembles : $A = (A \cap B) \cup (A \cap B^c)$.
2. Par l'axiome d'additivité des probabilités pour des ensembles disjoints, on a : $\mathbb{P}(A) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c)$.
3. On isole le terme qui nous intéresse : $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$.
4. On utilise l'hypothèse d'indépendance de $A$ et $B$ : $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B)$.
5. On factorise par $\mathbb{P}(A)$ : $\mathbb{P}(A \cap B^c) = \mathbb{P}(A)(1 - \mathbb{P}(B))$.
6. On reconnaît la probabilité du complémentaire : $\mathbb{P}(A \cap B^c) = \mathbb{P}(A)\mathbb{P}(B^c)$.
Ceci démontre que $A$ et $B^c$ sont indépendants.

**Démonstration 2 : Indépendance de $A^c$ et $B^c$**
1. D'après le point précédent, si deux événements sont indépendants, le premier est indépendant du complémentaire du second.
2. Appliquons ce résultat à la paire d'événements indépendants $B^c$ et $A$. (Note : si $A$ est indépendant de $B^c$, alors $B^c$ est indépendant de $A$).
3. Le résultat précédent nous dit que $B^c$ est indépendant du complémentaire de $A$, c'est-à-dire $A^c$.
4. L'indépendance étant symétrique, on conclut immédiatement que $A^c$ et $B^c$ sont indépendants.

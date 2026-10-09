# Exercice 3 : Indépendance des événements complémentaires \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**

Soient $A$ et $B$ deux événements indépendants d'un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$.
Démontrer rigoureusement que $A$ et le complémentaire de $B$ (noté $B^c$) sont également des événements indépendants.

**Correction Détaillée :**

1. Nous voulons démontrer que $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) \cdot \mathbb{P}(B^c)$.
2. Par définition, les ensembles $B$ et $B^c$ forment une partition de l'univers $\Omega$.
3. Nous pouvons donc écrire l'événement $A$ comme l'union disjointe de ses intersections avec $B$ et $B^c$ : $A = (A \cap B) \cup (A \cap B^c)$.
4. Par l'axiome d'additivité des probabilités pour des ensembles disjoints, on obtient :
   $\mathbb{P}(A) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c)$.
5. Isolons le terme qui nous intéresse :
   $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$.
6. Puisque $A$ et $B$ sont supposés indépendants, nous savons que $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$. Substituons cette expression :
   $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B)$.
7. Factorisons $\mathbb{P}(A)$ dans le membre de droite :
   $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) \cdot (1 - \mathbb{P}(B))$.
8. Par la propriété des événements complémentaires, $1 - \mathbb{P}(B) = \mathbb{P}(B^c)$.
9. En remplaçant, on obtient l'égalité finale :
   $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) \cdot \mathbb{P}(B^c)$.
10. La relation définissant l'indépendance est satisfaite, $A$ et $B^c$ sont indépendants.

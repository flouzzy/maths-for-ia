---
uuid: "jalon-4-exo-01"
title: "Exercice 01 - 1 étoiles"
---
# Exercice 01 : Loi d'absorption fondamentale
**Difficulté :** ⭐

## Énoncé
Soient $E$ un ensemble non vide, et $A$ et $B$ deux parties de $E$.
Démontrez l'égalité d'ensembles suivante :
$$A \cup (A \cap B) = A$$

## Correction Détaillée
* **Analyse de l'énoncé :**
Nous devons démontrer l'égalité entre deux ensembles, $A \cup (A \cap B)$ et $A$. Pour prouver que deux ensembles sont égaux, la méthode standard en théorie des ensembles est de démontrer une double inclusion. C'est-à-dire, nous devons montrer que $A \cup (A \cap B) \subseteq A$ et que $A \subseteq A \cup (A \cap B)$. La démonstration se fera par l'analyse des propriétés des éléments.

* **Résolution pas-à-pas :**

**Partie 1 : Démontrons que $A \cup (A \cap B) \subseteq A$.**

1.  Soit $x$ un élément arbitraire de l'ensemble $A \cup (A \cap B)$.
2.  Par la définition de l'union d'ensembles, l'appartenance de $x$ à $A \cup (A \cap B)$ signifie que $x \in A$ ou $x \in (A \cap B)$.
3.  Nous analysons ces deux cas distinctement, en considérant chaque terme de la disjonction :
    *   **Cas 1 :** Supposons que $x \in A$.
        Dans cette hypothèse, la condition que $x$ appartient à l'ensemble $A$ est directement satisfaite.
    *   **Cas 2 :** Supposons que $x \in (A \cap B)$.
        Par la définition de l'intersection d'ensembles, l'appartenance de $x$ à $(A \cap B)$ signifie que $x \in A$ et $x \in B$.
        De cette conjonction logique, nous pouvons spécifiquement déduire que $x \in A$.
4.  Dans les deux cas possibles (que $x \in A$ ou que $x \in (A \cap B)$), nous avons systématiquement montré que $x$ appartient nécessairement à l'ensemble $A$.
5.  Puisque $x$ était un élément arbitraire de $A \cup (A \cap B)$ et que nous avons rigoureusement démontré qu'il appartient à $A$, nous pouvons conclure que l'ensemble $A \cup (A \cap B)$ est un sous-ensemble de $A$, ce qui s'écrit $A \cup (A \cap B) \subseteq A$.

**Partie 2 : Démontrons que $A \subseteq A \cup (A \cap B)$.**

1.  Soit $y$ un élément arbitraire de l'ensemble $A$.
2.  Par la définition de l'union d'ensembles, un élément appartient à $A \cup (A \cap B)$ si et seulement si il appartient à $A$ ou il appartient à $(A \cap B)$.
3.  Puisque nous avons supposé que $y \in A$, la première partie de la disjonction ("$y \in A$") est vraie.
4.  En logique propositionnelle, une disjonction (P ou Q) est vraie si au moins une de ses composantes (P ou Q) est vraie. Étant donné que "$y \in A$" est vraie, l'affirmation "$y \in A$ ou $y \in (A \cap B)$" est nécessairement vraie.
5.  Cela signifie, par la définition de l'union, que $y \in A \cup (A \cap B)$.
6.  Puisque $y$ était un élément arbitraire de $A$ et que nous avons démontré qu'il appartient à $A \cup (A \cap B)$, nous pouvons conclure que l'ensemble $A$ est un sous-ensemble de $A \cup (A \cap B)$, ce qui s'écrit $A \subseteq A \cup (A \cap B)$.

* **Conclusion :**
Nous avons démontré successivement que $A \cup (A \cap B) \subseteq A$ (Partie 1) et que $A \subseteq A \cup (A \cap B)$ (Partie 2). Par la propriété de double inclusion, qui stipule que si $X \subseteq Y$ et $Y \subseteq X$, alors $X = Y$, ces deux inclusions impliquent l'égalité des ensembles.
Par conséquent, nous avons prouvé que pour toutes parties $A$ et $B$ d'un ensemble $E$, l'égalité $A \cup (A \cap B) = A$ est vérifiée. Cette propriété est connue sous le nom de loi d'absorption pour l'union et l'intersection.
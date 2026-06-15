---
uuid: "jalon-4-exo-10"
title: "Exercice 10 - 5 étoiles"
---
# Exercice 10 : Distributivité de l'Intersection sur la Différence Symétrique et Conséquences
**Difficulté :** ⭐⭐⭐⭐⭐

## Énoncé
Soient $E$ un ensemble non vide et $A, B, C$ trois parties quelconques de $E$.

1.  Démontrer l'identité suivante, connue sous le nom de distributivité de l'intersection sur la différence symétrique :
    $$A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$$
    où $X \Delta Y$ représente la différence symétrique des ensembles $X$ et $Y$.

2.  En déduire que si $A \cap B = A \cap C$, alors $A \cap (B \Delta C) = \emptyset$.

## Correction Détaillée
*   **Analyse de l'énoncé :**
    L'exercice nous demande de prouver une identité fondamentale en théorie des ensembles, à savoir la distributivité de l'intersection sur la différence symétrique. Cette propriété est cruciale car elle est l'une des axiomes qui, avec d'autres, confère à l'ensemble des parties $\mathcal{P}(E)$ muni de la différence symétrique et de l'intersection une structure d'anneau de Boole. La première partie requiert une démonstration rigoureuse de cette identité. La stratégie la plus directe pour prouver l'égalité de deux ensembles est la double inclusion, c'est-à-dire montrer que chaque ensemble est un sous-ensemble de l'autre. Alternativement, on pourrait utiliser les fonctions indicatrices, mais la méthode par double inclusion est souvent plus fondamentale pour les débutants en théorie des ensembles et permet une justification pas-à-pas très explicite. La deuxième partie de l'exercice est une déduction directe de la première partie, ce qui signifie que le résultat de la première partie doit être utilisé comme point de départ pour la démonstration. Il faudra manipuler l'identité en utilisant l'hypothèse donnée.

*   **Résolution pas-à-pas :**

    **Partie 1 : Démontrer $A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$.**

    Pour prouver l'égalité de deux ensembles, nous allons démontrer la double inclusion : $A \cap (B \Delta C) \subseteq (A \cap B) \Delta (A \cap C)$ et $(A \cap B) \Delta (A \cap C) \subseteq A \cap (B \Delta C)$.

    Rappelons la définition de la différence symétrique pour deux ensembles $X$ et $Y$ :
    $$X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$$
    où $X \setminus Y = \{z \in E \mid z \in X \text{ et } z \notin Y\}$.

    **Étape 1 : Démontrons $A \cap (B \Delta C) \subseteq (A \cap B) \Delta (A \cap C)$.**

    Soit $x$ un élément quelconque de l'ensemble $A \cap (B \Delta C)$.
    Par définition de l'intersection, cela signifie que $x \in A$ et $x \in (B \Delta C)$.
    Par définition de la différence symétrique, $x \in (B \Delta C)$ signifie que $x \in (B \setminus C) \cup (C \setminus B)$.
    Cela implique que ($x \in B$ et $x \notin C$) ou ($x \in C$ et $x \notin B$).

    Nous allons analyser ces deux cas séparément.

    *   **Cas 1 : $x \in B$ et $x \notin C$.**
        Puisque nous savons que $x \in A$, nous avons les conditions suivantes :
        1.  $x \in A$
        2.  $x \in B$
        3.  $x \notin C$

        De (1) et (2), nous déduisons que $x \in A \cap B$ (par définition de l'intersection).
        De (1) et (3), nous déduisons que $x \notin A \cap C$ (car si $x$ était dans $A \cap C$, alors $x$ devrait être dans $C$, ce qui contredit $x \notin C$).
        Donc, $x \in A \cap B$ et $x \notin A \cap C$.
        Par définition de la différence ensembliste, cela signifie que $x \in (A \cap B) \setminus (A \cap C)$.
        Par définition de la différence symétrique, $(A \cap B) \setminus (A \cap C)$ est un sous-ensemble de $(A \cap B) \Delta (A \cap C)$.
        Par conséquent, $x \in (A \cap B) \Delta (A \cap C)$.

    *   **Cas 2 : $x \in C$ et $x \notin B$.**
        Puisque nous savons que $x \in A$, nous avons les conditions suivantes :
        1.  $x \in A$
        2.  $x \in C$
        3.  $x \notin B$

        De (1) et (2), nous déduisons que $x \in A \cap C$ (par définition de l'intersection).
        De (1) et (3), nous déduisons que $x \notin A \cap B$ (car si $x$ était dans $A \cap B$, alors $x$ devrait être dans $B$, ce qui contredit $x \notin B$).
        Donc, $x \in A \cap C$ et $x \notin A \cap B$.
        Par définition de la différence ensembliste, cela signifie que $x \in (A \cap C) \setminus (A \cap B)$.
        Par définition de la différence symétrique, $(A \cap C) \setminus (A \cap B)$ est un sous-ensemble de $(A \cap B) \Delta (A \cap C)$.
        Par conséquent, $x \in (A \cap B) \Delta (A \cap C)$.

    Dans les deux cas possibles, nous avons montré que si $x \in A \cap (B \Delta C)$, alors $x \in (A \cap B) \Delta (A \cap C)$.
    Nous avons donc prouvé la première inclusion : $A \cap (B \Delta C) \subseteq (A \cap B) \Delta (A \cap C)$.

    **Étape 2 : Démontrons $(A \cap B) \Delta (A \cap C) \subseteq A \cap (B \Delta C)$.**

    Soit $y$ un élément quelconque de l'ensemble $(A \cap B) \Delta (A \cap C)$.
    Par définition de la différence symétrique, cela signifie que $y \in ((A \cap B) \setminus (A \cap C)) \cup ((A \cap C) \setminus (A \cap B))$.
    Cela implique que ($y \in A \cap B$ et $y \notin A \cap C$) ou ($y \in A \cap C$ et $y \notin A \cap B$).

    Nous allons analyser ces deux cas séparément.

    *   **Cas 1 : $y \in A \cap B$ et $y \notin A \cap C$.**
        De $y \in A \cap B$, nous déduisons que $y \in A$ et $y \in B$ (par définition de l'intersection).
        De $y \notin A \cap C$, nous déduisons que $y$ n'est pas dans l'intersection de $A$ et $C$. Cela signifie que ($y \notin A$ ou $y \notin C$).
        Puisque nous savons déjà que $y \in A$, l'affirmation $y \notin A$ est fausse. Par conséquent, il doit être vrai que $y \notin C$.
        En résumé, nous avons les conditions suivantes :
        1.  $y \in A$
        2.  $y \in B$
        3.  $y \notin C$

        De (2) et (3), nous déduisons que $y \in B \setminus C$ (par définition de la différence ensembliste).
        Par définition de la différence symétrique, $B \setminus C$ est un sous-ensemble de $B \Delta C$.
        Donc, $y \in B \Delta C$.
        Puisque nous avons $y \in A$ (condition 1) et $y \in B \Delta C$, nous déduisons que $y \in A \cap (B \Delta C)$ (par définition de l'intersection).

    *   **Cas 2 : $y \in A \cap C$ et $y \notin A \cap B$.**
        De $y \in A \cap C$, nous déduisons que $y \in A$ et $y \in C$ (par définition de l'intersection).
        De $y \notin A \cap B$, nous déduisons que $y$ n'est pas dans l'intersection de $A$ et $B$. Cela signifie que ($y \notin A$ ou $y \notin B$).
        Puisque nous savons déjà que $y \in A$, l'affirmation $y \notin A$ est fausse. Par conséquent, il doit être vrai que $y \notin B$.
        En résumé, nous avons les conditions suivantes :
        1.  $y \in A$
        2.  $y \in C$
        3.  $y \notin B$

        De (2) et (3), nous déduisons que $y \in C \setminus B$ (par définition de la différence ensembliste).
        Par définition de la différence symétrique, $C \setminus B$ est un sous-ensemble de $B \Delta C$.
        Donc, $y \in B \Delta C$.
        Puisque nous avons $y \in A$ (condition 1) et $y \in B \Delta C$, nous déduisons que $y \in A \cap (B \Delta C)$ (par définition de l'intersection).

    Dans les deux cas possibles, nous avons montré que si $y \in (A \cap B) \Delta (A \cap C)$, alors $y \in A \cap (B \Delta C)$.
    Nous avons donc prouvé la deuxième inclusion : $(A \cap B) \Delta (A \cap C) \subseteq A \cap (B \Delta C)$.

    **Conclusion de la Partie 1 :**
    Puisque nous avons démontré les deux inclusions, $A \cap (B \Delta C) \subseteq (A \cap B) \Delta (A \cap C)$ et $(A \cap B) \Delta (A \cap C) \subseteq A \cap (B \Delta C)$, nous pouvons conclure que les deux ensembles sont égaux :
    $$A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$$

    ---

    **Partie 2 : En déduire que si $A \cap B = A \cap C$, alors $A \cap (B \Delta C) = \emptyset$.**

    Nous partons de l'identité démontrée dans la Partie 1 :
    $$A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$$

    Nous avons l'hypothèse que $A \cap B = A \cap C$.
    Nous allons substituer cette égalité dans le membre de droite de l'identité.
    Soit $X = A \cap B$. Alors, d'après l'hypothèse, $A \cap C = X$.
    Le membre de droite devient alors $X \Delta X$.

    Appliquons la définition de la différence symétrique à $X \Delta X$ :
    $$X \Delta X = (X \setminus X) \cup (X \setminus X)$$

    Par définition de la différence ensembliste, pour tout ensemble $X$, $X \setminus X$ est l'ensemble des éléments qui sont dans $X$ et qui ne sont pas dans $X$. Un tel ensemble ne contient aucun élément, il est donc égal à l'ensemble vide $\emptyset$.
    Ainsi, $X \setminus X = \emptyset$.

    En substituant cela dans l'expression de $X \Delta X$ :
    $$X \Delta X = \emptyset \cup \emptyset$$

    Par définition de l'union, l'union de l'ensemble vide avec l'ensemble vide est l'ensemble vide lui-même :
    $$\emptyset \cup \emptyset = \emptyset$$

    Par conséquent, nous avons montré que $(A \cap B) \Delta (A \cap C) = \emptyset$ sous l'hypothèse $A \cap B = A \cap C$.

    En utilisant l'identité démontrée dans la Partie 1, nous pouvons remplacer le membre de droite par $\emptyset$ :
    $$A \cap (B \Delta C) = \emptyset$$

    Nous avons ainsi déduit que si $A \cap B = A \cap C$, alors $A \cap (B \Delta C) = \emptyset$.

*   **Conclusion :**
    Nous avons rigoureusement démontré la propriété de distributivité de l'intersection sur la différence symétrique, à savoir $A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$, en utilisant la méthode de la double inclusion avec une analyse exhaustive de tous les cas possibles pour les éléments. Cette identité est fondamentale en théorie des ensembles et en algèbre booléenne. De plus, nous avons utilisé cette identité pour en déduire une conséquence significative : si l'intersection d'un ensemble $A$ avec $B$ est la même que son intersection avec $C$, alors l'intersection de $A$ avec la différence symétrique de $B$ et $C$ est nécessairement l'ensemble vide. Cela illustre comment des propriétés établies peuvent être utilisées pour dériver de nouveaux résultats logiques de manière structurée et déductive.
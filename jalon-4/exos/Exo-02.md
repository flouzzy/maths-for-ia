---
uuid: "jalon-4-exo-02"
title: "Exercice 02 - 1 étoiles"
---
# Exercice 02 : Égalité entre différence ensembliste et intersection du complémentaire
**Difficulté :** ⭐

## Énoncé
Soit $E$ un ensemble non vide. Soient $A$ et $B$ deux parties de $E$.
Démontrez l'égalité suivante :
$$A \setminus B = A \cap B^c$$
où $B^c$ désigne le complémentaire de $B$ dans $E$.

## Correction Détaillée
*   **Analyse de l'énoncé :**
    L'objectif de cet exercice est de démontrer l'égalité entre deux ensembles, $A \setminus B$ et $A \cap B^c$. Pour prouver que deux ensembles sont égaux, la stratégie standard en théorie des ensembles est de démontrer la double inclusion. C'est-à-dire, nous devons montrer que $A \setminus B \subseteq A \cap B^c$ et que $A \cap B^c \subseteq A \setminus B$. Pour chaque inclusion, nous prendrons un élément arbitraire de l'ensemble de départ et nous montrerons qu'il appartient nécessairement à l'ensemble d'arrivée, en utilisant les définitions précises des opérations ensemblistes (différence, intersection, complémentaire).

*   **Résolution pas-à-pas :**

    **Partie 1 : Démontrons que $A \setminus B \subseteq A \cap B^c$.**

    1.  Soit $x$ un élément arbitraire de l'ensemble $A \setminus B$.
    2.  Par définition de la différence ensembliste, un élément $x$ appartient à $A \setminus B$ si et seulement si $x$ appartient à $A$ et $x$ n'appartient pas à $B$.
        Ainsi, nous avons les deux conditions suivantes :
        (i) $x \in A$
        (ii) $x \notin B$
    3.  Par définition du complémentaire d'un ensemble, un élément $x$ n'appartient pas à $B$ (c'est-à-dire $x \notin B$) si et seulement si $x$ appartient au complémentaire de $B$ dans $E$, noté $B^c$.
        Donc, la condition (ii) $x \notin B$ est équivalente à $x \in B^c$.
    4.  En combinant les résultats des étapes 2 et 3, nous avons maintenant les deux conditions suivantes pour $x$ :
        (i) $x \in A$
        (ii) $x \in B^c$
    5.  Par définition de l'intersection ensembliste, un élément $x$ appartient à l'intersection de deux ensembles $A$ et $B^c$ (c'est-à-dire $A \cap B^c$) si et seulement si $x$ appartient à $A$ et $x$ appartient à $B^c$.
        Puisque $x \in A$ et $x \in B^c$, nous pouvons conclure que $x \in A \cap B^c$.
    6.  Ayant pris un élément $x$ arbitraire dans $A \setminus B$ et démontré qu'il appartient nécessairement à $A \cap B^c$, nous avons prouvé l'inclusion :
        $A \setminus B \subseteq A \cap B^c$.

    **Partie 2 : Démontrons que $A \cap B^c \subseteq A \setminus B$.**

    1.  Soit $y$ un élément arbitraire de l'ensemble $A \cap B^c$.
    2.  Par définition de l'intersection ensembliste, un élément $y$ appartient à $A \cap B^c$ si et seulement si $y$ appartient à $A$ et $y$ appartient à $B^c$.
        Ainsi, nous avons les deux conditions suivantes :
        (i) $y \in A$
        (ii) $y \in B^c$
    3.  Par définition du complémentaire d'un ensemble, un élément $y$ appartient à $B^c$ (c'est-à-dire $y \in B^c$) si et seulement si $y$ n'appartient pas à $B$ (c'est-à-dire $y \notin B$).
        Donc, la condition (ii) $y \in B^c$ est équivalente à $y \notin B$.
    4.  En combinant les résultats des étapes 2 et 3, nous avons maintenant les deux conditions suivantes pour $y$ :
        (i) $y \in A$
        (ii) $y \notin B$
    5.  Par définition de la différence ensembliste, un élément $y$ appartient à la différence de deux ensembles $A$ et $B$ (c'est-à-dire $A \setminus B$) si et seulement si $y$ appartient à $A$ et $y$ n'appartient pas à $B$.
        Puisque $y \in A$ et $y \notin B$, nous pouvons conclure que $y \in A \setminus B$.
    6.  Ayant pris un élément $y$ arbitraire dans $A \cap B^c$ et démontré qu'il appartient nécessairement à $A \setminus B$, nous avons prouvé l'inclusion :
        $A \cap B^c \subseteq A \setminus B$.

    **Partie 3 : Conclusion de l'égalité.**

    Puisque nous avons démontré la double inclusion :
    1.  $A \setminus B \subseteq A \cap B^c$
    2.  $A \cap B^c \subseteq A \setminus B$
    Nous pouvons affirmer que les deux ensembles sont égaux.

*   **Conclusion :**
    Nous avons rigoureusement démontré, en utilisant les définitions fondamentales des opérations ensemblistes (différence, complémentaire et intersection) et la méthode de la double inclusion, que pour toutes parties $A$ et $B$ d'un ensemble $E$, l'égalité $A \setminus B = A \cap B^c$ est vérifiée. Cette identité est un résultat fondamental en théorie des ensembles, souvent utilisée pour simplifier des expressions ensemblistes ou pour prouver d'autres propriétés.
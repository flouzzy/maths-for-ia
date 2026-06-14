---
uuid: "jalon-4-exo-03"
title: "Exercice 03 - 2 étoiles"
---
# Exercice 03 : Égalité de la Différence Symétrique par Opérations Fondamentales
**Difficulté :** ⭐⭐

## Énoncé
Soient $E$ un ensemble non vide, et $A$, $B$ deux parties de $E$.
La différence symétrique de $A$ et $B$, notée $A \Delta B$, est définie par $A \Delta B = (A \setminus B) \cup (B \setminus A)$.

Démontrer l'égalité suivante :
$$A \Delta B = (A \cup B) \setminus (A \cap B)$$

## Correction Détaillée
*   **Analyse de l'énoncé :**
    L'objectif de cet exercice est de démontrer une égalité entre deux expressions d'ensembles. La première expression est la définition de la différence symétrique $A \Delta B$, tandis que la seconde est une combinaison d'opérations d'union, d'intersection et de différence ensembliste. Pour prouver l'égalité de deux ensembles, nous allons utiliser la méthode des équivalences logiques pour un élément arbitraire $x$ de l'ensemble universel $E$. Cela signifie que nous allons montrer que $x \in A \Delta B$ est logiquement équivalent à $x \in (A \cup B) \setminus (A \cap B)$.

    Nous rappelons les définitions des opérations ensemblistes utilisées :
    *   $x \in X \cup Y \iff (x \in X \lor x \in Y)$
    *   $x \in X \cap Y \iff (x \in X \land x \in Y)$
    *   $x \in X \setminus Y \iff (x \in X \land x \notin Y)$
    *   $x \notin X \iff \neg (x \in X)$

*   **Résolution pas-à-pas :**
    Soit $x$ un élément arbitraire de l'ensemble $E$.

    1.  **Partir de la définition de $x \in A \Delta B$ :**
        Par définition de la différence symétrique, nous avons :
        $$x \in A \Delta B \iff x \in (A \setminus B) \cup (B \setminus A)$$

    2.  **Appliquer la définition de l'union :**
        L'appartenance à l'union $(A \setminus B) \cup (B \setminus A)$ signifie que $x$ appartient à au moins l'un des deux ensembles $A \setminus B$ ou $B \setminus A$.
        $$x \in (A \setminus B) \cup (B \setminus A) \iff (x \in A \setminus B) \lor (x \in B \setminus A)$$

    3.  **Appliquer la définition de la différence ensembliste :**
        Nous remplaçons les expressions $x \in A \setminus B$ et $x \in B \setminus A$ par leurs définitions logiques.
        *   $x \in A \setminus B \iff (x \in A \land x \notin B)$
        *   $x \in B \setminus A \iff (x \in B \land x \notin A)$
        En substituant ces équivalences dans l'expression précédente, nous obtenons :
        $$(x \in A \land x \notin B) \lor (x \in B \land x \notin A)$$
        Cette expression logique signifie que $x$ appartient à $A$ mais pas à $B$, OU $x$ appartient à $B$ mais pas à $A$. En d'autres termes, $x$ appartient à exactement un des deux ensembles $A$ ou $B$.

    4.  **Reformuler l'expression logique :**
        Nous cherchons à montrer que l'expression $(x \in A \land x \notin B) \lor (x \in B \land x \notin A)$ est équivalente à $(x \in A \lor x \in B) \land \neg (x \in A \land x \in B)$.

        Considérons les conditions pour que $x$ satisfasse $(x \in A \land x \notin B) \lor (x \in B \land x \notin A)$ :
        *   **Cas 1 :** $x \in A$ et $x \notin B$.
            Dans ce cas, $x$ est bien dans $A \cup B$ (car $x \in A$).
            De plus, $x$ n'est pas dans $A \cap B$ (car $x \notin B$).
            Donc, $x \in (A \cup B) \setminus (A \cap B)$.
        *   **Cas 2 :** $x \in B$ et $x \notin A$.
            Dans ce cas, $x$ est bien dans $A \cup B$ (car $x \in B$).
            De plus, $x$ n'est pas dans $A \cap B$ (car $x \notin A$).
            Donc, $x \in (A \cup B) \setminus (A \cap B)$.
        *   **Cas 3 :** $x \in A$ et $x \in B$.
            Dans ce cas, l'expression $(x \in A \land x \notin B)$ est fausse (car $x \notin B$ est faux).
            L'expression $(x \in B \land x \notin A)$ est fausse (car $x \notin A$ est faux).
            Donc, $(x \in A \land x \notin B) \lor (x \in B \land x \notin A)$ est fausse.
            Par ailleurs, si $x \in A$ et $x \in B$, alors $x \in A \cap B$.
            Donc $x \notin (A \cup B) \setminus (A \cap B)$ (car $x$ est dans $A \cap B$, donc il est "soustraite").
        *   **Cas 4 :** $x \notin A$ et $x \notin B$.
            Dans ce cas, l'expression $(x \in A \land x \notin B)$ est fausse (car $x \in A$ est faux).
            L'expression $(x \in B \land x \notin A)$ est fausse (car $x \in B$ est faux).
            Donc, $(x \in A \land x \notin B) \lor (x \in B \land x \notin A)$ est fausse.
            Par ailleurs, si $x \notin A$ et $x \notin B$, alors $x \notin A \cup B$.
            Donc $x \notin (A \cup B) \setminus (A \cap B)$ (car $x$ n'est pas dans $A \cup B$).

        Les quatre cas couvrent toutes les possibilités pour $x$. Nous avons montré que $x$ satisfait l'expression de gauche si et seulement si $x$ satisfait l'expression de droite.
        Ainsi, nous pouvons écrire l'équivalence logique :
        $$(x \in A \land x \notin B) \lor (x \in B \land x \notin A) \iff (x \in A \lor x \in B) \land \neg (x \in A \land x \in B)$$

    5.  **Traduire l'expression logique en termes d'ensembles :**
        L'expression $(x \in A \lor x \in B)$ est équivalente à $x \in A \cup B$.
        L'expression $(x \in A \land x \in B)$ est équivalente à $x \in A \cap B$.
        L'expression $\neg (x \in A \land x \in B)$ est équivalente à $x \notin A \cap B$.

        En combinant ces équivalences, nous obtenons :
        $$(x \in A \lor x \in B) \land \neg (x \in A \land x \in B) \iff (x \in A \cup B) \land (x \notin A \cap B)$$

    6.  **Appliquer la définition de la différence ensembliste pour la deuxième fois :**
        L'expression $(x \in A \cup B) \land (x \notin A \cap B)$ est, par définition, l'appartenance à la différence de deux ensembles.
        $$(x \in A \cup B) \land (x \notin A \cap B) \iff x \in (A \cup B) \setminus (A \cap B)$$

    7.  **Conclusion de la chaîne d'équivalences :**
        En récapitulant toutes les étapes, nous avons montré que pour tout élément $x \in E$ :
        $$x \in A \Delta B \iff x \in (A \setminus B) \cup (B \setminus A)$$
        $$\iff (x \in A \land x \notin B) \lor (x \in B \land x \notin A)$$
        $$\iff (x \in A \lor x \in B) \land \neg (x \in A \land x \in B)$$
        $$\iff (x \in A \cup B) \land (x \notin A \cap B)$$
        $$\iff x \in (A \cup B) \setminus (A \cap B)$$
        Puisque l'appartenance d'un élément arbitraire $x$ à $A \Delta B$ est logiquement équivalente à son appartenance à $(A \cup B) \setminus (A \cap B)$, les deux ensembles sont égaux.

*   **Conclusion :**
    Nous avons démontré, par une série d'équivalences logiques détaillées pour un élément arbitraire $x \in E$, que la définition de la différence symétrique $A \Delta B = (A \setminus B) \cup (B \setminus A)$ est équivalente à l'expression $(A \cup B) \setminus (A \cap B)$. Cette égalité est une propriété fondamentale de la théorie des ensembles, souvent utilisée pour caractériser la différence symétrique comme l'ensemble des éléments qui appartiennent à l'union mais pas à l'intersection des deux ensembles.
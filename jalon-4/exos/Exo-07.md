---
uuid: "jalon-4-exo-07"
title: "Exercice 07 - 4 étoiles"
---
# Exercice 07 : Associativité de la Différence Symétrique
**Difficulté :** ⭐⭐⭐⭐

## Énoncé
Soient $E$ un ensemble universel et $A, B, C$ trois parties quelconques de $E$.
La différence symétrique de deux ensembles $X$ et $Y$, notée $X \Delta Y$, est définie comme l'ensemble des éléments qui appartiennent à $X$ ou à $Y$, mais pas aux deux. Formellement :
$$X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$$
Démontrez que l'opération de différence symétrique est associative, c'est-à-dire que :
$$(A \Delta B) \Delta C = A \Delta (B \Delta C)$$

## Correction Détaillée
*   **Analyse de l'énoncé :**
    Nous devons démontrer l'associativité de l'opération de différence symétrique. Cela signifie que pour toutes parties $A, B, C$ d'un ensemble universel $E$, l'ensemble $(A \Delta B) \Delta C$ doit être égal à l'ensemble $A \Delta (B \Delta C)$. Pour prouver l'égalité de deux ensembles, la méthode la plus rigoureuse consiste à montrer que tout élément $x$ appartenant au premier ensemble appartient aussi au second, et réciproquement. Cela revient à établir l'équivalence logique : $x \in (A \Delta B) \Delta C \iff x \in A \Delta (B \Delta C)$ pour un élément $x$ arbitraire de $E$. Nous allons traduire l'appartenance aux ensembles en propositions logiques et utiliser une table de vérité pour démontrer l'équivalence des expressions logiques correspondantes.

*   **Résolution pas-à-pas :**

    1.  **Définition de la différence symétrique en termes d'appartenance :**
        Soient $X$ et $Y$ deux parties d'un ensemble $E$. Par définition, un élément $x$ de $E$ appartient à la différence symétrique $X \Delta Y$ si et seulement si $x$ appartient à $X$ et pas à $Y$, ou $x$ appartient à $Y$ et pas à $X$.
        Formellement, pour tout élément $x \in E$ :
        $$x \in X \Delta Y \iff (x \in X \land x \notin Y) \lor (x \in Y \land x \notin X)$$
        Cette proposition logique correspond à l'opérateur de disjonction exclusive (XOR), souvent noté $\oplus$. Si nous posons $P_X \equiv (x \in X)$ et $P_Y \equiv (x \in Y)$, alors l'appartenance s'écrit :
        $$x \in X \Delta Y \iff P_X \oplus P_Y$$

    2.  **Traduction de l'objectif en propositions logiques :**
        Nous voulons prouver que $(A \Delta B) \Delta C = A \Delta (B \Delta C)$. Cela équivaut à montrer que pour tout élément $x \in E$ :
        $$x \in (A \Delta B) \Delta C \iff x \in A \Delta (B \Delta C)$$
        En utilisant les propositions $P_A := (x \in A)$, $P_B := (x \in B)$ et $P_C := (x \in C)$, l'équivalence à démontrer devient :
        $$(P_A \oplus P_B) \oplus P_C \iff P_A \oplus (P_B \oplus P_C)$$
        Ceci est la propriété d'associativité de l'opérateur logique XOR.

    3.  **Démonstration par table de vérité :**
        Pour prouver cette équivalence logique de manière exhaustive et sans aucune ellipse, nous allons construire une table de vérité pour les deux expressions $(P_A \oplus P_B) \oplus P_C$ et $P_A \oplus (P_B \oplus P_C)$. La table de vérité énumère toutes les $2^3 = 8$ combinaisons possibles des valeurs de vérité (Vrai/V, Faux/F) pour les propositions $P_A, P_B, P_C$.

        Rappel de la définition de $P \oplus Q$ : $P \oplus Q$ est Vrai si et seulement si $P$ et $Q$ ont des valeurs de vérité différentes.

        | $P_A$ | $P_B$ | $P_C$ | $P_A \oplus P_B$ | $(P_A \oplus P_B) \oplus P_C$ | $P_B \oplus P_C$ | $P_A \oplus (P_B \oplus P_C)$ |
        | :---- | :---- | :---- | :--------------- | :----------------------------- | :--------------- | :----------------------------- |
        | F     | F     | F     | F                | F                              | F                | F                              |
        | F     | F     | V     | F                | V                              | V                | V                              |
        | F     | V     | F     | V                | V                              | V                | V                              |
        | F     | V     | V     | V                | F                              | F                | F                              |
        | V     | F     | F     | V                | V                              | F                | V                              |
        | V     | F     | V     | V                | F                              | V                | F                              |
        | V     | V     | F     | F                | F                              | V                | F                              |
        | V     | V     | V     | F                | V                              | F                | V                              |

        **Analyse détaillée des colonnes :**
        *   **Colonne $P_A \oplus P_B$ :** Cette colonne est obtenue en appliquant l'opérateur XOR aux valeurs de $P_A$ et $P_B$. Par exemple, à la première ligne (F, F), $P_A \oplus P_B$ est F. À la deuxième ligne (F, V), $P_A \oplus P_B$ est V.
        *   **Colonne $(P_A \oplus P_B) \oplus P_C$ :** Cette colonne est obtenue en appliquant l'opérateur XOR aux valeurs de la colonne $(P_A \oplus P_B)$ et de la colonne $P_C$. Par exemple, à la deuxième ligne, $(P_A \oplus P_B)$ est F et $P_C$ est V, donc $(P_A \oplus P_B) \oplus P_C$ est F $\oplus$ V, ce qui donne V. À la quatrième ligne, $(P_A \oplus P_B)$ est V et $P_C$ est V, donc $(P_A \oplus P_B) \oplus P_C$ est V $\oplus$ V, ce qui donne F.
        *   **Colonne $P_B \oplus P_C$ :** Cette colonne est obtenue en appliquant l'opérateur XOR aux valeurs de $P_B$ et $P_C$. Par exemple, à la première ligne (F, F), $P_B \oplus P_C$ est F. À la deuxième ligne (F, V), $P_B \oplus P_C$ est V.
        *   **Colonne $P_A \oplus (P_B \oplus P_C)$ :** Cette colonne est obtenue en appliquant l'opérateur XOR aux valeurs de la colonne $P_A$ et de la colonne $(P_B \oplus P_C)$. Par exemple, à la deuxième ligne, $P_A$ est F et $(P_B \oplus P_C)$ est V, donc $P_A \oplus (P_B \oplus P_C)$ est F $\oplus$ V, ce qui donne V. À la quatrième ligne, $P_A$ est F et $(P_B \oplus P_C)$ est F, donc $P_A \oplus (P_B \oplus P_C)$ est F $\oplus$ F, ce qui donne F.

        En comparant la colonne $(P_A \oplus P_B) \oplus P_C$ et la colonne $P_A \oplus (P_B \oplus P_C)$, nous observons qu'elles sont identiques pour toutes les 8 combinaisons possibles des valeurs de vérité de $P_A, P_B, P_C$.
        Par conséquent, l'équivalence logique $(P_A \oplus P_B) \oplus P_C \iff P_A \oplus (P_B \oplus P_C)$ est rigoureusement démontrée.

    4.  **Conclusion sur l'égalité des ensembles :**
        Puisque nous avons établi que $x \in (A \Delta B) \Delta C \iff (P_A \oplus P_B) \oplus P_C$ et $x \in A \Delta (B \Delta C) \iff P_A \oplus (P_B \oplus P_C)$, et que les expressions logiques correspondantes sont équivalentes, il s'ensuit que :
        $$x \in (A \Delta B) \Delta C \iff x \in A \Delta (B \Delta C)$$
        Cette équivalence est vraie pour tout élément $x$ de l'ensemble universel $E$. Par la définition de l'égalité des ensembles (deux ensembles sont égaux si et seulement s'ils contiennent exactement les mêmes éléments), nous pouvons conclure que les ensembles sont égaux.

*   **Conclusion :**
    Nous avons démontré de manière exhaustive, en utilisant la définition élémentaire de la différence symétrique et une table de vérité pour les propositions logiques associées, que l'opération de différence symétrique est associative. Pour toutes parties $A, B, C$ d'un ensemble universel $E$, l'égalité $(A \Delta B) \Delta C = A \Delta (B \Delta C)$ est vérifiée. Cette propriété fondamentale, combinée à la commutativité et à l'existence d'un élément neutre (l'ensemble vide) et d'un inverse (chaque ensemble est son propre inverse), fait de l'ensemble des parties de $E$, muni de la différence symétrique, une structure de groupe abélien.
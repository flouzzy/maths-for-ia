---
uuid: "jalon-4-exo-04"
title: "Exercice 04 - 2 étoiles"
---
# Exercice 04 : Propriété de la différence ensembliste et de l'union
**Difficulté :** ⭐⭐

## Énoncé
Soient $E$ un ensemble non vide, et $A, B, C$ trois parties quelconques de $E$.
Démontrez l'égalité suivante :
$$ A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) $$

## Correction Détaillée
*   **Analyse de l'énoncé :** Nous devons démontrer l'égalité entre deux ensembles, $A \setminus (B \cup C)$ et $(A \setminus B) \cap (A \setminus C)$. Pour ce faire, la stratégie standard en théorie des ensembles consiste à prouver une double inclusion. C'est-à-dire, nous allons montrer que tout élément appartenant au premier ensemble appartient également au second (première inclusion), et réciproquement, que tout élément appartenant au second ensemble appartient également au premier (seconde inclusion). Nous utiliserons rigoureusement les définitions des opérations ensemblistes : la différence ensembliste ($\setminus$), l'union ($\cup$) et l'intersection ($\cap$).

*   **Résolution pas-à-pas :**

    **Partie 1 : Démontrons que $A \setminus (B \cup C) \subseteq (A \setminus B) \cap (A \setminus C)$.**

    1.  Soit $x$ un élément quelconque appartenant à l'ensemble $A \setminus (B \cup C)$.
    2.  Par définition de la différence ensembliste, l'appartenance de $x$ à $A \setminus (B \cup C)$ signifie que $x \in A$ et $x \notin (B \cup C)$.
    3.  L'affirmation $x \notin (B \cup C)$ signifie, par définition de l'union ensembliste, que $x$ n'appartient ni à $B$ ni à $C$. Autrement dit, nous avons simultanément $x \notin B$ et $x \notin C$.
    4.  En combinant les informations obtenues aux étapes 2 et 3, nous avons les trois conditions suivantes vérifiées simultanément pour $x$ :
        *   $x \in A$
        *   $x \notin B$
        *   $x \notin C$
    5.  À partir des deux premières conditions ($x \in A$ et $x \notin B$), nous pouvons conclure, par définition de la différence ensembliste, que $x \in (A \setminus B)$.
    6.  De même, à partir de la première et de la troisième condition ($x \in A$ et $x \notin C$), nous pouvons conclure, par définition de la différence ensembliste, que $x \in (A \setminus C)$.
    7.  Puisque nous avons établi que $x \in (A \setminus B)$ (d'après l'étape 5) et $x \in (A \setminus C)$ (d'après l'étape 6), il s'ensuit, par définition de l'intersection ensembliste, que $x \in (A \setminus B) \cap (A \setminus C)$.
    8.  Ayant démontré que si un élément $x$ appartient à $A \setminus (B \cup C)$, alors cet élément $x$ appartient nécessairement à $(A \setminus B) \cap (A \setminus C)$, nous avons prouvé la première inclusion : $A \setminus (B \cup C) \subseteq (A \setminus B) \cap (A \setminus C)$.

    **Partie 2 : Démontrons que $(A \setminus B) \cap (A \setminus C) \subseteq A \setminus (B \cup C)$.**

    1.  Soit $y$ un élément quelconque appartenant à l'ensemble $(A \setminus B) \cap (A \setminus C)$.
    2.  Par définition de l'intersection ensembliste, l'appartenance de $y$ à $(A \setminus B) \cap (A \setminus C)$ signifie que $y \in (A \setminus B)$ et $y \in (A \setminus C)$.
    3.  L'affirmation $y \in (A \setminus B)$ signifie, par définition de la différence ensembliste, que $y \in A$ et $y \notin B$.
    4.  L'affirmation $y \in (A \setminus C)$ signifie, par définition de la différence ensembliste, que $y \in A$ et $y \notin C$.
    5.  En combinant les informations obtenues aux étapes 3 et 4, nous avons les trois conditions suivantes vérifiées simultanément pour $y$ :
        *   $y \in A$ (cette condition est présente dans les deux affirmations précédentes)
        *   $y \notin B$
        *   $y \notin C$
    6.  Les conditions $y \notin B$ et $y \notin C$ signifient, par définition de l'union ensembliste (et de sa négation), que $y$ n'appartient pas à l'union de $B$ et $C$. Autrement dit, $y \notin (B \cup C)$.
    7.  En combinant l'information $y \in A$ (de l'étape 5) et l'information $y \notin (B \cup C)$ (de l'étape 6), il s'ensuit, par définition de la différence ensembliste, que $y \in A \setminus (B \cup C)$.
    8.  Ayant démontré que si un élément $y$ appartient à $(A \setminus B) \cap (A \setminus C)$, alors cet élément $y$ appartient nécessairement à $A \setminus (B \cup C)$, nous avons prouvé la seconde inclusion : $(A \setminus B) \cap (A \setminus C) \subseteq A \setminus (B \cup C)$.

*   **Conclusion :** Puisque nous avons démontré la double inclusion, c'est-à-dire $A \setminus (B \cup C) \subseteq (A \setminus B) \cap (A \setminus C)$ (Partie 1) et $(A \setminus B) \cap (A \setminus C) \subseteq A \setminus (B \cup C)$ (Partie 2), nous pouvons conclure que les deux ensembles sont égaux.
    Ainsi, nous avons bien démontré que pour tout ensemble $E$ et toutes parties $A, B, C$ de $E$ :
    $$ A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) $$
    Cette propriété est une identité fondamentale en théorie des ensembles, souvent utile pour simplifier des expressions ensemblistes complexes.
---
uuid: "jalon-4-exo-05"
title: "Exercice 05 - 3 étoiles"
---
# Exercice 05 : Distributivité de l'intersection sur la différence symétrique
**Difficulté :** ⭐⭐⭐

## Énoncé
Soient $E$ un ensemble non vide, et $A$, $B$, $C$ trois parties quelconques de $E$.
Démontrer l'égalité ensembliste suivante :
$$ (A \Delta B) \cap C = (A \cap C) \Delta (B \cap C) $$

## Correction Détaillée
*   **Analyse de l'énoncé :**
    L'objectif de cet exercice est de démontrer une égalité entre deux ensembles. La stratégie adoptée sera de montrer que l'appartenance d'un élément $x$ à l'ensemble de gauche est logiquement équivalente à son appartenance à l'ensemble de droite. Pour ce faire, nous allons utiliser les définitions des opérations ensemblistes ($\cap$ pour l'intersection, $\Delta$ pour la différence symétrique, $\setminus$ pour la différence ensembliste) et les lois de la logique propositionnelle.

    Rappelons les définitions clés :
    1.  L'intersection : $X \cap Y = \{x \in E \mid x \in X \land x \in Y\}$
    2.  La différence ensembliste : $X \setminus Y = \{x \in E \mid x \in X \land x \notin Y\}$
    3.  La différence symétrique : $X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$

    Nous allons procéder par une chaîne d'équivalences logiques en partant de l'appartenance d'un élément $x$ à l'ensemble de gauche, et en le transformant pas à pas jusqu'à obtenir l'appartenance à l'ensemble de droite.

*   **Résolution pas-à-pas :**
    Soit $x$ un élément quelconque de l'ensemble $E$.

    Nous commençons par l'appartenance de $x$ à l'ensemble de gauche, $(A \Delta B) \cap C$ :
    $$ x \in (A \Delta B) \cap C $$
    Par définition de l'intersection, cela signifie que $x$ appartient à $A \Delta B$ ET $x$ appartient à $C$ :
    $$ \iff (x \in A \Delta B) \land (x \in C) $$
    Par définition de la différence symétrique, $x \in A \Delta B$ signifie que $x$ appartient à $(A \setminus B) \cup (B \setminus A)$ :
    $$ \iff ((x \in A \setminus B) \lor (x \in B \setminus A)) \land (x \in C) $$
    Par définition de la différence ensembliste, $x \in A \setminus B$ signifie $(x \in A \land x \notin B)$, et $x \in B \setminus A$ signifie $(x \in B \land x \notin A)$ :
    $$ \iff (((x \in A) \land (x \notin B)) \lor ((x \in B) \land (x \notin A))) \land (x \in C) $$
    Nous appliquons la loi de distributivité de la conjonction $(\land)$ sur la disjonction $(\lor)$, c'est-à-dire $(P \lor Q) \land R \iff (P \land R) \lor (Q \land R)$ :
    $$ \iff (((x \in A) \land (x \notin B) \land (x \in C)) \lor ((x \in B) \land (x \notin A) \land (x \in C))) $$
    Nous réarrangeons les termes dans chaque conjonction en utilisant la commutativité et l'associativité de la conjonction pour regrouper $x \in A$ avec $x \in C$, et $x \in B$ avec $x \in C$ :
    $$ \iff (((x \in A \land x \in C) \land x \notin B) \lor ((x \in B \land x \in C) \land x \notin A))) $$
    Par définition de l'intersection, $(x \in A \land x \in C)$ est équivalent à $x \in A \cap C$, et $(x \in B \land x \in C)$ est équivalent à $x \in B \cap C$ :
    $$ \iff ((x \in A \cap C \land x \notin B) \lor (x \in B \cap C \land x \notin A)) $$
    Ceci est notre expression intermédiaire. Nous allons maintenant travailler sur l'ensemble de droite, $(A \cap C) \Delta (B \cap C)$, et montrer qu'il est équivalent à cette expression.

    Soit $X' = A \cap C$ et $Y' = B \cap C$. Nous voulons montrer que $x \in X' \Delta Y'$.
    Par définition de la différence symétrique :
    $$ x \in (A \cap C) \Delta (B \cap C) \iff (x \in (A \cap C) \setminus (B \cap C)) \lor (x \in (B \cap C) \setminus (A \cap C)) $$
    Par définition de la différence ensembliste :
    $$ \iff ((x \in A \cap C \land x \notin B \cap C) \lor (x \in B \cap C \land x \notin A \cap C)) $$
    Par définition de l'intersection :
    $$ \iff ((x \in A \land x \in C \land \neg(x \in B \land x \in C)) \lor (x \in B \land x \in C \land \neg(x \in A \land x \in C))) $$
    Nous appliquons la loi de De Morgan pour la négation d'une conjonction, $\neg(P \land Q) \iff (\neg P \lor \neg Q)$ :
    $$ \iff ((x \in A \land x \in C \land (x \notin B \lor x \notin C)) \lor (x \in B \land x \in C \land (x \notin A \lor x \notin C))) $$
    Nous appliquons la loi de distributivité de la conjonction sur la disjonction pour chaque terme principal.
    Pour le premier terme : $(x \in A \land x \in C \land (x \notin B \lor x \notin C))$
    $$ \iff ((x \in A \land x \in C \land x \notin B) \lor (x \in A \land x \in C \land x \notin C)) $$
    Le sous-terme $(x \in C \land x \notin C)$ est une contradiction, donc il est toujours faux. Par conséquent, $(x \in A \land x \in C \land x \notin C)$ est toujours faux.
    Ainsi, le premier terme se simplifie à :
    $$ (x \in A \land x \in C \land x \notin B) $$
    De même pour le second terme : $(x \in B \land x \in C \land (x \notin A \lor x \notin C))$
    $$ \iff ((x \in B \land x \in C \land x \notin A) \lor (x \in B \land x \in C \land x \notin C)) $$
    Le sous-terme $(x \in C \land x \notin C)$ est une contradiction, donc il est toujours faux. Par conséquent, $(x \in B \land x \in C \land x \notin C)$ est toujours faux.
    Ainsi, le second terme se simplifie à :
    $$ (x \in B \land x \in C \land x \notin A) $$
    En combinant les deux termes simplifiés, nous obtenons :
    $$ \iff ((x \in A \land x \in C \land x \notin B) \lor (x \in B \land x \in C \land x \notin A)) $$
    En réarrangeant les termes dans chaque conjonction (commutativité et associativité de $\land$) :
    $$ \iff ((x \in A \cap C \land x \notin B) \lor (x \in B \cap C \land x \notin A)) $$
    Cette dernière expression est identique à l'expression intermédiaire que nous avions obtenue en partant de l'ensemble de gauche.

    Puisque nous avons établi une chaîne d'équivalences logiques de l'appartenance à $(A \Delta B) \cap C$ à l'appartenance à $(A \cap C) \Delta (B \cap C)$, l'égalité des deux ensembles est démontrée.

*   **Conclusion :**
    Nous avons démontré, par une série d'équivalences logiques détaillées et justifiées à chaque étape, que pour tout élément $x$ de l'ensemble $E$, l'appartenance de $x$ à $(A \Delta B) \cap C$ est équivalente à son appartenance à $(A \cap C) \Delta (B \cap C)$. Cette démonstration rigoureuse confirme l'égalité ensembliste :
    $$ (A \Delta B) \cap C = (A \cap C) \Delta (B \cap C) $$
    Cette propriété illustre que l'opération d'intersection est distributive sur la différence symétrique, ce qui est une propriété fondamentale dans la structure d'anneau de Boole que forme l'ensemble des parties d'un ensemble avec ces deux opérations.
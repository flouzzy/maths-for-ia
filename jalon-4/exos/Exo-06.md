---
uuid: "jalon-4-exo-06"
title: "Exercice 06 - 3 étoiles"
---
# Exercice 06 : Distributivité de l'intersection sur la différence symétrique
**Difficulté :** ⭐⭐⭐

## Énoncé
Soient $E$ un ensemble non vide et $A$, $B$, $C$ trois parties quelconques de $E$.
Démontrer l'égalité suivante :
$$ (A \Delta B) \cap C = (A \cap C) \Delta (B \cap C) $$
où $\Delta$ désigne la différence symétrique, définie pour deux ensembles $X$ et $Y$ par $X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$.

## Correction Détaillée
*   **Analyse de l'énoncé :**
    Nous devons démontrer une égalité entre deux ensembles. Pour ce faire, nous allons utiliser la méthode de la chaîne d'équivalences logiques pour un élément $x$ quelconque de l'ensemble $E$. La stratégie consiste à partir de l'appartenance d'un élément $x$ au membre de gauche de l'égalité et de montrer, par des étapes logiques rigoureuses, que cela est équivalent à l'appartenance de $x$ au membre de droite. Nous utiliserons les définitions des opérations ensemblistes : intersection ($\cap$), union ($\cup$), différence ensembliste ($X \setminus Y = X \cap Y^c$), et différence symétrique ($X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$). Nous ferons également appel aux lois fondamentales de la logique propositionnelle, telles que la distributivité et les lois de De Morgan.

*   **Résolution pas-à-pas :**
    Soit $x$ un élément quelconque de l'ensemble $E$.

    Nous allons démontrer l'équivalence $x \in (A \Delta B) \cap C \iff x \in (A \cap C) \Delta (B \cap C)$.

    **Partie 1 : Développer le membre de gauche**
    Commençons par le membre de gauche, $(A \Delta B) \cap C$.
    Un élément $x$ appartient à cet ensemble si et seulement si :
    $$ x \in (A \Delta B) \cap C $$
    Par définition de l'intersection, cela signifie que :
    $$ (x \in A \Delta B) \quad \text{et} \quad (x \in C) $$
    Par définition de la différence symétrique $X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$, l'expression $(x \in A \Delta B)$ est équivalente à :
    $$ (x \in A \setminus B) \quad \text{ou} \quad (x \in B \setminus A) $$
    Par définition de la différence ensembliste $X \setminus Y = X \cap Y^c$, l'expression $(x \in A \setminus B)$ est équivalente à $(x \in A \quad \text{et} \quad x \notin B)$, et l'expression $(x \in B \setminus A)$ est équivalente à $(x \in B \quad \text{et} \quad x \notin A)$.
    Donc, $(x \in A \Delta B)$ est équivalent à :
    $$ (x \in A \quad \text{et} \quad x \notin B) \quad \text{ou} \quad (x \in B \quad \text{et} \quad x \notin A) $$
    En combinant avec $(x \in C)$, l'appartenance de $x$ au membre de gauche est équivalente à :
    $$ \left( (x \in A \quad \text{et} \quad x \notin B) \quad \text{ou} \quad (x \in B \quad \text{et} \quad x \notin A) \right) \quad \text{et} \quad (x \in C) $$
    Nous pouvons distribuer la conjonction $(x \in C)$ sur la disjonction, en utilisant la loi de distributivité de la logique propositionnelle ($ (P \lor Q) \land R \iff (P \land R) \lor (Q \land R) $):
    $$ \iff (x \in A \quad \text{et} \quad x \notin B \quad \text{et} \quad x \in C) \quad \text{ou} \quad (x \in B \quad \text{et} \quad x \notin A \quad \text{et} \quad x \in C) $$
    Par commutativité et associativité de la conjonction, nous pouvons réorganiser les termes :
    $$ \iff (x \in A \quad \text{et} \quad x \in C \quad \text{et} \quad x \notin B) \quad \text{ou} \quad (x \in B \quad \text{et} \quad x \in C \quad \text{et} \quad x \notin A) $$
    En utilisant la définition de l'intersection ($x \in X \cap Y \iff x \in X \land x \in Y$):
    $$ \iff (x \in A \cap C \quad \text{et} \quad x \notin B) \quad \text{ou} \quad (x \in B \cap C \quad \text{et} \quad x \notin A) \quad (\star) $$

    **Partie 2 : Développer le membre de droite**
    Maintenant, développons le membre de droite, $(A \cap C) \Delta (B \cap C)$.
    Un élément $x$ appartient à cet ensemble si et seulement si :
    $$ x \in (A \cap C) \Delta (B \cap C) $$
    Par définition de la différence symétrique :
    $$ \iff (x \in (A \cap C) \setminus (B \cap C)) \quad \text{ou} \quad (x \in (B \cap C) \setminus (A \cap C)) $$
    Par définition de la différence ensembliste :
    $$ \iff (x \in A \cap C \quad \text{et} \quad x \notin B \cap C) \quad \text{ou} \quad (x \in B \cap C \quad \text{et} \quad x \notin A \cap C) $$
    Par la loi de De Morgan pour le complémentaire de l'intersection ($ (X \cap Y)^c = X^c \cup Y^c $), l'expression $x \notin X \cap Y$ est équivalente à $x \notin X \quad \text{ou} \quad x \notin Y$:
    $$ \iff (x \in A \cap C \quad \text{et} \quad (x \notin B \quad \text{ou} \quad x \notin C)) \quad \text{ou} \quad (x \in B \cap C \quad \text{et} \quad (x \notin A \quad \text{ou} \quad x \notin C)) $$
    Par distributivité de la conjonction sur la disjonction ($ P \land (Q \lor R) \iff (P \land Q) \lor (P \land R) $):
    $$ \iff ((x \in A \cap C \quad \text{et} \quad x \notin B) \quad \text{ou} \quad (x \in A \cap C \quad \text{et} \quad x \notin C)) \quad \text{ou} \quad ((x \in B \cap C \quad \text{et} \quad x \notin A) \quad \text{ou} \quad (x \in B \cap C \quad \text{et} \quad x \notin C)) $$
    Analysons les termes contenant $x \notin C$:
    *   Le terme $(x \in A \cap C \quad \text{et} \quad x \notin C)$ signifie $(x \in A \quad \text{et} \quad x \in C \quad \text{et} \quad x \notin C)$. La proposition $(x \in C \quad \text{et} \quad x \notin C)$ est une contradiction, donc elle est toujours fausse. Par conséquent, le terme entier est faux.
    *   De même, le terme $(x \in B \cap C \quad \text{et} \quad x \notin C)$ signifie $(x \in B \quad \text{et} \quad x \in C \quad \text{et} \quad x \notin C)$. La proposition $(x \in C \quad \text{et} \quad x \notin C)$ est une contradiction, donc elle est toujours fausse. Par conséquent, le terme entier est faux.
    En remplaçant les termes contradictoires par "Faux" (ou $\bot$ en logique) :
    $$ \iff ((x \in A \cap C \quad \text{et} \quad x \notin B) \quad \text{ou} \quad \text{Faux}) \quad \text{ou} \quad ((x \in B \cap C \quad \text{et} \quad x \notin A) \quad \text{ou} \quad \text{Faux}) $$
    Puisque $(P \lor \text{Faux}) \iff P$:
    $$ \iff (x \in A \cap C \quad \text{et} \quad x \notin B) \quad \text{ou} \quad (x \in B \cap C \quad \text{et} \quad x \notin A) $$
    Cette dernière expression est identique à l'expression $(\star)$ obtenue pour le membre de gauche.

*   **Conclusion :**
    Nous avons démontré, par une chaîne d'équivalences logiques détaillées pour un élément $x$ quelconque de $E$, que l'appartenance à l'ensemble $(A \Delta B) \cap C$ est strictement équivalente à l'appartenance à l'ensemble $(A \cap C) \Delta (B \cap C)$. Chaque étape a été justifiée par les définitions précises des opérations ensemblistes (intersection, différence, différence symétrique) et les lois fondamentales de la logique propositionnelle (distributivité de la conjonction sur la disjonction, lois de De Morgan, et propriétés des contradictions). L'égalité $(A \Delta B) \cap C = (A \cap C) \Delta (B \cap C)$ est donc établie pour toutes parties $A, B, C$ d'un ensemble $E$.
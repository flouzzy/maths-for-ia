---
uuid: "jalon-4-exo-08"
title: "Exercice 08 - 4 étoiles"
---
# Exercice 08 : Distributivité de l'intersection sur la différence symétrique
**Difficulté :** ⭐⭐⭐⭐

## Énoncé
Soient $E$ un ensemble non vide, et $A$, $B$, $C$ trois parties quelconques de $E$.
Démontrer l'égalité suivante :
$$ (A \Delta B) \cap C = (A \cap C) \Delta (B \cap C) $$
où $\Delta$ désigne la différence symétrique et $\cap$ désigne l'intersection.

## Correction Détaillée
*   **Analyse de l'énoncé :**
    L'objectif est de démontrer l'égalité entre les deux ensembles $(A \Delta B) \cap C$ et $(A \cap C) \Delta (B \cap C)$. Pour ce faire, nous allons employer la méthode des fonctions indicatrices. Cette approche consiste à montrer que les fonctions indicatrices des deux ensembles sont identiques pour tout élément $x$ appartenant à l'ensemble universel $E$. L'égalité des fonctions indicatrices pour tout $x \in E$ est une condition nécessaire et suffisante pour l'égalité des ensembles correspondants.

*   **Résolution pas-à-pas :**
    Soient $A$, $B$, $C$ des parties de l'ensemble non vide $E$.
    Soit $x$ un élément quelconque et arbitraire de $E$.
    Nous rappelons la définition de la fonction indicatrice d'une partie $X$ de $E$, notée $\mathbf{1}_X(x)$, qui est une fonction de $E$ dans l'ensemble $\{0, 1\}$ définie comme suit :
    $$ \mathbf{1}_X(x) = \begin{cases} 1 & \text{si } x \in X \\ 0 & \text{si } x \notin X \end{cases} $$
    Pour toutes parties $X$ et $Y$ de $E$, les fonctions indicatrices vérifient les propriétés algébriques suivantes :
    1.  $\mathbf{1}_{X \cap Y}(x) = \mathbf{1}_X(x) \cdot \mathbf{1}_Y(x)$
    2.  $\mathbf{1}_{X \cup Y}(x) = \mathbf{1}_X(x) + \mathbf{1}_Y(x) - \mathbf{1}_X(x) \cdot \mathbf{1}_Y(x)$
    3.  $\mathbf{1}_{X^c}(x) = 1 - \mathbf{1}_X(x)$
    4.  $\mathbf{1}_{X \setminus Y}(x) = \mathbf{1}_X(x) \cdot (1 - \mathbf{1}_Y(x))$
    5.  $\mathbf{1}_{X \Delta Y}(x) = \mathbf{1}_X(x) + \mathbf{1}_Y(x) - 2 \cdot \mathbf{1}_X(x) \cdot \mathbf{1}_Y(x)$
        Démontrons la propriété 5 en utilisant la définition de la différence symétrique :
        Par définition, la différence symétrique $X \Delta Y$ est égale à $(X \setminus Y) \cup (Y \setminus X)$.
        Les ensembles $(X \setminus Y)$ et $(Y \setminus X)$ sont disjoints, c'est-à-dire $(X \setminus Y) \cap (Y \setminus X) = \emptyset$.
        Par conséquent, la fonction indicatrice de leur union est la somme de leurs fonctions indicatrices (propriété 2 simplifiée pour ensembles disjoints, ou directement par définition) :
        $$ \mathbf{1}_{X \Delta Y}(x) = \mathbf{1}_{(X \setminus Y) \cup (Y \setminus X)}(x) = \mathbf{1}_{X \setminus Y}(x) + \mathbf{1}_{Y \setminus X}(x) $$
        En appliquant la propriété 4 pour chaque terme :
        $$ \mathbf{1}_{X \Delta Y}(x) = \mathbf{1}_X(x) \cdot (1 - \mathbf{1}_Y(x)) + \mathbf{1}_Y(x) \cdot (1 - \mathbf{1}_X(x)) $$
        Développons cette expression :
        $$ \mathbf{1}_{X \Delta Y}(x) = \mathbf{1}_X(x) - \mathbf{1}_X(x)\mathbf{1}_Y(x) + \mathbf{1}_Y(x) - \mathbf{1}_Y(x)\mathbf{1}_X(x) $$
        Regroupons les termes similaires :
        $$ \mathbf{1}_{X \Delta Y}(x) = \mathbf{1}_X(x) + \mathbf{1}_Y(x) - 2\mathbf{1}_X(x)\mathbf{1}_Y(x) $$
        La propriété 5 est ainsi établie.

    Calculons la fonction indicatrice du membre de gauche de l'égalité à démontrer, soit $(A \Delta B) \cap C$ :
    En utilisant la propriété 1 pour l'intersection :
    $$ \mathbf{1}_{(A \Delta B) \cap C}(x) = \mathbf{1}_{A \Delta B}(x) \cdot \mathbf{1}_C(x) $$
    Substituons l'expression de $\mathbf{1}_{A \Delta B}(x)$ en utilisant la propriété 5 :
    $$ \mathbf{1}_{(A \Delta B) \cap C}(x) = (\mathbf{1}_A(x) + \mathbf{1}_B(x) - 2 \cdot \mathbf{1}_A(x) \cdot \mathbf{1}_B(x)) \cdot \mathbf{1}_C(x) $$
    Développons le produit :
    $$ \mathbf{1}_{(A \Delta B) \cap C}(x) = \mathbf{1}_A(x) \cdot \mathbf{1}_C(x) + \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) - 2 \cdot \mathbf{1}_A(x) \cdot \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) \quad (*) $$

    Calculons maintenant la fonction indicatrice du membre de droite de l'égalité, soit $(A \cap C) \Delta (B \cap C)$ :
    Nous allons d'abord déterminer les fonctions indicatrices des ensembles $(A \cap C)$ et $(B \cap C)$.
    En utilisant la propriété 1 pour l'intersection :
    $$ \mathbf{1}_{A \cap C}(x) = \mathbf{1}_A(x) \cdot \mathbf{1}_C(x) $$
    $$ \mathbf{1}_{B \cap C}(x) = \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) $$
    Appliquons ensuite la propriété 5 pour la différence symétrique $(A \cap C) \Delta (B \cap C)$ :
    $$ \mathbf{1}_{(A \cap C) \Delta (B \cap C)}(x) = \mathbf{1}_{A \cap C}(x) + \mathbf{1}_{B \cap C}(x) - 2 \cdot \mathbf{1}_{A \cap C}(x) \cdot \mathbf{1}_{B \cap C}(x) $$
    Substituons les expressions des fonctions indicatrices de $(A \cap C)$ et $(B \cap C)$ dans cette équation :
    $$ \mathbf{1}_{(A \cap C) \Delta (B \cap C)}(x) = (\mathbf{1}_A(x) \cdot \mathbf{1}_C(x)) + (\mathbf{1}_B(x) \cdot \mathbf{1}_C(x)) - 2 \cdot (\mathbf{1}_A(x) \cdot \mathbf{1}_C(x)) \cdot (\mathbf{1}_B(x) \cdot \mathbf{1}_C(x)) $$
    Simplifions le dernier terme du produit :
    $$ (\mathbf{1}_A(x) \cdot \mathbf{1}_C(x)) \cdot (\mathbf{1}_B(x) \cdot \mathbf{1}_C(x)) = \mathbf{1}_A(x) \cdot \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) \cdot \mathbf{1}_C(x) $$
    Étant donné que la fonction indicatrice $\mathbf{1}_C(x)$ ne peut prendre que les valeurs 0 ou 1, nous avons la propriété $\mathbf{1}_C(x) \cdot \mathbf{1}_C(x) = \mathbf{1}_C(x)$.
    Par conséquent, le produit se simplifie en :
    $$ (\mathbf{1}_A(x) \cdot \mathbf{1}_C(x)) \cdot (\mathbf{1}_B(x) \cdot \mathbf{1}_C(x)) = \mathbf{1}_A(x) \cdot \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) $$
    En substituant cette simplification dans l'expression de $\mathbf{1}_{(A \cap C) \Delta (B \cap C)}(x)$ :
    $$ \mathbf{1}_{(A \cap C) \Delta (B \cap C)}(x) = \mathbf{1}_A(x) \cdot \mathbf{1}_C(x) + \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) - 2 \cdot \mathbf{1}_A(x) \cdot \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) \quad (**) $$

    En comparant les expressions finales des fonctions indicatrices obtenues pour le membre de gauche $(*)$ et le membre de droite $(**)$, nous constatons qu'elles sont rigoureusement identiques pour tout $x \in E$ :
    $$ \mathbf{1}_{(A \Delta B) \cap C}(x) = \mathbf{1}_A(x) \cdot \mathbf{1}_C(x) + \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) - 2 \cdot \mathbf{1}_A(x) \cdot \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) $$
    $$ \mathbf{1}_{(A \cap C) \Delta (B \cap C)}(x) = \mathbf{1}_A(x) \cdot \mathbf{1}_C(x) + \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) - 2 \cdot \mathbf{1}_A(x) \cdot \mathbf{1}_B(x) \cdot \mathbf{1}_C(x) $$
    Puisque les fonctions indicatrices des deux ensembles sont égales pour tout élément $x \in E$, les ensembles eux-mêmes sont égaux.

*   **Conclusion :**
    Par l'application rigoureuse de la méthode des fonctions indicatrices et de leurs propriétés algébriques, nous avons démontré que pour toutes parties $A$, $B$, $C$ d'un ensemble non vide $E$, l'égalité $(A \Delta B) \cap C = (A \cap C) \Delta (B \cap C)$ est vérifiée. Cette propriété illustre une forme de distributivité de l'intersection sur la différence symétrique, similaire à la distributivité de l'intersection sur l'union ou de l'union sur l'intersection.
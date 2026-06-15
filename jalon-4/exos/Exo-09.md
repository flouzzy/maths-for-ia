---
uuid: "jalon-4-exo-09"
title: "Exercice 09 - 5 étoiles"
---
# Exercice 09 : Associativité de la différence symétrique
**Difficulté :** ⭐⭐⭐⭐⭐

## Énoncé
Soient $E$ un ensemble non vide et $A, B, C$ trois parties quelconques de $E$.
Démontrer que l'opération de différence symétrique $\Delta$ est associative, c'est-à-dire que l'égalité suivante est vérifiée :
$$ (A \Delta B) \Delta C = A \Delta (B \Delta C) $$

Rappel : Pour deux parties $X$ et $Y$ d'un ensemble $E$, la différence symétrique $X \Delta Y$ est définie par $X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$.

## Correction Détaillée
*   **Analyse de l'énoncé :**
    L'objectif de cet exercice est de démontrer l'associativité de l'opération de différence symétrique pour trois ensembles $A, B, C$ qui sont des parties d'un ensemble universel $E$. Pour prouver l'égalité de deux ensembles, $X = Y$, la méthode la plus rigoureuse et exhaustive consiste à montrer que leurs fonctions indicatrices (ou fonctions caractéristiques) sont égales pour tout élément de l'ensemble universel $E$. Cette approche permet d'éviter les omissions de cas et garantit une démonstration complète et sans ambiguïté.

    La stratégie de résolution sera la suivante :
    1.  Définir formellement la fonction indicatrice d'une partie d'un ensemble.
    2.  Établir une relation clé entre la fonction indicatrice de la différence symétrique de deux ensembles et les fonctions indicatrices de ces ensembles, en utilisant l'arithmétique modulo 2. Cette étape nécessite une justification exhaustive par cas.
    3.  Appliquer cette relation de manière séquentielle pour calculer la fonction indicatrice du membre de gauche de l'égalité à démontrer : $(A \Delta B) \Delta C$.
    4.  Appliquer la même relation de manière séquentielle pour calculer la fonction indicatrice du membre de droite de l'égalité à démontrer : $A \Delta (B \Delta C)$.
    5.  Utiliser la propriété d'associativité de l'addition modulo 2 pour simplifier les expressions obtenues.
    6.  Conclure que l'égalité des fonctions indicatrices pour tout élément de $E$ implique l'égalité des ensembles.

*   **Résolution pas-à-pas :**

    **Étape 1 : Définition de la fonction indicatrice**
    Soit $X$ une partie de l'ensemble $E$. La fonction indicatrice de $X$, notée $\mathbf{1}_X$, est une application de $E$ dans l'ensemble $\{0, 1\}$ définie pour tout $x \in E$ par :
    $$ \mathbf{1}_X(x) = \begin{cases} 1 & \text{si } x \in X \\ 0 & \text{si } x \notin X \end{cases} $$

    **Étape 2 : Relation entre la fonction indicatrice de la différence symétrique et l'addition modulo 2**
    Soient $X$ et $Y$ deux parties quelconques de $E$. Nous allons démontrer que pour tout $x \in E$, la fonction indicatrice de leur différence symétrique $\mathbf{1}_{X \Delta Y}(x)$ est égale à la somme de leurs fonctions indicatrices modulo 2, c'est-à-dire $\mathbf{1}_{X \Delta Y}(x) = (\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2$.
    La différence symétrique $X \Delta Y$ est définie par $X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$.
    Un élément $x \in E$ appartient à $X \Delta Y$ si et seulement si $x$ appartient à $X$ et n'appartient pas à $Y$, ou $x$ appartient à $Y$ et n'appartient pas à $X$. Nous allons examiner exhaustivement tous les quatre cas possibles pour la localisation de $x$ par rapport à $X$ et $Y$.

    *   **Cas 1 :** $x \in X$ et $x \in Y$.
        Dans ce cas, $x$ n'appartient ni à $X \setminus Y$ (car $x \in Y$) ni à $Y \setminus X$ (car $x \in X$). Par conséquent, $x \notin (X \setminus Y) \cup (Y \setminus X)$, ce qui signifie $x \notin X \Delta Y$.
        Les valeurs des fonctions indicatrices sont : $\mathbf{1}_X(x) = 1$, $\mathbf{1}_Y(x) = 1$, et $\mathbf{1}_{X \Delta Y}(x) = 0$.
        Vérifions la relation proposée : $(\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2 = (1 + 1) \pmod 2 = 2 \pmod 2 = 0$.
        L'égalité $\mathbf{1}_{X \Delta Y}(x) = (\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2$ est vérifiée dans ce cas (0 = 0).

    *   **Cas 2 :** $x \in X$ et $x \notin Y$.
        Dans ce cas, $x$ appartient à $X \setminus Y$ et n'appartient pas à $Y \setminus X$. Par conséquent, $x \in (X \setminus Y) \cup (Y \setminus X)$, ce qui signifie $x \in X \Delta Y$.
        Les valeurs des fonctions indicatrices sont : $\mathbf{1}_X(x) = 1$, $\mathbf{1}_Y(x) = 0$, et $\mathbf{1}_{X \Delta Y}(x) = 1$.
        Vérifions la relation proposée : $(\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2 = (1 + 0) \pmod 2 = 1 \pmod 2 = 1$.
        L'égalité $\mathbf{1}_{X \Delta Y}(x) = (\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2$ est vérifiée dans ce cas (1 = 1).

    *   **Cas 3 :** $x \notin X$ et $x \in Y$.
        Dans ce cas, $x$ n'appartient pas à $X \setminus Y$ et appartient à $Y \setminus X$. Par conséquent, $x \in (X \setminus Y) \cup (Y \setminus X)$, ce qui signifie $x \in X \Delta Y$.
        Les valeurs des fonctions indicatrices sont : $\mathbf{1}_X(x) = 0$, $\mathbf{1}_Y(x) = 1$, et $\mathbf{1}_{X \Delta Y}(x) = 1$.
        Vérifions la relation proposée : $(\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2 = (0 + 1) \pmod 2 = 1 \pmod 2 = 1$.
        L'égalité $\mathbf{1}_{X \Delta Y}(x) = (\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2$ est vérifiée dans ce cas (1 = 1).

    *   **Cas 4 :** $x \notin X$ et $x \notin Y$.
        Dans ce cas, $x$ n'appartient ni à $X \setminus Y$ ni à $Y \setminus X$. Par conséquent, $x \notin (X \setminus Y) \cup (Y \setminus X)$, ce qui signifie $x \notin X \Delta Y$.
        Les valeurs des fonctions indicatrices sont : $\mathbf{1}_X(x) = 0$, $\mathbf{1}_Y(x) = 0$, et $\mathbf{1}_{X \Delta Y}(x) = 0$.
        Vérifions la relation proposée : $(\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2 = (0 + 0) \pmod 2 = 0 \pmod 2 = 0$.
        L'égalité $\mathbf{1}_{X \Delta Y}(x) = (\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2$ est vérifiée dans ce cas (0 = 0).

    Puisque la relation est vérifiée dans tous les cas possibles, nous pouvons affirmer que pour toutes parties $X, Y$ de $E$, et pour tout $x \in E$, nous avons :
    $$ \mathbf{1}_{X \Delta Y}(x) = (\mathbf{1}_X(x) + \mathbf{1}_Y(x)) \pmod 2 $$

    **Étape 3 : Calcul de la fonction indicatrice du membre de gauche**
    Considérons le membre de gauche de l'égalité à démontrer : $(A \Delta B) \Delta C$.
    En appliquant la relation fondamentale établie à l'étape 2, en posant $X' = (A \Delta B)$ et $Y' = C$, nous obtenons pour tout $x \in E$ :
    $$ \mathbf{1}_{(A \Delta B) \Delta C}(x) = (\mathbf{1}_{A \Delta B}(x) + \mathbf{1}_C(x)) \pmod 2 $$
    Nous appliquons ensuite la même relation à $\mathbf{1}_{A \Delta B}(x)$, en posant $X'' = A$ et $Y'' = B$ :
    $$ \mathbf{1}_{A \Delta B}(x) = (\mathbf{1}_A(x) + \mathbf{1}_B(x)) \pmod 2 $$
    En substituant cette expression dans la première égalité, nous obtenons :
    $$ \mathbf{1}_{(A \Delta B) \Delta C}(x) = ((\mathbf{1}_A(x) + \mathbf{1}_B(x)) \pmod 2 + \mathbf{1}_C(x)) \pmod 2 $$
    Soient $a = \mathbf{1}_A(x)$, $b = \mathbf{1}_B(x)$, et $c = \mathbf{1}_C(x)$. Ces valeurs sont toutes des éléments de l'ensemble $\{0, 1\}$.
    L'addition modulo 2 est une opération associative. Cela signifie que pour tout $a, b, c \in \{0, 1\}$ :
    $( (a+b) \pmod 2 + c ) \pmod 2 = ( a + (b+c) \pmod 2 ) \pmod 2 = (a+b+c) \pmod 2$.
    En appliquant cette propriété d'associativité de l'addition modulo 2, nous pouvons simplifier l'expression :
    $$ \mathbf{1}_{(A \Delta B) \Delta C}(x) = (\mathbf{1}_A(x) + \mathbf{1}_B(x) + \mathbf{1}_C(x)) \pmod 2 $$
    Cette expression est valable pour tout $x \in E$.

    **Étape 4 : Calcul de la fonction indicatrice du membre de droite**
    Considérons le membre de droite de l'égalité à démontrer : $A \Delta (B \Delta C)$.
    En appliquant la relation fondamentale établie à l'étape 2, en posant $X' = A$ et $Y' = (B \Delta C)$, nous obtenons pour tout $x \in E$ :
    $$ \mathbf{1}_{A \Delta (B \Delta C)}(x) = (\mathbf{1}_A(x) + \mathbf{1}_{B \Delta C}(x)) \pmod 2 $$
    Nous appliquons ensuite la même relation à $\mathbf{1}_{B \Delta C}(x)$, en posant $X'' = B$ et $Y'' = C$ :
    $$ \mathbf{1}_{B \Delta C}(x) = (\mathbf{1}_B(x) + \mathbf{1}_C(x)) \pmod 2 $$
    En substituant cette expression dans la première égalité, nous obtenons :
    $$ \mathbf{1}_{A \Delta (B \Delta C)}(x) = (\mathbf{1}_A(x) + (\mathbf{1}_B(x) + \mathbf{1}_C(x)) \pmod 2) \pmod 2 $$
    En utilisant à nouveau l'associativité de l'addition modulo 2, comme justifié à l'étape 3 :
    $$ \mathbf{1}_{A \Delta (B \Delta C)}(x) = (\mathbf{1}_A(x) + \mathbf{1}_B(x) + \mathbf{1}_C(x)) \pmod 2 $$
    Cette expression est valable pour tout $x \in E$.

    **Étape 5 : Conclusion de l'égalité des ensembles**
    Nous avons démontré que pour tout élément $x \in E$ :
    $$ \mathbf{1}_{(A \Delta B) \Delta C}(x) = (\mathbf{1}_A(x) + \mathbf{1}_B(x) + \mathbf{1}_C(x)) \pmod 2 $$
    et
    $$ \mathbf{1}_{A \Delta (B \Delta C)}(x) = (\mathbf{1}_A(x) + \mathbf{1}_B(x) + \mathbf{1}_C(x)) \pmod 2 $$
    Puisque les fonctions indicatrices des deux ensembles $(A \Delta B) \Delta C$ et $A \Delta (B \Delta C)$ sont égales pour tout élément $x$ de l'ensemble universel $E$, cela implique, par définition de l'égalité des ensembles, que les deux ensembles sont identiques.
    $$ (A \Delta B) \Delta C = A \Delta (B \Delta C) $$

*   **Conclusion :**
    Nous avons rigoureusement démontré que l'opération de différence symétrique est associative pour toutes parties $A, B, C$ d'un ensemble $E$. La preuve a été menée de manière exhaustive en utilisant les fonctions indicatrices des ensembles et les propriétés de l'arithmétique modulo 2, garantissant qu'aucune étape de raisonnement n'a été omise. Cette propriété fondamentale est cruciale en théorie des ensembles et en algèbre, car elle établit que l'ensemble des parties de $E$, muni de la différence symétrique comme addition et de l'intersection comme multiplication, forme un anneau de Boole, noté $(\mathcal{P}(E), \Delta, \cap)$.
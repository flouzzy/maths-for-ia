# Exercice 2 : Notions fondamentales sur les ensembles finis
**Difficulté :** ⭐
**Thème :** Appartenance, inclusion, opérations sur les ensembles finis, ensemble des parties.

## Énoncé
Soient les ensembles finis $A$, $B$ et $C$ définis comme suit :
*   $A = \{1, 2, 3\}$
*   $B = \{3, 4\}$
*   $C = \{2, \{4\}\}$

1.  Pour chacune des assertions suivantes, indiquer si elle est vraie ou fausse. Justifier rigoureusement votre réponse.
    a.  $1 \in A$
    b.  $\{1\} \in A$
    c.  $A \subseteq \{1, 2, 3, 4\}$
    d.  $B \subseteq A$
    e.  $4 \in B$
    f.  $\{4\} \in C$
    g.  $4 \in C$

2.  Calculer explicitement les ensembles suivants :
    a.  $A \cup B$
    b.  $A \cap B$
    c.  $A \setminus B$
    d.  $B \setminus A$
    e.  $(A \cup B) \cap C$

3.  Déterminer l'ensemble des parties de $A$, noté $\mathcal{P}(A)$. Quel est le cardinal de $\mathcal{P}(A)$ ?

## Correction Détaillée

### Question 1 : Appartenance et inclusion

**Rappel des définitions :**
*   Un élément $x$ **appartient** à un ensemble $E$, noté $x \in E$, si $x$ est un des objets listés comme élément de $E$.
*   Un ensemble $S_1$ est un **sous-ensemble** (ou est **inclus**) dans un ensemble $S_2$, noté $S_1 \subseteq S_2$, si tout élément de $S_1$ est également un élément de $S_2$.

Les ensembles donnés sont :
*   $A = \{1, 2, 3\}$
*   $B = \{3, 4\}$
*   $C = \{2, \{4\}\}$

a.  **Assertion :** $1 \in A$
    *   **Nature des objets :** $1$ est un élément. $A$ est un ensemble.
    *   **Justification :** L'ensemble $A$ est défini par l'énumération de ses éléments : $A = \{1, 2, 3\}$. Par définition de l'appartenance, un élément appartient à un ensemble s'il est listé parmi ses éléments. L'élément $1$ est explicitement listé comme un élément de $A$.
    *   **Conclusion :** L'assertion $1 \in A$ est **vraie**.

b.  **Assertion :** $\{1\} \in A$
    *   **Nature des objets :** $\{1\}$ est un ensemble (un ensemble contenant l'élément $1$). $A$ est un ensemble.
    *   **Justification :** Pour que l'ensemble $\{1\}$ appartienne à l'ensemble $A$, il faudrait que $\{1\}$ soit un des éléments listés dans $A$. Les éléments de $A$ sont $1$, $2$, et $3$. L'ensemble $\{1\}$ n'est pas l'élément $1$, ni l'élément $2$, ni l'élément $3$.
    *   **Conclusion :** L'assertion $\{1\} \in A$ est **fausse**.

c.  **Assertion :** $A \subseteq \{1, 2, 3, 4\}$
    *   **Nature des objets :** $A$ est un ensemble. $\{1, 2, 3, 4\}$ est un ensemble.
    *   **Justification :** Pour qu'un ensemble $A$ soit un sous-ensemble d'un ensemble $S'$, il faut que tout élément de $A$ soit également un élément de $S'$. Nous vérifions cette condition pour $A$ et $S' = \{1, 2, 3, 4\}$.
        *   L'élément $1 \in A$. L'élément $1$ est également présent dans $S'$.
        *   L'élément $2 \in A$. L'élément $2$ est également présent dans $S'$.
        *   L'élément $3 \in A$. L'élément $3$ est également présent dans $S'$.
        Puisque tous les éléments de $A$ appartiennent à $\{1, 2, 3, 4\}$, la condition d'inclusion est satisfaite.
    *   **Conclusion :** L'assertion $A \subseteq \{1, 2, 3, 4\}$ est **vraie**.

d.  **Assertion :** $B \subseteq A$
    *   **Nature des objets :** $B$ est un ensemble. $A$ est un ensemble.
    *   **Justification :** Pour que $B$ soit un sous-ensemble de $A$, tout élément de $B$ doit appartenir à $A$. Les éléments de $B$ sont $3$ et $4$.
        *   L'élément $3 \in B$. L'élément $3$ est également présent dans $A$.
        *   L'élément $4 \in B$. Cependant, l'élément $4$ n'est pas listé parmi les éléments de $A$ (qui sont $1, 2, 3$).
        Puisqu'il existe un élément de $B$ (à savoir $4$) qui n'appartient pas à $A$, la condition d'inclusion n'est pas satisfaite.
    *   **Conclusion :** L'assertion $B \subseteq A$ est **fausse**.

e.  **Assertion :** $4 \in B$
    *   **Nature des objets :** $4$ est un élément. $B$ est un ensemble.
    *   **Justification :** L'ensemble $B$ est défini par $B = \{3, 4\}$. Par définition, l'élément $4$ est explicitement listé comme un élément de $B$.
    *   **Conclusion :** L'assertion $4 \in B$ est **vraie**.

f.  **Assertion :** $\{4\} \in C$
    *   **Nature des objets :** $\{4\}$ est un ensemble. $C$ est un ensemble.
    *   **Justification :** L'ensemble $C$ est défini par $C = \{2, \{4\}\}$. Pour que $\{4\}$ appartienne à $C$, il faudrait que $\{4\}$ soit un des objets listés comme élément de $C$. Un des éléments listés dans $C$ est précisément $\{4\}$.
    *   **Conclusion :** L'assertion $\{4\} \in C$ est **vraie**.

g.  **Assertion :** $4 \in C$
    *   **Nature des objets :** $4$ est un élément. $C$ est un ensemble.
    *   **Justification :** L'ensemble $C$ est défini par $C = \{2, \{4\}\}$. Les éléments de $C$ sont l'élément $2$ et l'ensemble $\{4\}$. L'élément $4$ n'est pas listé directement comme un élément de $C$. Il est un élément de l'ensemble $\{4\}$, qui lui-même est un élément de $C$, mais $4$ n'est pas un élément de $C$ en soi. C'est une distinction cruciale entre appartenance et inclusion, et entre un élément et un ensemble contenant cet élément.
    *   **Conclusion :** L'assertion $4 \in C$ est **fausse**.

### Question 2 : Calcul d'opérations sur les ensembles

**Rappel des définitions :**
Soient $S_1$ et $S_2$ des ensembles.
*   **Union ($S_1 \cup S_2$) :** L'ensemble de tous les éléments qui appartiennent à $S_1$ ou à $S_2$ (ou aux deux). Formellement, $S_1 \cup S_2 = \{x \mid x \in S_1 \text{ ou } x \in S_2\}$.
*   **Intersection ($S_1 \cap S_2$) :** L'ensemble de tous les éléments qui appartiennent à la fois à $S_1$ et à $S_2$. Formellement, $S_1 \cap S_2 = \{x \mid x \in S_1 \text{ et } x \in S_2\}$.
*   **Différence ($S_1 \setminus S_2$) :** L'ensemble de tous les éléments qui appartiennent à $S_1$ mais n'appartiennent pas à $S_2$. Formellement, $S_1 \setminus S_2 = \{x \mid x \in S_1 \text{ et } x \notin S_2\}$.

Les ensembles donnés sont :
*   $A = \{1, 2, 3\}$
*   $B = \{3, 4\}$
*   $C = \{2, \{4\}\}$

a.  **Calcul :** $A \cup B$
    *   **Nature des objets :** $A$ et $B$ sont des ensembles. $A \cup B$ est un ensemble.
    *   **Calcul détaillé :**
        Par définition, $A \cup B$ contient tous les éléments de $A$ et tous les éléments de $B$, en ne listant qu'une seule fois les éléments qui apparaissent dans les deux.
        Les éléments de $A$ sont : $1, 2, 3$.
        Les éléments de $B$ sont : $3, 4$.
        En combinant ces éléments sans répétition, nous obtenons : $\{1, 2, 3, 4\}$.
    *   **Résultat :** $A \cup B = \{1, 2, 3, 4\}$.

b.  **Calcul :** $A \cap B$
    *   **Nature des objets :** $A$ et $B$ sont des ensembles. $A \cap B$ est un ensemble.
    *   **Calcul détaillé :**
        Par définition, $A \cap B$ contient uniquement les éléments qui sont présents à la fois dans $A$ et dans $B$.
        Éléments de $A$ : $1, 2, 3$.
        Éléments de $B$ : $3, 4$.
        *   L'élément $1$ est dans $A$ mais pas dans $B$.
        *   L'élément $2$ est dans $A$ mais pas dans $B$.
        *   L'élément $3$ est dans $A$ et dans $B$.
        *   L'élément $4$ est dans $B$ mais pas dans $A$.
        Le seul élément commun est $3$.
    *   **Résultat :** $A \cap B = \{3\}$.

c.  **Calcul :** $A \setminus B$
    *   **Nature des objets :** $A$ et $B$ sont des ensembles. $A \setminus B$ est un ensemble.
    *   **Calcul détaillé :**
        Par définition, $A \setminus B$ contient les éléments qui sont dans $A$ mais pas dans $B$.
        Nous examinons chaque élément de $A$:
        *   L'élément $1 \in A$. Est-ce que $1 \in B$? Non, car $1 \notin \{3, 4\}$. Donc, $1$ est inclus dans $A \setminus B$.
        *   L'élément $2 \in A$. Est-ce que $2 \in B$? Non, car $2 \notin \{3, 4\}$. Donc, $2$ est inclus dans $A \setminus B$.
        *   L'élément $3 \in A$. Est-ce que $3 \in B$? Oui, car $3 \in \{3, 4\}$. Donc, $3$ n'est pas inclus dans $A \setminus B$.
    *   **Résultat :** $A \setminus B = \{1, 2\}$.

d.  **Calcul :** $B \setminus A$
    *   **Nature des objets :** $A$ et $B$ sont des ensembles. $B \setminus A$ est un ensemble.
    *   **Calcul détaillé :**
        Par définition, $B \setminus A$ contient les éléments qui sont dans $B$ mais pas dans $A$.
        Nous examinons chaque élément de $B$:
        *   L'élément $3 \in B$. Est-ce que $3 \in A$? Oui, car $3 \in \{1, 2, 3\}$. Donc, $3$ n'est pas inclus dans $B \setminus A$.
        *   L'élément $4 \in B$. Est-ce que $4 \in A$? Non, car $4 \notin \{1, 2, 3\}$. Donc, $4$ est inclus dans $B \setminus A$.
    *   **Résultat :** $B \setminus A = \{4\}$.

e.  **Calcul :** $(A \cup B) \cap C$
    *   **Nature des objets :** $A, B, C$ sont des ensembles. $(A \cup B) \cap C$ est un ensemble.
    *   **Calcul détaillé :**
        Pour calculer cette expression, nous devons d'abord déterminer l'ensemble $A \cup B$, puis son intersection avec $C$.
        D'après la question 2.a, nous avons déjà calculé $A \cup B$:
        $$A \cup B = \{1, 2, 3, 4\}$$
        Maintenant, nous calculons l'intersection de cet ensemble avec $C = \{2, \{4\}\}$.
        $$(A \cup B) \cap C = \{1, 2, 3, 4\} \cap \{2, \{4\}\}$$
        Par définition, l'intersection contient les éléments communs aux deux ensembles :
        *   L'élément $1 \in (A \cup B)$ mais $1 \notin C$.
        *   L'élément $2 \in (A \cup B)$ et $2 \in C$. Donc $2$ est dans l'intersection.
        *   L'élément $3 \in (A \cup B)$ mais $3 \notin C$.
        *   L'élément $4 \in (A \cup B)$. Est-ce que $4 \in C$? Non. Rappelons que les éléments de $C$ sont $2$ et l'ensemble $\{4\}$, pas l'élément $4$ lui-même.
        Le seul élément commun est $2$.
    *   **Résultat :** $(A \cup B) \cap C = \{2\}$.

### Question 3 : Ensemble des parties

**Rappel des définitions :**
*   L'**ensemble des parties** d'un ensemble $E$, noté $\mathcal{P}(E)$, est l'ensemble de tous les sous-ensembles de $E$. Cela inclut l'ensemble vide $\emptyset$ et l'ensemble $E$ lui-même.
*   Le **cardinal** d'un ensemble fini $E$, noté $|E|$, est le nombre d'éléments distincts qu'il contient.
*   Pour tout ensemble fini $E$, le cardinal de son ensemble des parties est donné par la formule $|\mathcal{P}(E)| = 2^{|E|}$.

L'ensemble donné est $A = \{1, 2, 3\}$.

a.  **Détermination de $\mathcal{P}(A)$ :**
    *   **Nature des objets :** $A$ est un ensemble. $\mathcal{P}(A)$ est un ensemble d'ensembles.
    *   **Calcul détaillé :**
        L'ensemble $A$ a trois éléments : $1, 2, 3$. Nous devons lister tous les sous-ensembles possibles de $A$.
        1.  **Sous-ensemble avec 0 élément :** L'ensemble vide.
            $\emptyset$
        2.  **Sous-ensembles avec 1 élément :** Chaque élément pris individuellement, encapsulé dans un ensemble.
            $\{1\}$
            $\{2\}$
            $\{3\}$
        3.  **Sous-ensembles avec 2 éléments :** Toutes les combinaisons de deux éléments.
            $\{1, 2\}$
            $\{1, 3\}$
            $\{2, 3\}$
        4.  **Sous-ensemble avec 3 éléments :** L'ensemble $A$ lui-même.
            $\{1, 2, 3\}$
    *   **Résultat :**
        $$\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$$

b.  **Cardinal de $\mathcal{P}(A)$ :**
    *   **Nature des objets :** $|\mathcal{P}(A)|$ est un nombre entier naturel.
    *   **Calcul détaillé :**
        L'ensemble $A = \{1, 2, 3\}$ est un ensemble fini.
        Le cardinal de $A$ est $|A| = 3$, car il contient trois éléments distincts.
        En utilisant la formule pour le cardinal de l'ensemble des parties d'un ensemble fini :
        $$|\mathcal{P}(A)| = 2^{|A|} = 2^3$$
        $$|\mathcal{P}(A)| = 8$$
        Nous pouvons vérifier ce résultat en comptant les sous-ensembles listés ci-dessus : il y en a bien 8.
    *   **Résultat :** Le cardinal de $\mathcal{P}(A)$ est $8$.

# Exercice 1 : Concepts fondamentaux d'ensembles, d'appartenance et d'inclusion
**Difficulté :** ⭐
**Thème :** Appartenance, inclusion, sous-ensembles, ensemble des parties, cardinalité d'ensembles finis.

## Énoncé
Soit un ensemble $E$ défini comme $E = \{1, 2, 3\}$.

1.  Spécifier les éléments de l'ensemble $E$.
2.  Déterminer tous les sous-ensembles de $E$.
3.  Définir l'ensemble des parties de $E$, noté $\mathcal{P}(E)$, en énumérant explicitement ses éléments.
4.  Calculer les cardinaux de $E$ et de $\mathcal{P}(E)$, c'est-à-dire $|E|$ et $|\mathcal{P}(E)|$.
5.  Pour chacun des objets suivants, indiquer s'il s'agit d'une assertion vraie ou fausse, en justifiant rigoureusement votre réponse :
    a.  $1 \in E$
    b.  $\{1\} \in E$
    c.  $\{1\} \subseteq E$
    d.  $1 \in \mathcal{P}(E)$
    e.  $\{1\} \in \mathcal{P}(E)$
    f.  $\emptyset \in E$
    g.  $\emptyset \subseteq E$
    h.  $\emptyset \in \mathcal{P}(E)$
    i.  $E \in \mathcal{P}(E)$
    j.  $E \subseteq \mathcal{P}(E)$

## Correction Détaillée

### 1. Spécification des éléments de l'ensemble $E$
**Définition :** Un ensemble est une collection d'objets distincts, appelés éléments.
L'ensemble $E$ est défini explicitement par énumération de ses éléments comme $E = \{1, 2, 3\}$.
Les éléments de $E$ sont donc les nombres entiers $1$, $2$, et $3$.
On peut formaliser cela par les assertions d'appartenance suivantes :
*   $1 \in E$ (Le nombre entier $1$ est un élément de l'ensemble $E$).
*   $2 \in E$ (Le nombre entier $2$ est un élément de l'ensemble $E$).
*   $3 \in E$ (Le nombre entier $3$ est un élément de l'ensemble $E$).

### 2. Détermination de tous les sous-ensembles de $E$
**Définition :** Un ensemble $A$ est un sous-ensemble de $E$, noté $A \subseteq E$, si et seulement si tout élément de $A$ est également un élément de $E$. Formellement, $\forall x, (x \in A \implies x \in E)$.

Les sous-ensembles de $E$ sont énumérés de la manière suivante, en classant par le nombre d'éléments qu'ils contiennent :
*   **Sous-ensembles à 0 élément :**
    *   L'ensemble vide : $\emptyset$ (L'ensemble vide est, par définition, un sous-ensemble de tout ensemble).
*   **Sous-ensembles à 1 élément (singletons) :**
    *   $\{1\}$ (L'unique élément $1$ de cet ensemble est dans $E$).
    *   $\{2\}$ (L'unique élément $2$ de cet ensemble est dans $E$).
    *   $\{3\}$ (L'unique élément $3$ de cet ensemble est dans $E$).
*   **Sous-ensembles à 2 éléments (paires) :**
    *   $\{1, 2\}$ (Les éléments $1$ et $2$ de cet ensemble sont tous deux dans $E$).
    *   $\{1, 3\}$ (Les éléments $1$ et $3$ de cet ensemble sont tous deux dans $E$).
    *   $\{2, 3\}$ (Les éléments $2$ et $3$ de cet ensemble sont tous deux dans $E$).
*   **Sous-ensembles à 3 éléments :**
    *   $\{1, 2, 3\}$ (Tous les éléments de cet ensemble sont dans $E$. C'est l'ensemble $E$ lui-même).

En résumé, les sous-ensembles de $E$ sont : $\emptyset$, $\{1\}$, $\{2\}$, $\{3\}$, $\{1, 2\}$, $\{1, 3\}$, $\{2, 3\}$, $\{1, 2, 3\}$.

### 3. Définition de l'ensemble des parties de $E$, $\mathcal{P}(E)$
**Définition :** L'ensemble des parties d'un ensemble $E$, noté $\mathcal{P}(E)$, est l'ensemble de tous les sous-ensembles de $E$. Formellement, $\mathcal{P}(E) = \{A \mid A \subseteq E\}$.

En utilisant la liste des sous-ensembles déterminée au point 2, les éléments de $\mathcal{P}(E)$ sont ces sous-ensembles. Ainsi, on a :
$$ \mathcal{P}(E) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\} $$

### 4. Calcul des cardinaux de $E$ et de $\mathcal{P}(E)$
**Définition :** Le cardinal d'un ensemble fini $X$, noté $|X|$, est le nombre d'éléments distincts contenus dans $X$.

*   **Cardinal de $E$ :** L'ensemble $E = \{1, 2, 3\}$ contient trois éléments distincts (les nombres entiers $1, 2, 3$).
    Donc, $|E| = 3$.

*   **Cardinal de $\mathcal{P}(E)$ :** L'ensemble $\mathcal{P}(E)$ est composé de tous les sous-ensembles de $E$. En comptant les éléments de $\mathcal{P}(E)$ que nous avons énumérés au point 3 :
    $\mathcal{P}(E) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$.
    Cet ensemble contient $8$ éléments distincts.
    Donc, $|\mathcal{P}(E)| = 8$.

    **Propriété générale :** Pour tout ensemble fini $E$, le cardinal de son ensemble des parties est donné par la formule $|\mathcal{P}(E)| = 2^{|E|}$.
    Dans notre cas, $|E| = 3$, donc $|\mathcal{P}(E)| = 2^{3} = 8$. Ce résultat est cohérent avec le dénombrement explicite des éléments de $\mathcal{P}(E)$.

### 5. Validation d'assertions d'appartenance et d'inclusion
Nous allons évaluer la véracité de chaque assertion en nous basant sur les définitions de l'appartenance ($\in$) et de l'inclusion ($\subseteq$).

**a. $1 \in E$**
*   **Nature des objets :** $1$ est un nombre entier (un objet, un élément potentiel). $E$ est un ensemble.
*   **Justification :** L'ensemble $E$ est défini comme $E = \{1, 2, 3\}$. Par cette définition, le nombre entier $1$ est explicitement listé comme un élément de $E$.
*   **Valeur de vérité :** Vraie.

**b. $\{1\} \in E$**
*   **Nature des objets :** $\{1\}$ est un ensemble (un singleton, c'est-à-dire un ensemble contenant le nombre entier $1$). $E$ est un ensemble.
*   **Justification :** Pour qu'un objet soit un élément de $E$, il doit être l'un des objets listés dans la définition de $E$. Les éléments de $E$ sont $1, 2, 3$. L'ensemble $\{1\}$ n'est ni le nombre $1$, ni le nombre $2$, ni le nombre $3$. L'objet $\{1\}$ est un ensemble, tandis que les éléments de $E$ sont des nombres.
*   **Valeur de vérité :** Fausse.

**c. $\{1\} \subseteq E$**
*   **Nature des objets :** $\{1\}$ est un ensemble. $E$ est un ensemble.
*   **Justification :** Un ensemble $A$ est un sous-ensemble de $E$ si et seulement si tout élément de $A$ est aussi un élément de $E$. L'ensemble $\{1\}$ a pour unique élément le nombre entier $1$. Nous avons établi en 5.a que $1 \in E$. Par conséquent, tout élément de $\{1\}$ (en l'occurrence, le seul élément $1$) est un élément de $E$.
*   **Valeur de vérité :** Vraie.

**d. $1 \in \mathcal{P}(E)$**
*   **Nature des objets :** $1$ est un nombre entier. $\mathcal{P}(E)$ est un ensemble dont les éléments sont eux-mêmes des ensembles (plus précisément, tous les sous-ensembles de $E$).
*   **Justification :** Les éléments de $\mathcal{P}(E)$ sont des ensembles. Le nombre entier $1$ n'est pas un ensemble (c'est un élément atomique, non un conteneur d'éléments dans ce contexte). Par conséquent, $1$ ne peut pas être un élément de $\mathcal{P}(E)$.
*   **Valeur de vérité :** Fausse.

**e. $\{1\} \in \mathcal{P}(E)$**
*   **Nature des objets :** $\{1\}$ est un ensemble. $\mathcal{P}(E)$ est un ensemble dont les éléments sont des ensembles.
*   **Justification :** Par définition, $\mathcal{P}(E)$ contient précisément tous les sous-ensembles de $E$. Nous avons établi en 5.c que l'ensemble $\{1\}$ est un sous-ensemble de $E$ (i.e., $\{1\} \subseteq E$). Par conséquent, $\{1\}$ est un élément de $\mathcal{P}(E)$.
*   **Valeur de vérité :** Vraie.

**f. $\emptyset \in E$**
*   **Nature des objets :** $\emptyset$ est un ensemble (l'ensemble vide). $E$ est un ensemble.
*   **Justification :** Pour que l'ensemble vide soit un élément de $E$, il faudrait qu'il soit listé explicitement comme un des éléments de $E$. Les éléments de $E$ sont $1, 2, 3$. L'ensemble vide n'est pas l'un de ces nombres. Dans la théorie des ensembles (ZFC), l'ensemble vide est généralement un ensemble et non un élément "atomique" comme $1$ ou $2$ à moins qu'il ne soit spécifiquement inclus.
*   **Valeur de vérité :** Fausse.

**g. $\emptyset \subseteq E$**
*   **Nature des objets :** $\emptyset$ est un ensemble. $E$ est un ensemble.
*   **Justification :** L'ensemble vide est, par définition fondamentale en théorie des ensembles (et par l'axiome de l'ensemble vide conjugué à l'axiome d'extensionnalité), un sous-ensemble de tout ensemble. La condition $\forall x, (x \in \emptyset \implies x \in E)$ est toujours vraie, car la prémisse $x \in \emptyset$ est toujours fausse (l'ensemble vide n'a aucun élément). Une implication avec une prémisse fausse est toujours vraie.
*   **Valeur de vérité :** Vraie.

**h. $\emptyset \in \mathcal{P}(E)$**
*   **Nature des objets :** $\emptyset$ est un ensemble. $\mathcal{P}(E)$ est un ensemble d'ensembles.
*   **Justification :** Par définition, $\mathcal{P}(E)$ contient tous les sous-ensembles de $E$. Nous avons établi en 5.g que $\emptyset$ est un sous-ensemble de $E$ (i.e., $\emptyset \subseteq E$). Par conséquent, l'ensemble vide est un élément de $\mathcal{P}(E)$.
*   **Valeur de vérité :** Vraie.

**i. $E \in \mathcal{P}(E)$**
*   **Nature des objets :** $E$ est un ensemble. $\mathcal{P}(E)$ est un ensemble d'ensembles.
*   **Justification :** Par définition, $\mathcal{P}(E)$ contient tous les sous-ensembles de $E$. L'ensemble $E$ est toujours un sous-ensemble de lui-même (i.e., $E \subseteq E$). Par conséquent, $E$ est un élément de $\mathcal{P}(E)$.
*   **Valeur de vérité :** Vraie.

**j. $E \subseteq \mathcal{P}(E)$**
*   **Nature des objets :** $E$ est un ensemble. $\mathcal{P}(E)$ est un ensemble d'ensembles.
*   **Justification :** Pour que $E \subseteq \mathcal{P}(E)$ soit vraie, il faudrait que chaque élément de $E$ soit également un élément de $\mathcal{P}(E)$. Les éléments de $E$ sont $1, 2, 3$. Les éléments de $\mathcal{P}(E)$ sont des ensembles (sous-ensembles de $E$).
    Considérons l'élément $1 \in E$. Pour que $E \subseteq \mathcal{P}(E)$ soit vraie, il faudrait que $1 \in \mathcal{P}(E)$. Or, nous avons montré en 5.d que l'assertion $1 \in \mathcal{P}(E)$ est fausse, car $1$ est un nombre et non un ensemble.
    Puisqu'il existe au moins un élément de $E$ (à savoir $1$) qui n'est pas un élément de $\mathcal{P}(E)$, l'assertion $E \subseteq \mathcal{P}(E)$ est fausse.
*   **Valeur de vérité :** Fausse.

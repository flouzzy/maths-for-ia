# Exercice 4 : Opérations Élémentaires sur les Ensembles et l'Ensemble des Parties
**Difficulté :** ⭐⭐
**Thème :** Appartenance, inclusion, opérations ensemblistes (union, intersection, différence, complémentaire), ensemble des parties, cardinaux finis.

## Énoncé

Dans cet exercice, nous allons manipuler des ensembles finis et démontrer une identité fondamentale.

### Partie 1 : Opérations ensemblistes
Soit $E = \{1, 2, 3, 4, 5, 6, 7, 8\}$ un ensemble de référence, que l'on appellera l'ensemble universel pour cette partie de l'exercice.
Soient $A = \{1, 2, 3, 4\}$ et $B = \{3, 4, 5, 6\}$ deux sous-ensembles de $E$.

Déterminer explicitement les ensembles suivants :
a) $A \cup B$
b) $A \cap B$
c) $A \setminus B$
d) $B \setminus A$
e) $A^c$ (le complémentaire de $A$ dans $E$)
f) $(A \cup B)^c$

### Partie 2 : Ensemble des Parties
Soit $S = \{a, b, c\}$ un ensemble dont les éléments sont $a$, $b$ et $c$.

a) Déterminer explicitement l'ensemble $\mathcal{P}(S)$ (l'ensemble des parties de $S$).
b) Préciser le cardinal de $\mathcal{P}(S)$.

### Partie 3 : Preuve d'égalité ensembliste
Soient $X$ et $Y$ deux ensembles quelconques.
Démontrer l'égalité suivante : $X = (X \cap Y) \cup (X \setminus Y)$.

## Correction Détaillée

### Partie 1 : Opérations ensemblistes

Nous avons les ensembles donnés :
$E = \{1, 2, 3, 4, 5, 6, 7, 8\}$ (l'ensemble universel)
$A = \{1, 2, 3, 4\}$
$B = \{3, 4, 5, 6\}$

a) **Calcul de $A \cup B$**
Par définition, $A \cup B$ est l'ensemble de tous les éléments qui appartiennent à $A$ ou qui appartiennent à $B$ (ou aux deux).
Un élément $x$ appartient à $A \cup B$ si et seulement si $x \in A$ ou $x \in B$.
Les éléments de $A$ sont $1, 2, 3, 4$.
Les éléments de $B$ sont $3, 4, 5, 6$.
En combinant ces éléments sans répétition, nous obtenons :
$A \cup B = \{1, 2, 3, 4, 5, 6\}$.

b) **Calcul de $A \cap B$**
Par définition, $A \cap B$ est l'ensemble de tous les éléments qui appartiennent à $A$ et qui appartiennent à $B$.
Un élément $x$ appartient à $A \cap B$ si et seulement si $x \in A$ et $x \in B$.
Les éléments communs à $A$ et $B$ sont $3$ et $4$.
$A \cap B = \{3, 4\}$.

c) **Calcul de $A \setminus B$**
Par définition, $A \setminus B$ (ou $A - B$) est l'ensemble de tous les éléments qui appartiennent à $A$ mais n'appartiennent pas à $B$.
Un élément $x$ appartient à $A \setminus B$ si et seulement si $x \in A$ et $x \notin B$.
Les éléments de $A$ sont $1, 2, 3, 4$.
Les éléments de $B$ sont $3, 4, 5, 6$.
Les éléments de $A$ qui ne sont pas dans $B$ sont $1$ et $2$.
$A \setminus B = \{1, 2\}$.

d) **Calcul de $B \setminus A$**
Par définition, $B \setminus A$ est l'ensemble de tous les éléments qui appartiennent à $B$ mais n'appartiennent pas à $A$.
Un élément $x$ appartient à $B \setminus A$ si et seulement si $x \in B$ et $x \notin A$.
Les éléments de $B$ sont $3, 4, 5, 6$.
Les éléments de $A$ sont $1, 2, 3, 4$.
Les éléments de $B$ qui ne sont pas dans $A$ sont $5$ et $6$.
$B \setminus A = \{5, 6\}$.

e) **Calcul de $A^c$ (le complémentaire de $A$ dans $E$)**
Par définition, le complémentaire de $A$ dans $E$, noté $A^c$, est l'ensemble de tous les éléments de $E$ qui n'appartiennent pas à $A$.
Un élément $x$ appartient à $A^c$ si et seulement si $x \in E$ et $x \notin A$.
Les éléments de $E$ sont $1, 2, 3, 4, 5, 6, 7, 8$.
Les éléments de $A$ sont $1, 2, 3, 4$.
Les éléments de $E$ qui ne sont pas dans $A$ sont $5, 6, 7, 8$.
$A^c = \{5, 6, 7, 8\}$.

f) **Calcul de $(A \cup B)^c$**
Nous avons déjà calculé $A \cup B = \{1, 2, 3, 4, 5, 6\}$.
Par définition, $(A \cup B)^c$ est l'ensemble de tous les éléments de $E$ qui n'appartiennent pas à $A \cup B$.
Un élément $x$ appartient à $(A \cup B)^c$ si et seulement si $x \in E$ et $x \notin (A \cup B)$.
Les éléments de $E$ sont $1, 2, 3, 4, 5, 6, 7, 8$.
Les éléments de $A \cup B$ sont $1, 2, 3, 4, 5, 6$.
Les éléments de $E$ qui ne sont pas dans $A \cup B$ sont $7$ et $8$.
$(A \cup B)^c = \{7, 8\}$.

### Partie 2 : Ensemble des Parties

Soit $S = \{a, b, c\}$ un ensemble.

a) **Détermination de $\mathcal{P}(S)$**
L'ensemble $\mathcal{P}(S)$ est l'ensemble de tous les sous-ensembles de $S$, y compris l'ensemble vide $\emptyset$ et l'ensemble $S$ lui-même.
Les sous-ensembles de $S$ sont :
*   L'ensemble vide : $\emptyset$
*   Les sous-ensembles à un élément : $\{a\}$, $\{b\}$, $\{c\}$
*   Les sous-ensembles à deux éléments : $\{a, b\}$, $\{a, c\}$, $\{b, c\}$
*   Le sous-ensemble à trois éléments (qui est $S$ lui-même) : $\{a, b, c\}$

En rassemblant tous ces sous-ensembles, nous obtenons :
$\mathcal{P}(S) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}\}$.

b) **Cardinal de $\mathcal{P}(S)$**
Le cardinal d'un ensemble fini $S$, noté $|S|$, est le nombre d'éléments qu'il contient. Ici, $|S| = 3$.
Le cardinal de l'ensemble des parties d'un ensemble fini $S$ est $2^{|S|}$.
Dans notre cas, $|S| = 3$.
Donc, $|\mathcal{P}(S)| = 2^3 = 8$.
Nous confirmons ce résultat en comptant les éléments listés à la question précédente : il y a bien 8 sous-ensembles.

### Partie 3 : Preuve d'égalité ensembliste

Nous devons démontrer l'égalité $X = (X \cap Y) \cup (X \setminus Y)$ pour deux ensembles quelconques $X$ et $Y$.
Pour prouver une égalité entre ensembles, nous devons montrer une double inclusion :
1.  $X \subseteq (X \cap Y) \cup (X \setminus Y)$
2.  $(X \cap Y) \cup (X \setminus Y) \subseteq X$

**Démonstration de $X \subseteq (X \cap Y) \cup (X \setminus Y)$ :**
Soit $x$ un élément arbitraire de $X$.
Par la loi du tiers exclu, un élément $x$ appartient à $Y$ ou n'appartient pas à $Y$. Nous avons donc deux cas possibles :
*   **Cas 1 :** $x \in Y$.
    Puisque $x \in X$ (par hypothèse) et $x \in Y$, il s'ensuit que $x \in X \cap Y$ (par définition de l'intersection).
    Si $x \in X \cap Y$, alors $x$ appartient nécessairement à l'union $(X \cap Y) \cup (X \setminus Y)$ (par définition de l'union).
*   **Cas 2 :** $x \notin Y$.
    Puisque $x \in X$ (par hypothèse) et $x \notin Y$, il s'ensuit que $x \in X \setminus Y$ (par définition de la différence ensembliste).
    Si $x \in X \setminus Y$, alors $x$ appartient nécessairement à l'union $(X \cap Y) \cup (X \setminus Y)$ (par définition de l'union).

Dans les deux cas possibles (exhaustivement, car tout $x$ est soit dans $Y$ soit hors de $Y$), nous avons montré que si $x \in X$, alors $x \in (X \cap Y) \cup (X \setminus Y)$.
Par conséquent, $X \subseteq (X \cap Y) \cup (X \setminus Y)$.

**Démonstration de $(X \cap Y) \cup (X \setminus Y) \subseteq X$ :**
Soit $x$ un élément arbitraire de $(X \cap Y) \cup (X \setminus Y)$.
Par définition de l'union, cela signifie que $x \in X \cap Y$ ou $x \in X \setminus Y$. Nous avons deux cas possibles :
*   **Cas 1 :** $x \in X \cap Y$.
    Par définition de l'intersection, cela signifie que $x \in X$ et $x \in Y$.
    En particulier, $x \in X$.
*   **Cas 2 :** $x \in X \setminus Y$.
    Par définition de la différence ensembliste, cela signifie que $x \in X$ et $x \notin Y$.
    En particulier, $x \in X$.

Dans les deux cas possibles, nous avons montré que si $x \in (X \cap Y) \cup (X \setminus Y)$, alors $x \in X$.
Par conséquent, $(X \cap Y) \cup (X \setminus Y) \subseteq X$.

**Conclusion :**
Puisque nous avons démontré les deux inclusions $X \subseteq (X \cap Y) \cup (X \setminus Y)$ et $(X \cap Y) \cup (X \setminus Y) \subseteq X$, nous pouvons conclure que les deux ensembles sont égaux.
$X = (X \cap Y) \cup (X \setminus Y)$.
Cette identité exprime que tout élément de $X$ est soit dans $Y$ (et donc dans l'intersection $X \cap Y$), soit n'est pas dans $Y$ (et donc dans la différence $X \setminus Y$). Les deux parties $(X \cap Y)$ et $(X \setminus Y)$ sont disjointes et leur union reconstitue $X$.
# Exercice 5 : Propriétés de l'Ensemble des Parties face aux Opérations d'Ensembles
**Difficulté :** ⭐⭐⭐
**Thème :** Ensemble des parties, opérations sur les ensembles (intersection, union), inclusion et égalité d'ensembles.

## Énoncé
Soient $A$ et $B$ deux ensembles quelconques. Nous n'imposons aucune restriction de finitude à ces ensembles.

1.  Démontrer que l'ensemble des parties de l'intersection de $A$ et $B$ est égal à l'intersection de l'ensemble des parties de $A$ et de l'ensemble des parties de $B$. Formellement, prouver que $\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$.
2.  Démontrer que l'union de l'ensemble des parties de $A$ et de l'ensemble des parties de $B$ est un sous-ensemble de l'ensemble des parties de l'union de $A$ et $B$. Formellement, prouver que $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$.
3.  L'égalité $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$ est-elle toujours vraie pour des ensembles $A$ et $B$ quelconques ? Justifier votre réponse de manière rigoureuse par une preuve ou par un contre-exemple explicite.

## Correction Détaillée

### Question 1 : Démontrer $\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$

Pour démontrer l'égalité entre deux ensembles, il est nécessaire et suffisant de démontrer la double inclusion. Soient $A$ et $B$ des ensembles.

#### Preuve de l'inclusion $\mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B)$

Soit $X$ un ensemble arbitraire.
1.  Supposons que $X$ est un élément de $\mathcal{P}(A \cap B)$.
2.  Par définition de l'ensemble des parties, cela signifie que $X$ est un sous-ensemble de $A \cap B$. Nous écrivons $X \subseteq A \cap B$.
3.  Par définition de l'intersection d'ensembles, si un ensemble $X$ est un sous-ensemble de $A \cap B$, alors tout élément de $X$ est un élément de $A \cap B$. Ceci implique que tout élément de $X$ est un élément de $A$, et tout élément de $X$ est un élément de $B$.
4.  La condition "tout élément de $X$ est un élément de $A$" signifie que $X$ est un sous-ensemble de $A$. Nous écrivons $X \subseteq A$.
5.  La condition "tout élément de $X$ est un élément de $B$" signifie que $X$ est un sous-ensemble de $B$. Nous écrivons $X \subseteq B$.
6.  Par définition de l'ensemble des parties, si $X \subseteq A$, alors $X$ est un élément de $\mathcal{P}(A)$. Nous écrivons $X \in \mathcal{P}(A)$.
7.  Par définition de l'ensemble des parties, si $X \subseteq B$, alors $X$ est un élément de $\mathcal{P}(B)$. Nous écrivons $X \in \mathcal{P}(B)$.
8.  Puisque $X \in \mathcal{P}(A)$ et $X \in \mathcal{P}(B)$, par définition de l'intersection d'ensembles, $X$ est un élément de $\mathcal{P}(A) \cap \mathcal{P}(B)$. Nous écrivons $X \in \mathcal{P}(A) \cap \mathcal{P}(B)$.
9.  Ayant montré que tout élément $X$ de $\mathcal{P}(A \cap B)$ est aussi un élément de $\mathcal{P}(A) \cap \mathcal{P}(B)$, nous avons démontré l'inclusion $\mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B)$.

#### Preuve de l'inclusion $\mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B)$

Soit $Y$ un ensemble arbitraire.
1.  Supposons que $Y$ est un élément de $\mathcal{P}(A) \cap \mathcal{P}(B)$.
2.  Par définition de l'intersection d'ensembles, cela signifie que $Y$ est un élément de $\mathcal{P}(A)$ et $Y$ est un élément de $\mathcal{P}(B)$. Nous écrivons $Y \in \mathcal{P}(A)$ et $Y \in \mathcal{P}(B)$.
3.  Par définition de l'ensemble des parties, si $Y \in \mathcal{P}(A)$, alors $Y$ est un sous-ensemble de $A$. Nous écrivons $Y \subseteq A$.
4.  Par définition de l'ensemble des parties, si $Y \in \mathcal{P}(B)$, alors $Y$ est un sous-ensemble de $B$. Nous écrivons $Y \subseteq B$.
5.  Par définition de l'intersection d'ensembles, si un ensemble $Y$ est un sous-ensemble de $A$ et un sous-ensemble de $B$, alors tout élément de $Y$ est à la fois un élément de $A$ et un élément de $B$. Cela signifie que tout élément de $Y$ est un élément de $A \cap B$. Donc, $Y$ est un sous-ensemble de $A \cap B$. Nous écrivons $Y \subseteq A \cap B$.
6.  Par définition de l'ensemble des parties, si $Y \subseteq A \cap B$, alors $Y$ est un élément de $\mathcal{P}(A \cap B)$. Nous écrivons $Y \in \mathcal{P}(A \cap B)$.
7.  Ayant montré que tout élément $Y$ de $\mathcal{P}(A) \cap \mathcal{P}(B)$ est aussi un élément de $\mathcal{P}(A \cap B)$, nous avons démontré l'inclusion $\mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B)$.

#### Conclusion de la Question 1

Puisque nous avons démontré les deux inclusions $\mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B)$ et $\mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B)$, nous pouvons conclure que les deux ensembles sont égaux :
$$ \mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B) $$

### Question 2 : Démontrer $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$

Soient $A$ et $B$ des ensembles.
1.  Soit $X$ un ensemble arbitraire. Supposons que $X$ est un élément de $\mathcal{P}(A) \cup \mathcal{P}(B)$.
2.  Par définition de l'union d'ensembles, cela signifie que $X$ est un élément de $\mathcal{P}(A)$ ou $X$ est un élément de $\mathcal{P}(B)$. Nous examinons ces deux cas séparément.

    *   **Cas 1 :** $X \in \mathcal{P}(A)$.
        *   Par définition de l'ensemble des parties, cela signifie que $X$ est un sous-ensemble de $A$. Nous écrivons $X \subseteq A$.
        *   Par définition de l'union d'ensembles, tout élément de $A$ est aussi un élément de $A \cup B$. Ceci signifie que $A$ est un sous-ensemble de $A \cup B$. Nous écrivons $A \subseteq A \cup B$.
        *   Puisque $X \subseteq A$ et $A \subseteq A \cup B$, par la propriété de transitivité de l'inclusion, nous avons $X \subseteq A \cup B$.
        *   Par définition de l'ensemble des parties, si $X \subseteq A \cup B$, alors $X$ est un élément de $\mathcal{P}(A \cup B)$. Nous écrivons $X \in \mathcal{P}(A \cup B)$.

    *   **Cas 2 :** $X \in \mathcal{P}(B)$.
        *   Par définition de l'ensemble des parties, cela signifie que $X$ est un sous-ensemble de $B$. Nous écrivons $X \subseteq B$.
        *   Par définition de l'union d'ensembles, tout élément de $B$ est aussi un élément de $A \cup B$. Ceci signifie que $B$ est un sous-ensemble de $A \cup B$. Nous écrivons $B \subseteq A \cup B$.
        *   Puisque $X \subseteq B$ et $B \subseteq A \cup B$, par la propriété de transitivité de l'inclusion, nous avons $X \subseteq A \cup B$.
        *   Par définition de l'ensemble des parties, si $X \subseteq A \cup B$, alors $X$ est un élément de $\mathcal{P}(A \cup B)$. Nous écrivons $X \in \mathcal{P}(A \cup B)$.

3.  Dans les deux cas possibles, nous avons montré que $X \in \mathcal{P}(A \cup B)$.
4.  Ayant montré que tout élément $X$ de $\mathcal{P}(A) \cup \mathcal{P}(B)$ est aussi un élément de $\mathcal{P}(A \cup B)$, nous avons démontré l'inclusion :
    $$ \mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B) $$

### Question 3 : L'égalité $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$ est-elle toujours vraie ?

Non, l'égalité $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$ n'est pas toujours vraie pour des ensembles $A$ et $B$ quelconques. Nous allons le prouver par un contre-exemple.

#### Contre-exemple

1.  Soit l'ensemble $A = \{1\}$. Cet ensemble est un ensemble fini contenant un seul élément.
2.  Soit l'ensemble $B = \{2\}$. Cet ensemble est un ensemble fini contenant un seul élément, distinct de celui de $A$.
3.  Calculons l'union de ces deux ensembles :
    *   $A \cup B = \{1\} \cup \{2\} = \{1, 2\}$. Cet ensemble est un ensemble fini.

4.  Calculons l'ensemble des parties de $A \cup B$:
    *   $\mathcal{P}(A \cup B) = \mathcal{P}(\{1, 2\})$.
    *   Les sous-ensembles de $\{1, 2\}$ sont : l'ensemble vide ($\emptyset$), l'ensemble $\{1\}$, l'ensemble $\{2\}$, et l'ensemble $\{1, 2\}$ lui-même.
    *   Ainsi, $\mathcal{P}(A \cup B) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$. Cet ensemble est un ensemble de sous-ensembles.

5.  Calculons $\mathcal{P}(A)$ :
    *   $\mathcal{P}(A) = \mathcal{P}(\{1\})$.
    *   Les sous-ensembles de $\{1\}$ sont : l'ensemble vide ($\emptyset$) et l'ensemble $\{1\}$.
    *   Ainsi, $\mathcal{P}(A) = \{\emptyset, \{1\}\}$. Cet ensemble est un ensemble de sous-ensembles.

6.  Calculons $\mathcal{P}(B)$ :
    *   $\mathcal{P}(B) = \mathcal{P}(\{2\})$.
    *   Les sous-ensembles de $\{2\}$ sont : l'ensemble vide ($\emptyset$) et l'ensemble $\{2\}$.
    *   Ainsi, $\mathcal{P}(B) = \{\emptyset, \{2\}\}$. Cet ensemble est un ensemble de sous-ensembles.

7.  Calculons l'union de $\mathcal{P}(A)$ et $\mathcal{P}(B)$:
    *   $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}\} \cup \{\emptyset, \{2\}\}$.
    *   Par définition de l'union, nous combinons tous les éléments uniques de chaque ensemble :
    *   $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}\}$. Cet ensemble est un ensemble de sous-ensembles.

8.  Comparaison :
    *   Nous avons $\mathcal{P}(A \cup B) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.
    *   Nous avons $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}\}$.
    *   Nous observons que l'ensemble $\{1, 2\}$ est un élément de $\mathcal{P}(A \cup B)$.
    *   Cependant, l'ensemble $\{1, 2\}$ n'est pas un élément de $\mathcal{P}(A) \cup \mathcal{P}(B)$. En effet :
        *   $\{1, 2\} \notin \mathcal{P}(A)$ car $\{1, 2\} \not\subseteq A$ (l'élément $2$ n'est pas dans $A$).
        *   $\{1, 2\} \notin \mathcal{P}(B)$ car $\{1, 2\} \not\subseteq B$ (l'élément $1$ n'est pas dans $B$).
        *   Puisque $\{1, 2\}$ n'appartient ni à $\mathcal{P}(A)$ ni à $\mathcal{P}(B)$, il n'appartient pas à leur union $\mathcal{P}(A) \cup \mathcal{P}(B)$.

#### Conclusion de la Question 3

Puisqu'il existe au moins un ensemble $X$ (en l'occurrence $X = \{1, 2\}$) tel que $X \in \mathcal{P}(A \cup B)$ mais $X \notin \mathcal{P}(A) \cup \mathcal{P}(B)$, nous concluons que l'ensemble $\mathcal{P}(A \cup B)$ n'est pas inclus dans $\mathcal{P}(A) \cup \mathcal{P}(B)$. Par conséquent, l'égalité ne tient pas :
$$ \mathcal{P}(A \cup B) \neq \mathcal{P}(A) \cup \mathcal{P}(B) $$
L'égalité n'est donc pas toujours vraie.

# Exercice 6 : Propriétés du Foncteur Ensembles des Parties : Union et Inclusion
**Difficulté :** ⭐⭐⭐
**Thème :** Ensemble des parties, union d'ensembles, inclusion d'ensembles, preuve par contre-exemple.

## Énoncé
Soient $A$ et $B$ deux ensembles quelconques.

1.  Démontrer l'inclusion suivante : $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$.
2.  Montrer, par un contre-exemple explicite, que l'inclusion réciproque $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est généralement fausse.

## Correction Détaillée

### Partie 1 : Démonstration de $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$

Pour démontrer qu'un ensemble $X$ est inclus dans un ensemble $Y$ (c'est-à-dire $X \subseteq Y$), il faut montrer que tout élément de $X$ est aussi un élément de $Y$.
Dans notre cas, $X = \mathcal{P}(A) \cup \mathcal{P}(B)$ et $Y = \mathcal{P}(A \cup B)$.

1.  Soit $S$ un ensemble arbitraire. Supposons que $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$.
2.  Par la définition de l'union d'ensembles, l'assertion $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$ signifie que $S \in \mathcal{P}(A)$ ou $S \in \mathcal{P}(B)$. Nous allons examiner ces deux cas séparément.

    **Cas 1 : $S \in \mathcal{P}(A)$**
    *   Par la définition de l'ensemble des parties, si $S \in \mathcal{P}(A)$, alors $S$ est un sous-ensemble de $A$. C'est-à-dire, $S \subseteq A$.
    *   Par la définition de l'union d'ensembles, nous savons que $A$ est un sous-ensemble de $A \cup B$. C'est-à-dire, $A \subseteq A \cup B$.
    *   Puisque $S \subseteq A$ et $A \subseteq A \cup B$, par la propriété de transitivité de l'inclusion, nous pouvons conclure que $S \subseteq A \cup B$.
    *   Par la définition de l'ensemble des parties, si $S \subseteq A \cup B$, alors $S$ est un élément de l'ensemble des parties de $A \cup B$. C'est-à-dire, $S \in \mathcal{P}(A \cup B)$.

    **Cas 2 : $S \in \mathcal{P}(B)$**
    *   Par la définition de l'ensemble des parties, si $S \in \mathcal{P}(B)$, alors $S$ est un sous-ensemble de $B$. C'est-à-dire, $S \subseteq B$.
    *   Par la définition de l'union d'ensembles, nous savons que $B$ est un sous-ensemble de $A \cup B$. C'est-à-dire, $B \subseteq A \cup B$.
    *   Puisque $S \subseteq B$ et $B \subseteq A \cup B$, par la propriété de transitivité de l'inclusion, nous pouvons conclure que $S \subseteq A \cup B$.
    *   Par la définition de l'ensemble des parties, si $S \subseteq A \cup B$, alors $S$ est un élément de l'ensemble des parties de $A \cup B$. C'est-à-dire, $S \in \mathcal{P}(A \cup B)$.

3.  Dans les deux cas possibles ($S \in \mathcal{P}(A)$ ou $S \in \mathcal{P}(B)$), nous avons montré que $S \in \mathcal{P}(A \cup B)$.
4.  Par conséquent, tout élément de $\mathcal{P}(A) \cup \mathcal{P}(B)$ est un élément de $\mathcal{P}(A \cup B)$.
5.  Nous concluons donc que $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$.

### Partie 2 : Démonstration que l'inclusion réciproque est généralement fausse

Pour montrer qu'une inclusion $X \subseteq Y$ est fausse, il suffit de fournir un contre-exemple. Un contre-exemple consiste à trouver des ensembles spécifiques $A$ et $B$ pour lesquels il existe un ensemble $S$ tel que $S \in \mathcal{P}(A \cup B)$ mais $S \notin \mathcal{P}(A) \cup \mathcal{P}(B)$.

1.  Considérons les ensembles finis suivants :
    *   Soit $A = \{1\}$ (un ensemble contenant un seul élément).
    *   Soit $B = \{2\}$ (un ensemble contenant un seul élément, distinct du précédent).

2.  Calculons $A \cup B$ :
    *   $A \cup B = \{1\} \cup \{2\} = \{1, 2\}$.

3.  Calculons les ensembles des parties $\mathcal{P}(A)$, $\mathcal{P}(B)$ et $\mathcal{P}(A \cup B)$ :
    *   $\mathcal{P}(A) = \{\emptyset, \{1\}\}$.
    *   $\mathcal{P}(B) = \{\emptyset, \{2\}\}$.
    *   $\mathcal{P}(A \cup B) = \mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.

4.  Calculons $\mathcal{P}(A) \cup \mathcal{P}(B)$ :
    *   $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}\} \cup \{\emptyset, \{2\}\} = \{\emptyset, \{1\}, \{2\}\}$.

5.  Nous voulons maintenant vérifier si l'inclusion $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est vraie pour ces ensembles.
    *   Nous avons $\mathcal{P}(A \cup B) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.
    *   Nous avons $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}\}$.

6.  Observons l'ensemble $S = \{1, 2\}$.
    *   Nous constatons que $S = \{1, 2\}$ est un sous-ensemble de $A \cup B = \{1, 2\}$.
    *   Par la définition de l'ensemble des parties, $S \in \mathcal{P}(A \cup B)$. En effet, $\{1, 2\} \in \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.

7.  Vérifions maintenant si $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$ :
    *   Pour que $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$, il faudrait que $S \in \mathcal{P}(A)$ ou $S \in \mathcal{P}(B)$.
    *   Vérifions si $S \in \mathcal{P}(A)$ : Pour cela, il faudrait que $S \subseteq A$. Or, $S = \{1, 2\}$ et $A = \{1\}$. L'élément $2$ appartient à $S$ mais n'appartient pas à $A$. Donc, $S \not\subseteq A$. Par conséquent, $S \notin \mathcal{P}(A)$.
    *   Vérifions si $S \in \mathcal{P}(B)$ : Pour cela, il faudrait que $S \subseteq B$. Or, $S = \{1, 2\}$ et $B = \{2\}$. L'élément $1$ appartient à $S$ mais n'appartient pas à $B$. Donc, $S \not\subseteq B$. Par conséquent, $S \notin \mathcal{P}(B)$.

8.  Puisque $S \notin \mathcal{P}(A)$ et $S \notin \mathcal{P}(B)$, par la définition de l'union d'ensembles, nous pouvons conclure que $S \notin \mathcal{P}(A) \cup \mathcal{P}(B)$.

9.  Nous avons trouvé un ensemble $S = \{1, 2\}$ tel que $S \in \mathcal{P}(A \cup B)$ mais $S \notin \mathcal{P}(A) \cup \mathcal{P}(B)$.
    Cela signifie que l'ensemble $\mathcal{P}(A \cup B)$ contient au moins un élément qui n'est pas dans $\mathcal{P}(A) \cup \mathcal{P}(B)$.
    Par conséquent, l'inclusion $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est fausse pour les ensembles $A = \{1\}$ et $B = \{2\}$.

En conclusion, l'inclusion $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$ est toujours vraie, mais l'inclusion réciproque $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est généralement fausse.
# Exercice 9 : Propriétés des familles de parties à complémentaire-disjointe-exhaustive
**Difficulté :** ⭐⭐⭐⭐⭐
**Thème :** Théorie des ensembles, opérations sur les ensembles, ensemble des parties, cardinaux, démonstration par l'absurde.

## Énoncé
Soit $E$ un ensemble non vide.
On considère une famille $\mathcal{F} \subseteq \mathcal{P}(E)$ de parties de $E$ qui satisfait la propriété suivante :
(P) Pour toute partie $X \in \mathcal{P}(E)$, on a $X \in \mathcal{F}$ si et seulement si $E \setminus X \notin \mathcal{F}$.

1.  Démontrer que pour toute partie $X \in \mathcal{P}(E)$, soit $X \in \mathcal{F}$ soit $E \setminus X \in \mathcal{F}$, mais pas les deux.
2.  Supposons que $E$ est un ensemble fini de cardinal $n \in \mathbb{N}^*$. Quel est le cardinal de $\mathcal{F}$? Justifier rigoureusement.
3.  Pour les besoins de cette question, on admet qu'une telle famille $\mathcal{F}$ existe pour tout ensemble non vide $E$.
    Soit $E$ un ensemble infini. Démontrer que $\mathcal{F}$ ne peut pas être stable par unions arbitraires (i.e., pour toute sous-famille $\mathcal{G} \subseteq \mathcal{F}$, $\bigcup_{A \in \mathcal{G}} A \in \mathcal{F}$) et en même temps stable par intersections arbitraires (i.e., pour toute sous-famille $\mathcal{G} \subseteq \mathcal{F}$, $\bigcap_{A \in \mathcal{G}} A \in \mathcal{F}$).

## Correction Détaillée

1.  **Démontrer que pour toute partie $X \in \mathcal{P}(E)$, soit $X \in \mathcal{F}$ soit $E \setminus X \in \mathcal{F}$, mais pas les deux.**

    Soit $X$ une partie quelconque de $E$, i.e., $X \in \mathcal{P}(E)$.
    La propriété (P) s'énonce comme $X \in \mathcal{F} \iff E \setminus X \notin \mathcal{F}$.
    Ceci est une équivalence logique de la forme $P \iff \neg Q$, où $P$ est "$X \in \mathcal{F}$" et $Q$ est "$E \setminus X \in \mathcal{F}$".

    *   **Prouvons que soit $X \in \mathcal{F}$ soit $E \setminus X \in \mathcal{F}$ :**
        Supposons par l'absurde que ni $X \in \mathcal{F}$ ni $E \setminus X \in \mathcal{F}$.
        Alors $X \notin \mathcal{F}$ et $E \setminus X \notin \mathcal{F}$.
        De $X \notin \mathcal{F}$, la propriété (P) implique $\neg (X \in \mathcal{F}) \iff \neg (E \setminus X \notin \mathcal{F})$.
        Donc $X \notin \mathcal{F} \iff E \setminus X \in \mathcal{F}$.
        Puisque $X \notin \mathcal{F}$ est vraie par hypothèse, on doit avoir $E \setminus X \in \mathcal{F}$.
        Ceci contredit notre hypothèse $E \setminus X \notin \mathcal{F}$.
        Donc l'hypothèse de départ est fausse. Par conséquent, au moins l'une des deux affirmations "$X \in \mathcal{F}$" ou "$E \setminus X \in \mathcal{F}$" est vraie.

    *   **Prouvons que $X \in \mathcal{F}$ et $E \setminus X \in \mathcal{F}$ ne peuvent pas être vraies simultanément :**
        Supposons par l'absurde que $X \in \mathcal{F}$ et $E \setminus X \in \mathcal{F}$.
        De $X \in \mathcal{F}$, la propriété (P) implique $X \in \mathcal{F} \iff E \setminus X \notin \mathcal{F}$.
        Puisque $X \in \mathcal{F}$ est vraie par hypothèse, on doit avoir $E \setminus X \notin \mathcal{F}$.
        Ceci contredit notre hypothèse $E \setminus X \in \mathcal{F}$.
        Donc l'hypothèse de départ est fausse. Par conséquent, les deux affirmations "$X \in \mathcal{F}$" et "$E \setminus X \in \mathcal{F}$" ne peuvent pas être vraies simultanément.

    En combinant ces deux points, on conclut que pour toute partie $X \in \mathcal{P}(E)$, soit $X \in \mathcal{F}$ soit $E \setminus X \in \mathcal{F}$, mais pas les deux.

2.  **Calcul du cardinal de $\mathcal{F}$ si $E$ est fini.**

    Soit $E$ un ensemble fini de cardinal $n \in \mathbb{N}^*$.
    Le cardinal de l'ensemble des parties $\mathcal{P}(E)$ est $2^n$.
    Considérons la relation de complémentation sur $\mathcal{P}(E)$. Pour toute partie $X \in \mathcal{P}(E)$, $E \setminus X$ est son complémentaire.
    Nous allons montrer que pour tout $X \in \mathcal{P}(E)$, $X \neq E \setminus X$.
    Supposons par l'absurde que $X = E \setminus X$. Alors, pour tout élément $x \in E$, si $x \in X$, alors $x \in E \setminus X$, ce qui implique $x \notin X$. Ceci est une contradiction. Donc $X \neq E \setminus X$.
    Puisque $X \neq E \setminus X$, les paires $\{X, E \setminus X\}$ formées d'une partie et de son complémentaire sont des ensembles de deux éléments distincts.
    De plus, ces paires partitionnent $\mathcal{P}(E)$. En effet, chaque partie $Y \in \mathcal{P}(E)$ appartient à exactement une telle paire (soit $\{Y, E \setminus Y\}$).
    Le nombre de ces paires distinctes est donc $|\mathcal{P}(E)| / 2 = 2^n / 2 = 2^{n-1}$.
    Par la question 1, pour chaque paire $\{X, E \setminus X\}$, exactement l'un des deux éléments doit appartenir à $\mathcal{F}$.
    Puisqu'il y a $2^{n-1}$ de ces paires, et que pour chaque paire nous devons choisir exactement un élément pour $\mathcal{F}$, le cardinal de $\mathcal{F}$ est $2^{n-1} \times 1 = 2^{n-1}$.
    Ainsi, $|\mathcal{F}| = 2^{n-1}$.

3.  **Démonstration pour un ensemble infini $E$ : $\mathcal{F}$ ne peut pas être stable par unions arbitraires et intersections arbitraires simultanément.**

    Supposons par l'absurde que $\mathcal{F}$ satisfait la propriété (P) et est stable par unions arbitraires et intersections arbitraires.
    Soit $I$ l'intersection de tous les éléments de $\mathcal{F}$, i.e., $I = \bigcap_{A \in \mathcal{F}} A$.
    Soit $U$ l'union de tous les éléments de $\mathcal{F}$, i.e., $U = \bigcup_{A \in \mathcal{F}} A$.
    Puisque $\mathcal{F}$ est stable par intersections arbitraires, $I \in \mathcal{F}$.
    Puisque $\mathcal{F}$ est stable par unions arbitraires, $U \in \mathcal{F}$.

    D'après la définition de $I$ et $U$, pour toute partie $A \in \mathcal{F}$, nous avons $I \subseteq A \subseteq U$.
    Si $\mathcal{F}$ est non vide (ce qui est le cas car $E$ est non vide et $\mathcal{F}$ ne peut être vide d'après la Q1 : si $\mathcal{F}=\emptyset$, alors $X \notin \mathcal{F}$ est toujours vrai, donc (P) devient $X \in \mathcal{F} \iff E \setminus X \in \mathcal{F}$, donc $E \setminus X \in \mathcal{F}$ doit être faux pour tout $X$, ce qui est impossible car la Q1 dit qu'au moins l'un doit être dans $\mathcal{F}$).
    En fait, $I$ et $U$ sont des éléments de $\mathcal{F}$. Par la Q1, $\mathcal{F}$ n'est ni $\emptyset$ ni $\mathcal{P}(E)$.

    Puisque $I \in \mathcal{F}$ et $U \in \mathcal{F}$, la famille $\mathcal{F}$ doit être exactement l'ensemble des parties $A$ de $E$ telles que $I \subseteq A \subseteq U$.
    Donc, $\mathcal{F} = \{A \in \mathcal{P}(E) \mid I \subseteq A \subseteq U\}$.

    Appliquons la propriété (P) aux parties $\emptyset$ et $E$:
    *   Si $\emptyset \in \mathcal{F}$ :
        Alors d'après (P), $E \setminus \emptyset = E \notin \mathcal{F}$.
        Si $\emptyset \in \mathcal{F}$, cela implique que $I \subseteq \emptyset \subseteq U$, donc $I = \emptyset$.
        Si $E \notin \mathcal{F}$, cela implique que l'affirmation $I \subseteq E \subseteq U$ est fausse.
        Puisque $I=\emptyset$, cela signifie que $\emptyset \subseteq E \subseteq U$ est fausse, ce qui ne peut être que si $U \neq E$.
        Donc, si $\emptyset \in \mathcal{F}$, alors $I = \emptyset$ et $U \subsetneq E$.
    *   Si $E \in \mathcal{F}$ :
        Alors d'après (P), $E \setminus E = \emptyset \notin \mathcal{F}$.
        Si $E \in \mathcal{F}$, cela implique que $I \subseteq E \subseteq U$, donc $U = E$.
        Si $\emptyset \notin \mathcal{F}$, cela implique que l'affirmation $I \subseteq \emptyset \subseteq U$ est fausse.
        Puisque $U=E$, cela signifie que $I \subseteq \emptyset \subseteq E$ est fausse, ce qui ne peut être que si $I \neq \emptyset$.
        Donc, si $E \in \mathcal{F}$, alors $U = E$ et $I \supsetneq \emptyset$.

    D'après la question 1, soit $\emptyset \in \mathcal{F}$ soit $E \in \mathcal{F}$ (mais pas les deux).
    *   Si $\emptyset \in \mathcal{F}$, alors $I = \emptyset$ et $U \subsetneq E$.
    *   Si $E \in \mathcal{F}$, alors $U = E$ et $I \supsetneq \emptyset$.

    Dans les deux cas, on ne peut pas avoir $I = \emptyset$ et $U = E$ simultanément.
    Si $I = \emptyset$ et $U = E$, alors $\mathcal{F} = \{A \in \mathcal{P}(E) \mid \emptyset \subseteq A \subseteq E\} = \mathcal{P}(E)$.
    Mais si $\mathcal{F} = \mathcal{P}(E)$, alors pour tout $X \in \mathcal{P}(E)$, $X \in \mathcal{F}$ et $E \setminus X \in \mathcal{F}$. Cela contredit la question 1 ("pas les deux").
    Donc $\mathcal{F} \neq \mathcal{P}(E)$.
    Par conséquent, nous avons montré que $I \neq \emptyset$ et $U \neq E$.

    Reprenons notre expression de $\mathcal{F}$: $\mathcal{F} = \{A \in \mathcal{P}(E) \mid I \subseteq A \subseteq U\}$.
    Puisque $I \in \mathcal{F}$, nous avons $I \subseteq I \subseteq U$, ce qui est vrai.
    Par la propriété (P), $E \setminus I \notin \mathcal{F}$.
    Ceci signifie que l'affirmation "$I \subseteq E \setminus I \subseteq U$" est fausse.
    Pour que $I \subseteq E \setminus I$ soit vraie, il faudrait que $I \cap I = \emptyset$, ce qui signifie $I = \emptyset$.
    Mais nous avons prouvé que $I \neq \emptyset$.
    Donc, l'affirmation $I \subseteq E \setminus I$ est fausse.
    Par conséquent, la condition "$I \subseteq E \setminus I \subseteq U$" est fausse (car sa première partie l'est).
    Donc, $E \setminus I \notin \mathcal{F}$ est une conséquence logique de $I \neq \emptyset$. Cette partie est consistante.

    Faisons le même raisonnement avec $U$.
    Puisque $U \in \mathcal{F}$, nous avons $I \subseteq U \subseteq U$, ce qui est vrai.
    Par la propriété (P), $E \setminus U \notin \mathcal{F}$.
    Ceci signifie que l'affirmation "$I \subseteq E \setminus U \subseteq U$" est fausse.
    Pour que $E \setminus U \subseteq U$ soit vraie, il faudrait que $U \cup (E \setminus U) = U$, ce qui signifie $E = U$.
    Mais nous avons prouvé que $U \neq E$.
    Donc, l'affirmation $E \setminus U \subseteq U$ est fausse.
    Par conséquent, la condition "$I \subseteq E \setminus U \subseteq U$" est fausse (car sa deuxième partie l'est).
    Donc, $E \setminus U \notin \mathcal{F}$ est une conséquence logique de $U \neq E$. Cette partie est consistante.

    Le point crucial est que pour tout $A \in \mathcal{P}(E)$, la propriété (P) nous dit que $A \in \mathcal{F} \iff E \setminus A \notin \mathcal{F}$.
    En utilisant la forme de $\mathcal{F}$, cela devient:
    $(I \subseteq A \subseteq U) \iff \neg (I \subseteq E \setminus A \subseteq U)$.

    Considérons la partie de droite : $\neg (I \subseteq E \setminus A \subseteq U)$.
    Nous avons déjà montré que $I \subseteq E \setminus A$ est faux si $I \ne \emptyset$ (ce que nous avons établi).
    En effet, si $I \ne \emptyset$, et si $I \subseteq E \setminus A$ était vrai, alors pour tout $x \in I$, $x \in E \setminus A$, ce qui signifie $x \notin A$. Mais par la définition de $\mathcal{F}$, si $A \in \mathcal{F}$, alors $I \subseteq A$. Donc $x \in A$.
    Ceci est une contradiction ($x \notin A$ et $x \in A$). Donc, si $I \ne \emptyset$, alors $I \not\subseteq E \setminus A$ est toujours vrai.

    Puisque $I \not\subseteq E \setminus A$ est toujours vrai (car $I \ne \emptyset$), alors l'affirmation "$I \subseteq E \setminus A \subseteq U$" est toujours fausse.
    Par conséquent, sa négation $\neg (I \subseteq E \setminus A \subseteq U)$ est toujours vraie.

    Reprenons la propriété (P) avec cette déduction :
    $(I \subseteq A \subseteq U) \iff \text{Vrai}$.
    Cette équivalence logique signifie que l'affirmation $(I \subseteq A \subseteq U)$ doit être toujours vraie pour n'importe quelle partie $A \in \mathcal{P}(E)$.
    Ceci implique que pour toute partie $A \in \mathcal{P}(E)$, $A \in \mathcal{F}$.
    Autrement dit, $\mathcal{F} = \mathcal{P}(E)$.

    Cependant, nous avons montré au début de la Q3 (déduite de Q1) que $\mathcal{F} \neq \mathcal{P}(E)$ car cette situation mène à une contradiction avec la propriété (P) elle-même (True $\iff$ False).

    Nous sommes donc arrivés à une contradiction.
    L'hypothèse initiale que $\mathcal{F}$ peut être stable par unions arbitraires et intersections arbitraires sur un ensemble infini $E$ est donc fausse.

    **Conclusion :** Pour un ensemble infini $E$, une famille $\mathcal{F} \subseteq \mathcal{P}(E)$ satisfaisant la propriété (P) ne peut pas être stable par unions arbitraires et en même temps stable par intersections arbitraires.
# Exercice 7 : Relations entre Ensembles des Parties et Opérations Ensemblistes
**Difficulté :** ⭐⭐⭐⭐
**Thème :** Théorie des ensembles (ZFC), opérations sur les ensembles, ensemble des parties $\mathcal{P}(E)$.

## Énoncé
Soient $A$ et $B$ des ensembles arbitraires définis dans un univers donné $\mathcal{U}$.

1.  **Relation entre $\mathcal{P}(A \cup B)$ et $\mathcal{P}(A) \cup \mathcal{P}(B)$**
    a.  Démontrer rigoureusement l'inclusion $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$.
    b.  Fournir un contre-exemple explicite, en spécifiant les ensembles $A$ et $B$ ainsi qu'un élément pertinent, pour montrer que l'inclusion inverse $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ n'est pas vraie en général.
    c.  Déterminer la condition nécessaire et suffisante pour que l'égalité $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$ soit vérifiée. Démontrer rigoureusement cette condition.

2.  **Relation entre $\mathcal{P}(A \setminus B)$ et $\mathcal{P}(A) \setminus \mathcal{P}(B)$**
    a.  Démontrer que l'ensemble vide $\emptyset$ est un élément de l'ensemble des parties $\mathcal{P}(A \setminus B)$ pour tout choix d'ensembles $A$ et $B$.
    b.  Démontrer que l'ensemble vide $\emptyset$ n'est jamais un élément de l'ensemble $\mathcal{P}(A) \setminus \mathcal{P}(B)$ pour tout choix d'ensembles $A$ et $B$.
    c.  En déduire que l'égalité $\mathcal{P}(A \setminus B) = \mathcal{P}(A) \setminus \mathcal{P}(B)$ ne peut jamais être vérifiée.
    d.  Fournir un contre-exemple explicite, en spécifiant les ensembles $A$ et $B$ ainsi qu'un élément pertinent, pour montrer que l'inclusion $\mathcal{P}(A \setminus B) \subseteq \mathcal{P}(A) \setminus \mathcal{P}(B)$ n'est pas vraie.
    e.  Fournir un contre-exemple explicite, en spécifiant les ensembles $A$ et $B$ ainsi qu'un élément pertinent, pour montrer que l'inclusion $\mathcal{P}(A) \setminus \mathcal{P}(B) \subseteq \mathcal{P}(A \setminus B)$ n'est pas vraie.

## Correction Détaillée

Pour la correction, nous rappelons les définitions fondamentales de la théorie des ensembles (ZFC) :
*   Un ensemble $X$ est un sous-ensemble d'un ensemble $Y$, noté $X \subseteq Y$, si et seulement si tout élément de $X$ est un élément de $Y$. Formellement : $\forall x, (x \in X \implies x \in Y)$.
*   L'ensemble des parties d'un ensemble $E$, noté $\mathcal{P}(E)$, est l'ensemble de tous les sous-ensembles de $E$. Formellement : $X \in \mathcal{P}(E) \iff X \subseteq E$.
*   L'union de deux ensembles $A$ et $B$, notée $A \cup B$, est l'ensemble des éléments qui appartiennent à $A$ ou à $B$ (ou aux deux). Formellement : $x \in A \cup B \iff (x \in A \text{ ou } x \in B)$.
*   La différence ensembliste de deux ensembles $A$ et $B$, notée $A \setminus B$, est l'ensemble des éléments qui appartiennent à $A$ mais pas à $B$. Formellement : $x \in A \setminus B \iff (x \in A \text{ et } x \notin B)$.

---

1.  **Relation entre $\mathcal{P}(A \cup B)$ et $\mathcal{P}(A) \cup \mathcal{P}(B)$**

    a.  **Démonstration de $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$**
        Soit $X$ un ensemble. Nous voulons démontrer que si $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$, alors $X \in \mathcal{P}(A \cup B)$.

        1.  Par définition de l'union d'ensembles, $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$ signifie que $X \in \mathcal{P}(A)$ ou $X \in \mathcal{P}(B)$.

        2.  **Cas 1 :** $X \in \mathcal{P}(A)$.
            Par définition de l'ensemble des parties, cela signifie que $X \subseteq A$.
            Puisque $A \subseteq A \cup B$ (par définition de l'union), et que la relation d'inclusion est transitive, nous avons $X \subseteq A \cup B$.
            Par définition de l'ensemble des parties, $X \subseteq A \cup B$ signifie que $X \in \mathcal{P}(A \cup B)$.

        3.  **Cas 2 :** $X \in \mathcal{P}(B)$.
            Par définition de l'ensemble des parties, cela signifie que $X \subseteq B$.
            Puisque $B \subseteq A \cup B$ (par définition de l'union), et que la relation d'inclusion est transitive, nous avons $X \subseteq A \cup B$.
            Par définition de l'ensemble des parties, $X \subseteq A \cup B$ signifie que $X \in \mathcal{P}(A \cup B)$.

        4.  Dans les deux cas possibles, nous avons montré que $X \in \mathcal{P}(A \cup B)$.
        5.  Par conséquent, l'inclusion $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$ est démontrée.

    b.  **Contre-exemple pour $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$**
        Nous allons montrer que l'inclusion inverse n'est pas toujours vraie.
        Soient les ensembles $A = \{1\}$ et $B = \{2\}$.

        1.  Calculons $A \cup B$.
            $A \cup B = \{x \mid x \in \{1\} \text{ ou } x \in \{2\}\} = \{1, 2\}$.

        2.  Calculons $\mathcal{P}(A \cup B)$.
            $\mathcal{P}(A \cup B) = \mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.

        3.  Calculons $\mathcal{P}(A)$.
            $\mathcal{P}(A) = \mathcal{P}(\{1\}) = \{\emptyset, \{1\}\}$.

        4.  Calculons $\mathcal{P}(B)$.
            $\mathcal{P}(B) = \mathcal{P}(\{2\}) = \{\emptyset, \{2\}\}$.

        5.  Calculons $\mathcal{P}(A) \cup \mathcal{P}(B)$.
            $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}\} \cup \{\emptyset, \{2\}\} = \{\emptyset, \{1\}, \{2\}\}$.

        6.  Considérons l'ensemble $X = \{1, 2\}$.
            Nous observons que $X \in \mathcal{P}(A \cup B)$ car $X = \{1, 2\} \subseteq \{1, 2\}$.
            Cependant, $X \notin \mathcal{P}(A) \cup \mathcal{P}(B)$ car $X \notin \mathcal{P}(A)$ (puisque $\{1, 2\} \not\subseteq \{1\}$) et $X \notin \mathcal{P}(B)$ (puisque $\{1, 2\} \not\subseteq \{2\}$).

        7.  Puisqu'il existe un ensemble $X = \{1, 2\}$ tel que $X \in \mathcal{P}(A \cup B)$ et $X \notin \mathcal{P}(A) \cup \mathcal{P}(B)$, l'inclusion $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ n'est pas vraie en général.

    c.  **Condition nécessaire et suffisante pour que $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$**

        La condition nécessaire et suffisante est que $A \subseteq B$ ou $B \subseteq A$.

        **Démonstration de la suffisance :**
        Supposons que $A \subseteq B$.
        Alors $A \cup B = B$.
        Par conséquent, $\mathcal{P}(A \cup B) = \mathcal{P}(B)$.
        D'autre part, puisque $A \subseteq B$, il s'ensuit que pour tout ensemble $X$, si $X \subseteq A$ alors $X \subseteq B$. Cela signifie que $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.
        Donc, $\mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(B)$.
        Ainsi, si $A \subseteq B$, alors $\mathcal{P}(A \cup B) = \mathcal{P}(B) = \mathcal{P}(A) \cup \mathcal{P}(B)$.

        Supposons que $B \subseteq A$.
        Alors $A \cup B = A$.
        Par conséquent, $\mathcal{P}(A \cup B) = \mathcal{P}(A)$.
        D'autre part, puisque $B \subseteq A$, il s'ensuit que pour tout ensemble $X$, si $X \subseteq B$ alors $X \subseteq A$. Cela signifie que $\mathcal{P}(B) \subseteq \mathcal{P}(A)$.
        Donc, $\mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A)$.
        Ainsi, si $B \subseteq A$, alors $\mathcal{P}(A \cup B) = \mathcal{P}(A) = \mathcal{P}(A) \cup \mathcal{P}(B)$.
        La suffisance est démontrée.

        **Démonstration de la nécessité :**
        Supposons que $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$.
        Nous allons procéder par contraposition. Supposons que la condition n'est pas vérifiée, c'est-à-dire que ni $A \subseteq B$ ni $B \subseteq A$.
        1.  Puisque $A \not\subseteq B$, il existe un élément $x_0$ tel que $x_0 \in A$ et $x_0 \notin B$.
        2.  Puisque $B \not\subseteq A$, il existe un élément $y_0$ tel que $y_0 \in B$ et $y_0 \notin A$.
        3.  Considérons l'ensemble $X = \{x_0, y_0\}$.
        4.  Puisque $x_0 \in A$ et $y_0 \in B$, il s'ensuit que $x_0 \in A \cup B$ et $y_0 \in A \cup B$.
        5.  Donc, $X \subseteq A \cup B$.
        6.  Par définition de l'ensemble des parties, $X \in \mathcal{P}(A \cup B)$.
        7.  Puisque nous avons supposé que $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$, il s'ensuit que $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$.
        8.  Par définition de l'union d'ensembles, cela signifie que $X \in \mathcal{P}(A)$ ou $X \in \mathcal{P}(B)$.
        9.  **Cas a) :** Si $X \in \mathcal{P}(A)$, alors $X \subseteq A$. Cela implique que tous les éléments de $X$ sont dans $A$. En particulier, $y_0 \in A$. Mais nous avons choisi $y_0$ tel que $y_0 \notin A$. Ceci est une contradiction.
        10. **Cas b) :** Si $X \in \mathcal{P}(B)$, alors $X \subseteq B$. Cela implique que tous les éléments de $X$ sont dans $B$. En particulier, $x_0 \in B$. Mais nous avons choisi $x_0$ tel que $x_0 \notin B$. Ceci est également une contradiction.
        11. Puisque les deux cas possibles mènent à une contradiction, notre hypothèse initiale ("ni $A \subseteq B$ ni $B \subseteq A$") doit être fausse.
        12. Par conséquent, il est nécessaire que $A \subseteq B$ ou $B \subseteq A$.
        La nécessité est démontrée.

        En conclusion, la condition nécessaire et suffisante pour que $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$ est que $A \subseteq B$ ou $B \subseteq A$.

---

2.  **Relation entre $\mathcal{P}(A \setminus B)$ et $\mathcal{P}(A) \setminus \mathcal{P}(B)$**

    a.  **Démonstration que $\emptyset \in \mathcal{P}(A \setminus B)$**
        1.  L'ensemble vide $\emptyset$ est un sous-ensemble de tout ensemble. Formellement, $\forall E, \emptyset \subseteq E$.
        2.  En particulier, l'ensemble $A \setminus B$ est un ensemble.
        3.  Donc, $\emptyset \subseteq A \setminus B$.
        4.  Par définition de l'ensemble des parties, $X \in \mathcal{P}(E) \iff X \subseteq E$.
        5.  Ainsi, $\emptyset \in \mathcal{P}(A \setminus B)$.
        Ceci est vrai pour tout choix d'ensembles $A$ et $B$.

    b.  **Démonstration que $\emptyset \notin \mathcal{P}(A) \setminus \mathcal{P}(B)$**
        Soit $X$ un ensemble. Nous voulons vérifier si $X = \emptyset$ peut être un élément de $\mathcal{P}(A) \setminus \mathcal{P}(B)$.

        1.  Par définition de la différence ensembliste entre ensembles, $X \in \mathcal{P}(A) \setminus \mathcal{P}(B)$ signifie que $X \in \mathcal{P}(A)$ et $X \notin \mathcal{P}(B)$.

        2.  Considérons l'ensemble $X = \emptyset$.
            Nous savons que l'ensemble vide $\emptyset$ est un sous-ensemble de tout ensemble $E$.
            En particulier, $\emptyset \subseteq B$.

        3.  Par définition de l'ensemble des parties, $\emptyset \subseteq B$ signifie que $\emptyset \in \mathcal{P}(B)$.

        4.  Pour que $\emptyset$ soit un élément de $\mathcal{P}(A) \setminus \mathcal{P}(B)$, il faudrait que $\emptyset \notin \mathcal{P}(B)$.
            Cependant, nous avons montré que $\emptyset \in \mathcal{P}(B)$ est toujours vrai.

        5.  Par conséquent, la condition $\emptyset \notin \mathcal{P}(B)$ n'est jamais satisfaite pour $X = \emptyset$.
        6.  Donc, $\emptyset \notin \mathcal{P}(A) \setminus \mathcal{P}(B)$.
        Ceci est vrai pour tout choix d'ensembles $A$ et $B$.

    c.  **Déduction sur l'égalité $\mathcal{P}(A \setminus B) = \mathcal{P}(A) \setminus \mathcal{P}(B)$**
        1.  D'après la question 2.a, l'ensemble $\mathcal{P}(A \setminus B)$ contient toujours l'ensemble vide $\emptyset$.
        2.  D'après la question 2.b, l'ensemble $\mathcal{P}(A) \setminus \mathcal{P}(B)$ ne contient jamais l'ensemble vide $\emptyset$.
        3.  Pour que deux ensembles soient égaux, ils doivent contenir exactement les mêmes éléments.
        4.  Puisque $\emptyset$ est un élément de $\mathcal{P}(A \setminus B)$ mais n'est pas un élément de $\mathcal{P}(A) \setminus \mathcal{P}(B)$, ces deux ensembles ne peuvent jamais être égaux.
        5.  Par conséquent, l'égalité $\mathcal{P}(A \setminus B) = \mathcal{P}(A) \setminus \mathcal{P}(B)$ ne peut jamais être vérifiée pour des ensembles $A$ et $B$ non-vides. Même si $A$ ou $B$ est vide, le raisonnement sur $\emptyset$ tient.

    d.  **Contre-exemple pour $\mathcal{P}(A \setminus B) \subseteq \mathcal{P}(A) \setminus \mathcal{P}(B)$**
        Cette inclusion n'est pas vraie. En fait, la conclusion de 2.c nous donne déjà le contre-exemple universel.
        Soient $A$ et $B$ des ensembles arbitraires.
        1.  D'après 2.a, l'ensemble $\emptyset$ est un élément de $\mathcal{P}(A \setminus B)$.
        2.  D'après 2.b, l'ensemble $\emptyset$ n'est pas un élément de $\mathcal{P}(A) \setminus \mathcal{P}(B)$.
        3.  Puisque $\emptyset \in \mathcal{P}(A \setminus B)$ et $\emptyset \notin \mathcal{P}(A) \setminus \mathcal{P}(B)$, cela démontre que l'inclusion $\mathcal{P}(A \setminus B) \subseteq \mathcal{P}(A) \setminus \mathcal{P}(B)$ n'est pas vraie en général.
        On peut prendre $A=\{1\}$ et $B=\{2\}$ par exemple. $A \setminus B = \{1\}$. $\mathcal{P}(A \setminus B) = \{\emptyset, \{1\}\}$. $\mathcal{P}(A) = \{\emptyset, \{1\}\}$. $\mathcal{P}(B) = \{\emptyset, \{2\}\}$. $\mathcal{P}(A) \setminus \mathcal{P}(B) = \{\{1\}\}$. Ici, $\emptyset \in \mathcal{P}(A \setminus B)$ mais $\emptyset \notin \mathcal{P}(A) \setminus \mathcal{P}(B)$.

    e.  **Contre-exemple pour $\mathcal{P}(A) \setminus \mathcal{P}(B) \subseteq \mathcal{P}(A \setminus B)$**
        Soient les ensembles $A = \{1, 2\}$ et $B = \{2\}$.

        1.  Calculons $A \setminus B$.
            $A \setminus B = \{x \mid x \in \{1, 2\} \text{ et } x \notin \{2\}\} = \{1\}$.

        2.  Calculons $\mathcal{P}(A \setminus B)$.
            $\mathcal{P}(A \setminus B) = \mathcal{P}(\{1\}) = \{\emptyset, \{1\}\}$.

        3.  Calculons $\mathcal{P}(A)$.
            $\mathcal{P}(A) = \mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.

        4.  Calculons $\mathcal{P}(B)$.
            $\mathcal{P}(B) = \mathcal{P}(\{2\}) = \{\emptyset, \{2\}\}$.

        5.  Calculons $\mathcal{P}(A) \setminus \mathcal{P}(B)$.
            $\mathcal{P}(A) \setminus \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\} \setminus \{\emptyset, \{2\}\} = \{\{1\}, \{1, 2\}\}$.

        6.  Considérons l'ensemble $X = \{1, 2\}$.
            Nous observons que $X \in \mathcal{P}(A) \setminus \mathcal{P}(B)$ car $X = \{1, 2\} \subseteq A$ et $X = \{1, 2\} \not\subseteq B$ (puisque $1 \in X$ et $1 \notin B$).
            Cependant, $X \notin \mathcal{P}(A \setminus B)$ car $X = \{1, 2\}$ et $A \setminus B = \{1\}$, donc $X \not\subseteq A \setminus B$ (puisque $2 \in X$ et $2 \notin A \setminus B$).

        7.  Puisqu'il existe un ensemble $X = \{1, 2\}$ tel que $X \in \mathcal{P}(A) \setminus \mathcal{P}(B)$ et $X \notin \mathcal{P}(A \setminus B)$, l'inclusion $\mathcal{P}(A) \setminus \mathcal{P}(B) \subseteq \mathcal{P}(A \setminus B)$ n'est pas vraie en général.

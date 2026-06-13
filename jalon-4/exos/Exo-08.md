# Exercice 8 : Caractérisation de l'Union des Ensembles des Parties

**Difficulté :** ⭐⭐⭐⭐
**Thème :** Ensembles des parties, opérations ensemblistes, inclusions d'ensembles.

## Énoncé
Soient $A$ et $B$ deux ensembles arbitraires. Démontrer l'équivalence suivante :
$$ \mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A \cup B) \iff (A \subseteq B \text{ ou } B \subseteq A) $$

## Correction Détaillée

Pour démontrer une équivalence de la forme $P \iff Q$, nous devons prouver les deux implications : $P \Rightarrow Q$ et $Q \Rightarrow P$.

### Partie 1 : Démonstration de l'implication $(\Rightarrow)$
Nous allons prouver que si $\mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A \cup B)$, alors $A \subseteq B$ ou $B \subseteq A$.
Nous allons utiliser une preuve par contraposition ou par l'absurde. Supposons que la conclusion soit fausse, c'est-à-dire que ni $A \subseteq B$ ni $B \subseteq A$ ne soient vrais.
Cela signifie qu'il existe un élément $x$ tel que $x \in A$ et $x \notin B$, ET il existe un élément $y$ tel que $y \in B$ et $y \notin A$.

1.  **Existence de $x$ et $y$ :**
    *   Puisque $A \not\subseteq B$, par définition de l'inclusion, il existe un élément $x$ (que nous notons $x_0$) tel que $x_0 \in A$ et $x_0 \notin B$.
    *   Puisque $B \not\subseteq A$, par définition de l'inclusion, il existe un élément $y$ (que nous notons $y_0$) tel que $y_0 \in B$ et $y_0 \notin A$.

2.  **Construction d'un ensemble test :**
    Considérons l'ensemble $S$ défini comme $S = \{x_0, y_0\}$. Cet ensemble est bien défini par l'Axiome de la Paire.

3.  **Appartenance de $S$ à $\mathcal{P}(A \cup B)$ :**
    *   Nous avons $x_0 \in A$. Par définition de l'union, $A \subseteq A \cup B$, donc $x_0 \in A \cup B$.
    *   Nous avons $y_0 \in B$. Par définition de l'union, $B \subseteq A \cup B$, donc $y_0 \in A \cup B$.
    *   Puisque tous les éléments de $S$ (à savoir $x_0$ et $y_0$) appartiennent à $A \cup B$, nous pouvons conclure que $S \subseteq A \cup B$.
    *   Par définition de l'ensemble des parties, cela signifie que $S \in \mathcal{P}(A \cup B)$.

4.  **Application de l'hypothèse :**
    *   Notre hypothèse est $\mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A \cup B)$.
    *   Puisque $S \in \mathcal{P}(A \cup B)$, il s'ensuit que $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Par définition de l'union d'ensembles, cela signifie que $S \in \mathcal{P}(A)$ ou $S \in \mathcal{P}(B)$.

5.  **Analyse des deux cas menant à une contradiction :**
    *   **Cas 1 :** Supposons $S \in \mathcal{P}(A)$.
        *   Par définition de l'ensemble des parties, $S \subseteq A$.
        *   Puisque $S = \{x_0, y_0\}$, cela implique que $x_0 \in A$ et $y_0 \in A$.
        *   Cependant, nous avons initialement défini $y_0$ comme un élément tel que $y_0 \in B$ et $y_0 \notin A$.
        *   L'affirmation $y_0 \in A$ contredit $y_0 \notin A$. Nous avons donc une contradiction.

    *   **Cas 2 :** Supposons $S \in \mathcal{P}(B)$.
        *   Par définition de l'ensemble des parties, $S \subseteq B$.
        *   Puisque $S = \{x_0, y_0\}$, cela implique que $x_0 \in B$ et $y_0 \in B$.
        *   Cependant, nous avons initialement défini $x_0$ comme un élément tel que $x_0 \in A$ et $x_0 \notin B$.
        *   L'affirmation $x_0 \in B$ contredit $x_0 \notin B$. Nous avons donc une contradiction.

6.  **Conclusion de l'implication $(\Rightarrow)$ :**
    Puisque les deux cas (qui couvrent toutes les possibilités découlant de l'hypothèse $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$) mènent à une contradiction, notre supposition initiale ("ni $A \subseteq B$ ni $B \subseteq A$") doit être fausse.
    Par conséquent, il est vrai que $A \subseteq B$ ou $B \subseteq A$.

### Partie 2 : Démonstration de l'implication $(\Leftarrow)$
Nous allons prouver que si $A \subseteq B$ ou $B \subseteq A$, alors $\mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A \cup B)$.
Pour prouver l'égalité de deux ensembles, nous devons montrer la double inclusion :
1.  $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$
2.  $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$

#### Sous-partie 2.1 : Démonstration de $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$
Cette inclusion est toujours vraie, indépendamment de la condition $A \subseteq B$ ou $B \subseteq A$.
1.  Soit $X$ un ensemble quelconque tel que $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$.
2.  Par définition de l'union d'ensembles, cela signifie que $X \in \mathcal{P}(A)$ ou $X \in \mathcal{P}(B)$.
3.  **Cas 1 :** Si $X \in \mathcal{P}(A)$.
    *   Par définition de l'ensemble des parties, $X \subseteq A$.
    *   Nous savons que $A \subseteq A \cup B$.
    *   Par transitivité de l'inclusion, $X \subseteq A \cup B$.
    *   Par définition de l'ensemble des parties, $X \in \mathcal{P}(A \cup B)$.
4.  **Cas 2 :** Si $X \in \mathcal{P}(B)$.
    *   Par définition de l'ensemble des parties, $X \subseteq B$.
    *   Nous savons que $B \subseteq A \cup B$.
    *   Par transitivité de l'inclusion, $X \subseteq A \cup B$.
    *   Par définition de l'ensemble des parties, $X \in \mathcal{P}(A \cup B)$.
5.  Dans les deux cas, nous avons montré que si $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$, alors $X \in \mathcal{P}(A \cup B)$.
6.  Par conséquent, $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$.

#### Sous-partie 2.2 : Démonstration de $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$
Cette inclusion utilise notre hypothèse : $A \subseteq B$ ou $B \subseteq A$.
Nous allons examiner les deux cas séparément.

1.  **Cas A :** Supposons que $A \subseteq B$.
    *   Par définition de l'union, si $A \subseteq B$, alors $A \cup B = B$.
    *   En substituant $A \cup B$ par $B$ dans notre inclusion à prouver, nous devons montrer que $\mathcal{P}(B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Soit $X$ un ensemble quelconque tel que $X \in \mathcal{P}(B)$.
    *   Par définition de l'union d'ensembles, tout ensemble appartenant à $\mathcal{P}(B)$ appartient également à $\mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Donc, $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Par conséquent, si $A \subseteq B$, alors $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est vraie.

2.  **Cas B :** Supposons que $B \subseteq A$.
    *   Par définition de l'union, si $B \subseteq A$, alors $A \cup B = A$.
    *   En substituant $A \cup B$ par $A$ dans notre inclusion à prouver, nous devons montrer que $\mathcal{P}(A) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Soit $X$ un ensemble quelconque tel que $X \in \mathcal{P}(A)$.
    *   Par définition de l'union d'ensembles, tout ensemble appartenant à $\mathcal{P}(A)$ appartient également à $\mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Donc, $X \in \mathcal{P}(A) \cup \mathcal{P}(B)$.
    *   Par conséquent, si $B \subseteq A$, alors $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est vraie.

3.  **Conclusion pour la sous-partie 2.2 :**
    Puisque l'hypothèse est "$A \subseteq B$ ou $B \subseteq A$", et que dans chacun de ces cas l'inclusion $\mathcal{P}(A \cup B) \subseteq \mathcal{P}(A) \cup \mathcal{P}(B)$ est démontrée, cette inclusion est vraie sous l'hypothèse donnée.

### Conclusion Générale
Nous avons démontré que l'implication $(\Rightarrow)$ est vraie et que l'implication $(\Leftarrow)$ est vraie. Par conséquent, l'équivalence est prouvée :
$$ \mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A \cup B) \iff (A \subseteq B \text{ ou } B \subseteq A) $$
Cette démonstration ne fait aucune hypothèse de finitude sur les ensembles $A$ et $B$; elle est valable pour des ensembles arbitraires, qu'ils soient finis ou infinis. Les principes utilisés sont les axiomes fondamentaux de la théorie des ensembles (Extensionalité, Paire, Union, Ensemble des Parties).
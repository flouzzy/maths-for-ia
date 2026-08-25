# Exercice 1 : Mesurabilité d'une fonction indicatrice

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{A})$ un espace mesurable et $A \in \mathcal{A}$. Démontrer, en revenant aux définitions fondamentales de la mesurabilité, que la fonction indicatrice $\mathbf{1}_A : X \to \mathbb{R}$ est mesurable par rapport à la tribu borélienne $\mathcal{B}(\mathbb{R})$.

**Démonstration :**
Pour démontrer que $\mathbf{1}_A$ est mesurable, nous devons prouver que pour tout ensemble borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $\mathbf{1}_A^{-1}(B)$ appartient à la tribu $\mathcal{A}$.
La fonction indicatrice $\mathbf{1}_A$ ne prend que deux valeurs : $0$ et $1$. Ainsi, pour tout ensemble $B \subseteq \mathbb{R}$, l'image réciproque $\mathbf{1}_A^{-1}(B)$ dépend uniquement de la présence de $0$ et $1$ dans $B$.
Quatre cas disjoints et exhaustifs se présentent :
1. Si $0 \notin B$ et $1 \notin B$ : alors l'image réciproque est vide. $\mathbf{1}_A^{-1}(B) = \emptyset$. Puisque $\mathcal{A}$ est une tribu, $\emptyset \in \mathcal{A}$.
2. Si $0 \in B$ et $1 \notin B$ : alors $\mathbf{1}_A(x) \in B$ si et seulement si $\mathbf{1}_A(x) = 0$, ce qui équivaut à $x \notin A$. Donc $\mathbf{1}_A^{-1}(B) = X \setminus A$. Puisque $A \in \mathcal{A}$ et que $\mathcal{A}$ est stable par passage au complémentaire, $X \setminus A \in \mathcal{A}$.
3. Si $0 \notin B$ et $1 \in B$ : alors $\mathbf{1}_A(x) \in B$ si et seulement si $\mathbf{1}_A(x) = 1$, ce qui équivaut à $x \in A$. Donc $\mathbf{1}_A^{-1}(B) = A \in \mathcal{A}$ par hypothèse.
4. Si $0 \in B$ et $1 \in B$ : alors pour tout $x \in X$, $\mathbf{1}_A(x) \in \{0, 1\} \subseteq B$. Donc $\mathbf{1}_A^{-1}(B) = X$. Puisque $\mathcal{A}$ est une tribu, $X \in \mathcal{A}$.
Dans les quatre configurations possibles, l'image réciproque $\mathbf{1}_A^{-1}(B)$ appartient à $\mathcal{A}$. La fonction indicatrice est donc strictement mesurable.

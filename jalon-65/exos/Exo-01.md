## Mesurabilité de la fonction indicatrice \quad $\bigstar\star\star\star\star$

Soit $(X, \mathcal{F})$ un espace mesurable et $A \subset X$. Démontrez que la fonction indicatrice $\mathbf{1}_A : X \to \mathbb{R}$ est mesurable si et seulement si $A \in \mathcal{F}$.

### Correction Détaillée

1. **Sens ($\implies$) :**
   Supposons que $\mathbf{1}_A$ soit mesurable de $(X, \mathcal{F})$ vers $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.
   Considérons l'ensemble $B = \{1\}$. Puisque $\{1\}$ est un ensemble fermé de $\mathbb{R}$, c'est un borélien, donc $B \in \mathcal{B}(\mathbb{R})$.
   Par définition de la mesurabilité, l'image réciproque $\mathbf{1}_A^{-1}(B)$ doit appartenir à $\mathcal{F}$.
   Or, par définition de la fonction indicatrice, $\mathbf{1}_A(x) = 1$ si et seulement si $x \in A$.
   Ainsi, $\mathbf{1}_A^{-1}(\{1\}) = A$.
   Conclusion : $A \in \mathcal{F}$.

2. **Sens ($\impliedby$) :**
   Supposons que $A \in \mathcal{F}$. Nous devons prouver que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $\mathbf{1}_A^{-1}(B) \in \mathcal{F}$.
   La fonction $\mathbf{1}_A$ ne prend que les valeurs $0$ et $1$. Ainsi, pour tout sous-ensemble $B$ de $\mathbb{R}$, il n'y a que 4 cas possibles pour son intersection avec $\{0, 1\}$ :
   - Cas 1 : $1 \in B$ et $0 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = A$. Comme $A \in \mathcal{F}$ par hypothèse, c'est vérifié.
   - Cas 2 : $0 \in B$ et $1 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = X \setminus A = A^c$. Comme $\mathcal{F}$ est une tribu, le complémentaire d'un de ses éléments lui appartient, donc $A^c \in \mathcal{F}$.
   - Cas 3 : $0 \in B$ et $1 \in B$. Alors $\mathbf{1}_A^{-1}(B) = X$. Or l'espace total $X$ appartient toujours à une tribu.
   - Cas 4 : $0 \notin B$ et $1 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = \emptyset$. L'ensemble vide appartient toujours à une tribu.
   Dans tous les cas possibles, $\mathbf{1}_A^{-1}(B) \in \mathcal{F}$.
   Conclusion : La fonction $\mathbf{1}_A$ est mesurable.

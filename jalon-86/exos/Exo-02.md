# Exercice 2

## Exercice 2 : Mesurabilité d'une fonction indicatrice $\bigstar\star\star\star\star$

Soit $(\Omega, \mathcal{F})$ un espace mesurable et $A$ un sous-ensemble de $\Omega$. On définit la fonction indicatrice $\mathbf{1}_A : \Omega \to \mathbb{R}$ par :
$$ \mathbf{1}_A(\omega) = \begin{cases} 1 & \text{si } \omega \in A \\ 0 & \text{si } \omega \notin A \end{cases} $$
Montrer que $\mathbf{1}_A$ est une variable aléatoire si et seulement si $A \in \mathcal{F}$.

### Correction pas à pas

1. **Condition suffisante (Si $A \in \mathcal{F}$, alors $\mathbf{1}_A$ est mesurable)**
   Supposons $A \in \mathcal{F}$. Soit $B \in \mathcal{B}(\mathbb{R})$ un borélien quelconque.
   Évaluons l'image réciproque $\mathbf{1}_A^{-1}(B) = \{ \omega \in \Omega \mid \mathbf{1}_A(\omega) \in B \}$.
   La fonction $\mathbf{1}_A$ ne prend que les valeurs $0$ et $1$. Il y a 4 cas :
   - Cas 1 : $0 \notin B$ et $1 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = \emptyset \in \mathcal{F}$.
   - Cas 2 : $0 \in B$ et $1 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = \{ \omega \mid \mathbf{1}_A(\omega) = 0 \} = A^c$. Comme $\mathcal{F}$ est une tribu et $A \in \mathcal{F}$, son complémentaire $A^c \in \mathcal{F}$.
   - Cas 3 : $0 \notin B$ et $1 \in B$. Alors $\mathbf{1}_A^{-1}(B) = \{ \omega \mid \mathbf{1}_A(\omega) = 1 \} = A \in \mathcal{F}$.
   - Cas 4 : $0 \in B$ et $1 \in B$. Alors $\mathbf{1}_A^{-1}(B) = \Omega \in \mathcal{F}$.
   Dans tous les cas, l'image réciproque appartient à $\mathcal{F}$, donc $\mathbf{1}_A$ est mesurable.

2. **Condition nécessaire (Si $\mathbf{1}_A$ est mesurable, alors $A \in \mathcal{F}$)**
   Supposons que $\mathbf{1}_A$ soit mesurable.
   Prenons le borélien particulier $B = \{1\}$.
   Par définition de la mesurabilité, l'image réciproque de ce borélien doit appartenir à $\mathcal{F}$.
   Or, $\mathbf{1}_A^{-1}(\{1\}) = \{ \omega \in \Omega \mid \mathbf{1}_A(\omega) = 1 \} = A$.
   Donc $A \in \mathcal{F}$.

3. **Conclusion**
   L'équivalence est rigoureusement démontrée.

# Exercice 3

## Exercice 3 : Tribu engendrée par une variable aléatoire $\bigstar\bigstar\star\star\star$

Soit $X : (\Omega, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ une variable aléatoire.
On note $\sigma(X) = \{ X^{-1}(B) \mid B \in \mathcal{B}(\mathbb{R}) \}$ la classe des événements engendrés par $X$.
Démontrer rigoureusement que $\sigma(X)$ est une tribu sur $\Omega$, et que c'est la plus petite tribu qui rende $X$ mesurable.

### Correction pas à pas

1. **$\sigma(X)$ contient l'ensemble vide**
   Prenons l'ensemble vide dans l'espace d'arrivée : $\emptyset \in \mathcal{B}(\mathbb{R})$.
   $X^{-1}(\emptyset) = \{ \omega \in \Omega \mid X(\omega) \in \emptyset \} = \emptyset$.
   Donc $\emptyset \in \sigma(X)$.

2. **$\sigma(X)$ est stable par passage au complémentaire**
   Soit $A \in \sigma(X)$. Par définition, il existe un borélien $B \in \mathcal{B}(\mathbb{R})$ tel que $A = X^{-1}(B)$.
   Considérons le complémentaire de $A$ :
   $A^c = (X^{-1}(B))^c = \{ \omega \mid X(\omega) \in B \}^c = \{ \omega \mid X(\omega) \notin B \}$.
   Ceci s'écrit encore : $A^c = \{ \omega \mid X(\omega) \in B^c \} = X^{-1}(B^c)$.
   Comme $\mathcal{B}(\mathbb{R})$ est une tribu, $B^c \in \mathcal{B}(\mathbb{R})$. Donc $A^c \in \sigma(X)$.

3. **$\sigma(X)$ est stable par union dénombrable**
   Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\sigma(X)$.
   Pour chaque $n$, il existe $B_n \in \mathcal{B}(\mathbb{R})$ tel que $A_n = X^{-1}(B_n)$.
   L'union s'écrit : $\bigcup_{n} A_n = \bigcup_{n} X^{-1}(B_n) = X^{-1}\left( \bigcup_{n} B_n \right)$.
   Puisque $\mathcal{B}(\mathbb{R})$ est une tribu, $\bigcup_{n} B_n \in \mathcal{B}(\mathbb{R})$.
   Donc $\bigcup_{n} A_n \in \sigma(X)$.
   Ceci prouve que $\sigma(X)$ est une tribu sur $\Omega$.

4. **Minimalité**
   Soit $\mathcal{G}$ une tribu sur $\Omega$ rendant $X$ mesurable.
   Par définition de la mesurabilité, $\forall B \in \mathcal{B}(\mathbb{R})$, on doit avoir $X^{-1}(B) \in \mathcal{G}$.
   Or, $\sigma(X)$ est précisément l'ensemble de tous les $X^{-1}(B)$.
   Donc $\sigma(X) \subset \mathcal{G}$. $\sigma(X)$ est bien la plus petite tribu rendant $X$ mesurable.

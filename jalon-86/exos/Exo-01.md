# Exercice 1 : Variable indicatrice \quad $\bigstar\star\star\star\star$

## Énoncé

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. Soit $A$ une partie de $\Omega$. On définit la fonction indicatrice $\mathbf{1}_A : \Omega \to \mathbb{R}$ par :
$$ \mathbf{1}_A(\omega) = \begin{cases} 1 & \text{si } \omega \in A \\ 0 & \text{si } \omega \notin A \end{cases} $$
Démontrer que $\mathbf{1}_A$ est une variable aléatoire si et seulement si $A \in \mathcal{F}$.

## Correction

Pour vérifier si $\mathbf{1}_A$ est une variable aléatoire, nous devons étudier l'image réciproque des boréliens $B \in \mathcal{B}(\mathbb{R})$ par $\mathbf{1}_A$, soit $\mathbf{1}_A^{-1}(B) = \{\omega \in \Omega \mid \mathbf{1}_A(\omega) \in B\}$.
La fonction $\mathbf{1}_A$ ne prend que deux valeurs : $0$ et $1$. Ainsi, pour tout borélien $B \subset \mathbb{R}$, il n'y a que 4 cas possibles :
1. Cas 1 : $0 \in B$ et $1 \in B$. Alors pour tout $\omega \in \Omega$, $\mathbf{1}_A(\omega) \in B$. Donc $\mathbf{1}_A^{-1}(B) = \Omega$.
2. Cas 2 : $1 \in B$ et $0 \notin B$. Alors $\mathbf{1}_A(\omega) \in B \iff \mathbf{1}_A(\omega) = 1 \iff \omega \in A$. Donc $\mathbf{1}_A^{-1}(B) = A$.
3. Cas 3 : $0 \in B$ et $1 \notin B$. Alors $\mathbf{1}_A(\omega) \in B \iff \mathbf{1}_A(\omega) = 0 \iff \omega \notin A$. Donc $\mathbf{1}_A^{-1}(B) = A^c$ (le complémentaire de $A$).
4. Cas 4 : $0 \notin B$ et $1 \notin B$. Alors aucun $\omega \in \Omega$ ne vérifie $\mathbf{1}_A(\omega) \in B$. Donc $\mathbf{1}_A^{-1}(B) = \emptyset$.

**Sens direct :** Si $\mathbf{1}_A$ est une variable aléatoire, par définition, pour tout borélien $B$, l'image réciproque $\mathbf{1}_A^{-1}(B)$ appartient à la tribu $\mathcal{F}$. Prenons le borélien $B = \{1\}$. D'après le cas 2, $\mathbf{1}_A^{-1}(\{1\}) = A$. Donc $A$ appartient nécessairement à $\mathcal{F}$.

**Sens réciproque :** Supposons que $A \in \mathcal{F}$. Comme $\mathcal{F}$ est une tribu, elle contient l'espace entier $\Omega$, l'ensemble vide $\emptyset$, et est stable par passage au complémentaire, donc $A^c \in \mathcal{F}$. Ainsi, dans chacun des 4 cas examinés précédemment, l'ensemble $\mathbf{1}_A^{-1}(B)$ (qui vaut $\Omega$, $A$, $A^c$, ou $\emptyset$) appartient bien à la tribu $\mathcal{F}$. La condition de mesurabilité est vérifiée pour tout borélien $B$, donc $\mathbf{1}_A$ est une variable aléatoire. $\blacksquare$

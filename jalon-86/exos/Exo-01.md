# Exercice 1

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé. Soit $A \in \mathcal{F}$ un événement. Montrer que la fonction indicatrice $\mathbf{1}_A : \Omega \to \mathbb{R}$ définie par $\mathbf{1}_A(\omega) = 1$ si $\omega \in A$ et $0$ sinon, est une variable aléatoire réelle.

## Correction Détaillée

**Correction de l'exercice 1 :**

1. Par définition, on doit montrer que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $\mathbf{1}_A^{-1}(B)$ appartient à la tribu $\mathcal{F}$.
2. La fonction $\mathbf{1}_A$ ne prend que deux valeurs : 0 et 1.
3. Calculons l'image réciproque $\mathbf{1}_A^{-1}(B)$ pour un sous-ensemble $B$ quelconque :
   - Si $0 \notin B$ et $1 \notin B$, alors $\mathbf{1}_A^{-1}(B) = \emptyset \in \mathcal{F}$.
   - Si $0 \in B$ et $1 \notin B$, alors $\mathbf{1}_A^{-1}(B) = A^c \in \mathcal{F}$ (car $A \in \mathcal{F}$ et $\mathcal{F}$ est une tribu).
   - Si $0 \notin B$ et $1 \in B$, alors $\mathbf{1}_A^{-1}(B) = A \in \mathcal{F}$.
   - Si $0 \in B$ et $1 \in B$, alors $\mathbf{1}_A^{-1}(B) = \Omega \in \mathcal{F}$.
4. Dans tous les cas, l'image réciproque est mesurable, donc $\mathbf{1}_A$ est une variable aléatoire.
$\blacksquare$

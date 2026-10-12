# Exercice 05 : Indépendance de fonctions mesurables
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires réelles indépendantes. Soient $f, g : \mathbb{R} \to \mathbb{R}$ deux fonctions mesurables.
Montrer rigoureusement que $f(X)$ et $g(Y)$ sont indépendantes.

**Correction :**
1. Soient $B_1, B_2 \in \mathcal{B}(\mathbb{R})$ deux boréliens quelconques.
Nous devons montrer que $\mathbb{P}(f(X) \in B_1 \cap g(Y) \in B_2) = \mathbb{P}(f(X) \in B_1) \mathbb{P}(g(Y) \in B_2)$.
2. L'événement $\{f(X) \in B_1\}$ est l'image réciproque par $f$, il s'écrit $\{X \in f^{-1}(B_1)\}$.
Puisque $f$ est mesurable, $f^{-1}(B_1)$ est un borélien de $\mathbb{R}$. Posons $A_1 = f^{-1}(B_1)$.
De même, l'événement $\{g(Y) \in B_2\}$ s'écrit $\{Y \in g^{-1}(B_2)\}$.
Puisque $g$ est mesurable, $g^{-1}(B_2)$ est un borélien. Posons $A_2 = g^{-1}(B_2)$.
3. Nous cherchons donc à évaluer $\mathbb{P}(X \in A_1 \cap Y \in A_2)$.
Puisque $X$ et $Y$ sont indépendantes par hypothèse (Définition 4), et que $A_1, A_2$ sont des boréliens, on a :
$\mathbb{P}(X \in A_1 \cap Y \in A_2) = \mathbb{P}(X \in A_1)\mathbb{P}(Y \in A_2)$.
4. En remplaçant $A_1$ et $A_2$ par leurs expressions :
$\mathbb{P}(f(X) \in B_1 \cap g(Y) \in B_2) = \mathbb{P}(f(X) \in B_1) \mathbb{P}(g(Y) \in B_2)$.
Ceci étant vrai pour tous boréliens, les variables aléatoires $f(X)$ et $g(Y)$ sont indépendantes.

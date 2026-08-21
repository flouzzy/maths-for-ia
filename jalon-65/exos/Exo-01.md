---
uuid: "jalon-65-exo-01"
title: "Exercice 1 : Mesurabilité de fonctions indicatrices"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Mesurabilité de fonctions indicatrices

## Énoncé

Soit $(X, \mathcal{A})$ un espace mesurable. Soient $A, B \subset X$. Démontrer que la fonction $f = \mathbb{1}_A + 2\mathbb{1}_B$ est mesurable si et seulement si $A \in \mathcal{A}$ et $B \in \mathcal{A}$.

## Solution Détaillée

Supposons $A \in \mathcal{A}$ et $B \in \mathcal{A}$. Les fonctions $\mathbb{1}_A$ et $\mathbb{1}_B$ sont mesurables car l'image réciproque de tout borélien s'exprime à l'aide de $A$, $A^c$, $X$, ou $\emptyset$. Comme l'espace des fonctions mesurables est un espace vectoriel, $f = \mathbb{1}_A + 2\mathbb{1}_B$ est mesurable. Réciproquement, supposons $f$ mesurable. $f$ prend ses valeurs dans $\{0, 1, 2, 3\}$. Remarquons que $f^{-1}(\{1, 3\}) = A$. Comme $\{1, 3\}$ est un borélien de $\mathbb{R}$ (partie finie), $f^{-1}(\{1, 3\}) = A \in \mathcal{A}$. De même $f^{-1}(\{2, 3\}) = B \in \mathcal{A}$. Ainsi, $A$ et $B$ sont mesurables. $\blacksquare$

---
uuid: "jalon-65-exo-02"
title: "Exercice 2 : Composition de fonctions"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 2 : Composition de fonctions

## Énoncé

Soient $(E, \mathcal{A})$, $(F, \mathcal{B})$ et $(G, \mathcal{C})$ trois espaces mesurables. Montrer que si $f : E \to F$ est $(\mathcal{A}, \mathcal{B})$-mesurable et $g : F \to G$ est $(\mathcal{B}, \mathcal{C})$-mesurable, alors $g \circ f$ est $(\mathcal{A}, \mathcal{C})$-mesurable.

## Solution Détaillée

Soit $C \in \mathcal{C}$. L'image réciproque par la composition est donnée par $(g \circ f)^{-1}(C) = f^{-1}(g^{-1}(C))$. Comme $g$ est mesurable, l'ensemble $B = g^{-1}(C)$ appartient à $\mathcal{B}$. Ensuite, puisque $f$ est mesurable et $B \in \mathcal{B}$, l'ensemble $A = f^{-1}(B)$ appartient à $\mathcal{A}$. Ainsi, pour tout $C \in \mathcal{C}$, $(g \circ f)^{-1}(C) \in \mathcal{A}$. Par définition, la fonction $g \circ f$ est mesurable. $\blacksquare$

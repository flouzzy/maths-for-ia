---
uuid: "jalon-58-exo-10"
title: "Exercice 10 : Généricité des matrices diagonalisables"
---

## Généricité des matrices diagonalisables \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Démontrer topologiquement que l'ensemble des matrices diagonalisables à coefficients complexes de taille $n \times n$ est dense dans $\mathcal{M}_n(\mathbb{C})$. (Indice: relier à Baire et au discriminant).

## Correction Détaillée (Zéro Ellipse)


1. Soit $\Delta(M)$ le discriminant du polynôme caractéristique de $M \in \mathcal{M}_n(\mathbb{C})$. $\Delta$ est un polynôme en les coefficients de $M$.
2. Une matrice $M$ possède $n$ valeurs propres distinctes si et seulement si $\Delta(M) \neq 0$. Les matrices ayant $n$ valeurs propres distinctes sont diagonalisables.
3. L'ensemble des matrices non diagonalisables ayant des valeurs propres multiples est inclus dans l'ensemble $Z = \{M \in \mathcal{M}_n(\mathbb{C}) \mid \Delta(M) = 0\}$.
4. Comme $\Delta$ est un polynôme non nul, l'ensemble de ses zéros, $Z$, est un ensemble fermé d'intérieur vide (une hypersurface algébrique propre).
5. (On peut voir cela via Baire : l'espace est complet, si $Z$ contenait un ouvert, le polynôme serait nul partout, ce qui est faux pour la matrice diagonale $(1, 2, \dots, n)$).
6. Ainsi, le complémentaire de $Z$, $\mathcal{M}_n(\mathbb{C}) \setminus Z$, qui ne contient que des matrices diagonalisables, est un ouvert dense.

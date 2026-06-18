---
uuid: "exo-7-6"
title: "Exo 6 - Jalon 7"
---

# Exercice 6 : Intersection et somme d'espaces vectoriels

## Énoncé
Dans $E = \mathbb{R}^4$, on donne les espaces $F = Vect(e_1, e_2)$ et $G = Vect(e_3, e_4)$ où :
$e_1 = (1, 2, 0, 1)$, $e_2 = (0, 1, 1, 1)$, $e_3 = (1, 3, 1, 2)$, $e_4 = (1, 1, -1, 0)$.
Déterminer une base de $F \cap G$ et de $F + G$.

## Correction
**Pour $F+G$ :**
$F+G = Vect(e_1, e_2, e_3, e_4)$.
On cherche une relation de dépendance linéaire.
Remarquons que $e_1 + e_2 = (1, 3, 1, 2) = e_3$.
Et $e_1 - e_2 = (1, 1, -1, 0) = e_4$.
Ainsi, $F+G = Vect(e_1, e_2)$ car $e_3, e_4 \in Vect(e_1, e_2)$.
Puisque $e_1, e_2$ ne sont pas colinéaires, $(e_1, e_2)$ est une base de $F+G$, et $\dim(F+G) = 2$.

**Pour $F \cap G$ :**
Par la formule de Grassmann :
$\dim(F+G) = \dim(F) + \dim(G) - \dim(F \cap G)$
On sait que $\dim(F) = 2$ (base $e_1, e_2$) et $\dim(G) = 2$ (base $e_3, e_4$).
Et on vient de trouver $\dim(F+G) = 2$.
Donc $2 = 2 + 2 - \dim(F \cap G) \implies \dim(F \cap G) = 2$.
Ainsi, $F \cap G = F = G$. Une base de $F \cap G$ est donc simplement $(e_1, e_2)$.

---
title: "Exo-06 : Distance de Hausdorff"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exo-06 : Distance de Hausdorff


## 1. Énoncé

Soit $(X, d)$ un espace métrique. Pour une partie non vide $A \subset X$ et un point $x \in X$, on définit la distance de $x$ à $A$ par :
$$d(x, A) = \inf_{a \in A} d(x, a)$$
1. Montrer que l'application $x \mapsto d(x, A)$ est $1$-lipschitzienne, donc continue.
2. Montrer que $d(x, A) = 0 \iff x \in \bar{A}$ (l'adhérence de $A$).
3. Si $A$ et $B$ sont deux fermés disjoints, trouver une fonction continue $f : X \to \mathbb{R}$ telle que $f$ vaille $0$ sur $A$ et $1$ sur $B$.

## 2. Correction détaillée

**Question 1 :**
Soient $x, y \in X$. Pour tout $a \in A$, l'inégalité triangulaire donne :
$d(x, a) \le d(x, y) + d(y, a)$.
Prenons l'infimum sur $a \in A$ du membre de gauche. Le membre de droite reste supérieur, donc on doit prendre l'inf sur $a$ à droite aussi :
$\inf_{a \in A} d(x, a) \le d(x, y) + \inf_{a \in A} d(y, a)$.
Soit $d(x, A) \le d(x, y) + d(y, A)$, ce qui donne $d(x, A) - d(y, A) \le d(x, y)$.
En inversant les rôles de $x$ et $y$, on obtient par symétrie :
$|d(x, A) - d(y, A)| \le d(x, y)$.
La fonction est donc bien 1-lipschitzienne.

**Question 2 :**
$d(x, A) = 0 \iff \inf_{a \in A} d(x, a) = 0$.
Cela signifie que pour tout $\epsilon > 0$, il existe $a \in A$ tel que $d(x, a) < \epsilon$.
Autrement dit, toute boule ouverte $B(x, \epsilon)$ rencontre $A$.
C'est précisément la définition de $x$ appartient à l'adhérence de $A$ ($\bar{A}$).

**Question 3 :**
Puisque $A$ et $B$ sont des fermés disjoints, $A = \bar{A}$ et $B = \bar{B}$.
Ainsi, pour tout $x \in A$, $d(x, B) > 0$ (car $x \notin B$) et vice-versa.
Considérons la fonction :
$$f(x) = \frac{d(x, A)}{d(x, A) + d(x, B)}$$
Le dénominateur ne s'annule jamais car $A$ et $B$ sont disjoints (on ne peut pas avoir $x \in A$ et $x \in B$ simultanément).
$f$ est continue comme quotient de fonctions continues.
Si $x \in A$, $d(x, A) = 0$ donc $f(x) = 0 / d(x, B) = 0$.
Si $x \in B$, $d(x, B) = 0$ donc $f(x) = d(x, A) / d(x, A) = 1$.
Ce résultat classique est le Lemme d'Urysohn pour les espaces métriques.

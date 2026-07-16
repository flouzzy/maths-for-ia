---
title: "Exercice 8 : Décomposition d'un endomorphisme via Cayley-Hamilton"
difficulty: 4
---

# Exercice 8 : Décomposition d'un endomorphisme via Cayley-Hamilton (★★★★☆)

## Énoncé

Soit $E$ un $\mathbb{R}$-espace vectoriel de dimension 3, et $u \in \mathcal{L}(E)$ un endomorphisme dont le polynôme caractéristique est :
$$\chi_u(X) = (X - 2)^2 (X + 1)$$
L'endomorphisme $u$ n'est pas supposé diagonalisable.
Déterminer explicitement des polynômes $P_1, P_2 \in \mathbb{R}[X]$ tels que les endomorphismes $p_1 = P_1(u)$ et $p_2 = P_2(u)$ soient des projecteurs spectraux vérifiant :
1. $p_1 + p_2 = \text{id}_E$
2. $p_1 \circ p_2 = p_2 \circ p_1 = 0_{\mathcal{L}(E)}$
3. $\text{Im}(p_1) = \ker((u - 2\text{id}_E)^2)$ et $\text{Im}(p_2) = \ker(u + \text{id}_E)$

## Solution Rigoureuse

Nous allons exploiter le lemme des noyaux, rendu opérant par la relation de Bézout.
Soit $Q_1(X) = (X-2)^2 = X^2 - 4X + 4$ et $Q_2(X) = X+1$.
Par le théorème de Cayley-Hamilton, $\chi_u(u) = Q_1(u) \circ Q_2(u) = 0_{\mathcal{L}(E)}$.
Les polynômes $Q_1$ et $Q_2$ sont premiers entre eux dans $\mathbb{R}[X]$ puisqu'ils n'ont aucune racine complexe commune.
Cherchons la relation de Bézout : $U(X) Q_1(X) + V(X) Q_2(X) = 1$.
Utilisons l'algorithme d'Euclide étendu, ou plus simplement, divisons $Q_1$ par $Q_2$.
$$X^2 - 4X + 4 = (X-5)(X+1) + 9$$
On réécrit le reste :
$$9 = (X^2 - 4X + 4) - (X-5)(X+1)$$
On divise par 9 :
$$1 = \frac{1}{9}(X^2 - 4X + 4) - \frac{1}{9}(X-5)(X+1)$$
Identifions les composantes de Bézout :
$$1 = \left( \frac{1}{9} \right) Q_1(X) + \left( \frac{-X+5}{9} \right) Q_2(X)$$
Posons donc les polynômes :
$$P_2(X) = \frac{1}{9} Q_1(X) = \frac{1}{9}(X^2 - 4X + 4)$$
$$P_1(X) = \frac{-X+5}{9} Q_2(X) = \frac{-X+5}{9}(X+1) = \frac{1}{9}(-X^2 + 4X + 5)$$

Vérifions que $P_1(X) + P_2(X) = 1$ :
$$P_1(X) + P_2(X) = \frac{1}{9}(-X^2 + 4X + 5 + X^2 - 4X + 4) = \frac{9}{9} = 1$$

Évaluons l'identité de Bézout en l'endomorphisme $u$ :
$$P_1(u) + P_2(u) = \text{id}_E$$
Posons $p_1 = P_1(u)$ et $p_2 = P_2(u)$. La relation devient $p_1 + p_2 = \text{id}_E$ (propriété 1 vérifiée).

Calculons le produit :
$$P_1(X) P_2(X) = \left( \frac{-X+5}{9} Q_2(X) \right) \left( \frac{1}{9} Q_1(X) \right) = \frac{-X+5}{81} Q_1(X) Q_2(X) = \frac{-X+5}{81} \chi_u(X)$$
En évaluant en $u$, par le théorème de Cayley-Hamilton, $\chi_u(u) = 0_{\mathcal{L}(E)}$. Donc :
$$p_1 \circ p_2 = p_2 \circ p_1 = P_1(u) P_2(u) = \frac{-u+5\text{id}}{81} \circ \chi_u(u) = 0_{\mathcal{L}(E)}$$
(Propriété 2 vérifiée).

Montrons que $p_1$ et $p_2$ sont des projecteurs :
On a $p_1 + p_2 = \text{id}_E$. En composant avec $p_1$ :
$$p_1 \circ p_1 + p_2 \circ p_1 = p_1 \implies p_1^2 + 0 = p_1 \implies p_1^2 = p_1$$
De même pour $p_2$. Ce sont bien des projecteurs.

Montrons les images :
Soit $x \in \text{Im}(p_1)$. Comme $p_1$ est un projecteur, $x = p_1(x)$.
Calculons $Q_1(u)(x) = Q_1(u)(p_1(x)) = (Q_1(u) \circ P_1(u))(x)$.
Or $Q_1(X) P_1(X) = Q_1(X) \frac{-X+5}{9} Q_2(X) = \frac{-X+5}{9} \chi_u(X)$.
Donc $Q_1(u) \circ P_1(u) = \frac{-u+5\text{id}}{9} \chi_u(u) = 0_{\mathcal{L}(E)}$.
Ainsi $Q_1(u)(x) = 0_E$. Or $Q_1(u) = (u - 2\text{id}_E)^2$. Donc $x \in \ker((u - 2\text{id}_E)^2)$.
L'inclusion inverse se démontre classiquement avec la relation de Bézout, confirmant ainsi $\text{Im}(p_1) = \ker((u - 2\text{id}_E)^2)$.
De même pour $p_2$.

Les polynômes sont explicitement :
$$P_1(X) = -\frac{1}{9}X^2 + \frac{4}{9}X + \frac{5}{9} \quad \text{et} \quad P_2(X) = \frac{1}{9}X^2 - \frac{4}{9}X + \frac{4}{9}$$

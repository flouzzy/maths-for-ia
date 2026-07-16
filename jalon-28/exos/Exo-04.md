---
title: "Exercice 4 : Idéal annulateur et somme directe"
difficulty: 3
---

# Exercice 4 : Idéal annulateur et somme directe (★★★☆☆)

## Énoncé

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie, et $u \in \mathcal{L}(E)$.
On suppose que $P \in \mathbb{K}[X]$ est un polynôme annulateur de $u$, et que l'on peut écrire $P(X) = P_1(X) P_2(X)$, où $P_1$ et $P_2$ sont deux polynômes premiers entre eux.
Démontrer rigoureusement (lemme des noyaux pour deux polynômes) que :
$$E = \ker(P_1(u)) \oplus \ker(P_2(u))$$

## Solution Rigoureuse

Nous devons démontrer deux choses :
1. $\ker(P_1(u)) \cap \ker(P_2(u)) = \{0_E\}$ (la somme est directe)
2. $\ker(P_1(u)) + \ker(P_2(u)) = E$ (la somme couvre tout l'espace)

Puisque $P_1$ et $P_2$ sont premiers entre eux dans l'anneau principal $\mathbb{K}[X]$, le théorème de Bachet-Bézout garantit l'existence de deux polynômes $U, V \in \mathbb{K}[X]$ tels que :
$$U(X) P_1(X) + V(X) P_2(X) = 1$$
Appliquons le morphisme d'évaluation $\Phi_u$ (substitution de $X$ par l'endomorphisme $u$) à cette égalité polynomiale. Comme $\Phi_u$ préserve les opérations, nous obtenons dans $\mathcal{L}(E)$ :
$$U(u) \circ P_1(u) + V(u) \circ P_2(u) = \text{id}_E$$
C'est la relation fondamentale.

### 1. Intersection réduite au vecteur nul
Soit $x \in \ker(P_1(u)) \cap \ker(P_2(u))$.
Par définition, $P_1(u)(x) = 0_E$ et $P_2(u)(x) = 0_E$.
Évaluons la relation fondamentale en $x$ :
$$x = \text{id}_E(x) = (U(u) \circ P_1(u))(x) + (V(u) \circ P_2(u))(x)$$
$$x = U(u)(P_1(u)(x)) + V(u)(P_2(u)(x))$$
$$x = U(u)(0_E) + V(u)(0_E)$$
Comme les endomorphismes envoient le vecteur nul sur le vecteur nul, nous avons :
$$x = 0_E + 0_E = 0_E$$
Ainsi, l'intersection est bien $\ker(P_1(u)) \cap \ker(P_2(u)) = \{0_E\}$.

### 2. Somme génératrice
Soit $x \in E$. D'après la relation de Bézout évaluée, on peut écrire :
$$x = \text{id}_E(x) = (U(u) \circ P_1(u))(x) + (V(u) \circ P_2(u))(x)$$
Posons $x_1 = (V(u) \circ P_2(u))(x)$ et $x_2 = (U(u) \circ P_1(u))(x)$.
De sorte que $x = x_1 + x_2$.

Vérifions que $x_1 \in \ker(P_1(u))$ :
Calculons $P_1(u)(x_1) = P_1(u) \circ V(u) \circ P_2(u) (x)$.
Dans $\mathbb{K}[X]$, le produit est commutatif, donc $P_1 V P_2 = V P_1 P_2 = V P$.
Par le morphisme $\Phi_u$, les endomorphismes commutent : $P_1(u) \circ V(u) \circ P_2(u) = V(u) \circ (P_1(u) \circ P_2(u)) = V(u) \circ P(u)$.
Ainsi, $P_1(u)(x_1) = V(u)(P(u)(x))$.
Or, par hypothèse de l'énoncé, $P$ est un polynôme annulateur de $u$, donc $P(u) = 0_{\mathcal{L}(E)}$.
Il s'ensuit que $P(u)(x) = 0_E$, puis $V(u)(0_E) = 0_E$.
Donc $x_1 \in \ker(P_1(u))$.

Par un raisonnement rigoureusement symétrique, on vérifie que $x_2 \in \ker(P_2(u))$ :
$P_2(u)(x_2) = P_2(u) \circ U(u) \circ P_1(u) (x) = U(u) \circ P(u)(x) = U(u)(0_E) = 0_E$.

Nous avons décomposé tout vecteur $x \in E$ comme la somme d'un vecteur de $\ker(P_1(u))$ et d'un vecteur de $\ker(P_2(u))$.
En conclusion :
$$E = \ker(P_1(u)) \oplus \ker(P_2(u))$$
La démonstration est complète.

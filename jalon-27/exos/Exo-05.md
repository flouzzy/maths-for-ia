---
uuid: "jalon-27-exo-05"
title: "Exercice 05 : Polynôme d'un endomorphisme symétrique"
---
# Exercice 05 : Polynôme d'un endomorphisme symétrique

**Difficulté :** ★★★☆☆

## Énoncé

Soit $f$ un endomorphisme symétrique. Montrer que pour tout polynôme $P \in \mathbb{R}[X]$, l'endomorphisme $P(f)$ est symétrique.

## Démonstration sans ellipse

Soit $f$ symétrique, c'est-à-dire $f^* = f$.
Considérons $f^k$. L'adjoint de $f^k$ est $(f^k)^* = (f^*)^k = f^k$. Ainsi, les puissances de $f$ sont symétriques.
Soit $P = \sum_{k=0}^d a_k X^k$.
Alors $P(f) = \sum_{k=0}^d a_k f^k$.
L'adjoint est linéaire, donc :
$$ (P(f))^* = \left( \sum_{k=0}^d a_k f^k \right)^* = \sum_{k=0}^d a_k (f^k)^* = \sum_{k=0}^d a_k f^k = P(f) $$
Ainsi, $P(f)$ est bien symétrique. $\blacksquare$

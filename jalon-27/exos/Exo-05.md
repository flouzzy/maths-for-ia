---
uuid: "jalon-27-exo-05"
title: "Exercice 05 : Polynôme d'un endomorphisme symétrique"
---
# Exercice 05 : Polynôme d'un endomorphisme symétrique

**Difficulté :** ★★★☆☆

## Énoncé

Soit $f$ un endomorphisme symétrique. Montrer que pour tout polynôme $P \in \mathbb{R}[X]$, l'endomorphisme $P(f)$ est également symétrique.

## Démonstration sans ellipse

Soit $f \in \mathcal{L}(E)$ un endomorphisme symétrique. Par définition, $f^* = f$.
Soit $P \in \mathbb{R}[X]$ un polynôme quelconque. Il s'écrit sous la forme $P(X) = \sum_{k=0}^d a_k X^k$, où $a_k \in \mathbb{R}$ sont ses coefficients et $d$ son degré.
L'endomorphisme $P(f)$ est défini par :
$$ P(f) = \sum_{k=0}^d a_k f^k $$
où $f^k = f \circ f \circ \dots \circ f$ ($k$ fois) et $f^0 = \operatorname{Id}_E$.
Calculons l'adjoint de $P(f)$. L'opération d'adjonction est linéaire, donc :
$$ (P(f))^* = \left( \sum_{k=0}^d a_k f^k \right)^* = \sum_{k=0}^d a_k (f^k)^* $$
Calculons l'adjoint de $f^k$. Par récurrence, en utilisant la propriété $(u \circ v)^* = v^* \circ u^*$ :
- Pour $k=0$, $(\operatorname{Id}_E)^* = \operatorname{Id}_E = f^0$.
- Pour $k=1$, $f^* = f = f^1$.
- Pour un $k$ quelconque, $(f^k)^* = (f \circ f^{k-1})^* = (f^{k-1})^* \circ f^* = (f^{k-1}) \circ f = f^k$.
Ainsi, pour tout $k \in \mathbb{N}$, on a $(f^k)^* = f^k$.
En réinjectant ce résultat dans l'expression de l'adjoint de $P(f)$ :
$$ (P(f))^* = \sum_{k=0}^d a_k f^k = P(f) $$
L'endomorphisme $P(f)$ est donc égal à son adjoint. Il est bien symétrique. $\blacksquare$

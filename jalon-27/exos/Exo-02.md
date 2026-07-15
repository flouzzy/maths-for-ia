---
uuid: "jalon-27-exo-02"
title: "Exercice 02 : Adjoint et inverse"
---
# Exercice 02 : Adjoint et inverse

**Difficulté :** ★☆☆☆☆

## Énoncé

Montrer que si un endomorphisme $f \in \mathcal{L}(E)$ est inversible, alors $f^*$ est inversible et $(f^*)^{-1} = (f^{-1})^*$.

## Démonstration sans ellipse

Soit $f$ inversible. On a $f \circ f^{-1} = f^{-1} \circ f = \operatorname{Id}_E$.
En prenant l'adjoint de l'identité, on obtient :
$$ \operatorname{Id}_E^* = \operatorname{Id}_E $$
D'autre part, en utilisant la propriété $(g \circ h)^* = h^* \circ g^*$, on obtient :
$$ (f \circ f^{-1})^* = (f^{-1})^* \circ f^* = \operatorname{Id}_E $$
Et de même :
$$ (f^{-1} \circ f)^* = f^* \circ (f^{-1})^* = \operatorname{Id}_E $$
Ainsi, $f^*$ est inversible, et son inverse est $(f^{-1})^*$. $\blacksquare$

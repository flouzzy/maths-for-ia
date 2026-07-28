---
uuid: "jalon-27-exo-02"
title: "Exercice 02 : Adjoint et inverse"
---
# Exercice 02 : Adjoint et inverse

**Difficulté :** ★☆☆☆☆

## Énoncé

Montrer que si un endomorphisme $f \in \mathcal{L}(E)$ est inversible, alors $f^*$ est inversible et $(f^*)^{-1} = (f^{-1})^*$.

## Démonstration sans ellipse

Soit $f \in \mathcal{L}(E)$ un endomorphisme inversible.
Par définition de l'inverse, nous avons $f \circ f^{-1} = f^{-1} \circ f = \operatorname{Id}_E$.
Nous savons que l'adjoint de l'identité est l'identité elle-même, car :
$$ \langle \operatorname{Id}_E(x), y \rangle = \langle x, y \rangle = \langle x, \operatorname{Id}_E(y) \rangle $$
Donc $\operatorname{Id}_E^* = \operatorname{Id}_E$.
Prenons l'adjoint de l'égalité $f \circ f^{-1} = \operatorname{Id}_E$. En utilisant la propriété de l'exercice 1, $(u \circ v)^* = v^* \circ u^*$, nous obtenons :
$$ (f \circ f^{-1})^* = \operatorname{Id}_E^* \implies (f^{-1})^* \circ f^* = \operatorname{Id}_E $$
De même, en prenant l'adjoint de $f^{-1} \circ f = \operatorname{Id}_E$ :
$$ (f^{-1} \circ f)^* = \operatorname{Id}_E^* \implies f^* \circ (f^{-1})^* = \operatorname{Id}_E $$
Les relations $(f^{-1})^* \circ f^* = \operatorname{Id}_E$ et $f^* \circ (f^{-1})^* = \operatorname{Id}_E$ démontrent exactement que l'endomorphisme $f^*$ est inversible, et que son inverse est donné par $(f^{-1})^*$. $\blacksquare$

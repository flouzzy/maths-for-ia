---
uuid: "jalon-27-exo-01"
title: "Exercice 01 : Adjoint d'une composée"
---
# Exercice 01 : Adjoint d'une composée

**Difficulté :** ★☆☆☆☆

## Énoncé

Démontrer que pour tout $f, g \in \mathcal{L}(E)$, on a $(f \circ g)^* = g^* \circ f^*$.

## Démonstration sans ellipse

Soient $x, y \in E$. Par définition de l'adjoint de $f \circ g$, on a :
$$ \langle (f \circ g)(x), y \rangle = \langle x, (f \circ g)^*(y) \rangle $$
D'autre part, en développant la composition :
$$ \langle (f \circ g)(x), y \rangle = \langle f(g(x)), y \rangle $$
En appliquant la définition de l'adjoint de $f$ à la paire $(g(x), y)$ :
$$ \langle f(g(x)), y \rangle = \langle g(x), f^*(y) \rangle $$
Ensuite, en appliquant la définition de l'adjoint de $g$ à la paire $(x, f^*(y))$ :
$$ \langle g(x), f^*(y) \rangle = \langle x, g^*(f^*(y)) \rangle = \langle x, (g^* \circ f^*)(y) \rangle $$
Ainsi, pour tout $x, y \in E$, on obtient :
$$ \langle x, (f \circ g)^*(y) \rangle = \langle x, (g^* \circ f^*)(y) \rangle $$
Ceci implique que $(f \circ g)^*(y) = (g^* \circ f^*)(y)$ pour tout $y \in E$.
Par conséquent, $(f \circ g)^* = g^* \circ f^*$. $\blacksquare$

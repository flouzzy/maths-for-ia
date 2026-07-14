---
uuid: "jalon-27-exo-01"
title: "Exercice 01 : Adjoint d'une composée"
---
# Exercice 01 : Adjoint d'une composée

**Difficulté :** ★☆☆☆☆

## Énoncé

Démontrer que pour tout $f, g \in \mathcal{L}(E)$, on a $(f \circ g)^* = g^* \circ f^*$.

## Démonstration sans ellipse

Soit $x, y \in E$. Par définition de l'adjoint, on a :
$$ \langle (f \circ g)(x), y \rangle = \langle f(g(x)), y \rangle $$
En appliquant la définition de l'adjoint de $f$ :
$$ \langle f(g(x)), y \rangle = \langle g(x), f^*(y) \rangle $$
Puis, en appliquant la définition de l'adjoint de $g$ sur le vecteur de gauche :
$$ \langle g(x), f^*(y) \rangle = \langle x, g^*(f^*(y)) \rangle $$
On en déduit que :
$$ \langle (f \circ g)(x), y \rangle = \langle x, (g^* \circ f^*)(y) \rangle $$
Par unicité de l'adjoint, on a bien $(f \circ g)^* = g^* \circ f^*$. $\blacksquare$

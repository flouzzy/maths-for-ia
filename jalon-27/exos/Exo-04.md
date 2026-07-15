---
uuid: "jalon-27-exo-04"
title: "Exercice 04 : Adjoint d'une translation"
---
# Exercice 04 : Adjoint d'une translation

**Difficulté :** ★★☆☆☆

## Énoncé

Un endomorphisme antisymétrique est tel que $f^* = -f$. Montrer que si $f$ est antisymétrique, alors pour tout $x \in E, \langle f(x), x \rangle = 0$.

## Démonstration sans ellipse

Soit $f$ antisymétrique. Par définition, $f^* = -f$.
Calculons le produit scalaire $\langle f(x), x \rangle$.
Par propriété de l'adjoint :
$$ \langle f(x), x \rangle = \langle x, f^*(x) \rangle $$
Puisque $f^* = -f$, on a :
$$ \langle x, f^*(x) \rangle = \langle x, -f(x) \rangle = -\langle x, f(x) \rangle $$
Par symétrie du produit scalaire euclidien :
$$ -\langle x, f(x) \rangle = -\langle f(x), x \rangle $$
On obtient donc $\langle f(x), x \rangle = -\langle f(x), x \rangle$, ce qui implique $2\langle f(x), x \rangle = 0$, et donc $\langle f(x), x \rangle = 0$. $\blacksquare$

---
uuid: "jalon-27-exo-04"
title: "Exercice 04 : Adjoint d'une translation"
---
# Exercice 04 : Endomorphisme antisymétrique

**Difficulté :** ★★☆☆☆

## Énoncé

Un endomorphisme $f \in \mathcal{L}(E)$ est dit antisymétrique si $f^* = -f$. Montrer que si $f$ est antisymétrique, alors pour tout vecteur $x \in E$, on a $\langle f(x), x \rangle = 0$.

## Démonstration sans ellipse

Soit $f \in \mathcal{L}(E)$ un endomorphisme antisymétrique. Par définition, nous avons la relation $f^* = -f$.
Considérons le produit scalaire $\langle f(x), x \rangle$ pour un vecteur arbitraire $x \in E$.
D'après la définition de l'endomorphisme adjoint, nous pouvons transférer l'opérateur $f$ sur le second argument du produit scalaire :
$$ \langle f(x), x \rangle = \langle x, f^*(x) \rangle $$
En utilisant l'hypothèse d'antisymétrie $f^* = -f$, nous remplaçons $f^*(x)$ par $-f(x)$ :
$$ \langle x, f^*(x) \rangle = \langle x, -f(x) \rangle $$
Par bilinéarité du produit scalaire (spécifiquement la linéarité par rapport à la seconde variable), nous pouvons sortir le scalaire $-1$ :
$$ \langle x, -f(x) \rangle = -\langle x, f(x) \rangle $$
Par ailleurs, le produit scalaire sur un espace euclidien réel est symétrique, ce qui signifie que $\langle x, y \rangle = \langle y, x \rangle$ pour tout $x, y$. En appliquant cela, nous obtenons :
$$ -\langle x, f(x) \rangle = -\langle f(x), x \rangle $$
Nous avons ainsi établi l'égalité :
$$ \langle f(x), x \rangle = -\langle f(x), x \rangle $$
En additionnant $\langle f(x), x \rangle$ des deux côtés de l'équation, il vient :
$$ 2\langle f(x), x \rangle = 0 $$
Puisque le scalaire $2$ est non nul, il en résulte nécessairement que :
$$ \langle f(x), x \rangle = 0 $$
Cette propriété démontre que pour un endomorphisme antisymétrique, le vecteur image $f(x)$ est toujours orthogonal au vecteur source $x$. $\blacksquare$

---
uuid: "jalon-26-exo-08"
title: "Théorème de Riesz (cas fini)"
difficulty: 5
---

# Exercice 8 : Théorème de Riesz (cas fini) (Difficulté ★★★★★)

Soit $E$ un espace euclidien. On considère l'application $\Phi : E \to E^*$ (où $E^*$ est l'espace dual de $E$) définie par $\Phi(y)(x) = \langle y, x \rangle$.
1. Montrer que $\Phi$ est une application linéaire.
2. Déterminer le noyau de $\Phi$.
3. En utilisant un argument de dimension, prouver le théorème de représentation de Riesz : pour toute forme linéaire $f \in E^*$, il existe un unique vecteur $y \in E$ tel que pour tout $x \in E$, $f(x) = \langle y, x \rangle$.

## Démonstration Rigoureuse à Blanc

1. Montrons que $\Phi$ est linéaire. Soient $y_1, y_2 \in E$ et $\lambda \in \mathbb{R}$.
   - Pour tout $x \in E$, $\Phi(\lambda y_1 + y_2)(x) = \langle \lambda y_1 + y_2, x \rangle$.
   - Par bilinéarité du produit scalaire : $= \lambda \langle y_1, x \rangle + \langle y_2, x \rangle$.
   - Par définition de $\Phi$ : $= \lambda \Phi(y_1)(x) + \Phi(y_2)(x) = (\lambda \Phi(y_1) + \Phi(y_2))(x)$.
   - Les deux fonctions sont égales sur $E$, donc $\Phi(\lambda y_1 + y_2) = \lambda \Phi(y_1) + \Phi(y_2)$. $\Phi$ est une application linéaire.

2. Cherchons $\ker(\Phi)$.
   - $y \in \ker(\Phi) \iff \Phi(y) = 0_{E^*} \iff \forall x \in E, \Phi(y)(x) = 0$.
   - Soit $\forall x \in E, \langle y, x \rangle = 0$.
   - Puisque cela est vrai pour tout $x$, choisissons $x = y$. On a alors $\langle y, y \rangle = 0$.
   - L'axiome de définition positive du produit scalaire implique alors $y = 0_E$.
   - Donc $\ker(\Phi) = \{0_E\}$. L'application $\Phi$ est injective.

3. En dimension finie, on sait que l'espace dual $E^*$ a la même dimension que $E$.
   - $\dim(E) = \dim(E^*)$.
   - $\Phi$ est une application linéaire injective entre deux espaces de même dimension finie.
   - D'après le théorème du rang, $\Phi$ est un isomorphisme, donc une bijection.
   - La surjectivité de $\Phi$ signifie exactement que pour toute forme linéaire $f \in E^*$, il existe un vecteur $y \in E$ tel que $\Phi(y) = f$.
   - C'est-à-dire, $\forall x \in E, \Phi(y)(x) = f(x)$, soit $\langle y, x \rangle = f(x)$.
   - L'injectivité garantit que ce vecteur $y$ est unique.
   - C'est la preuve complète du théorème de Riesz en dimension finie.
   $\blacksquare$

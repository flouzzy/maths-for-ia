# Exercice 8 : Séparation par un polyèdre $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soient $x_1, ..., x_m \in \mathbb{R}^n$ des points. Montrez que l'enveloppe convexe $C$ de ces points est l'intersection d'un nombre fini de demi-espaces fermés.

## Correction Complète
L'ensemble $C = \{ \sum_{i=1}^m \lambda_i x_i \mid \lambda_i \geq 0, \sum \lambda_i = 1 \}$ est un polytope (convexe compact engendré par un nombre fini de sommets).
Pour tout point $y \notin C$, le théorème de séparation stricte de Hahn-Banach (seconde forme) garantit qu'il existe un hyperplan séparant strictement $y$ de $C$.
Donc, $C$ est l'intersection de tous les demi-espaces fermés qui le contiennent.
Cependant, l'énoncé demande de prouver que c'est une intersection d'un nombre *fini* de demi-espaces.
Ceci est le théorème fondamental de la théorie des polytopes (théorème de Weyl-Minkowski).
Considérons le polaire de $C$ translaté à l'origine. L'espace dual (l'espace des formes linéaires) est fini dimensionnel.
Les hyperplans "d'appui" (ceux dont la frontière intersecte $C$) sont définis par les facettes de la frontière de $C$.
Puisque $C$ a un nombre fini de sommets, par combinatoire, les faces de dimension $n-1$ reliant ces sommets sont en nombre fini.
Chaque face de dimension $n-1$ détermine un unique hyperplan affine (et le demi-espace associé pointant vers l'intérieur de $C$).
Par convexité, l'intersection de ces $k$ demi-espaces est exactement $C$. $\blacksquare$

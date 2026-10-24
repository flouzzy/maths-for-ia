# Exercice 2 : $\bigstar\star\star\star\star$

## Énoncé

Soit $E$ un espace vectoriel normé et $A \subset E$ un ensemble convexe fermé. Montrer que tout point $x_0 \notin A$ peut être séparé strictement de $A$ par un hyperplan affine fermé.

## Correction

**Étape 1 : Formulation**
Nous souhaitons appliquer la forme géométrique stricte du théorème de Hahn-Banach. Les ensembles à séparer sont $A$ et $B = \{x_0\}$.
- $A$ est convexe et fermé (par hypothèse).
- $B = \{x_0\}$ est un singleton, donc compact et convexe.
- Comme $x_0 \notin A$, $A \cap B = \emptyset$.

**Étape 2 : Application du théorème**
D'après la deuxième forme géométrique de Hahn-Banach, puisque $A$ est fermé, $B$ compact, et $A, B$ convexes disjoints, il existe un hyperplan affine fermé qui les sépare strictement.
Il existe donc une forme linéaire continue $f \in E'$ et un réel $\alpha$ tels que pour un certain $\epsilon > 0$ :
$\forall a \in A, f(a) \le \alpha - \epsilon < \alpha < \alpha + \epsilon \le f(x_0)$.

Ainsi, l'hyperplan affine d'équation $f(x) = \alpha$ sépare strictement le point $x_0$ du convexe fermé $A$. $\blacksquare$

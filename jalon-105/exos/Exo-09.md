# Exercice 9 : Inverse d'un opérateur et son adjoint $\bigstar\bigstar\bigstar\bigstar\bigstar$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$ un opérateur inversible (bijectif, d'inverse borné $T^{-1} \in \mathcal{L}(H)$).
1. Démontrer que l'opérateur adjoint $T^*$ est également inversible et que $(T^*)^{-1} = (T^{-1})^*$.
2. Déduire que si un opérateur inversible est auto-adjoint, alors son inverse est également auto-adjoint.

## Correction
1. Par hypothèse, $T$ est inversible, ce qui signifie que $T T^{-1} = I$ et $T^{-1} T = I$, où $I$ est l'opérateur identité sur $H$.
Prenons l'adjoint de chaque membre de ces deux équations vectorielles. Nous utiliserons la propriété algébrique multiplicative $(AB)^* = B^*A^*$.
Pour la première équation :
$$ (T T^{-1})^* = I^* $$
L'adjoint de l'identité est l'identité elle-même (car $\langle Ix, y \rangle = \langle x, y \rangle = \langle x, Iy \rangle$). En appliquant la règle d'inversion de l'ordre pour l'adjoint d'un produit, on obtient :
$$ (T^{-1})^* T^* = I $$
Pour la seconde équation :
$$ (T^{-1} T)^* = I^* $$
$$ T^* (T^{-1})^* = I $$
Nous venons de démontrer qu'il existe un opérateur, spécifiquement $S = (T^{-1})^*$, tel que $S T^* = I$ et $T^* S = I$.
Par la définition même de l'opérabilité inverse, cela signifie que $T^*$ est inversible, et que son inverse inverse (unique) est précisément $S$.
On conclut rigoureusement que :
$$ (T^*)^{-1} = (T^{-1})^* $$

2. Hypothèse : $T$ est inversible et auto-adjoint, ce qui signifie que $T^* = T$.
Nous voulons montrer que $T^{-1}$ est auto-adjoint, c'est-à-dire que $(T^{-1})^* = T^{-1}$.
D'après le résultat démontré à la question 1, nous connaissons la relation :
$$ (T^{-1})^* = (T^*)^{-1} $$
Maintenant, appliquons l'hypothèse que $T$ est auto-adjoint en remplaçant l'opérateur $T^*$ par l'opérateur $T$ dans le membre de droite de l'équation :
$$ (T^*)^{-1} = (T)^{-1} = T^{-1} $$
En connectant les deux parties de la chaîne logique, on obtient formellement :
$$ (T^{-1})^* = T^{-1} $$
Cette équation est la définition exacte stipulant que l'opérateur inverse $T^{-1}$ est un opérateur auto-adjoint.

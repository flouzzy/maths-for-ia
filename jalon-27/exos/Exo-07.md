---
uuid: "jalon-27-exo-07"
title: "Exercice 07 : Rang de l'adjoint"
---
# Exercice 07 : Diagonalisation simultanée

**Difficulté :** ★★★★☆

## Énoncé

Soient $f$ et $g$ deux endomorphismes symétriques de $E$ qui commutent ($f \circ g = g \circ f$). Montrer qu'ils sont co-diagonalisables dans une même base orthonormée.

## Démonstration sans ellipse

Soient $f$ et $g$ deux endomorphismes symétriques qui commutent. D'après le théorème spectral, $f$ est diagonalisable. Ses sous-espaces propres $E_\lambda(f)$ sont mutuellement orthogonaux et leur somme directe est $E$.
Soit $\lambda$ une valeur propre de $f$. Montrons que $E_\lambda(f)$ est stable par $g$.
Soit $x \in E_\lambda(f)$. Alors $f(x) = \lambda x$.
Calculons $f(g(x))$. Comme $f$ et $g$ commutent, $f(g(x)) = g(f(x))$.
Puisque $f(x) = \lambda x$, on a $g(f(x)) = g(\lambda x) = \lambda g(x)$.
Donc $f(g(x)) = \lambda g(x)$, ce qui prouve que $g(x) \in E_\lambda(f)$.
Ainsi, la restriction $g_\lambda$ de $g$ à $E_\lambda(f)$ est un endomorphisme symétrique de l'espace euclidien $E_\lambda(f)$.
En appliquant le théorème spectral à $g_\lambda$ sur $E_\lambda(f)$, on trouve une base orthonormée $B_\lambda$ de $E_\lambda(f)$ formée de vecteurs propres de $g$.
Ces vecteurs sont par construction des vecteurs propres de $f$ (puisqu'ils sont dans $E_\lambda(f)$) et des vecteurs propres de $g$.
En réunissant les bases $B_\lambda$ pour toutes les valeurs propres $\lambda$ de $f$, on obtient une base $B$ de $E$.
Comme les sous-espaces propres $E_\lambda(f)$ sont orthogonaux deux à deux, et que chaque $B_\lambda$ est orthonormée, la réunion $B$ est une base orthonormée de $E$.
Dans cette base $B$, les matrices de $f$ et de $g$ sont simultanément diagonales. $\blacksquare$

---
title: "Exercice 6 : Comportement de la mesure par homothétie"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

## Énoncé

Soit $A \subset \mathbb{R}$ un sous-ensemble mesurable au sens de Lebesgue et soit $t > 0$ un scalaire réel strictement positif.
On définit l'homothétie de $A$ par le rapport $t$ comme l'ensemble :
$$tA = \{ t \cdot x \mid x \in A \}$$
Démontrer que $tA$ est également mesurable et que :
$$\lambda(tA) = t \cdot \lambda(A)$$

## Correction Détaillée

1. **Effet de l'homothétie sur la mesure extérieure :**
Soit $A \subset \mathbb{R}$. Nous allons d'abord montrer que $\lambda^*(tA) = t\lambda^*(A)$.
Si $\lambda^*(A) = +\infty$, alors tout recouvrement de $tA$ divisé par $t$ donne un recouvrement de $A$, impliquant que l'infimum pour $tA$ est aussi infini.
Supposons $\lambda^*(A)$ finie. Pour tout $\epsilon > 0$, il existe un recouvrement $(I_n)$ de $A$ par des intervalles ouverts tel que $\sum \ell(I_n) \le \lambda^*(A) + \epsilon$.
Considérons la famille d'intervalles dilatés $J_n = t \cdot I_n$.
Si $I_n = ]a_n, b_n[$, alors $J_n = ]ta_n, tb_n[$, dont la longueur est $\ell(J_n) = t(b_n - a_n) = t \cdot \ell(I_n)$.
La famille $(J_n)$ forme manifestement un recouvrement ouvert de l'ensemble $tA$.
Par définition de la mesure extérieure :
$$\lambda^*(tA) \le \sum \ell(J_n) = \sum t \ell(I_n) = t \sum \ell(I_n) \le t(\lambda^*(A) + \epsilon)$$
En passant à la limite $\epsilon \to 0$, on obtient la majoration : $\lambda^*(tA) \le t\lambda^*(A)$.

Pour l'inégalité inverse, appliquons le résultat précédent à l'ensemble $tA$ avec le scalaire $1/t$ :
$$\lambda^*(A) = \lambda^*\left(\frac{1}{t} (tA)\right) \le \frac{1}{t} \lambda^*(tA)$$
En multipliant par $t > 0$, on obtient : $t\lambda^*(A) \le \lambda^*(tA)$.
Par double inégalité, on a prouvé l'égalité fondamentale : $\lambda^*(tA) = t\lambda^*(A)$.

2. **Préservation de la mesurabilité par le critère de Carathéodory :**
Par hypothèse, $A$ est mesurable. Il vérifie le critère de Carathéodory pour tout ensemble de test $E \subset \mathbb{R}$ :
$$\lambda^*(E) = \lambda^*(E \cap A) + \lambda^*(E \cap A^c)$$
Nous devons prouver que l'ensemble $tA$ vérifie ce même critère. Soit $F \subset \mathbb{R}$ un ensemble test quelconque pour $tA$.
Formons l'ensemble $E = \frac{1}{t} F = \{ \frac{x}{t} \mid x \in F \}$. On injecte cet ensemble $E$ dans la relation de Carathéodory de $A$ :
$$\lambda^*\left(\frac{1}{t}F\right) = \lambda^*\left(\frac{1}{t}F \cap A\right) + \lambda^*\left(\frac{1}{t}F \cap A^c\right)$$
En utilisant la propriété d'homothétie de la mesure extérieure démontrée au point 1, on extrait le scalaire :
$$\frac{1}{t} \lambda^*(F) = \frac{1}{t} \lambda^*(F \cap tA) + \frac{1}{t} \lambda^*(F \cap tA^c)$$
Où l'on a utilisé l'identité ensembliste géométrique $\frac{1}{t}F \cap A = \frac{1}{t}(F \cap tA)$.
De plus, le complémentaire respecte l'homothétie : $tA^c = (tA)^c$.
En multipliant l'équation entière par $t > 0$, on retrouve formellement le critère de Carathéodory :
$$\lambda^*(F) = \lambda^*(F \cap tA) + \lambda^*(F \cap (tA)^c)$$
L'ensemble test $F$ étant arbitraire, cela démontre que l'ensemble dilaté $tA$ est Lebesgue-mesurable. L'égalité des mesures découle alors trivialement de la première étape, achevant la preuve de la linéarité par homothétie.

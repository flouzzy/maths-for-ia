---
title: "Exercice 2 : Noyau et image d'un adjoint"
difficulty: "★★☆☆☆"
---
# Exercice 2 : Noyau et image d'un adjoint

## Énoncé
Soit $E$ un espace euclidien et $f \in \mathcal{L}(E)$.
Démontrer rigoureusement les relations fondamentales suivantes :
1. $\text{Ker}(f^*) = (\text{Im}(f))^\perp$
2. $\text{Im}(f^*) = (\text{Ker}(f))^\perp$

## Correction Zéro Ellipse
**1. Preuve de $\text{Ker}(f^*) = (\text{Im}(f))^\perp$**
Soit $y \in E$.
$y \in \text{Ker}(f^*) \iff f^*(y) = 0_E$.
Le vecteur $f^*(y)$ est nul si et seulement si son produit scalaire avec tout vecteur $x \in E$ est nul.
$\iff \forall x \in E, \langle x, f^*(y) \rangle = 0$.
Par définition de l'adjoint, on peut transférer $f^*$ sur l'autre argument :
$\iff \forall x \in E, \langle f(x), y \rangle = 0$.
Or, l'ensemble des vecteurs de la forme $f(x)$ pour $x \in E$ constitue exactement l'image de $f$, notée $\text{Im}(f)$.
Donc la proposition s'écrit :
$\iff \forall z \in \text{Im}(f), \langle z, y \rangle = 0$.
Par définition de l'orthogonal d'un sous-espace vectoriel, cela signifie exactement que $y \in (\text{Im}(f))^\perp$.
Ainsi, l'équivalence est totale et $\text{Ker}(f^*) = (\text{Im}(f))^\perp$.

**2. Preuve de $\text{Im}(f^*) = (\text{Ker}(f))^\perp$**
Nous pourrions faire une démonstration directe, mais il est plus élégant et rigoureux d'utiliser la propriété précédente.
Appliquons le résultat 1. à l'endomorphisme $f^*$ au lieu de $f$ :
$\text{Ker}((f^*)^*) = (\text{Im}(f^*))^\perp$.
Or, l'adjoint de l'adjoint est l'opérateur lui-même : $(f^*)^* = f$. En effet, $\forall x,y, \langle f^*(x), y \rangle = \langle x, f(y) \rangle = \langle f(y), x \rangle$.
Donc $\text{Ker}(f) = (\text{Im}(f^*))^\perp$.
Prenons maintenant l'orthogonal des deux membres de cette égalité. Dans un espace euclidien (donc de dimension finie), pour tout sous-espace $F$, on a $(F^\perp)^\perp = F$.
Ainsi :
$(\text{Ker}(f))^\perp = ((\text{Im}(f^*))^\perp)^\perp = \text{Im}(f^*)$.
Ce qui conclut la preuve.

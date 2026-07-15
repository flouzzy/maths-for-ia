---
title: "Exercice 1 : Adjoint d'une composée et d'une combinaison linéaire"
difficulty: "★☆☆☆☆"
---
# Exercice 1 : Adjoint d'une composée et d'une combinaison linéaire

## Énoncé
Soient $E$ un espace euclidien, et $f, g \in \mathcal{L}(E)$. Soient $\alpha, \beta \in \mathbb{R}$.
Démontrer, en utilisant uniquement la définition de l'adjoint par le produit scalaire, que :
1. L'adjoint est une application linéaire : $(\alpha f + \beta g)^* = \alpha f^* + \beta g^*$
2. L'adjoint renverse l'ordre de la composition : $(f \circ g)^* = g^* \circ f^*$

## Correction Zéro Ellipse
**1. Linéarité de l'adjoint**
Soient $x, y \in E$. Par définition de l'adjoint, on évalue :
$$ \langle (\alpha f + \beta g)(x), y \rangle $$
Par linéarité de l'évaluation :
$$ \langle \alpha f(x) + \beta g(x), y \rangle $$
Par bilinéarité (linéarité à gauche) du produit scalaire :
$$ \alpha \langle f(x), y \rangle + \beta \langle g(x), y \rangle $$
Par définition des adjoints $f^*$ et $g^*$ :
$$ \alpha \langle x, f^*(y) \rangle + \beta \langle x, g^*(y) \rangle $$
Par bilinéarité (linéarité à droite) du produit scalaire :
$$ \langle x, \alpha f^*(y) \rangle + \langle x, \beta g^*(y) \rangle = \langle x, \alpha f^*(y) + \beta g^*(y) \rangle $$
Par définition de l'addition et de la multiplication par un scalaire dans $\mathcal{L}(E)$ :
$$ \langle x, (\alpha f^* + \beta g^*)(y) \rangle $$
Puisque cette égalité $\langle (\alpha f + \beta g)(x), y \rangle = \langle x, (\alpha f^* + \beta g^*)(y) \rangle$ est vraie pour tous $x, y \in E$, on conclut par unicité de l'adjoint que :
$$ (\alpha f + \beta g)^* = \alpha f^* + \beta g^* $$

**2. Adjoint de la composition**
Soient $x, y \in E$. Évaluons :
$$ \langle (f \circ g)(x), y \rangle = \langle f(g(x)), y \rangle $$
En appliquant la définition de $f^*$ sur les vecteurs $g(x)$ et $y$ :
$$ \langle g(x), f^*(y) \rangle $$
En appliquant ensuite la définition de $g^*$ sur les vecteurs $x$ et $f^*(y)$ :
$$ \langle x, g^*(f^*(y)) \rangle = \langle x, (g^* \circ f^*)(y) \rangle $$
Puisque l'égalité est vraie pour tous $x, y \in E$, on conclut par unicité de l'adjoint que :
$$ (f \circ g)^* = g^* \circ f^* $$

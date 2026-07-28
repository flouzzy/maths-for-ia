---
uuid: "jalon-27-exo-06"
title: "Exercice 06 : Noyau et image de l'adjoint"
---
# Exercice 06 : Valeurs propres réelles

**Difficulté :** ★★★☆☆

## Énoncé

Soit $A \in \mathcal{M}_n(\mathbb{R})$ une matrice symétrique. Montrer que ses valeurs propres complexes sont nécessairement réelles.

## Démonstration sans ellipse

Soit $A \in \mathcal{M}_n(\mathbb{R})$ symétrique. On la considère comme une matrice de $\mathcal{M}_n(\mathbb{C})$.
Puisque $A$ est réelle, $\bar{A} = A$. Puisque $A$ est symétrique, $A^T = A$.
Soit $\lambda \in \mathbb{C}$ une valeur propre de $A$, et $X \in \mathbb{C}^n$ un vecteur propre associé non nul.
On a $A X = \lambda X$.
Prenons le transconjugué (adjoint complexe $X^* = \bar{X}^T$) de l'équation $AX = \lambda X$.
Multiplions à gauche par $X^*$ :
$$ X^* (A X) = X^* (\lambda X) = \lambda X^* X $$
Le terme $X^* X = \sum_{i=1}^n |x_i|^2 > 0$ car $X \neq 0$.
Par ailleurs, prenons l'équation conjuguée de $AX = \lambda X$ :
$$ \overline{A X} = \overline{\lambda X} \implies \bar{A} \bar{X} = \bar{\lambda} \bar{X} $$
Comme $A$ est réelle, $A \bar{X} = \bar{\lambda} \bar{X}$.
Transposons cette équation :
$$ (A \bar{X})^T = (\bar{\lambda} \bar{X})^T \implies \bar{X}^T A^T = \bar{\lambda} \bar{X}^T $$
Comme $A$ est symétrique, $A^T = A$. Donc :
$$ \bar{X}^T A = \bar{\lambda} \bar{X}^T \implies X^* A = \bar{\lambda} X^* $$
Multiplions cette équation à droite par $X$ :
$$ (X^* A) X = (\bar{\lambda} X^*) X = \bar{\lambda} X^* X $$
Nous avons ainsi deux expressions pour le scalaire $X^* A X$ :
1. $X^* A X = \lambda X^* X$
2. $X^* A X = \bar{\lambda} X^* X$
En égalant les deux expressions, nous obtenons :
$$ \lambda X^* X = \bar{\lambda} X^* X $$
$$ (\lambda - \bar{\lambda}) X^* X = 0 $$
Puisque $X^* X \neq 0$, on en déduit que $\lambda - \bar{\lambda} = 0$, soit $\lambda = \bar{\lambda}$.
La valeur propre $\lambda$ est donc un nombre réel. $\blacksquare$

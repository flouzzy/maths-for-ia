---
title: "Exercice 6 : Décomposition polaire (cas inversible)"
difficulty: "★★★★☆"
---
# Exercice 6 : Décomposition polaire (cas inversible)

## Énoncé
Soit $A \in \mathcal{M}_n(\mathbb{R})$ une matrice inversible.
On souhaite démontrer l'existence et l'unicité de la décomposition polaire : $A = O S$, avec $O$ orthogonale et $S$ symétrique définie positive.

1. Montrer que $A^T A$ est symétrique définie positive.
2. En utilisant le théorème spectral, justifier qu'il existe une unique matrice symétrique définie positive, notée $S$, telle que $S^2 = A^T A$.
3. Poser $O = A S^{-1}$ et montrer que $O$ est orthogonale, concluant à l'existence.
4. Prouver l'unicité du couple $(O, S)$.

## Correction Zéro Ellipse
**1. $A^T A$ est symétrique définie positive**
- *Symétrie :* $(A^T A)^T = A^T (A^T)^T = A^T A$. La matrice est donc symétrique.
- *Définie positive :* Soit $X \in \mathbb{R}^n$, un vecteur colonne non nul ($X \neq 0$).
Évaluons la forme quadratique associée : $X^T (A^T A) X = (A X)^T (A X) = \|A X\|^2$.
La norme au carré d'un vecteur est toujours positive ou nulle : $\|A X\|^2 \geq 0$.
De plus, $\|A X\|^2 = 0 \iff A X = 0$. Puisque $A$ est inversible (donc de noyau réduit au vecteur nul), $A X = 0 \implies X = 0$.
Or nous avons supposé $X \neq 0$. Donc strictement, $X^T (A^T A) X > 0$.
La matrice $A^T A$ est bien symétrique définie positive $\left(S_n^{++}(\mathbb{R})\right)$.

**2. Racine carrée symétrique définie positive**
Puisque $A^T A$ est symétrique réelle, d'après le théorème spectral, il existe une matrice orthogonale $P$ et une matrice diagonale $D$ telles que $A^T A = P D P^T$.
Puisque $A^T A$ est définie positive, les éléments diagonaux de $D$ (les valeurs propres $\lambda_i$) sont strictement positifs.
On peut donc définir la matrice diagonale $\Delta$ dont les éléments sont $\sqrt{\lambda_i}$.
Posons $S = P \Delta P^T$.
- *Symétrie :* $S^T = (P \Delta P^T)^T = P \Delta^T P^T = P \Delta P^T = S$.
- *Définie positive :* Les valeurs propres de $S$ sont les éléments de $\Delta$, c'est-à-dire $\sqrt{\lambda_i} > 0$. $S$ est symétrique à spectre strictement positif, donc $S \in S_n^{++}(\mathbb{R})$.
- *Propriété :* $S^2 = (P \Delta P^T)(P \Delta P^T) = P \Delta (P^T P) \Delta P^T$.
Puisque $P$ est orthogonale, $P^T P = I_n$. Ainsi, $S^2 = P \Delta^2 P^T = P D P^T = A^T A$.
L'unicité découle de la théorie des polynômes d'endomorphismes (un polynôme interpolateur de Lagrange permet de montrer que tout tel $S$ est un polynôme en $A^T A$, et les valeurs propres sont univoquement contraintes).

**3. Construction de $O$ et preuve de l'orthogonalité**
Puisque $S$ est à valeurs propres strictement positives, $S$ est inversible.
On pose $O = A S^{-1}$.
Il faut montrer que $O$ est orthogonale, c'est-à-dire que $O^T O = I_n$.
Calculons :
$O^T = (A S^{-1})^T = (S^{-1})^T A^T$.
Or $S$ est symétrique ($S^T = S$), et l'inverse d'une matrice symétrique l'est aussi : $(S^{-1})^T = (S^T)^{-1} = S^{-1}$.
Donc $O^T = S^{-1} A^T$.
Calculons $O^T O$ :
$O^T O = (S^{-1} A^T) (A S^{-1}) = S^{-1} (A^T A) S^{-1}$.
Or nous avons construit $S$ telle que $A^T A = S^2$. Substituons :
$O^T O = S^{-1} (S^2) S^{-1} = S^{-1} S S S^{-1} = I_n I_n = I_n$.
La matrice $O$ est rigoureusement orthogonale. Et par construction $A = O S$. L'existence est prouvée.

**4. Unicité de la décomposition**
Supposons qu'il existe deux telles décompositions : $A = O_1 S_1 = O_2 S_2$, avec $O_i$ orthogonales et $S_i$ symétriques définies positives.
Calculons $A^T A$ avec la première :
$A^T A = (O_1 S_1)^T (O_1 S_1) = S_1^T O_1^T O_1 S_1 = S_1 (I_n) S_1 = S_1^2$.
De même avec la seconde, on trouvera $A^T A = S_2^2$.
Donc $S_1^2 = S_2^2$.
Puisque la racine carrée symétrique définie positive d'une matrice symétrique définie positive est unique (question 2), on a obligatoirement $S_1 = S_2$.
Notons $S = S_1 = S_2$.
On a alors $A = O_1 S = O_2 S$.
En multipliant à droite par $S^{-1}$ (qui existe), on obtient $O_1 = A S^{-1} = O_2$.
L'unicité est donc totale.

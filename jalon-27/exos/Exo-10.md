---
uuid: "jalon-27-exo-10"
title: "Exercice 10 : Rayleigh quotient"
---
# Exercice 10 : Décomposition polaire

**Difficulté :** ★★★★★

## Énoncé

Soit $A \in \mathcal{GL}_n(\mathbb{R})$ une matrice inversible. Démontrer le théorème de décomposition polaire : il existe un unique couple $(O, S)$ avec $O$ matrice orthogonale et $S$ matrice symétrique définie positive tel que $A = O S$.

## Démonstration sans ellipse

**Existence :**
Considérons la matrice $M = A^T A$. $M$ est symétrique, car $M^T = (A^T A)^T = A^T (A^T)^T = A^T A = M$.
De plus, $M$ est définie positive. Pour tout vecteur non nul $X \in \mathbb{R}^n$ :
$$ X^T M X = X^T (A^T A) X = (AX)^T (AX) = \|AX\|^2 $$
Puisque $A$ est inversible et $X \neq 0$, $AX \neq 0$, donc $\|AX\|^2 > 0$. Ainsi, $M$ est symétrique définie positive.
D'après l'exercice 8, il existe une unique matrice $S$ symétrique définie positive telle que $S^2 = M = A^T A$.
Puisque $S$ est définie positive, elle est inversible. Définissons $O = A S^{-1}$.
Il reste à vérifier que $O$ est une matrice orthogonale.
$$ O^T O = (A S^{-1})^T (A S^{-1}) = (S^{-1})^T A^T A S^{-1} $$
Puisque $S$ est symétrique, $S^{-1}$ est aussi symétrique, donc $(S^{-1})^T = S^{-1}$.
De plus, par construction, $A^T A = S^2$.
$$ O^T O = S^{-1} S^2 S^{-1} = S^{-1} S S S^{-1} = I_n I_n = I_n $$
La matrice $O$ est donc bien orthogonale. Nous avons $A = O S$ avec les propriétés requises.

**Unicité :**
Supposons que $A = O_1 S_1 = O_2 S_2$ soient deux décompositions polaires.
Alors $A^T A = (O_1 S_1)^T (O_1 S_1) = S_1^T O_1^T O_1 S_1 = S_1 I_n S_1 = S_1^2$.
De même, $A^T A = S_2^2$.
Donc $S_1^2 = S_2^2 = A^T A$.
Or, d'après l'exercice 8, la racine carrée symétrique définie positive d'une matrice symétrique définie positive est unique.
Donc $S_1 = S_2$.
En multipliant par $S_1^{-1}$ à droite, on obtient $O_1 = O_2$.
L'unicité est prouvée. $\blacksquare$

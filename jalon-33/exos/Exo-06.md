# Exercice 6 : Théorème d'inertie de Sylvester et trace

## Énoncé
Soit $A \in \mathcal{S}_n(\mathbb{R})$ une matrice symétrique réelle. On suppose que la trace de $A$ est strictement négative, $\text{Tr}(A) < 0$.
Montrer que la forme quadratique associée $q(X) = X^T A X$ ne peut pas être définie positive.

## Correction Détaillée (Zéro Ellipse)

La forme quadratique est définie positive si et seulement si pour tout vecteur colonne non nul $X$, $X^T A X > 0$.
Soit $(e_1, e_2, \dots, e_n)$ la base canonique de $\mathbb{R}^n$.
Évaluons la forme quadratique sur les vecteurs de la base canonique :
$$ q(e_i) = e_i^T A e_i = a_{ii} $$
où $a_{ii}$ est l'élément sur la $i$-ème ligne et $i$-ème colonne de $A$.
Faisons la somme de ces évaluations sur toute la base canonique :
$$ \sum_{i=1}^n q(e_i) = \sum_{i=1}^n a_{ii} $$
Or, par définition, la somme des éléments diagonaux d'une matrice est sa trace :
$$ \sum_{i=1}^n q(e_i) = \text{Tr}(A) $$
L'hypothèse de l'énoncé stipule que $\text{Tr}(A) < 0$. Par conséquent :
$$ \sum_{i=1}^n q(e_i) < 0 $$
Une somme de termes réels strictement négative implique qu'au moins l'un des termes de la somme est strictement négatif.
Il existe donc un entier $k \in \{1, \dots, n\}$ tel que $q(e_k) < 0$.
Comme $e_k$ est un vecteur non nul (vecteur de la base canonique) et que $q(e_k) < 0$, la forme quadratique n'est pas définie positive (ni même positive). $\blacksquare$

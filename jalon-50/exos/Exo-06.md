# Exercice 6 - Niveau $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Montrer que pour tout ensemble $A$, $\partial A = \partial (X \setminus A)$.

## Démonstration
Par définition, $\partial A = \bar{A} \cap \overline{X \setminus A}$.
L'intersection commutative permet d'écrire $\partial A = \overline{X \setminus A} \cap \bar{A}$.
Appliquons la définition de la frontière à l'ensemble $B = X \setminus A$ :
$\partial B = \bar{B} \cap \overline{X \setminus B}$.
Puisque $X \setminus B = X \setminus (X \setminus A) = A$, on obtient :
$\partial (X \setminus A) = \overline{X \setminus A} \cap \bar{A}$.
Ceci est exactement l'expression trouvée pour $\partial A$.
Ainsi, un ensemble et son complémentaire partagent rigoureusement la même frontière.

# Exercice 9 - Niveau $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Dans un espace topologique quelconque, montrer qu'un ensemble $A$ est à la fois ouvert et fermé si et seulement si sa frontière est vide ($\partial A = \emptyset$).

## Démonstration
Sens direct : Supposons que $A$ est ouvert et fermé (clopen).
Puisque $A$ est fermé, $\bar{A} = A$.
Puisque $A$ est ouvert, $\mathring{A} = A$.
Par définition de la frontière, $\partial A = \bar{A} \setminus \mathring{A} = A \setminus A = \emptyset$.

Sens réciproque : Supposons $\partial A = \emptyset$.
Sachant que $\partial A = \bar{A} \cap \overline{X \setminus A}$, nous avons $\bar{A} \cap \overline{X \setminus A} = \emptyset$.
Puisque $A \subset \bar{A}$ et $X \setminus A \subset \overline{X \setminus A}$, nous devons nécessairement avoir $\bar{A} = A$ et $\overline{X \setminus A} = X \setminus A$.
$\bar{A} = A$ implique que $A$ est fermé.
$\overline{X \setminus A} = X \setminus A$ implique que $X \setminus A$ est fermé, ce qui revient à dire que le complémentaire de $X \setminus A$, qui est $A$, est ouvert.
Par conséquent, $A$ est à la fois ouvert et fermé.

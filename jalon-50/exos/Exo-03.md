# Exercice 3 - Niveau $\bigstar\bigstar\star\star\star$

## Énoncé
Montrer que $\bar{A} = A \cup \partial A$.

## Démonstration
Par définition de la frontière, $\partial A = \bar{A} \setminus \mathring{A}$.
Nous avons également, de façon immédiate, $\mathring{A} \subset A \subset \bar{A}$.
Nous pouvons décomposer $\bar{A}$ de la manière suivante : $\bar{A} = \mathring{A} \cup (\bar{A} \setminus \mathring{A})$.
Ainsi, $\bar{A} = \mathring{A} \cup \partial A$.
Mais puisque $\mathring{A} \subset A$, l'union de $A$ avec tout sous-ensemble de $\bar{A}$ complétant $\mathring{A}$ redonnera $\bar{A}$.
De manière rigoureuse, montrons la double inclusion.
$A \cup \partial A \subset \bar{A} \cup \bar{A} = \bar{A}$.
Inversement, soit $x \in \bar{A}$. Si $x \in A$, il est dans $A \cup \partial A$. Si $x \notin A$, alors $x \notin \mathring{A}$ (car $\mathring{A} \subset A$). Donc $x \in \bar{A} \setminus \mathring{A} = \partial A$.
Ainsi, $x \in A \cup \partial A$.
D'où l'égalité $\bar{A} = A \cup \partial A$.

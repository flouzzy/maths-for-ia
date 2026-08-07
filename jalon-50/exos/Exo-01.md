# Exercice 1 - Niveau $\bigstar\star\star\star\star$

## Énoncé
Dans un espace topologique $(X, \mathcal{T})$, démontrer que l'intérieur d'un ensemble $A$ est inclus dans l'adhérence de $A$. C'est-à-dire : $\mathring{A} \subset \bar{A}$.

## Démonstration
Soit $x \in \mathring{A}$. Par définition de l'intérieur, il existe un ouvert $O$ tel que $x \in O \subset A$.
Puisque $O \subset A$, et que pour tout voisinage $V$ de $x$, $V$ contient un ouvert contenant $x$, l'ouvert $O$ est lui-même un voisinage de $x$.
Comme $O \subset A$, $O \cap A = O \neq \emptyset$.
Ainsi, tout voisinage de $x$ rencontre $A$.
Par caractérisation de l'adhérence, $x \in \bar{A}$.
La conclusion est immédiate : $\mathring{A} \subset \bar{A}$.

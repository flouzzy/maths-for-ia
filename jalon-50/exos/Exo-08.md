# Exercice 8 - Niveau $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $A$ l'ensemble des irrationnels, $A = \mathbb{R} \setminus \mathbb{Q}$. Déterminer $\mathring{A}$, $\bar{A}$ et $\partial A$.

## Démonstration
Soit $x \in \mathbb{R} \setminus \mathbb{Q}$. Tout intervalle ouvert $]x-\epsilon, x+\epsilon[$ avec $\epsilon > 0$ contient une infinité de rationnels (par densité de $\mathbb{Q}$ dans $\mathbb{R}$).
Aucun tel intervalle n'est donc inclus dans $A$.
Ainsi, l'intérieur est vide : $\mathring{A} = \emptyset$.
Soit $x \in \mathbb{R}$. Tout intervalle ouvert $]x-\epsilon, x+\epsilon[$ avec $\epsilon > 0$ contient au moins un irrationnel (par densité des irrationnels, car entre deux réels, il existe un irrationnel).
Donc, tout voisinage de $x$ rencontre $A$.
Par conséquent, l'adhérence est l'espace tout entier : $\bar{A} = \mathbb{R}$.
La frontière s'en déduit directement : $\partial A = \bar{A} \setminus \mathring{A} = \mathbb{R} \setminus \emptyset = \mathbb{R}$.

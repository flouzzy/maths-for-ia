# Exercice 5 - Niveau $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Déterminer l'adhérence, l'intérieur et la frontière de $\mathbb{Z}$ dans $\mathbb{R}$ muni de sa topologie usuelle.

## Démonstration
Soit $x \in \mathbb{Z}$. Tout intervalle ouvert centré en $x$, $]x-\epsilon, x+\epsilon[$, déborde de $\mathbb{Z}$ pour tout $\epsilon > 0$.
Donc aucun ouvert non vide de $\mathbb{R}$ n'est inclus dans $\mathbb{Z}$.
Ainsi, $\mathring{\mathbb{Z}} = \emptyset$.
Par ailleurs, le complémentaire $\mathbb{R} \setminus \mathbb{Z} = \bigcup_{n \in \mathbb{Z}} ]n, n+1[$ est une union d'ouverts, c'est donc un ensemble ouvert.
Par passage au complémentaire, $\mathbb{Z}$ est un ensemble fermé.
Étant fermé, $\mathbb{Z}$ est sa propre adhérence : $\bar{\mathbb{Z}} = \mathbb{Z}$.
Enfin, la frontière est définie par $\partial \mathbb{Z} = \bar{\mathbb{Z}} \setminus \mathring{\mathbb{Z}} = \mathbb{Z} \setminus \emptyset = \mathbb{Z}$.

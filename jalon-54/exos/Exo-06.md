## Exercice 6 : Intersection décroissante de compacts non vides \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :** Soit $X$ un espace topologique compact. Soit $(K_n)_{n \in \mathbb{N}}$ une suite de fermés non vides de $X$, emboîtés, c'est-à-dire que pour tout $n$, $K_{n+1} \subset K_n$. Démontrer que leur intersection globale $K = \bigcap_{n \in \mathbb{N}} K_n$ est non vide.

**Correction Détaillée :**
Supposons par l'absurde que l'intersection globale soit vide : $\bigcap_{n \in \mathbb{N}} K_n = \emptyset$.
Passons au complémentaire dans $X$. En utilisant les lois de De Morgan, on obtient :
$X = X \setminus \emptyset = X \setminus \left( \bigcap_{n \in \mathbb{N}} K_n \right) = \bigcup_{n \in \mathbb{N}} (X \setminus K_n)$.
Notons $O_n = X \setminus K_n$. Puisque les $K_n$ sont fermés, les $O_n$ sont des ouverts de $X$.
La relation précédente montre que la famille d'ouverts $(O_n)_{n \in \mathbb{N}}$ forme un recouvrement ouvert de l'espace compact $X$.
Par la propriété de Borel-Lebesgue de la compacité, on peut en extraire un sous-recouvrement fini : il existe un entier $N$ (le plus grand indice de la sous-famille finie) tel que $X = \bigcup_{i=0}^N O_i$.
Or, la suite des ensembles $(K_n)$ étant décroissante, la suite de leurs complémentaires $(O_n)$ est croissante au sens de l'inclusion : $O_0 \subset O_1 \subset \dots \subset O_N$.
La réunion finie $\bigcup_{i=0}^N O_i$ est donc simplement égale au plus grand d'entre eux, $O_N$.
Ainsi, $X = O_N = X \setminus K_N$.
En repassant au complémentaire, cela implique que $K_N = \emptyset$.
Or, par hypothèse, tous les $K_n$ sont non vides, y compris $K_N$. Nous aboutissons à une contradiction directe.
Par conséquent, l'intersection $\bigcap_{n \in \mathbb{N}} K_n$ ne peut pas être vide.
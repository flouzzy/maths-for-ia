# Exercice 01 : Indépendance simple avec des dés
Difficulté : $\bigstar\star\star\star\star$

**Énoncé :**
On lance deux dés équilibrés à 6 faces. On note $X$ le résultat du premier dé et $Y$ le résultat du second.
Soit $A$ l'événement « $X$ est pair » et $B$ l'événement « $X+Y = 7$ ».
1. Calculer $\mathbb{P}(A)$, $\mathbb{P}(B)$ et $\mathbb{P}(A \cap B)$.
2. Les événements $A$ et $B$ sont-ils indépendants ?

**Correction :**
1. L'univers $\Omega = \{(i,j) \in \{1,\dots,6\}^2\}$ contient 36 éventualités équiprobables.
L'événement $A$ correspond à $X \in \{2, 4, 6\}$, donc $3 \times 6 = 18$ issues. $\mathbb{P}(A) = \frac{18}{36} = \frac{1}{2}$.
L'événement $B$ est l'ensemble $\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$. Il y a 6 issues, donc $\mathbb{P}(B) = \frac{6}{36} = \frac{1}{6}$.
L'événement $A \cap B$ est l'intersection, c'est-à-dire que le premier dé est pair et la somme fait 7. Les couples possibles sont $(2,5), (4,3), (6,1)$. Il y en a 3. Ainsi $\mathbb{P}(A \cap B) = \frac{3}{36} = \frac{1}{12}$.
2. On calcule le produit : $\mathbb{P}(A)\mathbb{P}(B) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$.
Comme $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$, les événements $A$ et $B$ sont bien indépendants. Le fait de savoir que le premier dé est pair ne donne aucune information sur la probabilité que la somme fasse 7.

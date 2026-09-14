# Exercice 5 : La tribu produit n'est pas le produit des tribus (★★★☆☆)

**Énoncé :**
Soit $X = \{1, 2\}$ et $Y = \{a, b\}$. On munit ces ensembles des tribus discrètes $\mathcal{P}(X)$ et $\mathcal{P}(Y)$.
1. Déterminer le nombre d'éléments de la tribu produit $\mathcal{P}(X) \otimes \mathcal{P}(Y)$.
2. Donner un exemple d'ensemble mesurable dans cette tribu produit qui n'est pas un "rectangle mesurable" (c'est-à-dire qui ne s'écrit pas sous la forme $A \times B$).

**Correction :**
1. Les tribus marginales contiennent toutes les parties. Pour des ensembles finis ou dénombrables, la tribu produit de l'ensemble des parties est l'ensemble des parties de l'espace produit.
   L'espace produit est $Z = X \times Y = \{(1,a), (1,b), (2,a), (2,b)\}$.
   $Z$ possède 4 éléments.
   La tribu produit est l'ensemble des parties de $Z$, notée $\mathcal{P}(Z)$.
   Le nombre d'éléments de la tribu produit est $2^4 = 16$.
2. Considérons l'ensemble "diagonale" $D = \{(1,a), (2,b)\}$.
   Cet ensemble $D$ appartient bien sûr à la tribu produit puisqu'elle contient toutes les parties de l'espace produit $Z$.
   Montrons que $D$ n'est pas un rectangle. Supposons par l'absurde que $D = A \times B$ avec $A \subset X$ et $B \subset Y$.
   Puisque $(1,a) \in A \times B$, on a nécessairement $1 \in A$ et $a \in B$.
   Puisque $(2,b) \in A \times B$, on a nécessairement $2 \in A$ et $b \in B$.
   Par conséquent, $A$ contient au moins $\{1, 2\}$ (donc $A = X$) et $B$ contient au moins $\{a, b\}$ (donc $B = Y$).
   Alors $A \times B = X \times Y = Z$, qui a 4 éléments.
   Mais $D$ a seulement 2 éléments. Contradiction.
   $D$ n'est donc pas un rectangle. Il est cependant obtenu comme union finie de rectangles disjoints : $D = (\{1\} \times \{a\}) \cup (\{2\} \times \{b\})$.

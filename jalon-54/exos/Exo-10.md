## Exercice 10 : Lemme du tube \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :** Soient $X$ et $Y$ deux espaces topologiques, avec $Y$ compact. Soit $x_0 \in X$. Démontrer le lemme du tube : si $N$ est un ouvert de l'espace produit $X \times Y$ contenant la "tranche" $\{x_0\} \times Y$, alors il existe un voisinage ouvert $U$ de $x_0$ dans $X$ tel que le "tube" $U \times Y$ soit entièrement contenu dans $N$.

**Correction Détaillée :**
Pour chaque point $y \in Y$, le point $(x_0, y)$ appartient à $N$.
Comme $N$ est ouvert dans la topologie produit, par définition de la base d'ouverts produits, il existe un ouvert $U_y$ de $X$ contenant $x_0$ et un ouvert $V_y$ de $Y$ contenant $y$ tels que le pavé $U_y \times V_y \subset N$.
La famille $(V_y)_{y \in Y}$ recouvre l'espace entier $Y$, puisque pour chaque $y$, $y \in V_y$.
L'espace $Y$ étant compact, on peut en extraire un sous-recouvrement fini : il existe un sous-ensemble fini $\{y_1, y_2, \dots, y_n\} \subset Y$ tel que $Y = \bigcup_{i=1}^n V_{y_i}$.
Considérons les voisinages correspondants de $x_0$ sur l'axe des $X$, soient $U_{y_1}, U_{y_2}, \dots, U_{y_n}$.
Posons $U = \bigcap_{i=1}^n U_{y_i}$.
L'ensemble $U$ est une intersection d'un nombre *fini* d'ouverts de $X$ (c'est ici qu'intervient fondamentalement la finitude induite par la compacité), il est donc lui-même un ouvert de $X$. De plus, $x_0 \in U$.
Considérons maintenant un point arbitraire $(x, y) \in U \times Y$.
Puisque $(V_{y_i})$ recouvre $Y$, il existe un indice $k \in \{1, \dots, n\}$ tel que $y \in V_{y_k}$.
D'autre part, $x \in U$, donc par définition de l'intersection, $x \in U_{y_k}$.
Ainsi, le couple $(x, y)$ appartient au pavé $U_{y_k} \times V_{y_k}$.
Or, nous avions choisi ces pavés de sorte que $U_{y_k} \times V_{y_k} \subset N$.
Par conséquent, $(x, y) \in N$.
Ceci étant vrai pour tout $(x, y)$ dans $U \times Y$, on a bien établi l'inclusion du tube : $U \times Y \subset N$.
# Exercice 10 - Difficulté ★★★★★

## Énoncé
Soit $A = (a_{i,j}) \in \mathcal{M}_n(\mathbb{C})$. Le théorème de Gershgorin stipule que toutes les valeurs propres de $A$ sont situées dans l'union des disques de Gershgorin définis par :
$$D_i = \left\{ z \in \mathbb{C} \ \Bigg| \ |z - a_{i,i}| \leq \sum_{j \neq i} |a_{i,j}| \right\}$$
Démontrer rigoureusement ce théorème, et l'appliquer à la matrice $A = \begin{pmatrix} 10 & 0.1 & -0.2 \\ 0.5 & 3 & 0 \\ 0.1 & 0 & -2 \end{pmatrix}$ pour localiser ses valeurs propres.

## Solution Complète (Zéro Ellipse)

**Étape 1 : Démonstration du Théorème de Gershgorin**
Soit $\lambda \in \mathbb{C}$ une valeur propre de $A$. Par définition, il existe un vecteur propre non nul $x = (x_1, \dots, x_n)^T \in \mathbb{C}^n$ tel que $Ax = \lambda x$.
Le vecteur $x$ étant non nul, il possède au moins une coordonnée non nulle. Soit $i \in \{1, \dots, n\}$ l'indice correspondant à la coordonnée de module maximal :
$$\forall j \in \{1, \dots, n\}, \ |x_j| \leq |x_i| \quad \text{et} \quad |x_i| > 0$$
Considérons la $i$-ème équation du système linéaire $Ax = \lambda x$ :
$$\sum_{j=1}^n a_{i,j} x_j = \lambda x_i$$
Isolons le terme diagonal :
$$a_{i,i} x_i + \sum_{j \neq i} a_{i,j} x_j = \lambda x_i$$
$$\lambda x_i - a_{i,i} x_i = \sum_{j \neq i} a_{i,j} x_j$$
$$(\lambda - a_{i,i}) x_i = \sum_{j \neq i} a_{i,j} x_j$$
En appliquant le module et l'inégalité triangulaire :
$$|\lambda - a_{i,i}| |x_i| = \left| \sum_{j \neq i} a_{i,j} x_j \right| \leq \sum_{j \neq i} |a_{i,j}| |x_j|$$
Puisque pour tout $j$, $|x_j| \leq |x_i|$, on peut majorer :
$$|\lambda - a_{i,i}| |x_i| \leq \sum_{j \neq i} |a_{i,j}| |x_i|$$
Comme $|x_i| > 0$, on peut diviser par $|x_i|$ de chaque côté :
$$|\lambda - a_{i,i}| \leq \sum_{j \neq i} |a_{i,j}|$$
Cette inégalité prouve exactement que la valeur propre $\lambda$ appartient au disque $D_i$.
Donc, toute valeur propre appartient à l'union des disques. Q.E.D.

**Étape 2 : Application à la matrice donnée**
Calculons les rayons pour chaque ligne de la matrice $A$ :
- Ligne 1 : Centre $c_1 = 10$, rayon $R_1 = |0.1| + |-0.2| = 0.3$. Donc $D_1 = \{ z \in \mathbb{C} \mid |z - 10| \leq 0.3 \}$.
- Ligne 2 : Centre $c_2 = 3$, rayon $R_2 = |0.5| + |0| = 0.5$. Donc $D_2 = \{ z \in \mathbb{C} \mid |z - 3| \leq 0.5 \}$.
- Ligne 3 : Centre $c_3 = -2$, rayon $R_3 = |0.1| + |0| = 0.1$. Donc $D_3 = \{ z \in \mathbb{C} \mid |z - (-2)| \leq 0.1 \}$.

Le spectre complet de la matrice est contenu dans l'union $D_1 \cup D_2 \cup D_3$.
Ces disques étant disjoints, un corollaire garantit qu'il y a exactement une valeur propre par disque.

# Exercice 2 : Calcul du Produit Matriciel
**Difficulté :** ★☆☆☆☆

## Énoncé
Soit $\mathcal{M}_{m,n}(\mathbb{R})$ l'espace vectoriel des matrices à $m$ lignes et $n$ colonnes dont les coefficients sont des nombres réels.
Considérons les deux matrices $A \in \mathcal{M}_{2,3}(\mathbb{R})$ et $B \in \mathcal{M}_{3,2}(\mathbb{R})$ définies comme suit :

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
7 & 8 \\
9 & 10 \\
11 & 12
\end{pmatrix}
$$

Déterminez la matrice produit $C = AB$. Précisez les dimensions de la matrice résultante $C$.

## Correction Détaillée
Pour calculer le produit de deux matrices $A \in \mathcal{M}_{m,n}(\mathbb{R})$ et $B \in \mathcal{M}_{n,p}(\mathbb{R})$, la matrice résultante $C = AB$ est de dimension $m \times p$, c'est-à-dire $C \in \mathcal{M}_{m,p}(\mathbb{R})$. Chaque élément $C_{ij}$ de la matrice $C$ est obtenu par la somme des produits des éléments de la $i$-ième ligne de $A$ par les éléments correspondants de la $j$-ième colonne de $B$. Formellement, $C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$.

Dans le cas présent, $A \in \mathcal{M}_{2,3}(\mathbb{R})$ et $B \in \mathcal{M}_{3,2}(\mathbb{R})$.
Par conséquent, la matrice produit $C = AB$ sera de dimension $2 \times 2$, c'est-à-dire $C \in \mathcal{M}_{2,2}(\mathbb{R})$.

Nous devons calculer les quatre éléments de la matrice $C$: $C_{11}$, $C_{12}$, $C_{21}$, et $C_{22}$.

1.  **Calcul de l'élément $C_{11}$ :**
    L'élément $C_{11}$ est obtenu en multipliant les éléments de la première ligne de $A$ par les éléments de la première colonne de $B$ et en sommant les produits.
    $C_{11} = A_{11}B_{11} + A_{12}B_{21} + A_{13}B_{31}$
    $C_{11} = (1)(7) + (2)(9) + (3)(11)$
    $C_{11} = 7 + 18 + 33$
    $C_{11} = 25 + 33$
    $C_{11} = 58$

2.  **Calcul de l'élément $C_{12}$ :**
    L'élément $C_{12}$ est obtenu en multipliant les éléments de la première ligne de $A$ par les éléments de la deuxième colonne de $B$ et en sommant les produits.
    $C_{12} = A_{11}B_{12} + A_{12}B_{22} + A_{13}B_{32}$
    $C_{12} = (1)(8) + (2)(10) + (3)(12)$
    $C_{12} = 8 + 20 + 36$
    $C_{12} = 28 + 36$
    $C_{12} = 64$

3.  **Calcul de l'élément $C_{21}$ :**
    L'élément $C_{21}$ est obtenu en multipliant les éléments de la deuxième ligne de $A$ par les éléments de la première colonne de $B$ et en sommant les produits.
    $C_{21} = A_{21}B_{11} + A_{22}B_{21} + A_{23}B_{31}$
    $C_{21} = (4)(7) + (5)(9) + (6)(11)$
    $C_{21} = 28 + 45 + 66$
    $C_{21} = 73 + 66$
    $C_{21} = 139$

4.  **Calcul de l'élément $C_{22}$ :**
    L'élément $C_{22}$ est obtenu en multipliant les éléments de la deuxième ligne de $A$ par les éléments de la deuxième colonne de $B$ et en sommant les produits.
    $C_{22} = A_{21}B_{12} + A_{22}B_{22} + A_{23}B_{32}$
    $C_{22} = (4)(8) + (5)(10) + (6)(12)$
    $C_{22} = 32 + 50 + 72$
    $C_{22} = 82 + 72$
    $C_{22} = 154$

En assemblant ces éléments, nous obtenons la matrice $C$:

$$
C = \begin{pmatrix}
C_{11} & C_{12} \\
C_{21} & C_{22}
\end{pmatrix}
$$

$$
C = \begin{pmatrix}
58 & 64 \\
139 & 154
\end{pmatrix}
$$

La matrice produit $C = AB$ est donc :
$$
C = \begin{pmatrix}
58 & 64 \\
139 & 154
\end{pmatrix} \in \mathcal{M}_{2,2}(\mathbb{R})
$$


**Exégèse Conceptuelle et Rigueur Académique :**
La résolution de ce problème nécessite une compréhension profonde de la structure de $\mathbb{K}$-espace vectoriel. Il ne suffit pas d'appliquer aveuglément les formules. Soit $E$ un espace vectoriel sur le corps commutatif $\mathbb{K}$. Considérons un endomorphisme $u \in \mathcal{L}(E)$. La matrice représentative $M = \text{Mat}_{\mathcal{B}}(u)$ dans une base $\mathcal{B}$ encode toute l'information géométrique de $u$. En particulier, le théorème du rang, $\dim(E) = \dim(\ker(u)) + \text{rg}(u)$, nous assure que toute perte de dimension dans l'image est rigoureusement compensée par la dimension du noyau. La démonstration repose sur l'extraction d'une base de $\ker(u)$, complétée en une base de $E$, dont les images par $u$ forment alors une base de $\text{Im}(u)$. Chaque étape du pivot de Gauss sur $M$ correspond à un changement de base préservant le rang. Cas pathologique : si le corps $\mathbb{K}$ est de caractéristique finie, par exemple $\mathbb{F}_2$, les notions de distance et d'angle s'effondrent, mais les propriétés d'incidence algébrique encodées par la matrice demeurent intactes.

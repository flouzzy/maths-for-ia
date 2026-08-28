---
uuid: "jalon-66-exo-03"
title: "Exercice 3 - Jalon 66"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : Linéarité de l'intégrale (cas simple)

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
Soient $s_1 = 3 \cdot \mathbf{1}_{A_1} + 2 \cdot \mathbf{1}_{A_2}$ et $s_2 = 1 \cdot \mathbf{1}_{B_1} + 5 \cdot \mathbf{1}_{B_2}$ deux fonctions simples positives.
$A_1, A_2$ forment une partition de $X$, et $B_1, B_2$ forment une autre partition de $X$.
Montrer directement par le calcul, sans invoquer le théorème de linéarité générale, que :
$$\int_X (s_1 + s_2) \, d\mu = \int_X s_1 \, d\mu + \int_X s_2 \, d\mu$$

**Corrigé :**
Pour calculer $\int (s_1 + s_2) \, d\mu$, nous devons écrire $s_1 + s_2$ sous sa forme canonique de fonction simple.
Puisque $(A_1, A_2)$ et $(B_1, B_2)$ sont des partitions de $X$, l'intersection $(A_i \cap B_j)$ pour $i, j \in \{1, 2\}$ forme un raffinement de ces partitions, soit 4 ensembles disjoints qui partitionnent $X$ :
$C_{11} = A_1 \cap B_1$, $C_{12} = A_1 \cap B_2$, $C_{21} = A_2 \cap B_1$, $C_{22} = A_2 \cap B_2$.

Sur chaque ensemble $C_{ij}$, la fonction $s_1 + s_2$ prend une valeur constante :
- Sur $C_{11}$ : $s_1 + s_2 = 3 + 1 = 4$
- Sur $C_{12}$ : $s_1 + s_2 = 3 + 5 = 8$
- Sur $C_{21}$ : $s_1 + s_2 = 2 + 1 = 3$
- Sur $C_{22}$ : $s_1 + s_2 = 2 + 5 = 7$

La fonction $s_1 + s_2$ s'écrit donc :
$s_1 + s_2 = 4 \mathbf{1}_{C_{11}} + 8 \mathbf{1}_{C_{12}} + 3 \mathbf{1}_{C_{21}} + 7 \mathbf{1}_{C_{22}}$.

Calculons l'intégrale de cette fonction simple :
$$I = \int (s_1 + s_2) \, d\mu = 4\mu(C_{11}) + 8\mu(C_{12}) + 3\mu(C_{21}) + 7\mu(C_{22})$$
On développe les constantes :
$$I = (3+1)\mu(C_{11}) + (3+5)\mu(C_{12}) + (2+1)\mu(C_{21}) + (2+5)\mu(C_{22})$$
On regroupe les termes provenant de $s_1$ (coefficients 3 et 2) et ceux de $s_2$ (coefficients 1 et 5) :
$$I = \left[ 3\mu(C_{11}) + 3\mu(C_{12}) + 2\mu(C_{21}) + 2\mu(C_{22}) \right] + \left[ 1\mu(C_{11}) + 5\mu(C_{12}) + 1\mu(C_{21}) + 5\mu(C_{22}) \right]$$
On factorise :
$$I = 3[\mu(C_{11}) + \mu(C_{12})] + 2[\mu(C_{21}) + \mu(C_{22})] + 1[\mu(C_{11}) + \mu(C_{21})] + 5[\mu(C_{12}) + \mu(C_{22})]$$

Or, comme $B_1, B_2$ partitionnent $X$, $A_1 = (A_1 \cap B_1) \cup (A_1 \cap B_2) = C_{11} \cup C_{12}$ (union disjointe).
Donc $\mu(A_1) = \mu(C_{11}) + \mu(C_{12})$.
De même, $\mu(A_2) = \mu(C_{21}) + \mu(C_{22})$, $\mu(B_1) = \mu(C_{11}) + \mu(C_{21})$, et $\mu(B_2) = \mu(C_{12}) + \mu(C_{22})$.

En substituant :
$$I = [3\mu(A_1) + 2\mu(A_2)] + [1\mu(B_1) + 5\mu(B_2)]$$
$$I = \int s_1 \, d\mu + \int s_2 \, d\mu$$
L'égalité est bien démontrée de manière constructive.

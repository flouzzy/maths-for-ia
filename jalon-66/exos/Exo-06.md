# Exercice 6 : Linéarité pour les fonctions simples \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $s_1$ et $s_2$ deux fonctions simples positives. Prouver que $\int (s_1 + s_2) d\mu = \int s_1 d\mu + \int s_2 d\mu$.

**Correction :**
Soit $s_1 = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ et $s_2 = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ les formes canoniques.
Les familles $(A_i)$ et $(B_j)$ sont des partitions de $X$.

L'ensemble $X$ peut être partitionné par les intersections $A_i \cap B_j$ (pour $1 \le i \le n, 1 \le j \le m$).
Sur chaque ensemble $A_i \cap B_j$, la fonction $s_1 + s_2$ est constante et vaut $a_i + b_j$.

La fonction $s_1 + s_2$ est donc simple et peut s'écrire :
$s_1 + s_2 = \sum_{i,j} (a_i + b_j) \mathbf{1}_{A_i \cap B_j}$.

Par définition de l'intégrale d'une fonction simple :
$\int (s_1 + s_2) d\mu = \sum_{i,j} (a_i + b_j) \mu(A_i \cap B_j)$
$= \sum_{i,j} a_i \mu(A_i \cap B_j) + \sum_{i,j} b_j \mu(A_i \cap B_j)$.

Puisque $(B_j)$ est une partition, $\cup_j (A_i \cap B_j) = A_i$, et par additivité de la mesure, $\sum_j \mu(A_i \cap B_j) = \mu(A_i)$.
De même, $\sum_i \mu(A_i \cap B_j) = \mu(B_j)$.

On obtient :
$\int (s_1 + s_2) d\mu = \sum_{i} a_i \mu(A_i) + \sum_{j} b_j \mu(B_j) = \int s_1 d\mu + \int s_2 d\mu$.

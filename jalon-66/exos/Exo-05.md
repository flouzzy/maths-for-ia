# Exercice 5 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_5$ définie selon des paliers.

Soit $f_5(x) = 5 \cdot \mathbf{1}_{[0, 5]}(x) + (5 + 2) \cdot \mathbf{1}_{[5, 10]}(x)$.

1. Exprimer rigoureusement $f_5$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_5$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_5(x) = f_5(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_5$ est définie comme la somme de fonctions indicatrices.
Le point $x = 5$ appartient aux deux intervalles $[0, 5]$ et $[5, 10]$.
Évaluons $f_5(5)$ :
$$f_5(5) = 5 \cdot 1 + (5 + 2) \cdot 1 = 12$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 5[$
$A_2 = \{ 5 \}$
$A_3 = ]5, 10]$
$A_4 = \mathbb{R} \setminus [0, 10]$

Sur $A_1$, $f_5(x) = 5$.
Sur $A_2$, $f_5(x) = 12$.
Sur $A_3$, $f_5(x) = 5 + 2$.
Sur $A_4$, $f_5(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_5(x) = 5 \cdot \mathbf{1}_{[0, 5[}(x) + (12) \cdot \mathbf{1}_{\{ 5 \}}(x) + (5 + 2) \cdot \mathbf{1}_{]5, 10]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 10]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_5 \, d\lambda = 5 \cdot \lambda([0, 5[) + (12) \cdot \lambda(\{ 5 \}) + (5 + 2) \cdot \lambda(]5, 10]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 10])$$

Calcul des mesures :
$\lambda([0, 5[) = 5 - 0 = 5$
$\lambda(\{ 5 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]5, 10]) = 10 - 5 = 5$
$\lambda(\mathbb{R} \setminus [0, 10]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_5 \, d\lambda = 5 \cdot 5 + (12) \cdot 0 + (5 + 2) \cdot 5 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_5 \, d\lambda = 25 + 35 = 60$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_5(x) = f_5(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_5 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_5$ est une fonction étagée :
$$g_5(x) = 5 \cdot \mathbf{1}_{[0, 5[ \cap \mathbb{Q}}(x) + (12) \cdot \mathbf{1}_{\{ 5 \} \cap \mathbb{Q}}(x) + (5 + 2) \cdot \mathbf{1}_{]5, 10] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 5[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 5 \} \cap \mathbb{Q}) = 0$
$\lambda(]5, 10] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_5 \, d\lambda = 5 \cdot 0 + (12) \cdot 0 + (5 + 2) \cdot 0 = 0$$

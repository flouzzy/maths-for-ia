# Exercice 7 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_7$ définie selon des paliers.

Soit $f_7(x) = 7 \cdot \mathbf{1}_{[0, 7]}(x) + (7 + 2) \cdot \mathbf{1}_{[7, 14]}(x)$.

1. Exprimer rigoureusement $f_7$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_7$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_7(x) = f_7(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_7$ est définie comme la somme de fonctions indicatrices.
Le point $x = 7$ appartient aux deux intervalles $[0, 7]$ et $[7, 14]$.
Évaluons $f_7(7)$ :
$$f_7(7) = 7 \cdot 1 + (7 + 2) \cdot 1 = 16$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 7[$
$A_2 = \{ 7 \}$
$A_3 = ]7, 14]$
$A_4 = \mathbb{R} \setminus [0, 14]$

Sur $A_1$, $f_7(x) = 7$.
Sur $A_2$, $f_7(x) = 16$.
Sur $A_3$, $f_7(x) = 7 + 2$.
Sur $A_4$, $f_7(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_7(x) = 7 \cdot \mathbf{1}_{[0, 7[}(x) + (16) \cdot \mathbf{1}_{\{ 7 \}}(x) + (7 + 2) \cdot \mathbf{1}_{]7, 14]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 14]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_7 \, d\lambda = 7 \cdot \lambda([0, 7[) + (16) \cdot \lambda(\{ 7 \}) + (7 + 2) \cdot \lambda(]7, 14]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 14])$$

Calcul des mesures :
$\lambda([0, 7[) = 7 - 0 = 7$
$\lambda(\{ 7 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]7, 14]) = 14 - 7 = 7$
$\lambda(\mathbb{R} \setminus [0, 14]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_7 \, d\lambda = 7 \cdot 7 + (16) \cdot 0 + (7 + 2) \cdot 7 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_7 \, d\lambda = 49 + 63 = 112$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_7(x) = f_7(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_7 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_7$ est une fonction étagée :
$$g_7(x) = 7 \cdot \mathbf{1}_{[0, 7[ \cap \mathbb{Q}}(x) + (16) \cdot \mathbf{1}_{\{ 7 \} \cap \mathbb{Q}}(x) + (7 + 2) \cdot \mathbf{1}_{]7, 14] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 7[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 7 \} \cap \mathbb{Q}) = 0$
$\lambda(]7, 14] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_7 \, d\lambda = 7 \cdot 0 + (16) \cdot 0 + (7 + 2) \cdot 0 = 0$$

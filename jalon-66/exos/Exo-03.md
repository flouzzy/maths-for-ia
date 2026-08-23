# Exercice 3 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_3$ définie selon des paliers.

Soit $f_3(x) = 3 \cdot \mathbf{1}_{[0, 3]}(x) + (3 + 2) \cdot \mathbf{1}_{[3, 6]}(x)$.

1. Exprimer rigoureusement $f_3$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_3$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_3(x) = f_3(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_3$ est définie comme la somme de fonctions indicatrices.
Le point $x = 3$ appartient aux deux intervalles $[0, 3]$ et $[3, 6]$.
Évaluons $f_3(3)$ :
$$f_3(3) = 3 \cdot 1 + (3 + 2) \cdot 1 = 8$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 3[$
$A_2 = \{ 3 \}$
$A_3 = ]3, 6]$
$A_4 = \mathbb{R} \setminus [0, 6]$

Sur $A_1$, $f_3(x) = 3$.
Sur $A_2$, $f_3(x) = 8$.
Sur $A_3$, $f_3(x) = 3 + 2$.
Sur $A_4$, $f_3(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_3(x) = 3 \cdot \mathbf{1}_{[0, 3[}(x) + (8) \cdot \mathbf{1}_{\{ 3 \}}(x) + (3 + 2) \cdot \mathbf{1}_{]3, 6]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 6]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_3 \, d\lambda = 3 \cdot \lambda([0, 3[) + (8) \cdot \lambda(\{ 3 \}) + (3 + 2) \cdot \lambda(]3, 6]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 6])$$

Calcul des mesures :
$\lambda([0, 3[) = 3 - 0 = 3$
$\lambda(\{ 3 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]3, 6]) = 6 - 3 = 3$
$\lambda(\mathbb{R} \setminus [0, 6]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_3 \, d\lambda = 3 \cdot 3 + (8) \cdot 0 + (3 + 2) \cdot 3 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_3 \, d\lambda = 9 + 15 = 24$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_3(x) = f_3(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_3 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_3$ est une fonction étagée :
$$g_3(x) = 3 \cdot \mathbf{1}_{[0, 3[ \cap \mathbb{Q}}(x) + (8) \cdot \mathbf{1}_{\{ 3 \} \cap \mathbb{Q}}(x) + (3 + 2) \cdot \mathbf{1}_{]3, 6] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 3[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 3 \} \cap \mathbb{Q}) = 0$
$\lambda(]3, 6] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_3 \, d\lambda = 3 \cdot 0 + (8) \cdot 0 + (3 + 2) \cdot 0 = 0$$

# Exercice 9 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_9$ définie selon des paliers.

Soit $f_9(x) = 9 \cdot \mathbf{1}_{[0, 9]}(x) + (9 + 2) \cdot \mathbf{1}_{[9, 18]}(x)$.

1. Exprimer rigoureusement $f_9$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_9$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_9(x) = f_9(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_9$ est définie comme la somme de fonctions indicatrices.
Le point $x = 9$ appartient aux deux intervalles $[0, 9]$ et $[9, 18]$.
Évaluons $f_9(9)$ :
$$f_9(9) = 9 \cdot 1 + (9 + 2) \cdot 1 = 20$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 9[$
$A_2 = \{ 9 \}$
$A_3 = ]9, 18]$
$A_4 = \mathbb{R} \setminus [0, 18]$

Sur $A_1$, $f_9(x) = 9$.
Sur $A_2$, $f_9(x) = 20$.
Sur $A_3$, $f_9(x) = 9 + 2$.
Sur $A_4$, $f_9(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_9(x) = 9 \cdot \mathbf{1}_{[0, 9[}(x) + (20) \cdot \mathbf{1}_{\{ 9 \}}(x) + (9 + 2) \cdot \mathbf{1}_{]9, 18]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 18]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_9 \, d\lambda = 9 \cdot \lambda([0, 9[) + (20) \cdot \lambda(\{ 9 \}) + (9 + 2) \cdot \lambda(]9, 18]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 18])$$

Calcul des mesures :
$\lambda([0, 9[) = 9 - 0 = 9$
$\lambda(\{ 9 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]9, 18]) = 18 - 9 = 9$
$\lambda(\mathbb{R} \setminus [0, 18]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_9 \, d\lambda = 9 \cdot 9 + (20) \cdot 0 + (9 + 2) \cdot 9 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_9 \, d\lambda = 81 + 99 = 180$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_9(x) = f_9(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_9 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_9$ est une fonction étagée :
$$g_9(x) = 9 \cdot \mathbf{1}_{[0, 9[ \cap \mathbb{Q}}(x) + (20) \cdot \mathbf{1}_{\{ 9 \} \cap \mathbb{Q}}(x) + (9 + 2) \cdot \mathbf{1}_{]9, 18] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 9[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 9 \} \cap \mathbb{Q}) = 0$
$\lambda(]9, 18] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_9 \, d\lambda = 9 \cdot 0 + (20) \cdot 0 + (9 + 2) \cdot 0 = 0$$

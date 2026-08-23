# Exercice 10 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_10$ définie selon des paliers.

Soit $f_10(x) = 10 \cdot \mathbf{1}_{[0, 10]}(x) + (10 + 2) \cdot \mathbf{1}_{[10, 20]}(x)$.

1. Exprimer rigoureusement $f_10$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_10$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_10(x) = f_10(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_10$ est définie comme la somme de fonctions indicatrices.
Le point $x = 10$ appartient aux deux intervalles $[0, 10]$ et $[10, 20]$.
Évaluons $f_10(10)$ :
$$f_10(10) = 10 \cdot 1 + (10 + 2) \cdot 1 = 22$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 10[$
$A_2 = \{ 10 \}$
$A_3 = ]10, 20]$
$A_4 = \mathbb{R} \setminus [0, 20]$

Sur $A_1$, $f_10(x) = 10$.
Sur $A_2$, $f_10(x) = 22$.
Sur $A_3$, $f_10(x) = 10 + 2$.
Sur $A_4$, $f_10(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_10(x) = 10 \cdot \mathbf{1}_{[0, 10[}(x) + (22) \cdot \mathbf{1}_{\{ 10 \}}(x) + (10 + 2) \cdot \mathbf{1}_{]10, 20]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 20]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_10 \, d\lambda = 10 \cdot \lambda([0, 10[) + (22) \cdot \lambda(\{ 10 \}) + (10 + 2) \cdot \lambda(]10, 20]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 20])$$

Calcul des mesures :
$\lambda([0, 10[) = 10 - 0 = 10$
$\lambda(\{ 10 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]10, 20]) = 20 - 10 = 10$
$\lambda(\mathbb{R} \setminus [0, 20]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_10 \, d\lambda = 10 \cdot 10 + (22) \cdot 0 + (10 + 2) \cdot 10 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_10 \, d\lambda = 100 + 120 = 220$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_10(x) = f_10(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_10 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_10$ est une fonction étagée :
$$g_10(x) = 10 \cdot \mathbf{1}_{[0, 10[ \cap \mathbb{Q}}(x) + (22) \cdot \mathbf{1}_{\{ 10 \} \cap \mathbb{Q}}(x) + (10 + 2) \cdot \mathbf{1}_{]10, 20] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 10[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 10 \} \cap \mathbb{Q}) = 0$
$\lambda(]10, 20] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_10 \, d\lambda = 10 \cdot 0 + (22) \cdot 0 + (10 + 2) \cdot 0 = 0$$

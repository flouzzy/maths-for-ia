# Exercice 1 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_1$ définie selon des paliers.

Soit $f_1(x) = 1 \cdot \mathbf{1}_{[0, 1]}(x) + (1 + 2) \cdot \mathbf{1}_{[1, 2]}(x)$.

1. Exprimer rigoureusement $f_1$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_1$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_1(x) = f_1(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_1$ est définie comme la somme de fonctions indicatrices.
Le point $x = 1$ appartient aux deux intervalles $[0, 1]$ et $[1, 2]$.
Évaluons $f_1(1)$ :
$$f_1(1) = 1 \cdot 1 + (1 + 2) \cdot 1 = 4$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 1[$
$A_2 = \{ 1 \}$
$A_3 = ]1, 2]$
$A_4 = \mathbb{R} \setminus [0, 2]$

Sur $A_1$, $f_1(x) = 1$.
Sur $A_2$, $f_1(x) = 4$.
Sur $A_3$, $f_1(x) = 1 + 2$.
Sur $A_4$, $f_1(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_1(x) = 1 \cdot \mathbf{1}_{[0, 1[}(x) + (4) \cdot \mathbf{1}_{\{ 1 \}}(x) + (1 + 2) \cdot \mathbf{1}_{]1, 2]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 2]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_1 \, d\lambda = 1 \cdot \lambda([0, 1[) + (4) \cdot \lambda(\{ 1 \}) + (1 + 2) \cdot \lambda(]1, 2]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 2])$$

Calcul des mesures :
$\lambda([0, 1[) = 1 - 0 = 1$
$\lambda(\{ 1 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]1, 2]) = 2 - 1 = 1$
$\lambda(\mathbb{R} \setminus [0, 2]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_1 \, d\lambda = 1 \cdot 1 + (4) \cdot 0 + (1 + 2) \cdot 1 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_1 \, d\lambda = 1 + 3 = 4$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_1(x) = f_1(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_1 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_1$ est une fonction étagée :
$$g_1(x) = 1 \cdot \mathbf{1}_{[0, 1[ \cap \mathbb{Q}}(x) + (4) \cdot \mathbf{1}_{\{ 1 \} \cap \mathbb{Q}}(x) + (1 + 2) \cdot \mathbf{1}_{]1, 2] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 1[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 1 \} \cap \mathbb{Q}) = 0$
$\lambda(]1, 2] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_1 \, d\lambda = 1 \cdot 0 + (4) \cdot 0 + (1 + 2) \cdot 0 = 0$$

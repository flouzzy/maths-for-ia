# Exercice 6 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_6$ définie selon des paliers.

Soit $f_6(x) = 6 \cdot \mathbf{1}_{[0, 6]}(x) + (6 + 2) \cdot \mathbf{1}_{[6, 12]}(x)$.

1. Exprimer rigoureusement $f_6$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_6$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_6(x) = f_6(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_6$ est définie comme la somme de fonctions indicatrices.
Le point $x = 6$ appartient aux deux intervalles $[0, 6]$ et $[6, 12]$.
Évaluons $f_6(6)$ :
$$f_6(6) = 6 \cdot 1 + (6 + 2) \cdot 1 = 14$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 6[$
$A_2 = \{ 6 \}$
$A_3 = ]6, 12]$
$A_4 = \mathbb{R} \setminus [0, 12]$

Sur $A_1$, $f_6(x) = 6$.
Sur $A_2$, $f_6(x) = 14$.
Sur $A_3$, $f_6(x) = 6 + 2$.
Sur $A_4$, $f_6(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_6(x) = 6 \cdot \mathbf{1}_{[0, 6[}(x) + (14) \cdot \mathbf{1}_{\{ 6 \}}(x) + (6 + 2) \cdot \mathbf{1}_{]6, 12]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 12]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_6 \, d\lambda = 6 \cdot \lambda([0, 6[) + (14) \cdot \lambda(\{ 6 \}) + (6 + 2) \cdot \lambda(]6, 12]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 12])$$

Calcul des mesures :
$\lambda([0, 6[) = 6 - 0 = 6$
$\lambda(\{ 6 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]6, 12]) = 12 - 6 = 6$
$\lambda(\mathbb{R} \setminus [0, 12]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_6 \, d\lambda = 6 \cdot 6 + (14) \cdot 0 + (6 + 2) \cdot 6 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_6 \, d\lambda = 36 + 48 = 84$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_6(x) = f_6(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_6 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_6$ est une fonction étagée :
$$g_6(x) = 6 \cdot \mathbf{1}_{[0, 6[ \cap \mathbb{Q}}(x) + (14) \cdot \mathbf{1}_{\{ 6 \} \cap \mathbb{Q}}(x) + (6 + 2) \cdot \mathbf{1}_{]6, 12] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 6[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 6 \} \cap \mathbb{Q}) = 0$
$\lambda(]6, 12] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_6 \, d\lambda = 6 \cdot 0 + (14) \cdot 0 + (6 + 2) \cdot 0 = 0$$

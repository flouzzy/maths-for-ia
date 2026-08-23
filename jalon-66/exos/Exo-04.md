# Exercice 4 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_4$ définie selon des paliers.

Soit $f_4(x) = 4 \cdot \mathbf{1}_{[0, 4]}(x) + (4 + 2) \cdot \mathbf{1}_{[4, 8]}(x)$.

1. Exprimer rigoureusement $f_4$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_4$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_4(x) = f_4(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_4$ est définie comme la somme de fonctions indicatrices.
Le point $x = 4$ appartient aux deux intervalles $[0, 4]$ et $[4, 8]$.
Évaluons $f_4(4)$ :
$$f_4(4) = 4 \cdot 1 + (4 + 2) \cdot 1 = 10$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 4[$
$A_2 = \{ 4 \}$
$A_3 = ]4, 8]$
$A_4 = \mathbb{R} \setminus [0, 8]$

Sur $A_1$, $f_4(x) = 4$.
Sur $A_2$, $f_4(x) = 10$.
Sur $A_3$, $f_4(x) = 4 + 2$.
Sur $A_4$, $f_4(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_4(x) = 4 \cdot \mathbf{1}_{[0, 4[}(x) + (10) \cdot \mathbf{1}_{\{ 4 \}}(x) + (4 + 2) \cdot \mathbf{1}_{]4, 8]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 8]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_4 \, d\lambda = 4 \cdot \lambda([0, 4[) + (10) \cdot \lambda(\{ 4 \}) + (4 + 2) \cdot \lambda(]4, 8]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 8])$$

Calcul des mesures :
$\lambda([0, 4[) = 4 - 0 = 4$
$\lambda(\{ 4 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]4, 8]) = 8 - 4 = 4$
$\lambda(\mathbb{R} \setminus [0, 8]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_4 \, d\lambda = 4 \cdot 4 + (10) \cdot 0 + (4 + 2) \cdot 4 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_4 \, d\lambda = 16 + 24 = 40$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_4(x) = f_4(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_4 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_4$ est une fonction étagée :
$$g_4(x) = 4 \cdot \mathbf{1}_{[0, 4[ \cap \mathbb{Q}}(x) + (10) \cdot \mathbf{1}_{\{ 4 \} \cap \mathbb{Q}}(x) + (4 + 2) \cdot \mathbf{1}_{]4, 8] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 4[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 4 \} \cap \mathbb{Q}) = 0$
$\lambda(]4, 8] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_4 \, d\lambda = 4 \cdot 0 + (10) \cdot 0 + (4 + 2) \cdot 0 = 0$$

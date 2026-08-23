# Exercice 8 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_8$ définie selon des paliers.

Soit $f_8(x) = 8 \cdot \mathbf{1}_{[0, 8]}(x) + (8 + 2) \cdot \mathbf{1}_{[8, 16]}(x)$.

1. Exprimer rigoureusement $f_8$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_8$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_8(x) = f_8(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_8$ est définie comme la somme de fonctions indicatrices.
Le point $x = 8$ appartient aux deux intervalles $[0, 8]$ et $[8, 16]$.
Évaluons $f_8(8)$ :
$$f_8(8) = 8 \cdot 1 + (8 + 2) \cdot 1 = 18$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 8[$
$A_2 = \{ 8 \}$
$A_3 = ]8, 16]$
$A_4 = \mathbb{R} \setminus [0, 16]$

Sur $A_1$, $f_8(x) = 8$.
Sur $A_2$, $f_8(x) = 18$.
Sur $A_3$, $f_8(x) = 8 + 2$.
Sur $A_4$, $f_8(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_8(x) = 8 \cdot \mathbf{1}_{[0, 8[}(x) + (18) \cdot \mathbf{1}_{\{ 8 \}}(x) + (8 + 2) \cdot \mathbf{1}_{]8, 16]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 16]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_8 \, d\lambda = 8 \cdot \lambda([0, 8[) + (18) \cdot \lambda(\{ 8 \}) + (8 + 2) \cdot \lambda(]8, 16]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 16])$$

Calcul des mesures :
$\lambda([0, 8[) = 8 - 0 = 8$
$\lambda(\{ 8 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]8, 16]) = 16 - 8 = 8$
$\lambda(\mathbb{R} \setminus [0, 16]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_8 \, d\lambda = 8 \cdot 8 + (18) \cdot 0 + (8 + 2) \cdot 8 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_8 \, d\lambda = 64 + 80 = 144$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_8(x) = f_8(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_8 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_8$ est une fonction étagée :
$$g_8(x) = 8 \cdot \mathbf{1}_{[0, 8[ \cap \mathbb{Q}}(x) + (18) \cdot \mathbf{1}_{\{ 8 \} \cap \mathbb{Q}}(x) + (8 + 2) \cdot \mathbf{1}_{]8, 16] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 8[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 8 \} \cap \mathbb{Q}) = 0$
$\lambda(]8, 16] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_8 \, d\lambda = 8 \cdot 0 + (18) \cdot 0 + (8 + 2) \cdot 0 = 0$$

# Exercice 2 : Intégrale de Lebesgue pour les fonctions mesurables positives
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons une fonction mesurable positive $f_2$ définie selon des paliers.

Soit $f_2(x) = 2 \cdot \mathbf{1}_{[0, 2]}(x) + (2 + 2) \cdot \mathbf{1}_{[2, 4]}(x)$.

1. Exprimer rigoureusement $f_2$ comme une fonction étagée positive sous sa forme canonique sur une partition.
2. Calculer l'intégrale de Lebesgue de $f_2$ par rapport à la mesure $\lambda$.
3. Étudier l'intégrale de la fonction $g_2(x) = f_2(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.

## Solution Détaillée

**Question 1 : Forme canonique**

La fonction $f_2$ est définie comme la somme de fonctions indicatrices.
Le point $x = 2$ appartient aux deux intervalles $[0, 2]$ et $[2, 4]$.
Évaluons $f_2(2)$ :
$$f_2(2) = 2 \cdot 1 + (2 + 2) \cdot 1 = 6$$

Nous partitionnons $\mathbb{R}$ en sous-ensembles disjoints :
$A_1 = [0, 2[$
$A_2 = \{ 2 \}$
$A_3 = ]2, 4]$
$A_4 = \mathbb{R} \setminus [0, 4]$

Sur $A_1$, $f_2(x) = 2$.
Sur $A_2$, $f_2(x) = 6$.
Sur $A_3$, $f_2(x) = 2 + 2$.
Sur $A_4$, $f_2(x) = 0$.

La fonction étagée sous sa forme canonique s'écrit donc :
$$f_2(x) = 2 \cdot \mathbf{1}_{[0, 2[}(x) + (6) \cdot \mathbf{1}_{\{ 2 \}}(x) + (2 + 2) \cdot \mathbf{1}_{]2, 4]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 4]}(x)$$

**Question 2 : Calcul de l'intégrale**

Par définition de l'intégrale d'une fonction étagée par rapport à la mesure de Lebesgue $\lambda$ :
$$\int_{\mathbb{R}} f_2 \, d\lambda = 2 \cdot \lambda([0, 2[) + (6) \cdot \lambda(\{ 2 \}) + (2 + 2) \cdot \lambda(]2, 4]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 4])$$

Calcul des mesures :
$\lambda([0, 2[) = 2 - 0 = 2$
$\lambda(\{ 2 \}) = 0$ (la mesure de Lebesgue d'un point est nulle)
$\lambda(]2, 4]) = 4 - 2 = 2$
$\lambda(\mathbb{R} \setminus [0, 4]) = +\infty$

On obtient :
$$\int_{\mathbb{R}} f_2 \, d\lambda = 2 \cdot 2 + (6) \cdot 0 + (2 + 2) \cdot 2 + 0 \cdot (+\infty)$$
Avec la convention de la théorie de la mesure $0 \cdot (+\infty) = 0$, l'expression devient :
$$\int_{\mathbb{R}} f_2 \, d\lambda = 4 + 8 = 12$$

**Question 3 : Intégrale avec l'indicatrice des rationnels**

Considérons $g_2(x) = f_2(x) \cdot \mathbf{1}_{\mathbb{Q}}(x)$.
Cette fonction ne prend des valeurs non nulles que sur $\mathbb{Q}$.
On a $g_2 = 0$ presque partout car l'ensemble des rationnels $\mathbb{Q}$ est de mesure de Lebesgue nulle, c'est-à-dire $\lambda(\mathbb{Q}) = 0$.
Par les propriétés de l'intégrale de Lebesgue, pour toute fonction positive $h$, si $h=0$ $\lambda$-presque partout, alors son intégrale est nulle.

Vérifions formellement.
$g_2$ est une fonction étagée :
$$g_2(x) = 2 \cdot \mathbf{1}_{[0, 2[ \cap \mathbb{Q}}(x) + (6) \cdot \mathbf{1}_{\{ 2 \} \cap \mathbb{Q}}(x) + (2 + 2) \cdot \mathbf{1}_{]2, 4] \cap \mathbb{Q}}(x)$$

La mesure de Lebesgue de chaque ensemble est nulle :
$\lambda([0, 2[ \cap \mathbb{Q}) \leq \lambda(\mathbb{Q}) = 0$
$\lambda(\{ 2 \} \cap \mathbb{Q}) = 0$
$\lambda(]2, 4] \cap \mathbb{Q}) = 0$

L'intégrale vaut donc :
$$\int_{\mathbb{R}} g_2 \, d\lambda = 2 \cdot 0 + (6) \cdot 0 + (2 + 2) \cdot 0 = 0$$

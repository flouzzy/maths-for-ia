# Exercice 1 : Opérations Linéaires Élémentaires sur les Matrices
**Difficulté :** ★☆☆☆☆

## Énoncé
Soit $\mathbb{K}$ un corps commutatif, que nous identifierons à $\mathbb{R}$ dans le cadre de cet exercice. Nous considérons l'espace vectoriel $\mathcal{M}_{2,2}(\mathbb{K})$ des matrices carrées d'ordre 2 à coefficients dans $\mathbb{K}$.

Soient les matrices $A$ et $B$ définies comme suit :
$$ A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \in \mathcal{M}_{2,2}(\mathbb{K}) $$
$$ B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \in \mathcal{M}_{2,2}(\mathbb{K}) $$
Soit également le scalaire $\lambda = 3 \in \mathbb{K}$.

Déterminer les matrices $C, D, E \in \mathcal{M}_{2,2}(\mathbb{K})$ telles que :
1.  $C = A + B$
2.  $D = A - B$
3.  $E = \lambda A$

Pour chacune de ces matrices, expliciter l'ensemble de ses coefficients $(M_{i,j})_{1 \le i,j \le 2}$.

## Correction Détaillée

Nous allons procéder à la détermination de chaque matrice en appliquant les définitions formelles des opérations matricielles.

### 1. Détermination de la matrice $C = A + B$

Par définition, l'addition de deux matrices $A = (A_{i,j})$ et $B = (B_{i,j})$ de même dimension $n \times p$ est la matrice $C = (C_{i,j})$ de dimension $n \times p$ dont les coefficients sont donnés par $C_{i,j} = A_{i,j} + B_{i,j}$ pour tout $1 \le i \le n$ et $1 \le j \le p$.
Dans notre cas, $n=2$ et $p=2$.

Les coefficients de $C$ sont calculés comme suit :
*   $C_{1,1} = A_{1,1} + B_{1,1} = 1 + 5 = 6$
*   $C_{1,2} = A_{1,2} + B_{1,2} = 2 + 6 = 8$
*   $C_{2,1} = A_{2,1} + B_{2,1} = 3 + 7 = 10$
*   $C_{2,2} = A_{2,2} + B_{2,2} = 4 + 8 = 12$

Ainsi, la matrice $C$ est :
$$ C = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix} $$

### 2. Détermination de la matrice $D = A - B$

Par définition, la soustraction de deux matrices $A = (A_{i,j})$ et $B = (B_{i,j})$ de même dimension $n \times p$ est la matrice $D = (D_{i,j})$ de dimension $n \times p$ dont les coefficients sont donnés par $D_{i,j} = A_{i,j} - B_{i,j}$ pour tout $1 \le i \le n$ et $1 \le j \le p$.
Dans notre cas, $n=2$ et $p=2$.

Les coefficients de $D$ sont calculés comme suit :
*   $D_{1,1} = A_{1,1} - B_{1,1} = 1 - 5 = -4$
*   $D_{1,2} = A_{1,2} - B_{1,2} = 2 - 6 = -4$
*   $D_{2,1} = A_{2,1} - B_{2,1} = 3 - 7 = -4$
*   $D_{2,2} = A_{2,2} - B_{2,2} = 4 - 8 = -4$

Ainsi, la matrice $D$ est :
$$ D = \begin{pmatrix} -4 & -4 \\ -4 & -4 \end{pmatrix} $$

### 3. Détermination de la matrice $E = \lambda A$

Par définition, la multiplication d'une matrice $A = (A_{i,j})$ de dimension $n \times p$ par un scalaire $\lambda \in \mathbb{K}$ est la matrice $E = (E_{i,j})$ de dimension $n \times p$ dont les coefficients sont donnés par $E_{i,j} = \lambda \cdot A_{i,j}$ pour tout $1 \le i \le n$ et $1 \le j \le p$.
Dans notre cas, $n=2$, $p=2$, et $\lambda = 3$.

Les coefficients de $E$ sont calculés comme suit :
*   $E_{1,1} = \lambda \cdot A_{1,1} = 3 \cdot 1 = 3$
*   $E_{1,2} = \lambda \cdot A_{1,2} = 3 \cdot 2 = 6$
*   $E_{2,1} = \lambda \cdot A_{2,1} = 3 \cdot 3 = 9$
*   $E_{2,2} = \lambda \cdot A_{2,2} = 3 \cdot 4 = 12$

Ainsi, la matrice $E$ est :
$$ E = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix} $$


**Exégèse Conceptuelle et Rigueur Académique :**
La résolution de ce problème nécessite une compréhension profonde de la structure de $\mathbb{K}$-espace vectoriel. Il ne suffit pas d'appliquer aveuglément les formules. Soit $E$ un espace vectoriel sur le corps commutatif $\mathbb{K}$. Considérons un endomorphisme $u \in \mathcal{L}(E)$. La matrice représentative $M = \text{Mat}_{\mathcal{B}}(u)$ dans une base $\mathcal{B}$ encode toute l'information géométrique de $u$. En particulier, le théorème du rang, $\dim(E) = \dim(\ker(u)) + \text{rg}(u)$, nous assure que toute perte de dimension dans l'image est rigoureusement compensée par la dimension du noyau. La démonstration repose sur l'extraction d'une base de $\ker(u)$, complétée en une base de $E$, dont les images par $u$ forment alors une base de $\text{Im}(u)$. Chaque étape du pivot de Gauss sur $M$ correspond à un changement de base préservant le rang. Cas pathologique : si le corps $\mathbb{K}$ est de caractéristique finie, par exemple $\mathbb{F}_2$, les notions de distance et d'angle s'effondrent, mais les propriétés d'incidence algébrique encodées par la matrice demeurent intactes.

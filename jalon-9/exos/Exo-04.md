# Exercice 4 : Résolution d'une équation matricielle impliquant la transposition
**Difficulté :** ★★☆☆☆

## Énoncé
Soient $A$ et $B$ deux matrices appartenant à l'espace $\mathcal{M}_{2,2}(\mathbb{R})$ des matrices carrées d'ordre 2 à coefficients réels. On définit ces matrices par :
$$ A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} $$
$$ B = \begin{pmatrix} 5 & 0 \\ -1 & 6 \end{pmatrix} $$
Déterminer l'unique matrice $X \in \mathcal{M}_{2,2}(\mathbb{R})$ satisfaisant l'équation matricielle suivante :
$$ 2X + A^T = B $$
où $A^T$ désigne la transposée de la matrice $A$.

## Correction Détaillée

Nous sommes invités à déterminer la matrice $X \in \mathcal{M}_{2,2}(\mathbb{R})$ qui est solution de l'équation matricielle $2X + A^T = B$.

**Étape 1 : Isolation de la matrice $X$ dans l'équation.**
L'équation donnée est :
$$ 2X + A^T = B $$
Pour isoler $2X$, nous soustrayons la matrice $A^T$ des deux côtés de l'équation. Par les propriétés de l'algèbre matricielle, cette opération est bien définie dans $\mathcal{M}_{2,2}(\mathbb{R})$ :
$$ 2X = B - A^T $$
Ensuite, pour obtenir $X$, nous multiplions les deux côtés de l'équation par le scalaire $\frac{1}{2}$. La multiplication scalaire est également une opération bien définie dans $\mathcal{M}_{2,2}(\mathbb{R})$ :
$$ X = \frac{1}{2}(B - A^T) $$
Cette expression nous indique la séquence des calculs à effectuer.

**Étape 2 : Calcul de la transposée de la matrice $A$.**
La matrice $A$ est donnée par :
$$ A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} $$
La transposée d'une matrice $M$, notée $M^T$, est obtenue en échangeant ses lignes et ses colonnes. Formellement, si $M = (m_{ij})$, alors $M^T = (m'_{ij})$ où $m'_{ij} = m_{ji}$.
Appliquons cette définition à la matrice $A$ :
$$ A^T = \begin{pmatrix} A_{11} & A_{21} \\ A_{12} & A_{22} \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} $$

**Étape 3 : Calcul de la différence matricielle $B - A^T$.**
Nous avons les matrices $B$ et $A^T$ :
$$ B = \begin{pmatrix} 5 & 0 \\ -1 & 6 \end{pmatrix} $$
$$ A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} $$
La soustraction de deux matrices de mêmes dimensions s'effectue élément par élément. Formellement, si $M = (m_{ij})$ et $N = (n_{ij})$, alors $M - N = (m_{ij} - n_{ij})$.
$$ B - A^T = \begin{pmatrix} 5 & 0 \\ -1 & 6 \end{pmatrix} - \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} $$
$$ B - A^T = \begin{pmatrix} 5 - 1 & 0 - 3 \\ -1 - 2 & 6 - 4 \end{pmatrix} $$
Effectuons les soustractions arithmétiques pour chaque élément :
$$ B - A^T = \begin{pmatrix} 4 & -3 \\ -3 & 2 \end{pmatrix} $$

**Étape 4 : Multiplication par le scalaire $\frac{1}{2}$.**
Nous devons maintenant multiplier la matrice résultante de l'Étape 3 par le scalaire $\frac{1}{2}$ pour obtenir $X$.
$$ X = \frac{1}{2}(B - A^T) = \frac{1}{2} \begin{pmatrix} 4 & -3 \\ -3 & 2 \end{pmatrix} $$
La multiplication d'une matrice par un scalaire s'effectue en multipliant chaque élément de la matrice par ce scalaire. Formellement, si $c$ est un scalaire et $M = (m_{ij})$, alors $cM = (c \cdot m_{ij})$.
$$ X = \begin{pmatrix} \frac{1}{2} \times 4 & \frac{1}{2} \times (-3) \\ \frac{1}{2} \times (-3) & \frac{1}{2} \times 2 \end{pmatrix} $$
Effectuons les multiplications arithmétiques pour chaque élément :
$$ X = \begin{pmatrix} 2 & -\frac{3}{2} \\ -\frac{3}{2} & 1 \end{pmatrix} $$

**Conclusion :**
La matrice $X$ satisfaisant l'équation $2X + A^T = B$ est :
$$ X = \begin{pmatrix} 2 & -\frac{3}{2} \\ -\frac{3}{2} & 1 \end{pmatrix} $$

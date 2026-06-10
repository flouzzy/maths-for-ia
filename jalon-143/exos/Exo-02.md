```yaml
uuid: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
title: Analyse Spectrale d'un Graphe Complet et Partitions Optimales
```

# Exercice 2 : Analyse Spectrale d'un Graphe Complet et Partitions Optimales

Soit $G = K_3$ le graphe complet à 3 sommets, avec $V = \{1, 2, 3\}$ et $E = \{(1,2), (2,3), (3,1)\}$.

## Partie A : Laplacien Combinatoire et Coupures

1.  Déterminez la matrice d'adjacence $A$ et la matrice des degrés $D$ du graphe $G$.
2.  Calculez le Laplacien combinatoire $L = D - A$.
3.  Déterminez toutes les valeurs propres et une base orthonormée de vecteurs propres pour $L$.
4.  Identifiez la deuxième plus petite valeur propre non nulle (valeur de Fiedler) et son vecteur propre associé (vecteur de Fiedler).
5.  Utilisez le vecteur de Fiedler pour proposer une partition du graphe $V = S_1 \cup S_2$ en deux sous-ensembles non vides et disjoints. Calculez la valeur de la coupure $\text{cut}(S_1, S_2)$ et le Ratio Cut $\text{RatioCut}(S_1, S_2)$ de cette partition.

## Partie B : Laplacien Normalisé (Symétrique) et Coupures

1.  Calculez le Laplacien normalisé symétrique $L_{sym} = D^{-1/2} L D^{-1/2}$.
2.  Déterminez toutes les valeurs propres et une base orthonormée de vecteurs propres pour $L_{sym}$.
3.  Identifiez la deuxième plus petite valeur propre non nulle et son vecteur propre associé.
4.  Utilisez ce vecteur propre pour proposer une partition du graphe $V = S_1 \cup S_2$. Calculez la valeur de la coupure $\text{cut}(S_1, S_2)$ et le Normalized Cut $\text{Ncut}(S_1, S_2)$ de cette partition.

## Partie C : Comparaison et Discussion

1.  Comparez les partitions obtenues à partir des Laplaciens combinatoire et normalisé.
2.  Discutez des relations entre les valeurs propres et les valeurs des coupures obtenues. Expliquez pourquoi les résultats peuvent être similaires ou différents pour ce type de graphe.

---

# Correction Détaillée

## Partie A : Laplacien Combinatoire et Coupures

1.  **Matrice d'adjacence $A$ et matrice des degrés $D$**

    Le graphe $K_3$ a 3 sommets, et chaque sommet est connecté à tous les autres.
    Les arêtes sont $(1,2), (2,3), (3,1)$.
    La matrice d'adjacence $A$ est donnée par $A_{ij} = 1$ si $(i,j) \in E$ et $0$ sinon.
    $$
    A = \begin{pmatrix}
    0 & 1 & 1 \\
    1 & 0 & 1 \\
    1 & 1 & 0
    \end{pmatrix}
    $$
    La matrice des degrés $D$ est une matrice diagonale où $D_{ii}$ est le degré du sommet $i$.
    Pour $K_3$, chaque sommet a un degré de 2 (il est connecté aux deux autres sommets).
    $d(1) = 2$, $d(2) = 2$, $d(3) = 2$.
    $$
    D = \begin{pmatrix}
    2 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 0 & 2
    \end{pmatrix}
    $$

2.  **Laplacien combinatoire $L = D - A$**

    $$
    L = D - A = \begin{pmatrix}
    2 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 0 & 2
    \end{pmatrix} - \begin{pmatrix}
    0 & 1 & 1 \\
    1 & 0 & 1 \\
    1 & 1 & 0
    \end{pmatrix} = \begin{pmatrix}
    2 & -1 & -1 \\
    -1 & 2 & -1 \\
    -1 & -1 & 2
    \end{pmatrix}
    $$

3.  **Valeurs propres et vecteurs propres de $L$**

    Le Laplacien combinatoire est toujours semi-défini positif. La plus petite valeur propre est toujours 0, avec le vecteur propre $\mathbf{1} = (1,1,1)^T$.
    Vérifions :
    $$
    L \mathbf{1} = \begin{pmatrix}
    2 & -1 & -1 \\
    -1 & 2 & -1 \\
    -1 & -1 & 2
    \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2-1-1 \\ -1+2-1 \\ -1-1+2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = 0 \cdot \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
    $$
    Donc $\lambda_1 = 0$ avec $v_1 = \frac{1}{\sqrt{3}}(1,1,1)^T$ (normalisé).

    Pour trouver les autres valeurs propres, nous pouvons calculer le polynôme caractéristique $\det(L - \lambda I) = 0$.
    $$
    \det \begin{pmatrix}
    2-\lambda & -1 & -1 \\
    -1 & 2-\lambda & -1 \\
    -1 & -1 & 2-\lambda
    \end{pmatrix} = 0
    $$
    Développons le déterminant :
    $(2-\lambda)[(2-\lambda)^2 - 1] - (-1)[-(2-\lambda) - 1] + (-1)[1 + (2-\lambda)] = 0$
    $(2-\lambda)[(2-\lambda-1)(2-\lambda+1)] + [2-\lambda+1] - [1+2-\lambda] = 0$
    $(2-\lambda)[(1-\lambda)(3-\lambda)] + (3-\lambda) - (3-\lambda) = 0$
    $(2-\lambda)(1-\lambda)(3-\lambda) = 0$
    Les valeurs propres sont $\lambda_1 = 0$, $\lambda_2 = 1$, $\lambda_3 = 3$.
    *Erratum*: J'ai fait une erreur dans le calcul du déterminant.
    $(2-\lambda)[(2-\lambda)^2 - 1] + [-(2-\lambda) - 1] - [1 + (2-\lambda)] = 0$
    $(2-\lambda)[(2-\lambda-1)(2-\lambda+1)] - (3-\lambda) - (3-\lambda) = 0$
    $(2-\lambda)(1-\lambda)(3-\lambda) - 2(3-\lambda) = 0$
    $(3-\lambda)[(2-\lambda)(1-\lambda) - 2] = 0$
    $(3-\lambda)[\lambda^2 - 3\lambda + 2 - 2] = 0$
    $(3-\lambda)[\lambda^2 - 3\lambda] = 0$
    $(3-\lambda)\lambda(\lambda-3) = 0$
    Les valeurs propres sont $\lambda_1 = 0$, $\lambda_2 = 3$, $\lambda_3 = 3$.

    Maintenant, trouvons les vecteurs propres pour $\lambda_2 = 3$ et $\lambda_3 = 3$.
    Pour $\lambda = 3$:
    $(L - 3I)v = \mathbf{0}$
    $$
    \begin{pmatrix}
    2-3 & -1 & -1 \\
    -1 & 2-3 & -1 \\
    -1 & -1 & 2-3
    \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
    \implies \begin{pmatrix}
    -1 & -1 & -1 \\
    -1 & -1 & -1 \\
    -1 & -1 & -1
    \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
    $$
    Ceci implique $-v_1 - v_2 - v_3 = 0$, ou $v_1 + v_2 + v_3 = 0$.
    L'espace propre pour $\lambda=3$ est le plan orthogonal à $(1,1,1)^T$.
    Nous devons trouver deux vecteurs propres linéairement indépendants et orthogonaux à $(1,1,1)^T$.
    Choisissons $v_2$: Soit $v_1=1, v_2=-1$. Alors $v_3=0$.
    $v_2 = (1,-1,0)^T$. Normalisé : $\frac{1}{\sqrt{2}}(1,-1,0)^T$.
    Vérifions : $L(1,-1,0)^T = (2+1, -1-2, -1+1)^T = (3,-3,0)^T = 3(1,-1,0)^T$. Correct.

    Choisissons $v_3$: Il doit être orthogonal à $v_1$ et $v_2$.
    $v_3 = (a,b,c)^T$.
    $a+b+c=0$
    $a-b=0 \implies a=b$.
    Donc $a+a+c=0 \implies 2a+c=0 \implies c=-2a$.
    Soit $a=1$. Alors $b=1, c=-2$.
    $v_3 = (1,1,-2)^T$. Normalisé : $\frac{1}{\sqrt{6}}(1,1,-2)^T$.
    Vérifions : $L(1,1,-2)^T = (2-1+2, -1+2+2, -1-1-4)^T = (3,3,-6)^T = 3(1,1,-2)^T$. Correct.

    Base orthonormée de vecteurs propres :
    $v_1 = \frac{1}{\sqrt{3}}(1,1,1)^T$ pour $\lambda_1 = 0$.
    $v_2 = \frac{1}{\sqrt{2}}(1,-1,0)^T$ pour $\lambda_2 = 3$.
    $v_3 = \frac{1}{\sqrt{6}}(1,1,-2)^T$ pour $\lambda_3 = 3$.

4.  **Vecteur de Fiedler**

    La deuxième plus petite valeur propre non nulle est $\lambda_2 = 3$.
    Le vecteur de Fiedler est $v_2 = \frac{1}{\sqrt{2}}(1,-1,0)^T$ (ou tout autre vecteur propre de l'espace propre de $\lambda=3$, comme $v_3$, ou une combinaison linéaire). Nous utiliserons $v_2 = (1,-1,0)^T$ pour la partition.

5.  **Partition et Ratio Cut**

    Le vecteur de Fiedler $v_2 = (1,-1,0)^T$ a des composantes : $v_2(1)=1$, $v_2(2)=-1$, $v_2(3)=0$.
    Une partition spectrale est obtenue en séparant les sommets selon le signe des composantes du vecteur de Fiedler.
    $S_1 = \{i \in V \mid v_2(i) > 0\} = \{1\}$.
    $S_2 = \{i \in V \mid v_2(i) \le 0\} = \{2, 3\}$. (Alternativement, on peut inclure $v_2(i)=0$ dans $S_1$ ou $S_2$).
    Vérifions que $S_1$ et $S_2$ sont non vides et disjoints. C'est le cas.

    Calcul de la coupure $\text{cut}(S_1, S_2)$:
    La coupure est l'ensemble des arêtes ayant une extrémité dans $S_1$ et l'autre dans $S_2$.
    Les arêtes entre $\{1\}$ et $\{2,3\}$ sont $(1,2)$ et $(1,3)$.
    $\text{cut}(S_1, S_2) = 2$.

    Calcul du Ratio Cut $\text{RatioCut}(S_1, S_2)$:
    $\text{RatioCut}(S_1, S_2) = \frac{\text{cut}(S_1, S_2)}{|S_1|} + \frac{\text{cut}(S_1, S_2)}{|S_2|}$
    $|S_1| = 1$ (nombre de sommets dans $S_1$).
    $|S_2| = 2$ (nombre de sommets dans $S_2$).
    $\text{RatioCut}(S_1, S_2) = \frac{2}{1} + \frac{2}{2} = 2 + 1 = 3$.
    La valeur du Ratio Cut est égale à la valeur de Fiedler $\lambda_2 = 3$.

## Partie B : Laplacien Normalisé (Symétrique) et Coupures

1.  **Laplacien normalisé symétrique $L_{sym} = D^{-1/2} L D^{-1/2}$**

    La matrice des degrés $D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.
    Donc $D^{-1/2} = \begin{pmatrix} 1/\sqrt{2} & 0 & 0 \\ 0 & 1/\sqrt{2} & 0 \\ 0 & 0 & 1/\sqrt{2} \end{pmatrix} = \frac{1}{\sqrt{2}}I$.
    $$
    L_{sym} = \left(\frac{1}{\sqrt{2}}I\right) L \left(\frac{1}{\sqrt{2}}I\right) = \frac{1}{2} L
    $$
    $$
    L_{sym} = \frac{1}{2} \begin{pmatrix}
    2 & -1 & -1 \\
    -1 & 2 & -1 \\
    -1 & -1 & 2
    \end{pmatrix} = \begin{pmatrix}
    1 & -1/2 & -1/2 \\
    -1/2 & 1 & -1/2 \\
    -1/2 & -1/2 & 1
    \end{pmatrix}
    $$

2.  **Valeurs propres et vecteurs propres de $L_{sym}$**

    Puisque $L_{sym} = \frac{1}{2}L$, les valeurs propres de $L_{sym}$ sont la moitié de celles de $L$, et les vecteurs propres sont les mêmes.
    Valeurs propres de $L_{sym}$: $\lambda_1 = 0$, $\lambda_2 = 3/2$, $\lambda_3 = 3/2$.
    Base orthonormée de vecteurs propres :
    $v_1 = \frac{1}{\sqrt{3}}(1,1,1)^T$ pour $\lambda_1 = 0$.
    $v_2 = \frac{1}{\sqrt{2}}(1,-1,0)^T$ pour $\lambda_2 = 3/2$.
    $v_3 = \frac{1}{\sqrt{6}}(1,1,-2)^T$ pour $\lambda_3 = 3/2$.

3.  **Deuxième plus petite valeur propre et vecteur propre associé**

    La deuxième plus petite valeur propre non nulle de $L_{sym}$ est $\lambda_2 = 3/2$.
    Le vecteur propre associé est $v_2 = \frac{1}{\sqrt{2}}(1,-1,0)^T$.

4.  **Partition et Normalized Cut**

    En utilisant le vecteur propre $v_2 = (1,-1,0)^T$ (les composantes sont les mêmes que pour le Laplacien combinatoire) :
    $S_1 = \{i \in V \mid v_2(i) > 0\} = \{1\}$.
    $S_2 = \{i \in V \mid v_2(i) \le 0\} = \{2, 3\}$.

    Calcul de la coupure $\text{cut}(S_1, S_2)$:
    Comme précédemment, $\text{cut}(S_1, S_2) = 2$.

    Calcul du Normalized Cut $\text{Ncut}(S_1, S_2)$:
    $\text{Ncut}(S_1, S_2) = \frac{\text{cut}(S_1, S_2)}{\text{vol}(S_1)} + \frac{\text{cut}(S_1, S_2)}{\text{vol}(S_2)}$
    où $\text{vol}(S) = \sum_{i \in S} d(i)$.
    $\text{vol}(S_1) = d(1) = 2$.
    $\text{vol}(S_2) = d(2) + d(3) = 2 + 2 = 4$.
    $\text{Ncut}(S_1, S_2) = \frac{2}{2} + \frac{2}{4} = 1 + 0.5 = 1.5$.
    La valeur du Normalized Cut est égale à la deuxième plus petite valeur propre de $L_{sym}$, $\lambda_2 = 3/2 = 1.5$.

## Partie C : Comparaison et Discussion

1.  **Comparaison des partitions**

    Dans cet exercice, les deux Laplaciens (combinatoire et normalisé symétrique) ont produit la même partition du graphe : $S_1 = \{1\}$ et $S_2 = \{2,3\}$.
    Ceci est dû au fait que le graphe $K_3$ est un graphe régulier, c'est-à-dire que tous ses sommets ont le même degré ($d_i=2$ pour tout $i$).

2.  **Relations entre valeurs propres et coupures**

    Pour le Laplacien combinatoire $L$, la deuxième plus petite valeur propre $\lambda_2(L)$ (valeur de Fiedler) est une borne inférieure pour le Ratio Cut minimum sur le graphe. Dans notre cas, $\lambda_2(L) = 3$, et le Ratio Cut de la partition obtenue est également 3.
    Pour le Laplacien normalisé symétrique $L_{sym}$, la deuxième plus petite valeur propre $\lambda_2(L_{sym})$ est une borne inférieure pour le Normalized Cut minimum sur le graphe. Ici, $\lambda_2(L_{sym}) = 3/2$, et le Normalized Cut de la partition obtenue est également 3/2.

    La correspondance exacte entre la deuxième valeur propre et la valeur de la coupure pour la partition spectrale n'est pas toujours garantie pour tous les graphes. Cependant, pour les graphes réguliers, il existe une relation directe.
    Pour un graphe $k$-régulier (chaque sommet a un degré $k$), la matrice des degrés est $D = kI$.
    Alors $L_{sym} = D^{-1/2} L D^{-1/2} = (kI)^{-1/2} L (kI)^{-1/2} = \frac{1}{\sqrt{k}}I L \frac{1}{\sqrt{k}}I = \frac{1}{k}L$.
    Par conséquent, les valeurs propres de $L_{sym}$ sont simplement les valeurs propres de $L$ divisées par $k$. Les vecteurs propres sont identiques.
    Dans notre cas, $K_3$ est 2-régulier, donc $k=2$. Les valeurs propres de $L_{sym}$ sont la moitié de celles de $L$.
    $\lambda_2(L_{sym}) = \lambda_2(L) / k = 3/2$.

    Les deux approches de partitionnement spectral (basées sur $L$ et $L_{sym}$) visent à trouver des coupures "optimales" dans un certain sens.
    *   Le Ratio Cut cherche à minimiser la coupure par rapport à la taille des partitions (nombre de sommets). Il pénalise les partitions avec de petits sous-ensembles.
    *   Le Normalized Cut cherche à minimiser la coupure par rapport au volume des partitions (somme des degrés des sommets). Il pénalise les partitions avec des sous-ensembles de faible volume.
    Pour les graphes réguliers, la taille d'un ensemble de sommets est proportionnelle à son volume (car tous les degrés sont égaux), donc les deux critères sont proportionnels et mènent aux mêmes partitions.

    Dans le cas de $K_3$, la coupure minimale est de 2 (en retirant n'importe quelle paire d'arêtes connectant un sommet au reste du graphe, par exemple $(1,2)$ et $(1,3)$ pour la partition $\{1\}, \{2,3\}$). La méthode spectrale a identifié cette coupure minimale.
    Ceci illustre comment la théorie spectrale des graphes peut être utilisée pour trouver des partitions de graphes qui sont des approximations de coupures minimales, avec des garanties théoriques (inégalités de Cheeger, non abordées en détail ici mais sous-jacentes).

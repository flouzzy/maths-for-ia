```yaml
uuid: 8c9e1d2a-f3b4-4c5d-8e9f-0a1b2c3d4e5f
title: Exercice 1 - Introduction au Laplacien Combinatoire et Coupures Spectrales
```

# Exercice 1 - Introduction au Laplacien Combinatoire et Coupures Spectrales

Ce premier exercice vise à familiariser l'étudiant avec les concepts fondamentaux de la théorie spectrale des graphes, en se concentrant sur le Laplacien combinatoire et son lien avec les coupures de graphes. Nous explorerons un petit graphe pour permettre des calculs explicites.

## Partie 1 : Le Laplacien Combinatoire

Soit le graphe $G=(V,E)$ défini par l'ensemble des sommets $V=\{1,2,3,4\}$ et l'ensemble des arêtes $E=\{(1,2), (1,3), (2,3), (3,4)\}$.

1.  Dessinez le graphe $G$.
2.  Écrivez la matrice d'adjacence $A$ et la matrice des degrés $D$ de $G$.
3.  Calculez le Laplacien combinatoire $L = D - A$.
4.  Calculez les valeurs propres de $L$. Vérifiez que la plus petite valeur propre est 0 et que son espace propre est lié aux composantes connexes de $G$.
5.  Identifiez la deuxième plus petite valeur propre $\lambda_2$ (valeur propre de Fiedler) et calculez un vecteur propre associé $v_2$ (vecteur de Fiedler).

## Partie 2 : Coupures et Partitionnement Spectral

1.  Définissez formellement une coupure $(S, \bar{S})$ d'un graphe $G=(V,E)$ et sa capacité $cut(S, \bar{S})$.
2.  Par inspection, identifiez toutes les coupures minimales de $G$ et leur capacité.
3.  Utilisez le vecteur de Fiedler $v_2$ calculé précédemment pour proposer une partition du graphe. Expliquez le principe de cette méthode. Comparez la coupure obtenue avec les coupures minimales trouvées précédemment.

## Partie 3 : Le Laplacien Normalisé (Introduction)

1.  Définissez la matrice des degrés inverse $D^{-1/2}$.
2.  Calculez le Laplacien normalisé $L_{norm} = D^{-1/2} L D^{-1/2}$ pour le graphe $G$.
3.  Calculez la plus petite valeur propre de $L_{norm}$ et son vecteur propre associé.
4.  (Bonus/Discussion) Sans effectuer de calculs supplémentaires pour les autres valeurs propres, expliquez pourquoi le Laplacien normalisé est souvent préféré au Laplacien combinatoire pour le partitionnement de graphes, en particulier pour des graphes avec des degrés très hétérogènes.

---

# Correction Détaillée

## Partie 1 : Le Laplacien Combinatoire

1.  **Dessin du graphe $G$ :**

    ```
    1 -- 2
    |  /
    3 -- 4
    ```

    Le graphe est composé d'un triangle formé par les sommets $\{1,2,3\}$ et d'une arête connectant le sommet $3$ au sommet $4$.

2.  **Matrice d'adjacence $A$ et matrice des degrés $D$ :**

    Les degrés des sommets sont :
    *   $d(1) = 2$ (arêtes $(1,2), (1,3)$)
    *   $d(2) = 2$ (arêtes $(1,2), (2,3)$)
    *   $d(3) = 3$ (arêtes $(1,3), (2,3), (3,4)$)
    *   $d(4) = 1$ (arête $(3,4)$)

    La matrice d'adjacence $A$ est une matrice $4 \times 4$ où $A_{ij}=1$ si $(i,j) \in E$ et $0$ sinon :
    $$
    A = \begin{pmatrix}
    0 & 1 & 1 & 0 \\
    1 & 0 & 1 & 0 \\
    1 & 1 & 0 & 1 \\
    0 & 0 & 1 & 0
    \end{pmatrix}
    $$

    La matrice des degrés $D$ est une matrice diagonale où $D_{ii}=d(i)$ :
    $$
    D = \begin{pmatrix}
    2 & 0 & 0 & 0 \\
    0 & 2 & 0 & 0 \\
    0 & 0 & 3 & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix}
    $$

3.  **Calcul du Laplacien combinatoire $L = D - A$ :**
    $$
    L = D - A = \begin{pmatrix}
    2 & 0 & 0 & 0 \\
    0 & 2 & 0 & 0 \\
    0 & 0 & 3 & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix} - \begin{pmatrix}
    0 & 1 & 1 & 0 \\
    1 & 0 & 1 & 0 \\
    1 & 1 & 0 & 1 \\
    0 & 0 & 1 & 0
    \end{pmatrix} = \begin{pmatrix}
    2 & -1 & -1 & 0 \\
    -1 & 2 & -1 & 0 \\
    -1 & -1 & 3 & -1 \\
    0 & 0 & -1 & 1
    \end{pmatrix}
    $$

4.  **Calcul des valeurs propres de $L$ :**

    Pour trouver les valeurs propres, nous devons résoudre l'équation caractéristique $\det(L - \lambda I) = 0$.
    $$
    \det(L - \lambda I) = \begin{vmatrix}
    2-\lambda & -1 & -1 & 0 \\
    -1 & 2-\lambda & -1 & 0 \\
    -1 & -1 & 3-\lambda & -1 \\
    0 & 0 & -1 & 1-\lambda
    \end{vmatrix}
    $$
    Développons le déterminant le long de la quatrième ligne :
    $$
    \det(L - \lambda I) = 0 \cdot C_{41} + 0 \cdot C_{42} + (-1) \cdot (-1)^{4+3} \begin{vmatrix}
    2-\lambda & -1 & 0 \\
    -1 & 2-\lambda & 0 \\
    -1 & -1 & -1
    \end{vmatrix} + (1-\lambda) \cdot (-1)^{4+4} \begin{vmatrix}
    2-\lambda & -1 & -1 \\
    -1 & 2-\lambda & -1 \\
    -1 & -1 & 3-\lambda
    \end{vmatrix}
    $$
    Calculons le premier sous-déterminant (mineur de $L_{43}$):
    $$
    \begin{vmatrix}
    2-\lambda & -1 & 0 \\
    -1 & 2-\lambda & 0 \\
    -1 & -1 & -1
    \end{vmatrix} = (-1) \cdot ((2-\lambda)^2 - (-1)(-1)) = -((2-\lambda)^2 - 1) = -(\lambda^2 - 4\lambda + 4 - 1) = -(\lambda^2 - 4\lambda + 3) = -(\lambda-1)(\lambda-3)
    $$
    Calculons le deuxième sous-déterminant (mineur de $L_{44}$, que nous appellerons $M(\lambda)$) :
    $$
    M(\lambda) = \begin{vmatrix}
    2-\lambda & -1 & -1 \\
    -1 & 2-\lambda & -1 \\
    -1 & -1 & 3-\lambda
    \end{vmatrix}
    $$
    $$
    M(\lambda) = (2-\lambda)[(2-\lambda)(3-\lambda)-(-1)(-1)] - (-1)[(-1)(3-\lambda)-(-1)(-1)] + (-1)[(-1)(-1)-(2-\lambda)(-1)]
    $$
    $$
    M(\lambda) = (2-\lambda)[\lambda^2-5\lambda+6-1] + [-(3-\lambda)-1] - [1+(2-\lambda)]
    $$
    $$
    M(\lambda) = (2-\lambda)(\lambda^2-5\lambda+5) + (\lambda-4) - (3-\lambda)
    $$
    $$
    M(\lambda) = (2\lambda^2-10\lambda+10-\lambda^3+5\lambda^2-5\lambda) + \lambda-4-3+\lambda
    $$
    $$
    M(\lambda) = -\lambda^3 + 7\lambda^2 - 15\lambda + 11
    $$
    En substituant ces résultats dans l'équation caractéristique :
    $$
    \det(L - \lambda I) = (-1) \cdot (-1) \cdot (-(\lambda-1)(\lambda-3)) + (1-\lambda) \cdot (1) \cdot (-\lambda^3 + 7\lambda^2 - 15\lambda + 11)
    $$
    $$
    \det(L - \lambda I) = -(\lambda-1)(\lambda-3) - (\lambda-1)(-\lambda^3 + 7\lambda^2 - 15\lambda + 11)
    $$
    $$
    \det(L - \lambda I) = (\lambda-1)[-(\lambda-3) - (-\lambda^3 + 7\lambda^2 - 15\lambda + 11)]
    $$
    $$
    \det(L - \lambda I) = (\lambda-1)[-\lambda+3 + \lambda^3 - 7\lambda^2 + 15\lambda - 11]
    $$
    $$
    \det(L - \lambda I) = (\lambda-1)[\lambda^3 - 7\lambda^2 + 14\lambda - 8]
    $$
    Nous savons que le graphe est connexe, donc $\lambda_1=0$ doit être une valeur propre. Cela signifie que $\det(L)=0$. Vérifions si $\lambda=0$ est une racine du polynôme caractéristique :
    $P(0) = (0-1)[0^3 - 7(0)^2 + 14(0) - 8] = (-1)(-8) = 8$.
    Il y a une erreur dans le calcul du polynôme caractéristique. Reprenons l'expansion du déterminant.

    La méthode la plus fiable pour un petit déterminant est de le calculer directement.
    $L = \begin{pmatrix}
    2 & -1 & -1 & 0 \\
    -1 & 2 & -1 & 0 \\
    -1 & -1 & 3 & -1 \\
    0 & 0 & -1 & 1
    \end{pmatrix}$
    On sait que $\lambda=0$ est une valeur propre car $G$ est connexe.
    On peut vérifier que $L \mathbf{1} = \mathbf{0}$, où $\mathbf{1}=(1,1,1,1)^T$.
    $\begin{pmatrix}
    2 & -1 & -1 & 0 \\
    -1 & 2 & -1 & 0 \\
    -1 & -1 & 3 & -1 \\
    0 & 0 & -1 & 1
    \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2-1-1+0 \\ -1+2-1+0 \\ -1-1+3-1 \\ 0+0-1+1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}$.
    Donc $\lambda_1=0$ est bien une valeur propre.

    Pour trouver les autres valeurs propres, nous pouvons utiliser la propriété que $\det(L-\lambda I)$ doit être divisible par $\lambda$.
    Le polynôme caractéristique est $\lambda^4 - 8\lambda^3 + 19\lambda^2 - 12\lambda$.
    Factorisons $\lambda$: $\lambda(\lambda^3 - 8\lambda^2 + 19\lambda - 12)$.
    Cherchons les racines du polynôme cubique $P(\lambda) = \lambda^3 - 8\lambda^2 + 19\lambda - 12$.
    Testons des diviseurs de 12 :
    *   $P(1) = 1 - 8 + 19 - 12 = 0$. Donc $\lambda=1$ est une racine.
    *   $P(2) = 8 - 8(4) + 19(2) - 12 = 8 - 32 + 38 - 12 = 2$.
    *   $P(3) = 27 - 8(9) + 19(3) - 12 = 27 - 72 + 57 - 12 = 0$. Donc $\lambda=3$ est une racine.
    *   $P(4) = 64 - 8(16) + 19(4) - 12 = 64 - 128 + 76 - 12 = 0$. Donc $\lambda=4$ est une racine.

    Les valeurs propres de $L$ sont donc $\lambda_1=0, \lambda_2=1, \lambda_3=3, \lambda_4=4$.

    La plus petite valeur propre est $\lambda_1=0$. Son espace propre est engendré par le vecteur $\mathbf{1}=(1,1,1,1)^T$. Puisque le graphe est connexe, l'espace propre de $\lambda_1=0$ est de dimension 1, ce qui est cohérent avec le fait que $G$ n'a qu'une seule composante connexe.

5.  **Valeur propre de Fiedler et vecteur de Fiedler :**

    La deuxième plus petite valeur propre est $\lambda_2=1$. C'est la valeur propre de Fiedler.
    Pour trouver le vecteur propre associé $v_2=(x_1, x_2, x_3, x_4)^T$, nous résolvons $(L - \lambda_2 I)v_2 = \mathbf{0}$, c'est-à-dire $(L - I)v_2 = \mathbf{0}$.
    $$
    (L - I) = \begin{pmatrix}
    2-1 & -1 & -1 & 0 \\
    -1 & 2-1 & -1 & 0 \\
    -1 & -1 & 3-1 & -1 \\
    0 & 0 & -1 & 1-1
    \end{pmatrix} = \begin{pmatrix}
    1 & -1 & -1 & 0 \\
    -1 & 1 & -1 & 0 \\
    -1 & -1 & 2 & -1 \\
    0 & 0 & -1 & 0
    \end{pmatrix}
    $$
    Le système d'équations est :
    1.  $x_1 - x_2 - x_3 = 0$
    2.  $-x_1 + x_2 - x_3 = 0$
    3.  $-x_1 - x_2 + 2x_3 - x_4 = 0$
    4.  $-x_3 = 0$

    De l'équation (4), nous avons $x_3 = 0$.
    Substituons $x_3=0$ dans l'équation (1) : $x_1 - x_2 = 0 \Rightarrow x_1 = x_2$.
    Substituons $x_3=0$ dans l'équation (2) : $-x_1 + x_2 = 0 \Rightarrow x_1 = x_2$. (Cohérent)
    Substituons $x_1=x_2$ et $x_3=0$ dans l'équation (3) : $-x_1 - x_1 + 2(0) - x_4 = 0 \Rightarrow -2x_1 - x_4 = 0 \Rightarrow x_4 = -2x_1$.

    Choisissons $x_1=1$. Alors $x_2=1$, $x_3=0$, $x_4=-2$.
    Le vecteur de Fiedler est $v_2 = (1, 1, 0, -2)^T$.

## Partie 2 : Coupures et Partitionnement Spectral

1.  **Définition d'une coupure et de sa capacité :**

    Une coupure $(S, \bar{S})$ d'un graphe $G=(V,E)$ est une partition des sommets $V$ en deux sous-ensembles non vides et disjoints $S$ et $\bar{S} = V \setminus S$.
    La capacité (ou poids) de la coupure, notée $cut(S, \bar{S})$, est le nombre d'arêtes ayant une extrémité dans $S$ et l'autre dans $\bar{S}$. Formellement :
    $$
    cut(S, \bar{S}) = |\{(u,v) \in E \mid u \in S, v \in \bar{S}\}|
    $$

2.  **Coupures minimales de $G$ par inspection :**

    Le graphe $G$ est :
    ```
    1 -- 2
    |  /
    3 -- 4
    ```
    Listons quelques coupures et leur capacité :
    *   $S=\{1\}$, $\bar{S}=\{2,3,4\}$ : Arêtes coupées : $(1,2), (1,3)$. $cut(S,\bar{S}) = 2$.
    *   $S=\{2\}$, $\bar{S}=\{1,3,4\}$ : Arêtes coupées : $(1,2), (2,3)$. $cut(S,\bar{S}) = 2$.
    *   $S=\{3\}$, $\bar{S}=\{1,2,4\}$ : Arêtes coupées : $(1,3), (2,3), (3,4)$. $cut(S,\bar{S}) = 3$.
    *   $S=\{4\}$, $\bar{S}=\{1,2,3\}$ : Arêtes coupées : $(3,4)$. $cut(S,\bar{S}) = 1$.
    *   $S=\{1,2\}$, $\bar{S}=\{3,4\}$ : Arêtes coupées : $(1,3), (2,3)$. $cut(S,\bar{S}) = 2$.
    *   $S=\{1,4\}$, $\bar{S}=\{2,3\}$ : Arêtes coupées : $(1,2), (1,3), (3,4)$. $cut(S,\bar{S}) = 3$.

    La coupure minimale est $cut(\{4\}, \{1,2,3\}) = 1$.

3.  **Partitionnement spectral avec le vecteur de Fiedler :**

    Le principe du partitionnement spectral est d'utiliser les signes des composantes du vecteur de Fiedler pour diviser le graphe en deux sous-ensembles. Les sommets dont la composante est positive vont dans un ensemble, et ceux dont la composante est négative vont dans l'autre. Les sommets dont la composante est nulle peuvent être assignés arbitrairement ou former un troisième ensemble.

    Le vecteur de Fiedler est $v_2 = (1, 1, 0, -2)^T$.
    *   Les sommets avec une composante positive sont $S_+ = \{1, 2\}$.
    *   Les sommets avec une composante négative sont $S_- = \{4\}$.
    *   Les sommets avec une composante nulle sont $S_0 = \{3\}$.

    Pour obtenir une partition binaire $(S, \bar{S})$, nous pouvons choisir un seuil. Une méthode courante est de regrouper les sommets avec des valeurs positives ou nulles dans un ensemble, et les négatives dans l'autre.
    Soit $S = \{i \mid v_2(i) \ge 0\} = \{1,2,3\}$.
    Alors $\bar{S} = \{i \mid v_2(i) < 0\} = \{4\}$.

    La coupure obtenue est $(\{1,2,3\}, \{4\})$.
    La capacité de cette coupure est $cut(\{1,2,3\}, \{4\}) = |\{(u,v) \in E \mid u \in \{1,2,3\}, v \in \{4\}\}|$.
    La seule arête qui correspond à cette condition est $(3,4)$.
    Donc $cut(\{1,2,3\}, \{4\}) = 1$.

    Comparaison : La coupure obtenue par le partitionnement spectral en utilisant le signe du vecteur de Fiedler correspond exactement à la coupure minimale trouvée par inspection. C'est un exemple où le partitionnement spectral donne une coupure optimale.

## Partie 3 : Le Laplacien Normalisé (Introduction)

1.  **Définition de la matrice des degrés inverse $D^{-1/2}$ :**

    La matrice $D^{-1/2}$ est une matrice diagonale dont les éléments diagonaux sont les inverses des racines carrées des degrés des sommets.
    $D_{ii}^{-1/2} = 1/\sqrt{d(i)}$.
    Pour notre graphe, les degrés sont $d(1)=2, d(2)=2, d(3)=3, d(4)=1$.
    $$
    D^{-1/2} = \begin{pmatrix}
    1/\sqrt{2} & 0 & 0 & 0 \\
    0 & 1/\sqrt{2} & 0 & 0 \\
    0 & 0 & 1/\sqrt{3} & 0 \\
    0 & 0 & 0 & 1/\sqrt{1}
    \end{pmatrix} = \begin{pmatrix}
    1/\sqrt{2} & 0 & 0 & 0 \\
    0 & 1/\sqrt{2} & 0 & 0 \\
    0 & 0 & 1/\sqrt{3} & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix}
    $$

2.  **Calcul du Laplacien normalisé $L_{norm} = D^{-1/2} L D^{-1/2}$ :**

    Les éléments de $L_{norm}$ sont donnés par :
    *   $(L_{norm})_{ii} = 1$
    *   $(L_{norm})_{ij} = -1/\sqrt{d(i)d(j)}$ si $(i,j) \in E$
    *   $(L_{norm})_{ij} = 0$ si $i \neq j$ et $(i,j) \notin E$

    $$
    L_{norm} = \begin{pmatrix}
    1 & -1/\sqrt{2 \cdot 2} & -1/\sqrt{2 \cdot 3} & 0 \\
    -1/\sqrt{2 \cdot 2} & 1 & -1/\sqrt{2 \cdot 3} & 0 \\
    -1/\sqrt{2 \cdot 3} & -1/\sqrt{2 \cdot 3} & 1 & -1/\sqrt{3 \cdot 1} \\
    0 & 0 & -1/\sqrt{3 \cdot 1} & 1
    \end{pmatrix}
    $$
    $$
    L_{norm} = \begin{pmatrix}
    1 & -1/2 & -1/\sqrt{6} & 0 \\
    -1/2 & 1 & -1/\sqrt{6} & 0 \\
    -1/\sqrt{6} & -1/\sqrt{6} & 1 & -1/\sqrt{3} \\
    0 & 0 & -1/\sqrt{3} & 1
    \end{pmatrix}
    $$

3.  **Plus petite valeur propre de $L_{norm}$ et son vecteur propre :**

    Le Laplacien normalisé a toujours 0 comme plus petite valeur propre si le graphe est connexe.
    Le vecteur propre associé est $D^{1/2}\mathbf{1}$, où $\mathbf{1}$ est le vecteur de tous les uns.
    $$
    D^{1/2}\mathbf{1} = \begin{pmatrix}
    \sqrt{2} & 0 & 0 & 0 \\
    0 & \sqrt{2} & 0 & 0 \\
    0 & 0 & \sqrt{3} & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} \sqrt{2} \\ \sqrt{2} \\ \sqrt{3} \\ 1 \end{pmatrix}
    $$
    Vérification :
    $L_{norm} (D^{1/2}\mathbf{1}) = D^{-1/2} L D^{-1/2} (D^{1/2}\mathbf{1}) = D^{-1/2} L \mathbf{1} = D^{-1/2} \mathbf{0} = \mathbf{0}$.
    Donc $\lambda_1(L_{norm})=0$ avec vecteur propre $v_1 = (\sqrt{2}, \sqrt{2}, \sqrt{3}, 1)^T$.

4.  **Pourquoi le Laplacien normalisé est préféré pour le partitionnement de graphes :**

    Le Laplacien combinatoire $L$ tend à favoriser les coupures qui séparent les sommets de faible degré, même si ces coupures ne sont pas "équilibrées" en termes de volume (somme des degrés) des partitions. Par exemple, couper un sommet de degré 1 d'un grand graphe aura toujours un coût de 1, ce qui peut être la coupure minimale pour $L$, mais n'est pas nécessairement une bonne partition.

    Le Laplacien normalisé $L_{norm}$ est conçu pour atténuer ce biais. Ses valeurs propres sont directement liées à la *conductance* des coupures, une mesure de qualité qui prend en compte le volume des partitions. La conductance d'une coupure $(S, \bar{S})$ est définie comme $\phi(S) = \frac{cut(S, \bar{S})}{\min(vol(S), vol(\bar{S}))}$, où $vol(S) = \sum_{u \in S} d(u)$. Cette mesure pénalise les coupures qui isolent de petits ensembles de sommets de faible degré.

    En d'autres termes, $L_{norm}$ est plus adapté pour trouver des coupures qui sont "équilibrées" par rapport aux degrés des sommets, ce qui est souvent désirable dans des applications comme le clustering de données ou la segmentation d'images, où l'on souhaite des partitions de taille comparable ou de volume comparable. La deuxième plus petite valeur propre de $L_{norm}$ (la valeur propre de Cheeger) est étroitement liée à la conductance minimale du graphe via l'inégalité de Cheeger, fournissant une borne inférieure et supérieure pour cette mesure.

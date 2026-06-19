---
uuid: "exo-7-1"
title: "Exo 1 - Jalon 7"
---
Cher étudiant,

Nous allons explorer les fondements des espaces vectoriels abstraits à travers un exemple concret mais non trivial. L'objectif de cet exercice est de consolider votre compréhension des définitions clés telles que l'espace vectoriel, la famille libre, la famille génératrice, la base et la dimension, dans un cadre qui s'éloigne des espaces $\mathbb{R}^n$ habituels.

Soit $\mathcal{M}_2(\mathbb{R})$ l'ensemble des matrices carrées d'ordre 2 à coefficients réels. Nous considérons l'ensemble $E$ défini comme suit :
$$ E = \left\{ M \in \mathcal{M}_2(\mathbb{R}) \mid \text{Tr}(M) = 0 \right\} $$
où $\text{Tr}(M)$ désigne la trace de la matrice $M$. Rappelons que pour une matrice $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$, sa trace est donnée par $\text{Tr}(M) = a+d$.

1.  Démontrez que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$. Précisez le corps de base et les opérations vectorielles considérées.
2.  Considérons la famille de matrices $S = \{M_1, M_2, M_3\}$ où :
    $$ M_1 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad M_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad M_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} $$
    a.  Vérifiez que chaque matrice de la famille $S$ appartient bien à $E$.
    b.  La famille $S$ est-elle une famille libre (linéairement indépendante) dans $E$ ? Justifiez rigoureusement votre réponse en détaillant chaque étape.
    c.  La famille $S$ est-elle une famille génératrice de $E$ ? Justifiez rigoureusement votre réponse en détaillant chaque étape.
    d.  La famille $S$ est-elle une base de $E$ ? Justifiez rigoureusement votre réponse.
3.  Quelle est la dimension de l'espace vectoriel $E$ ? Justifiez votre réponse.

---

### Correction Détaillée

Nous allons aborder chaque question avec la rigueur nécessaire, en explicitant chaque définition et chaque étape de raisonnement ou de calcul.

#### 1. Démonstration que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$

Pour démontrer que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$, nous devons vérifier trois conditions fondamentales, en considérant $\mathcal{M}_2(\mathbb{R})$ comme un espace vectoriel sur le corps $K = \mathbb{R}$ avec l'addition matricielle et la multiplication par un scalaire usuelles.

**Condition 1 : L'ensemble $E$ est non vide.**
Pour prouver que $E$ est non vide, il suffit de montrer qu'il contient au moins un élément. Le plus simple est de vérifier si la matrice nulle $\mathbf{0}_{2,2}$ de $\mathcal{M}_2(\mathbb{R})$ appartient à $E$.
La matrice nulle est $\mathbf{0}_{2,2} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
Sa trace est $\text{Tr}(\mathbf{0}_{2,2}) = 0+0 = 0$.
Puisque $\text{Tr}(\mathbf{0}_{2,2}) = 0$, la matrice nulle $\mathbf{0}_{2,2}$ appartient bien à $E$.
Par conséquent, $E$ est un ensemble non vide.

**Condition 2 : $E$ est stable par addition vectorielle.**
Soient $M$ et $N$ deux matrices quelconques appartenant à $E$. Nous devons montrer que leur somme $M+N$ appartient également à $E$.
Puisque $M \in E$, par définition de $E$, nous avons $\text{Tr}(M) = 0$.
Puisque $N \in E$, par définition de $E$, nous avons $\text{Tr}(N) = 0$.
Considérons la somme $M+N$. La trace de la somme de deux matrices est égale à la somme de leurs traces. C'est une propriété fondamentale de l'opérateur trace.
Ainsi, $\text{Tr}(M+N) = \text{Tr}(M) + \text{Tr}(N)$.
En substituant les valeurs des traces que nous connaissons :
$\text{Tr}(M+N) = 0 + 0 = 0$.
Puisque $\text{Tr}(M+N) = 0$, la matrice $M+N$ satisfait la condition d'appartenance à $E$.
Par conséquent, $M+N \in E$. L'ensemble $E$ est stable par addition vectorielle.

**Condition 3 : $E$ est stable par multiplication par un scalaire.**
Soit $\lambda$ un scalaire réel (c'est-à-dire $\lambda \in \mathbb{R}$) et soit $M$ une matrice quelconque appartenant à $E$. Nous devons montrer que le produit scalaire $\lambda M$ appartient également à $E$.
Puisque $M \in E$, par définition de $E$, nous avons $\text{Tr}(M) = 0$.
Considérons le produit $\lambda M$. La trace d'une matrice multipliée par un scalaire est égale au scalaire multiplié par la trace de la matrice. C'est une autre propriété fondamentale de l'opérateur trace.
Ainsi, $\text{Tr}(\lambda M) = \lambda \cdot \text{Tr}(M)$.
En substituant la valeur de la trace de $M$ :
$\text{Tr}(\lambda M) = \lambda \cdot 0 = 0$.
Puisque $\text{Tr}(\lambda M) = 0$, la matrice $\lambda M$ satisfait la condition d'appartenance à $E$.
Par conséquent, $\lambda M \in E$. L'ensemble $E$ est stable par multiplication par un scalaire.

Les trois conditions étant vérifiées, nous pouvons conclure que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$. Le corps de base est $\mathbb{R}$, et les opérations vectorielles sont l'addition matricielle et la multiplication d'une matrice par un scalaire réel.

#### 2. Analyse de la famille $S = \{M_1, M_2, M_3\}$

##### 2.a. Vérification de l'appartenance des matrices de $S$ à $E$

Nous devons vérifier que chaque matrice de la famille $S$ a une trace nulle.

*   Pour $M_1 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ :
    $\text{Tr}(M_1) = 1 + (-1) = 0$.
    Donc, $M_1 \in E$.

*   Pour $M_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ :
    $\text{Tr}(M_2) = 0 + 0 = 0$.
    Donc, $M_2 \in E$.

*   Pour $M_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ :
    $\text{Tr}(M_3) = 0 + 0 = 0$.
    Donc, $M_3 \in E$.

Chaque matrice de la famille $S$ appartient bien à l'espace vectoriel $E$.

##### 2.b. La famille $S$ est-elle une famille libre dans $E$ ?

Une famille de vecteurs $\{v_1, v_2, \dots, v_k\}$ d'un espace vectoriel $V$ est dite libre (ou linéairement indépendante) si la seule combinaison linéaire de ces vecteurs qui est égale au vecteur nul de $V$ est celle où tous les coefficients scalaires sont nuls.
Dans notre cas, les vecteurs sont les matrices $M_1, M_2, M_3$ et le vecteur nul de $E$ (et de $\mathcal{M}_2(\mathbb{R})$) est la matrice nulle $\mathbf{0}_{2,2}$.
Soient $\alpha_1, \alpha_2, \alpha_3$ des scalaires réels (c'est-à-dire $\alpha_1, \alpha_2, \alpha_3 \in \mathbb{R}$).
Nous posons l'équation de combinaison linéaire égale au vecteur nul :
$$ \alpha_1 M_1 + \alpha_2 M_2 + \alpha_3 M_3 = \mathbf{0}_{2,2} $$
Substituons les matrices :
$$ \alpha_1 \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + \alpha_2 \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + \alpha_3 \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} $$
Effectuons la multiplication par les scalaires :
$$ \begin{pmatrix} \alpha_1 & 0 \\ 0 & -\alpha_1 \end{pmatrix} + \begin{pmatrix} 0 & \alpha_2 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ \alpha_3 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} $$
Effectuons l'addition des matrices :
$$ \begin{pmatrix} \alpha_1 + 0 + 0 & 0 + \alpha_2 + 0 \\ 0 + 0 + \alpha_3 & -\alpha_1 + 0 + 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} $$
Ce qui simplifie en :
$$ \begin{pmatrix} \alpha_1 & \alpha_2 \\ \alpha_3 & -\alpha_1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} $$
Pour que deux matrices soient égales, leurs éléments correspondants doivent être égaux. Cela nous donne un système de quatre équations linéaires :
1.  $\alpha_1 = 0$
2.  $\alpha_2 = 0$
3.  $\alpha_3 = 0$
4.  $-\alpha_1 = 0$

La première équation $\alpha_1 = 0$ et la quatrième équation $-\alpha_1 = 0$ sont cohérentes et impliquent toutes deux que $\alpha_1$ doit être nul.
Les équations 2 et 3 nous donnent directement $\alpha_2 = 0$ et $\alpha_3 = 0$.
Ainsi, la seule solution à l'équation de combinaison linéaire est $\alpha_1 = 0$, $\alpha_2 = 0$, et $\alpha_3 = 0$.
Par conséquent, la famille $S = \{M_1, M_2, M_3\}$ est une famille libre dans $E$.

##### 2.c. La famille $S$ est-elle une famille génératrice de $E$ ?

Une famille de vecteurs $S = \{v_1, v_2, \dots, v_k\}$ d'un espace vectoriel $V$ est dite génératrice de $V$ si tout vecteur de $V$ peut être exprimé comme une combinaison linéaire des vecteurs de $S$.
Soit $M$ une matrice quelconque appartenant à $E$. Par définition de $E$, $M$ est une matrice $2 \times 2$ à coefficients réels dont la trace est nulle.
Nous pouvons écrire $M$ sous la forme générale :
$$ M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} $$
Puisque $M \in E$, nous savons que $\text{Tr}(M) = a+d = 0$. Cette condition implique que $d = -a$.
Ainsi, toute matrice $M \in E$ peut être écrite sous la forme :
$$ M = \begin{pmatrix} a & b \\ c & -a \end{pmatrix} $$
Nous devons déterminer s'il existe des scalaires réels $\alpha_1, \alpha_2, \alpha_3$ tels que $M$ puisse être exprimée comme une combinaison linéaire des matrices de $S$ :
$$ M = \alpha_1 M_1 + \alpha_2 M_2 + \alpha_3 M_3 $$
Substituons les matrices de $S$ :
$$ \begin{pmatrix} a & b \\ c & -a \end{pmatrix} = \alpha_1 \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + \alpha_2 \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + \alpha_3 \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} $$
Effectuons la combinaison linéaire des matrices de droite, comme nous l'avons fait à la question 2.b :
$$ \begin{pmatrix} a & b \\ c & -a \end{pmatrix} = \begin{pmatrix} \alpha_1 & \alpha_2 \\ \alpha_3 & -\alpha_1 \end{pmatrix} $$
En égalant les éléments correspondants des deux matrices, nous obtenons le système d'équations suivant :
1.  $a = \alpha_1$
2.  $b = \alpha_2$
3.  $c = \alpha_3$
4.  $-a = -\alpha_1$

Les équations 1 et 4 sont cohérentes et nous donnent $\alpha_1 = a$.
Les équations 2 et 3 nous donnent directement $\alpha_2 = b$ et $\alpha_3 = c$.
Pour toute matrice $M = \begin{pmatrix} a & b \\ c & -a \end{pmatrix}$ dans $E$, nous avons trouvé des scalaires $\alpha_1 = a$, $\alpha_2 = b$, et $\alpha_3 = c$ qui permettent d'exprimer $M$ comme une combinaison linéaire des matrices de $S$. Ces scalaires sont uniques pour chaque matrice $M$.
Puisque tout élément de $E$ peut être écrit comme une combinaison linéaire des éléments de $S$, la famille $S = \{M_1, M_2, M_3\}$ est une famille génératrice de $E$.

##### 2.d. La famille $S$ est-elle une base de $E$ ?

Une famille de vecteurs est une base d'un espace vectoriel si et seulement si elle est à la fois une famille libre et une famille génératrice de cet espace.
D'après la question 2.b, nous avons démontré que la famille $S$ est une famille libre dans $E$.
D'après la question 2.c, nous avons démontré que la famille $S$ est une famille génératrice de $E$.
Puisque la famille $S$ satisfait ces deux conditions, nous pouvons conclure que la famille $S = \{M_1, M_2, M_3\}$ est une base de l'espace vectoriel $E$.

#### 3. Dimension de l'espace vectoriel $E$

La dimension d'un espace vectoriel est définie comme le nombre de vecteurs dans n'importe laquelle de ses bases.
D'après la question 2.d, nous avons établi que la famille $S = \{M_1, M_2, M_3\}$ est une base de l'espace vectoriel $E$.
La famille $S$ contient exactement 3 vecteurs (qui sont des matrices dans ce contexte).
Par conséquent, la dimension de l'espace vectoriel $E$ est 3.
Nous pouvons écrire $\text{dim}(E) = 3$.

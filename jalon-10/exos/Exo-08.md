```yaml
---
title: "Exercice 08 : Changements de Base, Matrices de Passage et Matrices par Blocs"
subtitle: "Application à une Transformation Linéaire en Dimension 3"
authors:
  - Prénom Nom
date: 2023-10-27
keywords:
  - Algèbre Linéaire
  - Changement de base
  - Matrice de passage
  - Matrice inverse
  - Matrice par blocs
  - Transformation linéaire
  - Espace vectoriel
  - Sous-espace invariant
description: "Cet exercice approfondit les concepts de changements de base, de matrices de passage et de matrices par blocs à travers l'étude d'une transformation linéaire en dimension 3. Il exige une rigueur dans les calculs matriciels et une compréhension des structures sous-jacentes des espaces vectoriels et des transformations."
tags:
  - Mathématiques pour l'IA
  - L1
  - L2
  - L3
  - M1
  - Algèbre
  - Exercice
course: "Mathématiques pour l'Intelligence Artificielle"
level: "L1 à Master"
jalon: "Jalon 10"
exercice: "Exo-08"
difficulty: 4/5
---
```

# Exercice 08 : Changements de Base, Matrices de Passage et Matrices par Blocs

## Introduction

Cet exercice est conçu pour consolider votre compréhension des concepts fondamentaux de l'algèbre linéaire, en particulier les changements de base, la construction et l'utilisation des matrices de passage, ainsi que l'interprétation des matrices par blocs. Nous allons explorer ces notions à travers l'étude d'une transformation linéaire spécifique dans un espace vectoriel de dimension 3. Une attention particulière sera portée à la rigueur des calculs et à la justification de chaque étape.

---

## Partie 1 : Représentation dans la Base Canonique et Changement de Base

Soit $\mathbb{K}$ le corps des nombres réels, c'est-à-dire $\mathbb{K} = \mathbb{R}$.
Soit $E$ un espace vectoriel sur $\mathbb{K}$, défini comme $E = \mathbb{R}^3$.
Soit $\mathcal{B}_c = (e_1, e_2, e_3)$ la base canonique de $E$, où $e_1 = (1,0,0)$, $e_2 = (0,1,0)$ et $e_3 = (0,0,1)$.

Soit $f: E \to E$ une application linéaire définie pour tout vecteur $v = (x,y,z) \in E$ par :
$$f(x,y,z) = (2x+y, x+2y, z)$$

### Question 1.1 : Matrice de $f$ dans la base canonique

Déterminer la matrice $A$ de l'application linéaire $f$ dans la base canonique $\mathcal{B}_c$.

#### Solution 1.1

Pour déterminer la matrice $A$ de $f$ dans la base canonique $\mathcal{B}_c$, nous devons calculer l'image de chaque vecteur de base $e_i$ par $f$ et exprimer ces images comme combinaisons linéaires des vecteurs de $\mathcal{B}_c$. Les coordonnées obtenues formeront les colonnes de la matrice $A$.

1.  Calcul de $f(e_1)$:
    Le vecteur $e_1$ est $(1,0,0)$.
    $f(e_1) = f(1,0,0) = (2(1)+0, 1+2(0), 0) = (2,1,0)$.
    En termes de la base $\mathcal{B}_c$, $f(e_1) = 2e_1 + 1e_2 + 0e_3$.

2.  Calcul de $f(e_2)$:
    Le vecteur $e_2$ est $(0,1,0)$.
    $f(e_2) = f(0,1,0) = (2(0)+1, 0+2(1), 0) = (1,2,0)$.
    En termes de la base $\mathcal{B}_c$, $f(e_2) = 1e_1 + 2e_2 + 0e_3$.

3.  Calcul de $f(e_3)$:
    Le vecteur $e_3$ est $(0,0,1)$.
    $f(e_3) = f(0,0,1) = (2(0)+0, 0+2(0), 1) = (0,0,1)$.
    En termes de la base $\mathcal{B}_c$, $f(e_3) = 0e_1 + 0e_2 + 1e_3$.

La matrice $A$ est formée en plaçant les vecteurs de coordonnées de $f(e_1)$, $f(e_2)$, $f(e_3)$ en colonnes :
$$A = \begin{pmatrix}
2 & 1 & 0 \\
1 & 2 & 0 \\
0 & 0 & 1
\end{pmatrix}$$

### Question 1.2 : Définition d'une nouvelle base

Soit $\mathcal{B}' = (u_1, u_2, u_3)$ une nouvelle famille de vecteurs de $E$, où :
$u_1 = (1,1,0)$
$u_2 = (1,-1,0)$
$u_3 = (0,0,1)$

Vérifier que $\mathcal{B}'$ est bien une base de $E$.

#### Solution 1.2

Pour vérifier que $\mathcal{B}' = (u_1, u_2, u_3)$ est une base de l'espace vectoriel $E = \mathbb{R}^3$, il suffit de montrer que les vecteurs $u_1, u_2, u_3$ sont linéairement indépendants. Puisque la dimension de $E$ est 3 et que nous avons 3 vecteurs, l'indépendance linéaire est une condition suffisante pour qu'ils forment une base.

Nous pouvons tester l'indépendance linéaire en formant une matrice avec ces vecteurs en colonnes (ou en lignes) et en calculant son déterminant. Si le déterminant est non nul, les vecteurs sont linéairement indépendants.

Soit la matrice $M$ dont les colonnes sont les vecteurs $u_1, u_2, u_3$ exprimés dans la base canonique $\mathcal{B}_c$:
$$M = \begin{pmatrix}
1 & 1 & 0 \\
1 & -1 & 0 \\
0 & 0 & 1
\end{pmatrix}$$

Calculons le déterminant de $M$ en développant par rapport à la troisième ligne (ou troisième colonne) :
$$\det(M) = 0 \cdot \text{cofacteur}_{31} + 0 \cdot \text{cofacteur}_{32} + 1 \cdot \text{cofacteur}_{33}$$
$$\det(M) = 1 \cdot (-1)^{3+3} \det \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
$$\det(M) = 1 \cdot ((1)(-1) - (1)(1))$$
$$\det(M) = 1 \cdot (-1 - 1)$$
$$\det(M) = 1 \cdot (-2)$$
$$\det(M) = -2$$

Puisque $\det(M) = -2 \neq 0$, les vecteurs $u_1, u_2, u_3$ sont linéairement indépendants.
Par conséquent, $\mathcal{B}'$ est bien une base de $E = \mathbb{R}^3$.

### Question 1.3 : Matrices de passage

Déterminer la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ de la base $\mathcal{B}'$ à la base canonique $\mathcal{B}_c$.
En déduire la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ de la base canonique $\mathcal{B}_c$ à la base $\mathcal{B}'$. Détailler le calcul de l'inverse.

#### Solution 1.3

1.  **Matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ (de $\mathcal{B}'$ vers $\mathcal{B}_c$)**

    La matrice de passage de $\mathcal{B}'$ à $\mathcal{B}_c$, notée $P_{\mathcal{B}' \to \mathcal{B}_c}$, a pour colonnes les coordonnées des vecteurs de la base $\mathcal{B}'$ exprimées dans la base $\mathcal{B}_c$.
    Nous avons :
    $u_1 = (1,1,0) = 1e_1 + 1e_2 + 0e_3$
    $u_2 = (1,-1,0) = 1e_1 - 1e_2 + 0e_3$
    $u_3 = (0,0,1) = 0e_1 + 0e_2 + 1e_3$

    Donc, la matrice $P_{\mathcal{B}' \to \mathcal{B}_c}$ est :
    $$P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 1 & 0 \\
    1 & -1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$
    *Note : Cette matrice est la même que la matrice $M$ utilisée pour vérifier l'indépendance linéaire des vecteurs de $\mathcal{B}'$.*

2.  **Matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ (de $\mathcal{B}_c$ vers $\mathcal{B}'$)**

    La matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ est l'inverse de la matrice $P_{\mathcal{B}' \to \mathcal{B}_c}$.
    Nous devons donc calculer $(P_{\mathcal{B}' \to \mathcal{B}_c})^{-1}$.
    Soit $P = P_{\mathcal{B}' \to \mathcal{B}_c}$. Nous avons $P = \begin{pmatrix} 1 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
    Nous avons déjà calculé $\det(P) = -2$.

    Nous allons utiliser la méthode de la comatrice pour calculer l'inverse.
    La matrice inverse $P^{-1}$ est donnée par la formule $P^{-1} = \frac{1}{\det(P)} \text{com}(P)^T$, où $\text{com}(P)$ est la comatrice de $P$ et $\text{com}(P)^T$ est la transposée de la comatrice (matrice des cofacteurs).

    Calculons les cofacteurs $C_{ij} = (-1)^{i+j} M_{ij}$, où $M_{ij}$ est le mineur de l'élément $p_{ij}$.

    *   $C_{11} = (-1)^{1+1} \det \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = 1 \cdot ((-1)(1) - (0)(0)) = -1$
    *   $C_{12} = (-1)^{1+2} \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = -1 \cdot ((1)(1) - (0)(0)) = -1$
    *   $C_{13} = (-1)^{1+3} \det \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} = 1 \cdot ((1)(0) - (-1)(0)) = 0$

    *   $C_{21} = (-1)^{2+1} \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = -1 \cdot ((1)(1) - (0)(0)) = -1$
    *   $C_{22} = (-1)^{2+2} \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 1 \cdot ((1)(1) - (0)(0)) = 1$
    *   $C_{23} = (-1)^{2+3} \det \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = -1 \cdot ((1)(0) - (1)(0)) = 0$

    *   $C_{31} = (-1)^{3+1} \det \begin{pmatrix} 1 & 0 \\ -1 & 0 \end{pmatrix} = 1 \cdot ((1)(0) - (0)(-1)) = 0$
    *   $C_{32} = (-1)^{3+2} \det \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = -1 \cdot ((1)(0) - (0)(1)) = 0$
    *   $C_{33} = (-1)^{3+3} \det \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = 1 \cdot ((1)(-1) - (1)(1)) = 1 \cdot (-1 - 1) = -2$

    La comatrice de $P$ est :
    $$\text{com}(P) = \begin{pmatrix}
    -1 & -1 & 0 \\
    -1 & 1 & 0 \\
    0 & 0 & -2
    \end{pmatrix}$$

    La transposée de la comatrice est :
    $$\text{com}(P)^T = \begin{pmatrix}
    -1 & -1 & 0 \\
    -1 & 1 & 0 \\
    0 & 0 & -2
    \end{pmatrix}$$
    *(Dans ce cas particulier, la comatrice est symétrique, donc sa transposée est elle-même.)*

    Enfin, la matrice inverse $P^{-1}$ est :
    $$P^{-1} = \frac{1}{\det(P)} \text{com}(P)^T = \frac{1}{-2} \begin{pmatrix}
    -1 & -1 & 0 \\
    -1 & 1 & 0 \\
    0 & 0 & -2
    \end{pmatrix}$$
    $$P^{-1} = \begin{pmatrix}
    \frac{-1}{-2} & \frac{-1}{-2} & \frac{0}{-2} \\
    \frac{-1}{-2} & \frac{1}{-2} & \frac{0}{-2} \\
    \frac{0}{-2} & \frac{0}{-2} & \frac{-2}{-2}
    \end{pmatrix} = \begin{pmatrix}
    1/2 & 1/2 & 0 \\
    1/2 & -1/2 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$

    Donc, la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ est :
    $$P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    1/2 & 1/2 & 0 \\
    1/2 & -1/2 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$

    *Vérification (étape non demandée mais essentielle pour la rigueur) :*
    Calculons le produit $P P^{-1}$ pour s'assurer qu'il s'agit bien de la matrice identité $I_3$ :
    $$P P^{-1} = \begin{pmatrix}
    1 & 1 & 0 \\
    1 & -1 & 0 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
    1/2 & 1/2 & 0 \\
    1/2 & -1/2 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$
    $$P P^{-1} = \begin{pmatrix}
    (1)(1/2) + (1)(1/2) + (0)(0) & (1)(1/2) + (1)(-1/2) + (0)(0) & (1)(0) + (1)(0) + (0)(1) \\
    (1)(1/2) + (-1)(1/2) + (0)(0) & (1)(1/2) + (-1)(-1/2) + (0)(0) & (1)(0) + (-1)(0) + (0)(1) \\
    (0)(1/2) + (0)(1/2) + (1)(0) & (0)(1/2) + (0)(-1/2) + (1)(0) & (0)(0) + (0)(0) + (1)(1)
    \end{pmatrix}$$
    $$P P^{-1} = \begin{pmatrix}
    1/2 + 1/2 + 0 & 1/2 - 1/2 + 0 & 0 + 0 + 0 \\
    1/2 - 1/2 + 0 & 1/2 + 1/2 + 0 & 0 + 0 + 0 \\
    0 + 0 + 0 & 0 + 0 + 0 & 0 + 0 + 1
    \end{pmatrix}$$
    $$P P^{-1} = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix} = I_3$$
    La vérification est concluante.

### Question 1.4 : Matrice de $f$ dans la nouvelle base

Déterminer la matrice $A'$ de l'application linéaire $f$ dans la base $\mathcal{B}'$ en utilisant la formule de changement de base : $A' = P^{-1} A P$, où $P = P_{\mathcal{B}' \to \mathcal{B}_c}$. Détailler toutes les multiplications matricielles étape par étape.

#### Solution 1.4

Nous avons les matrices suivantes :
$A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ (matrice de $f$ dans la base $\mathcal{B}_c$)
$P = \begin{pmatrix} 1 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ (matrice de passage de $\mathcal{B}'$ à $\mathcal{B}_c$)
$P^{-1} = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & -1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ (matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}'$)

Nous devons calculer $A' = P^{-1} A P$. Nous allons effectuer les multiplications matricielles séquentiellement, en calculant d'abord le produit $AP$, puis le produit $(P^{-1})(AP)$.

1.  **Calcul de $AP$ :**
    $$AP = \begin{pmatrix}
    2 & 1 & 0 \\
    1 & 2 & 0 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
    1 & 1 & 0 \\
    1 & -1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$
    Calcul des éléments de la matrice produit :
    *   $(AP)_{11} = (2)(1)+(1)(1)+(0)(0) = 2+1+0 = 3$
    *   $(AP)_{12} = (2)(1)+(1)(-1)+(0)(0) = 2-1+0 = 1$
    *   $(AP)_{13} = (2)(0)+(1)(0)+(0)(1) = 0+0+0 = 0$
    *   $(AP)_{21} = (1)(1)+(2)(1)+(0)(0) = 1+2+0 = 3$
    *   $(AP)_{22} = (1)(1)+(2)(-1)+(0)(0) = 1-2+0 = -1$
    *   $(AP)_{23} = (1)(0)+(2)(0)+(0)(1) = 0+0+0 = 0$
    *   $(AP)_{31} = (0)(1)+(0)(1)+(1)(0) = 0+0+0 = 0$
    *   $(AP)_{32} = (0)(1)+(0)(-1)+(1)(0) = 0+0+0 = 0$
    *   $(AP)_{33} = (0)(0)+(0)(0)+(1)(1) = 0+0+1 = 1$

    Donc, le produit $AP$ est :
    $$AP = \begin{pmatrix}
    3 & 1 & 0 \\
    3 & -1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$

2.  **Calcul de $P^{-1}(AP)$ :**
    $$A' = P^{-1} (AP) = \begin{pmatrix}
    1/2 & 1/2 & 0 \\
    1/2 & -1/2 & 0 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
    3 & 1 & 0 \\
    3 & -1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$
    Calcul des éléments de la matrice produit :
    *   $(A')_{11} = (1/2)(3)+(1/2)(3)+(0)(0) = 3/2+3/2+0 = 6/2 = 3$
    *   $(A')_{12} = (1/2)(1)+(1/2)(-1)+(0)(0) = 1/2-1/2+0 = 0$
    *   $(A')_{13} = (1/2)(0)+(1/2)(0)+(0)(1) = 0+0+0 = 0$
    *   $(A')_{21} = (1/2)(3)+(-1/2)(3)+(0)(0) = 3/2-3/2+0 = 0$
    *   $(A')_{22} = (1/2)(1)+(-1/2)(-1)+(0)(0) = 1/2+1/2+0 = 2/2 = 1$
    *   $(A')_{23} = (1/2)(0)+(-1/2)(0)+(0)(1) = 0+0+0 = 0$
    *   $(A')_{31} = (0)(3)+(0)(3)+(1)(0) = 0+0+0 = 0$
    *   $(A')_{32} = (0)(1)+(0)(-1)+(1)(0) = 0+0+0 = 0$
    *   $(A')_{33} = (0)(0)+(0)(0)+(1)(1) = 0+0+1 = 1$

    Ainsi, la matrice de l'application linéaire $f$ dans la base $\mathcal{B}'$ est :
    $$A' = \begin{pmatrix}
    3 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$$

---

## Partie 2 : Interprétation par Blocs

### Question 2.1 : Observation de la structure des matrices

Observer la structure des matrices $A$, $P$, $P^{-1}$ et $A'$. Mettre en évidence des sous-blocs significatifs.

#### Solution 2.1

Reprenons les matrices calculées :
$$A = \begin{pmatrix}
2 & 1 & 0 \\
1 & 2 & 0 \\
0 & 0 & 1
\end{pmatrix}$$
$$P = \begin{pmatrix}
1 & 1 & 0 \\
1 & -1 & 0 \\
0 & 0 & 1
\end{pmatrix}$$
$$P^{-1} = \begin{pmatrix}
1/2 & 1/2 & 0 \\
1/2 & -1/2 & 0 \\
0 & 0 & 1
\end{pmatrix}$$
$$A' = \begin{pmatrix}
3 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}$$

Nous pouvons observer une structure par blocs commune à toutes ces matrices. Elles peuvent être décomposées en blocs de la forme :
$$M = \begin{pmatrix}
M_{11} & M_{12} \\
M_{21} & M_{22}
\end{pmatrix}$$
où $M_{11}$ est une matrice $2 \times 2$, $M_{12}$ est une matrice $2 \times 1$, $M_{21}$ est une matrice $1 \times 2$, et $M_{22}$ est une matrice $1 \times 1$.

Pour la matrice $A$:
$$A = \begin{pmatrix}
\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} & \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\
\begin{pmatrix} 0 & 0 \end{pmatrix} & \begin{pmatrix} 1 \end{pmatrix}
\end{pmatrix}$$
Ici, $A_{11} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $A_{12} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $A_{21} = \begin{pmatrix} 0 & 0 \end{pmatrix}$, $A_{22} = \begin{pmatrix} 1 \end{pmatrix}$.

Pour la matrice $P$:
$$P = \begin{pmatrix}
\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} & \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\
\begin{pmatrix} 0 & 0 \end{pmatrix} & \begin{pmatrix} 1 \end{pmatrix}
\end{pmatrix}$$
Ici, $P_{11} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, $P_{12} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $P_{21} = \begin{pmatrix} 0 & 0 \end{pmatrix}$, $P_{22} = \begin{pmatrix} 1 \end{pmatrix}$.

Pour la matrice $P^{-1}$:
$$P^{-1} = \begin{pmatrix}
\begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix} & \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\
\begin{pmatrix} 0 & 0 \end{pmatrix} & \begin{pmatrix} 1 \end{pmatrix}
\end{pmatrix}$$
Ici, $(P^{-1})_{11} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}$, $(P^{-1})_{12} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $(P^{-1})_{21} = \begin{pmatrix} 0 & 0 \end{pmatrix}$, $(P^{-1})_{22} = \begin{pmatrix} 1 \end{pmatrix}$.

Pour la matrice $A'$:
$$A' = \begin{pmatrix}
\begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} & \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\
\begin{pmatrix} 0 & 0 \end{pmatrix} & \begin{pmatrix} 1 \end{pmatrix}
\end{pmatrix}$$
Ici, $A'_{11} = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$, $A'_{12} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $A'_{21} = \begin{pmatrix} 0 & 0 \end{pmatrix}$, $A'_{22} = \begin{pmatrix} 1 \end{pmatrix}$.

Toutes ces matrices sont de la forme $\begin{pmatrix} M_{11} & 0 \\ 0 & M_{22} \end{pmatrix}$, ce qui signifie qu'elles sont des matrices diagonales par blocs. Les blocs $M_{12}$ et $M_{21}$ sont des matrices nulles.

### Question 2.2 : Décomposition de l'espace et invariance

Soient $E_1$ le sous-espace vectoriel de $E$ engendré par les vecteurs $u_1 = (1,1,0)$ et $u_2 = (1,-1,0)$, et $E_2$ le sous-espace vectoriel de $E$ engendré par le vecteur $u_3 = (0,0,1)$.
1.  Montrer que $E = E_1 \oplus E_2$ (somme directe).
2.  Montrer que $E_1$ et $E_2$ sont des sous-espaces stables (ou invariants) par l'application linéaire $f$.

#### Solution 2.2

1.  **Montrer que $E = E_1 \oplus E_2$**

    *   **Définition des sous-espaces :**
        $E_1 = \text{Vect}(u_1, u_2) = \text{Vect}((1,1,0), (1,-1,0))$.
        $E_2 = \text{Vect}(u_3) = \text{Vect}((0,0,1))$.

    *   **Indépendance linéaire des générateurs et dimensions :**
        Les vecteurs $u_1 = (1,1,0)$ et $u_2 = (1,-1,0)$ sont linéairement indépendants car ils ne sont pas colinéaires (il n'existe pas de scalaire $k \in \mathbb{R}$ tel que $u_1 = k u_2$). Par exemple, la première composante de $u_1$ est 1 et celle de $u_2$ est 1, mais la deuxième composante de $u_1$ est 1 et celle de $u_2$ est -1. Donc, $\dim(E_1) = 2$.
        Le vecteur $u_3 = (0,0,1)$ est non nul, donc $\dim(E_2) = 1$.

    *   **Intersection $E_1 \cap E_2 = \{0\}$ :**
        Pour montrer que la somme est directe, nous devons prouver que l'intersection des deux sous-espaces est le vecteur nul.
        Soit $v \in E_1 \cap E_2$. Alors $v$ peut s'écrire comme une combinaison linéaire des vecteurs de base de $E_1$ et aussi comme un multiple du vecteur de base de $E_2$.
        Ainsi, il existe des scalaires $\alpha, \beta, \gamma \in \mathbb{R}$ tels que :
        $v = \alpha u_1 + \beta u_2$
        $v = \gamma u_3$

        En égalant les deux expressions de $v$ :
        $\alpha(1,1,0) + \beta(1,-1,0) = \gamma(0,0,1)$
        $(\alpha+\beta, \alpha-\beta, 0) = (0,0,\gamma)$

        En égalant les composantes correspondantes, nous obtenons le système d'équations linéaires suivant :
        1.  $\alpha+\beta = 0$
        2.  $\alpha-\beta = 0$
        3.  $0 = \gamma$

        De l'équation (3), nous avons directement $\gamma = 0$.
        En additionnant l'équation (1) et l'équation (2) :
        $(\alpha+\beta) + (\alpha-\beta) = 0+0$
        $2\alpha = 0 \implies \alpha = 0$.
        En substituant $\alpha=0$ dans l'équation (1) :
        $0+\beta = 0 \implies \beta = 0$.

        Ainsi, $\alpha = 0, \beta = 0, \gamma = 0$. Cela implique que $v = 0 \cdot u_1 + 0 \cdot u_2 = (0,0,0)$.
        Donc, $E_1 \cap E_2 = \{0\}$.

    *   **Somme des dimensions :**
        La dimension de la somme des sous-espaces est donnée par la formule de Grassmann :
        $\dim(E_1 + E_2) = \dim(E_1) + \dim(E_2) - \dim(E_1 \cap E_2)$.
        $\dim(E_1 + E_2) = 2 + 1 - 0 = 3$.
        Puisque $\dim(E_1 + E_2) = 3$ et $\dim(E) = 3$, et que $E_1 + E_2$ est un sous-espace de $E$, nous pouvons conclure que $E_1 + E_2 = E$.
        Comme $E_1 \cap E_2 = \{0\}$ et $E_1 + E_2 = E$, nous avons bien $E = E_1 \oplus E_2$.

2.  **Montrer que $E_1$ et $E_2$ sont des sous-espaces stables par $f$**

    Un sous-espace $F$ est stable par une application linéaire $f$ si pour tout vecteur $v \in F$, l'image $f(v)$ appartient également à $F$. Pour un sous-espace engendré par une base, il suffit de vérifier que les images des vecteurs de cette base restent dans le sous-espace.

    *   **Stabilité de $E_1$ :**
        $E_1 = \text{Vect}(u_1, u_2)$. Nous devons vérifier si $f(u_1) \in E_1$ et $f(u_2) \in E_1$.
        $u_1 = (1,1,0)$.
        $f(u_1) = f(1,1,0) = (2(1)+1, 1+2(1), 0) = (3,3,0)$.
        Nous pouvons exprimer $(3,3,0)$ comme une combinaison linéaire de $u_1$ et $u_2$:
        $(3,3,0) = 3(1,1,0) = 3u_1$.
        Puisque $f(u_1) = 3u_1$, et $u_1 \in E_1$, alors $f(u_1) \in E_1$.

        $u_2 = (1,-1,0)$.
        $f(u_2) = f(1,-1,0) = (2(1)+(-1), 1+2(-1), 0) = (2-1, 1-2, 0) = (1,-1,0)$.
        Nous pouvons exprimer $(1,-1,0)$ comme une combinaison linéaire de $u_1$ et $u_2$:
        $(1,-1,0) = 1(1,-1,0) = u_2$.
        Puisque $f(u_2) = u_2$, et $u_2 \in E_1$, alors $f(u_2) \in E_1$.

        Étant donné que $f(u_1)$ et $f(u_2)$ appartiennent à $E_1$, et que $E_1$ est engendré par $u_1$ et $u_2$, tout vecteur $v \in E_1$ est de la forme $v = \alpha u_1 + \beta u_2$ pour des scalaires $\alpha, \beta \in \mathbb{R}$.
        Par linéarité de $f$, nous avons $f(v) = f(\alpha u_1 + \beta u_2) = \alpha f(u_1) + \beta f(u_2)$.
        Comme $\alpha f(u_1) \in E_1$ et $\beta f(u_2) \in E_1$, leur somme $\alpha f(u_1) + \beta f(u_2)$ appartient également à $E_1$.
        Donc, $E_1$ est un sous-espace stable par $f$.

    *   **Stabilité de $E_2$ :**
        $E_2 = \text{Vect}(u_3)$. Nous devons vérifier si $f(u_3) \in E_2$.
        $u_3 = (0,0,1)$.
        $f(u_3) = f(0,0,1) = (2(0)+0, 0+2(0), 1) = (0,0,1)$.
        Nous pouvons exprimer $(0,0,1)$ comme un multiple de $u_3$:
        $(0,0,1) = 1(0,0,1) = u_3$.
        Puisque $f(u_3) = u_3$, et $u_3 \in E_2$, alors $f(u_3) \in E_2$.

        Tout vecteur $v \in E_2$ est de la forme $v = \gamma u_3$ pour un scalaire $\gamma \in \mathbb{R}$.
        Par linéarité de $f$, nous avons $f(v) = f(\gamma u_3) = \gamma f(u_3) = \gamma u_3$.
        Puisque $\gamma u_3 \in E_2$, $E_2$ est un sous-espace stable par $f$.

### Question 2.3 : Matrice par blocs et restrictions

Expliquer comment la matrice $A'$ obtenue dans la Question 1.4 peut être interprétée comme une matrice par blocs, et relier ces blocs aux restrictions de $f$ sur les sous-espaces $E_1$ et $E_2$.

#### Solution 2.3

La matrice $A'$ de l'application linéaire $f$ dans la base $\mathcal{B}' = (u_1, u_2, u_3)$ est :
$$A' = \begin{pmatrix}
3 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}$$

Nous avons montré que l'espace vectoriel $E$ peut être décomposé en une somme directe de deux sous-espaces $E_1$ et $E_2$, c'est-à-dire $E = E_1 \oplus E_2$, où $E_1 = \text{Vect}(u_1, u_2)$ et $E_2 = \text{Vect}(u_3)$.
Nous avons également démontré que ces deux sous-espaces $E_1$ et $E_2$ sont stables (ou invariants) par l'application linéaire $f$. Cela signifie que $f(E_1) \subseteq E_1$ et $f(E_2) \subseteq E_2$.

La base $\mathcal{B}'$ est construite en concaténant une base de $E_1$ (qui est $(u_1, u_2)$) et une base de $E_2$ (qui est $(u_3)$). Lorsque l'espace vectoriel $E$ est une somme directe de sous-espaces stables $E_1, \dots, E_k$, et que la base de $E$ est formée en concaténant des bases de ces sous-espaces, alors la matrice de l'application linéaire dans cette base est une matrice diagonale par blocs.

Dans notre cas, la matrice $A'$ peut être décomposée en blocs de la manière suivante :
$$A' = \begin{pmatrix}
A'_{11} & A'_{12} \\
A'_{21} & A'_{22}
\end{pmatrix} = \begin{pmatrix}
\begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} & \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\
\begin{pmatrix} 0 & 0 \end{pmatrix} & \begin{pmatrix} 1 \end{pmatrix}
\end{pmatrix}$$

*   **Bloc $A'_{11}$ :** Ce bloc est la matrice $2 \times 2$ :
    $$A'_{11} = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$$
    Les colonnes de la matrice $A'$ représentent les images des vecteurs de base de $\mathcal{B}'$ exprimées dans la base $\mathcal{B}'$.
    La première colonne de $A'$ est $(3,0,0)^T$. Cela signifie que $f(u_1) = 3u_1 + 0u_2 + 0u_3 = 3u_1$.
    La deuxième colonne de $A'$ est $(0,1,0)^T$. Cela signifie que $f(u_2) = 0u_1 + 1u_2 + 0u_3 = u_2$.
    Puisque $f(u_1)$ et $f(u_2)$ sont des combinaisons linéaires des vecteurs $u_1$ et $u_2$ seulement, le bloc $A'_{11}$ représente la matrice de la restriction de $f$ à $E_1$, notée $f|_{E_1} : E_1 \to E_1$, dans la base $(u_1, u_2)$ de $E_1$.
    En effet, la matrice de $f|_{E_1}$ dans la base $(u_1, u_2)$ est $\begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$.

*   **Bloc $A'_{22}$ :** Ce bloc est la matrice $1 \times 1$ :
    $$A'_{22} = \begin{pmatrix} 1 \end{pmatrix}$$
    La troisième colonne de $A'$ est $(0,0,1)^T$. Cela signifie que $f(u_3) = 0u_1 + 0u_2 + 1u_3 = u_3$.
    Puisque $f(u_3)$ est un multiple du vecteur $u_3$ seulement, le bloc $A'_{22}$ représente la matrice de la restriction de $f$ à $E_2$, notée $f|_{E_2} : E_2 \to E_2$, dans la base $(u_3)$ de $E_2$.
    En effet, la matrice de $f|_{E_2}$ dans la base $(u_3)$ est $\begin{pmatrix} 1 \end{pmatrix}$.

*   **Blocs $A'_{12}$ et $A'_{21}$ :** Ces blocs sont des matrices nulles :
    $$A'_{12} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \quad \text{et} \quad A'_{21} = \begin{pmatrix} 0 & 0 \end{pmatrix}$$
    Le fait que le bloc $A'_{12}$ soit la matrice nulle signifie que les images des vecteurs de base de $E_2$ (c'est-à-dire $f(u_3)$) n'ont pas de composantes dans $E_1$. Autrement dit, $f(E_2) \subseteq E_2$.
    Le fait que le bloc $A'_{21}$ soit la matrice nulle signifie que les images des vecteurs de base de $E_1$ (c'est-à-dire $f(u_1)$ et $f(u_2)$) n'ont pas de composantes dans $E_2$. Autrement dit, $f(E_1) \subseteq E_1$.
    Ces blocs nuls confirment l'invariance des sous-espaces $E_1$ et $E_2$ sous l'application $f$, et la décomposition de l'action de $f$ en des actions indépendantes sur chacun de ces sous-espaces.

En résumé, la matrice $A'$ est une matrice diagonale par blocs, où chaque bloc diagonal correspond à la matrice de la restriction de l'application linéaire $f$ au sous-espace invariant correspondant, dans la base de ce sous-espace. Cette forme simplifiée de la matrice $A'$ est très utile pour analyser les propriétés de l'application linéaire $f$, notamment ses valeurs propres et vecteurs propres, qui sont directement lisibles ici (3 est une valeur propre associée au vecteur propre $u_1$, et 1 est une valeur propre associée aux vecteurs propres $u_2$ et $u_3$).

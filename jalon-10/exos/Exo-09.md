```yaml
title: "Exercice 09 - Changements de Base et Matrices par Blocs"
subtitle: "Analyse d'une Transformation Linéaire Structurée"
author: "Votre Nom"
date: "2023-10-27"
keywords:
  - Algèbre Linéaire
  - Changement de base
  - Matrice de passage
  - Matrices par blocs
  - Transformation linéaire
  - Inversion de matrice
  - Déterminant
  - Espace vectoriel
  - Base
level: "L1-Master"
tags:
  - Mathématiques pour l'IA
  - Jalon 10
  - Exercice
  - Algèbre Linéaire Avancée
```

# Exercice 09 - Changements de Base et Matrices par Blocs

Cet exercice approfondit les concepts de changements de base, de matrices de passage et d'opérations sur les matrices par blocs. Il est conçu pour une difficulté progressive, culminant avec des calculs matriciels par blocs détaillés et une discussion conceptuelle avancée.

Soit $\mathbb{R}^4$ un espace vectoriel sur le corps $\mathbb{K} = \mathbb{R}$. Nous désignons par $I_n$ la matrice identité de taille $n \times n$.

## Partie 1 : Changement de Base dans $\mathbb{R}^4$

Nous considérons deux bases de $\mathbb{R}^4$.

1.  La base canonique $\mathcal{B}_0 = (e_1, e_2, e_3, e_4)$, où les vecteurs sont définis comme suit :
    $e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$, $e_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$, $e_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}$, $e_4 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$.

2.  Une nouvelle base $\mathcal{B}_1 = (v_1, v_2, v_3, v_4)$, où les vecteurs sont définis par leurs coordonnées dans la base canonique $\mathcal{B}_0$ :
    $v_1 = e_1 + e_2 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}$
    $v_2 = e_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$
    $v_3 = e_3 + e_4 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}$
    $v_4 = e_4 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$

---

**Question 1.1 : Détermination de la matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$**

Déterminer la matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ de la base $\mathcal{B}_0$ à la base $\mathcal{B}_1$. Spécifier sa structure par blocs en la décomposant en quatre blocs $2 \times 2$.

**Réponse 1.1 :**

La matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ est la matrice dont les colonnes sont les coordonnées des vecteurs de la base $\mathcal{B}_1$ exprimés dans la base $\mathcal{B}_0$.
Les vecteurs de $\mathcal{B}_1$ sont :
$v_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}_{\mathcal{B}_0}$
$v_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}_{\mathcal{B}_0}$
$v_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}_{\mathcal{B}_0}$
$v_4 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}_{\mathcal{B}_0}$

Ainsi, la matrice $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ est :
$$ P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 1 & 1
\end{pmatrix} $$

Nous pouvons décomposer cette matrice en quatre blocs $2 \times 2$. Soit $P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix}$, où :
$P_{11} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$
$P_{12} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$
$P_{21} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$
$P_{22} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$

La matrice de passage $P_{\mathcal{B}_0 \to \mathcal{B}_1}$ est donc une matrice diagonale par blocs :
$$ P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} P_{11} & 0 \\ 0 & P_{22} \end{pmatrix} $$

---

**Question 1.2 : Détermination de la matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$**

Déterminer la matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ de la base $\mathcal{B}_1$ à la base $\mathcal{B}_0$. Détailler le calcul de l'inverse en utilisant la structure par blocs de $P_{\mathcal{B}_0 \to \mathcal{B}_1}$.

**Réponse 1.2 :**

La matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ est l'inverse de la matrice $P_{\mathcal{B}_0 \to \mathcal{B}_1}$.
Nous avons $P_{\mathcal{B}_0 \to \mathcal{B}_1} = P = \begin{pmatrix} P_{11} & 0 \\ 0 & P_{22} \end{pmatrix}$.
L'inverse d'une matrice diagonale par blocs est la matrice diagonale par blocs formée des inverses des blocs diagonaux :
$$ P^{-1} = \begin{pmatrix} P_{11}^{-1} & 0 \\ 0 & P_{22}^{-1} \end{pmatrix} $$

Calculons d'abord l'inverse de $P_{11}$ :
$P_{11} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$
Le déterminant de $P_{11}$ est $\det(P_{11}) = (1)(1) - (0)(1) = 1$.
L'inverse de $P_{11}$ est :
$$ P_{11}^{-1} = \frac{1}{\det(P_{11})} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \frac{1}{1} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} $$

Calculons ensuite l'inverse de $P_{22}$ :
$P_{22} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$
Le déterminant de $P_{22}$ est $\det(P_{22}) = (1)(1) - (0)(1) = 1$.
L'inverse de $P_{22}$ est :
$$ P_{22}^{-1} = \frac{1}{\det(P_{22})} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \frac{1}{1} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} $$

Par conséquent, la matrice de passage $P_{\mathcal{B}_1 \to \mathcal{B}_0}$ est :
$$ P_{\mathcal{B}_1 \to \mathcal{B}_0} = P^{-1} = \begin{pmatrix}
P_{11}^{-1} & 0 \\
0 & P_{22}^{-1}
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & -1 & 1
\end{pmatrix} $$

---

**Question 1.3 : Vérification de la relation d'inversion**

Vérifier que $P_{\mathcal{B}_0 \to \mathcal{B}_1} \cdot P_{\mathcal{B}_1 \to \mathcal{B}_0} = I_4$, où $I_4$ est la matrice identité de taille $4 \times 4$. Détailler la multiplication matricielle par blocs.

**Réponse 1.3 :**

Nous avons $P_{\mathcal{B}_0 \to \mathcal{B}_1} = \begin{pmatrix} P_{11} & 0 \\ 0 & P_{22} \end{pmatrix}$ et $P_{\mathcal{B}_1 \to \mathcal{B}_0} = \begin{pmatrix} P_{11}^{-1} & 0 \\ 0 & P_{22}^{-1} \end{pmatrix}$.
Effectuons la multiplication par blocs :
$$ P_{\mathcal{B}_0 \to \mathcal{B}_1} \cdot P_{\mathcal{B}_1 \to \mathcal{B}_0} = \begin{pmatrix} P_{11} & 0 \\ 0 & P_{22} \end{pmatrix} \begin{pmatrix} P_{11}^{-1} & 0 \\ 0 & P_{22}^{-1} \end{pmatrix} $$
$$ = \begin{pmatrix}
P_{11} P_{11}^{-1} + 0 \cdot 0 & P_{11} \cdot 0 + 0 \cdot P_{22}^{-1} \\
0 \cdot P_{11}^{-1} + P_{22} \cdot 0 & 0 \cdot 0 + P_{22} P_{22}^{-1}
\end{pmatrix} $$
$$ = \begin{pmatrix}
I_2 & 0 \\
0 & I_2
\end{pmatrix} $$
$$ = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} = I_4 $$
La vérification est concluante.

## Partie 2 : Matrice d'une Transformation Linéaire Structurée

Soit $f: \mathbb{R}^4 \to \mathbb{R}^4$ une application linéaire définie par son action sur les vecteurs de la base canonique $\mathcal{B}_0$ :
$f(e_1) = e_1 + e_3$
$f(e_2) = e_1 + e_2 + e_4$
$f(e_3) = e_3$
$f(e_4) = e_3 + e_4$

---

**Question 2.1 : Matrice de $f$ dans la base canonique**

Écrire la matrice $M_0 = \text{Mat}_{\mathcal{B}_0}(f)$ de l'application linéaire $f$ dans la base canonique $\mathcal{B}_0$. Spécifier sa structure par blocs $M_0 = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ avec $A, B, C, D \in \mathcal{M}_{2}(\mathbb{R})$.

**Réponse 2.1 :**

La matrice $M_0$ a pour colonnes les coordonnées des images des vecteurs de la base $\mathcal{B}_0$ par $f$, exprimées dans la base $\mathcal{B}_0$.
$f(e_1) = \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}_{\mathcal{B}_0}$
$f(e_2) = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 1 \end{pmatrix}_{\mathcal{B}_0}$
$f(e_3) = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}_{\mathcal{B}_0}$
$f(e_4) = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}_{\mathcal{B}_0}$

Ainsi, la matrice $M_0$ est :
$$ M_0 = \begin{pmatrix}
1 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 \\
0 & 1 & 0 & 1
\end{pmatrix} $$

Nous pouvons décomposer cette matrice en quatre blocs $2 \times 2$. Soit $M_0 = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$, où :
$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
$B = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$
$C = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
$D = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$

La matrice $M_0$ a donc la structure par blocs suivante :
$$ M_0 = \begin{pmatrix} A & 0 \\ C & D \end{pmatrix} $$

---

**Question 2.2 : Calcul du déterminant de $M_0$**

Calculer le déterminant de $M_0$ en utilisant la formule du déterminant pour les matrices par blocs, si applicable. Détailler chaque étape.

**Réponse 2.2 :**

La matrice $M_0$ est une matrice triangulaire inférieure par blocs : $M_0 = \begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$.
Pour une telle matrice, le déterminant est le produit des déterminants des blocs diagonaux : $\det(M_0) = \det(A) \det(D)$.

Calculons $\det(A)$ :
$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
$\det(A) = (1)(1) - (1)(0) = 1 - 0 = 1$.

Calculons $\det(D)$ :
$D = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
$\det(D) = (1)(1) - (1)(0) = 1 - 0 = 1$.

Par conséquent, le déterminant de $M_0$ est :
$\det(M_0) = \det(A) \det(D) = (1)(1) = 1$.

## Partie 3 : Matrice de la Transformation dans la Nouvelle Base

---

**Question 3.1 : Calcul de $M_1$**

Calculer la matrice $M_1 = \text{Mat}_{\mathcal{B}_1}(f)$ de l'application linéaire $f$ dans la base $\mathcal{B}_1$ en utilisant la formule de changement de base $M_1 = P_{\mathcal{B}_1 \to \mathcal{B}_0} M_0 P_{\mathcal{B}_0 \to \mathcal{B}_1}$. Détailler toutes les multiplications de matrices par blocs.

**Réponse 3.1 :**

Nous avons les matrices suivantes :
$P_{\mathcal{B}_1 \to \mathcal{B}_0} = P^{-1} = \begin{pmatrix} P_{11}^{-1} & 0 \\ 0 & P_{22}^{-1} \end{pmatrix}$
$M_0 = \begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$
$P_{\mathcal{B}_0 \to \mathcal{B}_1} = P = \begin{pmatrix} P_{11} & 0 \\ 0 & P_{22} \end{pmatrix}$

La formule de changement de base est $M_1 = P^{-1} M_0 P$.
Effectuons d'abord le produit $P^{-1} M_0$ par blocs :
$$ P^{-1} M_0 = \begin{pmatrix} P_{11}^{-1} & 0 \\ 0 & P_{22}^{-1} \end{pmatrix} \begin{pmatrix} A & 0 \\ C & D \end{pmatrix} $$
$$ = \begin{pmatrix}
P_{11}^{-1} A + 0 \cdot C & P_{11}^{-1} \cdot 0 + 0 \cdot D \\
0 \cdot A + P_{22}^{-1} C & 0 \cdot 0 + P_{22}^{-1} D
\end{pmatrix} $$
$$ = \begin{pmatrix}
P_{11}^{-1} A & 0 \\
P_{22}^{-1} C & P_{22}^{-1} D
\end{pmatrix} $$

Maintenant, effectuons le produit $(P^{-1} M_0) P$ par blocs :
$$ M_1 = \begin{pmatrix} P_{11}^{-1} A & 0 \\ P_{22}^{-1} C & P_{22}^{-1} D \end{pmatrix} \begin{pmatrix} P_{11} & 0 \\ 0 & P_{22} \end{pmatrix} $$
$$ = \begin{pmatrix}
P_{11}^{-1} A P_{11} + 0 \cdot 0 & P_{11}^{-1} A \cdot 0 + 0 \cdot P_{22} \\
P_{22}^{-1} C P_{11} + P_{22}^{-1} D \cdot 0 & P_{22}^{-1} C \cdot 0 + P_{22}^{-1} D P_{22}
\end{pmatrix} $$
$$ = \begin{pmatrix}
P_{11}^{-1} A P_{11} & 0 \\
P_{22}^{-1} C P_{11} & P_{22}^{-1} D P_{22}
\end{pmatrix} $$

Calculons chaque bloc $2 \times 2$ :

**Bloc supérieur gauche : $P_{11}^{-1} A P_{11}$**
Nous avons $P_{11}^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$, $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $P_{11} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
1.  Calculons $P_{11}^{-1} A$ :
    $$ P_{11}^{-1} A = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(0)(0) & (1)(1)+(0)(1) \\ (-1)(1)+(1)(0) & (-1)(1)+(1)(1) \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix} $$
2.  Calculons $(P_{11}^{-1} A) P_{11}$ :
    $$ \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(1)(1) & (1)(0)+(1)(1) \\ (-1)(1)+(0)(1) & (-1)(0)+(0)(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix} $$
Donc, le bloc supérieur gauche de $M_1$ est $\begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}$.

**Bloc inférieur gauche : $P_{22}^{-1} C P_{11}$**
Nous avons $P_{22}^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$, $C = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, $P_{11} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
1.  Calculons $P_{22}^{-1} C$ :
    $$ P_{22}^{-1} C = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(0)(0) & (1)(0)+(0)(1) \\ (-1)(1)+(1)(0) & (-1)(0)+(1)(1) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} $$
2.  Calculons $(P_{22}^{-1} C) P_{11}$ :
    $$ \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(0)(1) & (1)(0)+(0)(1) \\ (-1)(1)+(1)(1) & (-1)(0)+(1)(1) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $$
Donc, le bloc inférieur gauche de $M_1$ est $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.

**Bloc inférieur droit : $P_{22}^{-1} D P_{22}$**
Nous avons $P_{22}^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $P_{22} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
1.  Calculons $P_{22}^{-1} D$ :
    $$ P_{22}^{-1} D = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(0)(0) & (1)(1)+(0)(1) \\ (-1)(1)+(1)(0) & (-1)(1)+(1)(1) \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix} $$
2.  Calculons $(P_{22}^{-1} D) P_{22}$ :
    $$ \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(1)(1) & (1)(0)+(1)(1) \\ (-1)(1)+(0)(1) & (-1)(0)+(0)(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix} $$
Donc, le bloc inférieur droit de $M_1$ est $\begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}$.

En assemblant les blocs, la matrice $M_1$ est :
$$ M_1 = \begin{pmatrix}
\begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix} & \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \\
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} & \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}
\end{pmatrix} = \begin{pmatrix}
2 & 1 & 0 & 0 \\
-1 & 0 & 0 & 0 \\
1 & 0 & 2 & 1 \\
0 & 1 & -1 & 0
\end{pmatrix} $$

## Partie 4 : Inversion d'une Matrice par Blocs

Soit $g: \mathbb{R}^4 \to \mathbb{R}^4$ une autre application linéaire dont la matrice dans la base canonique $\mathcal{B}_0$ est donnée par :
$$ M'_0 = \begin{pmatrix} A' & B' \\ 0 & D' \end{pmatrix} $$
où les blocs $A', B', D'$ sont des éléments de $\mathcal{M}_{2}(\mathbb{R})$ définis comme suit :
$A' = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
$B' = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
$D' = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$

---

**Question 4.1 : Vérification et calcul des inverses des blocs diagonaux**

Vérifier que les blocs $A'$ et $D'$ sont inversibles et calculer leurs inverses $A'^{-1}$ et $D'^{-1}$.

**Réponse 4.1 :**

Pour qu'une matrice soit inversible, son déterminant doit être non nul.

**Pour le bloc $A'$ :**
$A' = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
$\det(A') = (1)(1) - (1)(0) = 1 - 0 = 1$.
Puisque $\det(A') = 1 \neq 0$, la matrice $A'$ est inversible.
L'inverse de $A'$ est :
$$ A'^{-1} = \frac{1}{\det(A')} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \frac{1}{1} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} $$

**Pour le bloc $D'$ :**
$D' = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$
$\det(D') = (1)(1) - (0)(1) = 1 - 0 = 1$.
Puisque $\det(D') = 1 \neq 0$, la matrice $D'$ est inversible.
L'inverse de $D'$ est :
$$ D'^{-1} = \frac{1}{\det(D')} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \frac{1}{1} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} $$

---

**Question 4.2 : Calcul de l'inverse de $M'_0$**

Calculer l'inverse de $M'_0$ en utilisant la formule d'inversion pour les matrices triangulaires supérieures par blocs :
$(M'_0)^{-1} = \begin{pmatrix} A'^{-1} & -A'^{-1} B' D'^{-1} \\ 0 & D'^{-1} \end{pmatrix}$.
Détailler toutes les étapes de calcul, y compris les multiplications de matrices $2 \times 2$.

**Réponse 4.2 :**

Nous avons déjà calculé $A'^{-1}$ et $D'^{-1}$. Il nous reste à calculer le bloc $-A'^{-1} B' D'^{-1}$.

1.  **Calcul de $A'^{-1} B'$ :**
    $$ A'^{-1} B' = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(-1)(0) & (1)(0)+(-1)(1) \\ (0)(1)+(1)(0) & (0)(0)+(1)(1) \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} $$

2.  **Calcul de $(A'^{-1} B') D'^{-1}$ :**
    $$ (A'^{-1} B') D'^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} (1)(1)+(-1)(-1) & (1)(0)+(-1)(1) \\ (0)(1)+(1)(-1) & (0)(0)+(1)(1) \end{pmatrix} $$
    $$ = \begin{pmatrix} 1+1 & 0-1 \\ 0-1 & 0+1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} $$

3.  **Calcul de $-A'^{-1} B' D'^{-1}$ :**
    $$ -A'^{-1} B' D'^{-1} = - \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ 1 & -1 \end{pmatrix} $$

En assemblant tous les blocs, l'inverse de $M'_0$ est :
$$ (M'_0)^{-1} = \begin{pmatrix}
A'^{-1} & -A'^{-1} B' D'^{-1} \\
0 & D'^{-1}
\end{pmatrix} = \begin{pmatrix}
\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} & \begin{pmatrix} -2 & 1 \\ 1 & -1 \end{pmatrix} \\
\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} & \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}
\end{pmatrix} $$
$$ (M'_0)^{-1} = \begin{pmatrix}
1 & -1 & -2 & 1 \\
0 & 1 & 1 & -1 \\
0 & 0 & 1 & 0 \\
0 & 0 & -1 & 1
\end{pmatrix} $$

## Partie 5 : Discussion Conceptuelle sur la Structure par Blocs

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$. Soit $f: E \to E$ une application linéaire.
Supposons que $E$ puisse être décomposé en une somme directe de deux sous-espaces vectoriels $E_1$ et $E_2$, c'est-à-dire $E = E_1 \oplus E_2$.
Soit $\mathcal{B} = (e_1, \dots, e_k, e_{k+1}, \dots, e_n)$ une base de $E$ adaptée à cette décomposition, c'est-à-dire $(e_1, \dots, e_k)$ est une base de $E_1$ et $(e_{k+1}, \dots, e_n)$ est une base de $E_2$.

---

**Question 5.1 : Structure de la matrice si $f$ préserve $E_1$ et $E_2$**

Si $f$ préserve les sous-espaces $E_1$ et $E_2$ (c'est-à-dire $f(E_1) \subseteq E_1$ et $f(E_2) \subseteq E_2$), quelle est la structure de la matrice $\text{Mat}_{\mathcal{B}}(f)$ ? Justifier votre réponse.

**Réponse 5.1 :**

Si $f(E_1) \subseteq E_1$, cela signifie que pour tout vecteur $x \in E_1$, $f(x)$ est également dans $E_1$. Puisque $(e_1, \dots, e_k)$ est une base de $E_1$, l'image de chaque $e_i$ pour $i \in \{1, \dots, k\}$ doit être une combinaison linéaire de $e_1, \dots, e_k$.
Par conséquent, les $k$ premières colonnes de la matrice $\text{Mat}_{\mathcal{B}}(f)$ n'auront des composantes non nulles que dans les $k$ premières lignes. Les composantes des lignes $k+1$ à $n$ seront nulles pour ces colonnes.

De même, si $f(E_2) \subseteq E_2$, cela signifie que pour tout vecteur $y \in E_2$, $f(y)$ est également dans $E_2$. Puisque $(e_{k+1}, \dots, e_n)$ est une base de $E_2$, l'image de chaque $e_j$ pour $j \in \{k+1, \dots, n\}$ doit être une combinaison linéaire de $e_{k+1}, \dots, e_n$.
Par conséquent, les $n-k$ dernières colonnes de la matrice $\text{Mat}_{\mathcal{B}}(f)$ n'auront des composantes non nulles que dans les lignes $k+1$ à $n$. Les composantes des $k$ premières lignes seront nulles pour ces colonnes.

En combinant ces deux observations, la matrice $\text{Mat}_{\mathcal{B}}(f)$ aura une structure diagonale par blocs :
$$ \text{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} $$
où $A \in \mathcal{M}_k(\mathbb{K})$ est la matrice de la restriction de $f$ à $E_1$ (vue comme une application de $E_1$ dans $E_1$) dans la base $(e_1, \dots, e_k)$, et $D \in \mathcal{M}_{n-k}(\mathbb{K})$ est la matrice de la restriction de $f$ à $E_2$ (vue comme une application de $E_2$ dans $E_2$) dans la base $(e_{k+1}, \dots, e_n)$. Les blocs $0$ sont des matrices nulles de tailles appropriées ($k \times (n-k)$ et $(n-k) \times k$).

---

**Question 5.2 : Structure de la matrice si $f$ ne préserve que $E_1$**

Si $f$ ne préserve que $E_1$ (c'est-à-dire $f(E_1) \subseteq E_1$ mais $f(E_2)$ n'est pas nécessairement inclus dans $E_2$), quelle est la structure de la matrice $\text{Mat}_{\mathcal{B}}(f)$ ? Justifier votre réponse.

**Réponse 5.2 :**

Si $f(E_1) \subseteq E_1$, alors, comme expliqué précédemment, les $k$ premières colonnes de $\text{Mat}_{\mathcal{B}}(f)$ n'auront des composantes non nulles que dans les $k$ premières lignes. Cela signifie que le bloc inférieur gauche de la matrice sera nul.
$$ \text{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} $$
où $A \in \mathcal{M}_k(\mathbb{K})$ est la matrice de la restriction de $f$ à $E_1$ (vue comme une application de $E_1$ dans $E_1$) dans la base $(e_1, \dots, e_k)$.
Le bloc $0$ est une matrice nulle de taille $(n-k) \times k$.
Le bloc $D \in \mathcal{M}_{n-k}(\mathbb{K})$ représente la partie de $f$ qui mappe $E_2$ vers $E_2$.
Le bloc $B \in \mathcal{M}_{k, n-k}(\mathbb{K})$ représente la partie de $f$ qui mappe $E_2$ vers $E_1$.
Puisque $f(E_2)$ n'est pas nécessairement inclus dans $E_2$, les images des vecteurs de $E_2$ peuvent avoir des composantes non nulles dans $E_1$. Cela se traduit par le bloc $B$ qui n'est pas nécessairement nul.
La matrice $\text{Mat}_{\mathcal{B}}(f)$ aura donc une structure triangulaire supérieure par blocs.

---

**Question 5.3 : Perte de structure par blocs après changement de base**

Supposons maintenant que $f$ préserve $E_1$ et $E_2$, et que sa matrice dans $\mathcal{B}$ est donc diagonale par blocs. Si l'on effectue un changement de base vers une nouvelle base $\mathcal{B}'$ qui n'est pas adaptée à la décomposition $E = E_1 \oplus E_2$ (c'est-à-dire $\text{Vect}(e'_1, \dots, e'_k)$ n'est ni $E_1$ ni $E_2$), que peut-on dire de la structure par blocs de $\text{Mat}_{\mathcal{B}'}(f)$ ? Discuter des implications de cette perte de structure pour l'analyse de $f$ et pour les calculs numériques.

**Réponse 5.3 :**

Soit $M = \text{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix}$ la matrice de $f$ dans la base $\mathcal{B}$ adaptée à la décomposition $E = E_1 \oplus E_2$.
Soit $P = P_{\mathcal{B} \to \mathcal{B}'}$ la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$.
La matrice de $f$ dans la nouvelle base $\mathcal{B}'$ est $M' = \text{Mat}_{\mathcal{B}'}(f) = P^{-1} M P$.

Si la base $\mathcal{B}'$ n'est pas adaptée à la décomposition $E = E_1 \oplus E_2$, alors la matrice de passage $P$ n'aura généralement pas une structure diagonale par blocs, ni même triangulaire par blocs. Elle sera une matrice pleine.
Par exemple, si $P = \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix}$ où $P_{12}$ et $P_{21}$ ne sont pas nuls.
Alors $P^{-1}$ sera également une matrice pleine, disons $P^{-1} = \begin{pmatrix} Q_{11} & Q_{12} \\ Q_{21} & Q_{22} \end{pmatrix}$.

Calculons $M'$ par blocs :
$$ M' = \begin{pmatrix} Q_{11} & Q_{12} \\ Q_{21} & Q_{22} \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix} $$
$$ M' = \begin{pmatrix} Q_{11} A & Q_{12} D \\ Q_{21} A & Q_{22} D \end{pmatrix} \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix} $$
$$ M' = \begin{pmatrix}
Q_{11} A P_{11} + Q_{12} D P_{21} & Q_{11} A P_{12} + Q_{12} D P_{22} \\
Q_{21} A P_{11} + Q_{22} D P_{21} & Q_{21} A P_{12} + Q_{22} D P_{22}
\end{pmatrix} $$
En général, tous les blocs de $M'$ seront non nuls. La structure diagonale par blocs de $M$ est donc perdue dans $M'$.

**Implications de cette perte de structure :**

1.  **Analyse de $f$ :** La structure diagonale par blocs de $M$ dans la base $\mathcal{B}$ révèle que l'application linéaire $f$ agit indépendamment sur les sous-espaces $E_1$ et $E_2$. Cela simplifie grandement l'analyse des propriétés de $f$ (valeurs propres, vecteurs propres, noyau, image) car elles peuvent être étudiées séparément pour les restrictions de $f$ à $E_1$ et $E_2$. La perte de cette structure dans une base non adaptée rend cette interprétation directe impossible. La transformation $f$ apparaît comme une opération "mélangée" sur les composantes, masquant sa nature sous-jacente.

2.  **Calculs numériques :**
    *   **Coût de calcul :** Les opérations matricielles (multiplication, inversion, calcul de déterminant) sont significativement plus coûteuses pour des matrices pleines que pour des matrices par blocs. Par exemple, le déterminant d'une matrice diagonale par blocs est le produit des déterminants des blocs, ce qui est beaucoup plus rapide à calculer que le déterminant d'une matrice pleine de grande taille. De même, l'inversion d'une matrice diagonale par blocs se fait en inversant chaque bloc séparément.
    *   **Stabilité numérique :** Les algorithmes numériques peuvent être plus stables et précis lorsqu'ils exploitent la structure des matrices. La perte de structure par blocs peut conduire à des problèmes numériques accrus, notamment pour des matrices de grande taille.
    *   **Stockage :** Une matrice par blocs avec des blocs nuls peut être stockée de manière plus efficace en ne stockant que les blocs non nuls. Une matrice pleine nécessite le stockage de tous ses éléments.

En résumé, choisir une base adaptée à la structure d'une transformation linéaire (comme une décomposition en somme directe de sous-espaces invariants) permet de représenter la transformation par une matrice par blocs, ce qui simplifie son analyse théorique et optimise les calculs numériques. Un changement vers une base non adaptée détruit généralement cette structure bénéfique, rendant l'analyse plus complexe et les calculs plus coûteux.

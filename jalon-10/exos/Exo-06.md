---
title: "Exercice 06 - Changements de base et matrices de passage"
subtitle: "Jalon 10 - Changements de base, matrices de passage et matrices par blocs"
course: "Mathématiques pour l'Intelligence Artificielle"
level: "L1 à Master"
date: "2023-10-27"
tags:
  - Algèbre Linéaire
  - Espaces Vectoriels
  - Bases
  - Changement de Base
  - Matrices de Passage
  - Matrices de Transformation
  - Matrices Inversibles
---

# Exercice 06 : Changements de base et matrices de passage

Cet exercice explore les concepts fondamentaux de changement de base et de matrices de passage dans un espace vectoriel de dimension finie. Il vise à renforcer la compréhension des relations entre les coordonnées d'un vecteur, la représentation d'une application linéaire et les différentes bases.

Soit $\mathbb{K}$ le corps des nombres réels, $\mathbb{K} = \mathbb{R}$.
Soit $E$ l'espace vectoriel $\mathbb{R}^3$ sur le corps $\mathbb{R}$.

## Partie 1 : Définition des bases et expression de vecteurs

1.  **Définition de la base canonique**
    Soit $\mathcal{B}_c = (e_1, e_2, e_3)$ la base canonique de l'espace vectoriel $E = \mathbb{R}^3$, où les vecteurs $e_1, e_2, e_3$ sont définis comme suit :
    $$e_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad e_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad e_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$
    Ces vecteurs sont des éléments de $\mathbb{R}^3$.

2.  **Définition d'une nouvelle base**
    Soit $\mathcal{B}' = (u_1, u_2, u_3)$ une famille de vecteurs de $E = \mathbb{R}^3$, définie par :
    $$u_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad u_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \quad u_3 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$
    Démontrez que $\mathcal{B}'$ est une base de $E$.

    *Démonstration :*
    Pour que la famille $\mathcal{B}'$ soit une base de $\mathbb{R}^3$, il faut et il suffit que les vecteurs $u_1, u_2, u_3$ soient linéairement indépendants. Puisque nous sommes dans un espace de dimension 3 et que nous avons 3 vecteurs, cela équivaut à vérifier que la matrice $M_{\mathcal{B}'}$ formée par ces vecteurs en colonnes est inversible, ou de manière équivalente, que son déterminant est non nul.
    La matrice $M_{\mathcal{B}'}$ est un élément de $\mathcal{M}_{3,3}(\mathbb{R})$ :
    $$M_{\mathcal{B}'} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$
    Calculons le déterminant de $M_{\mathcal{B}'}$ en utilisant la règle de Sarrus ou un développement par cofacteurs. Développons par rapport à la première ligne :
    $$\det(M_{\mathcal{B}'}) = 1 \cdot \det \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} - 0 \cdot \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + 1 \cdot \det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
    $$\det(M_{\mathcal{B}'}) = 1 \cdot (1 \cdot 1 - 0 \cdot 1) - 0 + 1 \cdot (1 \cdot 1 - 1 \cdot 0)$$
    $$\det(M_{\mathcal{B}'}) = 1 \cdot (1 - 0) + 1 \cdot (1 - 0)$$
    $$\det(M_{\mathcal{B}'}) = 1 + 1$$
    $$\det(M_{\mathcal{B}'}) = 2$$
    Puisque $\det(M_{\mathcal{B}'}) = 2 \neq 0$, les vecteurs $u_1, u_2, u_3$ sont linéairement indépendants. Par conséquent, $\mathcal{B}'$ est bien une base de $\mathbb{R}^3$.

3.  **Coordonnées d'un vecteur dans différentes bases**
    Soit un vecteur $v \in E$ défini par $v = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}$.

    a.  Donnez les coordonnées du vecteur $v$ dans la base canonique $\mathcal{B}_c$.
        *Réponse :*
        Par définition de la base canonique, les coordonnées d'un vecteur $v = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$ dans $\mathcal{B}_c$ sont $(x, y, z)$.
        Ainsi, les coordonnées de $v$ dans $\mathcal{B}_c$, notées $[v]_{\mathcal{B}_c}$, sont :
        $$[v]_{\mathcal{B}_c} = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}$$

    b.  Calculez les coordonnées du vecteur $v$ dans la base $\mathcal{B}'$.
        *Calcul :*
        Nous cherchons des scalaires $\alpha_1, \alpha_2, \alpha_3 \in \mathbb{R}$ tels que $v = \alpha_1 u_1 + \alpha_2 u_2 + \alpha_3 u_3$.
        Ceci se traduit par le système d'équations linéaires suivant :
        $$\begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} = \alpha_1 \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \alpha_2 \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + \alpha_3 \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$
        $$\begin{cases}
        1\alpha_1 + 0\alpha_2 + 1\alpha_3 = 2 \\
        1\alpha_1 + 1\alpha_2 + 0\alpha_3 = 3 \\
        0\alpha_1 + 1\alpha_2 + 1\alpha_3 = 1
        \end{cases}$$
        Ce système peut s'écrire sous forme matricielle $M_{\mathcal{B}'} [\alpha]_{\mathcal{B}'} = [v]_{\mathcal{B}_c}$, où $[\alpha]_{\mathcal{B}'} = \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{pmatrix}$.
        Nous allons résoudre ce système en utilisant la méthode d'élimination de Gauss-Jordan sur la matrice augmentée :
        $$\left( \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 1 & 1 & 0 & 3 \\ 0 & 1 & 1 & 1 \end{array} \right)$$
        Appliquons les opérations sur les lignes :
        $L_2 \leftarrow L_2 - L_1$
        $$\left( \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 0 & 1 & -1 & 1 \\ 0 & 1 & 1 & 1 \end{array} \right)$$
        $L_3 \leftarrow L_3 - L_2$
        $$\left( \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 2 & 0 \end{array} \right)$$
        De la troisième ligne, nous obtenons $2\alpha_3 = 0$, donc $\alpha_3 = 0$.
        Substituons $\alpha_3 = 0$ dans la deuxième ligne :
        $\alpha_2 - \alpha_3 = 1 \implies \alpha_2 - 0 = 1 \implies \alpha_2 = 1$.
        Substituons $\alpha_3 = 0$ dans la première ligne :
        $\alpha_1 + \alpha_3 = 2 \implies \alpha_1 + 0 = 2 \implies \alpha_1 = 2$.
        Ainsi, les coordonnées de $v$ dans la base $\mathcal{B}'$, notées $[v]_{\mathcal{B}'}$, sont :
        $$[v]_{\mathcal{B}'} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}$$

## Partie 2 : Matrices de passage

1.  **Matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}'$**
    Déterminez la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ (parfois notée $P_{\mathcal{B}' \leftarrow \mathcal{B}_c}$) de la base canonique $\mathcal{B}_c$ à la base $\mathcal{B}'$. Cette matrice est un élément de $\mathcal{M}_{3,3}(\mathbb{R})$.

    *Calcul :*
    La matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}'$ a pour colonnes les vecteurs de la base $\mathcal{B}'$ exprimés dans la base $\mathcal{B}_c$.
    Les vecteurs $u_1, u_2, u_3$ sont déjà donnés avec leurs coordonnées dans $\mathcal{B}_c$.
    $$P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix} | & | & | \\ u_1 & u_2 & u_3 \\ | & | & | \end{pmatrix}_{\mathcal{B}_c} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

2.  **Matrice de passage de $\mathcal{B}'$ à $\mathcal{B}_c$**
    Déterminez la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ (parfois notée $P_{\mathcal{B}_c \leftarrow \mathcal{B}'}$) de la base $\mathcal{B}'$ à la base canonique $\mathcal{B}_c$. Cette matrice est un élément de $\mathcal{M}_{3,3}(\mathbb{R})$.

    *Calcul :*
    La matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ est l'inverse de la matrice $P_{\mathcal{B}_c \to \mathcal{B}'}$.
    Nous devons calculer $(P_{\mathcal{B}_c \to \mathcal{B}'})^{-1}$. Nous utiliserons la méthode de Gauss-Jordan sur la matrice augmentée $[P_{\mathcal{B}_c \to \mathcal{B}'} | I_3]$.
    $$P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$
    Matrice augmentée :
    $$\left( \begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 & 1 \end{array} \right)$$
    Opérations sur les lignes :
    $L_2 \leftarrow L_2 - L_1$
    $$\left( \begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & -1 & -1 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 & 1 \end{array} \right)$$
    $L_3 \leftarrow L_3 - L_2$
    $$\left( \begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & -1 & -1 & 1 & 0 \\ 0 & 0 & 2 & 1 & -1 & 1 \end{array} \right)$$
    $L_3 \leftarrow \frac{1}{2} L_3$
    $$\left( \begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & -1 & -1 & 1 & 0 \\ 0 & 0 & 1 & 1/2 & -1/2 & 1/2 \end{array} \right)$$
    $L_2 \leftarrow L_2 + L_3$
    $$\left( \begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & -1/2 & 1/2 & 1/2 \\ 0 & 0 & 1 & 1/2 & -1/2 & 1/2 \end{array} \right)$$
    $L_1 \leftarrow L_1 - L_3$
    $$\left( \begin{array}{ccc|ccc} 1 & 0 & 0 & 1/2 & 1/2 & -1/2 \\ 0 & 1 & 0 & -1/2 & 1/2 & 1/2 \\ 0 & 0 & 1 & 1/2 & -1/2 & 1/2 \end{array} \right)$$
    Donc, la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ est :
    $$P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix} 1/2 & 1/2 & -1/2 \\ -1/2 & 1/2 & 1/2 \\ 1/2 & -1/2 & 1/2 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$$

## Partie 3 : Vérification des propriétés

1.  **Vérification de l'inversibilité**
    Vérifiez que $P_{\mathcal{B}_c \to \mathcal{B}'} \cdot P_{\mathcal{B}' \to \mathcal{B}_c} = I_3$ et $P_{\mathcal{B}' \to \mathcal{B}_c} \cdot P_{\mathcal{B}_c \to \mathcal{B}'} = I_3$, où $I_3$ est la matrice identité de taille $3 \times 3$.

    *Calcul :*
    Soit $P = P_{\mathcal{B}_c \to \mathcal{B}'}$ et $P^{-1} = P_{\mathcal{B}' \to \mathcal{B}_c}$.
    $$P \cdot P^{-1} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \cdot \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$$
    $$P \cdot P^{-1} = \frac{1}{2} \begin{pmatrix}
    (1)(1) + (0)(-1) + (1)(1) & (1)(1) + (0)(1) + (1)(-1) & (1)(-1) + (0)(1) + (1)(1) \\
    (1)(1) + (1)(-1) + (0)(1) & (1)(1) + (1)(1) + (0)(-1) & (1)(-1) + (1)(1) + (0)(1) \\
    (0)(1) + (1)(-1) + (1)(1) & (0)(1) + (1)(1) + (1)(-1) & (0)(-1) + (1)(1) + (1)(1)
    \end{pmatrix}$$
    $$P \cdot P^{-1} = \frac{1}{2} \begin{pmatrix}
    1 + 0 + 1 & 1 + 0 - 1 & -1 + 0 + 1 \\
    1 - 1 + 0 & 1 + 1 + 0 & -1 + 1 + 0 \\
    0 - 1 + 1 & 0 + 1 - 1 & 0 + 1 + 1
    \end{pmatrix}$$
    $$P \cdot P^{-1} = \frac{1}{2} \begin{pmatrix}
    2 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 0 & 2
    \end{pmatrix} = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix} = I_3$$
    La vérification de $P^{-1} \cdot P = I_3$ est similaire et est également satisfaite par la définition de l'inverse.

2.  **Vérification des coordonnées**
    Utilisez les matrices de passage pour retrouver les coordonnées de $v$ dans $\mathcal{B}'$ à partir de ses coordonnées dans $\mathcal{B}_c$, et vice-versa.

    a.  Retrouver $[v]_{\mathcal{B}'}$ à partir de $[v]_{\mathcal{B}_c}$ :
        La formule est $[v]_{\mathcal{B}'} = P_{\mathcal{B}' \to \mathcal{B}_c} [v]_{\mathcal{B}_c}$.
        $$[v]_{\mathcal{B}'} = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}$$
        $$[v]_{\mathcal{B}'} = \frac{1}{2} \begin{pmatrix}
        (1)(2) + (1)(3) + (-1)(1) \\
        (-1)(2) + (1)(3) + (1)(1) \\
        (1)(2) + (-1)(3) + (1)(1)
        \end{pmatrix}$$
        $$[v]_{\mathcal{B}'} = \frac{1}{2} \begin{pmatrix}
        2 + 3 - 1 \\
        -2 + 3 + 1 \\
        2 - 3 + 1
        \end{pmatrix}$$
        $$[v]_{\mathcal{B}'} = \frac{1}{2} \begin{pmatrix}
        4 \\
        2 \\
        0
        \end{pmatrix} = \begin{pmatrix}
        2 \\
        1 \\
        0
        \end{pmatrix}$$
        Ceci correspond bien au résultat obtenu dans la Partie 1.3.b.

    b.  Retrouver $[v]_{\mathcal{B}_c}$ à partir de $[v]_{\mathcal{B}'}$ :
        La formule est $[v]_{\mathcal{B}_c} = P_{\mathcal{B}_c \to \mathcal{B}'} [v]_{\mathcal{B}'}$.
        $$[v]_{\mathcal{B}_c} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}$$
        $$[v]_{\mathcal{B}_c} = \begin{pmatrix}
        (1)(2) + (0)(1) + (1)(0) \\
        (1)(2) + (1)(1) + (0)(0) \\
        (0)(2) + (1)(1) + (1)(0)
        \end{pmatrix}$$
        $$[v]_{\mathcal{B}_c} = \begin{pmatrix}
        2 + 0 + 0 \\
        2 + 1 + 0 \\
        0 + 1 + 0
        \end{pmatrix}$$
        $$[v]_{\mathcal{B}_c} = \begin{pmatrix}
        2 \\
        3 \\
        1
        \end{pmatrix}$$
        Ceci correspond bien au résultat obtenu dans la Partie 1.3.a.

## Partie 4 : Application aux transformations linéaires

1.  **Matrice d'une transformation linéaire dans la base canonique**
    Soit $f: E \to E$ une application linéaire, où $E = \mathbb{R}^3$. L'application $f$ est définie pour tout vecteur $(x,y,z)^T \in \mathbb{R}^3$ par :
    $$f\left(\begin{pmatrix} x \\ y \\ z \end{pmatrix}\right) = \begin{pmatrix} x+y \\ y+z \\ x+z \end{pmatrix}$$
    Déterminez la matrice $M$ de l'application linéaire $f$ dans la base canonique $\mathcal{B}_c$. Cette matrice est un élément de $\mathcal{M}_{3,3}(\mathbb{R})$.

    *Calcul :*
    La matrice $M$ de $f$ dans $\mathcal{B}_c$ a pour colonnes les images des vecteurs de $\mathcal{B}_c$ par $f$, exprimées dans $\mathcal{B}_c$.
    Calculons $f(e_1)$, $f(e_2)$, $f(e_3)$ :
    $$f(e_1) = f\left(\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1+0 \\ 0+0 \\ 1+0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$
    $$f(e_2) = f\left(\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 0+1 \\ 1+0 \\ 0+0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$$
    $$f(e_3) = f\left(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0+0 \\ 0+1 \\ 0+1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$
    La matrice $M$ est donc :
    $$M = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$$

2.  **Matrice de $f$ dans la nouvelle base $\mathcal{B}'$**
    Déterminez la matrice $M'$ de l'application linéaire $f$ dans la base $\mathcal{B}'$. Cette matrice est un élément de $\mathcal{M}_{3,3}(\mathbb{R})$.
    Utilisez la formule de changement de base pour les matrices d'applications linéaires : $M' = P_{\mathcal{B}' \to \mathcal{B}_c} M P_{\mathcal{B}_c \to \mathcal{B}'}$.

    *Calcul :*
    Nous avons $P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$, $P_{\mathcal{B}' \to \mathcal{B}_c} = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$, et $M = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$.
    Calculons d'abord le produit $M \cdot P_{\mathcal{B}_c \to \mathcal{B}'}$ :
    $$M \cdot P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$
    $$M \cdot P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    (1)(1)+(1)(1)+(0)(0) & (1)(0)+(1)(1)+(0)(1) & (1)(1)+(1)(0)+(0)(1) \\
    (0)(1)+(1)(1)+(1)(0) & (0)(0)+(1)(1)+(1)(1) & (0)(1)+(1)(0)+(1)(1) \\
    (1)(1)+(0)(1)+(1)(0) & (1)(0)+(0)(1)+(1)(1) & (1)(1)+(0)(0)+(1)(1)
    \end{pmatrix}$$
    $$M \cdot P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    1+1+0 & 0+1+0 & 1+0+0 \\
    0+1+0 & 0+1+1 & 0+0+1 \\
    1+0+0 & 0+0+1 & 1+0+1
    \end{pmatrix}$$
    $$M \cdot P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    2 & 1 & 1 \\
    1 & 2 & 1 \\
    1 & 1 & 2
    \end{pmatrix}$$
    Maintenant, calculons $M' = P_{\mathcal{B}' \to \mathcal{B}_c} \cdot (M \cdot P_{\mathcal{B}_c \to \mathcal{B}'})$ :
    $$M' = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$
    $$M' = \frac{1}{2} \begin{pmatrix}
    (1)(2)+(1)(1)+(-1)(1) & (1)(1)+(1)(2)+(-1)(1) & (1)(1)+(1)(1)+(-1)(2) \\
    (-1)(2)+(1)(1)+(1)(1) & (-1)(1)+(1)(2)+(1)(1) & (-1)(1)+(1)(1)+(1)(2) \\
    (1)(2)+(-1)(1)+(1)(1) & (1)(1)+(-1)(2)+(1)(1) & (1)(1)+(-1)(1)+(1)(2)
    \end{pmatrix}$$
    $$M' = \frac{1}{2} \begin{pmatrix}
    2+1-1 & 1+2-1 & 1+1-2 \\
    -2+1+1 & -1+2+1 & -1+1+2 \\
    2-1+1 & 1-2+1 & 1-1+2
    \end{pmatrix}$$
    $$M' = \frac{1}{2} \begin{pmatrix}
    2 & 2 & 0 \\
    0 & 2 & 2 \\
    2 & 0 & 2
    \end{pmatrix}$$
    $$M' = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 1 \\
    1 & 0 & 1
    \end{pmatrix}$$
    Il est intéressant de noter que dans ce cas particulier, $M' = M$. Cela signifie que la matrice de l'application linéaire $f$ est la même dans la base canonique $\mathcal{B}_c$ et dans la base $\mathcal{B}'$. Ce n'est pas une généralité, mais une coïncidence due à la structure spécifique de $f$ et de $\mathcal{B}'$. En effet, les vecteurs de $\mathcal{B}'$ sont précisément les images des vecteurs de $\mathcal{B}_c$ par $f$, à un réarrangement près.

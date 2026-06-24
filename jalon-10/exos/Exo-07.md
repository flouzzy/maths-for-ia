---
title: "Exercice 07"
subtitle: "Changements de base, matrices de passage et matrices d'applications linéaires"
date: "2023-10-27"
authors: ["Votre Nom / Nom de l'enseignant"]
keywords: ["algèbre linéaire", "espace vectoriel", "base", "coordonnées", "matrice de passage", "changement de base", "transformation linéaire", "matrice d'une application linéaire", "polynômes", "Mathématiques pour l'IA", "L1", "L2", "L3", "Master"]
lang: "fr"
geometry: "a4paper, margin=1in"
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
  - \usepackage{amsfonts}
  - \usepackage{amsthm}
  - \usepackage{mathrsfs}
  - \usepackage{enumitem}
  - \usepackage{xcolor}
---

# Exercice 07 : Changements de base et matrices d'applications linéaires

Cet exercice approfondit les concepts fondamentaux de changement de base, de matrices de passage et de représentation matricielle d'applications linéaires. Il est conçu pour développer une compréhension rigoureuse de ces notions en les appliquant à un espace vectoriel de polynômes. Chaque étape de calcul doit être explicitée avec la plus grande précision.

Soit $\mathbb{K}$ le corps des nombres réels, $\mathbb{K} = \mathbb{R}$.
Soit $E$ l'espace vectoriel des polynômes à coefficients réels de degré inférieur ou égal à 2, noté $E = \mathbb{R}_2[X]$.
La dimension de $E$ sur $\mathbb{R}$ est $\dim_{\mathbb{R}}(E) = 3$.

## Partie 1 : Définition et vérification des bases

1.  **Base canonique de $E$**
    Soit $\mathcal{B}_c = (e_0, e_1, e_2)$ une famille de vecteurs de $E$, où $e_0(X) = 1$, $e_1(X) = X$, et $e_2(X) = X^2$.
    1.1.   Démontrer que $\mathcal{B}_c$ est une base de l'espace vectoriel $E = \mathbb{R}_2[X]$.
    \newline
    *Démonstration :*
    Pour démontrer que la famille $\mathcal{B}_c$ est une base de l'espace vectoriel $E$, il est nécessaire et suffisant de prouver qu'elle est à la fois une famille génératrice de $E$ et une famille libre dans $E$.

    *   **Preuve que $\mathcal{B}_c$ est une famille génératrice de $E$ :**
        Soit $P(X)$ un polynôme quelconque appartenant à l'espace vectoriel $E = \mathbb{R}_2[X]$. Par définition de cet espace, $P(X)$ peut être écrit sous la forme générale :
        $P(X) = a_0 + a_1 X + a_2 X^2$, où $a_0, a_1, a_2$ sont des scalaires réels appartenant à $\mathbb{R}$.
        Nous pouvons exprimer $P(X)$ comme une combinaison linéaire des vecteurs de la famille $\mathcal{B}_c$ :
        $P(X) = a_0 \cdot 1 + a_1 \cdot X + a_2 \cdot X^2$
        $P(X) = a_0 \cdot e_0(X) + a_1 \cdot e_1(X) + a_2 \cdot e_2(X)$.
        Puisque tout polynôme de $E$ peut être écrit comme une combinaison linéaire des vecteurs de $\mathcal{B}_c$, la famille $\mathcal{B}_c$ est bien une famille génératrice de $E$.

    *   **Preuve que $\mathcal{B}_c$ est une famille libre dans $E$ :**
        Considérons une combinaison linéaire des vecteurs de $\mathcal{B}_c$ qui est égale au vecteur nul de $E$, c'est-à-dire le polynôme nul $0_E(X) = 0$ :
        $\alpha_0 e_0(X) + \alpha_1 e_1(X) + \alpha_2 e_2(X) = 0_E(X)$, où $\alpha_0, \alpha_1, \alpha_2$ sont des scalaires réels.
        En substituant les expressions des vecteurs de $\mathcal{B}_c$, nous obtenons :
        $\alpha_0 \cdot 1 + \alpha_1 \cdot X + \alpha_2 \cdot X^2 = 0$.
        Par la propriété d'unicité de la représentation d'un polynôme et de l'égalité des polynômes, un polynôme est identiquement nul si et seulement si tous ses coefficients sont nuls.
        Par conséquent, nous devons avoir :
        $\alpha_0 = 0$
        $\alpha_1 = 0$
        $\alpha_2 = 0$.
        Puisque la seule combinaison linéaire des vecteurs de $\mathcal{B}_c$ qui produit le polynôme nul est celle où tous les coefficients sont nuls, la famille $\mathcal{B}_c$ est une famille libre.

    *   **Conclusion :**
        La famille $\mathcal{B}_c$ est à la fois génératrice et libre dans $E$. De plus, le nombre de vecteurs dans $\mathcal{B}_c$ est 3, ce qui est égal à la dimension de $E$.
        Par conséquent, $\mathcal{B}_c$ est une base de l'espace vectoriel $E = \mathbb{R}_2[X]$.

2.  **Nouvelle base de $E$**
    Soit $\mathcal{B}' = (e'_0, e'_1, e'_2)$ une autre famille de vecteurs de $E$, où $e'_0(X) = 1$, $e'_1(X) = X-1$, et $e'_2(X) = (X-1)^2$.
    2.1.   Démontrer que $\mathcal{B}'$ est une base de l'espace vectoriel $E = \mathbb{R}_2[X]$.
    \newline
    *Démonstration :*
    Pour démontrer que la famille $\mathcal{B}'$ est une base de $E$, nous allons d'abord vérifier que ses vecteurs appartiennent à $E$, puis prouver qu'elle est une famille libre dans $E$. Étant donné que le nombre de vecteurs dans $\mathcal{B}'$ est 3, ce qui est égal à la dimension de $E$, une famille libre de 3 vecteurs dans $E$ est nécessairement une base de $E$.

    *   **Vérification de l'appartenance des vecteurs à $E$ :**
        $e'_0(X) = 1$ est un polynôme de degré 0, donc $e'_0 \in \mathbb{R}_2[X]$.
        $e'_1(X) = X-1$ est un polynôme de degré 1, donc $e'_1 \in \mathbb{R}_2[X]$.
        $e'_2(X) = (X-1)^2 = X^2 - 2X + 1$ est un polynôme de degré 2, donc $e'_2 \in \mathbb{R}_2[X]$.
        Tous les vecteurs de la famille $\mathcal{B}'$ appartiennent bien à l'espace vectoriel $E$.

    *   **Preuve que $\mathcal{B}'$ est une famille libre dans $E$ :**
        Considérons une combinaison linéaire des vecteurs de $\mathcal{B}'$ qui est égale au polynôme nul $0_E(X) = 0$ :
        $\beta_0 e'_0(X) + \beta_1 e'_1(X) + \beta_2 e'_2(X) = 0_E(X)$, où $\beta_0, \beta_1, \beta_2$ sont des scalaires réels.
        En substituant les expressions des vecteurs de $\mathcal{B}'$, nous obtenons :
        $\beta_0 \cdot 1 + \beta_1 \cdot (X-1) + \beta_2 \cdot (X-1)^2 = 0$.
        Développons cette expression polynomiale :
        $\beta_0 + \beta_1 X - \beta_1 + \beta_2 (X^2 - 2X + 1) = 0$
        $\beta_0 + \beta_1 X - \beta_1 + \beta_2 X^2 - 2\beta_2 X + \beta_2 = 0$.
        Regroupons les termes par puissance décroissante de $X$ :
        $\beta_2 X^2 + (\beta_1 - 2\beta_2) X + (\beta_0 - \beta_1 + \beta_2) = 0$.
        Par identification des coefficients avec ceux du polynôme nul (qui sont tous nuls), nous obtenons le système d'équations linéaires suivant :
        1.  $\beta_2 = 0$
        2.  $\beta_1 - 2\beta_2 = 0$
        3.  $\beta_0 - \beta_1 + \beta_2 = 0$

        Résolvons ce système :
        De l'équation (1), nous avons directement $\beta_2 = 0$.
        Substituons la valeur de $\beta_2$ dans l'équation (2) :
        $\beta_1 - 2(0) = 0 \implies \beta_1 = 0$.
        Substituons les valeurs de $\beta_1$ et $\beta_2$ dans l'équation (3) :
        $\beta_0 - 0 + 0 = 0 \implies \beta_0 = 0$.
        Ainsi, nous avons trouvé que $\beta_0 = 0$, $\beta_1 = 0$, et $\beta_2 = 0$.
        Puisque la seule combinaison linéaire des vecteurs de $\mathcal{B}'$ qui produit le polynôme nul est celle où tous les coefficients sont nuls, la famille $\mathcal{B}'$ est une famille libre.

    *   **Conclusion :**
        La famille $\mathcal{B}'$ est une famille libre de 3 vecteurs dans un espace vectoriel $E$ de dimension 3.
        Par conséquent, $\mathcal{B}'$ est une base de l'espace vectoriel $E = \mathbb{R}_2[X]$.

## Partie 2 : Matrices de passage

1.  **Matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}'$**
    Calculer la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ de la base $\mathcal{B}_c$ à la base $\mathcal{B}'$.
    \newline
    *Calcul :*
    La matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ est la matrice dont les colonnes sont les vecteurs de coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ exprimés dans l'ancienne base $\mathcal{B}_c$.
    Les vecteurs de la base $\mathcal{B}'$ sont :
    $e'_0(X) = 1$
    $e'_1(X) = X-1$
    $e'_2(X) = (X-1)^2 = X^2 - 2X + 1$

    Les vecteurs de la base $\mathcal{B}_c$ sont $e_0(X) = 1$, $e_1(X) = X$, $e_2(X) = X^2$.

    Exprimons chaque vecteur de $\mathcal{B}'$ comme une combinaison linéaire des vecteurs de $\mathcal{B}_c$:
    *   Pour $e'_0(X) = 1$:
        $e'_0(X) = 1 \cdot e_0(X) + 0 \cdot e_1(X) + 0 \cdot e_2(X)$.
        Le vecteur de coordonnées de $e'_0$ dans $\mathcal{B}_c$ est $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.

    *   Pour $e'_1(X) = X-1$:
        $e'_1(X) = -1 \cdot e_0(X) + 1 \cdot e_1(X) + 0 \cdot e_2(X)$.
        Le vecteur de coordonnées de $e'_1$ dans $\mathcal{B}_c$ est $\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$.

    *   Pour $e'_2(X) = X^2 - 2X + 1$:
        $e'_2(X) = 1 \cdot e_0(X) - 2 \cdot e_1(X) + 1 \cdot e_2(X)$.
        Le vecteur de coordonnées de $e'_2$ dans $\mathcal{B}_c$ est $\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}$.

    En arrangeant ces vecteurs colonnes, nous formons la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$:
    $P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    1 & -1 & 1 \\
    0 & 1 & -2 \\
    0 & 0 & 1
    \end{pmatrix}$.

2.  **Matrice de passage de $\mathcal{B}'$ à $\mathcal{B}_c$**
    Calculer la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ de la base $\mathcal{B}'$ à la base $\mathcal{B}_c$.
    \newline
    *Calcul (par inversion) :*
    La matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ est l'inverse de la matrice $P_{\mathcal{B}_c \to \mathcal{B}'}$.
    $P_{\mathcal{B}' \to \mathcal{B}_c} = (P_{\mathcal{B}_c \to \mathcal{B}'})^{-1}$.
    Nous allons utiliser la méthode de Gauss-Jordan pour calculer l'inverse de $P_{\mathcal{B}_c \to \mathcal{B}'}$. Soit $A = P_{\mathcal{B}_c \to \mathcal{B}'}$. Nous formons la matrice augmentée $[A | I_3]$ et nous la transformons en $[I_3 | A^{-1}]$ par des opérations élémentaires sur les lignes.

    La matrice augmentée initiale est :
    $[A | I_3] = \begin{pmatrix}
    1 & -1 & 1 & | & 1 & 0 & 0 \\
    0 & 1 & -2 & | & 0 & 1 & 0 \\
    0 & 0 & 1 & | & 0 & 0 & 1
    \end{pmatrix}$

    L'objectif est de transformer la partie gauche en la matrice identité $I_3$. La matrice $A$ est déjà triangulaire supérieure. Nous allons procéder par des opérations sur les lignes pour annuler les éléments au-dessus de la diagonale.

    *   Opération $L_1 \leftarrow L_1 - L_3$ (pour annuler l'élément $a_{13}$):
        $\begin{pmatrix}
        1 & -1 & 1 - 1 & | & 1 - 0 & 0 - 0 & 0 - 1 \\
        0 & 1 & -2 & | & 0 & 1 & 0 \\
        0 & 0 & 1 & | & 0 & 0 & 1
        \end{pmatrix} = \begin{pmatrix}
        1 & -1 & 0 & | & 1 & 0 & -1 \\
        0 & 1 & -2 & | & 0 & 1 & 0 \\
        0 & 0 & 1 & | & 0 & 0 & 1
        \end{pmatrix}$

    *   Opération $L_2 \leftarrow L_2 + 2L_3$ (pour annuler l'élément $a_{23}$):
        $\begin{pmatrix}
        1 & -1 & 0 & | & 1 & 0 & -1 \\
        0 & 1 & -2 + 2(1) & | & 0 + 2(0) & 1 + 2(0) & 0 + 2(1) \\
        0 & 0 & 1 & | & 0 & 0 & 1
        \end{pmatrix} = \begin{pmatrix}
        1 & -1 & 0 & | & 1 & 0 & -1 \\
        0 & 1 & 0 & | & 0 & 1 & 2 \\
        0 & 0 & 1 & | & 0 & 0 & 1
        \end{pmatrix}$

    *   Opération $L_1 \leftarrow L_1 + L_2$ (pour annuler l'élément $a_{12}$):
        $\begin{pmatrix}
        1 & -1 + 1 & 0 & | & 1 + 0 & 0 + 1 & -1 + 2 \\
        0 & 1 & 0 & | & 0 & 1 & 2 \\
        0 & 0 & 1 & | & 0 & 0 & 1
        \end{pmatrix} = \begin{pmatrix}
        1 & 0 & 0 & | & 1 & 1 & 1 \\
        0 & 1 & 0 & | & 0 & 1 & 2 \\
        0 & 0 & 1 & | & 0 & 0 & 1
        \end{pmatrix}$

    La partie gauche de la matrice augmentée est maintenant la matrice identité $I_3$. La partie droite est l'inverse de $A$.
    Donc, la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ est :
    $P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.

    *Calcul (par définition) :*
    La matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ est la matrice dont les colonnes sont les vecteurs de coordonnées des vecteurs de la nouvelle base $\mathcal{B}_c$ exprimés dans l'ancienne base $\mathcal{B}'$.
    Les vecteurs de la base $\mathcal{B}_c$ sont :
    $e_0(X) = 1$
    $e_1(X) = X$
    $e_2(X) = X^2$

    Les vecteurs de la base $\mathcal{B}'$ sont :
    $e'_0(X) = 1$
    $e'_1(X) = X-1$
    $e'_2(X) = (X-1)^2$

    Exprimons chaque vecteur de $\mathcal{B}_c$ comme une combinaison linéaire des vecteurs de $\mathcal{B}'$:
    *   Pour $e_0(X) = 1$:
        $e_0(X) = 1 \cdot e'_0(X) + 0 \cdot e'_1(X) + 0 \cdot e'_2(X)$.
        Le vecteur de coordonnées de $e_0$ dans $\mathcal{B}'$ est $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.

    *   Pour $e_1(X) = X$:
        Nous cherchons des scalaires $a, b, c \in \mathbb{R}$ tels que $X = a \cdot e'_0(X) + b \cdot e'_1(X) + c \cdot e'_2(X)$.
        $X = a \cdot 1 + b \cdot (X-1) + c \cdot (X-1)^2$.
        Développons l'expression du côté droit :
        $X = a + bX - b + c(X^2 - 2X + 1)$
        $X = cX^2 + (b-2c)X + (a-b+c)$.
        Par identification des coefficients avec le polynôme $X$ (qui est $0X^2 + 1X + 0$) :
        $c = 0$
        $b-2c = 1 \implies b-2(0) = 1 \implies b=1$
        $a-b+c = 0 \implies a-1+0 = 0 \implies a=1$.
        Donc, $e_1(X) = 1 \cdot e'_0(X) + 1 \cdot e'_1(X) + 0 \cdot e'_2(X)$.
        Le vecteur de coordonnées de $e_1$ dans $\mathcal{B}'$ est $\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$.

    *   Pour $e_2(X) = X^2$:
        Nous cherchons des scalaires $a, b, c \in \mathbb{R}$ tels que $X^2 = a \cdot e'_0(X) + b \cdot e'_1(X) + c \cdot e'_2(X)$.
        $X^2 = a \cdot 1 + b \cdot (X-1) + c \cdot (X-1)^2$.
        Développons l'expression du côté droit :
        $X^2 = a + bX - b + c(X^2 - 2X + 1)$
        $X^2 = cX^2 + (b-2c)X + (a-b+c)$.
        Par identification des coefficients avec le polynôme $X^2$ (qui est $1X^2 + 0X + 0$) :
        $c = 1$
        $b-2c = 0 \implies b-2(1) = 0 \implies b=2$
        $a-b+c = 0 \implies a-2+1 = 0 \implies a=1$.
        Donc, $e_2(X) = 1 \cdot e'_0(X) + 2 \cdot e'_1(X) + 1 \cdot e'_2(X)$.
        Le vecteur de coordonnées de $e_2$ dans $\mathcal{B}'$ est $\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$.

    En arrangeant ces vecteurs colonnes, nous formons la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$:
    $P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.
    Les deux méthodes (inversion et définition directe) donnent le même résultat, ce qui confirme l'exactitude des calculs.

3.  **Vérification de la propriété des matrices de passage**
    Vérifier que $P_{\mathcal{B}_c \to \mathcal{B}'} \cdot P_{\mathcal{B}' \to \mathcal{B}_c} = I_3$, où $I_3$ est la matrice identité de taille $3 \times 3$.
    \newline
    *Vérification :*
    Nous avons calculé les matrices de passage suivantes :
    $P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    1 & -1 & 1 \\
    0 & 1 & -2 \\
    0 & 0 & 1
    \end{pmatrix}$
    et
    $P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Effectuons le produit matriciel $P_{\mathcal{B}_c \to \mathcal{B}'} \cdot P_{\mathcal{B}' \to \mathcal{B}_c}$ :
    $P_{\mathcal{B}_c \to \mathcal{B}'} \cdot P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & -1 & 1 \\
    0 & 1 & -2 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Calculons chaque élément $c_{ij}$ de la matrice résultante $C$:
    $c_{11} = (1)(1) + (-1)(0) + (1)(0) = 1 + 0 + 0 = 1$
    $c_{12} = (1)(1) + (-1)(1) + (1)(0) = 1 - 1 + 0 = 0$
    $c_{13} = (1)(1) + (-1)(2) + (1)(1) = 1 - 2 + 1 = 0$

    $c_{21} = (0)(1) + (1)(0) + (-2)(0) = 0 + 0 + 0 = 0$
    $c_{22} = (0)(1) + (1)(1) + (-2)(0) = 0 + 1 + 0 = 1$
    $c_{23} = (0)(1) + (1)(2) + (-2)(1) = 0 + 2 - 2 = 0$

    $c_{31} = (0)(1) + (0)(0) + (1)(0) = 0 + 0 + 0 = 0$
    $c_{32} = (0)(1) + (0)(1) + (1)(0) = 0 + 0 + 0 = 0$
    $c_{33} = (0)(1) + (0)(2) + (1)(1) = 0 + 0 + 1 = 1$

    Le produit matriciel est donc :
    $P_{\mathcal{B}_c \to \mathcal{B}'} \cdot P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix} = I_3$.
    La vérification est concluante, la propriété fondamentale des matrices de passage est satisfaite.

## Partie 3 : Changement de coordonnées d'un vecteur

Soit $P(X)$ un vecteur de l'espace vectoriel $E$ défini par $P(X) = 2X^2 - 3X + 1$.

1.  **Coordonnées de $P(X)$ dans la base $\mathcal{B}_c$**
    Déterminer le vecteur de coordonnées $[P]_{\mathcal{B}_c}$ de $P(X)$ dans la base canonique $\mathcal{B}_c$.
    \newline
    *Détermination :*
    La base canonique $\mathcal{B}_c = (e_0, e_1, e_2)$ est constituée des polynômes $(1, X, X^2)$.
    Le polynôme $P(X) = 2X^2 - 3X + 1$ peut être directement exprimé comme une combinaison linéaire des vecteurs de $\mathcal{B}_c$ :
    $P(X) = 1 \cdot 1 + (-3) \cdot X + 2 \cdot X^2$
    $P(X) = 1 \cdot e_0(X) + (-3) \cdot e_1(X) + 2 \cdot e_2(X)$.
    Le vecteur de coordonnées de $P(X)$ dans la base $\mathcal{B}_c$ est donc :
    $[P]_{\mathcal{B}_c} = \begin{pmatrix} 1 \\ -3 \\ 2 \end{pmatrix}$.

2.  **Coordonnées de $P(X)$ dans la base $\mathcal{B}'$ par matrice de passage**
    Utiliser la matrice de passage appropriée pour calculer le vecteur de coordonnées $[P]_{\mathcal{B}'}$ de $P(X)$ dans la base $\mathcal{B}'$.
    \newline
    *Calcul :*
    La relation entre les coordonnées d'un vecteur dans deux bases est donnée par la formule :
    $[P]_{\mathcal{B}'} = P_{\mathcal{B}' \to \mathcal{B}_c} [P]_{\mathcal{B}_c}$.
    Nous avons les matrices et vecteurs suivants :
    $P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$
    et
    $[P]_{\mathcal{B}_c} = \begin{pmatrix} 1 \\ -3 \\ 2 \end{pmatrix}$.

    Effectuons la multiplication matricielle :
    $[P]_{\mathcal{B}'} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix} 1 \\ -3 \\ 2 \end{pmatrix}$.

    Calculons chaque composante du vecteur résultant :
    Première composante : $(1)(1) + (1)(-3) + (1)(2) = 1 - 3 + 2 = 0$
    Deuxième composante : $(0)(1) + (1)(-3) + (2)(2) = 0 - 3 + 4 = 1$
    Troisième composante : $(0)(1) + (0)(-3) + (1)(2) = 0 + 0 + 2 = 2$

    Donc, le vecteur de coordonnées de $P(X)$ dans la base $\mathcal{B}'$ est :
    $[P]_{\mathcal{B}'} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}$.

3.  **Vérification directe des coordonnées de $P(X)$ dans la base $\mathcal{B}'$**
    Retrouver le vecteur de coordonnées $[P]_{\mathcal{B}'}$ en exprimant directement $P(X)$ comme une combinaison linéaire des vecteurs de $\mathcal{B}'$.
    \newline
    *Vérification :*
    Nous cherchons des scalaires $a, b, c \in \mathbb{R}$ tels que $P(X) = a \cdot e'_0(X) + b \cdot e'_1(X) + c \cdot e'_2(X)$.
    $P(X) = a \cdot 1 + b \cdot (X-1) + c \cdot (X-1)^2$.
    Nous savons que $P(X) = 2X^2 - 3X + 1$.

    Pour exprimer $P(X)$ dans la base $\mathcal{B}' = (1, X-1, (X-1)^2)$, il est commode d'effectuer un changement de variable. Posons $Y = X-1$, ce qui implique $X = Y+1$.
    Substituons $X$ par $Y+1$ dans l'expression de $P(X)$ :
    $P(Y+1) = 2(Y+1)^2 - 3(Y+1) + 1$.
    Développons l'expression :
    $P(Y+1) = 2(Y^2 + 2Y + 1) - 3Y - 3 + 1$
    $P(Y+1) = 2Y^2 + 4Y + 2 - 3Y - 3 + 1$
    Regroupons les termes par puissance de $Y$ :
    $P(Y+1) = 2Y^2 + (4-3)Y + (2-3+1)$
    $P(Y+1) = 2Y^2 + 1Y + 0$.
    Maintenant, substituons $Y$ par $X-1$ pour revenir à la variable $X$ :
    $P(X) = 2(X-1)^2 + 1(X-1) + 0 \cdot 1$.
    En comparant cette expression avec $a \cdot e'_0(X) + b \cdot e'_1(X) + c \cdot e'_2(X)$, nous identifions les coefficients :
    $a = 0$
    $b = 1$
    $c = 2$.
    Le vecteur de coordonnées de $P(X)$ dans la base $\mathcal{B}'$ est donc :
    $[P]_{\mathcal{B}'} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}$.
    Ce résultat est identique à celui obtenu par la matrice de passage, ce qui confirme l'exactitude des calculs.

## Partie 4 : Matrice d'une transformation linéaire et changement de base

Soit $L: E \to E$ l'application définie par $L(P(X)) = P'(X) + P(X)$, où $P'(X)$ désigne la dérivée de $P(X)$ par rapport à $X$.

1.  **Vérification de la linéarité de $L$**
    Démontrer que $L$ est une application linéaire.
    \newline
    *Démonstration :*
    Pour démontrer que $L$ est une application linéaire, nous devons vérifier deux propriétés :
    1.  **Additivité :** Pour tous vecteurs $P_1(X), P_2(X) \in E$, $L(P_1(X) + P_2(X)) = L(P_1(X)) + L(P_2(X))$.
    2.  **Homogénéité :** Pour tout vecteur $P(X) \in E$ et tout scalaire $\lambda \in \mathbb{R}$, $L(\lambda P(X)) = \lambda L(P(X))$.

    *   **Preuve de l'additivité :**
        Soient $P_1(X)$ et $P_2(X)$ deux polynômes quelconques de $E$.
        Appliquons $L$ à leur somme :
        $L(P_1(X) + P_2(X)) = (P_1(X) + P_2(X))' + (P_1(X) + P_2(X))$.
        En utilisant la propriété de linéarité de l'opérateur de dérivation (la dérivée d'une somme est la somme des dérivées) :
        $(P_1(X) + P_2(X))' = P_1'(X) + P_2'(X)$.
        Substituons cela dans l'expression de $L$:
        $L(P_1(X) + P_2(X)) = P_1'(X) + P_2'(X) + P_1(X) + P_2(X)$.
        Regroupons les termes pour faire apparaître la définition de $L$:
        $L(P_1(X) + P_2(X)) = (P_1'(X) + P_1(X)) + (P_2'(X) + P_2(X))$.
        Par définition de l'application $L$:
        $L(P_1(X) + P_2(X)) = L(P_1(X)) + L(P_2(X))$.
        La propriété d'additivité est vérifiée.

    *   **Preuve de l'homogénéité :**
        Soit $P(X)$ un polynôme quelconque de $E$ et $\lambda$ un scalaire réel.
        Appliquons $L$ au produit scalaire $\lambda P(X)$ :
        $L(\lambda P(X)) = (\lambda P(X))' + (\lambda P(X))$.
        En utilisant la propriété de linéarité de l'opérateur de dérivation (la dérivée d'un produit par un scalaire est le produit du scalaire par la dérivée) :
        $(\lambda P(X))' = \lambda P'(X)$.
        Substituons cela dans l'expression de $L$:
        $L(\lambda P(X)) = \lambda P'(X) + \lambda P(X)$.
        Factorisons le scalaire $\lambda$:
        $L(\lambda P(X)) = \lambda (P'(X) + P(X))$.
        Par définition de l'application $L$:
        $L(\lambda P(X)) = \lambda L(P(X))$.
        La propriété d'homogénéité est vérifiée.

    *   **Conclusion :**
        Puisque l'application $L$ satisfait à la fois les propriétés d'additivité et d'homogénéité, $L$ est une application linéaire de l'espace vectoriel $E$ vers lui-même.

2.  **Matrice de $L$ dans la base $\mathcal{B}_c$**
    Déterminer la matrice $M_{\mathcal{B}_c}(L)$ de l'application linéaire $L$ dans la base $\mathcal{B}_c$.
    \newline
    *Détermination :*
    La matrice $M_{\mathcal{B}_c}(L)$ est une matrice de taille $3 \times 3$ dont les colonnes sont les vecteurs de coordonnées des images des vecteurs de la base $\mathcal{B}_c$ par $L$, exprimés dans la base $\mathcal{B}_c$.
    La base $\mathcal{B}_c = (e_0, e_1, e_2)$ est $(1, X, X^2)$.

    *   Calcul de $L(e_0(X)) = L(1)$:
        La dérivée de $e_0(X) = 1$ est $e_0'(X) = 0$.
        $L(1) = e_0'(X) + e_0(X) = 0 + 1 = 1$.
        Exprimons $L(1)$ dans la base $\mathcal{B}_c$:
        $L(1) = 1 \cdot e_0(X) + 0 \cdot e_1(X) + 0 \cdot e_2(X)$.
        Le vecteur de coordonnées de $L(e_0)$ dans $\mathcal{B}_c$ est $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.

    *   Calcul de $L(e_1(X)) = L(X)$:
        La dérivée de $e_1(X) = X$ est $e_1'(X) = 1$.
        $L(X) = e_1'(X) + e_1(X) = 1 + X$.
        Exprimons $L(X)$ dans la base $\mathcal{B}_c$:
        $L(X) = 1 \cdot e_0(X) + 1 \cdot e_1(X) + 0 \cdot e_2(X)$.
        Le vecteur de coordonnées de $L(e_1)$ dans $\mathcal{B}_c$ est $\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$.

    *   Calcul de $L(e_2(X)) = L(X^2)$:
        La dérivée de $e_2(X) = X^2$ est $e_2'(X) = 2X$.
        $L(X^2) = e_2'(X) + e_2(X) = 2X + X^2$.
        Exprimons $L(X^2)$ dans la base $\mathcal{B}_c$:
        $L(X^2) = 0 \cdot e_0(X) + 2 \cdot e_1(X) + 1 \cdot e_2(X)$.
        Le vecteur de coordonnées de $L(e_2)$ dans $\mathcal{B}_c$ est $\begin{pmatrix} 0 \\ 2 \\ 1 \end{pmatrix}$.

    En arrangeant ces vecteurs colonnes, nous obtenons la matrice $M_{\mathcal{B}_c}(L)$:
    $M_{\mathcal{B}_c}(L) = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.

3.  **Matrice de $L$ dans la base $\mathcal{B}'$**
    Déterminer la matrice $M_{\mathcal{B}'}(L)$ de l'application linéaire $L$ dans la base $\mathcal{B}'$.
    \newline
    *Détermination :*
    La matrice $M_{\mathcal{B}'}(L)$ est une matrice de taille $3 \times 3$ dont les colonnes sont les vecteurs de coordonnées des images des vecteurs de la base $\mathcal{B}'$ par $L$, exprimés dans la base $\mathcal{B}'$.
    La base $\mathcal{B}' = (e'_0, e'_1, e'_2)$ est $(1, X-1, (X-1)^2)$.

    *   Calcul de $L(e'_0(X)) = L(1)$:
        La dérivée de $e'_0(X) = 1$ est $(e'_0)'(X) = 0$.
        $L(1) = (e'_0)'(X) + e'_0(X) = 0 + 1 = 1$.
        Exprimons $L(1)$ dans la base $\mathcal{B}'$:
        $L(1) = 1 \cdot e'_0(X) + 0 \cdot e'_1(X) + 0 \cdot e'_2(X)$.
        Le vecteur de coordonnées de $L(e'_0)$ dans $\mathcal{B}'$ est $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.

    *   Calcul de $L(e'_1(X)) = L(X-1)$:
        La dérivée de $e'_1(X) = X-1$ est $(e'_1)'(X) = 1$.
        $L(X-1) = (e'_1)'(X) + e'_1(X) = 1 + (X-1) = X$.
        Exprimons $L(X-1)$ dans la base $\mathcal{B}'$:
        Nous avons déjà établi dans la Partie 2.2 que $X = 1 \cdot e'_0(X) + 1 \cdot e'_1(X) + 0 \cdot e'_2(X)$.
        Le vecteur de coordonnées de $L(e'_1)$ dans $\mathcal{B}'$ est $\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$.

    *   Calcul de $L(e'_2(X)) = L((X-1)^2)$:
        La dérivée de $e'_2(X) = (X-1)^2$ est $(e'_2)'(X) = 2(X-1)$.
        $L((X-1)^2) = (e'_2)'(X) + e'_2(X) = 2(X-1) + (X-1)^2$.
        Exprimons $L((X-1)^2)$ dans la base $\mathcal{B}'$:
        $L((X-1)^2) = 0 \cdot e'_0(X) + 2 \cdot e'_1(X) + 1 \cdot e'_2(X)$.
        Le vecteur de coordonnées de $L(e'_2)$ dans $\mathcal{B}'$ est $\begin{pmatrix} 0 \\ 2 \\ 1 \end{pmatrix}$.

    En arrangeant ces vecteurs colonnes, nous obtenons la matrice $M_{\mathcal{B}'}(L)$:
    $M_{\mathcal{B}'}(L) = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.
    Il est à noter que, dans ce cas particulier, la matrice de l'opérateur $L$ est la même dans les deux bases, $M_{\mathcal{B}_c}(L) = M_{\mathcal{B}'}(L)$. Cela n'est pas une généralité mais une spécificité de cet opérateur et de ces bases.

4.  **Vérification de la formule de changement de base pour les matrices d'applications linéaires**
    Vérifier que la relation $M_{\mathcal{B}'}(L) = P_{\mathcal{B}' \to \mathcal{B}_c} \cdot M_{\mathcal{B}_c}(L) \cdot P_{\mathcal{B}_c \to \mathcal{B}'}$ est satisfaite.
    \newline
    *Vérification :*
    Nous avons les matrices suivantes :
    $P_{\mathcal{B}' \to \mathcal{B}_c} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$

    $M_{\mathcal{B}_c}(L) = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$

    $P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    1 & -1 & 1 \\
    0 & 1 & -2 \\
    0 & 0 & 1
    \end{pmatrix}$

    Calculons le produit de droite à gauche, en commençant par $M_{\text{temp}} = M_{\mathcal{B}_c}(L) \cdot P_{\mathcal{B}_c \to \mathcal{B}'}$ :
    $M_{\text{temp}} = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
    1 & -1 & 1 \\
    0 & 1 & -2 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Calculons chaque élément $m_{ij}$ de la matrice $M_{\text{temp}}$:
    $m_{11} = (1)(1) + (1)(0) + (0)(0) = 1 + 0 + 0 = 1$
    $m_{12} = (1)(-1) + (1)(1) + (0)(0) = -1 + 1 + 0 = 0$
    $m_{13} = (1)(1) + (1)(-2) + (0)(1) = 1 - 2 + 0 = -1$

    $m_{21} = (0)(1) + (1)(0) + (2)(0) = 0 + 0 + 0 = 0$
    $m_{22} = (0)(-1) + (1)(1) + (2)(0) = 0 + 1 + 0 = 1$
    $m_{23} = (0)(1) + (1)(-2) + (2)(1) = 0 - 2 + 2 = 0$

    $m_{31} = (0)(1) + (0)(0) + (1)(0) = 0 + 0 + 0 = 0$
    $m_{32} = (0)(-1) + (0)(1) + (1)(0) = 0 + 0 + 0 = 0$
    $m_{33} = (0)(1) + (0)(-2) + (1)(1) = 0 + 0 + 1 = 1$

    Donc, la matrice intermédiaire est :
    $M_{\text{temp}} = \begin{pmatrix}
    1 & 0 & -1 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Maintenant, calculons le produit final $P_{\mathcal{B}' \to \mathcal{B}_c} \cdot M_{\text{temp}}$:
    $P_{\mathcal{B}' \to \mathcal{B}_c} \cdot M_{\text{temp}} = \begin{pmatrix}
    1 & 1 & 1 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
    1 & 0 & -1 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Calculons chaque élément $c'_{ij}$ de la matrice résultante $C'$:
    $c'_{11} = (1)(1) + (1)(0) + (1)(0) = 1 + 0 + 0 = 1$
    $c'_{12} = (1)(0) + (1)(1) + (1)(0) = 0 + 1 + 0 = 1$
    $c'_{13} = (1)(-1) + (1)(0) + (1)(1) = -1 + 0 + 1 = 0$

    $c'_{21} = (0)(1) + (1)(0) + (2)(0) = 0 + 0 + 0 = 0$
    $c'_{22} = (0)(0) + (1)(1) + (2)(0) = 0 + 1 + 0 = 1$
    $c'_{23} = (0)(-1) + (1)(0) + (2)(1) = 0 + 0 + 2 = 2$

    $c'_{31} = (0)(1) + (0)(0) + (1)(0) = 0 + 0 + 0 = 0$
    $c'_{32} = (0)(0) + (0)(1) + (1)(0) = 0 + 0 + 0 = 0$
    $c'_{33} = (0)(-1) + (0)(0) + (1)(1) = 0 + 0 + 1 = 1$

    Le résultat final du produit est :
    $P_{\mathcal{B}' \to \mathcal{B}_c} \cdot M_{\mathcal{B}_c}(L) \cdot P_{\mathcal{B}_c \to \mathcal{B}'} = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Nous comparons ce résultat avec la matrice $M_{\mathcal{B}'}(L)$ que nous avons calculée directement dans la question 4.3 :
    $M_{\mathcal{B}'}(L) = \begin{pmatrix}
    1 & 1 & 0 \\
    0 & 1 & 2 \\
    0 & 0 & 1
    \end{pmatrix}$.

    Les deux matrices sont identiques. La formule de changement de base pour les matrices d'applications linéaires est donc vérifiée pour cet exemple.

---

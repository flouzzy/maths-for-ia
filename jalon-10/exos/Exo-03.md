---
title: "Exercice 3 : Matrices de Passage en Dimension 2"
subtitle: "Jalon 10 - Changements de base, matrices de passage et matrices par blocs"
course: "Mathématiques pour l'Intelligence Artificielle"
level: "L1 à Master"
tags:
  - Algèbre Linéaire
  - Changement de base
  - Matrice de passage
  - Coordonnées
  - Matrices
difficulty: 2/5
---

## Introduction

Soit $E$ un espace vectoriel sur le corps $\mathbb{K} = \mathbb{R}$. Dans cet exercice, nous allons considérer l'espace vectoriel $E = \mathbb{R}^2$.
Nous allons travailler avec deux bases de cet espace vectoriel :
1.  La base canonique $B_c = (e_1, e_2)$, où les vecteurs sont $e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
2.  Une nouvelle base $B = (u_1, u_2)$, où les vecteurs sont $u_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

L'objectif de cet exercice est de construire et d'utiliser les matrices de passage entre ces deux bases, ainsi que de déterminer les coordonnées d'un vecteur dans une base donnée.

## Partie 1 : Construction des Matrices de Passage

### Question 1.1 : Détermination de la matrice de passage de $B_c$ à $B$.

Déterminer la matrice de passage $P_{B_c \to B}$ de la base canonique $B_c$ à la base $B$.
La matrice $P_{B_c \to B}$ est la matrice dont les colonnes sont les coordonnées des vecteurs de la base $B$ exprimés dans la base $B_c$.

**Solution :**

Les vecteurs de la base $B$ sont $u_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
Ces vecteurs sont, par définition, déjà exprimés dans la base canonique $B_c$.
En effet, nous pouvons écrire $u_1$ et $u_2$ comme combinaisons linéaires des vecteurs de la base $B_c$ :
$$ u_1 = 2 \cdot e_1 + 1 \cdot e_2 $$
$$ u_2 = -1 \cdot e_1 + 1 \cdot e_2 $$

Par définition de la matrice de passage $P_{B_c \to B}$, ses colonnes sont les vecteurs de coordonnées des éléments de la nouvelle base $B$ (c'est-à-dire $u_1$ et $u_2$) exprimés dans l'ancienne base $B_c$.

Ainsi, la première colonne de $P_{B_c \to B}$ est le vecteur de coordonnées de $u_1$ dans $B_c$, soit $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
La deuxième colonne de $P_{B_c \to B}$ est le vecteur de coordonnées de $u_2$ dans $B_c$, soit $\begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

La matrice de passage $P_{B_c \to B}$ est donc donnée par :
$$ P_{B_c \to B} = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} $$

### Question 1.2 : Détermination de la matrice de passage de $B$ à $B_c$.

Déterminer la matrice de passage $P_{B \to B_c}$ de la base $B$ à la base canonique $B_c$.
La matrice $P_{B \to B_c}$ est la matrice dont les colonnes sont les coordonnées des vecteurs de la base $B_c$ exprimés dans la base $B$.
Il est également connu que $P_{B \to B_c}$ est l'inverse de $P_{B_c \to B}$.

**Solution :**

Nous allons calculer l'inverse de la matrice $P_{B_c \to B}$ que nous avons déterminée à la Question 1.1.
Soit la matrice $A = P_{B_c \to B} = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$.
Pour une matrice $2 \times 2$ générique $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, son inverse $A^{-1}$ est donnée par la formule :
$$ A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$
où $\det(A) = ad - bc$.

Calculons le déterminant de $A = P_{B_c \to B}$ :
$$ \det(P_{B_c \to B}) = (2)(1) - (-1)(1) $$
$$ \det(P_{B_c \to B}) = 2 - (-1) $$
$$ \det(P_{B_c \to B}) = 2 + 1 $$
$$ \det(P_{B_c \to B}) = 3 $$

Puisque $\det(P_{B_c \to B}) = 3 \neq 0$, la matrice $P_{B_c \to B}$ est inversible.
Appliquons la formule de l'inverse :
$$ P_{B \to B_c} = (P_{B_c \to B})^{-1} = \frac{1}{3} \begin{pmatrix} 1 & -(-1) \\ -1 & 2 \end{pmatrix} $$
$$ P_{B \to B_c} = \frac{1}{3} \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} $$

En distribuant le scalaire $\frac{1}{3}$ à chaque élément de la matrice :
$$ P_{B \to B_c} = \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix} $$

### Question 1.3 : Vérification de l'inversibilité.

Vérifier que $P_{B_c \to B}$ et $P_{B \to B_c}$ sont bien inverses l'une de l'autre en calculant leur produit. Le produit de deux matrices inverses doit être la matrice identité $I_2$.

**Solution :**

Nous devons calculer le produit matriciel $P_{B_c \to B} \cdot P_{B \to B_c}$ et vérifier qu'il est égal à la matrice identité $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
$$ P_{B_c \to B} \cdot P_{B \to B_c} = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix} $$
Nous pouvons factoriser le scalaire $\frac{1}{3}$ de la deuxième matrice pour simplifier le calcul :
$$ P_{B_c \to B} \cdot P_{B \to B_c} = \frac{1}{3} \left( \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} \right) $$

Effectuons la multiplication des deux matrices $2 \times 2$ :
$$ \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} (2)(1) + (-1)(-1) & (2)(1) + (-1)(2) \\ (1)(1) + (1)(-1) & (1)(1) + (1)(2) \end{pmatrix} $$
$$ = \begin{pmatrix} 2 + 1 & 2 - 2 \\ 1 - 1 & 1 + 2 \end{pmatrix} $$
$$ = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} $$

Maintenant, multiplions ce résultat par le scalaire $\frac{1}{3}$ :
$$ P_{B_c \to B} \cdot P_{B \to B_c} = \frac{1}{3} \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} $$
$$ = \begin{pmatrix} \frac{1}{3} \cdot 3 & \frac{1}{3} \cdot 0 \\ \frac{1}{3} \cdot 0 & \frac{1}{3} \cdot 3 \end{pmatrix} $$
$$ = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $$

Le résultat est bien la matrice identité $I_2$.
Ceci confirme que $P_{B_c \to B}$ et $P_{B \to B_c}$ sont inverses l'une de l'autre, comme attendu.

## Partie 2 : Changement de Coordonnées

### Question 2.1 : Calcul des coordonnées d'un vecteur dans la base $B$.

Soit un vecteur $v \in \mathbb{R}^2$ dont les coordonnées dans la base canonique $B_c$ sont $[v]_{B_c} = \begin{pmatrix} 5 \\ 0 \end{pmatrix}$.
Calculer les coordonnées de $v$ dans la base $B$, notées $[v]_B$, en utilisant la matrice de passage appropriée.

**Solution :**

La relation entre les coordonnées d'un vecteur $v$ dans deux bases $B_c$ et $B$ est donnée par la formule :
$$ [v]_B = P_{B \to B_c} \cdot [v]_{B_c} $$
où $P_{B \to B_c}$ est la matrice de passage de la base $B$ à la base $B_c$.

Nous avons déterminé $P_{B \to B_c} = \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix}$ à la Question 1.2.
Les coordonnées du vecteur $v$ dans la base canonique $B_c$ sont $[v]_{B_c} = \begin{pmatrix} 5 \\ 0 \end{pmatrix}$.

Effectuons la multiplication matricielle :
$$ [v]_B = \begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix} \begin{pmatrix} 5 \\ 0 \end{pmatrix} $$
$$ [v]_B = \begin{pmatrix} (1/3)(5) + (1/3)(0) \\ (-1/3)(5) + (2/3)(0) \end{pmatrix} $$
$$ [v]_B = \begin{pmatrix} 5/3 + 0 \\ -5/3 + 0 \end{pmatrix} $$
$$ [v]_B = \begin{pmatrix} 5/3 \\ -5/3 \end{pmatrix} $$

Les coordonnées du vecteur $v$ dans la base $B$ sont donc $[v]_B = \begin{pmatrix} 5/3 \\ -5/3 \end{pmatrix}$.

### Question 2.2 : Vérification par calcul direct.

Vérifier le résultat de la Question 2.1 en exprimant directement le vecteur $v$ comme une combinaison linéaire des vecteurs de la base $B$.

**Solution :**

Nous cherchons des scalaires $\alpha, \beta \in \mathbb{R}$ tels que le vecteur $v$ puisse s'écrire $v = \alpha u_1 + \beta u_2$.
Les coordonnées de $v$ dans la base canonique sont $\begin{pmatrix} 5 \\ 0 \end{pmatrix}$.
Les vecteurs de la base $B$ sont $u_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ et $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

L'équation vectorielle $v = \alpha u_1 + \beta u_2$ se traduit par le système d'équations linéaires suivant, en utilisant les coordonnées dans la base canonique :
$$ \begin{pmatrix} 5 \\ 0 \end{pmatrix} = \alpha \begin{pmatrix} 2 \\ 1 \end{pmatrix} + \beta \begin{pmatrix} -1 \\ 1 \end{pmatrix} $$
$$ \begin{pmatrix} 5 \\ 0 \end{pmatrix} = \begin{pmatrix} 2\alpha \\ \alpha \end{pmatrix} + \begin{pmatrix} -\beta \\ \beta \end{pmatrix} $$
$$ \begin{pmatrix} 5 \\ 0 \end{pmatrix} = \begin{pmatrix} 2\alpha - \beta \\ \alpha + \beta \end{pmatrix} $$

Ceci nous conduit au système de deux équations à deux inconnues $\alpha$ et $\beta$ :
1.  $2\alpha - \beta = 5$
2.  $\alpha + \beta = 0$

De l'équation (2), nous pouvons facilement exprimer $\beta$ en fonction de $\alpha$ :
$$ \beta = -\alpha $$

Substituons cette expression de $\beta$ dans l'équation (1) :
$$ 2\alpha - (-\alpha) = 5 $$
$$ 2\alpha + \alpha = 5 $$
$$ 3\alpha = 5 $$
$$ \alpha = \frac{5}{3} $$

Maintenant, substituons la valeur de $\alpha$ dans l'expression de $\beta$ :
$$ \beta = -\left(\frac{5}{3}\right) $$
$$ \beta = -\frac{5}{3} $$

Ainsi, les scalaires sont $\alpha = 5/3$ et $\beta = -5/3$.
Les coordonnées de $v$ dans la base $B$ sont donc $[v]_B = \begin{pmatrix} 5/3 \\ -5/3 \end{pmatrix}$.

Ce résultat est identique à celui obtenu à la Question 2.1 en utilisant la matrice de passage, ce qui confirme l'exactitude de nos calculs et la cohérence des deux méthodes.

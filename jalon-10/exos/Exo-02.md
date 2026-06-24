```yaml
title: "Exercice 2 : Calcul de matrices de passage et coordonnées"
subtitle: "Jalon 10 - Changements de base, matrices de passage et matrices par blocs"
date: "2023-10-27"
authors:
  - "Votre Nom"
keywords:
  - "algèbre linéaire"
  - "changement de base"
  - "matrice de passage"
  - "coordonnées de vecteur"
  - "espace vectoriel"
level: "1/5 (Facile)"
jalon: "10"
exercice: "02"
```

---

# Exercice 2 : Calcul de matrices de passage et coordonnées

## Introduction

Cet exercice vise à consolider la compréhension des concepts de bases d'un espace vectoriel, de matrices de passage et de la manière de déterminer les coordonnées d'un vecteur dans une nouvelle base. Nous travaillerons dans un espace vectoriel de dimension finie sur le corps des nombres réels.

## Prérequis

*   Définition d'un espace vectoriel et d'une base.
*   Opérations sur les matrices (addition, multiplication, inversion).
*   Définition des coordonnées d'un vecteur dans une base donnée.

## Énoncé de l'exercice

Soit $\mathbb{K}$ le corps des nombres réels, noté $\mathbb{R}$.
Soit $E$ l'espace vectoriel $\mathbb{R}^2$ sur le corps $\mathbb{R}$.

Nous considérons deux bases de $E$:

1.  La base canonique $\mathcal{B}_0 = (e_1, e_2)$, où les vecteurs sont définis par :
    $$ e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}_{\mathcal{B}_0} \quad \text{et} \quad e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}_{\mathcal{B}_0} $$
    (Les indices $\mathcal{B}_0$ indiquent que ces vecteurs sont exprimés dans la base $\mathcal{B}_0$ elle-même, ce qui est la convention pour les vecteurs de la base canonique).

2.  Une nouvelle base $\mathcal{B} = (u_1, u_2)$, où les vecteurs sont définis par leurs coordonnées dans la base canonique $\mathcal{B}_0$:
    $$ u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}_{\mathcal{B}_0} \quad \text{et} \quad u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}_{\mathcal{B}_0} $$

### Question 1 : Détermination de la matrice de passage de $\mathcal{B}$ à $\mathcal{B}_0$

Déterminer la matrice de passage $P_{\mathcal{B}_0 \leftarrow \mathcal{B}}$ de la base $\mathcal{B}$ à la base $\mathcal{B}_0$.

### Question 2 : Détermination de la matrice de passage de $\mathcal{B}_0$ à $\mathcal{B}$

Déterminer la matrice de passage $P_{\mathcal{B} \leftarrow \mathcal{B}_0}$ de la base $\mathcal{B}_0$ à la base $\mathcal{B}$.

### Question 3 : Calcul des coordonnées d'un vecteur dans la nouvelle base

Soit un vecteur $v \in E$ dont les coordonnées dans la base canonique $\mathcal{B}_0$ sont données par :
$$ [v]_{\mathcal{B}_0} = \begin{pmatrix} 3 \\ 2 \end{pmatrix} $$
Déterminer les coordonnées de ce vecteur $v$ dans la base $\mathcal{B}$, notées $[v]_{\mathcal{B}}$.

## Solution détaillée

### Question 1 : Détermination de la matrice de passage de $\mathcal{B}$ à $\mathcal{B}_0$

La matrice de passage $P_{\mathcal{B}_0 \leftarrow \mathcal{B}}$ est la matrice dont les colonnes sont les coordonnées des vecteurs de la base $\mathcal{B}$ exprimés dans la base $\mathcal{B}_0$.

Les vecteurs de la base $\mathcal{B}$ sont donnés par :
$$ u_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}_{\mathcal{B}_0} \quad \text{et} \quad u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}_{\mathcal{B}_0} $$

Par définition, la première colonne de $P_{\mathcal{B}_0 \leftarrow \mathcal{B}}$ est $[u_1]_{\mathcal{B}_0}$ et la deuxième colonne est $[u_2]_{\mathcal{B}_0}$.

Ainsi, la matrice de passage $P_{\mathcal{B}_0 \leftarrow \mathcal{B}}$ est :
$$ P_{\mathcal{B}_0 \leftarrow \mathcal{B}} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} $$

### Question 2 : Détermination de la matrice de passage de $\mathcal{B}_0$ à $\mathcal{B}$

La matrice de passage $P_{\mathcal{B} \leftarrow \mathcal{B}_0}$ est l'inverse de la matrice $P_{\mathcal{B}_0 \leftarrow \mathcal{B}}$.
Nous devons donc calculer $(P_{\mathcal{B}_0 \leftarrow \mathcal{B}})^{-1}$.

Soit $A = P_{\mathcal{B}_0 \leftarrow \mathcal{B}} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$.

Le déterminant de $A$ est $\det(A) = ad - bc$.
$$ \det(A) = (1)(1) - (-1)(1) $$
$$ \det(A) = 1 - (-1) $$
$$ \det(A) = 1 + 1 $$
$$ \det(A) = 2 $$

Puisque $\det(A) \neq 0$, la matrice $A$ est inversible.

L'inverse d'une matrice $2 \times 2$ est donnée par la formule :
$$ A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$

En substituant les valeurs de $a, b, c, d$ et $\det(A)$ :
$$ P_{\mathcal{B} \leftarrow \mathcal{B}_0} = \frac{1}{2} \begin{pmatrix} 1 & -(-1) \\ -1 & 1 \end{pmatrix} $$
$$ P_{\mathcal{B} \leftarrow \mathcal{B}_0} = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} $$

Nous pouvons distribuer le facteur $\frac{1}{2}$ à chaque élément de la matrice :
$$ P_{\mathcal{B} \leftarrow \mathcal{B}_0} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{pmatrix} $$

### Question 3 : Calcul des coordonnées d'un vecteur dans la nouvelle base

Nous avons le vecteur $v$ dont les coordonnées dans la base canonique $\mathcal{B}_0$ sont :
$$ [v]_{\mathcal{B}_0} = \begin{pmatrix} 3 \\ 2 \end{pmatrix} $$

Pour trouver les coordonnées de $v$ dans la base $\mathcal{B}$, nous utilisons la relation fondamentale de changement de base :
$$ [v]_{\mathcal{B}} = P_{\mathcal{B} \leftarrow \mathcal{B}_0} [v]_{\mathcal{B}_0} $$

Nous avons calculé $P_{\mathcal{B} \leftarrow \mathcal{B}_0}$ à la question précédente :
$$ P_{\mathcal{B} \leftarrow \mathcal{B}_0} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{pmatrix} $$

Effectuons la multiplication matricielle :
$$ [v]_{\mathcal{B}} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} $$

Calcul de la première composante de $[v]_{\mathcal{B}}$ :
$$ \left( \frac{1}{2} \right) \cdot 3 + \left( \frac{1}{2} \right) \cdot 2 $$
$$ = \frac{3}{2} + \frac{2}{2} $$
$$ = \frac{5}{2} $$

Calcul de la deuxième composante de $[v]_{\mathcal{B}}$ :
$$ \left( -\frac{1}{2} \right) \cdot 3 + \left( \frac{1}{2} \right) \cdot 2 $$
$$ = -\frac{3}{2} + \frac{2}{2} $$
$$ = -\frac{1}{2} $$

Donc, les coordonnées du vecteur $v$ dans la base $\mathcal{B}$ sont :
$$ [v]_{\mathcal{B}} = \begin{pmatrix} \frac{5}{2} \\ -\frac{1}{2} \end{pmatrix} $$

---

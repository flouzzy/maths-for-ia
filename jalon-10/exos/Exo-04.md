```yaml
title: "Exercice 04"
subtitle: "Changements de base et matrices de passage"
course: "Mathématiques pour l'Intelligence Artificielle"
level: "L1 à Master"
jalon: "Jalon 10"
topics: ["Changements de base", "Matrices de passage", "Coordonnées d'un vecteur", "Inversion de matrice 2x2"]
difficulty: "2/5"
date: "2023-10-27"
author: "Équipe Pédagogique"
```

# Exercice 04 : Changements de base dans $\mathbb{R}^2$

Cet exercice vise à consolider la compréhension des concepts de bases, de matrices de passage et de calcul de coordonnées de vecteurs dans différentes bases.

---

## Contexte et Définitions Préliminaires

Soit $E$ un espace vectoriel sur le corps $\mathbb{K} = \mathbb{R}$. Dans cet exercice, nous considérons spécifiquement l'espace vectoriel $E = \mathbb{R}^2$.

Nous définissons la base canonique de $\mathbb{R}^2$, notée $\mathcal{B}_c$, comme l'ensemble ordonné de vecteurs :
$$ \mathcal{B}_c = (e_1, e_2) $$
où $e_1 \in \mathbb{R}^2$ est le vecteur colonne $e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $e_2 \in \mathbb{R}^2$ est le vecteur colonne $e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

Nous introduisons une nouvelle famille de vecteurs de $\mathbb{R}^2$, notée $\mathcal{B}'$, définie par :
$$ \mathcal{B}' = (u_1, u_2) $$
où $u_1 \in \mathbb{R}^2$ est le vecteur colonne $u_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ et $u_2 \in \mathbb{R}^2$ est le vecteur colonne $u_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

---

## Questions

1.  **Vérification de la nature de $\mathcal{B}'$ :**
    Démontrer rigoureusement que la famille de vecteurs $\mathcal{B}' = (u_1, u_2)$ constitue bien une base de l'espace vectoriel $E = \mathbb{R}^2$.
    Pour ce faire, vous pouvez vérifier la liberté de la famille.

2.  **Détermination de la matrice de passage de $\mathcal{B}_c$ à $\mathcal{B}'$ :**
    Déterminer la matrice de passage $P_{\mathcal{B}_c \to \mathcal{B}'}$ (parfois notée $P_{\mathcal{B}', \mathcal{B}_c}$ dans certaines conventions), qui permet de passer des coordonnées exprimées dans la base $\mathcal{B}'$ aux coordonnées exprimées dans la base $\mathcal{B}_c$.
    Cette matrice est construite en plaçant les vecteurs de la nouvelle base $\mathcal{B}'$ (exprimés dans l'ancienne base $\mathcal{B}_c$) en colonnes.

3.  **Détermination de la matrice de passage de $\mathcal{B}'$ à $\mathcal{B}_c$ :**
    Déterminer la matrice de passage $P_{\mathcal{B}' \to \mathcal{B}_c}$ (parfois notée $P_{\mathcal{B}_c, \mathcal{B}'}$ dans certaines conventions), qui permet de passer des coordonnées exprimées dans la base $\mathcal{B}_c$ aux coordonnées exprimées dans la base $\mathcal{B}'$.
    Expliquer la relation entre $P_{\mathcal{B}' \to \mathcal{B}_c}$ et $P_{\mathcal{B}_c \to \mathcal{B}'}$.
    Pour calculer $P_{\mathcal{B}' \to \mathcal{B}_c}$, vous devrez calculer l'inverse d'une matrice $2 \times 2$. Rappelons que pour une matrice $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, son inverse est $A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, à condition que $\det(A) \neq 0$.

4.  **Calcul des coordonnées d'un vecteur dans la nouvelle base :**
    Soit un vecteur $v \in \mathbb{R}^2$ dont les coordonnées dans la base canonique $\mathcal{B}_c$ sont $[v]_{\mathcal{B}_c} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
    Calculer les coordonnées de $v$ dans la base $\mathcal{B}'$, notées $[v]_{\mathcal{B}'}$, en utilisant la matrice de passage appropriée déterminée précédemment.
    Expliciter toutes les étapes du calcul matriciel.

5.  **Vérification du résultat :**
    Vérifier le résultat obtenu à la question 4. Pour ce faire, exprimez le vecteur $v$ comme une combinaison linéaire des vecteurs de la base $\mathcal{B}'$ en utilisant les coordonnées $[v]_{\mathcal{B}'}$ que vous avez calculées, et montrez que cela correspond bien au vecteur $v$ dont les coordonnées dans $\mathcal{B}_c$ sont $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
    Expliciter toutes les étapes du calcul vectoriel.

---

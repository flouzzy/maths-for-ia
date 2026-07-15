---
title: "Exercice 7 : Matrice de Gram et Indépendance Linéaire"
difficulty: "★★★★☆"
---
# Exercice 7 : Matrice de Gram et Indépendance Linéaire

## Énoncé
Soit $E$ un espace euclidien et $x_1, \dots, x_k$ une famille de $k$ vecteurs de $E$.
On définit la matrice de Gram $G \in \mathcal{M}_k(\mathbb{R})$ par $G_{i,j} = \langle x_i, x_j \rangle$.
1. Démontrer que la matrice de Gram $G$ est symétrique positive (ses valeurs propres sont $\geq 0$).
2. Démontrer le théorème fondamental : La famille $(x_1, \dots, x_k)$ est libre (linéairement indépendante) si et seulement si la matrice de Gram $G$ est inversible (auquel cas elle est définie positive).

## Correction Zéro Ellipse
**1. Symétrie et positivité de $G$**
- *Symétrie :* Par définition du produit scalaire euclidien (symétrique), $G_{j,i} = \langle x_j, x_i \rangle = \langle x_i, x_j \rangle = G_{i,j}$. Donc $G = G^T$, la matrice est symétrique.
- *Positivité :* Soit $U = \begin{pmatrix} u_1 \\ \vdots \\ u_k \end{pmatrix} \in \mathbb{R}^k$. Évaluons la forme quadratique $U^T G U$.
Par définition du produit matriciel :
$U^T G U = \sum_{i=1}^k \sum_{j=1}^k u_i G_{i,j} u_j = \sum_{i=1}^k \sum_{j=1}^k u_i \langle x_i, x_j \rangle u_j$.
Par bilinéarité du produit scalaire, on peut faire entrer les sommes à l'intérieur :
$U^T G U = \left\langle \sum_{i=1}^k u_i x_i, \sum_{j=1}^k u_j x_j \right\rangle$.
Posons $v = \sum_{i=1}^k u_i x_i$. Le vecteur $v$ est un élément de l'espace euclidien $E$.
L'expression devient : $U^T G U = \langle v, v \rangle = \|v\|^2$.
La norme euclidienne étant toujours positive ou nulle, $U^T G U \geq 0$ pour tout vecteur $U \in \mathbb{R}^k$.
La matrice $G$ est donc symétrique positive ($S_k^+(\mathbb{R})$).

**2. Indépendance linéaire et inversibilité**
Nous allons étudier le noyau de $G$.
Soit $U \in \mathbb{R}^k$.
$U \in \text{Ker}(G) \iff G U = 0 \implies U^T G U = 0$.
D'après le calcul précédent, $U^T G U = \|v\|^2$ où $v = \sum_{i=1}^k u_i x_i$.
Donc $\|v\|^2 = 0$, ce qui implique $v = 0_E$.
Ainsi, $\sum_{i=1}^k u_i x_i = 0_E$.

**Sens direct ($\implies$) : Famille libre $\implies G$ inversible**
Supposons la famille $(x_1, \dots, x_k)$ libre.
Soit $U \in \text{Ker}(G)$. D'après ce qui précède, $\sum_{i=1}^k u_i x_i = 0_E$.
Puisque la famille est libre, la seule combinaison linéaire nulle est celle dont tous les coefficients sont nuls.
Donc $u_1 = u_2 = \dots = u_k = 0$.
Ainsi, le vecteur $U$ est le vecteur nul de $\mathbb{R}^k$.
Le noyau de $G$ est réduit à $\{0\}$, ce qui prouve que la matrice carrée $G$ est inversible (et de plus définie positive car $U^T G U > 0$ pour $U \neq 0$).

**Sens réciproque ($\impliedby$) : $G$ inversible $\implies$ Famille libre**
Supposons que $G$ soit inversible. Son noyau est donc réduit à $\{0\}$.
Soit une combinaison linéaire nulle des vecteurs de la famille : $\sum_{i=1}^k u_i x_i = 0_E$.
Soit $U$ le vecteur colonne de $\mathbb{R}^k$ contenant les composantes $u_i$.
Pour tout indice $j \in \{1, \dots, k\}$, prenons le produit scalaire de l'équation avec $x_j$ :
$\left\langle \sum_{i=1}^k u_i x_i, x_j \right\rangle = \langle 0_E, x_j \rangle = 0$.
Par linéarité à gauche :
$\sum_{i=1}^k u_i \langle x_i, x_j \rangle = 0$.
Ce qui s'écrit formellement avec la matrice de Gram : $\sum_{i=1}^k G_{j,i} u_i = 0$.
Cette équation, vraie pour chaque ligne $j$, équivaut matriciellement à $G U = 0$.
Donc $U \in \text{Ker}(G)$.
Puisque $G$ est inversible, $\text{Ker}(G) = \{0\}$, donc $U = 0$.
Tous les coefficients $u_i$ sont nuls. La famille est donc libre.
L'équivalence est parfaitement démontrée.

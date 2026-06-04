---
uuid: "jalon-105"
title: "Opérateurs adjoints"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 104 (Bases hilbertiennes).md]]"
next: "[[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]]"
---

# Jalon 105 : Opérateurs adjoints

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une machine à transformer les sons (un opérateur $T$). Elle prend une note pure et la déforme.
    - Vous avez aussi un micro qui mesure la ressemblance entre deux sons (le produit scalaire $\langle \cdot, \cdot \rangle$).
    - L'**Opérateur Adjoint ($T^*$)**, c'est la "machine miroir" : c'est l'unique transformation qui, si on l'applique au son que le micro écoute ($y$), donne le même résultat de ressemblance que si on avait appliqué la machine originale au son qui chante ($x$).
    - On dit que $\langle \text{Machine}(x), y \rangle = \langle x, \text{Miroir}(y) \rangle$.
    - Si la machine et son miroir sont identiques ($T = T^*$), on dit que l'opérateur est **Auto-adjoint** (ou symétrique). C'est le cas des forces physiques naturelles et des mesures de similarité en IA.
- **Le "Pourquoi on a inventé ça" :** En dimension finie, c'est simplement la matrice transposée $A^T$. En dimension infinie, on ne peut pas toujours écrire de matrices. L'adjoint est la généralisation universelle de la symétrie. Il permet de "faire passer" un opérateur d'un côté à l'autre d'un calcul, ce qui est crucial pour résoudre des équations.
- **Visualisation :** Un reflet. Si $T$ fait une rotation vers la droite, $T^*$ fait la même rotation vers la gauche pour compenser et garder l'alignement.

## 2. Formalisation & Rigueur Académique

Soit $H$ un espace de Hilbert.

### A. Définition de l'Adjoint

> **Théorème et Définition :**
> Soit $T \in \mathcal{L}(H)$ un opérateur linéaire continu. Il existe un unique opérateur $T^* \in \mathcal{L}(H)$, appelé **adjoint de T**, vérifiant :
> $$\forall x, y \in H, \quad \langle Tx, y \rangle = \langle x, T^*y \rangle$$

### B. Propriétés Algébriques

> **Théorème :**
> 1. $(T^*)^* = T$.
> 2. $(\alpha T + \beta S)^* = \bar{\alpha} T^* + \bar{\beta} S^*$.
> 3. $(ST)^* = S^* T^*$.
> 4. $\|T^*\| = \|T\|$ et $\|T^* T\| = \|T\|^2$ (Propriété de $\mathcal{C}^*$-algèbre).

### C. Types d'Opérateurs spéciaux

1. **Auto-adjoint :** $T^* = T$. (Analogue des matrices symétriques réelles).
2. **Unitaire :** $T^* = T^{-1}$. (Conserve le produit scalaire, analogue des rotations).
3. **Normal :** $T^* T = T T^*$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Existence de l'adjoint (via Riesz)

1. **Fixons y :** Soit $y \in H$. Considérons l'application $L_y : x \mapsto \langle Tx, y \rangle$.
2. **Linéarité :** $L_y(ax+bz) = \langle T(ax+bz), y \rangle = a \langle Tx, y \rangle + b \langle Tz, y \rangle$ par linéarité de $T$ et du produit scalaire.
3. **Continuité :** $|L_y(x)| = |\langle Tx, y \rangle| \le \|Tx\| \cdot \|y\| \le (\|T\| \cdot \|y\|) \cdot \|x\|$ par Cauchy-Schwarz.
   Donc $L_y$ est une forme linéaire continue sur $H$.
4. **Application de Riesz :** D'après le **Théorème de Représentation de Riesz** (Jalon 103), il existe un unique vecteur $z_y \in H$ tel que :
   $$\forall x \in H, \quad L_y(x) = \langle x, z_y \rangle$$
5. **Construction de l'opérateur :** On définit l'application $T^*$ par $T^*(y) = z_y$.
6. **Linéarité de T* :** On vérifie facilement que $y \mapsto z_y$ est linéaire.
7. **Unicité :** Découle de l'unicité du vecteur dans le théorème de Riesz.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : L'opérateur de décalage (Shift)
**Énoncé :** Sur $\ell^2(\mathbb{N})$, on définit $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$. Calculer $S^*$.
**Correction Détaillée :**
1. $\langle Sx, y \rangle = \sum_{n=0}^\infty (Sx)_n \bar{y}_n = 0\bar{y}_0 + x_0 \bar{y}_1 + x_1 \bar{y}_2 + \dots$
2. On veut que ce soit égal à $\sum x_n (\overline{S^*y})_n$.
3. Par identification : $(S^*y)_0 = y_1, (S^*y)_1 = y_2, \dots$
4. **Résultat :** $S^*(y_0, y_1, \dots) = (y_1, y_2, \dots)$.
L'adjoint du décalage à droite est le décalage à gauche.

### Exercice 2 : Niveau Avancé (Adjoint et Noyau)
**Énoncé :** Montrer que $\ker(T^*) = (\text{im } T)^\perp$.
**Correction Détaillée :**
$y \in \ker(T^*) \iff T^*y = 0 \iff \forall x, \langle x, T^*y \rangle = 0 \iff \forall x, \langle Tx, y \rangle = 0$.
Cela signifie que $y$ est orthogonal à tous les vecteurs de l'image de $T$.
**Conséquence :** C'est la base de la résolution des moindres carrés : l'erreur minimale est orthogonale à l'espace des prédictions.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Dans un réseau de neurones, la **Rétropropagation** est l'application successive des adjoints des opérateurs linéaires de chaque couche.
- **Example Concret :**
    - **Backprop :** Si une couche fait $y = Wx$, alors pour remonter l'erreur, on calcule $\nabla_x \mathcal{L} = W^T \nabla_y \mathcal{L}$. Ici $W^T$ est exactement l'adjoint de l'opérateur $W$.
    - **Algorithmes de descente de gradient :** Pour minimiser $\|Ax - b\|^2$, le gradient fait apparaître $A^T(Ax-b)$. L'adjoint $A^T$ "ramène" l'erreur du monde des sorties vers le monde des paramètres.
    - **Auto-encodeurs :** Un auto-encodeur linéaire parfait cherche une matrice $W$ telle que $W^T W = I$. Cela signifie que l'encodeur est l'adjoint du décodeur, formant une paire unitaire qui préserve toute l'information.
    - **Attention Mechanism :** Dans les Transformers, le calcul des scores d'attention $QK^T$ utilise la transposée (l'adjoint) de la matrice des Keys pour mesurer la similarité avec les Queries.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 9 (Calcul matriciel).md]]
- **Concepts Futurs dépendants :** [[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]], [[Jalon 125 (Opérateurs proximaux).md]]

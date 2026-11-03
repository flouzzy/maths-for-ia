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

 Imaginez que vous ayez une machine à transformer les sons (un opérateur $T$). Elle prend une note pure et la déforme.
    - Vous avez aussi un micro qui mesure la ressemblance entre deux sons (le produit scalaire $\langle \cdot, \cdot \rangle$).
    - L'**Opérateur Adjoint ($T^*$)**, c'est la "machine miroir" : c'est l'unique transformation qui, si on l'applique au son que le micro écoute ($y$), donne le même résultat de ressemblance que si on avait appliqué la machine originale au son qui chante ($x$).
    - On dit que $\langle \text{Machine}(x), y \rangle = \langle x, \text{Miroir}(y) \rangle$.
    - Si la machine et son miroir sont identiques ($T = T^*$), on dit que l'opérateur est **Auto-adjoint** (ou symétrique). C'est le cas des forces physiques naturelles et des mesures de similarité en IA.
 En dimension finie, c'est simplement la matrice transposée $A^T$. En dimension infinie, on ne peut pas toujours écrire de matrices. L'adjoint est la généralisation universelle de la symétrie. Il permet de "faire passer" un opérateur d'un côté à l'autre d'un calcul, ce qui est crucial pour résoudre des équations.
 Un reflet. Si $T$ fait une rotation vers la droite, $T^*$ fait la même rotation vers la gauche pour compenser et garder l'alignement.

## 2. Formalisation

Soit $H$ un espace de Hilbert.

### A. Définition de l'Adjoint

> **Théorème et Définition :**
> Soit $T \in \mathcal{L}(H)$ un opérateur linéaire continu. Il existe un unique opérateur $T^* \in \mathcal{L}(H)$, appelé **adjoint de T**, vérifiant :
> $$\forall x, y \in H, \quad \langle Tx, y \rangle = \langle x, T^*y \rangle$$


**Exemple Concret (Dimension finie) :**
Soit $H = \mathbb{R}^3$ muni du produit scalaire usuel et $T : \mathbb{R}^3 \to \mathbb{R}^3$ un endomorphisme dont la matrice dans la base canonique est :
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$
L'adjoint $T^*$ correspond simplement à la transposée de la matrice $A$ dans cette base orthonormée, c'est-à-dire :
$$A^T = \begin{pmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix}$$
Ainsi, pour $x = (x_1, x_2, x_3)$ et $y = (y_1, y_2, y_3)$, on a bien $\langle Tx, y \rangle = \langle x, T^*y \rangle$.


\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Espaces H
  \draw[thick] (0,0) ellipse (1.5 and 2);
  \node at (0, 2.3) {$H$};
  \draw[thick] (5,0) ellipse (1.5 and 2);
  \node at (5, 2.3) {$H$};

  % Points
  \fill (0, 1) circle (2pt) node[left] {$x$};
  \fill (5, 1) circle (2pt) node[right] {$Tx$};

  \fill (5, -1) circle (2pt) node[right] {$y$};
  \fill (0, -1) circle (2pt) node[left] {$T^*y$};

  % Flèches T et T*
  \draw[->, thick, blue] (0.2, 1) to[bend left=20] node[above] {$T$} (4.8, 1);
  \draw[->, thick, red] (4.8, -1) to[bend left=20] node[below] {$T^*$} (0.2, -1);

  % Produit scalaire
  \node at (2.5, 0) {$\langle Tx, y \rangle = \langle x, T^*y \rangle$};
\end{tikzpicture}
\end{center}


### B. Propriétés Algébriques

> **Théorème :**
> 1. $(T^*)^* = T$.
> 2. $(\alpha T + \beta S)^* = \bar{\alpha} T^* + \bar{\beta} S^*$.
> 3. $(ST)^* = S^* T^*$.


**Exemple Concret (L'opérateur de dérivation) :**
Soit $H = L^2([0, 1], \mathbb{C})$ et $T = \frac{d}{dt}$ défini sur un domaine dense de fonctions nulles au bord (pour éviter les termes de bord lors de l'intégration par parties).
$$\langle Tf, g \rangle = \int_0^1 f'(t) \overline{g(t)} dt$$
Par intégration par parties :
$$\int_0^1 f'(t) \overline{g(t)} dt = [f(t)\overline{g(t)}]_0^1 - \int_0^1 f(t) \overline{g'(t)} dt = - \int_0^1 f(t) \overline{g'(t)} dt = \langle f, -g' \rangle$$
L'adjoint de la dérivée $T = \frac{d}{dt}$ est donc $T^* = -\frac{d}{dt}$. C'est un opérateur **anti-symétrique** ($T^* = -T$).

> 4. $\|T^*\| = \|T\|$ et $\|T^* T\| = \|T\|^2$ (Propriété de $\mathcal{C}^*$-algèbre).

### C. Types d'Opérateurs spéciaux

1. **Auto-adjoint :** $T^* = T$. (Analogue des matrices symétriques réelles).


**Exemple Concret (Opérateur de multiplication) :**
Soit $H = L^2(\mathbb{R}, \mathbb{C})$ et $T$ l'opérateur de multiplication par une fonction $m(t)$ bornée : $(Tf)(t) = m(t)f(t)$.
$$\langle Tf, g \rangle = \int_\mathbb{R} (m(t)f(t)) \overline{g(t)} dt = \int_\mathbb{R} f(t) \overline{(\overline{m(t)}g(t))} dt = \langle f, \overline{m}g \rangle$$
Donc l'adjoint est l'opérateur de multiplication par la fonction conjuguée : $(T^*f)(t) = \overline{m(t)}f(t)$.
Si $m$ est à valeurs réelles, alors $T^* = T$ et l'opérateur est **auto-adjoint**.

2. **Unitaire :** $T^* = T^{-1}$. (Conserve le produit scalaire, analogue des rotations).


**Exemple Concret (L'opérateur unitaire de Fourier) :**
Sur $L^2(\mathbb{R})$, la transformée de Fourier $\mathcal{F}$ vérifie la formule de Plancherel : $\langle \mathcal{F}f, \mathcal{F}g \rangle = \langle f, g \rangle$.
Cela se réécrit $\langle f, \mathcal{F}^* \mathcal{F} g \rangle = \langle f, g \rangle$ pour tout $f, g$.
Ainsi $\mathcal{F}^* \mathcal{F} = I$. Comme la transformée de Fourier est inversible, $\mathcal{F}^* = \mathcal{F}^{-1}$. L'opérateur de Fourier est unitaire.

3. **Normal :** $T^* T = T T^*$.


**Exemple Concret (Projection Orthogonale) :**
Soit $M$ un sous-espace fermé de $H$, et $P_M$ le projecteur orthogonal sur $M$. Tout $x \in H$ s'écrit $x = x_M + x_{M^\perp}$.
Pour $x, y \in H$, calculons $\langle P_M x, y \rangle$ :
$$\langle P_M x, y \rangle = \langle x_M, y_M + y_{M^\perp} \rangle = \langle x_M, y_M \rangle + \langle x_M, y_{M^\perp} \rangle = \langle x_M, y_M \rangle + 0$$
D'autre part :
$$\langle x, P_M y \rangle = \langle x_M + x_{M^\perp}, y_M \rangle = \langle x_M, y_M \rangle + 0$$
Donc $\langle P_M x, y \rangle = \langle x, P_M y \rangle$. Tout projecteur orthogonal est auto-adjoint ($P_M = P_M^*$).


\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Espace M
  \draw[thick, fill=blue!10] (-2, -0.5) -- (2, -0.5) -- (3, 1) -- (-1, 1) -- cycle;
  \node at (2.5, 0.5) {$M$};

  % Vecteur x
  \coordinate (O) at (0,0);
  \coordinate (X) at (1, 1.5);
  \coordinate (PX) at (1, 0.25); % Projection grossière

  \draw[->, thick, red] (O) -- (X) node[above] {$x$};
  \draw[->, thick, blue] (O) -- (PX) node[below] {$P_M x$};
  \draw[dashed] (X) -- (PX);

  % Orthogonalité
  \draw (1, 0.45) -- (0.8, 0.45) -- (0.8, 0.25);
  \node at (-1.5, 1.5) {$P_M = P_M^*$};
\end{tikzpicture}
\end{center}


## 3. Démonstrations

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

## 4. Exercices d'Application

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

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Dans un réseau de neurones, la **Rétropropagation** est l'application successive des adjoints des opérateurs linéaires de chaque couche.
- **Example Concret :**
    - **Backprop :** Si une couche fait $y = Wx$, alors pour remonter l'erreur, on calcule $\nabla_x \mathcal{L} = W^T \nabla_y \mathcal{L}$. Ici $W^T$ est exactement l'adjoint de l'opérateur $W$.
    - **Algorithmes de descente de gradient :** Pour minimiser $\|Ax - b\|^2$, le gradient fait apparaître $A^T(Ax-b)$. L'adjoint $A^T$ "ramène" l'erreur du monde des sorties vers le monde des paramètres.
    - **Auto-encodeurs :** Un auto-encodeur linéaire parfait cherche une matrice $W$ telle que $W^T W = I$. Cela signifie que l'encodeur est l'adjoint du décodeur, formant une paire unitaire qui préserve toute l'information.
    - **Attention Mechanism :** Dans les Transformers, le calcul des scores d'attention $QK^T$ utilise la transposée (l'adjoint) de la matrice des Keys pour mesurer la similarité avec les Queries.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 9 (Calcul matriciel).md]]
- **Concepts Futurs dépendants :** [[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]], [[Jalon 125 (Opérateurs proximaux).md]]

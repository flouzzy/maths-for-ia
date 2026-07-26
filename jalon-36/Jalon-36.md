---
uuid: "jalon-36"
title: "Livrable IA T3 : Décomposition en valeurs singulières (SVD) et compression d'image"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/compression
prev: "[[Jalon 35 (Caractérisation séquentielle des ouverts).md]]"
next: "[[Jalon 37 (Intégrale de Riemann sur un segment).md]]"
---

# Jalon 36 : Livrable IA T3 : Décomposition en valeurs singulières (SVD) et compression d'image

## 1. Genèse et Motivation (L'Échafaudage Cognitif)

L'algèbre linéaire a longtemps été dominée par l'étude des endomorphismes et des matrices carrées, pour lesquelles la diagonalisation et le théorème spectral apportent des réponses élégantes. Cependant, dans le monde réel, et particulièrement en analyse de données et en traitement du signal, l'information ne se présente presque jamais sous la forme de matrices carrées parfaitement symétriques. Imaginez une photographie en niveaux de gris : elle est représentée par une matrice $M$ de dimensions $m \times n$, où $m$ est le nombre de pixels en hauteur et $n$ en largeur. Il n'y a aucune raison que $m$ soit égal à $n$. De plus, comment extraire les "concepts fondamentaux" ou les "motifs récurrents" d'une telle image sans perdre son sens global ?

Le problème mathématique sous-jacent est vertigineux : comment trouver une décomposition canonique pour *n'importe quelle* matrice, même rectangulaire ? C'est le mathématicien italien Eugenio Beltrami en 1873, suivi de près par le français Camille Jordan en 1874, qui, de manière indépendante, ont commencé à poser les jalons de ce qui allait devenir la Décomposition en Valeurs Singulières (SVD). Leur intuition reposait sur la géométrie des formes bilinéaires. Plus tard, Carl Eckart et Gale Young en 1936 ont prouvé un théorème fondamental reliant la SVD à la meilleure approximation de rang faible d'une matrice.

La Décomposition en Valeurs Singulières permet de considérer n'importe quelle transformation linéaire comme la succession de trois opérations géométriques élémentaires : une première rotation de l'espace de départ, un redimensionnement (étirement ou compression) le long d'axes orthogonaux, et une seconde rotation dans l'espace d'arrivée. Cette vision est prodigieuse. Elle signifie que même la matrice la plus informe et rectangulaire cache en elle une structure orthonormée parfaite. Dans le contexte de l'IA, la SVD est le couteau suisse absolu : elle est le moteur de l'Analyse en Composantes Principales (PCA), des systèmes de recommandation, et bien sûr, de la compression d'images, où l'on cherche à isoler et conserver uniquement les valeurs singulières dominantes qui portent la "sémantique" visuelle de l'image, tout en jetant le bruit.

## 2. Formalisation de la Décomposition en Valeurs Singulières (SVD)

### A. Énoncé Symbolique Strict du Théorème Fondamental

Soient $m, n \in \mathbb{N}^*$ deux entiers naturels non nuls. Soit $A \in \mathcal{M}_{m,n}(\mathbb{R})$ une matrice réelle arbitraire.
Il existe une matrice orthogonale $U \in \mathcal{O}(m)$, une matrice orthogonale $V \in \mathcal{O}(n)$, et une matrice "diagonale" $\Sigma \in \mathcal{M}_{m,n}(\mathbb{R})$ (c'est-à-dire telle que $\Sigma_{i,j} = 0$ pour tout $i \neq j$) telles que :
$$A = U \Sigma V^T$$
De plus, les coefficients diagonaux de $\Sigma$, notés $\sigma_i = \Sigma_{i,i}$ pour $1 \le i \le p$ où $p = \min(m, n)$, sont des réels positifs ou nuls ($\sigma_i \ge 0$). Quitte à réordonner les colonnes de $U$ et $V$, on peut toujours imposer l'ordre décroissant :
$$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0$$

### B. Anatomie et Typage Chirurgical

Décortiquons chaque objet mathématique de cette décomposition :
- $\mathcal{M}_{m,n}(\mathbb{R})$ : L'espace vectoriel des matrices à coefficients réels possédant $m$ lignes et $n$ colonnes. L'opérateur associé à $A$ agit de $\mathbb{R}^n$ vers $\mathbb{R}^m$.
- $\mathcal{O}(m)$ et $\mathcal{O}(n)$ : Les groupes orthogonaux de dimension $m$ et $n$. Cela signifie que $U^T U = I_m$ et $V^T V = I_n$. Géométriquement, ces matrices représentent des isométries (rotations ou symétries).
- $U \in \mathcal{O}(m)$ : Ses vecteurs colonnes, notés $u_1, u_2, \dots, u_m$, sont appelés les **vecteurs singuliers à gauche** de $A$. Ils forment une base orthonormée de $\mathbb{R}^m$.
- $V \in \mathcal{O}(n)$ : Ses vecteurs colonnes, notés $v_1, v_2, \dots, v_n$, sont appelés les **vecteurs singuliers à droite** de $A$. Ils forment une base orthonormée de $\mathbb{R}^n$.
- $\Sigma \in \mathcal{M}_{m,n}(\mathbb{R})$ : Cette matrice n'est carrée que si $m=n$. Sinon, elle contient un bloc diagonal de taille $p \times p$ (avec $p = \min(m,n)$) et des blocs de zéros ailleurs pour combler les dimensions. Ses coefficients diagonaux $\sigma_i$ sont appelés les **valeurs singulières** de $A$.
- $V^T$ : La transposée de $V$, qui est aussi son inverse puisque $V$ est orthogonale ($V^{-1} = V^T$).

### C. Exemples de Validation

**Exemple trivial (Matrice diagonale carrée) :**
Soit $A = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix}$. Bien qu'elle soit diagonale, ses valeurs propres (2 et -3) ne sont pas toutes positives.
On peut écrire :
$$A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}^T$$
Ici, $U = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ est bien orthogonale, $\Sigma = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ a ses termes diagonaux positifs, et $V = I_2$ est orthogonale. Les valeurs singulières sont 2 et 3 (l'ordre décroissant nécessiterait juste de permuter les colonnes).

**Exemple rectangulaire :**
Soit $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ -1 & 1 \end{pmatrix} \in \mathcal{M}_{3,2}(\mathbb{R})$.
La SVD de $A$ donnera une matrice $U \in \mathcal{M}_{3,3}(\mathbb{R})$, $\Sigma = \begin{pmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \\ 0 & 0 \end{pmatrix} \in \mathcal{M}_{3,2}(\mathbb{R})$, et $V \in \mathcal{M}_{2,2}(\mathbb{R})$. (Le calcul explicite sera l'objet des exercices).

### D. Cas Pathologiques et Contre-exemples

- **Valeurs singulières non ordonnées ou négatives :** Il est fréquent de trouver une décomposition $A = U D V^T$ où $D$ est diagonale mais avec des termes négatifs ou non triés. Ce n'est *pas* la SVD standard. Il faut corriger le signe (en multipliant la colonne correspondante de $U$ ou $V$ par -1) et réordonner (en appliquant des matrices de permutation à droite de $U$ et $D$, et à gauche de $V^T$).
- **Matrice Nulle :** Si $A$ est la matrice nulle de taille $m \times n$, alors toutes ses valeurs singulières sont nulles ($\sigma_i = 0$). Dans ce cas, n'importe quelles matrices orthogonales $U$ et $V$ satisfont $A = U \Sigma V^T$. La décomposition n'est donc pas unique. L'unicité des vecteurs singuliers n'est garantie (à un signe près) que pour des valeurs singulières distinctes et strictement positives.

## 3. Le Théorème d'Eckart-Young-Mirsky (L'Approximation de Rang Faible)

C'est ici que la SVD devient l'outil central de la compression.

### A. Énoncé Symbolique Strict

Soit $A \in \mathcal{M}_{m,n}(\mathbb{R})$ de rang $r \le \min(m, n)$. Sa SVD est $A = U \Sigma V^T = \sum_{i=1}^r \sigma_i u_i v_i^T$.
Soit un entier $k$ tel que $1 \le k < r$.
On définit la matrice tronquée :
$$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$$
Le théorème affirme que $A_k$ est la **meilleure approximation de $A$ par une matrice de rang au plus $k$**, au sens de la norme de Frobenius (et de la norme spectrale).
Mathématiquement :
$$\min_{B \in \mathcal{M}_{m,n}(\mathbb{R}), \, \text{rg}(B) \le k} \|A - B\|_F = \|A - A_k\|_F = \sqrt{\sum_{i=k+1}^r \sigma_i^2}$$
Où la norme de Frobenius d'une matrice $M$ est $\|M\|_F = \sqrt{\text{Tr}(M^T M)} = \sqrt{\sum_{i,j} M_{i,j}^2}$.

### B. Anatomie et Typage Chirurgical

- $A_k \in \mathcal{M}_{m,n}(\mathbb{R})$ : C'est une matrice de même taille que $A$.
- $\text{rg}(B) \le k$ : L'ensemble des matrices de rang au plus $k$ n'est pas un sous-espace vectoriel (l'addition de deux matrices de rang $k$ peut avoir un rang $>k$), ce qui rend le problème de minimisation non trivial (pas de projection orthogonale simple globale).
- $u_i v_i^T$ : C'est le produit d'un vecteur colonne $u_i \in \mathbb{R}^m$ par un vecteur ligne $v_i^T \in \mathbb{R}^{1 \times n}$. Le résultat est une matrice de taille $m \times n$, de rang exactement égal à 1.
- Ainsi, $A_k$ est construite comme la somme pondérée (par les plus grandes valeurs singulières $\sigma_i$) des $k$ matrices de rang 1 "les plus représentatives" de $A$.

## 4. Zéro Ellipse Mathématique : Démonstration de l'Existence de la SVD

Prouvons l'existence de la SVD pour toute matrice réelle $A \in \mathcal{M}_{m,n}(\mathbb{R})$.
Soit $A \in \mathcal{M}_{m,n}(\mathbb{R})$.

**Étape 1 : Construction de la matrice de covariance $S$ et de la base $V$.**
Considérons la matrice $S = A^T A \in \mathcal{M}_n(\mathbb{R})$.
Observons les propriétés de $S$ :
1. $S$ est symétrique : $S^T = (A^T A)^T = A^T (A^T)^T = A^T A = S$.
2. $S$ est positive : Pour tout vecteur $x \in \mathbb{R}^n$, évaluons la forme quadratique associée :
   $x^T S x = x^T (A^T A) x = (Ax)^T (Ax) = \|Ax\|_2^2 \ge 0$.
Puisque $S$ est une matrice symétrique réelle, d'après le théorème spectral, elle est orthogonalement diagonalisable. Il existe donc une base orthonormée $(v_1, v_2, \dots, v_n)$ de $\mathbb{R}^n$ constituée de vecteurs propres de $S$, associés aux valeurs propres réelles $\lambda_1, \lambda_2, \dots, \lambda_n$.
Puisque $S$ est positive, on a pour tout $i$, $v_i^T S v_i = v_i^T (\lambda_i v_i) = \lambda_i \|v_i\|_2^2 = \lambda_i$.
Or, on sait aussi que $v_i^T S v_i = \|A v_i\|_2^2 \ge 0$. On en déduit que pour tout $i \in \{1, \dots, n\}$, $\lambda_i \ge 0$.
Quitte à réindexer, on peut ordonner les valeurs propres de manière décroissante :
$$\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_r > 0 \quad \text{et} \quad \lambda_{r+1} = \dots = \lambda_n = 0$$
où $r$ est le nombre de valeurs propres strictement positives (on montrera que $r$ est le rang de $A$).
On définit les **valeurs singulières** $\sigma_i = \sqrt{\lambda_i}$ pour $1 \le i \le n$.
La matrice $V$ est définie comme la matrice dont les colonnes sont les $v_i$ : $V = (v_1 | v_2 | \dots | v_n) \in \mathcal{O}(n)$.

**Étape 2 : Construction de la base orthonormée $U$ partielle.**
Pour $i \in \{1, \dots, r\}$, on a $\sigma_i > 0$. On définit les vecteurs $u_i \in \mathbb{R}^m$ par :
$$u_i = \frac{1}{\sigma_i} A v_i$$
Vérifions que la famille $(u_1, \dots, u_r)$ est une famille orthonormée de $\mathbb{R}^m$.
Calculons le produit scalaire euclidien usuel entre $u_i$ et $u_j$ (pour $i, j \in \{1, \dots, r\}$) :
$$\langle u_i, u_j \rangle = u_j^T u_i = \left( \frac{1}{\sigma_j} A v_j \right)^T \left( \frac{1}{\sigma_i} A v_i \right) = \frac{1}{\sigma_i \sigma_j} v_j^T A^T A v_i = \frac{1}{\sigma_i \sigma_j} v_j^T S v_i$$
Puisque $v_i$ est un vecteur propre de $S$ associé à la valeur propre $\lambda_i = \sigma_i^2$, on a $S v_i = \sigma_i^2 v_i$.
$$\langle u_i, u_j \rangle = \frac{1}{\sigma_i \sigma_j} v_j^T (\sigma_i^2 v_i) = \frac{\sigma_i}{\sigma_j} v_j^T v_i$$
Comme la base $(v_1, \dots, v_n)$ est orthonormée, $v_j^T v_i = \delta_{i,j}$ (symbole de Kronecker).
Donc si $i \neq j$, $\langle u_i, u_j \rangle = 0$.
Et si $i = j$, $\langle u_i, u_i \rangle = \frac{\sigma_i}{\sigma_i} \times 1 = 1$.
La famille $(u_1, \dots, u_r)$ est donc bien orthonormée.

**Étape 3 : Complétion de la base $U$ et synthèse.**
D'après le théorème de la base incomplète (et le procédé d'orthonormalisation de Gram-Schmidt si nécessaire), on peut compléter la famille orthonormée $(u_1, \dots, u_r)$ en une base orthonormée complète de $\mathbb{R}^m$, que l'on notera $(u_1, \dots, u_r, u_{r+1}, \dots, u_m)$.
On définit la matrice orthogonale $U = (u_1 | u_2 | \dots | u_m) \in \mathcal{O}(m)$.
Maintenant, construisons la matrice $\Sigma \in \mathcal{M}_{m,n}(\mathbb{R})$ dont les éléments diagonaux $\Sigma_{i,i}$ valent $\sigma_i$ pour $1 \le i \le r$, et tous les autres éléments (y compris les diagonaux pour $i > r$) valent $0$.

Vérifions enfin que $A V = U \Sigma$, ce qui équivaut à $A = U \Sigma V^T$ car $V \in \mathcal{O}(n) \implies V^{-1} = V^T$.
Calculons l'action de $A$ sur chaque vecteur de la base $V$.
Pour $1 \le i \le r$ :
D'après notre définition de $u_i$, on a directement $A v_i = \sigma_i u_i$.
Pour $r < i \le n$ :
On sait que $\lambda_i = 0$, donc $S v_i = 0$. Ainsi, $A^T A v_i = 0$.
Multiplions à gauche par $v_i^T$ : $v_i^T A^T A v_i = 0 \implies (A v_i)^T (A v_i) = 0 \implies \|A v_i\|_2^2 = 0 \implies A v_i = 0$.
Par ailleurs, exprimons les colonnes du produit matriciel $U \Sigma$.
La $i$-ème colonne de $U \Sigma$ est obtenue en multipliant la matrice $U$ par la $i$-ème colonne de $\Sigma$.
Pour $1 \le i \le r$, la $i$-ème colonne de $\Sigma$ a un seul élément non nul, $\sigma_i$, à la ligne $i$. Donc le produit $U \Sigma$ donne exactement $\sigma_i u_i$.
Pour $r < i \le n$, la $i$-ème colonne de $\Sigma$ est constituée de zéros. Le produit $U \Sigma$ donne le vecteur nul.
On a donc bien prouvé que pour tout $i \in \{1, \dots, n\}$, la $i$-ème colonne de $A V$ est égale à la $i$-ème colonne de $U \Sigma$.
Par conséquent, $A V = U \Sigma$, et en post-multipliant par $V^T$, on obtient la décomposition finale absolue :
$$A = U \Sigma V^T$$
CQFD. Ce niveau de détail est la seule façon acceptable de faire des mathématiques supérieures. L'ellipse n'a pas sa place ici.

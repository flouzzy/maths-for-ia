---
title: "Exercice 1 : Unicité de la solution des moindres carrés"
difficulty: ★☆☆☆☆
---
# Énoncé
Soit un jeu de données de $n$ points $\mathcal{D} = {(x_i, y_i)\}_{1 \le i \le n}$ où les $x_i$ sont deux à deux distincts. On cherche à ajuster un polynôme $P(X) = \sum_{k=0}^d a_k X^k$ de degré $d < n$.
Démontrer rigoureusement que la matrice $\mathbf{X}^\top\mathbf{X}$ (où $\mathbf{X}$ est la matrice de Vandermonde associée) est définie positive, et en déduire l'unicité de la solution.

# Correction Détaillée
Soit $\mathbf{X} \in \mathcal{M}_{n, d+1}(\mathbb{R})$ définie par $X_{i,j} = x_i^{j-1}$.
1. **Semi-définie positivité :** Soit $\mathbf{u} \in \mathbb{R}^{d+1}$.
   $\mathbf{u}^\top(\mathbf{X}^\top\mathbf{X})\mathbf{u} = (\mathbf{X}\mathbf{u})^\top(\mathbf{X}\mathbf{u}) = \|\mathbf{X}\mathbf{u}\|_2^2 \ge 0$.
   Donc $\mathbf{X}^\top\mathbf{X}$ est semi-définie positive.
2. **Définie positivité :** Supposons qu'il existe $\mathbf{u}$ tel que $\mathbf{u}^\top(\mathbf{X}^\top\mathbf{X})\mathbf{u} = 0$.
   Alors $\|\mathbf{X}\mathbf{u}\|_2^2 = 0$, d'où $\mathbf{X}\mathbf{u} = \mathbf{0}_n$.
   La $i$-ème coordonnée de ce vecteur est $\sum_{k=0}^d u_k x_i^k = Q(x_i) = 0$, où $Q(X) = \sum_{k=0}^d u_k X^k$.
   Ainsi, le polynôme $Q$, de degré au plus $d$, possède $n$ racines distinctes (les $x_i$).
   Puisque $n > d$, le seul polynôme de degré $\le d$ ayant plus de $d$ racines est le polynôme nul.
   Donc $\forall k, u_k = 0$, c'est-à-dire $\mathbf{u} = \mathbf{0}$.
   La matrice $\mathbf{X}^\top\mathbf{X}$ est donc définie positive, ce qui implique qu'elle est inversible.
3. **Unicité :** Les équations normales s'écrivent $(\mathbf{X}^\top\mathbf{X})\mathbf{a} = \mathbf{X}^\top\mathbf{y}$. L'inversibilité garantit une unique solution $\hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$.

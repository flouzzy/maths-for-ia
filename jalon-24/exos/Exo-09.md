---
title: "Exercice 9 : Polynômes Orthogonaux et Stabilité Numérique"
difficulty: ★★★★★
---
# Énoncé
Expliquer rigoureusement pourquoi utiliser la base canonique ${1, X, X^2, \dots, X^d\}$ conduit à un système mal conditionné lorsque $d$ grandit.
Montrer que si l'on utilise une base de polynômes orthogonaux ${L_0, L_1, \dots, L_d\}$ tels que $\sum_{i=1}^n L_k(x_i)L_m(x_i) = \delta_{km}$, la matrice $\mathbf{X}^\top\mathbf{X}$ devient l'identité.

# Correction Détaillée
1. **Mal-conditionnement de la base canonique :**
   Pour des points $x_i \in [0, 1]$, les colonnes de $\mathbf{X}$ sont les vecteurs $c_k = (x_1^k, \dots, x_n^k)^\top$.
   Pour $k$ grand, $x_i^k \to 0$ ou $1$, les vecteurs colonnes deviennent presque colinéaires. Le déterminant de $\mathbf{X}^\top\mathbf{X}$ (matrice de Hilbert pour la limite continue) tend vers $0$ exponentiellement vite, provoquant une explosion des erreurs d'arrondi lors de l'inversion numérique.
2. **Utilisation de polynômes orthogonaux :**
   Construisons une nouvelle matrice $\mathbf{\tilde{X}}$ où $\tilde{X}_{i,k} = L_{k-1}(x_i)$.
   L'élément $(k, m)$ de la matrice $\mathbf{\tilde{X}}^\top\mathbf{\tilde{X}}$ est le produit scalaire des colonnes $k$ et $m$ :
   $(\mathbf{\tilde{X}}^\top\mathbf{\tilde{X}})_{k,m} = \sum_{i=1}^n \tilde{X}_{i,k} \tilde{X}_{i,m} = \sum_{i=1}^n L_{k-1}(x_i) L_{m-1}(x_i)$.
   Par définition de l'orthogonalité de cette base discrète, cela vaut $1$ si $k=m$ et $0$ sinon.
   Donc $\mathbf{\tilde{X}}^\top\mathbf{\tilde{X}} = \mathbf{I}_{d+1}$.
3. **Conclusion Numérique :**
   L'inversion matricielle devient triviale, et les coefficients sont simplement $\hat{a}_k = \sum_{i=1}^n y_i L_k(x_i)$. Cette méthode, souvent réalisée via l'algorithme de Gram-Schmidt, immunise complètement la régression polynomiale contre les instabilités de la matrice de Vandermonde.

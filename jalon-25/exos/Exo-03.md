---
title: "Exercice 3 : Identité du parallélogramme"
difficulty: 2
---

### Exercice 3 : Matrices de Gram et indépendance linéaire
**Niveau : \star \star**

**Énoncé :**
Soit $E$ un espace euclidien et $x_1, \ldots, x_n$ des vecteurs de $E$. La matrice de Gram $G(x_1, \ldots, x_n)$ est la matrice de terme général $G_{i,j} = \langle x_i, x_j \rangle$.
Démontrer que la famille $(x_1, \ldots, x_n)$ est libre si et seulement si $\det(G) \neq 0$.

**Correction (Zéro Ellipse) :**
Soit $G \in M_n(\mathbb{R})$ définie par $G_{i,j} = \langle x_i, x_j \rangle$.
Soit $U \in M_{n,1}(\mathbb{R})$ un vecteur colonne.
Calculons la quantité matricielle $U^T G U$.
Par définition du produit matriciel, le coefficient $i$ du vecteur $GU$ est $\sum_{j=1}^n G_{i,j} U_j = \sum_{j=1}^n \langle x_i, x_j \rangle U_j$.
Puis $U^T (GU) = \sum_{i=1}^n U_i (\sum_{j=1}^n \langle x_i, x_j \rangle U_j) = \sum_{i=1}^n \sum_{j=1}^n U_i U_j \langle x_i, x_j \rangle$.
Par bilinéarité du produit scalaire, ceci équivaut à :
\[ U^T G U = \left\langle \sum_{i=1}^n U_i x_i, \sum_{j=1}^n U_j x_j \right\rangle = \left\| \sum_{i=1}^n U_i x_i \right\|^2 \]
Supposons que la famille $(x_1, \ldots, x_n)$ est libre. Si $GU = 0$, alors $U^T G U = 0$, donc $\left\| \sum U_i x_i \right\|^2 = 0$. Le produit scalaire étant défini positif, $\sum_{i=1}^n U_i x_i = 0_E$. Comme la famille est libre, $\forall i, U_i = 0$, donc $U = 0$. Le noyau de $G$ est réduit à $\{0\}$, $G$ est inversible, d'où $\det(G) \neq 0$.
Réciproquement, supposons $\det(G) \neq 0$. Si $\sum_{i=1}^n U_i x_i = 0_E$, alors pour tout $k \in \{1,\ldots,n\}$, $\langle x_k, \sum U_i x_i \rangle = 0$, ce qui se traduit par $\sum_{i=1}^n G_{k,i} U_i = 0$. Sous forme matricielle, $GU = 0$. Puisque $G$ est inversible, $U = 0$, donc $\forall i, U_i = 0$. La famille est bien libre.

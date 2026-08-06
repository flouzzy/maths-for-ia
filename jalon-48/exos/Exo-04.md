# Exercice 4 : Jacobienne d'une couche dense
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé
Considérons l'application de pré-activation $z = W a + b$, où $W \in \mathcal{M}_{m,n}(\mathbb{R})$, $a \in \mathbb{R}^n$ et $b \in \mathbb{R}^m$. Calculer formellement la matrice Jacobienne $J_a(z) = \frac{\partial z}{\partial a}$.

## Correction détaillée
1. La définition de la matrice Jacobienne d'une fonction vectorielle $f : \mathbb{R}^n \to \mathbb{R}^m$ est la matrice de taille $m \times n$ dont le coefficient $(i, j)$ est $\frac{\partial f_i}{\partial x_j}$.
2. Explicitons la i-ème composante du vecteur $z$ : $z_i = \sum_{k=1}^n W_{ik} a_k + b_i$.
3. Dérivons $z_i$ par rapport à la variable d'entrée $a_j$. Les termes de la somme où $k \neq j$ ne dépendent pas de $a_j$, leur dérivée est donc nulle. Le biais $b_i$ est constant par rapport à $a_j$.
4. Il reste uniquement le terme pour $k=j$ : $\frac{\partial z_i}{\partial a_j} = \frac{\partial}{\partial a_j} (W_{ij} a_j) = W_{ij}$.
5. Ainsi, le coefficient de la matrice Jacobienne en ligne $i$ et colonne $j$ est exactement le coefficient $W_{ij}$ de la matrice des poids.
6. En conclusion, la matrice Jacobienne est simplement la matrice des poids : $J_a(z) = W$.
C'est pourquoi, lors de la rétropropagation, on multiplie l'erreur par la transposée de la matrice des poids $W^T$ (pour faire redescendre le gradient de $\mathbb{R}^m$ vers $\mathbb{R}^n$).

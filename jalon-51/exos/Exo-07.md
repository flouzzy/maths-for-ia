---
title: "Exo-07 : Produit d'espaces métriques"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exo-07 : Produit d'espaces métriques


## 1. Énoncé

Soient $(X_1, d_1)$ et $(X_2, d_2)$ deux espaces métriques. Sur le produit cartésien $X = X_1 \times X_2$, on définit :
$$D((x_1, x_2), (y_1, y_2)) = d_1(x_1, y_1) + d_2(x_2, y_2)$$

1. Montrer que $D$ est une distance sur $X$.
2. Montrer qu'une suite $z_n = (x_{1,n}, x_{2,n})$ converge vers $l = (l_1, l_2)$ dans $(X, D)$ si et seulement si $x_{1,n} \to l_1$ dans $(X_1, d_1)$ et $x_{2,n} \to l_2$ dans $(X_2, d_2)$.

## 2. Correction détaillée

**Question 1 :**
Soient $x=(x_1, x_2), y=(y_1, y_2), z=(z_1, z_2) \in X$.
- **Séparation :** $D(x, y) = 0 \iff d_1(x_1, y_1) + d_2(x_2, y_2) = 0$. Étant des quantités positives, la somme est nulle si et seulement si chacune est nulle. $d_1(x_1, y_1) = 0 \iff x_1 = y_1$ et $d_2(x_2, y_2) = 0 \iff x_2 = y_2$. Donc $x=y$.
- **Symétrie :** $D(x, y) = d_1(x_1, y_1) + d_2(x_2, y_2) = d_1(y_1, x_1) + d_2(y_2, x_2) = D(y, x)$.
- **Inégalité triangulaire :**
  $D(x, z) = d_1(x_1, z_1) + d_2(x_2, z_2)$
  $\le (d_1(x_1, y_1) + d_1(y_1, z_1)) + (d_2(x_2, y_2) + d_2(y_2, z_2))$
  $= (d_1(x_1, y_1) + d_2(x_2, y_2)) + (d_1(y_1, z_1) + d_2(y_2, z_2))$
  $= D(x, y) + D(y, z)$.
$D$ est bien une distance.

**Question 2 :**
- Supposons $z_n \to l$. Alors pour tout $\epsilon > 0$, il existe $N$ tel que $n \ge N \implies D(z_n, l) < \epsilon$.
  Comme $d_1(x_{1,n}, l_1) \le D(z_n, l)$, on a $d_1(x_{1,n}, l_1) < \epsilon$. Donc $x_{1,n} \to l_1$. De même pour $x_{2,n}$.
- Réciproquement, supposons $x_{1,n} \to l_1$ et $x_{2,n} \to l_2$.
  Soit $\epsilon > 0$. Il existe $N_1$ tel que $n \ge N_1 \implies d_1(x_{1,n}, l_1) < \epsilon/2$.
  Il existe $N_2$ tel que $n \ge N_2 \implies d_2(x_{2,n}, l_2) < \epsilon/2$.
  Pour $n \ge \max(N_1, N_2)$, $D(z_n, l) = d_1(x_{1,n}, l_1) + d_2(x_{2,n}, l_2) < \epsilon/2 + \epsilon/2 = \epsilon$.
  Donc $z_n \to l$.
La convergence dans l'espace produit métrique est bien la convergence coordonnée par coordonnée.

---
uuid: "jalon-26-exo-04"
title: "Matrice de Gram et liberté"
difficulty: 3
---

# Exercice 4 : Matrice de Gram et liberté (Difficulté ★★★☆☆)

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace préhilbertien réel. Soit $(x_1, \ldots, x_p)$ une famille de $p$ vecteurs de $E$.
On définit la matrice de Gram $G(x_1, \ldots, x_p) \in \mathcal{M}_p(\mathbb{R})$ par $G_{i,j} = \langle x_i, x_j \rangle$.
1. Montrer que pour tout vecteur colonne $X \in \mathbb{R}^p$, $X^T G X = \|\sum_{i=1}^p X_i x_i\|^2$.
2. En déduire que la matrice $G$ est symétrique définie positive si et seulement si la famille $(x_1, \ldots, x_p)$ est libre.
3. Montrer que si la famille est liée, le déterminant de $G$ est nul.

## Démonstration Rigoureuse à Blanc

1. Soit $X = \begin{pmatrix} X_1 \\ \vdots \\ X_p \end{pmatrix}$. Le scalaire $X^T G X$ s'écrit :
   $$ X^T G X = \sum_{i=1}^p \sum_{j=1}^p X_i G_{i,j} X_j $$
   Puisque $G_{i,j} = \langle x_i, x_j \rangle$ :
   $$ X^T G X = \sum_{i=1}^p \sum_{j=1}^p X_i X_j \langle x_i, x_j \rangle $$
   En utilisant la bilinéarité du produit scalaire :
   $$ \sum_{i=1}^p \sum_{j=1}^p \langle X_i x_i, X_j x_j \rangle = \langle \sum_{i=1}^p X_i x_i, \sum_{j=1}^p X_j x_j \rangle $$
   Ce qui donne par définition de la norme :
   $$ X^T G X = \left\| \sum_{i=1}^p X_i x_i \right\|^2 $$

2. La matrice $G$ est symétrique car $G_{i,j} = \langle x_i, x_j \rangle = \langle x_j, x_i \rangle = G_{j,i}$.
   - D'après la question 1, $X^T G X \ge 0$ pour tout $X$, donc $G$ est positive.
   - $G$ est définie positive si et seulement si $X^T G X = 0 \implies X = 0$.
   - Or, $X^T G X = 0 \iff \left\| \sum_{i=1}^p X_i x_i \right\|^2 = 0 \iff \sum_{i=1}^p X_i x_i = 0_E$.
   - Dire que $\sum_{i=1}^p X_i x_i = 0_E \implies X_1 = X_2 = \ldots = X_p = 0$, c'est exactement la définition d'une famille $(x_1, \ldots, x_p)$ libre.
   - Donc $G$ est définie positive si et seulement si la famille est libre.

3. Si la famille est liée, il existe une combinaison linéaire non triviale qui s'annule, donc il existe $X \neq 0$ tel que $\sum_{i=1}^p X_i x_i = 0_E$.
   - Alors $X^T G X = 0$.
   - De plus, si $V = \sum_{i=1}^p X_i x_i = 0_E$, alors pour tout $k$, $\langle x_k, V \rangle = 0$.
   - C'est-à-dire $\sum_{j=1}^p X_j \langle x_k, x_j \rangle = 0$, soit $\sum_{j=1}^p G_{k,j} X_j = 0$.
   - Donc $GX = 0$ (avec $X \neq 0$). Le noyau de $G$ n'est pas réduit à $\{0\}$, ce qui implique que $G$ n'est pas inversible.
   - Par conséquent, son déterminant est nul : $\det(G) = 0$.
   $\blacksquare$

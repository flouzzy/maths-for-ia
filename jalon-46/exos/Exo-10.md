# Exercice 10 : Jacobienne d'un réseau multi-couches $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$
## Énoncé
Soit un réseau $f(x) = W_2 \sigma(W_1 x)$ où $x \in \mathbb{R}^n$, $W_1 \in \mathcal{M}_{p,n}(\mathbb{R})$, $W_2 \in \mathcal{M}_{m,p}(\mathbb{R})$ et $\sigma$ agit composante par composante.
Démontrer que la jacobienne de $f$ par rapport à l'entrée $x$ s'écrit :
$J_f(x) = W_2 \Sigma'(W_1 x) W_1$ où $\Sigma'(z)$ est la matrice diagonale des dérivées des activations.
## Correction Détaillée
Soit $h = g \circ k \circ l$, avec :
- $l(x) = W_1 x$ : application linéaire, $J_l(x) = W_1$.
- $k(z) = \sigma(z)$ : application de $\mathbb{R}^p \to \mathbb{R}^p$ où $k_i(z) = \sigma(z_i)$.
  Puisque la $i$-ème coordonnée de $k$ ne dépend que de $z_i$, les dérivées croisées $\frac{\partial k_i}{\partial z_j}$ sont nulles pour $i \neq j$.
  Donc $J_k(z)$ est une matrice diagonale : $J_k(z) = \mathrm{Diag}(\sigma'(z_1), \dots, \sigma'(z_p)) = \Sigma'(z)$.
- $g(a) = W_2 a$ : application linéaire, $J_g(a) = W_2$.

Appliquons la règle de la chaîne généralisée :
$$ J_f(x) = J_g(k(l(x))) \times J_k(l(x)) \times J_l(x) $$
En remplaçant par les matrices trouvées :
$$ J_f(x) = W_2 \times \Sigma'(W_1 x) \times W_1 $$
Ce produit $m \times p \times p \times p \times p \times n$ donne bien une matrice de taille $m \times n$, reflétant fidèlement l'étirement global de l'espace par le réseau au voisinage de $x$.
$\blacksquare$

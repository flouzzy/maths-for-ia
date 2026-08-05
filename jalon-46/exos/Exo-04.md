# Exercice 4 : Règle de la chaîne dimension 1 $\to$ 2 $\to$ 1 $\quad \bigstar\bigstar$
## Énoncé
Soit $f : \mathbb{R} \to \mathbb{R}^2$ définie par $f(t) = (t^2, e^t)^T$ et $g : \mathbb{R}^2 \to \mathbb{R}$ définie par $g(x,y) = x y^2$.
Soit $h = g \circ f$. Calculer $h'(t)$ de deux manières différentes :
1) Par composition explicite puis dérivation classique.
2) En utilisant le produit des matrices jacobiennes.
## Correction Détaillée
**Méthode 1 : Composition explicite**
$h(t) = g(f(t)) = g(t^2, e^t) = (t^2)(e^t)^2 = t^2 e^{2t}$.
La dérivée (produit) : $h'(t) = 2t e^{2t} + t^2(2e^{2t}) = 2t e^{2t}(1+t)$.

**Méthode 2 : Produit des Jacobiennes**
- $J_f(t) = \begin{pmatrix} 2t \\ e^t \end{pmatrix}$
- $J_g(x,y) = \begin{pmatrix} y^2 & 2xy \end{pmatrix}$
La matrice $J_{g \circ f}(t) = J_g(f(t)) J_f(t)$.
$J_g(f(t)) = J_g(t^2, e^t) = \begin{pmatrix} (e^t)^2 & 2(t^2)(e^t) \end{pmatrix} = \begin{pmatrix} e^{2t} & 2t^2 e^t \end{pmatrix}$.
Le produit matriciel :
$$ J_{g \circ f}(t) = \begin{pmatrix} e^{2t} & 2t^2 e^t \end{pmatrix} \begin{pmatrix} 2t \\ e^t \end{pmatrix} = 2t e^{2t} + (2t^2 e^t)(e^t) = 2te^{2t} + 2t^2e^{2t} = 2t e^{2t}(1+t) $$
Les deux méthodes coïncident parfaitement.
$\blacksquare$

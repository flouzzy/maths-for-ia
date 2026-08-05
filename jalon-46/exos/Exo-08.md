# Exercice 8 : Dérivation d'une équation implicite $\quad \bigstar\bigstar\bigstar\star\star$
## Énoncé
Soit l'équation $x^2 y + y^3 x - 2 = 0$. On suppose que cette équation définit localement $y$ comme une fonction de $x$, soit $y = \phi(x)$.
Calculer $\phi'(x)$ en utilisant le théorème de composition.
## Correction Détaillée
Posons $F(x, y) = x^2 y + y^3 x - 2$. Nous savons que $F(x, \phi(x)) = 0$ pour tout $x$.
On définit $g(x) = (x, \phi(x))^T$, de sorte que la fonction composée $h(x) = F(g(x)) = 0$.
Par la règle de la chaîne, $dh_x = dF_{g(x)} \circ dg_x = 0$.
En termes de matrices jacobiennes :
$J_h(x) = J_F(x, \phi(x)) \times J_g(x) = 0$.
- $J_F(x, y) = \begin{pmatrix} \frac{\partial F}{\partial x} & \frac{\partial F}{\partial y} \end{pmatrix} = \begin{pmatrix} 2xy + y^3 & x^2 + 3y^2 x \end{pmatrix}$.
- $J_g(x) = \begin{pmatrix} 1 \\ \phi'(x) \end{pmatrix}$.

Le produit donne l'équation scalaire :
$$ (2x\phi(x) + \phi(x)^3) \cdot 1 + (x^2 + 3\phi(x)^2 x) \cdot \phi'(x) = 0 $$
On isole $\phi'(x)$ :
$$ \phi'(x) = - \frac{2x\phi(x) + \phi(x)^3}{x^2 + 3x\phi(x)^2} $$
$\blacksquare$

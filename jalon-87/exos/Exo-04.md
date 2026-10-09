# Exercice 4 : Théorème de transfert en deux dimensions

**Difficulté :** $\bigstarigstarigstar\star\star$

On considère un couple de variables aléatoires $(X, Y)$ de densité conjointe :
$$ f_{X,Y}(x,y) = \begin{cases} 2 & \text{si } 0 \le x \le y \le 1 \\ 0 & \text{sinon} \end{cases} $$
Calculer l'espérance du produit $XY$, soit $\mathbb{E}[XY]$.

### Correction détaillée

Par le théorème de transfert étendu aux vecteurs aléatoires, pour une fonction mesurable $g(x,y)$, l'espérance est donnée par :
$$ \mathbb{E}[g(X,Y)] = \int_{\mathbb{R}^2} g(x,y) f_{X,Y}(x,y) \, \mathrm{d}x \, \mathrm{d}y $$

1. Ici $g(x,y) = xy$. Le domaine d'intégration est le triangle $D = \{(x,y) \in \mathbb{R}^2 \mid 0 \le x \le y \le 1\}$.
   L'intégrale double s'écrit :
   $$ \mathbb{E}[XY] = \iint_D xy \times 2 \, \mathrm{d}x \, \mathrm{d}y $$
2. On applique le théorème de Fubini pour réécrire cette intégrale double en intégrales itérées. On choisit par exemple d'intégrer d'abord par rapport à $x$ (pour $y$ fixé, $x$ varie de $0$ à $y$), puis par rapport à $y$ (qui varie globalement de $0$ à $1$) :
   $$ \mathbb{E}[XY] = \int_{0}^{1} \left( \int_{0}^{y} 2xy \, \mathrm{d}x \right) \, \mathrm{d}y $$
3. Calcul de l'intégrale interne (à $y$ constant) :
   $$ \int_{0}^{y} 2xy \, \mathrm{d}x = y \int_{0}^{y} 2x \, \mathrm{d}x = y \left[ x^2 \right]_0^y = y (y^2 - 0) = y^3 $$
4. Calcul de l'intégrale externe :
   $$ \mathbb{E}[XY] = \int_{0}^{1} y^3 \, \mathrm{d}y = \left[ \frac{y^4}{4} \right]_0^1 = \frac{1}{4} - 0 = \frac{1}{4} $$
L'espérance du produit est donc $1/4$.

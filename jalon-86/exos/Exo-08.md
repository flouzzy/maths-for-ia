## Vecteur aléatoire et loi marginale \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Un vecteur aléatoire continu $(X, Y)$ admet pour densité conjointe :
$$f_{X,Y}(x, y) = c \cdot (x^2 + \frac{xy}{2}) \mathbf{1}_{[0, 1]}(x) \mathbf{1}_{[0, 2]}(y)$$
où $c$ est une constante réelle de normalisation.
1. Déterminer la valeur exacte de la constante $c$.
2. Déterminer la densité marginale de la variable aléatoire $X$, notée $f_X(x)$.

**Correction Explicative :**
1. Pour qu'une fonction soit une densité de probabilité conjointe, elle doit être positive et son intégrale sur l'espace tout entier $\mathbb{R}^2$ doit être égale à $1$. Cette condition axiomatique permet de déterminer la constante de normalisation $c$.
   $$1 = \iint_{\mathbb{R}^2} f_{X,Y}(x, y) dx dy = \int_{0}^{1} \int_{0}^{2} c \left(x^2 + \frac{xy}{2}\right) dy dx$$
2. Calculons l'intégrale double en intégrant d'abord par rapport à $y$, en considérant $x$ comme une constante :
   $$\int_{0}^{2} \left(x^2 + \frac{xy}{2}\right) dy = \left[ x^2 y + \frac{x y^2}{4} \right]_{y=0}^{y=2}$$
   $$= \left( x^2(2) + \frac{x(2^2)}{4} \right) - (0 + 0) = 2x^2 + \frac{4x}{4} = 2x^2 + x$$
3. Intégrons ensuite le résultat obtenu par rapport à $x$ sur son domaine d'intégration $[0, 1]$ :
   $$\int_{0}^{1} (2x^2 + x) dx = \left[ 2\frac{x^3}{3} + \frac{x^2}{2} \right]_0^1 = \left( \frac{2}{3} + \frac{1}{2} \right) - 0 = \frac{4}{6} + \frac{3}{6} = \frac{7}{6}$$
4. Nous pouvons alors déterminer $c$ :
   $$1 = c \times \frac{7}{6} \implies c = \frac{6}{7}$$
   La densité conjointe est donc $f_{X,Y}(x, y) = \frac{6}{7} (x^2 + \frac{xy}{2}) \mathbf{1}_{[0, 1]}(x) \mathbf{1}_{[0, 2]}(y)$.
5. La densité marginale de $X$ s'obtient en "marginalisant", c'est-à-dire en intégrant la densité conjointe sur toutes les valeurs possibles de la variable $Y$. L'idée géométrique est de projeter la masse de probabilité sur l'axe des $X$.
   $$f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y) dy$$
6. D'après l'indicatrice $\mathbf{1}_{[0, 1]}(x)$, on voit que $f_X(x) = 0$ si $x \notin [0, 1]$.
   Supposons $x \in [0, 1]$. L'intégration porte uniquement sur le support de $Y$, c'est-à-dire l'intervalle $[0, 2]$. Nous avons déjà calculé cette intégrale à l'étape 2, à la constante $c$ près :
   $$f_X(x) = \int_{0}^{2} \frac{6}{7} \left(x^2 + \frac{xy}{2}\right) dy = \frac{6}{7} \left(2x^2 + x\right)$$
7. Conclusion : La densité marginale de la variable aléatoire $X$ est donnée par :
   $$f_X(x) = \frac{6}{7}(2x^2 + x) \mathbf{1}_{[0, 1]}(x)$$
   On peut aisément vérifier que son intégrale sur $[0, 1]$ vaut bien $1$, confirmant sa validité en tant que densité de probabilité.

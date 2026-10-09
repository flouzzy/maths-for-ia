# Exercice 7 : Indépendance de variables à densité \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**

Soit $(X, Y)$ un couple de variables aléatoires réelles admettant pour densité jointe la fonction $f_{X,Y}$ définie sur $\mathbb{R}^2$ par :
$$ f_{X,Y}(x,y) = \begin{cases} C e^{-(x+y)} & \text{si } x \geq 0 \text{ et } y \geq 0 \\ 0 & \text{sinon} \end{cases} $$
1. Déterminer la valeur de la constante $C$ pour que $f_{X,Y}$ soit bien une densité de probabilité.
2. Déterminer les densités marginales $f_X$ et $f_Y$.
3. Montrer rigoureusement que $X$ et $Y$ sont indépendantes.

**Correction Détaillée :**

1. **Détermination de la constante $C$ :**
   - Pour que $f_{X,Y}$ soit une densité, son intégrale sur $\mathbb{R}^2$ doit valoir 1 :
     $$ \iint_{\mathbb{R}^2} f_{X,Y}(x,y) dx dy = 1 $$
   - La densité est nulle pour les valeurs négatives, donc le domaine d'intégration se réduit à $[0, +\infty[ \times [0, +\infty[$ :
     $$ \int_{0}^{+\infty} \left( \int_{0}^{+\infty} C e^{-(x+y)} dy \right) dx = 1 $$
   - L'exponentielle se factorise $e^{-(x+y)} = e^{-x}e^{-y}$ :
     $$ C \left( \int_{0}^{+\infty} e^{-x} dx \right) \left( \int_{0}^{+\infty} e^{-y} dy \right) = 1 $$
   - Calculons l'intégrale simple : $\int_{0}^{+\infty} e^{-x} dx = [-e^{-x}]_{0}^{+\infty} = 0 - (-1) = 1$.
   - On obtient donc $C \cdot 1 \cdot 1 = 1$, soit $C = 1$.
   - La densité jointe est : $f_{X,Y}(x,y) = e^{-x}e^{-y} \mathbf{1}_{\{x \geq 0\}} \mathbf{1}_{\{y \geq 0\}}$.
2. **Calcul des densités marginales :**
   - La densité marginale de $X$ s'obtient en intégrant la densité jointe sur toutes les valeurs possibles de $y$ :
     $$ f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) dy $$
   - Si $x < 0$, $f_{X,Y}(x,y) = 0$ pour tout $y$, donc $f_X(x) = 0$.
   - Si $x \geq 0$, le support non nul par rapport à $y$ est $[0, +\infty[$ :
     $$ f_X(x) = \int_{0}^{+\infty} e^{-x}e^{-y} dy = e^{-x} \int_{0}^{+\infty} e^{-y} dy = e^{-x} \cdot 1 = e^{-x} $$
   - Ainsi, $f_X(x) = e^{-x} \mathbf{1}_{\{x \geq 0\}}$. On reconnait la densité d'une loi exponentielle de paramètre $\lambda=1$.
   - Par symétrie évidente des rôles de $x$ et $y$ dans la fonction de densité jointe, on obtient immédiatement $f_Y(y) = e^{-y} \mathbf{1}_{\{y \geq 0\}}$.
3. **Preuve de l'indépendance :**
   - Un théorème fondamental stipule que deux variables aléatoires à densité sont indépendantes si et seulement si leur densité jointe est le produit (presque partout) de leurs densités marginales.
   - Vérifions cette propriété. Calculons le produit des densités marginales trouvées à l'étape 2 :
     $$ f_X(x) \cdot f_Y(y) = \left( e^{-x} \mathbf{1}_{\{x \geq 0\}} \right) \cdot \left( e^{-y} \mathbf{1}_{\{y \geq 0\}} \right) = e^{-(x+y)} \mathbf{1}_{\{x \geq 0 \text{ et } y \geq 0\}} $$
   - On constate une égalité parfaite avec la densité jointe identifiée à l'étape 1 :
     $$ f_X(x) \cdot f_Y(y) = f_{X,Y}(x,y) $$
   - L'égalité étant vraie pour tout couple $(x,y) \in \mathbb{R}^2$, les variables aléatoires $X$ et $Y$ sont formellement indépendantes.

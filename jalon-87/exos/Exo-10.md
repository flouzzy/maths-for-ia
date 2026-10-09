# Exercice 10 : Espérance conditionnelle (Introduction IA)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit un couple de variables aléatoires continues $(X,Y)$ modélisant respectivement la taille et le poids d'un individu. La densité conjointe est :
$$ f_{X,Y}(x,y) = \begin{cases} \frac{6}{5}(x + y^2) & \text{si } 0 \le x \le 1 \text{ et } 0 \le y \le 1 \\ 0 & \text{sinon} \end{cases} $$
1. Trouver la densité marginale $f_X(x)$.
2. Trouver la densité conditionnelle $f_{Y|X}(y|x)$ pour un $x \in [0,1]$ fixé.
3. Calculer l'espérance conditionnelle $\mathbb{E}[Y|X=x]$, qui est la prédiction optimale de $Y$ sachant $X=x$ en Machine Learning.

### Correction détaillée

1. **Densité marginale $f_X(x)$ :**
   On intègre la densité conjointe par rapport à la variable cachée $y$ sur tout son domaine de définition :
   $$ f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) \, \mathrm{d}y = \int_{0}^{1} \frac{6}{5}(x + y^2) \, \mathrm{d}y $$
   $$ f_X(x) = \frac{6}{5} \left[ xy + \frac{y^3}{3} \right]_0^1 = \frac{6}{5} \left( x + \frac{1}{3} \right) = \frac{6x+2}{5} $$
   Cette densité est valable pour $x \in [0,1]$, et $0$ ailleurs.

2. **Densité conditionnelle $f_{Y|X}(y|x)$ :**
   Par définition (analogue discret : probabilité conditionnelle $\mathbb{P}(A|B) = \mathbb{P}(A \cap B)/\mathbb{P}(B)$) :
   $$ f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)} $$
   $$ f_{Y|X}(y|x) = \frac{\frac{6}{5}(x + y^2)}{\frac{6x+2}{5}} = \frac{6(x+y^2)}{6x+2} = \frac{3(x+y^2)}{3x+1} $$
   Valable pour $y \in [0,1]$ (et pour un $x$ tel que $3x+1 > 0$).

3. **Espérance conditionnelle $\mathbb{E}[Y|X=x]$ :**
   Il s'agit de l'espérance de la variable $Y$ mais sous la loi conditionnelle que l'on vient de trouver :
   $$ \mathbb{E}[Y|X=x] = \int_{0}^{1} y f_{Y|X}(y|x) \, \mathrm{d}y = \int_{0}^{1} y \frac{3(x+y^2)}{3x+1} \, \mathrm{d}y $$
   Le terme $\frac{3}{3x+1}$ est constant vis-à-vis de l'intégration en $y$, on le sort de l'intégrale :
   $$ \mathbb{E}[Y|X=x] = \frac{3}{3x+1} \int_{0}^{1} (xy + y^3) \, \mathrm{d}y $$
   $$ \int_{0}^{1} (xy + y^3) \, \mathrm{d}y = \left[ x\frac{y^2}{2} + \frac{y^4}{4} \right]_0^1 = \frac{x}{2} + \frac{1}{4} = \frac{2x+1}{4} $$
   Finalement :
   $$ \mathbb{E}[Y|X=x] = \frac{3}{3x+1} \times \frac{2x+1}{4} = \frac{6x+3}{4(3x+1)} $$

   En IA, si l'on observe la taille $x$, le modèle de régression optimal (au sens de l'erreur quadratique MSE) prédira le poids $\hat{y} = \frac{6x+3}{12x+4}$.

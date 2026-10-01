## Transformation d'un signal triangulaire

**Difficulté :** $\bigstar\star\star\star\star$


Considérons le signal triangulaire (ou fonction tente) $T(x) = \max(0, 1-|x|)$.
1. Montrer que $T(x)$ est l'autocorrélation de la fonction porte $P(x) = \mathbb{1}_{[-1/2, 1/2]}(x)$. (C'est-à-dire $T = P * P$).
2. En déduire la transformée de Fourier $\hat{T}(\xi)$.
3. Utiliser le théorème de Plancherel pour évaluer $\int_{\mathbb{R}} \frac{\sin^4(\xi/2)}{(\xi/2)^4} d\xi$.

### Correction :

1. Calculons le produit de convolution $P * P(x) = \int_{\mathbb{R}} P(y) P(x-y) dy$.
La fonction $P(y)$ vaut $1$ si $y \in [-1/2, 1/2]$ et $0$ sinon.
Ainsi, $P(x-y)$ vaut $1$ si $x-y \in [-1/2, 1/2]$, c'est-à-dire $y \in [x-1/2, x+1/2]$.
L'intégrale devient la mesure de l'intersection des intervalles $[-1/2, 1/2]$ et $[x-1/2, x+1/2]$.
- Si $x > 1$ ou $x < -1$, l'intersection est vide, l'intégrale est nulle.
- Si $x \in [0, 1]$, l'intersection est $[x-1/2, 1/2]$. La longueur est $1/2 - (x-1/2) = 1-x$.
- Si $x \in [-1, 0]$, l'intersection est $[-1/2, x+1/2]$. La longueur est $x+1/2 - (-1/2) = x+1 = 1-|x|$.
Dans tous les cas, on a bien $P * P(x) = \max(0, 1-|x|) = T(x)$.

2. La transformée de Fourier convertit la convolution en produit (car $P \in L^1$).
$$ \hat{T}(\xi) = \widehat{(P * P)}(\xi) = \hat{P}(\xi) \cdot \hat{P}(\xi) = (\hat{P}(\xi))^2 $$
Or, d'après l'exercice 1 (avec $a=1/2$), on a $\hat{P}(\xi) = \frac{\sin(\xi/2)}{\xi/2}$.
Donc :
$$ \hat{T}(\xi) = \left( \frac{\sin(\xi/2)}{\xi/2} \right)^2 $$

3. Appliquons Plancherel à la fonction $T$. Son énergie est :
$$ \|T\|_{L^2}^2 = \int_{-1}^1 (1-|x|)^2 dx = 2 \int_0^1 (1-x)^2 dx = 2 \left[ -\frac{(1-x)^3}{3} \right]_0^1 = 2 \left( 0 - \left(-\frac{1}{3}\right) \right) = \frac{2}{3} $$
D'autre part :
$$ \|\hat{T}\|_{L^2}^2 = \int_{\mathbb{R}} \left( \frac{\sin(\xi/2)}{\xi/2} \right)^4 d\xi $$
D'après Plancherel, $\|T\|_{L^2}^2 = \frac{1}{2\pi} \|\hat{T}\|_{L^2}^2$.
Donc :
$$ \frac{2}{3} = \frac{1}{2\pi} \int_{\mathbb{R}} \frac{\sin^4(\xi/2)}{(\xi/2)^4} d\xi \implies \int_{\mathbb{R}} \frac{\sin^4(\xi/2)}{(\xi/2)^4} d\xi = \frac{4\pi}{3} $$

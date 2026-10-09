# Exercice 7 : Loi Log-Normale \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $X$ une variable aléatoire de loi normale $\mathcal{N}(\mu, \sigma^2)$ avec $\sigma > 0$.
Soit $Y = e^X$.
Déterminer la densité de probabilité de $Y$. Cette loi est appelée loi Log-Normale.

## Correction

La densité de probabilité de la variable normale $X$ est :
$$ f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} $$
La variable $Y = e^X$ ne prend que des valeurs strictement positives.
Pour $y \leq 0$, l'événement $\{Y \leq y\}$ est impossible (probabilité nulle), donc la fonction de répartition de $Y$ vérifie $F_Y(y) = 0$, ce qui implique que la densité $f_Y(y) = 0$ pour $y \leq 0$.

Soit $y > 0$. La fonction de répartition de $Y$ s'écrit :
$$ F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(e^X \leq y) $$
Comme la fonction logarithme népérien est strictement croissante sur $]0, +\infty[$, on peut appliquer le logarithme aux deux membres de l'inégalité en préservant son sens :
$$ F_Y(y) = \mathbb{P}(X \leq \ln(y)) $$
Par définition de la fonction de répartition de $X$, cela s'écrit :
$$ F_Y(y) = F_X(\ln(y)) $$

Pour obtenir la densité $f_Y$ de la variable $Y$, il suffit de dériver $F_Y(y)$ par rapport à $y$ sur $]0, +\infty[$. En utilisant la règle de dérivation en chaîne $(g \circ h)' = (g' \circ h) \cdot h'$, et sachant que $F_X'(x) = f_X(x)$, nous obtenons :
$$ f_Y(y) = \frac{d}{dy} F_X(\ln(y)) = f_X(\ln(y)) \cdot \frac{d}{dy}(\ln(y)) = f_X(\ln(y)) \cdot \frac{1}{y} $$

Il ne reste plus qu'à substituer l'expression de la densité normale $f_X$ évaluée au point $\ln(y)$ :
$$ f_Y(y) = \frac{1}{y} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}} = \frac{1}{y\sigma\sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}} $$

Conclusion, la densité de la loi Log-Normale est :
$$ f_Y(y) = \begin{cases} \frac{1}{y\sigma\sqrt{2\pi}} e^{-\frac{(\ln(y) - \mu)^2}{2\sigma^2}} & \text{si } y > 0 \\ 0 & \text{si } y \leq 0 \end{cases} $$ $\blacksquare$

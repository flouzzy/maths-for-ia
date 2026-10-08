## Transformation affine d'une loi continue \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire suivant une loi exponentielle de paramètre $\lambda > 0$, dont la densité de probabilité est donnée par $f_X(x) = \lambda e^{-\lambda x} \mathbf{1}_{[0, +\infty[}(x)$.
On définit la variable aléatoire $Y = aX + b$, avec $a > 0$ et $b \in \mathbb{R}$.
Déterminer la fonction de répartition et la densité de probabilité de $Y$.

**Correction Explicative :**
1. La variable $Y$ est définie par une transformation affine strictement croissante (car $a > 0$).
2. Exprimons d'abord la fonction de répartition de $X$, notée $F_X(x)$.
   Par définition, $F_X(x) = \int_{-\infty}^{x} f_X(t) dt$.
   - Si $x < 0$, $f_X(t) = 0$ sur $]-\infty, x]$, donc $F_X(x) = 0$.
   - Si $x \geq 0$, $F_X(x) = \int_{0}^{x} \lambda e^{-\lambda t} dt = \left[-e^{-\lambda t}\right]_0^x = -e^{-\lambda x} - (-1) = 1 - e^{-\lambda x}$.
3. Calculons maintenant la fonction de répartition de $Y$, notée $F_Y(y)$ :
   Par définition, $F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(aX + b \leq y)$.
   Puisque $a > 0$, l'inégalité est préservée lorsqu'on isole $X$ :
   $F_Y(y) = \mathbb{P}\left(X \leq \frac{y - b}{a}\right)$.
   Ainsi, on relie $F_Y$ à $F_X$ : $F_Y(y) = F_X\left(\frac{y - b}{a}\right)$.
4. Évaluons cette expression en distinguant les cas, puisque $F_X$ est définie par morceaux :
   La condition $\frac{y - b}{a} < 0$ est équivalente à $y < b$.
   - Si $y < b$, alors $\frac{y - b}{a} < 0$, ce qui implique $F_X\left(\frac{y - b}{a}\right) = 0$. Donc $F_Y(y) = 0$.
   - Si $y \geq b$, alors $\frac{y - b}{a} \geq 0$, ce qui implique $F_X\left(\frac{y - b}{a}\right) = 1 - e^{-\lambda \left(\frac{y - b}{a}\right)}$.
5. Pour obtenir la densité de probabilité de $Y$, notée $f_Y(y)$, nous dérivons la fonction de répartition $F_Y(y)$ par rapport à $y$, en utilisant la règle de dérivation des fonctions composées (là où la fonction est dérivable) :
   - Pour $y < b$, la dérivée est nulle.
   - Pour $y > b$, on dérive l'expression $1 - e^{-\frac{\lambda}{a}(y - b)}$ :
     $$f_Y(y) = \frac{d}{dy} \left[ 1 - e^{-\frac{\lambda}{a}(y - b)} \right] = 0 - \left(-\frac{\lambda}{a}\right) e^{-\frac{\lambda}{a}(y - b)} = \frac{\lambda}{a} e^{-\frac{\lambda}{a}(y - b)}$$
6. Conclusion : La densité de probabilité de $Y$ est donnée par :
   $$f_Y(y) = \frac{\lambda}{a} e^{-\frac{\lambda}{a}(y - b)} \mathbf{1}_{[b, +\infty[}(y)$$
   On reconnait ici une loi exponentielle translatée (d'un paramètre de position $b$) et redimensionnée (avec un nouveau paramètre d'échelle $\lambda/a$).

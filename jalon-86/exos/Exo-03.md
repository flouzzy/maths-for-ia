# Exercice 3 : Loi uniforme et transformation affine \quad $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $X$ une variable aléatoire de loi uniforme sur le segment $[a, b]$, avec $a < b$.
Soit $Y = cX + d$, où $c > 0$ et $d \in \mathbb{R}$.
Démontrer que $Y$ suit une loi uniforme sur un intervalle à déterminer.

## Correction

La variable aléatoire $X$ suit une loi uniforme sur $[a, b]$. Sa densité de probabilité est donnée par :
$$ f_X(x) = \begin{cases} \frac{1}{b - a} & \text{si } x \in [a, b] \\ 0 & \text{sinon} \end{cases} $$
La fonction de répartition de $X$ pour $x \in [a,b]$ est $F_X(x) = \int_a^x \frac{1}{b-a} dt = \frac{x-a}{b-a}$.

Calculons la fonction de répartition de $Y$, notée $F_Y(y)$, pour $y \in \mathbb{R}$.
Par définition :
$$ F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(cX + d \leq y) $$
Puisque $c > 0$, l'inégalité est préservée lorsqu'on divise par $c$ :
$$ F_Y(y) = \mathbb{P}\left(X \leq \frac{y - d}{c}\right) = F_X\left(\frac{y - d}{c}\right) $$
Puisque $X \in [a, b]$ presque sûrement, les valeurs de $Y$ se trouvent dans le domaine où $a \leq \frac{y-d}{c} \leq b$, ce qui équivaut à $ac+d \leq y \leq bc+d$. Posons $\alpha = ac+d$ et $\beta = bc+d$.

Étudions les cas pour $y$ :
1. Si $y < \alpha$, alors $\frac{y - d}{c} < a$, donc $F_X\left(\frac{y - d}{c}\right) = 0$.
2. Si $y > \beta$, alors $\frac{y - d}{c} > b$, donc $F_X\left(\frac{y - d}{c}\right) = 1$.
3. Si $y \in [\alpha, \beta]$, alors :
$$ F_Y(y) = \frac{\frac{y - d}{c} - a}{b - a} = \frac{y - d - ac}{c(b - a)} = \frac{y - (ac+d)}{(bc+d) - (ac+d)} = \frac{y - \alpha}{\beta - \alpha} $$

La fonction de répartition $F_Y(y)$ est de la forme $\frac{y-\alpha}{\beta-\alpha}$ sur l'intervalle $[\alpha, \beta]$, $0$ avant et $1$ après. Ceci est exactement la définition de la fonction de répartition d'une variable aléatoire de loi uniforme sur le segment $[\alpha, \beta]$.
On conclut que $Y$ suit une loi uniforme sur $[ac+d, bc+d]$. $\blacksquare$

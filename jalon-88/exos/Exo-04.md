# Exercice 04 : Covariance nulle n'implique pas indépendance
Difficulté : $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire suivant une loi uniforme sur $\{-1, 0, 1\}$.
Soit $Y = |X|$.
1. Donner la loi de $Y$.
2. Calculer $\mathbb{E}[X]$, $\mathbb{E}[Y]$ et $\mathbb{E}[XY]$.
3. En déduire la covariance de $X$ et $Y$.
4. $X$ et $Y$ sont-elles indépendantes ?

**Correction :**
1. $Y$ prend ses valeurs dans $\{0, 1\}$.
$\mathbb{P}(Y = 0) = \mathbb{P}(X = 0) = \frac{1}{3}$.
$\mathbb{P}(Y = 1) = \mathbb{P}(X = -1) + \mathbb{P}(X = 1) = \frac{2}{3}$.
2. $\mathbb{E}[X] = \frac{1}{3}(-1) + \frac{1}{3}(0) + \frac{1}{3}(1) = 0$.
$\mathbb{E}[Y] = \frac{1}{3}(0) + \frac{2}{3}(1) = \frac{2}{3}$.
Calculons $XY$. Puisque $Y = |X|$, on a $XY = X|X|$.
Si $X=-1, XY=-1$. Si $X=0, XY=0$. Si $X=1, XY=1$.
Donc $XY = X$. Ainsi $\mathbb{E}[XY] = \mathbb{E}[X] = 0$.
3. $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] = 0 - 0 \times \frac{2}{3} = 0$.
4. Testons l'indépendance avec un événement spécifique :
$\mathbb{P}(X = 0 \text{ et } Y = 1) = \mathbb{P}(\emptyset) = 0$.
Or, $\mathbb{P}(X=0)\mathbb{P}(Y=1) = \frac{1}{3} \times \frac{2}{3} = \frac{2}{9}$.
Puisque $0 \neq \frac{2}{9}$, $X$ et $Y$ ne sont pas indépendantes.

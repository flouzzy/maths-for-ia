# Exercice 10 : Transformation d'un vecteur gaussien par une isométrie \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $\mathbf{X} = (X_1, X_2)^\top$ un vecteur aléatoire composé de variables aléatoires indépendantes $X_1, X_2 \sim \mathcal{N}(0,1)$.
Soit $R_\theta$ la matrice de rotation plane d'angle $\theta \in \mathbb{R}$ :
$$ R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $$
On définit le vecteur aléatoire $\mathbf{Y} = R_\theta \mathbf{X}$.
Démontrer, en utilisant le théorème du changement de variable pour les densités, que les composantes de $\mathbf{Y}$ sont des variables normales centrées réduites indépendantes.

## Correction

La densité conjointe du vecteur aléatoire $\mathbf{X} = (X_1, X_2)^\top$ est donnée par le produit de ses lois marginales puisque les composantes sont indépendantes :
$$ f_\mathbf{X}(x_1, x_2) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x_1^2}{2}} \frac{1}{\sqrt{2\pi}} e^{-\frac{x_2^2}{2}} = \frac{1}{2\pi} e^{-\frac{x_1^2 + x_2^2}{2}} $$
En notation vectorielle, l'argument de l'exponentielle s'écrit avec la norme euclidienne $||\mathbf{x}||^2 = x_1^2 + x_2^2 = \mathbf{x}^\top \mathbf{x}$ :
$$ f_\mathbf{X}(\mathbf{x}) = \frac{1}{2\pi} e^{-\frac{1}{2}||\mathbf{x}||^2} $$

Soit $\phi(\mathbf{x}) = R_\theta \mathbf{x}$. L'application $\phi$ est une application linéaire de $\mathbb{R}^2$ dans $\mathbb{R}^2$. Son jacobien est la matrice $R_\theta$ elle-même.
Calculons le déterminant de ce jacobien :
$$ J = \det(R_\theta) = (\cos\theta)(\cos\theta) - (-\sin\theta)(\sin\theta) = \cos^2\theta + \sin^2\theta = 1 $$
Le jacobien étant non nul (et valant 1), l'application est un difféomorphisme.
Le théorème du changement de variable pour les densités énonce que la densité du vecteur transformé $\mathbf{Y} = \phi(\mathbf{X})$ s'écrit :
$$ f_\mathbf{Y}(\mathbf{y}) = f_\mathbf{X}(\phi^{-1}(\mathbf{y})) \cdot \frac{1}{|\det J_{\phi^{-1}}(\mathbf{y})|} $$
L'inverse de la matrice de rotation $R_\theta$ est la matrice de rotation d'angle $-\theta$, soit $R_{-\theta} = R_\theta^\top$.
Ainsi, $\phi^{-1}(\mathbf{y}) = R_\theta^\top \mathbf{y}$. Le jacobien de l'inverse est $\det(R_\theta^\top) = 1$. L'expression de la densité devient :
$$ f_\mathbf{Y}(\mathbf{y}) = f_\mathbf{X}(R_\theta^\top \mathbf{y}) \cdot 1 $$
Remplaçons dans la formule de la densité de $\mathbf{X}$ :
$$ f_\mathbf{Y}(\mathbf{y}) = \frac{1}{2\pi} e^{-\frac{1}{2}||R_\theta^\top \mathbf{y}||^2} $$
Il faut maintenant évaluer la norme au carré du vecteur transformé. Par propriété du produit scalaire et des matrices transposées :
$$ ||R_\theta^\top \mathbf{y}||^2 = (R_\theta^\top \mathbf{y})^\top (R_\theta^\top \mathbf{y}) = (\mathbf{y}^\top (R_\theta^\top)^\top) (R_\theta^\top \mathbf{y}) = \mathbf{y}^\top R_\theta R_\theta^\top \mathbf{y} $$
Une matrice de rotation est orthogonale, ce qui signifie que $R_\theta R_\theta^\top = I_2$, la matrice identité de taille 2.
On a donc la propriété géométrique fondamentale des isométries (elles conservent la norme) :
$$ ||R_\theta^\top \mathbf{y}||^2 = \mathbf{y}^\top I_2 \mathbf{y} = \mathbf{y}^\top \mathbf{y} = ||\mathbf{y}||^2 = y_1^2 + y_2^2 $$
En substituant ce résultat dans la densité de $\mathbf{Y}$, on obtient :
$$ f_\mathbf{Y}(\mathbf{y}) = \frac{1}{2\pi} e^{-\frac{1}{2}(y_1^2 + y_2^2)} = \left(\frac{1}{\sqrt{2\pi}} e^{-\frac{y_1^2}{2}}\right) \left(\frac{1}{\sqrt{2\pi}} e^{-\frac{y_2^2}{2}}\right) $$
La densité du vecteur aléatoire $\mathbf{Y}$ s'écrit comme le produit de deux densités de la loi normale centrée réduite $\mathcal{N}(0,1)$.
Ceci démontre simultanément que $Y_1 \sim \mathcal{N}(0,1)$, $Y_2 \sim \mathcal{N}(0,1)$, et que les composantes $Y_1$ et $Y_2$ sont mutuellement indépendantes. Ce résultat illustre l'isotropie de la loi normale multidimensionnelle standard. $\blacksquare$

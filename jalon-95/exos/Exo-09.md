# Exercice 9
## Énoncé $\bigstar\bigstar\bigstar\bigstar\bigstar$
Soit $X_1, X_2, X_3$ des variables aléatoires i.i.d. de loi $\mathcal{N}(0, 1)$.
On pose $Y_1 = X_1 + X_2 + X_3$, $Y_2 = X_1 - X_2$, et $Y_3 = X_1 + X_2 - 2X_3$.
1. Montrer que $Y = (Y_1, Y_2, Y_3)^T$ est un vecteur gaussien et déterminer sa loi.
2. Les variables $Y_1, Y_2, Y_3$ sont-elles indépendantes ?
3. En déduire la loi de $Z = Y_2^2 + \frac{1}{3} Y_3^2$.

## Correction

1. Le vecteur $Y$ s'écrit $Y = A X$ où $X = (X_1, X_2, X_3)^T$ et $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 1 & -2 \end{pmatrix}$.
Puisque $X_1, X_2, X_3$ sont i.i.d. de loi $\mathcal{N}(0, 1)$, $X$ est un vecteur gaussien standard, $X \sim \mathcal{N}(0, I_3)$.
Étant une transformation linéaire d'un vecteur gaussien, $Y$ est un vecteur gaussien.
Son espérance est $\mathbb{E}[Y] = A \mathbb{E}[X] = 0$.
Sa matrice de covariance est $\Sigma_Y = A \Sigma_X A^T = A I_3 A^T = A A^T$.
Calculons $A A^T$ :
$\Sigma_Y = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 1 & -2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 0 & -2 \end{pmatrix} = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 6 \end{pmatrix}$.
Donc $Y \sim \mathcal{N}(0, \text{diag}(3, 2, 6))$.

2. La matrice de covariance $\Sigma_Y$ est diagonale. Les composantes du vecteur gaussien $Y$ sont donc non corrélées.
Par propriété des vecteurs gaussiens, des composantes non corrélées sont indépendantes.
Donc $Y_1, Y_2, Y_3$ sont indépendantes.

3. Nous savons que $Y_2 \sim \mathcal{N}(0, 2)$, donc $\frac{Y_2}{\sqrt{2}} \sim \mathcal{N}(0, 1)$.
De même, $Y_3 \sim \mathcal{N}(0, 6)$, donc $\frac{Y_3}{\sqrt{6}} \sim \mathcal{N}(0, 1)$.
Posons $U = \frac{Y_2}{\sqrt{2}}$ et $V = \frac{Y_3}{\sqrt{6}}$. $U$ et $V$ sont des gaussiennes standards indépendantes (car $Y_2$ et $Y_3$ le sont).
On a $Z = Y_2^2 + \frac{1}{3} Y_3^2 = 2 (\frac{Y_2}{\sqrt{2}})^2 + 2 (\frac{Y_3}{\sqrt{6}})^2 = 2 U^2 + 2 V^2 = 2(U^2 + V^2)$.
Par définition, la somme des carrés de deux gaussiennes standards indépendantes suit une loi du Khi-deux à 2 degrés de liberté, $\chi^2(2)$, qui est aussi une loi exponentielle $\mathcal{E}(1/2)$.
Donc $\frac{Z}{2} \sim \chi^2(2)$.
La fonction caractéristique de $\chi^2(2)$ est $\phi(t) = (1 - 2it)^{-1}$.
Celle de $Z$ est $\phi_Z(t) = \mathbb{E}[e^{it (2 \frac{Z}{2})}] = \phi_{\chi^2(2)}(2t) = (1 - 4it)^{-1}$.
C'est la fonction caractéristique d'une loi Exponentielle de paramètre $\lambda = 1/4$ (ou d'une Gamma(1, 4)).
Donc $Z$ suit une loi Exponentielle de paramètre $1/4$.

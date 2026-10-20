# Exercice 8
## Énoncé $\bigstar\bigstar\bigstar\bigstar\star$
Soit $X = (X_1, X_2)^T$ un vecteur gaussien centré de matrice de covariance $\Sigma = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
1. Déterminer une matrice orthogonale $P$ et une matrice diagonale $D$ telles que $\Sigma = P D P^T$.
2. En déduire un vecteur gaussien $Y = (Y_1, Y_2)^T$ à composantes indépendantes tel que $X = P Y$.
3. Calculer $\mathbb{E}[X_1^2 X_2^2]$.

## Correction

1. Cherchons les valeurs propres de $\Sigma$. Le polynôme caractéristique est :
$\chi_\Sigma(\lambda) = \det(\Sigma - \lambda I) = \det\begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3)$.
Les valeurs propres sont $\lambda_1 = 3$ et $\lambda_2 = 1$.
Cherchons les sous-espaces propres.
Pour $\lambda_1 = 3$ : $\Sigma - 3I = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$. Un vecteur propre est $v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. On le normalise : $u_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Pour $\lambda_2 = 1$ : $\Sigma - I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. Un vecteur propre est $v_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$. On le normalise : $u_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
La matrice $P$ est donc $P = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$, et $D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$. On a bien $P P^T = I$ et $\Sigma = P D P^T$.

2. Soit $Y = P^T X$. Puisque $X$ est gaussien et que $P^T$ est une matrice déterministe, $Y$ est un vecteur gaussien.
Son espérance est $\mathbb{E}[Y] = P^T \mathbb{E}[X] = 0$.
Sa matrice de covariance est $\text{Cov}(Y) = P^T \text{Cov}(X) P = P^T \Sigma P = P^T (P D P^T) P = D$.
Puisque $D$ est diagonale, les composantes $Y_1$ et $Y_2$ sont non corrélées. Étant conjointement gaussiennes, elles sont indépendantes. $Y_1 \sim \mathcal{N}(0, 3)$ et $Y_2 \sim \mathcal{N}(0, 1)$. De plus, $X = (P^T)^{-1} Y = P Y$.

3. On a $X_1 = \frac{1}{\sqrt{2}}(Y_1 - Y_2)$ et $X_2 = \frac{1}{\sqrt{2}}(Y_1 + Y_2)$.
On cherche $\mathbb{E}[X_1^2 X_2^2] = \mathbb{E}[\frac{1}{4}(Y_1 - Y_2)^2 (Y_1 + Y_2)^2] = \frac{1}{4}\mathbb{E}[(Y_1^2 - Y_2^2)^2] = \frac{1}{4}\mathbb{E}[Y_1^4 - 2Y_1^2 Y_2^2 + Y_2^4]$.
Par indépendance de $Y_1$ et $Y_2$, on a $\mathbb{E}[Y_1^2 Y_2^2] = \mathbb{E}[Y_1^2]\mathbb{E}[Y_2^2] = 3 \times 1 = 3$.
Pour une variable gaussienne centrée $Z \sim \mathcal{N}(0, \sigma^2)$, on a $\mathbb{E}[Z^4] = 3\sigma^4$.
Donc $\mathbb{E}[Y_1^4] = 3 \times 3^2 = 27$ et $\mathbb{E}[Y_2^4] = 3 \times 1^2 = 3$.
Ainsi, $\mathbb{E}[X_1^2 X_2^2] = \frac{1}{4}(27 - 2(3) + 3) = \frac{1}{4}(30 - 6) = \frac{24}{4} = 6$.

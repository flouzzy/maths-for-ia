# Exercice 10
## Énoncé $\bigstar\bigstar\bigstar\bigstar\bigstar$
Soit $X$ un vecteur gaussien de $\mathbb{R}^n$, de loi $\mathcal{N}(\mu, \Sigma)$ avec $\Sigma$ inversible.
On considère la forme quadratique $Q(X) = (X-\mu)^T \Sigma^{-1} (X-\mu)$.
Montrer rigoureusement que $Q(X)$ suit une loi du $\chi^2$ à $n$ degrés de liberté, et calculer son espérance et sa variance.

## Correction

Puisque $\Sigma$ est une matrice de covariance, elle est symétrique et positive. Comme elle est inversible, elle est définie positive.
Il existe donc une matrice symétrique définie positive $\Sigma^{1/2}$ telle que $(\Sigma^{1/2})^2 = \Sigma$.
Posons $Y = \Sigma^{-1/2} (X - \mu)$, où $\Sigma^{-1/2} = (\Sigma^{1/2})^{-1}$.
$Y$ est obtenu par transformation affine du vecteur gaussien $X$, donc $Y$ est un vecteur gaussien.
Son espérance est $\mathbb{E}[Y] = \Sigma^{-1/2}(\mathbb{E}[X] - \mu) = \Sigma^{-1/2}(\mu - \mu) = 0$.
Sa matrice de covariance est $\text{Cov}(Y) = \Sigma^{-1/2} \text{Cov}(X) (\Sigma^{-1/2})^T = \Sigma^{-1/2} \Sigma \Sigma^{-1/2}$.
Puisque $\Sigma = \Sigma^{1/2} \Sigma^{1/2}$, on a $\text{Cov}(Y) = \Sigma^{-1/2} \Sigma^{1/2} \Sigma^{1/2} \Sigma^{-1/2} = I_n$.
Ainsi, $Y$ est un vecteur gaussien standard de $\mathbb{R}^n$ : $Y = (Y_1, \dots, Y_n)^T$ où les $Y_i$ sont i.i.d. de loi $\mathcal{N}(0, 1)$.

Reprenons l'expression de $Q(X)$ :
$Q(X) = (X-\mu)^T \Sigma^{-1} (X-\mu) = (X-\mu)^T \Sigma^{-1/2} \Sigma^{-1/2} (X-\mu)$.
Puisque $\Sigma^{-1/2}$ est symétrique, $(\Sigma^{-1/2})^T = \Sigma^{-1/2}$, donc :
$Q(X) = (\Sigma^{-1/2} (X-\mu))^T (\Sigma^{-1/2} (X-\mu)) = Y^T Y$.
En développant le produit scalaire, on obtient :
$Q(X) = \sum_{i=1}^n Y_i^2$.
C'est la somme de $n$ carrés de variables aléatoires de loi normale centrée réduite indépendantes.
Par définition de la loi du $\chi^2$, la somme des carrés de $n$ variables $\mathcal{N}(0, 1)$ indépendantes suit une loi du $\chi^2$ à $n$ degrés de liberté.
Donc $Q(X) \sim \chi^2(n)$.

Calculons son espérance :
$\mathbb{E}[Q(X)] = \mathbb{E}[\sum_{i=1}^n Y_i^2] = \sum_{i=1}^n \mathbb{E}[Y_i^2]$.
Comme $Y_i \sim \mathcal{N}(0, 1)$, on a $\mathbb{E}[Y_i^2] = \text{Var}(Y_i) + (\mathbb{E}[Y_i])^2 = 1 + 0 = 1$.
Donc $\mathbb{E}[Q(X)] = n \times 1 = n$.

Calculons sa variance. Par indépendance des $Y_i$ (donc des $Y_i^2$) :
$\text{Var}(Q(X)) = \text{Var}(\sum_{i=1}^n Y_i^2) = \sum_{i=1}^n \text{Var}(Y_i^2)$.
Pour calculer $\text{Var}(Y_i^2)$, on utilise $\text{Var}(Y_i^2) = \mathbb{E}[Y_i^4] - (\mathbb{E}[Y_i^2])^2$.
On a vu que $\mathbb{E}[Y_i^2] = 1$.
De plus, le moment d'ordre 4 d'une variable normale centrée réduite est $\mathbb{E}[Y_i^4] = 3$.
Donc $\text{Var}(Y_i^2) = 3 - 1^2 = 2$.
Ainsi, $\text{Var}(Q(X)) = \sum_{i=1}^n 2 = 2n$.

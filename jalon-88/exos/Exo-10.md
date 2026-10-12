# Exercice 10 : Matrices de covariance et indépendance \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**

Soit $V = (X, Y)^T$ un vecteur aléatoire gaussien de dimension 2. Son espérance est le vecteur nul $\mu = (0, 0)^T$ et sa matrice de covariance est $\Sigma$.
Démontrer rigoureusement que si la covariance $\text{Cov}(X,Y)$ est nulle (matrice $\Sigma$ diagonale), alors les variables aléatoires $X$ et $Y$ sont indépendantes.
(Rappel : La densité d'un vecteur gaussien centré non dégénéré est $f(v) = \frac{1}{2\pi \sqrt{\det(\Sigma)}} \exp\left(-\frac{1}{2} v^T \Sigma^{-1} v\right)$).

**Correction Détaillée :**

1. Soit $\Sigma$ la matrice de covariance du vecteur gaussien $V = (X, Y)^T$. Par définition :
   $$ \Sigma = \begin{pmatrix} \text{Var}(X) & \text{Cov}(X,Y) \\ \text{Cov}(X,Y) & \text{Var}(Y) \end{pmatrix} = \begin{pmatrix} \sigma_X^2 & \sigma_{XY} \\ \sigma_{XY} & \sigma_Y^2 \end{pmatrix} $$
2. L'hypothèse indique que la covariance est nulle, soit $\sigma_{XY} = 0$. La matrice $\Sigma$ est donc diagonale :
   $$ \Sigma = \begin{pmatrix} \sigma_X^2 & 0 \\ 0 & \sigma_Y^2 \end{pmatrix} $$
3. Pour utiliser la fonction de densité du vecteur, nous devons calculer le déterminant et l'inverse de la matrice $\Sigma$.
   - Le déterminant d'une matrice diagonale est le produit de ses éléments diagonaux :
     $$ \det(\Sigma) = \sigma_X^2 \sigma_Y^2 $$
   - L'inverse d'une matrice diagonale inversible s'obtient en inversant ses éléments diagonaux :
     $$ \Sigma^{-1} = \begin{pmatrix} \frac{1}{\sigma_X^2} & 0 \\ 0 & \frac{1}{\sigma_Y^2} \end{pmatrix} $$
4. Explicitons le terme exponentiel dans la fonction de densité, c'est-à-dire la forme quadratique $v^T \Sigma^{-1} v$ avec $v = (x, y)^T$ :
   $$ v^T \Sigma^{-1} v = \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} \frac{1}{\sigma_X^2} & 0 \\ 0 & \frac{1}{\sigma_Y^2} \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} $$
5. En effectuant la multiplication matricielle :
   $$ = \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} \frac{x}{\sigma_X^2} \\ \frac{y}{\sigma_Y^2} \end{pmatrix} = \frac{x^2}{\sigma_X^2} + \frac{y^2}{\sigma_Y^2} $$
6. Remplaçons ces résultats dans l'expression générale de la densité jointe du vecteur gaussien $f_{X,Y}(x,y)$ :
   $$ f_{X,Y}(x,y) = \frac{1}{2\pi \sqrt{\sigma_X^2 \sigma_Y^2}} \exp\left(-\frac{1}{2} \left( \frac{x^2}{\sigma_X^2} + \frac{y^2}{\sigma_Y^2} \right) \right) $$
7. Utilisons les propriétés algébriques des racines carrées et de la fonction exponentielle :
   - Le dénominateur se sépare : $2\pi \sqrt{\sigma_X^2 \sigma_Y^2} = (\sqrt{2\pi} \sigma_X) (\sqrt{2\pi} \sigma_Y)$.
   - L'exponentielle d'une somme se transforme en produit : $\exp(A + B) = \exp(A)\exp(B)$.
8. La densité jointe se réécrit donc sous la forme factorisée suivante :
   $$ f_{X,Y}(x,y) = \left( \frac{1}{\sqrt{2\pi \sigma_X^2}} \exp\left(-\frac{x^2}{2\sigma_X^2}\right) \right) \cdot \left( \frac{1}{\sqrt{2\pi \sigma_Y^2}} \exp\left(-\frac{y^2}{2\sigma_Y^2}\right) \right) $$
9. On identifie immédiatement dans les deux facteurs les densités marginales $f_X(x)$ d'une loi $\mathcal{N}(0, \sigma_X^2)$ et $f_Y(y)$ d'une loi $\mathcal{N}(0, \sigma_Y^2)$.
   L'égalité s'écrit donc : $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ pour tout couple $(x,y) \in \mathbb{R}^2$.
10. La factorisation parfaite de la densité jointe en le produit des densités marginales est la condition nécessaire et suffisante d'indépendance pour des variables aléatoires continues.
11. **Conclusion :** Pour des variables aléatoires conjointement gaussiennes, une covariance nulle (décorrélation) implique rigoureusement l'indépendance mathématique totale. C'est une propriété exceptionnelle de la géométrie de la loi normale.

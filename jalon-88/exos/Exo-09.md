# Exercice 09 : Indépendance des vecteurs gaussiens et matrice de covariance diagonale
Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X, Y)$ un vecteur gaussien centré, de matrice de covariance $\Sigma = \begin{pmatrix} \sigma_X^2 & c \\ c & \sigma_Y^2 \end{pmatrix}$.
Montrer que si $\text{Cov}(X,Y) = c = 0$, alors $X$ et $Y$ sont indépendantes.

**Correction :**
1. La densité conjointe d'un vecteur gaussien non dégénéré de dimension $2$ est :
$f_{X,Y}(x,y) = \frac{1}{2\pi \sqrt{\det(\Sigma)}} \exp\left( -\frac{1}{2} (x, y) \Sigma^{-1} \begin{pmatrix} x \\ y \end{pmatrix} \right)$.
2. Si $c = 0$, la matrice est diagonale : $\Sigma = \begin{pmatrix} \sigma_X^2 & 0 \\ 0 & \sigma_Y^2 \end{pmatrix}$.
Le déterminant est $\det(\Sigma) = \sigma_X^2 \sigma_Y^2$. L'inverse est $\Sigma^{-1} = \begin{pmatrix} \frac{1}{\sigma_X^2} & 0 \\ 0 & \frac{1}{\sigma_Y^2} \end{pmatrix}$.
3. Évaluons le terme dans l'exponentielle :
$(x, y) \Sigma^{-1} \begin{pmatrix} x \\ y \end{pmatrix} = (x, y) \begin{pmatrix} \frac{x}{\sigma_X^2} \\ \frac{y}{\sigma_Y^2} \end{pmatrix} = \frac{x^2}{\sigma_X^2} + \frac{y^2}{\sigma_Y^2}$.
4. On remplace dans la densité conjointe :
$f_{X,Y}(x,y) = \frac{1}{2\pi \sigma_X \sigma_Y} \exp\left( -\frac{1}{2} \left( \frac{x^2}{\sigma_X^2} + \frac{y^2}{\sigma_Y^2} \right) \right)$.
5. Grâce à la propriété de l'exponentielle $\exp(a+b) = \exp(a)\exp(b)$, on peut séparer les variables :
$f_{X,Y}(x,y) = \left( \frac{1}{\sqrt{2\pi}\sigma_X} e^{-\frac{x^2}{2\sigma_X^2}} \right) \times \left( \frac{1}{\sqrt{2\pi}\sigma_Y} e^{-\frac{y^2}{2\sigma_Y^2}} \right)$.
6. On reconnaît $f_{X,Y}(x,y) = f_X(x) f_Y(y)$ où $f_X$ et $f_Y$ sont les densités marginales de $X$ et $Y$.
La densité conjointe s'écrivant comme le produit des densités marginales, les variables $X$ et $Y$ sont mutuellement indépendantes.
*(Note : Ce résultat est très spécifique aux variables gaussiennes. Pour des variables quelconques, l'absence de covariance n'implique pas l'indépendance, voir Exercice 4).*

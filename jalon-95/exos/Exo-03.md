# Exercice 3 ($\bigstar\bigstar\star\star\star$)

\textbf{Titre : Prédiction Linéaire Optimale d'une Variable Gaussienne Conditionnellement à des Observations Multiples}

Soit un vecteur gaussien $Z = \begin{pmatrix} X \\ Y_1 \\ Y_2 \end{pmatrix}$ de dimension $3$, où $X$ est une variable aléatoire réelle et $Y = \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix}$ est un vecteur aléatoire réel de dimension $2$.
On suppose que $Z$ suit une loi normale multivariée $\mathcal{N}(\mu, \Sigma)$ avec :
$$
\mu = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \quad \text{et} \quad \Sigma = \begin{pmatrix}
4 & 1 & 2 \\
1 & 2 & 1 \\
2 & 1 & 3
\end{pmatrix}
$$
On observe le vecteur $Y$ et on souhaite prédire la valeur de $X$.

**Questions :**
1. Déterminez les matrices de partition $\mu_X$, $\mu_Y$, $\Sigma_{XX}$, $\Sigma_{XY}$, $\Sigma_{YX}$ et $\Sigma_{YY}$ correspondant à la partition de $Z$ en $X$ et $Y$.
2. Calculez l'inverse de la matrice $\Sigma_{YY}$.
3. Pour une observation $y = \begin{pmatrix} 4 \\ 5 \end{pmatrix}$, calculez l'espérance conditionnelle $\mathbb{E}[X|Y=y]$.
4. Calculez la variance conditionnelle $\text{Var}(X|Y=y)$.

---

## Solution de l'Exercice 3

### Question 1 : Détermination des matrices de partition

Le vecteur $Z$ est partitionné en $X$ (la première composante, scalaire) et $Y = (Y_1, Y_2)^T$ (les deux dernières composantes, vecteur).
Ainsi, nous avons $Z = \begin{pmatrix} X \\ Y \end{pmatrix}$.

Le vecteur de moyennes $\mu$ est partitionné de la même manière :
$$
\mu = \begin{pmatrix} \mu_X \\ \mu_Y \end{pmatrix}
$$
En identifiant avec le vecteur $\mu$ donné dans l'énoncé :
$$
\mu_X = 1
$$
$$
\mu_Y = \begin{pmatrix} 2 \\ 3 \end{pmatrix}
$$

La matrice de covariance $\Sigma$ est partitionnée comme suit :
$$
\Sigma = \begin{pmatrix}
\Sigma_{XX} & \Sigma_{XY} \\
\Sigma_{YX} & \Sigma_{YY}
\end{pmatrix}
$$
En identifiant avec la matrice $\Sigma$ donnée dans l'énoncé :
$$
\Sigma_{XX} = 4 \quad \text{(matrice de taille 1x1, ou simplement un scalaire)}
$$
$$
\Sigma_{XY} = \begin{pmatrix} 1 & 2 \end{pmatrix} \quad \text{(matrice de taille 1x2)}
$$
$$
\Sigma_{YX} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \quad \text{(matrice de taille 2x1)}
$$
$$
\Sigma_{YY} = \begin{pmatrix}
2 & 1 \\
1 & 3
\end{pmatrix} \quad \text{(matrice de taille 2x2)}
$$

### Question 2 : Calcul de l'inverse de la matrice $\Sigma_{YY}$

Nous devons calculer l'inverse de la matrice $\Sigma_{YY} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$.

Pour une matrice carrée d'ordre 2, $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, son inverse $A^{-1}$ est donnée par la formule :
$$
A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$
où $\det(A)$ est le déterminant de $A$, calculé comme $ad - bc$.

Calculons d'abord le déterminant de $\Sigma_{YY}$ :
$$
\det(\Sigma_{YY}) = (2)(3) - (1)(1) = 6 - 1 = 5
$$
Puisque le déterminant est non nul (ici, 5), la matrice $\Sigma_{YY}$ est inversible.

Appliquons la formule pour trouver $\Sigma_{YY}^{-1}$ :
$$
\Sigma_{YY}^{-1} = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}
$$
En distribuant le facteur $\frac{1}{5}$ à chaque élément de la matrice :
$$
\Sigma_{YY}^{-1} = \begin{pmatrix}
\frac{3}{5} & -\frac{1}{5} \\
-\frac{1}{5} & \frac{2}{5}
\end{pmatrix}
$$

### Question 3 : Calcul de l'espérance conditionnelle $\mathbb{E}[X|Y=y]$

L'espérance conditionnelle $\mathbb{E}[X|Y=y]$ pour un vecteur gaussien est donnée par la formule générale :
$$
\mathbb{E}[X|Y=y] = \mu_X + \Sigma_{XY} \Sigma_{YY}^{-1} (y - \mu_Y)
$$
Nous avons identifié les composants suivants :
$\mu_X = 1$
$\mu_Y = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$
$\Sigma_{XY} = \begin{pmatrix} 1 & 2 \end{pmatrix}$
$\Sigma_{YY}^{-1} = \begin{pmatrix} \frac{3}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{pmatrix}$
L'observation $y$ est donnée comme $y = \begin{pmatrix} 4 \\ 5 \end{pmatrix}$.

Calculons le terme $(y - \mu_Y)$ :
$$
y - \mu_Y = \begin{pmatrix} 4 \\ 5 \end{pmatrix} - \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 4 - 2 \\ 5 - 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \end{pmatrix}
$$

Ensuite, calculons le produit matriciel $\Sigma_{YY}^{-1} (y - \mu_Y)$ :
$$
\Sigma_{YY}^{-1} (y - \mu_Y) = \begin{pmatrix} \frac{3}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{pmatrix} \begin{pmatrix} 2 \\ 2 \end{pmatrix}
$$
$$
= \begin{pmatrix}
(\frac{3}{5})(2) + (-\frac{1}{5})(2) \\
(-\frac{1}{5})(2) + (\frac{2}{5})(2)
\end{pmatrix}
= \begin{pmatrix}
\frac{6}{5} - \frac{2}{5} \\
-\frac{2}{5} + \frac{4}{5}
\end{pmatrix}
= \begin{pmatrix}
\frac{4}{5} \\
\frac{2}{5}
\end{pmatrix}
$$

Maintenant, calculons le produit matriciel $\Sigma_{XY} (\Sigma_{YY}^{-1} (y - \mu_Y))$ :
$$
\Sigma_{XY} (\Sigma_{YY}^{-1} (y - \mu_Y)) = \begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} \frac{4}{5} \\ \frac{2}{5} \end{pmatrix}
$$
Ce produit est un scalaire car $\Sigma_{XY}$ est de taille 1x2 et le vecteur résultant est de taille 2x1.
$$
= (1)\left(\frac{4}{5}\right) + (2)\left(\frac{2}{5}\right) = \frac{4}{5} + \frac{4}{5} = \frac{8}{5}
$$

Enfin, ajoutons $\mu_X$ pour obtenir l'espérance conditionnelle :
$$
\mathbb{E}[X|Y=y] = \mu_X + \Sigma_{XY} \Sigma_{YY}^{-1} (y - \mu_Y) = 1 + \frac{8}{5}
$$
Pour additionner, nous mettons 1 sous forme de fraction avec un dénominateur de 5 :
$$
\mathbb{E}[X|Y=y] = \frac{5}{5} + \frac{8}{5} = \frac{13}{5}
$$
Ainsi, l'espérance conditionnelle est $\mathbb{E}[X|Y=y] = \frac{13}{5}$, ou $2.6$.

### Question 4 : Calcul de la variance conditionnelle $\text{Var}(X|Y=y)$

La variance conditionnelle $\text{Var}(X|Y=y)$ pour un vecteur gaussien est donnée par la formule :
$$
\text{Var}(X|Y=y) = \Sigma_{XX} - \Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX}
$$
Notez que, pour les vecteurs gaussiens, la variance conditionnelle ne dépend pas de la valeur spécifique de l'observation $y$.

Nous avons les composants suivants :
$\Sigma_{XX} = 4$
$\Sigma_{XY} = \begin{pmatrix} 1 & 2 \end{pmatrix}$
$\Sigma_{YY}^{-1} = \begin{pmatrix} \frac{3}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{pmatrix}$
$\Sigma_{YX} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

Commençons par calculer le produit matriciel $\Sigma_{XY} \Sigma_{YY}^{-1}$ :
$$
\Sigma_{XY} \Sigma_{YY}^{-1} = \begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} \frac{3}{5} & -\frac{1}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{pmatrix}
$$
Ce produit est une matrice de taille 1x2.
$$
= \begin{pmatrix}
(1)(\frac{3}{5}) + (2)(-\frac{1}{5}) & (1)(-\frac{1}{5}) + (2)(\frac{2}{5})
\end{pmatrix}
$$
$$
= \begin{pmatrix}
\frac{3}{5} - \frac{2}{5} & -\frac{1}{5} + \frac{4}{5}
\end{pmatrix}
= \begin{pmatrix} \frac{1}{5} & \frac{3}{5} \end{pmatrix}
$$

Ensuite, calculons le produit matriciel $(\Sigma_{XY} \Sigma_{YY}^{-1}) \Sigma_{YX}$ :
$$
(\Sigma_{XY} \Sigma_{YY}^{-1}) \Sigma_{YX} = \begin{pmatrix} \frac{1}{5} & \frac{3}{5} \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$
Ce produit est un scalaire car le premier terme est de taille 1x2 et le second est de taille 2x1.
$$
= \left(\frac{1}{5}\right)(1) + \left(\frac{3}{5}\right)(2) = \frac{1}{5} + \frac{6}{5} = \frac{7}{5}
$$

Enfin, soustrayons ce résultat de $\Sigma_{XX}$ pour obtenir la variance conditionnelle :
$$
\text{Var}(X|Y=y) = \Sigma_{XX} - (\Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX}) = 4 - \frac{7}{5}
$$
Pour soustraire, nous mettons 4 sous forme de fraction avec un dénominateur de 5 :
$$
\text{Var}(X|Y=y) = \frac{20}{5} - \frac{7}{5} = \frac{13}{5}
$$
Ainsi, la variance conditionnelle est $\text{Var}(X|Y=y) = \frac{13}{5}$, ou $2.6$.
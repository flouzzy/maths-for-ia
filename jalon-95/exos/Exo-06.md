# Exercice 6 $\bigstar\bigstar\bigstar\star\star$

**Jalon 95 : Vecteurs Gaussiens**

### Énoncé

Soit un vecteur gaussien $Z \in \mathbb{R}^4$ partitionné en deux sous-vecteurs $X \in \mathbb{R}^2$ et $Y \in \mathbb{R}^2$ comme suit :
$$ Z = \begin{pmatrix} X_1 \\ X_2 \\ Y_1 \\ Y_2 \end{pmatrix} = \begin{pmatrix} X \\ Y \end{pmatrix} $$
Le vecteur $Z$ suit une distribution normale multivariée $\mathcal{N}(\mu, \Sigma)$ avec :
$$ \mu = \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix} $$
et la matrice de covariance $\Sigma$ est donnée par :
$$ \Sigma = \begin{pmatrix}
2 & 0.5 & 0.8 & 0.2 \\
0.5 & 3 & 0.3 & 0.7 \\
0.8 & 0.3 & 4 & 1 \\
0.2 & 0.7 & 1 & 5
\end{pmatrix} $$
On observe une réalisation du vecteur $Y$, notée $y$, telle que :
$$ y = \begin{pmatrix} 3.5 \\ 4.5 \end{pmatrix} $$
Votre tâche est de calculer l'espérance conditionnelle $\mathbb{E}[X|Y=y]$ et la matrice de covariance conditionnelle $\text{Var}(X|Y=y)$. Tous les calculs matriciels doivent être détaillés explicitement, sans aucune ellipse.

---

### Solution

Pour un vecteur gaussien $Z = \begin{pmatrix} X \\ Y \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} \mu_X \\ \mu_Y \end{pmatrix}, \begin{pmatrix} \Sigma_{XX} & \Sigma_{XY} \\ \Sigma_{YX} & \Sigma_{YY} \end{pmatrix}\right)$, l'espérance conditionnelle de $X$ sachant $Y=y$ et la matrice de covariance conditionnelle de $X$ sachant $Y=y$ sont données par les formules suivantes :

1.  $\mathbb{E}[X|Y=y] = \mu_X + \Sigma_{XY} \Sigma_{YY}^{-1} (y - \mu_Y)$
2.  $\text{Var}(X|Y=y) = \Sigma_{XX} - \Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX}$

Nous allons procéder par étapes pour calculer ces quantités, en détaillant chaque opération.

#### Étape 1 : Extraction des sous-matrices et sous-vecteurs

À partir des données de l'énoncé, nous identifions les composantes partitionnées :

$$ \mu_X = \begin{pmatrix} 1 \\ 2 \end{pmatrix} $$
$$ \mu_Y = \begin{pmatrix} 3 \\ 4 \end{pmatrix} $$
$$ \Sigma_{XX} = \begin{pmatrix} 2 & 0.5 \\ 0.5 & 3 \end{pmatrix} $$
$$ \Sigma_{XY} = \begin{pmatrix} 0.8 & 0.2 \\ 0.3 & 0.7 \end{pmatrix} $$
$$ \Sigma_{YX} = \Sigma_{XY}^T = \begin{pmatrix} 0.8 & 0.3 \\ 0.2 & 0.7 \end{pmatrix} $$
$$ \Sigma_{YY} = \begin{pmatrix} 4 & 1 \\ 1 & 5 \end{pmatrix} $$
Et le vecteur d'observation donné est $y = \begin{pmatrix} 3.5 \\ 4.5 \end{pmatrix}$.

#### Étape 2 : Calcul de $\Sigma_{YY}^{-1}$

La matrice $\Sigma_{YY}$ est une matrice $2 \times 2$. Pour une matrice générale $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, son inverse est $A^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

Pour $\Sigma_{YY} = \begin{pmatrix} 4 & 1 \\ 1 & 5 \end{pmatrix}$ :
Le déterminant est $\det(\Sigma_{YY}) = (4)(5) - (1)(1) = 20 - 1 = 19$.

L'inverse de $\Sigma_{YY}$ est donc :
$$ \Sigma_{YY}^{-1} = \frac{1}{19} \begin{pmatrix} 5 & -1 \\ -1 & 4 \end{pmatrix} = \begin{pmatrix} 5/19 & -1/19 \\ -1/19 & 4/19 \end{pmatrix} $$

#### Étape 3 : Calcul de $y - \mu_Y$

$$ y - \mu_Y = \begin{pmatrix} 3.5 \\ 4.5 \end{pmatrix} - \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 3.5 - 3 \\ 4.5 - 4 \end{pmatrix} = \begin{pmatrix} 0.5 \\ 0.5 \end{pmatrix} $$

#### Étape 4 : Calcul du produit matriciel $\Sigma_{XY} \Sigma_{YY}^{-1}$

$$ \Sigma_{XY} \Sigma_{YY}^{-1} = \begin{pmatrix} 0.8 & 0.2 \\ 0.3 & 0.7 \end{pmatrix} \begin{pmatrix} 5/19 & -1/19 \\ -1/19 & 4/19 \end{pmatrix} $$
Effectuons la multiplication terme par terme :
$$ \Sigma_{XY} \Sigma_{YY}^{-1} = \frac{1}{19} \begin{pmatrix}
(0.8)(5) + (0.2)(-1) & (0.8)(-1) + (0.2)(4) \\
(0.3)(5) + (0.7)(-1) & (0.3)(-1) + (0.7)(4)
\end{pmatrix} $$
$$ = \frac{1}{19} \begin{pmatrix}
4.0 - 0.2 & -0.8 + 0.8 \\
1.5 - 0.7 & -0.3 + 2.8
\end{pmatrix} $$
$$ = \frac{1}{19} \begin{pmatrix}
3.8 & 0 \\
0.8 & 2.5
\end{pmatrix} $$
Convertissons les éléments en fractions exactes pour plus de précision :
$3.8/19 = (38/10)/19 = 38/(10 \times 19) = 2/10 = 1/5$.
$0/19 = 0$.
$0.8/19 = (8/10)/19 = 8/190 = 4/95$.
$2.5/19 = (25/10)/19 = 25/190 = 5/38$.

Donc,
$$ \Sigma_{XY} \Sigma_{YY}^{-1} = \begin{pmatrix} 1/5 & 0 \\ 4/95 & 5/38 \end{pmatrix} $$

#### Étape 5 : Calcul de l'espérance conditionnelle $\mathbb{E}[X|Y=y]$

Nous utilisons la formule $\mathbb{E}[X|Y=y] = \mu_X + (\Sigma_{XY} \Sigma_{YY}^{-1}) (y - \mu_Y)$.
$$ \mathbb{E}[X|Y=y] = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 1/5 & 0 \\ 4/95 & 5/38 \end{pmatrix} \begin{pmatrix} 0.5 \\ 0.5 \end{pmatrix} $$
Effectuons la multiplication matricielle :
$$ = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} (1/5)(0.5) + (0)(0.5) \\ (4/95)(0.5) + (5/38)(0.5) \end{pmatrix} $$
$$ = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 0.1 \\ 4/190 + 5/76 \end{pmatrix} $$
Calculons la somme des fractions :
$4/190 = 2/95$.
$2/95 + 5/76$. Le plus petit commun multiple (PPCM) de $95 = 5 \times 19$ et $76 = 4 \times 19$ est $4 \times 5 \times 19 = 380$.
$2/95 = (2 \times 4)/(95 \times 4) = 8/380$.
$5/76 = (5 \times 5)/(76 \times 5) = 25/380$.
La somme est $8/380 + 25/380 = 33/380$.

Ainsi, l'espérance conditionnelle est :
$$ \mathbb{E}[X|Y=y] = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 0.1 \\ 33/380 \end{pmatrix} = \begin{pmatrix} 1 + 0.1 \\ 2 + 33/380 \end{pmatrix} $$
$$ = \begin{pmatrix} 1.1 \\ (2 \times 380 + 33)/380 \end{pmatrix} = \begin{pmatrix} 1.1 \\ (760 + 33)/380 \end{pmatrix} = \begin{pmatrix} 1.1 \\ 793/380 \end{pmatrix} $$
En valeurs décimales (arrondies à quatre décimales) :
$$ \mathbb{E}[X|Y=y] \approx \begin{pmatrix} 1.1000 \\ 2.0868 \end{pmatrix} $$

#### Étape 6 : Calcul du produit matriciel $\Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX}$

Nous utilisons le résultat de l'Étape 4 : $\Sigma_{XY} \Sigma_{YY}^{-1} = \begin{pmatrix} 1/5 & 0 \\ 4/95 & 5/38 \end{pmatrix}$.
Nous multiplions maintenant par $\Sigma_{YX} = \begin{pmatrix} 0.8 & 0.3 \\ 0.2 & 0.7 \end{pmatrix}$.
$$ \Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX} = \begin{pmatrix} 1/5 & 0 \\ 4/95 & 5/38 \end{pmatrix} \begin{pmatrix} 0.8 & 0.3 \\ 0.2 & 0.7 \end{pmatrix} $$
Effectuons la multiplication terme par terme :
$$ = \begin{pmatrix}
(1/5)(0.8) + (0)(0.2) & (1/5)(0.3) + (0)(0.7) \\
(4/95)(0.8) + (5/38)(0.2) & (4/95)(0.3) + (5/38)(0.7)
\end{pmatrix} $$
$$ = \begin{pmatrix}
(1/5)(4/5) & (1/5)(3/10) \\
(4/95)(4/5) + (5/38)(1/5) & (4/95)(3/10) + (5/38)(7/10)
\end{pmatrix} $$
$$ = \begin{pmatrix}
4/25 & 3/50 \\
16/475 + 1/38 & 12/950 + 7/76
\end{pmatrix} $$
Simplifions les fractions dans la matrice :
$4/25 = 0.16$.
$3/50 = 0.06$.
Pour $16/475 + 1/38$ : PPCM de $475 = 25 \times 19$ et $38 = 2 \times 19$ est $950$.
$16/475 = (16 \times 2)/(475 \times 2) = 32/950$.
$1/38 = (1 \times 25)/(38 \times 25) = 25/950$.
La somme est $32/950 + 25/950 = 57/950$.
Pour $12/950 + 7/76$ : PPCM de $950 = 50 \times 19$ et $76 = 4 \times 19$ est $1900$.
$12/950 = (12 \times 2)/(950 \times 2) = 24/1900$.
$7/76 = (7 \times 25)/(76 \times 25) = 175/1900$.
La somme est $24/1900 + 175/1900 = 199/1900$.

Donc,
$$ \Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX} = \begin{pmatrix} 4/25 & 3/50 \\ 57/950 & 199/1900 \end{pmatrix} $$

#### Étape 7 : Calcul de la matrice de covariance conditionnelle $\text{Var}(X|Y=y)$

Nous utilisons la formule $\text{Var}(X|Y=y) = \Sigma_{XX} - (\Sigma_{XY} \Sigma_{YY}^{-1} \Sigma_{YX})$.
$$ \text{Var}(X|Y=y) = \begin{pmatrix} 2 & 0.5 \\ 0.5 & 3 \end{pmatrix} - \begin{pmatrix} 4/25 & 3/50 \\ 57/950 & 199/1900 \end{pmatrix} $$
Effectuons les soustractions terme par terme :
$$ = \begin{pmatrix}
2 - 4/25 & 0.5 - 3/50 \\
0.5 - 57/950 & 3 - 199/1900
\end{pmatrix} $$
$2 - 4/25 = 50/25 - 4/25 = 46/25$.
$0.5 - 3/50 = 1/2 - 3/50 = 25/50 - 3/50 = 22/50 = 11/25$.
$0.5 - 57/950 = 1/2 - 57/950 = 475/950 - 57/950 = 418/950 = 209/475$.
$3 - 199/1900 = 5700/1900 - 199/1900 = 5501/1900$.

Ainsi, la matrice de covariance conditionnelle est :
$$ \text{Var}(X|Y=y) = \begin{pmatrix}
46/25 & 11/25 \\
209/475 & 5501/1900
\end{pmatrix} $$
En valeurs décimales (arrondies à quatre décimales) :
$$ \text{Var}(X|Y=y) \approx \begin{pmatrix}
1.8400 & 0.4400 \\
0.4400 & 2.8953
\end{pmatrix} $$
On observe que les éléments hors diagonale sont égaux ($11/25 = 0.44$ et $209/475 \approx 0.4400$), ce qui confirme la symétrie de la matrice de covariance conditionnelle, comme attendu.
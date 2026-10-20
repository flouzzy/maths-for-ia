# Exercice 2

Difficulté : $\bigstar\star\star\star\star$

Considérons un vecteur gaussien $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ de dimension 2, représentant les mesures de deux capteurs interdépendants. La moyenne $\mu_X$ et la matrice de covariance $\Sigma_X$ de $X$ sont données par :
$$ \mu_X = \mathbb{E}[X] = \begin{pmatrix} 1 \\ 2 \end{pmatrix} $$
$$ \Sigma_X = \text{Cov}(X) = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} $$
Ainsi, la distribution de $X$ est $X \sim \mathcal{N}(\mu_X, \Sigma_X)$.

Nous souhaitons analyser un nouveau vecteur aléatoire $Y = \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix}$ obtenu par une transformation affine des mesures de $X$. Cette transformation est définie comme suit :
$$ Y = AX + b $$
où $A$ est une matrice $2 \times 2$ et $b$ est un vecteur colonne de dimension 2, donnés par :
$$ A = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} $$
$$ b = \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

1.  Déterminez le vecteur de moyenne $\mu_Y = \mathbb{E}[Y]$ du vecteur $Y$.
2.  Déterminez la matrice de covariance $\Sigma_Y = \text{Cov}(Y)$ du vecteur $Y$.
3.  En déduire la loi de probabilité du vecteur $Y$.

---

# Solution de l'Exercice 2

Nous sommes en présence d'un vecteur gaussien $X \sim \mathcal{N}(\mu_X, \Sigma_X)$ avec $\mu_X = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ et $\Sigma_X = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$.
Le vecteur $Y$ est défini par une transformation affine $Y = AX + b$, où $A = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix}$ et $b = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

Il est un résultat fondamental en théorie des vecteurs gaussiens que si $X$ est un vecteur gaussien et si $Y = AX + b$ est une transformation affine de $X$ (où $A$ est une matrice et $b$ est un vecteur constant), alors $Y$ est également un vecteur gaussien. Sa moyenne $\mu_Y$ et sa matrice de covariance $\Sigma_Y$ sont déterminées par les formules suivantes :
$$ \mu_Y = \mathbb{E}[Y] = A\mu_X + b $$
$$ \Sigma_Y = \text{Cov}(Y) = A\Sigma_X A^T $$
où $A^T$ désigne la transposée de la matrice $A$.

---

### 1. Détermination du vecteur de moyenne $\mu_Y$

Nous devons calculer $\mu_Y = A\mu_X + b$.

Commençons par le produit matriciel $A\mu_X$ :
$$ A\mu_X = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} $$
Calculons chaque composante du vecteur résultant :
La première composante est obtenue en multipliant la première ligne de $A$ par le vecteur $\mu_X$:
$(1 \times 1) + (-1 \times 2) = 1 - 2 = -1$.

La deuxième composante est obtenue en multipliant la deuxième ligne de $A$ par le vecteur $\mu_X$:
$(2 \times 1) + (1 \times 2) = 2 + 2 = 4$.

Donc, le produit $A\mu_X$ est :
$$ A\mu_X = \begin{pmatrix} -1 \\ 4 \end{pmatrix} $$

Maintenant, nous ajoutons le vecteur $b$ à ce résultat :
$$ \mu_Y = A\mu_X + b = \begin{pmatrix} -1 \\ 4 \end{pmatrix} + \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$
Calculons chaque composante du vecteur somme :
Pour la première composante : $-1 + 0 = -1$.
Pour la deuxième composante : $4 + 1 = 5$.

Ainsi, le vecteur de moyenne $\mu_Y$ est :
$$ \mu_Y = \begin{pmatrix} -1 \\ 5 \end{pmatrix} $$

---

### 2. Détermination de la matrice de covariance $\Sigma_Y$

Nous devons calculer $\Sigma_Y = A\Sigma_X A^T$.

Premièrement, déterminons la transposée de la matrice $A$, notée $A^T$. Les lignes de $A$ deviennent les colonnes de $A^T$:
$$ A = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} \implies A^T = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} $$

Ensuite, calculons le produit matriciel $A\Sigma_X$:
$$ A\Sigma_X = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} $$
Calculons chaque élément de la matrice $A\Sigma_X$:
Élément $(1,1)$ (première ligne de $A$, première colonne de $\Sigma_X$): $(1 \times 2) + (-1 \times 1) = 2 - 1 = 1$.
Élément $(1,2)$ (première ligne de $A$, deuxième colonne de $\Sigma_X$): $(1 \times 1) + (-1 \times 3) = 1 - 3 = -2$.
Élément $(2,1)$ (deuxième ligne de $A$, première colonne de $\Sigma_X$): $(2 \times 2) + (1 \times 1) = 4 + 1 = 5$.
Élément $(2,2)$ (deuxième ligne de $A$, deuxième colonne de $\Sigma_X$): $(2 \times 1) + (1 \times 3) = 2 + 3 = 5$.

Donc, le produit $A\Sigma_X$ est :
$$ A\Sigma_X = \begin{pmatrix} 1 & -2 \\ 5 & 5 \end{pmatrix} $$

Enfin, calculons le produit $(A\Sigma_X)A^T$:
$$ \Sigma_Y = \begin{pmatrix} 1 & -2 \\ 5 & 5 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} $$
Calculons chaque élément de la matrice $\Sigma_Y$:
Élément $(1,1)$ (première ligne de $(A\Sigma_X)$, première colonne de $A^T$): $(1 \times 1) + (-2 \times -1) = 1 + 2 = 3$.
Élément $(1,2)$ (première ligne de $(A\Sigma_X)$, deuxième colonne de $A^T$): $(1 \times 2) + (-2 \times 1) = 2 - 2 = 0$.
Élément $(2,1)$ (deuxième ligne de $(A\Sigma_X)$, première colonne de $A^T$): $(5 \times 1) + (5 \times -1) = 5 - 5 = 0$.
Élément $(2,2)$ (deuxième ligne de $(A\Sigma_X)$, deuxième colonne de $A^T$): $(5 \times 2) + (5 \times 1) = 10 + 5 = 15$.

Ainsi, la matrice de covariance $\Sigma_Y$ est :
$$ \Sigma_Y = \begin{pmatrix} 3 & 0 \\ 0 & 15 \end{pmatrix} $$

---

### 3. Déduction de la loi de probabilité du vecteur $Y$

Comme nous l'avons rappelé en introduction, puisque $X$ est un vecteur gaussien et $Y$ est une transformation affine de $X$, $Y$ est également un vecteur gaussien. Nous avons déterminé son vecteur de moyenne $\mu_Y$ et sa matrice de covariance $\Sigma_Y$.

Par conséquent, la loi de probabilité du vecteur $Y$ est :
$$ Y \sim \mathcal{N}\left( \begin{pmatrix} -1 \\ 5 \end{pmatrix}, \begin{pmatrix} 3 & 0 \\ 0 & 15 \end{pmatrix} \right) $$
Il est intéressant de noter que la matrice de covariance $\Sigma_Y$ est diagonale. Cela implique que les composantes $Y_1$ et $Y_2$ du vecteur $Y$ sont des variables aléatoires indépendantes. Plus précisément, $Y_1$ suit une loi normale $\mathcal{N}(-1, 3)$ et $Y_2$ suit une loi normale $\mathcal{N}(5, 15)$, et $Y_1$ et $Y_2$ sont indépendantes.
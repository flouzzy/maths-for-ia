En tant que Système Agentique d'Élite, Professeur Émérite de Mathématiques, je vous présente l'exercice suivant, conçu avec la plus grande rigueur académique.

---

# Exercice 4 ($\bigstar\bigstar\star\star\star$)

**Thème :** Vecteurs Gaussiens, indépendance et transformations affines.
**Niveau :** Licence 3 (Moyen)

Dans un laboratoire d'analyse de données, on modélise deux mesures interreliées, $X_1$ et $X_2$, comme un vecteur Gaussien $X = (X_1, X_2)^T$. La distribution de $X$ est donnée par :
$$X \sim \mathcal{N}(\mu_X, \Sigma_X)$$
où le vecteur espérance $\mu_X$ et la matrice de covariance $\Sigma_X$ sont définis comme suit :
$$\mu_X = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \quad \text{et} \quad \Sigma_X = \begin{pmatrix} 4 & 1 \\ 1 & 9 \end{pmatrix}$$

Pour des raisons d'optimisation et d'interprétation, on s'intéresse à deux nouvelles variables aléatoires $Y_1$ et $Y_2$ qui sont des combinaisons linéaires de $X_1$ et $X_2$ :
$$Y_1 = X_1 + X_2$$
$$Y_2 = X_1 - X_2$$

Considérons le vecteur Gaussien $Y = (Y_1, Y_2)^T$.

1.  Exprimer le vecteur $Y$ sous forme d'une transformation affine $Y = A X + b$, où $A$ est une matrice et $b$ est un vecteur. Vous identifierez explicitement la matrice $A$ et le vecteur $b$.
2.  Déterminer la loi de probabilité du vecteur Gaussien $Y$. Vous calculerez explicitement son vecteur espérance $\mu_Y$ et sa matrice de covariance $\Sigma_Y$, en détaillant toutes les étapes des calculs matriciels.
3.  Les variables aléatoires $Y_1$ et $Y_2$ sont-elles indépendantes ? Justifier votre réponse de manière exhaustive.

---

## Solution de l'Exercice 4

Nous allons résoudre cet exercice étape par étape, en détaillant chaque calcul pour assurer une compréhension complète.

### Rappel Théorique

Si $X$ est un vecteur Gaussien de dimension $n$ suivant $X \sim \mathcal{N}(\mu_X, \Sigma_X)$, et si $Y$ est une transformation affine de $X$ donnée par $Y = A X + b$, où $A$ est une matrice de dimension $m \times n$ et $b$ est un vecteur de dimension $m$, alors $Y$ est également un vecteur Gaussien de dimension $m$. Sa loi est donnée par :
$$Y \sim \mathcal{N}(\mu_Y, \Sigma_Y)$$
où :
$$\mu_Y = \mathbb{E}[Y] = A \mu_X + b$$
$$\Sigma_Y = \text{Cov}(Y) = A \Sigma_X A^T$$
De plus, pour un vecteur Gaussien, l'indépendance de ses composantes est équivalente à la nullité de leurs covariances mutuelles. Autrement dit, $Y_i$ et $Y_j$ sont indépendantes si et seulement si $\text{Cov}(Y_i, Y_j) = 0$.

### Question 1 : Expression de $Y$ sous forme affine

Nous avons les définitions des variables $Y_1$ et $Y_2$ :
$$Y_1 = X_1 + X_2$$
$$Y_2 = X_1 - X_2$$
Nous voulons exprimer le vecteur $Y = \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix}$ sous la forme $Y = A X + b$.
En écrivant les équations sous forme matricielle :
$$\begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix} = \begin{pmatrix} 1 \cdot X_1 + 1 \cdot X_2 \\ 1 \cdot X_1 - 1 \cdot X_2 \end{pmatrix}$$
Nous pouvons identifier la matrice $A$ et le vecteur $b$ :
$$A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
$$b = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
En effet, $A X + b = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} X_1 \\ X_2 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot X_1 + 1 \cdot X_2 \\ 1 \cdot X_1 - 1 \cdot X_2 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} X_1 + X_2 \\ X_1 - X_2 \end{pmatrix} = \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix}$.
Donc, la matrice $A$ est $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ et le vecteur $b$ est $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

### Question 2 : Détermination de la loi de probabilité de $Y$

Puisque $X$ est un vecteur Gaussien et $Y$ est une transformation affine de $X$, $Y$ est également un vecteur Gaussien. Pour déterminer sa loi, nous devons calculer son vecteur espérance $\mu_Y$ et sa matrice de covariance $\Sigma_Y$.

#### Calcul du vecteur espérance $\mu_Y$ :
Nous utilisons la formule $\mu_Y = A \mu_X + b$.
Nous avons $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, $\mu_X = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, et $b = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
$$\mu_Y = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
Effectuons la multiplication matricielle $A \mu_X$ :
$$A \mu_X = \begin{pmatrix} (1 \cdot 1) + (1 \cdot 2) \\ (1 \cdot 1) + (-1 \cdot 2) \end{pmatrix} = \begin{pmatrix} 1 + 2 \\ 1 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$$
Maintenant, ajoutons le vecteur $b$ :
$$\mu_Y = \begin{pmatrix} 3 \\ -1 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$$
Ainsi, le vecteur espérance de $Y$ est $\mu_Y = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$.

#### Calcul de la matrice de covariance $\Sigma_Y$ :
Nous utilisons la formule $\Sigma_Y = A \Sigma_X A^T$.
Nous avons $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ et $\Sigma_X = \begin{pmatrix} 4 & 1 \\ 1 & 9 \end{pmatrix}$.
D'abord, calculons la transposée de $A$, $A^T$.
$$A^T = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}^T = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
Dans ce cas particulier, la matrice $A$ est symétrique, donc $A^T = A$.

Maintenant, effectuons le produit $A \Sigma_X$ :
$$A \Sigma_X = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 4 & 1 \\ 1 & 9 \end{pmatrix}$$
$$A \Sigma_X = \begin{pmatrix} (1 \cdot 4) + (1 \cdot 1) & (1 \cdot 1) + (1 \cdot 9) \\ (1 \cdot 4) + (-1 \cdot 1) & (1 \cdot 1) + (-1 \cdot 9) \end{pmatrix}$$
$$A \Sigma_X = \begin{pmatrix} 4 + 1 & 1 + 9 \\ 4 - 1 & 1 - 9 \end{pmatrix} = \begin{pmatrix} 5 & 10 \\ 3 & -8 \end{pmatrix}$$
Enfin, multiplions ce résultat par $A^T$:
$$\Sigma_Y = (A \Sigma_X) A^T = \begin{pmatrix} 5 & 10 \\ 3 & -8 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
$$\Sigma_Y = \begin{pmatrix} (5 \cdot 1) + (10 \cdot 1) & (5 \cdot 1) + (10 \cdot (-1)) \\ (3 \cdot 1) + (-8 \cdot 1) & (3 \cdot 1) + (-8 \cdot (-1)) \end{pmatrix}$$
$$\Sigma_Y = \begin{pmatrix} 5 + 10 & 5 - 10 \\ 3 - 8 & 3 + 8 \end{pmatrix} = \begin{pmatrix} 15 & -5 \\ -5 & 11 \end{pmatrix}$$
Ainsi, la matrice de covariance de $Y$ est $\Sigma_Y = \begin{pmatrix} 15 & -5 \\ -5 & 11 \end{pmatrix}$.

#### Conclusion sur la loi de $Y$ :
Le vecteur Gaussien $Y$ suit la loi :
$$Y \sim \mathcal{N}\left(\begin{pmatrix} 3 \\ -1 \end{pmatrix}, \begin{pmatrix} 15 & -5 \\ -5 & 11 \end{pmatrix}\right)$$

### Question 3 : Indépendance des variables aléatoires $Y_1$ et $Y_2$

Pour des variables aléatoires Gaussiennes, l'indépendance est équivalente à une covariance nulle. Nous devons donc examiner l'élément hors-diagonal de la matrice de covariance $\Sigma_Y$, qui représente la covariance entre $Y_1$ et $Y_2$.
La matrice de covariance $\Sigma_Y$ est donnée par :
$$\Sigma_Y = \begin{pmatrix} \text{Var}(Y_1) & \text{Cov}(Y_1, Y_2) \\ \text{Cov}(Y_2, Y_1) & \text{Var}(Y_2) \end{pmatrix} = \begin{pmatrix} 15 & -5 \\ -5 & 11 \end{pmatrix}$$
Nous lisons directement que $\text{Cov}(Y_1, Y_2) = -5$.

Puisque $\text{Cov}(Y_1, Y_2) = -5 \neq 0$, les variables aléatoires $Y_1$ et $Y_2$ ne sont pas indépendantes.
**Justification exhaustive :**
Pour des variables aléatoires générales, une covariance nulle n'implique pas nécessairement l'indépendance. Cependant, lorsque les variables aléatoires sont des composantes d'un vecteur Gaussien (et sont donc elles-mêmes Gaussiennes), la condition de covariance nulle est suffisante pour garantir l'indépendance.
Dans notre cas, $Y_1$ et $Y_2$ sont les composantes du vecteur Gaussien $Y$. Nous avons calculé que leur covariance mutuelle est $\text{Cov}(Y_1, Y_2) = -5$. Étant donné que cette covariance n'est pas nulle, il s'ensuit que $Y_1$ et $Y_2$ ne sont pas indépendantes.
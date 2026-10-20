# Exercice 7: Analyse d'un Système de Mesure Corrélationnel
$\bigstar\bigstar\bigstar\bigstar\star$

Un système de mesure tri-dimensionnel produit des observations $X = (X_1, X_2, X_3)^T$. On modélise $X$ comme un vecteur gaussien de dimension 3, noté $X \sim \mathcal{N}(\mu, \Sigma)$, où:
$$
\mu = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \quad \text{et} \quad \Sigma = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}
$$

1.  Considérons le sous-vecteur $Y = (X_1, X_2)^T$ et la variable $Z = X_3$.
    a.  Déterminez la moyenne $\mathbb{E}[Y]$ et la matrice de covariance $\text{Cov}(Y)$ du vecteur $Y$.
    b.  Calculez l'espérance conditionnelle $\mathbb{E}[Y|Z=z]$ et la matrice de covariance conditionnelle $\text{Var}(Y|Z=z)$.
    c.  Discutez si $Y$ et $Z$ sont indépendants. Justifiez votre réponse.

2.  Soit $W_1 = X_1 + X_2$ et $W_2 = X_3$.
    a.  Déterminez la moyenne $\mathbb{E}[W_1]$ et $\mathbb{E}[W_2]$.
    b.  Calculez la covariance $\text{Cov}(W_1, W_2)$.
    c.  Les variables $W_1$ et $W_2$ sont-elles indépendantes ? Justifiez votre réponse.

3.  Question conceptuelle sur l'indépendance de variables gaussiennes:
    On considère deux variables aléatoires $U$ et $V$. On vous donne les informations suivantes:
    i.   $U$ suit une loi normale $\mathcal{N}(0,1)$.
    ii.  $V$ suit une loi normale $\mathcal{N}(0,1)$.
    iii. $\text{Cov}(U,V) = 0$.
    Ces trois informations sont-elles suffisantes pour affirmer que $U$ et $V$ sont indépendantes ? Expliquez votre raisonnement en vous référant à la définition d'un vecteur gaussien.

---

# Solution de l'Exercice 7

**1. Analyse du sous-vecteur $Y = (X_1, X_2)^T$ et de la variable $Z = X_3$.**

Le vecteur $X = (X_1, X_2, X_3)^T$ est un vecteur gaussien de moyenne $\mu$ et de matrice de covariance $\Sigma$. Par définition, tout sous-vecteur d'un vecteur gaussien est également un vecteur gaussien.

**a. Détermination de la moyenne $\mathbb{E}[Y]$ et de la matrice de covariance $\text{Cov}(Y)$.**

Le vecteur $Y$ est formé des deux premières composantes de $X$. Ainsi, sa moyenne est simplement les deux premières composantes du vecteur $\mu$, et sa matrice de covariance est le bloc $2 \times 2$ supérieur gauche de $\Sigma$.

$$
\mathbb{E}[Y] = \mathbb{E}\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} = \begin{pmatrix} \mathbb{E}[X_1] \\ \mathbb{E}[X_2] \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

La matrice de covariance de $Y$, notée $\Sigma_{YY}$, est donnée par:
$$
\Sigma_{YY} = \text{Cov}(Y) = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_2, X_1) & \text{Var}(X_2) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}
$$

**b. Calcul de l'espérance conditionnelle $\mathbb{E}[Y|Z=z]$ et de la matrice de covariance conditionnelle $\text{Var}(Y|Z=z)$.**

Pour un vecteur gaussien $X = (X_1^T, X_2^T)^T$ partitionné en deux sous-vecteurs $X_1$ et $X_2$, avec $\mu = (\mu_1^T, \mu_2^T)^T$ et $\Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}$, l'espérance conditionnelle de $X_1$ sachant $X_2=x_2$ est donnée par:
$$
\mathbb{E}[X_1|X_2=x_2] = \mu_1 + \Sigma_{12}\Sigma_{22}^{-1}(x_2 - \mu_2)
$$
et la matrice de covariance conditionnelle est:
$$
\text{Var}(X_1|X_2=x_2) = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}
$$

Dans notre cas, nous identifions $Y$ au $X_1$ de la formule générale (le vecteur que nous cherchons à conditionner) et $Z$ au $X_2$ de la formule générale (le vecteur par rapport auquel nous conditionnons).
Nous avons:
$Y = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$, qui est de dimension $2 \times 1$.
$Z = X_3$, qui est de dimension $1 \times 1$.

Partitionnons $\mu$ et $\Sigma$ en conséquence:
$$
\mu = \begin{pmatrix} \mu_Y \\ \mu_Z \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ \hline 3 \end{pmatrix} \quad \Rightarrow \quad \mu_Y = \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \quad \mu_Z = 3
$$
$$
\Sigma = \begin{pmatrix} \Sigma_{YY} & \Sigma_{YZ} \\ \Sigma_{ZY} & \Sigma_{ZZ} \end{pmatrix} = \begin{pmatrix}
2 & 1 & | & 0 \\
1 & 3 & | & 1 \\
- & - & - & - \\
0 & 1 & | & 2
\end{pmatrix}
$$
D'où les blocs de la matrice de covariance:
$$
\Sigma_{YY} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}
$$
$$
\Sigma_{YZ} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$
$$
\Sigma_{ZY} = \begin{pmatrix} 0 & 1 \end{pmatrix}
$$
$$
\Sigma_{ZZ} = (2)
$$

Calculons l'inverse de $\Sigma_{ZZ}$:
$$
\Sigma_{ZZ}^{-1} = (2)^{-1} = \left(\frac{1}{2}\right)
$$

Maintenant, appliquons les formules pour l'espérance conditionnelle:
$$
\mathbb{E}[Y|Z=z] = \mu_Y + \Sigma_{YZ}\Sigma_{ZZ}^{-1}(z - \mu_Z)
$$
$$
\mathbb{E}[Y|Z=z] = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 0 \\ 1 \end{pmatrix} \left(\frac{1}{2}\right) (z - 3)
$$
$$
\mathbb{E}[Y|Z=z] = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 0 \cdot \frac{1}{2} (z - 3) \\ 1 \cdot \frac{1}{2} (z - 3) \end{pmatrix}
$$
$$
\mathbb{E}[Y|Z=z] = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 0 \\ \frac{1}{2}(z - 3) \end{pmatrix}
$$
$$
\mathbb{E}[Y|Z=z] = \begin{pmatrix} 1 \\ 2 + \frac{z - 3}{2} \end{pmatrix} = \begin{pmatrix} 1 \\ \frac{4 + z - 3}{2} \end{pmatrix} = \begin{pmatrix} 1 \\ \frac{z + 1}{2} \end{pmatrix}
$$

Ensuite, pour la matrice de covariance conditionnelle:
$$
\text{Var}(Y|Z=z) = \Sigma_{YY} - \Sigma_{YZ}\Sigma_{ZZ}^{-1}\Sigma_{ZY}
$$
$$
\text{Var}(Y|Z=z) = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \end{pmatrix} \left(\frac{1}{2}\right) \begin{pmatrix} 0 & 1 \end{pmatrix}
$$
Effectuons le produit matriciel $\begin{pmatrix} 0 \\ 1 \end{pmatrix} \left(\frac{1}{2}\right) \begin{pmatrix} 0 & 1 \end{pmatrix}$:
$$
\begin{pmatrix} 0 \\ 1 \end{pmatrix} \left(\frac{1}{2}\right) \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & \frac{1}{2} \end{pmatrix} = \begin{pmatrix} 0 \cdot 0 & 0 \cdot \frac{1}{2} \\ 1 \cdot 0 & 1 \cdot \frac{1}{2} \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & \frac{1}{2} \end{pmatrix}
$$
Donc:
$$
\text{Var}(Y|Z=z) = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} - \begin{pmatrix} 0 & 0 \\ 0 & \frac{1}{2} \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 3 - \frac{1}{2} \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & \frac{5}{2} \end{pmatrix}
$$
Il est à noter que la matrice de covariance conditionnelle ne dépend pas de la valeur $z$ de la variable conditionnée, ce qui est une propriété des vecteurs gaussiens.

**c. Discussion sur l'indépendance de $Y$ et $Z$.**

Pour que deux sous-vecteurs d'un vecteur gaussien soient indépendants, il faut et il suffit que leur matrice de covariance croisée soit nulle.
La matrice de covariance croisée entre $Y$ et $Z$ est $\Sigma_{YZ}$:
$$
\Sigma_{YZ} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$
Comme $\Sigma_{YZ}$ n'est pas une matrice nulle (elle contient le terme 1), $Y$ et $Z$ ne sont pas indépendants.
Plus précisément, on a $\text{Cov}(X_1, X_3) = 0$ (premier élément de $\Sigma_{YZ}$), mais $\text{Cov}(X_2, X_3) = 1 \neq 0$ (deuxième élément de $\Sigma_{YZ}$). La dépendance est portée par la relation entre $X_2$ et $X_3$.

**2. Analyse des variables $W_1 = X_1 + X_2$ et $W_2 = X_3$.**

Le vecteur $(W_1, W_2)^T$ est une transformation linéaire du vecteur gaussien $X$. En effet, $W = AX$ avec $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$. Par conséquent, $(W_1, W_2)^T$ est également un vecteur gaussien.

**a. Détermination de la moyenne $\mathbb{E}[W_1]$ et $\mathbb{E}[W_2]$.**

En utilisant la linéarité de l'espérance:
$$
\mathbb{E}[W_1] = \mathbb{E}[X_1 + X_2] = \mathbb{E}[X_1] + \mathbb{E}[X_2] = 1 + 2 = 3
$$
$$
\mathbb{E}[W_2] = \mathbb{E}[X_3] = 3
$$

**b. Calcul de la covariance $\text{Cov}(W_1, W_2)$.**

$$
\text{Cov}(W_1, W_2) = \text{Cov}(X_1 + X_2, X_3)
$$
En utilisant la bilinéarité de la covariance:
$$
\text{Cov}(X_1 + X_2, X_3) = \text{Cov}(X_1, X_3) + \text{Cov}(X_2, X_3)
$$
Nous extrayons ces valeurs de la matrice $\Sigma$:
$\text{Cov}(X_1, X_3) = \Sigma_{13} = 0$
$\text{Cov}(X_2, X_3) = \Sigma_{23} = 1$
$$
\text{Cov}(W_1, W_2) = 0 + 1 = 1
$$

**c. Les variables $W_1$ et $W_2$ sont-elles indépendantes ? Justifiez votre réponse.**

Puisque $(W_1, W_2)^T$ est un vecteur gaussien, $W_1$ et $W_2$ sont indépendantes si et seulement si elles sont non corrélées, c'est-à-dire si $\text{Cov}(W_1, W_2) = 0$.
Nous avons calculé $\text{Cov}(W_1, W_2) = 1$.
Puisque $\text{Cov}(W_1, W_2) = 1 \neq 0$, les variables $W_1$ et $W_2$ ne sont pas indépendantes. Elles sont corrélées.

**3. Question conceptuelle sur l'indépendance de variables gaussiennes.**

On considère deux variables aléatoires $U$ et $V$ avec les informations suivantes:
i.   $U$ suit une loi normale $\mathcal{N}(0,1)$.
ii.  $V$ suit une loi normale $\mathcal{N}(0,1)$.
iii. $\text{Cov}(U,V) = 0$.

Ces trois informations ne sont *pas* suffisantes pour affirmer que $U$ et $V$ sont indépendantes.

**Explication:**

L'indépendance de deux variables aléatoires $U$ et $V$ signifie que leur fonction de répartition conjointe $F_{U,V}(u,v) = P(U \le u, V \le v)$ peut être factorisée en le produit de leurs fonctions de répartition marginales: $F_{U,V}(u,v) = F_U(u)F_V(v)$ pour tout $u,v \in \mathbb{R}$. Pour les variables continues, cela équivaut à la factorisation de leurs densités de probabilité conjointes: $f_{U,V}(u,v) = f_U(u)f_V(v)$.

La condition $\text{Cov}(U,V) = 0$ signifie que $U$ et $V$ sont non corrélées.
En général, pour des variables aléatoires quelconques, la non-corrélation n'implique pas l'indépendance. Il existe de nombreux contre-exemples où des variables sont non corrélées mais dépendantes.

Le point crucial ici est la distinction entre des variables *individuellement* gaussiennes (marginalement gaussiennes) et un *vecteur gaussien*.
Si le vecteur $(U,V)^T$ est un **vecteur gaussien** (c'est-à-dire que leur distribution jointe est une distribution gaussienne multivariée), alors la non-corrélation ($\text{Cov}(U,V)=0$) est une condition *nécessaire et suffisante* pour l'indépendance de $U$ et $V$. C'est une propriété fondamentale des vecteurs gaussiens qui simplifie grandement leur analyse.

Cependant, les informations données (i), (ii), (iii) ne spécifient *pas* que le vecteur $(U,V)^T$ est un vecteur gaussien. Elles disent seulement que $U$ est gaussienne et $V$ est gaussienne (chacune prise séparément), et qu'elles sont non corrélées. Il est possible de construire des paires de variables $(U,V)$ qui sont marginalement gaussiennes, non corrélées, mais dépendantes, et dont la distribution jointe n'est pas gaussienne.

**Contre-exemple (illustrant des variables marginalement gaussiennes, non corrélées mais dépendantes):**
Soit $X_1 \sim \mathcal{N}(0,1)$ et $X_2 \sim \mathcal{N}(0,1)$ deux variables aléatoires indépendantes.
Soit $S$ une variable aléatoire de Bernoulli telle que $P(S=1) = P(S=-1) = 1/2$, et $S$ est indépendante de $X_1$ et $X_2$.
Définissons $U = X_1$ et $V = S X_1$.

Vérifions les conditions données:
1.  **$U \sim \mathcal{N}(0,1)$**: Par construction, $U=X_1$, donc $U$ suit une loi normale standard.
2.  **$V \sim \mathcal{N}(0,1)$**: Calculons la fonction de répartition de $V$:
    $P(V \le v) = P(S X_1 \le v) = P(S=1, X_1 \le v) + P(S=-1, -X_1 \le v)$.
    Puisque $S$ est indépendante de $X_1$:
    $P(V \le v) = P(S=1) P(X_1 \le v) + P(S=-1) P(-X_1 \le v)$.
    $P(V \le v) = \frac{1}{2} \Phi(v) + \frac{1}{2} P(X_1 \ge -v)$.
    Puisque $X_1$ est symétrique autour de 0, $P(X_1 \ge -v) = P(X_1 \le v) = \Phi(v)$.
    Donc $P(V \le v) = \frac{1}{2} \Phi(v) + \frac{1}{2} \Phi(v) = \Phi(v)$.
    Ainsi, $V \sim \mathcal{N}(0,1)$. (Les variables $U$ et $V$ sont marginalement gaussiennes).

3.  **$\text{Cov}(U,V) = 0$**:
    $\mathbb{E}[U] = \mathbb{E}[X_1] = 0$.
    $\mathbb{E}[V] = \mathbb{E}[S X_1] = \mathbb{E}[S] \mathbb{E}[X_1]$ (car $S$ et $X_1$ sont indépendantes).
    Comme $\mathbb{E}[S] = 1 \cdot \frac{1}{2} + (-1) \cdot \frac{1}{2} = 0$, et $\mathbb{E}[X_1] = 0$:
    $\mathbb{E}[V] = 0 \cdot 0 = 0$.
    Maintenant, calculons la covariance:
    $\text{Cov}(U,V) = \mathbb{E}[UV] - \mathbb{E}[U]\mathbb{E}[V] = \mathbb{E}[X_1 (S X_1)] - 0 \cdot 0 = \mathbb{E}[S X_1^2]$.
    Puisque $S$ est indépendante de $X_1$:
    $\mathbb{E}[S X_1^2] = \mathbb{E}[S] \mathbb{E}[X_1^2]$.
    Comme $\mathbb{E}[S] = 0$ et $\mathbb{E}[X_1^2] = \text{Var}(X_1) + (\mathbb{E}[X_1])^2 = 1 + 0^2 = 1$:
    $\text{Cov}(U,V) = 0 \cdot 1 = 0$.
    Donc $U$ et $V$ sont non corrélées.

Cependant, $U$ et $V$ sont clairement dépendantes. Par exemple, $V^2 = (S X_1)^2 = S^2 X_1^2$. Puisque $S$ prend les valeurs $\pm 1$, $S^2=1$. Donc $V^2 = X_1^2 = U^2$. Ceci montre une forte dépendance: la valeur de $U$ détermine la valeur absolue de $V$. Par exemple, si $U=1$, alors $V$ doit être $1$ ou $-1$. Si $U=0$, alors $V=0$. La connaissance de $U$ restreint fortement les valeurs possibles de $V$, ce qui signifie qu'elles ne sont pas indépendantes. La distribution jointe de $(U,V)$ dans ce cas n'est pas gaussienne.

En conclusion, pour affirmer l'indépendance de $U$ et $V$ à partir des trois informations données (marginalement gaussiennes et non corrélées), il est indispensable d'ajouter la condition que le vecteur $(U,V)^T$ est un vecteur gaussien. Sans cette condition supplémentaire, la non-corrélation n'implique pas l'indépendance.
# Exercice 5 : Analyse de Vecteurs Gaussiens Transformés par Fonctions Caractéristiques
$\bigstar\bigstar\bigstar\star\star$ (Difficulté 3/5)

**Contexte :**
Dans un système d'ingénierie, trois capteurs $C_1, C_2, C_3$ mesurent des grandeurs physiques. Leurs lectures sont modélisées par un vecteur aléatoire $X = (X_1, X_2, X_3)^T$. En raison de l'agitation thermique et d'autres bruits aléatoires, $X$ est supposé être un vecteur Gaussien. Pour des raisons d'analyse et de contrôle, on s'intéresse à de nouvelles variables dérivées $Y_1, Y_2, Y_3$ qui sont des combinaisons linéaires des lectures des capteurs.

**Énoncé :**
Soit $X = (X_1, X_2, X_3)^T$ un vecteur Gaussien de dimension 3, caractérisé par son vecteur moyenne $\mu_X$ et sa matrice de covariance $\Sigma_X$.
On donne :
$$ \mu_X = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \quad \text{et} \quad \Sigma_X = \begin{pmatrix} 1 & 0.5 & 0 \\ 0.5 & 1 & 0.5 \\ 0 & 0.5 & 1 \end{pmatrix} $$
On définit un nouveau vecteur aléatoire $Y = (Y_1, Y_2, Y_3)^T$ par la transformation linéaire suivante :
$$ \begin{cases} Y_1 = X_1 - X_3 \\ Y_2 = X_2 \\ Y_3 = X_1 + X_2 + X_3 \end{cases} $$

Répondez aux questions suivantes en utilisant les fonctions caractéristiques :

1.  **Fonction Caractéristique de $X$** : Rappelez la définition de la fonction caractéristique d'un vecteur aléatoire $X$ et donnez l'expression explicite de la fonction caractéristique $\varphi_X(t)$ pour le vecteur Gaussien $X$ donné, où $t = (t_1, t_2, t_3)^T \in \mathbb{R}^3$.
2.  **Fonction Caractéristique de $Y$** : Exprimez le vecteur $Y$ sous la forme $Y = AX$ où $A$ est une matrice $3 \times 3$. Ensuite, déduisez l'expression explicite de la fonction caractéristique $\varphi_Y(s)$ pour le vecteur $Y$, où $s = (s_1, s_2, s_3)^T \in \mathbb{R}^3$.
3.  **Distribution de $Y$** : À partir de l'expression de $\varphi_Y(s)$, identifiez la distribution du vecteur aléatoire $Y$. Précisez son vecteur moyenne $\mu_Y$ et sa matrice de covariance $\Sigma_Y$.
4.  **Indépendance de $Y_1$ et $Y_2$** : En vous basant sur les propriétés de la distribution de $Y$ trouvée en question 3, montrez que les variables aléatoires $Y_1$ et $Y_2$ sont indépendantes.

---

# Solution de l'Exercice 5

### 1. Fonction Caractéristique de $X$

La fonction caractéristique d'un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est définie pour tout $t = (t_1, \dots, t_d)^T \in \mathbb{R}^d$ par :
$$ \varphi_X(t) = \mathbb{E}\left[e^{i t^T X}\right] $$
où $i$ est l'unité imaginaire et $t^T X = \sum_{j=1}^d t_j X_j$.

Pour un vecteur Gaussien $X \sim \mathcal{N}(\mu_X, \Sigma_X)$, la fonction caractéristique prend la forme explicite suivante :
$$ \varphi_X(t) = \exp\left(i t^T \mu_X - \frac{1}{2} t^T \Sigma_X t\right) $$
Dans notre cas, $X$ est un vecteur Gaussien de dimension 3 avec :
$$ \mu_X = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \quad \text{et} \quad \Sigma_X = \begin{pmatrix} 1 & 0.5 & 0 \\ 0.5 & 1 & 0.5 \\ 0 & 0.5 & 1 \end{pmatrix} $$
Substituons ces valeurs dans l'expression générale.

Calcul du terme $i t^T \mu_X$ :
$$ i t^T \mu_X = i \begin{pmatrix} t_1 & t_2 & t_3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = i (1 \cdot t_1 + 2 \cdot t_2 + 3 \cdot t_3) = i(t_1 + 2t_2 + 3t_3) $$

Calcul du terme $t^T \Sigma_X t$ :
$$ \begin{aligned} t^T \Sigma_X t &= \begin{pmatrix} t_1 & t_2 & t_3 \end{pmatrix} \begin{pmatrix} 1 & 0.5 & 0 \\ 0.5 & 1 & 0.5 \\ 0 & 0.5 & 1 \end{pmatrix} \begin{pmatrix} t_1 \\ t_2 \\ t_3 \end{pmatrix} \\ &= \begin{pmatrix} t_1 & t_2 & t_3 \end{pmatrix} \begin{pmatrix} 1 \cdot t_1 + 0.5 \cdot t_2 + 0 \cdot t_3 \\ 0.5 \cdot t_1 + 1 \cdot t_2 + 0.5 \cdot t_3 \\ 0 \cdot t_1 + 0.5 \cdot t_2 + 1 \cdot t_3 \end{pmatrix} \\ &= \begin{pmatrix} t_1 & t_2 & t_3 \end{pmatrix} \begin{pmatrix} t_1 + 0.5t_2 \\ 0.5t_1 + t_2 + 0.5t_3 \\ 0.5t_2 + t_3 \end{pmatrix} \\ &= t_1(t_1 + 0.5t_2) + t_2(0.5t_1 + t_2 + 0.5t_3) + t_3(0.5t_2 + t_3) \\ &= t_1^2 + 0.5t_1t_2 + 0.5t_1t_2 + t_2^2 + 0.5t_2t_3 + 0.5t_2t_3 + t_3^2 \\ &= t_1^2 + t_2^2 + t_3^2 + t_1t_2 + t_2t_3 \end{aligned} $$
Par conséquent, la fonction caractéristique de $X$ est :
$$ \varphi_X(t) = \exp\left(i(t_1 + 2t_2 + 3t_3) - \frac{1}{2}(t_1^2 + t_2^2 + t_3^2 + t_1t_2 + t_2t_3)\right) $$

### 2. Fonction Caractéristique de $Y$

Le vecteur $Y = (Y_1, Y_2, Y_3)^T$ est défini par :
$$ \begin{cases} Y_1 = X_1 - X_3 \\ Y_2 = X_2 \\ Y_3 = X_1 + X_2 + X_3 \end{cases} $$
Nous pouvons exprimer cette transformation sous forme matricielle $Y = AX$. La matrice $A$ est obtenue en observant les coefficients de $X_1, X_2, X_3$ pour chaque composante de $Y$:
$$ Y = \begin{pmatrix} Y_1 \\ Y_2 \\ Y_3 \end{pmatrix} = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} X_1 \\ X_2 \\ X_3 \end{pmatrix} $$
Ainsi, la matrice $A$ est :
$$ A = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} $$
La fonction caractéristique d'un vecteur aléatoire $Y = AX$ est liée à celle de $X$ par la relation :
$$ \varphi_Y(s) = \mathbb{E}\left[e^{i s^T Y}\right] = \mathbb{E}\left[e^{i s^T (AX)}\right] = \mathbb{E}\left[e^{i (A^T s)^T X}\right] $$
En posant $t' = A^T s$, nous avons $\varphi_Y(s) = \varphi_X(A^T s)$.

Calculons d'abord $A^T s$:
$$ A^T = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & 0 & 1 \end{pmatrix} $$
Pour $s = (s_1, s_2, s_3)^T \in \mathbb{R}^3$:
$$ t' = A^T s = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & 0 & 1 \end{pmatrix} \begin{pmatrix} s_1 \\ s_2 \\ s_3 \end{pmatrix} = \begin{pmatrix} 1 \cdot s_1 + 0 \cdot s_2 + 1 \cdot s_3 \\ 0 \cdot s_1 + 1 \cdot s_2 + 1 \cdot s_3 \\ -1 \cdot s_1 + 0 \cdot s_2 + 1 \cdot s_3 \end{pmatrix} = \begin{pmatrix} s_1 + s_3 \\ s_2 + s_3 \\ -s_1 + s_3 \end{pmatrix} $$
Donc, $t'_1 = s_1 + s_3$, $t'_2 = s_2 + s_3$, $t'_3 = -s_1 + s_3$.

Maintenant, nous substituons $t'$ dans l'expression de $\varphi_X(t)$ :
$$ \varphi_Y(s) = \exp\left(i (t'_1 + 2t'_2 + 3t'_3) - \frac{1}{2}((t'_1)^2 + (t'_2)^2 + (t'_3)^2 + t'_1t'_2 + t'_2t'_3)\right) $$

Calcul du terme $i (t'_1 + 2t'_2 + 3t'_3)$ :
$$ \begin{aligned} i (t'_1 + 2t'_2 + 3t'_3) &= i ((s_1 + s_3) + 2(s_2 + s_3) + 3(-s_1 + s_3)) \\ &= i (s_1 + s_3 + 2s_2 + 2s_3 - 3s_1 + 3s_3) \\ &= i (-2s_1 + 2s_2 + 6s_3) \end{aligned} $$

Calcul du terme $-\frac{1}{2}((t'_1)^2 + (t'_2)^2 + (t'_3)^2 + t'_1t'_2 + t'_2t'_3)$ :
Il est plus efficace d'utiliser la forme matricielle $-\frac{1}{2} s^T A \Sigma_X A^T s$. Commençons par calculer $A \Sigma_X A^T$.
Premièrement, $A \Sigma_X$:
$$ \begin{aligned} A \Sigma_X &= \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0.5 & 0 \\ 0.5 & 1 & 0.5 \\ 0 & 0.5 & 1 \end{pmatrix} \\ &= \begin{pmatrix} 1 \cdot 1 + 0 \cdot 0.5 + (-1) \cdot 0 & 1 \cdot 0.5 + 0 \cdot 1 + (-1) \cdot 0.5 & 1 \cdot 0 + 0 \cdot 0.5 + (-1) \cdot 1 \\ 0 \cdot 1 + 1 \cdot 0.5 + 0 \cdot 0 & 0 \cdot 0.5 + 1 \cdot 1 + 0 \cdot 0.5 & 0 \cdot 0 + 1 \cdot 0.5 + 0 \cdot 1 \\ 1 \cdot 1 + 1 \cdot 0.5 + 1 \cdot 0 & 1 \cdot 0.5 + 1 \cdot 1 + 1 \cdot 0.5 & 1 \cdot 0 + 1 \cdot 0.5 + 1 \cdot 1 \end{pmatrix} \\ &= \begin{pmatrix} 1 & 0 & -1 \\ 0.5 & 1 & 0.5 \\ 1.5 & 2 & 1.5 \end{pmatrix} \end{aligned} $$
Maintenant, $(A \Sigma_X) A^T$:
$$ \begin{aligned} (A \Sigma_X) A^T &= \begin{pmatrix} 1 & 0 & -1 \\ 0.5 & 1 & 0.5 \\ 1.5 & 2 & 1.5 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & 0 & 1 \end{pmatrix} \\ &= \begin{pmatrix} 1 \cdot 1 + 0 \cdot 0 + (-1) \cdot (-1) & 1 \cdot 0 + 0 \cdot 1 + (-1) \cdot 0 & 1 \cdot 1 + 0 \cdot 1 + (-1) \cdot 1 \\ 0.5 \cdot 1 + 1 \cdot 0 + 0.5 \cdot (-1) & 0.5 \cdot 0 + 1 \cdot 1 + 0.5 \cdot 0 & 0.5 \cdot 1 + 1 \cdot 1 + 0.5 \cdot 1 \\ 1.5 \cdot 1 + 2 \cdot 0 + 1.5 \cdot (-1) & 1.5 \cdot 0 + 2 \cdot 1 + 1.5 \cdot 0 & 1.5 \cdot 1 + 2 \cdot 1 + 1.5 \cdot 1 \end{pmatrix} \\ &= \begin{pmatrix} 1 + 0 + 1 & 0 & 1 + 0 - 1 \\ 0.5 + 0 - 0.5 & 0 + 1 + 0 & 0.5 + 1 + 0.5 \\ 1.5 + 0 - 1.5 & 0 + 2 + 0 & 1.5 + 2 + 1.5 \end{pmatrix} \\ &= \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} \end{aligned} $$
Soit $\Sigma_Y = A \Sigma_X A^T = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix}$.

Alors le terme quadratique est :
$$ \begin{aligned} -\frac{1}{2} s^T \Sigma_Y s &= -\frac{1}{2} \begin{pmatrix} s_1 & s_2 & s_3 \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} \begin{pmatrix} s_1 \\ s_2 \\ s_3 \end{pmatrix} \\ &= -\frac{1}{2} \begin{pmatrix} s_1 & s_2 & s_3 \end{pmatrix} \begin{pmatrix} 2s_1 \\ 0 \cdot s_1 + 1 \cdot s_2 + 2 \cdot s_3 \\ 0 \cdot s_1 + 2 \cdot s_2 + 5 \cdot s_3 \end{pmatrix} \\ &= -\frac{1}{2} \begin{pmatrix} s_1 & s_2 & s_3 \end{pmatrix} \begin{pmatrix} 2s_1 \\ s_2 + 2s_3 \\ 2s_2 + 5s_3 \end{pmatrix} \\ &= -\frac{1}{2} (s_1(2s_1) + s_2(s_2 + 2s_3) + s_3(2s_2 + 5s_3)) \\ &= -\frac{1}{2} (2s_1^2 + s_2^2 + 2s_2s_3 + 2s_2s_3 + 5s_3^2) \\ &= -\frac{1}{2} (2s_1^2 + s_2^2 + 4s_2s_3 + 5s_3^2) \end{aligned} $$
En combinant les deux termes, la fonction caractéristique de $Y$ est :
$$ \varphi_Y(s) = \exp\left(i(-2s_1 + 2s_2 + 6s_3) - \frac{1}{2}(2s_1^2 + s_2^2 + 4s_2s_3 + 5s_3^2)\right) $$

### 3. Distribution de $Y$

La fonction caractéristique $\varphi_Y(s)$ que nous avons calculée a la forme générale d'une fonction caractéristique d'un vecteur Gaussien $Y \sim \mathcal{N}(\mu_Y, \Sigma_Y)$, qui est :
$$ \varphi_Y(s) = \exp\left(i s^T \mu_Y - \frac{1}{2} s^T \Sigma_Y s\right) $$
En comparant terme par terme l'expression obtenue pour $\varphi_Y(s)$ avec cette forme générale :
$$ \varphi_Y(s) = \exp\left(i(-2s_1 + 2s_2 + 6s_3) - \frac{1}{2}(2s_1^2 + s_2^2 + 4s_2s_3 + 5s_3^2)\right) $$

Le terme linéaire $i s^T \mu_Y$ nous donne le vecteur moyenne $\mu_Y$:
$$ i s^T \mu_Y = i (s_1, s_2, s_3) \begin{pmatrix} (\mu_Y)_1 \\ (\mu_Y)_2 \\ (\mu_Y)_3 \end{pmatrix} = i(s_1 (\mu_Y)_1 + s_2 (\mu_Y)_2 + s_3 (\mu_Y)_3) $$
En comparant avec $i(-2s_1 + 2s_2 + 6s_3)$, nous identifions :
$$ \mu_Y = \begin{pmatrix} -2 \\ 2 \\ 6 \end{pmatrix} $$
Ceci est cohérent avec le calcul direct $\mu_Y = A\mu_X$:
$$ \mu_Y = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 + 0 \cdot 2 + (-1) \cdot 3 \\ 0 \cdot 1 + 1 \cdot 2 + 0 \cdot 3 \\ 1 \cdot 1 + 1 \cdot 2 + 1 \cdot 3 \end{pmatrix} = \begin{pmatrix} 1 - 3 \\ 2 \\ 1 + 2 + 3 \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \\ 6 \end{pmatrix} $$

Le terme quadratique $-\frac{1}{2} s^T \Sigma_Y s$ nous donne la matrice de covariance $\Sigma_Y$:
$$ -\frac{1}{2} s^T \Sigma_Y s = -\frac{1}{2} (2s_1^2 + s_2^2 + 4s_2s_3 + 5s_3^2) $$
Nous savons que $\Sigma_Y$ est une matrice symétrique $3 \times 3$ :
$$ \Sigma_Y = \begin{pmatrix} (\Sigma_Y)_{11} & (\Sigma_Y)_{12} & (\Sigma_Y)_{13} \\ (\Sigma_Y)_{21} & (\Sigma_Y)_{22} & (\Sigma_Y)_{23} \\ (\Sigma_Y)_{31} & (\Sigma_Y)_{32} & (\Sigma_Y)_{33} \end{pmatrix} $$
avec $(\Sigma_Y)_{ij} = (\Sigma_Y)_{ji}$.
Alors :
$$ s^T \Sigma_Y s = \sum_{j=1}^3 \sum_{k=1}^3 s_j (\Sigma_Y)_{jk} s_k = \sum_{j=1}^3 (\Sigma_Y)_{jj} s_j^2 + 2 \sum_{j<k} (\Sigma_Y)_{jk} s_j s_k $$
En comparant avec $2s_1^2 + s_2^2 + 4s_2s_3 + 5s_3^2$:
*   Coefficient de $s_1^2$: $(\Sigma_Y)_{11} = 2$
*   Coefficient de $s_2^2$: $(\Sigma_Y)_{22} = 1$
*   Coefficient de $s_3^2$: $(\Sigma_Y)_{33} = 5$
*   Coefficient de $s_1s_2$: $2(\Sigma_Y)_{12} = 0 \implies (\Sigma_Y)_{12} = 0$
*   Coefficient de $s_1s_3$: $2(\Sigma_Y)_{13} = 0 \implies (\Sigma_Y)_{13} = 0$
*   Coefficient de $s_2s_3$: $2(\Sigma_Y)_{23} = 4 \implies (\Sigma_Y)_{23} = 2$
Par conséquent, la matrice de covariance de $Y$ est :
$$ \Sigma_Y = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} $$
Ceci est cohérent avec le calcul direct $\Sigma_Y = A\Sigma_X A^T$ effectué dans la question précédente.

En conclusion, le vecteur $Y$ est un vecteur Gaussien de dimension 3, $Y \sim \mathcal{N}(\mu_Y, \Sigma_Y)$, avec :
$$ \mu_Y = \begin{pmatrix} -2 \\ 2 \\ 6 \end{pmatrix} \quad \text{et} \quad \Sigma_Y = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} $$

### 4. Indépendance de $Y_1$ et $Y_2$

Pour des variables aléatoires Gaussiennes, l'indépendance est équivalente à l'absence de corrélation, c'est-à-dire que leur covariance est nulle.
Les variables $Y_1$ et $Y_2$ sont les deux premières composantes du vecteur Gaussien $Y$. Leur covariance est donnée par l'élément $(\Sigma_Y)_{12}$ de la matrice de covariance $\Sigma_Y$.

À partir de la matrice $\Sigma_Y$ que nous avons trouvée :
$$ \Sigma_Y = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} $$
Nous observons que l'élément $(\Sigma_Y)_{12}$ (la covariance entre $Y_1$ et $Y_2$) est nul :
$$ \text{Cov}(Y_1, Y_2) = (\Sigma_Y)_{12} = 0 $$
Puisque $Y_1$ et $Y_2$ sont des composantes d'un vecteur Gaussien, et que leur covariance est nulle, nous pouvons conclure qu'elles sont indépendantes.
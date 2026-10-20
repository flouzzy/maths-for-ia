# Exercice 1

**Difficulté :** $\bigstar\star\star\star\star$ (Très facile)

### Énoncé

Dans un laboratoire de physique expérimentale, un chercheur étudie deux mesures interconnectées, $M_1$ et $M_2$, qui sont affectées par des fluctuations aléatoires. Ces fluctuations sont modélisées par deux variables aléatoires indépendantes $N_1$ et $N_2$, chacune suivant une loi normale centrée réduite, c'est-à-dire $N_1 \sim \mathcal{N}(0, 1)$ et $N_2 \sim \mathcal{N}(0, 1)$.

Les mesures $M_1$ et $M_2$ sont définies comme suit :
$$
M_1 = 2 N_1 + N_2 + 5
$$
$$
M_2 = N_1 - 3 N_2 + 10
$$

On considère le vecteur aléatoire $M = \begin{pmatrix} M_1 \\ M_2 \end{pmatrix}$.

1.  Justifier pourquoi $M$ est un vecteur gaussien.
2.  Calculer le vecteur espérance $\mathbb{E}[M]$.
3.  Calculer la matrice de covariance $\text{Cov}(M)$.

---

### Solution

Nous allons aborder chaque question avec la rigueur et la précision requises en mathématiques.

**1. Justification que $M$ est un vecteur gaussien.**

Pour justifier que $M$ est un vecteur gaussien, nous devons d'abord examiner la nature des variables aléatoires qui le composent.
Soit le vecteur de variables aléatoires $N = \begin{pmatrix} N_1 \\ N_2 \end{pmatrix}$.

*   **Nature de $N$ :**
    Nous savons que $N_1 \sim \mathcal{N}(0, 1)$ et $N_2 \sim \mathcal{N}(0, 1)$.
    De plus, $N_1$ et $N_2$ sont des variables aléatoires indépendantes.
    Un vecteur aléatoire dont les composantes sont des variables aléatoires normales indépendantes est un vecteur gaussien.
    Par conséquent, $N$ est un vecteur gaussien.

*   **Paramètres de $N$ :**
    Le vecteur espérance de $N$ est $\mathbb{E}[N] = \begin{pmatrix} \mathbb{E}[N_1] \\ \mathbb{E}[N_2] \end{pmatrix}$.
    Puisque $N_1$ et $N_2$ sont centrées, $\mathbb{E}[N_1] = 0$ et $\mathbb{E}[N_2] = 0$.
    Ainsi, $\mathbb{E}[N] = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

    La matrice de covariance de $N$ est $\text{Cov}(N) = \begin{pmatrix} \text{Var}(N_1) & \text{Cov}(N_1, N_2) \\ \text{Cov}(N_2, N_1) & \text{Var}(N_2) \end{pmatrix}$.
    Puisque $N_1$ et $N_2$ sont réduites, $\text{Var}(N_1) = 1$ et $\text{Var}(N_2) = 1$.
    Puisque $N_1$ et $N_2$ sont indépendantes, $\text{Cov}(N_1, N_2) = 0$.
    Donc, $\text{Cov}(N) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$, la matrice identité d'ordre 2.

*   **Représentation de $M$ comme transformation affine :**
    Le vecteur $M = \begin{pmatrix} M_1 \\ M_2 \end{pmatrix}$ peut être exprimé comme une transformation affine du vecteur $N$.
    Nous avons :
    $M_1 = 2 N_1 + 1 N_2 + 5$
    $M_2 = 1 N_1 - 3 N_2 + 10$

    Ceci peut s'écrire sous forme matricielle $M = AN + b$, où $A$ est une matrice $2 \times 2$ et $b$ est un vecteur constant $2 \times 1$.
    En identifiant les coefficients, nous obtenons :
    $A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$
    $b = \begin{pmatrix} 5 \\ 10 \end{pmatrix}$

*   **Conclusion sur la nature gaussienne :**
    Un théorème fondamental de la théorie des vecteurs gaussiens stipule que toute transformation affine d'un vecteur gaussien est elle-même un vecteur gaussien.
    Puisque $N$ est un vecteur gaussien et $M = AN+b$ est une transformation affine de $N$, il s'ensuit que $M$ est un vecteur gaussien.

**2. Calcul du vecteur espérance $\mathbb{E}[M]$.**

Pour calculer le vecteur espérance de $M$, nous utilisons la propriété de linéarité de l'espérance mathématique pour les transformations affines de vecteurs aléatoires :
Pour un vecteur aléatoire $X$, une matrice constante $A$ et un vecteur constant $b$, on a $\mathbb{E}[AX+b] = A\mathbb{E}[X]+b$.

Dans notre cas, $X=N$, donc :
$\mathbb{E}[M] = \mathbb{E}[AN+b] = A\mathbb{E}[N]+b$.

Nous avons déjà déterminé les composants nécessaires :
$A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$
$\mathbb{E}[N] = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
$b = \begin{pmatrix} 5 \\ 10 \end{pmatrix}$

Effectuons le calcul étape par étape :
1.  Calcul du produit $A\mathbb{E}[N]$ :
    $A\mathbb{E}[N] = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
    $= \begin{pmatrix} (2 \times 0) + (1 \times 0) \\ (1 \times 0) + (-3 \times 0) \end{pmatrix}$
    $= \begin{pmatrix} 0 + 0 \\ 0 + 0 \end{pmatrix}$
    $= \begin{pmatrix} 0 \\ 0 \end{pmatrix}$

2.  Ajout du vecteur $b$ :
    $\mathbb{E}[M] = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 5 \\ 10 \end{pmatrix}$
    $= \begin{pmatrix} 0 + 5 \\ 0 + 10 \end{pmatrix}$
    $= \begin{pmatrix} 5 \\ 10 \end{pmatrix}$

Le vecteur espérance de $M$ est donc $\mathbb{E}[M] = \begin{pmatrix} 5 \\ 10 \end{pmatrix}$.

**3. Calcul de la matrice de covariance $\text{Cov}(M)$.**

Pour calculer la matrice de covariance de $M$, nous utilisons la propriété de la matrice de covariance pour une transformation affine :
Pour un vecteur aléatoire $X$, une matrice constante $A$ et un vecteur constant $b$, on a $\text{Cov}(AX+b) = A\text{Cov}(X)A^T$.
Notez que l'ajout d'un vecteur constant $b$ n'affecte pas la matrice de covariance.

Dans notre cas, $X=N$, donc :
$\text{Cov}(M) = A\text{Cov}(N)A^T$.

Nous avons déjà identifié les composants nécessaires :
$A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$
$\text{Cov}(N) = I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$

Nous devons également calculer la transposée de la matrice $A$, notée $A^T$. Pour une matrice $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, sa transposée est $A^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$.
Donc, pour $A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$, sa transposée est $A^T = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$. (Dans ce cas particulier, $A$ est une matrice symétrique).

Effectuons le calcul étape par étape :
1.  Calcul du produit $A\text{Cov}(N)$ :
    $A\text{Cov}(N) = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
    Puisque $\text{Cov}(N)$ est la matrice identité $I_2$, le produit $A I_2$ est simplement $A$.
    $A\text{Cov}(N) = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$

2.  Calcul du produit $(A\text{Cov}(N))A^T$ :
    $\text{Cov}(M) = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}$

    Effectuons la multiplication matricielle terme par terme :
    *   Le premier élément (ligne 1, colonne 1) est :
        $(2 \times 2) + (1 \times 1) = 4 + 1 = 5$
    *   Le deuxième élément (ligne 1, colonne 2) est :
        $(2 \times 1) + (1 \times (-3)) = 2 - 3 = -1$
    *   Le troisième élément (ligne 2, colonne 1) est :
        $(1 \times 2) + (-3 \times 1) = 2 - 3 = -1$
    *   Le quatrième élément (ligne 2, colonne 2) est :
        $(1 \times 1) + (-3 \times (-3)) = 1 + 9 = 10$

    Assemblons ces éléments pour former la matrice de covariance :
    $\text{Cov}(M) = \begin{pmatrix} 5 & -1 \\ -1 & 10 \end{pmatrix}$.

La matrice de covariance de $M$ est donc $\text{Cov}(M) = \begin{pmatrix} 5 & -1 \\ -1 & 10 \end{pmatrix}$.
Cette matrice est symétrique et définie positive, comme toute matrice de covariance valide.
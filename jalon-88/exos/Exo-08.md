# Produit de Cauchy d'espérances

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soient $X_1, X_2, \dots, X_n$ une suite de variables aléatoires de Bernoulli indépendantes, avec $\mathbb{P}(X_k = 1) = p_k$ et $\mathbb{P}(X_k = 0) = 1-p_k$.
On définit le produit $Y = \prod_{k=1}^n X_k$.
Montrer, par récurrence sur $n$, que $\mathbb{E}[Y] = \prod_{k=1}^n p_k$. Justifier rigoureusement chaque étape algébrique de la récurrence en utilisant les théorèmes du cours sur l'indépendance.

### Correction

Soit $X_1, X_2, \dots, X_n$ une suite de variables indépendantes de Bernoulli de paramètres respectifs $p_k$.

Démontrons par récurrence la proposition $P(n) : \mathbb{E}[\prod_{k=1}^n X_k] = \prod_{k=1}^n p_k$.

**Initialisation ($n=1$) :**
Pour $n=1$, le produit contient un seul terme, $Y = X_1$.
$\mathbb{E}[X_1] = 1 \times \mathbb{P}(X_1=1) + 0 \times \mathbb{P}(X_1=0) = p_1$.
La formule est triviale pour $n=1$. $P(1)$ est vraie.

**Hérédité :**
Supposons la proposition vraie pour un certain rang $n \geq 1$. Supposons $P(n)$ vraie.
Montrons que $P(n+1)$ est vraie, soit $\mathbb{E}[\prod_{k=1}^{n+1} X_k] = \prod_{k=1}^{n+1} p_k$.
On peut scinder le produit des $n+1$ termes en deux entités :
$Y_{n+1} = \left( \prod_{k=1}^n X_k \right) \times X_{n+1}$
Définissons $U_n = \prod_{k=1}^n X_k$.
Par hypothèse de l'énoncé, la famille $(X_1, \dots, X_n, X_{n+1})$ est mutuellement indépendante.
En vertu du Théorème 2 (Lemme des coalitions), toute fonction mesurable des variables $X_1, \dots, X_n$ est indépendante de $X_{n+1}$.
La multiplication étant une fonction mesurable, la variable aléatoire $U_n$ est indépendante de la variable aléatoire $X_{n+1}$.
D'après le Théorème 3 (Espérance du produit de variables indépendantes), l'espérance du produit est le produit des espérances :
$\mathbb{E}[Y_{n+1}] = \mathbb{E}[U_n \times X_{n+1}] = \mathbb{E}[U_n] \times \mathbb{E}[X_{n+1}]$
Par l'hypothèse de récurrence $P(n)$, on substitue $\mathbb{E}[U_n]$ :
$\mathbb{E}[Y_{n+1}] = \left( \prod_{k=1}^n p_k \right) \times \mathbb{E}[X_{n+1}]$
Or $\mathbb{E}[X_{n+1}] = p_{n+1}$. Donc :
$\mathbb{E}[Y_{n+1}] = \left( \prod_{k=1}^n p_k \right) \times p_{n+1} = \prod_{k=1}^{n+1} p_k$.
La proposition $P(n+1)$ est donc démontrée.

**Conclusion :** Par le principe de récurrence mathématique, la relation $\mathbb{E}[\prod_{k=1}^n X_k] = \prod_{k=1}^n p_k$ est vraie pour tout entier $n \geq 1$.

# Exercice 8

\subsection*{Exercice 8 : Indépendance et fonctions génératrices des moments \quad $\bigstar\bigstar\bigstar\bigstar\star$}

**Énoncé :**
Soient $X_1, X_2, \ldots, X_n$ des variables aléatoires indépendantes ayant des fonctions génératrices des moments $M_{X_i}(t) = \mathbb{E}[e^{tX_i}]$.
Montrer que la fonction génératrice des moments de la somme $S_n = \sum_{i=1}^n X_i$ est le produit des fonctions génératrices des $X_i$.
En déduire la loi de la somme de $n$ variables exponentielles indépendantes de même paramètre $\lambda$.

**Correction :**
1. Soit $S_n = X_1 + \ldots + X_n$. La fonction génératrice des moments de $S_n$ est $M_{S_n}(t) = \mathbb{E}[e^{tS_n}]$.
2. $M_{S_n}(t) = \mathbb{E}[e^{t(X_1 + \ldots + X_n)}] = \mathbb{E}[e^{tX_1} e^{tX_2} \ldots e^{tX_n}]$.
3. Par le lemme des coalitions, les variables $e^{tX_i}$ sont mutuellement indépendantes (car les $X_i$ le sont et $x \mapsto e^{tx}$ est mesurable).
4. L'espérance du produit de variables aléatoires indépendantes est égale au produit de leurs espérances :
   $M_{S_n}(t) = \mathbb{E}[e^{tX_1}] \times \mathbb{E}[e^{tX_2}] \times \ldots \times \mathbb{E}[e^{tX_n}]$.
5. Ainsi, $M_{S_n}(t) = \prod_{i=1}^n M_{X_i}(t)$.
6. Application : soit $X_i \sim \mathcal{E}(\lambda)$. Sa fonction génératrice des moments est, pour $t < \lambda$, $M_{X_i}(t) = \frac{\lambda}{\lambda - t} = \left(1 - \frac{t}{\lambda}\right)^{-1}$.
7. Pour $S_n$, on a $M_{S_n}(t) = \prod_{i=1}^n \left(1 - \frac{t}{\lambda}\right)^{-1} = \left(1 - \frac{t}{\lambda}\right)^{-n}$.
8. On reconnaît la fonction génératrice des moments de la loi Gamma de paramètres $(n, \lambda)$.
9. Donc la somme de $n$ lois exponentielles $\mathcal{E}(\lambda)$ indépendantes suit une loi Gamma $\Gamma(n, \lambda)$ (aussi appelée loi d'Erlang).

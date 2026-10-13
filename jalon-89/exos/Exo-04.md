# Exercice 4

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Variables de Bernoulli asymétriques

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires indépendantes suivant la loi de Bernoulli de paramètre $p_n = e^{-n}$.
Montrer que la somme $S = \sum_{n=1}^{\infty} X_n$ est presque sûrement finie.

**Correction détaillée :**
1. $X_n \sim \mathcal{B}(p_n)$, donc $\mathbb{P}(X_n = 1) = e^{-n}$. Soit l'événement $A_n = \{X_n = 1\}$.
2. Étudions la série $\sum_{n=1}^{\infty} \mathbb{P}(A_n) = \sum_{n=1}^{\infty} e^{-n}$.
3. Il s'agit d'une série géométrique de raison $e^{-1}$. Comme $|e^{-1}| < 1$, la série est convergente.
4. Par le premier lemme de Borel-Cantelli, on déduit que $\mathbb{P}(\limsup A_n) = 0$.
5. Ainsi, presque sûrement, il n'existe qu'un nombre fini d'indices $n$ pour lesquels $X_n = 1$. Pour tous les autres indices assez grands, $X_n = 0$.
6. Si $X_n = 0$ à partir d'un certain rang, la série $S(\omega) = \sum_{n=1}^{\infty} X_n(\omega)$ comporte un nombre fini de termes non nuls.
7. Par conséquent, cette somme est finie. Presque sûrement, $S < +\infty$.

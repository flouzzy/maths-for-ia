---
title: "Suite décroissante (Contre-exemple)"
difficulty: $\bigstar\bigstar\star\star\star$
---
# Suite décroissante (Contre-exemple)
**Énoncé :**
Soit $f_n(x) = \mathbf{1}_{[n, +\infty[}(x)$ pour $x \in \mathbb{R}$.
Calculer $\int f_n d\lambda$ et $\int \lim f_n d\lambda$. Le TCM s'applique-t-il ?

**Correction :**
1. Pour tout $n$, $\int_{\mathbb{R}} f_n d\lambda = \lambda([n, +\infty[) = +\infty$.
   Donc $\lim_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda = +\infty$.
2. Pour tout $x \in \mathbb{R}$, il existe $N$ tel que $n > N \implies n > x$, donc $f_n(x) = 0$.
   Ainsi, $\lim_{n \to \infty} f_n(x) = 0$ partout. L'intégrale de la limite est $0$.
3. On a $+\infty \neq 0$.
4. Le TCM ne s'applique pas car la suite $(f_n)$ est **décroissante** et non croissante. De plus, aucune des fonctions n'est intégrable pour initialiser un théorème de convergence dominée.

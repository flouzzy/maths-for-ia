# Exercice 8 : Produit de fonctions dans les espaces Lp (Hölder élémentaire)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $X$ un espace mesuré.
1. Soit $f \in L^1(X)$ et $g \in L^\infty(X)$. Montrer rigoureusement que le produit $fg$ appartient à $L^1(X)$ et que $\|fg\|_1 \le \|f\|_1 \|g\|_\infty$.
2. Application : Si la mesure de l'espace $\mu(X)$ est finie, montrer que pour toute fonction $f \in L^\infty(X)$, alors $f \in L^p(X)$ pour tout $p \ge 1$.

---

## Correction détaillée

1. **Produit $L^1 \times L^\infty$ :**
   $g \in L^\infty(X)$, donc il existe une constante $C = \|g\|_\infty$ telle que $|g(x)| \le C$ presque partout.
   $f \in L^1(X)$, donc $f$ est mesurable et $\int_X |f| \, d\mu < +\infty$.
   La fonction produit $fg$ est mesurable.
   Considérons son intégrale de module :
   $$ \int_X |f(x)g(x)| \, d\mu = \int_X |f(x)| |g(x)| \, d\mu $$
   Puisque $|g(x)| \le \|g\|_\infty$ p.p., et que $|f(x)| \ge 0$, on a presque partout :
   $$ |f(x)| |g(x)| \le |f(x)| \|g\|_\infty $$
   Par croissance de l'intégrale :
   $$ \int_X |fg| \, d\mu \le \int_X |f| \|g\|_\infty \, d\mu = \|g\|_\infty \int_X |f| \, d\mu = \|g\|_\infty \|f\|_1 $$
   Cette quantité est finie, donc $fg \in L^1(X)$. On a bien $\|fg\|_1 \le \|f\|_1 \|g\|_\infty$.

2. **Espace de mesure finie :**
   Supposons $\mu(X) < +\infty$. Soit $f \in L^\infty(X)$.
   Soit $p \ge 1$. Nous devons estimer $\int_X |f|^p \, d\mu$.
   Puisque $|f| \le \|f\|_\infty$ presque partout, en élevant à la puissance $p$ :
   $$ |f|^p \le \|f\|_\infty^p \quad \text{p.p.} $$
   On intègre sur $X$ :
   $$ \int_X |f|^p \, d\mu \le \int_X \|f\|_\infty^p \, d\mu = \|f\|_\infty^p \int_X 1 \, d\mu = \|f\|_\infty^p \mu(X) $$
   Puisque $\mu(X) < +\infty$, l'intégrale est finie. Donc $f \in L^p(X)$.
   De plus, en prenant la racine $p$-ième :
   $$ \|f\|_p \le \|f\|_\infty \mu(X)^{1/p} $$
   Ceci généralise l'inclusion $L^\infty \subset L^p$ sur un espace de mesure finie.

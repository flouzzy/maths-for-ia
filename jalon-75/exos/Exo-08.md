\subsection*{Exercice 8 : Produit de convolution dans $L^1$ \quad $\bigstar\bigstar\bigstar$}
**Énoncé :**
Soient $f, g \in L^1(\mathbb{R})$. On définit le produit de convolution $f * g(x) = \int_{\mathbb{R}} f(x-y)g(y) \, dy$.
1. Montrer que $f * g(x)$ est bien définie presque partout.
2. Montrer que $f * g \in L^1(\mathbb{R})$ et que $\|f * g\|_1 \le \|f\|_1 \|g\|_1$ (Inégalité de Young pour $L^1$).

**Correction détaillée :**
1. Considérons la fonction de deux variables $F(x,y) = f(x-y)g(y)$. Elle est mesurable.
   On intègre sa valeur absolue sur $\mathbb{R}^2$ et on utilise le théorème de Tonelli-Fubini :
   $\iint |F(x,y)| \, dx \, dy = \int \left( \int |f(x-y)| \, dx \right) |g(y)| \, dy$.
   Par invariance de la mesure par translation, $\int |f(x-y)| \, dx = \|f\|_1$.
   Donc $\iint |F(x,y)| \, dx \, dy = \|f\|_1 \int |g(y)| \, dy = \|f\|_1 \|g\|_1$.
   Cette double intégrale est finie, donc par le théorème de Fubini, la fonction $x \mapsto F(x,y)$ est intégrable pour presque tout $x$.
2. Ainsi, $f * g(x)$ est définie presque partout. De plus :
   $\|f * g\|_1 = \int \left| \int f(x-y)g(y) \, dy \right| dx \le \iint |f(x-y)g(y)| \, dx \, dy = \|f\|_1 \|g\|_1$.
   L'espace $L^1(\mathbb{R})$ muni de la convolution devient ainsi une algèbre de Banach. \qed

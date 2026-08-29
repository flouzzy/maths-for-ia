# Exercice 2 : Interversion série-intégrale avancée $\bigstar\bigstar\star\star\star$

## Énoncé
Calculer la valeur de $\int_0^\infty \frac{x}{e^x - 1} dx$ sachant que $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

## Correction Détaillée
1. L'intégrande peut s'écrire sous forme de série :
   $$ \frac{x}{e^x - 1} = \frac{x e^{-x}}{1 - e^{-x}} $$
2. Pour $x > 0$, on a $0 < e^{-x} < 1$, donc on peut développer $(1 - e^{-x})^{-1}$ en série géométrique :
   $$ \frac{x e^{-x}}{1 - e^{-x}} = x e^{-x} \sum_{n=0}^\infty (e^{-x})^n = \sum_{n=0}^\infty x e^{-(n+1)x} $$
   En posant $k = n+1$, on obtient $\sum_{k=1}^\infty x e^{-kx}$.
3. Posons $u_k(x) = x e^{-kx}$. Ces fonctions sont mesurables et positives sur $]0, \infty[$.
4. Le corollaire du Théorème de Convergence Monotone de Beppo Levi autorise l'interversion :
   $$ \int_0^\infty \sum_{k=1}^\infty x e^{-kx} dx = \sum_{k=1}^\infty \int_0^\infty x e^{-kx} dx $$
5. Pour calculer $\int_0^\infty x e^{-kx} dx$, on utilise une intégration par parties :
   - $u = x \implies u' = 1$
   - $v' = e^{-kx} \implies v = -\frac{1}{k}e^{-kx}$
   $$ \int_0^\infty x e^{-kx} dx = \left[ -x \frac{e^{-kx}}{k} \right]_0^\infty - \int_0^\infty 1 \cdot \left(-\frac{1}{k}e^{-kx}\right) dx $$
   Le terme de bord est nul, il reste $\frac{1}{k} \int_0^\infty e^{-kx} dx = \frac{1}{k^2}$.
6. Finalement :
   $$ \int_0^\infty \frac{x}{e^x - 1} dx = \sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6} $$

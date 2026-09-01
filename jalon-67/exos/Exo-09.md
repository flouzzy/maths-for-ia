# Exercice 9 : Mesure de Dirac exponentielle

**Difficulté :** $\bigstar\bigstar\star$

**Énoncé :**
Soit $\mu = \sum_{k=1}^\infty \frac{1}{k^2} \delta_k$. Calculer $\int x^2 e^{-x} d\mu(x)$.

**Correction :**
Posons $f(x) = x^2 e^{-x}$. On a $\int f d\mu = \int f d(\lim_{N} \sum_{1}^N \frac{1}{k^2} \delta_k)$. Par le TCM appliqué aux suites croissantes de mesures $\mu_N = \sum_1^N \frac{1}{k^2} \delta_k$, on obtient $\lim_N \int f d\mu_N = \lim_N \sum_1^N f(k) \frac{1}{k^2} = \sum_{k=1}^\infty \frac{k^2 e^{-k}}{k^2} = \sum_{k=1}^\infty e^{-k}$. C'est une série géométrique de raison $e^{-1} < 1$, sa somme est $\frac{e^{-1}}{1-e^{-1}} = \frac{1}{e-1}$. $\blacksquare$

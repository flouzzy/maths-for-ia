# Régularité et décroissance des coefficients

$\bigstar\bigstar\bigstar\star\star$

Soit $f$ une fonction $2\pi$-périodique de classe $C^k$ sur $\mathbb{R}$.
1. Démontrer, à l'aide d'intégrations par parties, que $c_n(f') = in c_n(f)$.
2. En déduire que $c_n(f^{(k)}) = (in)^k c_n(f)$.
3. Montrer que $c_n(f) = o(1/n^k)$ quand $|n| \to +\infty$.

**Correction détaillée :**
1. Calculons $c_n(f')$ par définition :
   $$ c_n(f') = \frac{1}{2\pi} \int_{-\pi}^\pi f'(t) e^{-int} dt $$
   On intègre par parties avec $u = e^{-int}$ et $v' = f'(t)$. Les fonctions sont $C^1$.
   $$ c_n(f') = \frac{1}{2\pi} \left( [f(t) e^{-int}]_{-\pi}^\pi - \int_{-\pi}^\pi f(t) (-in) e^{-int} dt \right) $$
   Puisque $f$ et $t \mapsto e^{-int}$ sont $2\pi$-périodiques, leurs valeurs en $\pi$ et $-\pi$ sont égales. Donc $[f(t) e^{-int}]_{-\pi}^\pi = 0$.
   $$ c_n(f') = \frac{in}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} dt = in \, c_n(f) $$
2. Par une récurrence immédiate. C'est vrai pour $k=1$. Supposons $c_n(f^{(p)}) = (in)^p c_n(f)$. Alors pour $f^{(p+1)} = (f^{(p)})'$, la fonction est $C^1$ car $f \in C^k$ et $p < k$.
   $$ c_n(f^{(p+1)}) = in \, c_n(f^{(p)}) = in (in)^p c_n(f) = (in)^{p+1} c_n(f) $$
   Donc $c_n(f^{(k)}) = (in)^k c_n(f)$.
3. Puisque $f^{(k)}$ est continue sur $[-\pi, \pi]$, elle est intégrable, et on peut lui appliquer le lemme de Riemann-Lebesgue :
   $$ \lim_{|n| \to +\infty} c_n(f^{(k)}) = 0 $$
   Or $c_n(f^{(k)}) = (in)^k c_n(f)$, ce qui implique que $|n|^k |c_n(f)| \to 0$ quand $|n| \to +\infty$.
   Ceci se réécrit exactement : $|c_n(f)| = o(\frac{1}{|n|^k})$, ce qui montre que la décroissance des coefficients de Fourier est d'autant plus rapide que la fonction est régulière (indéfiniment dérivable implique décroissance plus rapide que toute puissance inverse).
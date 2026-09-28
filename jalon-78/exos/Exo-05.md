# Exercice 5 : La fonction indicatrice d'un sous-intervalle $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $I = [-\alpha, \alpha]$ avec $0 < \alpha < \pi$.
Soit $f$ la fonction $2\pi$-périodique valant $1$ sur $I$ et $0$ sur $]-\pi, \pi] \setminus I$.
Calculer la série de Fourier de $f$ et en déduire la valeur de $\sum_{n=1}^{\infty} \frac{\sin(n\alpha)}{n}$.

**Correction Détaillée :**
1. **Coefficients :**
$f$ est paire, donc $b_n = 0$.
$a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) dt = \frac{1}{\pi} \int_{-\alpha}^{\alpha} 1 dt = \frac{2\alpha}{\pi}$.
Pour $n \ge 1$ :
$$ a_n = \frac{2}{\pi} \int_0^\pi f(t) \cos(nt) dt = \frac{2}{\pi} \int_0^\alpha \cos(nt) dt = \frac{2}{\pi} \left[ \frac{\sin(nt)}{n} \right]_0^\alpha = \frac{2\sin(n\alpha)}{n\pi} $$
La série est :
$$ S(f)(t) = \frac{\alpha}{\pi} + \sum_{n=1}^\infty \frac{2\sin(n\alpha)}{n\pi} \cos(nt) $$

2. **Somme de série :**
Pour $t=0$, $f$ est continue et $f(0)=1$. Par Dirichlet :
$$ 1 = \frac{\alpha}{\pi} + \frac{2}{\pi} \sum_{n=1}^\infty \frac{\sin(n\alpha)}{n} \implies \sum_{n=1}^\infty \frac{\sin(n\alpha)}{n} = \frac{\pi - \alpha}{2} $$

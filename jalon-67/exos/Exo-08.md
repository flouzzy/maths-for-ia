# Exercice 8 : Fonction de Weierstrass et intégration

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

On pose $f(x) = \sum_{n=0}^\infty 2^{-n} \cos(3^n x)$. Bien que continue et nulle part dérivable, montrer que son intégrale sur $[0, t]$ est bien définie et calculer cette primitive en justifiant l'interversion par les théorèmes de Lebesgue.

## Démonstration rigoureuse pas à pas

Soit $g_N(x) = \sum_{n=0}^N 2^{-n} \cos(3^n x)$. La série est normalement (donc uniformément) convergente sur $\mathbb{R}$ car $|2^{-n} \cos(3^n x)| \le 2^{-n}$ terme général d'une série géométrique convergente. De plus, on peut séparer en termes positifs et negatifs et appliquer le theoreme sur des dominants. Ici la majoration uniforme par une constante sur un intervalle borné $[0,t]$ suffit. Par Beppo-Levi (ou convergence dominée), on intègre terme à terme : $\int_0^t f(x) dx = \sum_{n=0}^\infty 2^{-n} \int_0^t \cos(3^n x) dx = \sum_{n=0}^\infty 2^{-n} \frac{\sin(3^n t)}{3^n} = \sum_{n=0}^\infty \frac{\sin(3^n t)}{6^n}$.

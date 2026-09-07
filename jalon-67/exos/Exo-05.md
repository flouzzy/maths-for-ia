# Exercice 5 : Intégrale sur la mesure de Dirac \quad $\bigstar\bigstar\bigstar\star\star$

Soit $\mu = \delta_0$ la mesure de Dirac en 0. Calculer $\lim \int_{\mathbb{R}} e^{-x^2/n} d\delta_0(x)$.

**Correction :**
$f_n(x) = e^{-x^2/n}$ est mesurable, strictement positive. On a $f_n(x) \le f_{n+1}(x)$ car $-x^2/n \le -x^2/(n+1)$. La limite est $f(x) = 1$. Par Beppo Levi, $\lim \int f_n d\delta_0 = \int 1 d\delta_0 = 1(0) = 1$. En calcul direct, $\int f_n d\delta_0 = f_n(0) = 1$ constant.

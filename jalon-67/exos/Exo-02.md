# Exercice 2 : Convergence vers l'infini sur un compact
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit $f_n(x) = n e^{-nx} \mathbf{1}_{[0, 1]}(x)$. Montrer que $(f_n)$ converge simplement vers 0 presque partout. Le TCM s'applique-t-il ?

## Correction Détaillée

Pour $x > 0$, $\lim_{n \to +\infty} n e^{-nx} = 0$ par croissances comparées. En $x=0$, $f_n(0) = n \to +\infty$.
Donc la suite converge simplement vers 0 presque partout (partout sauf en $x=0$, qui est de mesure de Lebesgue nulle).
Regardons les intégrales :
$\int_0^1 n e^{-nx} dx = \left[ -e^{-nx} \right]_0^1 = 1 - e^{-n}$.
$\lim_{n \to +\infty} \int_0^1 f_n(x) dx = \lim_{n \to +\infty} (1 - e^{-n}) = 1$.
Cependant, l'intégrale de la limite est $\int_0^1 0 \, dx = 0$.
L'égalité n'est pas vérifiée ($1 \neq 0$). Le Théorème de Convergence Monotone ne s'applique pas car la suite $(f_n)$ **n'est pas croissante**. En effet, pour $x=1$, $f_1(1) = 1/e \approx 0.36$ et $f_2(1) = 2/e^2 \approx 0.27$, donc $f_2(1) < f_1(1)$.

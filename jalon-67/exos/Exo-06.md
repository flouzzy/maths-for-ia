# Exercice 6 : Limite d'intégrale de Lebesgue avec limite de fonctions en escalier
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Calculer $\lim_{n \to +\infty} \int_0^1 \frac{nx}{1 + n^2 x^2} dx$. Peut-on utiliser le TCM ?

## Correction Détaillée

Soit $f_n(x) = \frac{nx}{1 + n^2 x^2}$. Pour $x>0$, on a $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{1}{nx} = 0$. En $x=0$, $f_n(0) = 0$. Donc $f_n \to 0$ p.p. sur $[0, 1]$.
Calculons $\int_0^1 f_n(x) dx = \frac{1}{2n} \int_0^1 \frac{2n^2 x}{1 + n^2 x^2} dx = \frac{1}{2n} \left[ \ln(1 + n^2 x^2) \right]_0^1 = \frac{\ln(1+n^2)}{2n}$.
La limite de l'intégrale est $\lim_{n \to \infty} \frac{\ln(1+n^2)}{2n} = 0$.
Dans ce cas, l'intégrale de la limite (qui vaut 0) est égale à la limite de l'intégrale.
Cependant, peut-on appliquer Beppo-Levi ? Non, car la suite $(f_n(x))$ n'est pas croissante ! Par exemple pour $x=1$, $f_1(1) = 1/2$, mais $f_2(1) = 2/5 = 0.4 < 0.5$. La non-croissance interdit l'usage du TCM, bien que le résultat final (0) soit correct par le Théorème de Convergence Dominée (qui sera vu plus tard, car $f_n(x) \leq 1/2$).

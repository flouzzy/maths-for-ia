---
title: "Exercice 4 : L'intégrale de Gauss et la limite de Riemann"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 4 : L'intégrale de Gauss et la limite de Riemann

## Énoncé

Soit $f_n(x) = \left( 1 - \frac{x}{n} \right)^n \mathbf{1}_{[0, n]}(x)$.
1. Montrer que la suite $(f_n)$ converge ponctuellement vers la fonction exponentielle $x \mapsto e^{-x}$.
2. Démontrer, en utilisant une inégalité classique, que la suite $(f_n)$ est croissante.
3. En déduire la valeur de $\int_0^\infty e^{-x} dx$ par passage à la limite sur des intégrales de polynômes sur un domaine borné.

## Correction

1. **Limite ponctuelle :**
Fixons $x \ge 0$. Pour $n > x$, $x/n < 1$.
On prend le logarithme : $\ln f_n(x) = n \ln(1 - x/n)$.
Par développement limité à l'ordre 1 au voisinage de 0, $\ln(1 - u) = -u + o(u)$.
Donc $\ln f_n(x) = n (-x/n + o(1/n)) = -x + o(1)$.
En passant à l'exponentielle (qui est continue), on obtient $\lim_{n \to \infty} f_n(x) = e^{-x}$.

2. **Croissance de la suite :**
Nous devons montrer que $(1 - x/n)^n \le (1 - x/(n+1))^{n+1}$ pour $x \in [0, n]$.
Si $x \in [0, n]$, alors $1 - x/n \ge 0$.
Appliquons l'inégalité de Bernoulli : $(1 + u)^p \ge 1 + pu$ pour $u \ge -1$ et $p \ge 1$.
Posons le rapport :
$$ \frac{f_{n+1}(x)}{f_n(x)} = \frac{(1 - x/(n+1))^{n+1}}{(1 - x/n)^n} = (1 - x/n) \left( \frac{1 - x/(n+1)}{1 - x/n} \right)^{n+1} $$
L'expression dans la parenthèse est $\frac{n(n+1-x)}{(n+1)(n-x)} = \frac{n^2+n-nx}{n^2+n-nx-x} = 1 + \frac{x}{(n+1)(n-x)}$.
Par Bernoulli avec l'exposant $n+1$ :
$$ \left( 1 + \frac{x}{(n+1)(n-x)} \right)^{n+1} \ge 1 + (n+1) \frac{x}{(n+1)(n-x)} = 1 + \frac{x}{n-x} = \frac{n}{n-x} = \left( 1 - \frac{x}{n} \right)^{-1} $$
En multipliant par $1 - x/n$, on trouve $\frac{f_{n+1}(x)}{f_n(x)} \ge (1 - x/n) \times (1 - x/n)^{-1} = 1$.
Donc $f_n(x) \le f_{n+1}(x)$, la suite est bien croissante.

3. **Application de Beppo Levi :**
Les fonctions $f_n$ sont mesurables, positives, et croissent vers $f(x) = e^{-x}$.
Par le TCM, $\int_0^\infty e^{-x} dx = \lim_{n \to \infty} \int_0^n \left( 1 - \frac{x}{n} \right)^n dx$.
Le changement de variable $u = 1 - x/n \implies dx = -n du$ donne :
$\int_0^n (1 - x/n)^n dx = \int_1^0 u^n (-n du) = n \int_0^1 u^n du = n \left[ \frac{u^{n+1}}{n+1} \right]_0^1 = \frac{n}{n+1}$.
La limite quand $n \to \infty$ est 1.
On retrouve rigoureusement $\int_0^\infty e^{-x} dx = 1$.

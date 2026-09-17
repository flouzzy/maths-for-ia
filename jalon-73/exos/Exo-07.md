# Exercice 7 : Une fonction dans l'intersection de tous les $L^p$, mais pas dans $L^\infty$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Sur $X = [0, 1/2]$ muni de la mesure de Lebesgue, on considère la fonction $f(x) = -\ln(x)$ pour $x > 0$ et $f(0) = 0$.
Montrer que $f \in L^p(\lambda)$ pour tout $1 \le p < +\infty$, mais que $f \notin L^\infty(\lambda)$.

**Correction :**
1. Soit $p \ge 1$.
$\int_0^{1/2} |f(x)|^p dx = \int_0^{1/2} (-\ln(x))^p dx$.
Faisons le changement de variable $u = -\ln(x) \iff x = e^{-u}$, $dx = -e^{-u} du$.
Les bornes : $x=0 \implies u = +\infty$, $x=1/2 \implies u = \ln(2)$.
L'intégrale devient $\int_{\ln(2)}^{+\infty} u^p e^{-u} du$.
Cette intégrale converge car l'exponentielle l'emporte sur toute puissance polynomiale : $u^p e^{-u} \underset{u \to +\infty}{=} o(e^{-u/2})$, et $\int e^{-u/2} du$ converge.
Donc $f \in L^p(\lambda)$.

2. $f(x) = -\ln(x)$ tend vers $+\infty$ lorsque $x \to 0^+$.
Pour tout $C > 0$, l'ensemble $\{x \in [0, 1/2] \mid f(x) > C\} = \{x \in [0, 1/2] \mid x < e^{-C}\} = [0, e^{-C}[$ est de mesure $e^{-C} > 0$.
Donc $f$ n'est pas essentiellement bornée. Ainsi, $f \notin L^\infty(\lambda)$.

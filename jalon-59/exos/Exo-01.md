### Exercice 1 : Étude de convergence simple et uniforme \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit la suite de fonctions définie sur $X = [0, 1]$ par $f_n(x) = \frac{nx}{1 + n^2 x^2}$.
1. Étudier la convergence simple de la suite $(f_n)$.
2. Étudier la convergence uniforme sur $[0, 1]$.
3. Étudier la convergence uniforme sur $[a, 1]$ avec $a > 0$.

**Correction :**
1. Pour $x = 0$, $f_n(0) = 0 \to 0$. Pour $x \in ]0, 1]$, $f_n(x) \sim \frac{nx}{n^2 x^2} = \frac{1}{nx} \to 0$. La limite simple est donc la fonction nulle $f(x) = 0$.
2. Étudions la convergence uniforme. La dérivée est $f_n'(x) = \frac{n(1 + n^2 x^2) - nx(2n^2 x)}{(1 + n^2 x^2)^2} = \frac{n(1 - n^2 x^2)}{(1 + n^2 x^2)^2}$.
Elle s'annule en $x_n = \frac{1}{n}$. Le maximum de $f_n$ sur $[0, 1]$ est $f_n(x_n) = \frac{1}{1+1} = \frac{1}{2}$.
Ainsi, $\sup_{x \in [0, 1]} |f_n(x) - 0| = \frac{1}{2} \not\to 0$. La convergence n'est pas uniforme sur $[0, 1]$.
3. Sur $[a, 1]$, pour $n$ assez grand tel que $\frac{1}{n} < a$, la fonction $f_n$ est décroissante. Le maximum sur cet intervalle est atteint en $a$, valant $\frac{na}{1 + n^2 a^2}$. Or $\frac{na}{1 + n^2 a^2} \to 0$. Donc la convergence est uniforme sur tout segment ne contenant pas 0.

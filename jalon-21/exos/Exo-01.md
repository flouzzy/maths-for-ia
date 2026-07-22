# Exercice 1 : Étude complète d'une convergence simple et uniforme
**Énoncé :**
Pour tout entier $n \ge 1$, on définit la fonction $f_n : \mathbb{R}_+ \to \mathbb{R}$ par :
$$f_n(x) = \frac{nx}{1 + n^2 x^2}$$
1. Étudier la convergence simple de la suite $(f_n)_{n \ge 1}$ sur $\mathbb{R}_+$.
2. Étudier la convergence uniforme sur $\mathbb{R}_+$, puis sur des intervalles de la forme $[a, +\infty[$ avec $a > 0$.

**Solution Rigoureuse :**
1. **Convergence simple :**
Soit $x \in \mathbb{R}_+$ fixé.
Si $x = 0$, pour tout $n \ge 1$, $f_n(0) = 0$. Donc $\lim_{n \to +\infty} f_n(0) = 0$.
Si $x > 0$, on a :
$$f_n(x) = \frac{nx}{n^2 x^2(1 + \frac{1}{n^2 x^2})} = \frac{1}{nx(1 + \frac{1}{n^2 x^2})}$$
Comme $x > 0$, $\lim_{n \to +\infty} nx = +\infty$, d'où $\lim_{n \to +\infty} f_n(x) = 0$.
Ainsi, la suite de fonctions $(f_n)_{n \ge 1}$ converge simplement vers la fonction nulle $f = 0$ sur $\mathbb{R}_+$.

2. **Convergence uniforme sur $\mathbb{R}_+$ :**
Pour étudier la convergence uniforme, nous devons calculer la norme $\|f_n - f\|_{\infty, \mathbb{R}_+} = \sup_{x \in \mathbb{R}_+} |f_n(x)|$.
Les fonctions $f_n$ sont dérivables sur $\mathbb{R}_+$. Calculons la dérivée :
$$f_n'(x) = \frac{n(1 + n^2 x^2) - nx(2n^2 x)}{(1 + n^2 x^2)^2} = \frac{n(1 - n^2 x^2)}{(1 + n^2 x^2)^2}$$
La dérivée s'annule en $x = \frac{1}{n}$, est positive sur $[0, \frac{1}{n}[$ et négative sur $]\frac{1}{n}, +\infty[$.
Ainsi, $f_n$ atteint son maximum global sur $\mathbb{R}_+$ en $x_n = \frac{1}{n}$.
La valeur de ce maximum est :
$$f_n\left(\frac{1}{n}\right) = \frac{n \cdot \frac{1}{n}}{1 + n^2 \cdot \frac{1}{n^2}} = \frac{1}{1 + 1} = \frac{1}{2}$$
Par conséquent, $\sup_{x \in \mathbb{R}_+} |f_n(x)| = \frac{1}{2}$.
Puisque $\lim_{n \to +\infty} \|f_n\|_{\infty, \mathbb{R}_+} = \frac{1}{2} \neq 0$, la suite $(f_n)$ **ne converge pas uniformément** vers $0$ sur $\mathbb{R}_+$.

3. **Convergence uniforme sur $[a, +\infty[$ avec $a > 0$ :**
Soit $a > 0$. Pour $n$ suffisamment grand (précisément $n \ge \frac{1}{a}$), on a $\frac{1}{n} \le a$.
Sur l'intervalle $[a, +\infty[$, la fonction $f_n$ est strictement décroissante car $x \ge a \ge \frac{1}{n}$.
Donc le supremum de $f_n$ sur $[a, +\infty[$ est atteint en $x = a$ :
$$\sup_{x \in [a, +\infty[} |f_n(x)| = f_n(a) = \frac{na}{1 + n^2 a^2}$$
Or, $\lim_{n \to +\infty} \frac{na}{1 + n^2 a^2} = 0$.
Il s'ensuit que la suite converge uniformément sur tout intervalle de la forme $[a, +\infty[$ avec $a > 0$.

# Exercice 3 : Application du Théorème de Dini
**Énoncé :**
Soit $f_n(x) = \left(1 - \frac{x}{n}\right)^n$ pour $x \in [0, A]$ où $A > 0$ est fixé.
Montrer que $f_n$ converge uniformément vers $e^{-x}$ sur $[0, A]$.

**Solution Rigoureuse :**
On sait que pour tout $x \in [0, A]$ fixé, $\lim_{n \to +\infty} \left(1 - \frac{x}{n}\right)^n = e^{-x}$.
La suite $(f_n)$ converge donc simplement vers $f(x) = e^{-x}$ sur $[0, A]$.
La limite $f$ est une fonction continue sur le compact $[0, A]$.
Pour appliquer le théorème de Dini, il faut vérifier que pour tout $x \in [0, A]$, la suite $(f_n(x))_{n \ge 1}$ est monotone, pour $n$ assez grand ($n \ge A$).
Soit $x \in [0, A]$. Posons $u_n = n \ln(1 - \frac{x}{n})$ (pour $n > A$).
On étudie la fonction $\phi(t) = t \ln(1 - \frac{x}{t})$ pour $t \in ]A, +\infty[$.
La dérivée est :
$$\phi'(t) = \ln(1 - \frac{x}{t}) + t \frac{\frac{x}{t^2}}{1 - \frac{x}{t}} = \ln(1 - \frac{x}{t}) + \frac{x}{t - x}$$
Posons $u = \frac{x}{t}$, avec $0 \le u < 1$. Alors $\phi'(t) = \ln(1-u) + \frac{u}{1-u}$.
La fonction $\psi(u) = \ln(1-u) + \frac{u}{1-u}$ a pour dérivée $\psi'(u) = \frac{-1}{1-u} + \frac{1-u+u}{(1-u)^2} = \frac{u}{(1-u)^2} \ge 0$.
Comme $\psi(0) = 0$, $\psi(u) \ge 0$ pour tout $u \in [0, 1[$.
Ainsi $\phi'(t) \ge 0$. La suite $n \mapsto f_n(x)$ est donc croissante pour tout $n > A$.
Les hypothèses du théorème de Dini sont réunies :
1. $K = [0, A]$ est compact.
2. $(f_n)$ est une suite de fonctions continues sur $K$.
3. La suite $(f_n(x))$ est croissante pour chaque $x \in K$.
4. La fonction limite $f$ est continue sur $K$.
Par le théorème de Dini, la convergence est **uniforme** sur $[0, A]$.

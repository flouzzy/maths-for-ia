# Exercice 6 : Convergence et suites de polynômes
**Énoncé :**
Soit $f_n(x) = n x (1 - x^2)^n$ sur $[0, 1]$. Étudier les convergences, et évaluer $\lim_{n \to +\infty} \int_0^1 f_n(x) dx$ comparativement à l'intégrale de la limite.

**Solution Rigoureuse :**
1. **Convergence simple :**
Si $x = 0$ ou $x = 1$, $f_n(x) = 0$ pour tout $n$.
Si $x \in ]0, 1[$, on a $0 < 1 - x^2 < 1$. Posons $q = 1 - x^2$. $f_n(x) = x n q^n$.
Par croissances comparées, $\lim_{n \to +\infty} n q^n = 0$.
La suite converge simplement vers la fonction nulle $f \equiv 0$ sur $[0, 1]$.

2. **Intégrales :**
Calculons l'intégrale de $f_n$ :
$$I_n = \int_0^1 n x (1 - x^2)^n dx$$
Posons $u = 1 - x^2$, $du = -2x dx$. Pour $x=0, u=1$, et pour $x=1, u=0$.
$$I_n = \int_1^0 n \left( \frac{-du}{2} \right) u^n = \frac{n}{2} \int_0^1 u^n du = \frac{n}{2} \left[ \frac{u^{n+1}}{n+1} \right]_0^1 = \frac{n}{2(n+1)}$$
On a alors $\lim_{n \to +\infty} I_n = \frac{1}{2}$.
Cependant, $\int_0^1 f(x) dx = \int_0^1 0 dx = 0$.
Il y a défaut de commutation limite-intégrale :
$$\lim_{n \to +\infty} \int_0^1 f_n \neq \int_0^1 \lim_{n \to +\infty} f_n$$

3. **Conséquence sur la convergence uniforme :**
Par contraposée du théorème d'intégration sur un segment, la suite $(f_n)$ **ne converge pas uniformément** vers $0$ sur $[0, 1]$.
En cherchant le maximum par la dérivée : $f_n'(x) = n(1-x^2)^n - 2n^2 x^2 (1-x^2)^{n-1} = n(1-x^2)^{n-1}(1 - x^2 - 2nx^2) = n(1-x^2)^{n-1}(1 - (2n+1)x^2)$.
Le maximum est atteint en $x_n = \frac{1}{\sqrt{2n+1}}$, et $f_n(x_n) \sim \frac{n}{\sqrt{2n}} e^{-1/2} \to +\infty$, confirmant l'absence de convergence uniforme.

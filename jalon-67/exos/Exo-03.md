---
title: "Exercice 3"
---
## Exercice 3 : Un classique sur $(1 - \frac{x}{n})^n$ $\bigstar\bigstar\star$

**Énoncé :**
Montrer, à l'aide du théorème de convergence monotone, que $\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n e^{x/2} dx = \int_0^\infty e^{-x/2} dx = 2$.

**Correction Détaillée :**
1. On pose $f_n(x) = \left(1 - \frac{x}{n}\right)^n e^{x/2} \mathbf{1}_{[0,n]}(x)$.
2. On sait que pour tout $x \ge 0$, $\lim_{n \to \infty} \left(1 - \frac{x}{n}\right)^n = e^{-x}$.
   Donc, pour tout $x \ge 0$, $f_n(x) \to e^{-x} e^{x/2} = e^{-x/2}$.
3. Pour appliquer Beppo Levi, il faut montrer que la suite $(f_n)$ est croissante.
   Posons $g_n(x) = n \ln(1 - x/n) \mathbf{1}_{[0,n]}(x)$.
   On a $\frac{d}{dn} \left(n \ln(1 - \frac{x}{n})\right) = \ln(1 - \frac{x}{n}) + \frac{x/n}{1 - x/n} = \ln(1 - u) + \frac{u}{1-u}$ avec $u = x/n < 1$.
   Or, par étude de fonction, pour $u \in [0,1[$, $\ln(1-u) + \frac{u}{1-u} \ge 0$.
   Donc $n \mapsto n \ln(1-x/n)$ est croissante en $n$.
4. Par suite, $n \mapsto (1-x/n)^n$ est croissante.
5. Donc la suite de fonctions $f_n$ est positive et croissante.
6. Le TCM s'applique :
   $$\lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty \lim_{n \to \infty} f_n(x) dx = \int_0^\infty e^{-x/2} dx$$
7. L'intégrale de droite se calcule facilement : $\left[-2 e^{-x/2}\right]_0^\infty = 2$.

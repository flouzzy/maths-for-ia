# Exercice 4 : Croissance via l'exponentielle
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $f_n(x) = \left(1 + \frac{x}{n}\right)^n e^{-x} \mathbf{1}_{[0, n]}(x)$. Étudier la limite de l'intégrale $\int_0^{+\infty} f_n(x) dx$.

## Correction Détaillée

On utilise l'inégalité classique $\ln(1+u) \leq u$ pour $u > -1$.
Pour $x \in [0, n]$, $f_n(x) = \exp\left( n \ln(1 + \frac{x}{n}) - x \right)$.
Montrons la monotonie de la suite. Soit $g_x(t) = t \ln(1 + \frac{x}{t})$.
La dérivée $g_x'(t) = \ln(1 + \frac{x}{t}) - \frac{x/t}{1 + x/t}$. Posons $y = x/t \geq 0$. On a $\ln(1+y) \geq \frac{y}{1+y}$ pour $y \geq 0$. Donc $g_x'(t) \geq 0$.
La suite $(f_n)$ est donc croissante pour tout $x$.
Les fonctions $f_n$ sont positives et mesurables.
La limite simple est $f(x) = \lim_{n \to +\infty} \left(1 + \frac{x}{n}\right)^n e^{-x} = e^x e^{-x} = 1$.
Par le Théorème de Convergence Monotone :
$$\lim_{n \to +\infty} \int_0^n \left(1 + \frac{x}{n}\right)^n e^{-x} dx = \int_0^{+\infty} \lim_{n \to +\infty} f_n(x) dx = \int_0^{+\infty} 1 \, dx = +\infty$$

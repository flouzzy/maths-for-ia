# Exercice 7 : Comportement au bord \quad $\bigstar\bigstar\star\star\star$

## Énoncé
Soit $f_n(x) = n \chi_{]0, 1/n]}(x)$. La suite $(f_n)$ n'est pas croissante. Montrer que Beppo Levi ne s'y applique pas.

## Correction Détaillée
Pour $x > 0$, il existe un rang $N$ tel que $1/n < x$ pour $n > N$, donc $f_n(x) = 0$. Ainsi $\lim_{n\to\infty} f_n(x) = 0$ pour tout $x > 0$.
L'intégrale de la limite est $\int 0 dx = 0$.
Or, pour tout $n$, $\int_{\mathbb{R}} f_n dx = \int_0^{1/n} n dx = 1$.
La limite des intégrales est $1 \neq 0$. L'hypothèse de croissance est impérative.

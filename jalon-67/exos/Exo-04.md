# Exercice 4 : Limite d'intégrale fractionnaire

**Difficulté :** $\bigstar\bigstar\bigstar\☆☆$

## Énoncé

Calculer, en justifiant rigoureusement, la limite quand $n \to +\infty$ de $\int_0^n (1-\frac{x}{n})^n x^{p-1} dx$ pour $p>0$ (Fonction Gamma).

## Démonstration rigoureuse pas à pas

Posons $f_n(x) = (1-\frac{x}{n})^n x^{p-1} \mathbf{1}_{[0,n]}(x)$. On sait que pour tout $x \ge 0$, la suite $n \mapsto (1-\frac{x}{n})^n$ croît vers $e^{-x}$. Ainsi, la suite de fonctions positives $(f_n)$ est une suite croissante qui converge simplement vers $f(x) = e^{-x} x^{p-1} \mathbf{1}_{[0,+\infty[}(x)$. Par le théorème de Beppo-Levi, on a : $\lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty \lim_n f_n(x) dx = \int_0^\infty x^{p-1} e^{-x} dx = \Gamma(p)$.

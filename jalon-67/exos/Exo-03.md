# Exercice 3 : Intégration d'une suite croissante simple \quad $\bigstar\bigstar\star\star\star$

Soit $f_n(x) = (1 - \frac{x}{n})^n \mathbb{1}_{[0, n]}(x)$. Montrer que $f_n$ est croissante et trouver l'intégrale de sa limite sur $[0, +\infty[$.

**Correction :**
Par une étude de fonction (dérivée par rapport à $n$ ou via logarithme), on montre que $f_n(x)$ croît vers $e^{-x}$. Par Beppo Levi, $\int_0^\infty e^{-x} dx = 1$ est la limite des intégrales $\int_0^n (1 - x/n)^n dx$. (Cette intégrale partielle vaut $\frac{n}{n+1}n$).

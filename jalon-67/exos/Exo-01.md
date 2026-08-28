# Exercice 1 : Étude d'une intégrale par limite croissante ★★☆☆☆

**Énoncé :**
Soit $f_n(x) = \left(1 - \frac{x}{n}\right)^n \chi_{[0, n]}(x)$ sur $\mathbb{R}^+$. Montrer que $f_n$ est une suite croissante de fonctions mesurables. En déduire $\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n dx$.

**Correction :**
1. On a $f_n(x) = \exp(n \ln(1 - x/n)) \chi_{[0, n]}(x)$. Posons $g_n(x) = n \ln(1 - x/n)$. On calcule la dérivée par rapport à $n$ (ou on étudie le rapport) et on obtient que $f_n(x)$ est strictement croissante en $n$.
2. La limite ponctuelle est $f(x) = \lim \exp(n \ln(1 - x/n))$. Or $n \ln(1 - x/n) = n (-x/n + O(1/n^2)) = -x + O(1/n)$. Donc $f(x) = e^{-x}$.
3. Les $f_n$ sont positives et mesurables (continues sur leur support). Par le théorème de convergence monotone, $\lim \int_0^\infty f_n = \int_0^\infty \lim f_n = \int_0^\infty e^{-x} dx$.
4. L'intégrale de $e^{-x}$ sur $\mathbb{R}^+$ vaut $[-e^{-x}]_0^\infty = 1$. Donc la limite de l'intégrale est $1$.

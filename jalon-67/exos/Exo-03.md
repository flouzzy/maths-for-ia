# Exercice 3 : Fonction Gamma d'Euler \quad $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Démontrer que $\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n x^{z-1} dx = \int_0^\infty e^{-x} x^{z-1} dx$ pour $z > 1$ en utilisant le fait que la suite $f_n(x) = \left(1 - \frac{x}{n}\right)^n \chi_{[0, n]}(x)$ est croissante vers $e^{-x}$.

## Correction Détaillée
1. Pour $x \ge 0$, la suite $g_n(x) = \left(1 - \frac{x}{n}\right)^n$ définie sur $[0, n]$ est bien connue pour être croissante en $n$ et converger vers $e^{-x}$.
2. Les fonctions $h_n(x) = f_n(x) x^{z-1}$ sont donc des fonctions mesurables positives.
3. La suite $(h_n)$ est croissante pour presque tout $x>0$.
4. D'après le théorème de Beppo Levi : $\lim_{n \to \infty} \int_0^\infty h_n(x) dx = \int_0^\infty \lim_{n \to \infty} h_n(x) dx$.
5. Or $\lim h_n(x) = e^{-x} x^{z-1}$, d'où le résultat, qui identifie la fonction Gamma avec sa définition en produit.

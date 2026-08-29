# Exercice 4 : Fonction Gamma d'Euler $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Montrer que $\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n x^{s-1} dx = \Gamma(s)$ pour $s > 0$.

## Correction Détaillée
1. Posons $f_n(x) = \left(1 - \frac{x}{n}\right)^n x^{s-1} \mathbf{1}_{[0, n]}(x)$ pour $x > 0$.
2. Les fonctions $f_n$ sont positives pour $x > 0$.
3. Comme vu dans l'exercice précédent, la suite $(1 - x/n)^n \mathbf{1}_{[0, n]}(x)$ est croissante et converge vers $e^{-x}$.
4. Ainsi, $f_n(x)$ est une suite croissante de fonctions mesurables qui converge ponctuellement vers $f(x) = e^{-x} x^{s-1} \mathbf{1}_{[0, \infty[}(x)$.
5. D'après le TCM, l'intégrale de la limite est la limite des intégrales :
   $$ \lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty f(x) dx $$
6. Or, par définition, $\int_0^\infty e^{-x} x^{s-1} dx = \Gamma(s)$.
7. D'où le résultat.

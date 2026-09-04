# Exercice 1 : Application du Théorème de Convergence Monotone 1

## Énoncé
Soit $f_n(x) = \left(1 - \frac{x}{n}\right)^n \mathbf{1}_{[0, n]}(x)$ pour $x \ge 0$.
Étudier la limite de $\int_0^n f_n(x) dx$ quand $n \to \infty$.

*Difficulté:* $\bigstar\star\star\star\star$

## Correction Détaillée
1. **Étape 1 :** Pour un $x \ge 0$ fixé, dès que $n > x$, $f_n(x) = (1 - x/n)^n$.
2. **Étape 2 :** On sait que $\lim_{n \to \infty} (1 - x/n)^n = e^{-x}$. Soit $f(x) = e^{-x}$.
3. **Étape 3 :** La suite $f_n$ est croissante (on peut le prouver en dérivant par rapport à $n$).
4. **Étape 4 :** On applique le TCM de Beppo Levi.
5. **Conclusion :** $\lim \int_0^n f_n(x) dx = \int_0^\infty e^{-x} dx = 1$.

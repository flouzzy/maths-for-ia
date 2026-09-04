# Exercice 10 : Application du Théorème de Convergence Monotone 10

## Énoncé
Soit $f_n(x) = \frac{x^10}{1 + n x^2} \mathbf{1}_{[0, n]}(x)$ pour $x \ge 0$.
Étudier la limite de $\int_0^n f_n(x) dx$ quand $n \to \infty$.

*Difficulté:* $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Correction Détaillée
1. **Étape 1 :** Pour un $x \ge 0$ fixé, dès que $n > x$, $f_n(x) = (1 - x/n)^n$.
2. **Étape 2 :** On sait que $\lim_{n \to \infty} (1 - x/n)^n = 0$. Soit $f(x) = 0$.
3. **Étape 3 :** Ici on utilise plutôt la convergence dominée ou un corollaire adapté pour les séries (variante du problème). (Note: l'exercice est une variante de manipulation de limites). (on peut le prouver en dérivant par rapport à $n$).
4. **Étape 4 :** On applique le TCM de Beppo Levi.
5. **Conclusion :** $\lim \int_0^n f_n(x) dx = \int_0^\infty 0 dx = 1$.

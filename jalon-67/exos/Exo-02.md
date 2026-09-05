# Exercice 2 : Suite croissante de fonctions en escalier \quad $\bigstar\bigstar\star\star\star$

Soit $f_n(x) = \left( 1 - \frac{x}{n} \right)^n \mathbf{1}_{[0, n]}(x)$.

**Question :** Utiliser le théorème de convergence monotone pour calculer la limite de $\int_{0}^{\infty} f_n(x) dx$.

**Solution Détaillée :**
1. Les fonctions $f_n$ sont mesurables sur $[0, +\infty[$ et à valeurs positives.
2. Étudions la monotonie de la suite $(f_n(x))_{n \ge 1}$ à $x$ fixé.
   Pour $x \ge 0$ fixé, dès que $n > x$, $f_n(x) = \left( 1 - \frac{x}{n} \right)^n = \exp\left( n \ln\left(1 - \frac{x}{n}\right) \right)$.
   Or, la fonction $t \mapsto \ln(1 - x t) / t$ est décroissante au voisinage de $0$, donc la suite $n \mapsto f_n(x)$ est croissante.
   Plus élémentairement, l'inégalité de Bernoulli permet de montrer la croissance.
3. Déterminons la limite simple $f(x) = \lim_{n \to \infty} f_n(x)$.
   Pour $x \ge 0$, $\lim_{n \to \infty} n \ln\left(1 - \frac{x}{n}\right) = n \left(-\frac{x}{n} + o(1/n)\right) = -x$.
   Donc $f(x) = e^{-x}$.
4. D'après le théorème de convergence monotone, puisque $f_n \ge 0$ et $f_n \le f_{n+1}$ :
   $$ \lim_{n \to \infty} \int_{0}^{\infty} f_n(x) dx = \int_{0}^{\infty} \lim_{n \to \infty} f_n(x) dx = \int_{0}^{\infty} e^{-x} dx $$
5. Calcul de l'intégrale de la limite :
   $$ \int_{0}^{\infty} e^{-x} dx = \left[ -e^{-x} \right]_0^\infty = 1 $$
6. Ainsi, la limite de l'intégrale est 1.

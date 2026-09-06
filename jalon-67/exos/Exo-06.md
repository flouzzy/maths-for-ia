---
title: "Exercice 6"
---
## Exercice 6 : Convergence d'une intégrale paramétrique impropre $\bigstar\bigstar\star\star$

**Énoncé :**
Calculer $\lim_{n \to \infty} \int_0^\infty e^{-nx} \sin(x)^2 dx$.

**Correction Détaillée :**
1. Posons $f_n(x) = e^{-nx} \sin(x)^2$.
2. Les fonctions $f_n$ sont mesurables et positives sur $]0, +\infty[$.
3. Contrairement aux apparences, la suite $(f_n)$ est \textbf{décroissante}. En effet, pour $x > 0$, $e^{-nx} > e^{-(n+1)x}$.
4. Le Théorème de Convergence Monotone s'applique aux suites croissantes. Comment l'utiliser ici ?
   On peut utiliser Beppo Levi "à l'envers" si on a une majoration intégrable (ce qui s'appelle le théorème de convergence dominée, mais on peut s'en passer).
   Posons $g_n(x) = f_1(x) - f_n(x)$.
5. La suite $(g_n)$ est positive (car $f_n \le f_1$) et \textbf{croissante} (car $f_n$ décroît).
6. La limite simple de $g_n(x)$ est $g(x) = f_1(x) - 0 = e^{-x} \sin(x)^2$ pour $x > 0$.
7. Appliquons Beppo Levi à $g_n$ :
   $$\lim_{n \to \infty} \int_0^\infty (f_1(x) - f_n(x)) dx = \int_0^\infty f_1(x) dx$$
8. Comme $\int_0^\infty f_1(x) dx$ est finie (car $e^{-x}\sin(x)^2 \le e^{-x}$ qui est intégrable), on a :
   $$\int_0^\infty f_1(x) dx - \lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty f_1(x) dx$$
9. On en déduit que $\lim_{n \to \infty} \int_0^\infty f_n(x) dx = 0$.

# Exercice 3 : La limite d'une suite croissante impliquant l'exponentielle

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f_n(x) = \left(1 + \frac{x}{n}\right)^n e^{-2x}$ sur $[0, +\infty[$.
Calculer $\lim_{n \to \infty} \int_0^\infty f_n(x) dx$.

**Solution Détaillée :**
1. **Convergence simple :**
On sait que pour tout $x \ge 0$, $\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x$.
Donc la suite $(f_n)$ converge simplement vers $f(x) = e^x \cdot e^{-2x} = e^{-x}$.

2. **Monotonie :**
Pour appliquer Beppo Levi, nous devons montrer que la suite $g_n(x) = \left(1 + \frac{x}{n}\right)^n$ est croissante en $n$ pour $x$ fixé.
Prenons le logarithme : $\ln(g_n(x)) = n \ln\left(1 + \frac{x}{n}\right)$.
L'étude de la fonction $h(y) = \frac{1}{y} \ln(1+xy)$ (avec $y=1/n$) montre qu'elle est décroissante sur $y \in ]0, +\infty[$. Donc quand $n$ croît (et $y$ décroît), la suite croît.
Puisque l'exponentielle est une fonction croissante, $g_n(x)$ est croissante.
Comme $e^{-2x} > 0$, la suite complète $f_n(x)$ est également croissante et positive.

3. **Application du TCM :**
Les hypothèses du théorème de convergence monotone étant vérifiées :
$$\lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty \lim_{n \to \infty} f_n(x) dx = \int_0^\infty e^{-x} dx$$

4. **Calcul final :**
$$\int_0^\infty e^{-x} dx = \left[ -e^{-x} \right]_0^\infty = 0 - (-1) = 1$$
La limite cherchée vaut donc 1.

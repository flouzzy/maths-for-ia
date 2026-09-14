## Exercice 4 : Mesure d'un triangle \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Calculer la mesure de Lebesgue $\lambda_2$ du triangle $T = \{ (x, y) \in \mathbb{R}^2 \mid x \ge 0, y \ge 0, x+y \le 2 \}$ en intégrant ses sections.

**Correction :**
1. Les sections $T_x$ sont données par :
   - Si $x < 0$ ou $x > 2$, $T_x = \emptyset$ et $\lambda(T_x) = 0$.
   - Si $x \in [0, 2]$, $T_x = [0, 2-x]$ et $\lambda(T_x) = 2-x$.
2. Par le théorème d'intégration des sections (qui découle de la définition de la mesure produit) :
   $\lambda_2(T) = \int_{\mathbb{R}} \lambda(T_x) d\lambda(x) = \int_0^2 (2-x) dx$.
3. Calcul de l'intégrale :
   $\int_0^2 (2-x) dx = \left[ 2x - \frac{x^2}{2} \right]_0^2 = (4 - 2) - 0 = 2$.

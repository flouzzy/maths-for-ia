## Exercice 3 : Vérification de l'identité du parallélogramme \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soient $f(x) = 1$ et $g(x) = x^2$ dans $L^2([0,1])$. Calculer $\|f+g\|_2^2 + \|f-g\|_2^2$ et $2(\|f\|_2^2 + \|g\|_2^2)$ pour vérifier l'identité du parallélogramme.

**Correction Détaillée :**
1. **Calcul des normes individuelles :**
   $$ \|f\|_2^2 = \int_0^1 1^2 dx = 1 $$
   $$ \|g\|_2^2 = \int_0^1 (x^2)^2 dx = \int_0^1 x^4 dx = \left[ \frac{x^5}{5} \right]_0^1 = \frac{1}{5} $$
   Le membre de droite de l'identité vaut donc : $2(1 + \frac{1}{5}) = 2(\frac{6}{5}) = \frac{12}{5}$.
2. **Calcul de $\|f+g\|_2^2$ :**
   $$ \|f+g\|_2^2 = \int_0^1 (1+x^2)^2 dx = \int_0^1 (1 + 2x^2 + x^4) dx $$
   $$ = \left[ x + \frac{2x^3}{3} + \frac{x^5}{5} \right]_0^1 = 1 + \frac{2}{3} + \frac{1}{5} = \frac{15}{15} + \frac{10}{15} + \frac{3}{15} = \frac{28}{15} $$
3. **Calcul de $\|f-g\|_2^2$ :**
   $$ \|f-g\|_2^2 = \int_0^1 (1-x^2)^2 dx = \int_0^1 (1 - 2x^2 + x^4) dx $$
   $$ = \left[ x - \frac{2x^3}{3} + \frac{x^5}{5} \right]_0^1 = 1 - \frac{2}{3} + \frac{1}{5} = \frac{15}{15} - \frac{10}{15} + \frac{3}{15} = \frac{8}{15} $$
4. **Vérification finale :**
   $$ \|f+g\|_2^2 + \|f-g\|_2^2 = \frac{28}{15} + \frac{8}{15} = \frac{36}{15} = \frac{12 \cdot 3}{5 \cdot 3} = \frac{12}{5} $$
   Les deux membres sont égaux à $\frac{12}{5}$. L'identité du parallélogramme est parfaitement vérifiée.

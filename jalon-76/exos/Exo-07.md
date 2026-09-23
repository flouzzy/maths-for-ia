## Exercice 7 : Calcul de distance à un sous-espace vectoriel \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Dans $L^2([-1,1])$, calculer la distance de la fonction $f(x) = x^3$ au sous-espace $M = \text{Vect}(1, x)$.

**Correction Détaillée :**
1. **Caractérisation de la distance :** La distance $d(f, M)$ est égale à $\|f - p_M(f)\|_2$, où $p_M(f)$ est la projection orthogonale de $f$ sur $M$.
2. **Recherche de la projection :** Les vecteurs $e_0(x)=1$ et $e_1(x)=x$ forment une base orthogonale de $M$ car $\int_{-1}^1 1 \cdot x dx = 0$.
   On peut donc calculer $p_M(f)$ directement :
   $$ p_M(f) = \frac{\langle f, e_0 \rangle}{\|e_0\|^2} e_0 + \frac{\langle f, e_1 \rangle}{\|e_1\|^2} e_1 $$
3. **Calcul des coefficients :**
   $\|e_0\|^2 = 2$. $\|e_1\|^2 = \frac{2}{3}$.
   $\langle f, e_0 \rangle = \int_{-1}^1 x^3 dx = 0$ (fonction impaire).
   $\langle f, e_1 \rangle = \int_{-1}^1 x^4 dx = \left[ \frac{x^5}{5} \right]_{-1}^1 = \frac{2}{5}$.
4. **Forme de la projection :**
   $$ p_M(f) = 0 \cdot 1 + \frac{2/5}{2/3} x = \frac{3}{5} x $$
5. **Calcul de la distance au carré :**
   $$ d(f, M)^2 = \|f - p_M(f)\|_2^2 = \int_{-1}^1 \left(x^3 - \frac{3}{5} x\right)^2 dx = \int_{-1}^1 \left(x^6 - \frac{6}{5}x^4 + \frac{9}{25}x^2\right) dx $$
   $$ = \left[ \frac{x^7}{7} - \frac{6}{25}x^5 + \frac{3}{25}x^3 \right]_{-1}^1 = 2 \left( \frac{1}{7} - \frac{6}{25} + \frac{3}{25} \right) = 2 \left( \frac{1}{7} - \frac{3}{25} \right) = 2 \left( \frac{25 - 21}{175} \right) = \frac{8}{175} $$
   La distance est donc $\sqrt{\frac{8}{175}} = \frac{2\sqrt{2}}{5\sqrt{7}}$.

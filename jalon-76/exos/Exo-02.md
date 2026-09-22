## Exercice 2 : Calcul de norme et inégalité de Cauchy-Schwarz \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f(x) = x$ et $g(x) = e^x$ sur l'intervalle $[0, 1]$. Calculer $\|f\|_2, \|g\|_2$ et vérifier numériquement que $\langle f, g \rangle \le \|f\|_2 \|g\|_2$.

**Correction Détaillée :**
1. **Calcul de $\|f\|_2$ :**
   $$ \|f\|_2^2 = \int_0^1 x^2 dx = \left[ \frac{x^3}{3} \right]_0^1 = \frac{1}{3} $$
   Donc $\|f\|_2 = \frac{1}{\sqrt{3}}$.
2. **Calcul de $\|g\|_2$ :**
   $$ \|g\|_2^2 = \int_0^1 (e^x)^2 dx = \int_0^1 e^{2x} dx = \left[ \frac{e^{2x}}{2} \right]_0^1 = \frac{e^2 - 1}{2} $$
   Donc $\|g\|_2 = \sqrt{\frac{e^2 - 1}{2}}$.
3. **Calcul de $\langle f, g \rangle$ :**
   $$ \langle f, g \rangle = \int_0^1 x e^x dx $$
   On procède par intégration par parties avec $u = x$ ($du = dx$) et $dv = e^x dx$ ($v = e^x$) :
   $$ \langle f, g \rangle = \left[ x e^x \right]_0^1 - \int_0^1 e^x dx = (1\cdot e^1 - 0) - \left[ e^x \right]_0^1 = e - (e - 1) = 1 $$
4. **Vérification de Cauchy-Schwarz :**
   On veut vérifier que $1 \le \frac{1}{\sqrt{3}} \sqrt{\frac{e^2 - 1}{2}} = \sqrt{\frac{e^2 - 1}{6}}$.
   En élevant au carré, on vérifie si $1 \le \frac{e^2 - 1}{6} \iff 6 \le e^2 - 1 \iff 7 \le e^2$.
   Sachant que $e \approx 2.718$, on a $e^2 \approx 7.389$. L'inégalité $7 \le 7.389$ est vraie. Cauchy-Schwarz est bien respectée.

# Exercice 9 : Equation différentielle avec forçage périodique

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\bigstar

**Énoncé :**
Trouver l'unique solution $2\pi$-périodique de l'équation différentielle $y'' + 2y' + 2y = f(t)$, où $f(t)$ est la fonction définie dans l'exercice 1 ($f(t) = 1 - \frac{|t|}{\pi}$ sur $[-\pi, \pi]$).

**Correction :**
1. Nous cherchons une solution $2\pi$-périodique, que nous écrivons sous forme de série de Fourier complexe : $y(t) = \sum_{n=-\infty}^{+\infty} c_n(y) e^{int}$.
2. Puisque l'opérateur différentiel est linéaire et à coefficients constants, on a $c_n(y') = in c_n(y)$ et $c_n(y'') = -n^2 c_n(y)$.
   En injectant dans l'équation et en identifiant les coefficients de Fourier, on obtient :
   $(-n^2 + 2in + 2) c_n(y) = c_n(f)$
   Le polynôme caractéristique évalué en $in$ ne s'annule jamais pour $n \in \mathbb{Z}$, donc :
   $c_n(y) = \frac{c_n(f)}{2 - n^2 + 2in}$
3. Les coefficients de la fonction de l'exercice 1 sont réels. Pour $n$ impair, $n = 2p+1$, $a_n = \frac{4}{\pi^2 n^2}$ et $b_n = 0$. Donc $c_n(f) = \frac{a_n}{2} = \frac{2}{\pi^2 n^2}$. Pour $n$ pair non nul, $c_n(f) = 0$. Et $c_0(f) = a_0 = 1$.
4. Pour $n=0$, on a $2 c_0(y) = 1 \implies c_0(y) = \frac{1}{2}$.
   Pour $n = 2p+1$ :
   $c_n(y) = \frac{2}{\pi^2 n^2 (2 - n^2 + 2in)} = \frac{2(2 - n^2 - 2in)}{\pi^2 n^2 ((2 - n^2)^2 + 4n^2)}$
5. On reconstruit $y(t)$ à l'aide des coefficients réels : $A_n = 2 \text{Re}(c_n(y))$ et $B_n = -2 \text{Im}(c_n(y))$.
   $A_n = \frac{4(2 - n^2)}{\pi^2 n^2 ((2-n^2)^2 + 4n^2)}$
   $B_n = \frac{8n}{\pi^2 n^2 ((2-n^2)^2 + 4n^2)} = \frac{8}{\pi^2 n ((2-n^2)^2 + 4n^2)}$
   La solution unique est :
   $$y(t) = \frac{1}{2} + \sum_{k=0}^{+\infty} \left( A_{2k+1} \cos((2k+1)t) + B_{2k+1} \sin((2k+1)t) \right)$$
   (avec les $A_n, B_n$ calculés pour $n=2k+1$).

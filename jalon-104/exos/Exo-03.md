# Exercice 3 : Polynômes de Laguerre $\bigstar\bigstar\star\star\star$

**Énoncé :**
On considère l'espace de Hilbert $H = L^2([0, +\infty[, e^{-x}dx)$ avec le produit scalaire $\langle f, g \rangle = \int_0^{+\infty} f(x)g(x)e^{-x} dx$.
Soient les monômes $P_0(x) = 1$, $P_1(x) = x$, $P_2(x) = x^2$.
Appliquer le procédé de Gram-Schmidt pour obtenir une famille orthonormée $(L_0, L_1, L_2)$ à partir de $(P_0, P_1, P_2)$.
On rappelle que $\int_0^{+\infty} x^n e^{-x} dx = n!$.

**Correction détaillée :**
1. Pour $L_0$ :
   $\|P_0\|^2 = \int_0^{+\infty} 1 \cdot e^{-x} dx = 0! = 1$.
   Donc $L_0(x) = \frac{P_0(x)}{\|P_0\|} = 1$.

2. Pour $L_1$ :
   Calculons la projection de $P_1$ sur $L_0$ :
   $\langle P_1, L_0 \rangle = \int_0^{+\infty} x \cdot 1 \cdot e^{-x} dx = 1! = 1$.
   $u_1(x) = P_1(x) - \langle P_1, L_0 \rangle L_0(x) = x - 1$.
   Calculons sa norme :
   $\|u_1\|^2 = \int_0^{+\infty} (x-1)^2 e^{-x} dx = \int_0^{+\infty} (x^2 - 2x + 1) e^{-x} dx = 2! - 2(1!) + 0! = 2 - 2 + 1 = 1$.
   Donc $L_1(x) = u_1(x) = x - 1$.
   *(Note : les polynômes de Laguerre standard sont souvent définis avec une normalisation différente, ici nous construisons la base orthonormée exacte).*

3. Pour $L_2$ :
   Calculons les projections de $P_2$ sur $L_0$ et $L_1$ :
   $\langle P_2, L_0 \rangle = \int_0^{+\infty} x^2 \cdot 1 \cdot e^{-x} dx = 2! = 2$.
   $\langle P_2, L_1 \rangle = \int_0^{+\infty} x^2(x-1) e^{-x} dx = \int_0^{+\infty} (x^3 - x^2) e^{-x} dx = 3! - 2! = 6 - 2 = 4$.
   On forme le polynôme résiduel :
   $u_2(x) = P_2(x) - \langle P_2, L_0 \rangle L_0(x) - \langle P_2, L_1 \rangle L_1(x)$
   $u_2(x) = x^2 - 2(1) - 4(x-1) = x^2 - 4x + 2$.
   Calculons la norme de $u_2$ :
   $\|u_2\|^2 = \int_0^{+\infty} (x^2 - 4x + 2)^2 e^{-x} dx = \int_0^{+\infty} (x^4 + 16x^2 + 4 - 8x^3 + 4x^2 - 16x) e^{-x} dx$
   $\|u_2\|^2 = \int_0^{+\infty} (x^4 - 8x^3 + 20x^2 - 16x + 4) e^{-x} dx$
   $\|u_2\|^2 = 4! - 8(3!) + 20(2!) - 16(1!) + 4(0!) = 24 - 48 + 40 - 16 + 4 = 4$.
   Donc $L_2(x) = \frac{u_2(x)}{\|u_2\|} = \frac{x^2 - 4x + 2}{2} = \frac{1}{2}x^2 - 2x + 1$.

Les trois premiers polynômes de la base hilbertienne sont $L_0(x) = 1$, $L_1(x) = x - 1$ et $L_2(x) = \frac{1}{2}x^2 - 2x + 1$.

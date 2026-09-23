## Exercice 5 : Procédé de Gram-Schmidt dans $L^2$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Dans $L^2([-1,1])$, appliquer le procédé d'orthogonalisation de Gram-Schmidt à la famille $(1, x, x^2)$ pour obtenir une famille orthogonale $(P_0, P_1, P_2)$.

**Correction Détaillée :**
1. **Initialisation :** Soit $e_0(x) = 1, e_1(x) = x, e_2(x) = x^2$.
   On pose $P_0(x) = e_0(x) = 1$.
2. **Calcul de $P_1$ :**
   $$ P_1 = e_1 - \frac{\langle e_1, P_0 \rangle}{\|P_0\|^2} P_0 $$
   Calculs intermédiaires :
   $\|P_0\|^2 = \int_{-1}^1 1 dx = 2$.
   $\langle e_1, P_0 \rangle = \int_{-1}^1 x \cdot 1 dx = \left[ \frac{x^2}{2} \right]_{-1}^1 = 0$.
   Donc $P_1(x) = x - 0 = x$.
3. **Calcul de $P_2$ :**
   $$ P_2 = e_2 - \frac{\langle e_2, P_0 \rangle}{\|P_0\|^2} P_0 - \frac{\langle e_2, P_1 \rangle}{\|P_1\|^2} P_1 $$
   Calculs intermédiaires :
   $\|P_1\|^2 = \int_{-1}^1 x^2 dx = \left[ \frac{x^3}{3} \right]_{-1}^1 = \frac{2}{3}$.
   $\langle e_2, P_0 \rangle = \int_{-1}^1 x^2 \cdot 1 dx = \frac{2}{3}$.
   $\langle e_2, P_1 \rangle = \int_{-1}^1 x^2 \cdot x dx = \int_{-1}^1 x^3 dx = 0$ (fonction impaire).
   En substituant :
   $$ P_2(x) = x^2 - \frac{2/3}{2} \cdot 1 - 0 = x^2 - \frac{1}{3} $$
4. **Conclusion :** La famille orthogonale obtenue est $(1, x, x^2 - \frac{1}{3})$. (Ce sont, à des constantes multiplicatives près, les polynômes de Legendre).

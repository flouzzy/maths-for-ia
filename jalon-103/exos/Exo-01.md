# Exercice 1 : Projection sur un hyperplan de L^2

## Énoncé

Soit $H = L^2([-1, 1])$ muni de son produit scalaire usuel. Soit $F = \{f \in H \mid \int_{-1}^1 f(t) dt = 0\}$. Montrer que $F$ est fermé, puis calculer la projection orthogonale de la fonction $g(t) = t^2$ sur $F$.

*Niveau de difficulté :* $\bigstar\star\star\star\star$

## Correction

1. **Fermeture de F :** L'application $L(f) = \int_{-1}^1 f(t) dt$ est une forme linéaire. Par l'inégalité de Cauchy-Schwarz, $|L(f)| \le \sqrt{\int_{-1}^1 1^2 dt} \sqrt{\int_{-1}^1 |f(t)|^2 dt} = \sqrt{2} \|f\|_2$. Donc $L$ est continue. $F = \ker L$ est donc un hyperplan fermé.
2. **Vecteur normal :** Par le théorème de représentation de Riesz, $L(f) = \langle f, u \rangle$ avec $u(t) = 1$. L'orthogonal de $F$ est engendré par $u$.
3. **Calcul de la projection :** La projection de $g$ sur $F$ est $P_F(g) = g - \frac{\langle g, u \rangle}{\|u\|^2} u$.
4. **Évaluation :** $\langle g, u \rangle = \int_{-1}^1 t^2 \cdot 1 dt = \frac{2}{3}$. Et $\|u\|^2 = \int_{-1}^1 1 dt = 2$.
5. **Conclusion :** $P_F(g)(t) = t^2 - \frac{2/3}{2} \cdot 1 = t^2 - \frac{1}{3}$.

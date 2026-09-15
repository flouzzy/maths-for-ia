## Exercice 1 : Application directe de Tonelli sur un rectangle \quad $\bigstar\star\star\star\star$

**Énoncé :**
Calculer l'intégrale double $I = \int_{[0, 1] \times [0, 2]} x y^2 dx dy$.

**Correction :**
1. Soit $f(x, y) = x y^2$. La fonction $f$ est continue sur le rectangle $R = [0, 1] \times [0, 2]$, donc elle est mesurable.
2. Pour tout $(x, y) \in R$, $x \ge 0$ et $y^2 \ge 0$, donc $f(x, y) \ge 0$.
3. Les hypothèses du théorème de Tonelli sont satisfaites (fonction positive, espaces de mesure finie).
4. Nous pouvons calculer l'intégrale itérée dans l'ordre de notre choix. Intégrons d'abord par rapport à $y$ :
   $$ I = \int_0^1 \left( \int_0^2 x y^2 dy \right) dx $$
5. Pour $x$ fixé, une primitive de $y \mapsto x y^2$ est $y \mapsto x \frac{y^3}{3}$.
   $$ \int_0^2 x y^2 dy = x \left[ \frac{y^3}{3} \right]_0^2 = x \left( \frac{8}{3} - 0 \right) = \frac{8x}{3} $$
6. Nous intégrons maintenant le résultat par rapport à $x$ :
   $$ I = \int_0^1 \frac{8x}{3} dx = \frac{8}{3} \left[ \frac{x^2}{2} \right]_0^1 = \frac{8}{3} \times \frac{1}{2} = \frac{4}{3} $$
7. **Conclusion :** L'intégrale vaut $4/3$.

## Exercice 2 : Fubini et fonction à signe variable \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Montrer que $f(x, y) = x - y$ est intégrable sur $[0, 1]^2$ et calculer $I = \iint_{[0, 1]^2} (x - y) dx dy$.

**Correction :**
1. La fonction $f(x, y) = x - y$ change de signe sur le domaine. Pour appliquer le théorème de Fubini, nous devons d'abord vérifier que l'intégrale de sa valeur absolue est finie.
2. Considérons $|f(x, y)| = |x - y|$. Cette fonction est positive, donc Tonelli s'applique :
   $$ \iint |x - y| dx dy = \int_0^1 \left( \int_0^1 |x - y| dy \right) dx $$
3. Calculons l'intégrale interne pour un $x \in [0, 1]$ fixé. On découpe l'intervalle selon le signe de $x - y$ :
   $$ \int_0^1 |x - y| dy = \int_0^x (x - y) dy + \int_x^1 (y - x) dy $$
   $$ = \left[ xy - \frac{y^2}{2} \right]_0^x + \left[ \frac{y^2}{2} - xy \right]_x^1 $$
   $$ = \left( x^2 - \frac{x^2}{2} \right) + \left( \frac{1}{2} - x - (\frac{x^2}{2} - x^2) \right) = \frac{x^2}{2} + \frac{1}{2} - x + \frac{x^2}{2} = x^2 - x + \frac{1}{2} $$
4. Intégrons ce résultat en $x$ :
   $$ \int_0^1 \left( x^2 - x + \frac{1}{2} \right) dx = \left[ \frac{x^3}{3} - \frac{x^2}{2} + \frac{x}{2} \right]_0^1 = \frac{1}{3} - \frac{1}{2} + \frac{1}{2} = \frac{1}{3} $$
5. L'intégrale de la valeur absolue est $1/3 < +\infty$. La fonction $f$ est intégrable.
6. Fubini s'applique, nous pouvons calculer $I$ sans la valeur absolue :
   $$ I = \int_0^1 \left( \int_0^1 (x - y) dy \right) dx = \int_0^1 \left[ xy - \frac{y^2}{2} \right]_0^1 dx = \int_0^1 (x - \frac{1}{2}) dx = \left[ \frac{x^2}{2} - \frac{x}{2} \right]_0^1 = 0 $$

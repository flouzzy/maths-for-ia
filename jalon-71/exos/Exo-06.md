## Exercice 6 : Contre-exemple classique de Fubini \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f(x, y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}$ définie sur $]0, 1]^2$.
1. Calculer $I_{xy} = \int_0^1 \left( \int_0^1 f(x, y) dy \right) dx$.
2. Calculer $I_{yx} = \int_0^1 \left( \int_0^1 f(x, y) dx \right) dy$.
3. Conclure.

**Correction :**
1. Pour $x > 0$ fixé, calculons la primitive par rapport à $y$ : $\frac{\partial}{\partial y} \left( \frac{y}{x^2+y^2} \right) = \frac{1(x^2+y^2) - y(2y)}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2}$.
   Donc, $\int_0^1 \frac{x^2-y^2}{(x^2+y^2)^2} dy = \left[ \frac{y}{x^2+y^2} \right]_{y=0}^1 = \frac{1}{x^2+1} - 0 = \frac{1}{x^2+1}$.
   Intégrons maintenant par rapport à $x$ :
   $$ I_{xy} = \int_0^1 \frac{1}{x^2+1} dx = [\arctan x]_0^1 = \frac{\pi}{4} - 0 = \frac{\pi}{4} $$
2. Par antisymétrie, $f(y, x) = -f(x, y)$. En échangeant le rôle des variables, l'intégration interne en $x$ donne :
   $$ \int_0^1 \frac{x^2-y^2}{(x^2+y^2)^2} dx = \left[ \frac{-x}{x^2+y^2} \right]_{x=0}^1 = \frac{-1}{y^2+1} $$
   Intégrons ensuite par rapport à $y$ :
   $$ I_{yx} = \int_0^1 \frac{-1}{y^2+1} dy = [-\arctan y]_0^1 = -\frac{\pi}{4} $$
3. $I_{xy} \neq I_{yx}$. L'interversion des intégrales donne un résultat différent. Cela prouve par contraposée que la fonction $f$ **n'est pas** intégrable (au sens de Lebesgue, i.e., son intégrale absolue diverge sur le carré), empêchant l'application du théorème de Fubini.

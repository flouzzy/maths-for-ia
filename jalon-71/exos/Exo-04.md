## Exercice 4 : Intégration sur un domaine triangulaire \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Calculer $I = \iint_D x e^y dx dy$ où $D = \{(x, y) \in \mathbb{R}^2 \mid x \ge 0, y \ge 0, x + y \le 1\}$.

**Correction :**
1. Le domaine $D$ est un triangle plein de sommets $(0,0)$, $(1,0)$, et $(0,1)$. La fonction $f(x,y) = x e^y$ est continue et positive sur ce compact.
2. D'après Tonelli, on peut intervertir. Nous choisissons d'intégrer d'abord en $x$ (à $y$ fixé).
3. Pour un $y \in [0, 1]$ fixé, la variable $x$ varie de $0$ à $1 - y$.
   $$ I = \int_0^1 \left( \int_0^{1-y} x e^y dx \right) dy $$
4. Calculons l'intégrale interne :
   $$ \int_0^{1-y} x e^y dx = e^y \int_0^{1-y} x dx = e^y \left[ \frac{x^2}{2} \right]_0^{1-y} = \frac{e^y(1-y)^2}{2} $$
5. Intégrons maintenant ce résultat par rapport à $y$ sur $[0, 1]$ :
   $$ I = \frac{1}{2} \int_0^1 e^y(1-y)^2 dy $$
6. Procédons par intégration par parties. Posons $u = (1-y)^2 \implies u' = -2(1-y)$ et $v' = e^y \implies v = e^y$.
   $$ \int_0^1 e^y(1-y)^2 dy = \left[ e^y(1-y)^2 \right]_0^1 - \int_0^1 -2(1-y)e^y dy = (0 - 1) + 2 \int_0^1 (1-y)e^y dy $$
7. Deuxième IPP pour $\int_0^1 (1-y)e^y dy$. $u = 1-y \implies u' = -1$, $v' = e^y \implies v = e^y$.
   $$ \int_0^1 (1-y)e^y dy = \left[ e^y(1-y) \right]_0^1 - \int_0^1 -e^y dy = (0 - 1) + [e^y]_0^1 = -1 + (e - 1) = e - 2 $$
8. Reprenons l'équation : $\int e^y(1-y)^2 dy = -1 + 2(e - 2) = 2e - 5$.
9. Finalement, $I = \frac{2e - 5}{2}$.

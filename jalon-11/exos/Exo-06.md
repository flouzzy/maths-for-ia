# Exercice 6: Bidual d'un espace vectoriel
## Énoncé
Soient $a, b, c$ trois réels distincts. On considère l'espace $E = \mathbb{R}_2[X]$.
On définit les formes linéaires $\varphi_a(P) = P(a)$, $\varphi_b(P) = P(b)$ et $\varphi_c(P) = P(c)$.
Montrer que la famille $(\varphi_a, \varphi_b, \varphi_c)$ est une base de $E^*$. En déduire l'existence et l'unicité des polynômes d'interpolation de Lagrange.


## Correction détaillée
1. **Étape 1:** $\text{ev}_x$ est bien une forme linéaire sur $E^*$ car $\text{ev}_x(\phi_1 + \lambda \phi_2) = (\phi_1 + \lambda \phi_2)(x) = \phi_1(x) + \lambda \phi_2(x) = \text{ev}_x(\phi_1) + \lambda \text{ev}_x(\phi_2)$.
2. **Étape 2:** L'application $\Psi$ est linéaire. Soit $x, y \in E$ et $\lambda, \mu \in \mathbb{K}$. Évaluons $\Psi(\lambda x + \mu y)$ sur un élément quelconque $\phi \in E^*$ :
   $$\Psi(\lambda x + \mu y)(\phi) = \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y) = \lambda \Psi(x)(\phi) + \mu \Psi(y)(\phi)$$
   Ce qui démontre la linéarité.
3. **Étape 3:** Montrons que $\Psi$ est injective. Soit $x \in \ker \Psi$. Alors pour toute forme linéaire $\phi \in E^*$, on a $\phi(x) = 0$.
4. **Étape 4:** Si $x \neq 0$, on pourrait le compléter en une base $(x, e_2, \dots, e_n)$ et définir la forme coordonnée $\phi=x^*$ telle que $x^*(x)=1$, ce qui contredit $\phi(x)=0$.
5. **Conclusion:** Par conséquent $x=0$, d'où $\ker \Psi = \{0\}$. $\Psi$ est injective.

$\blacksquare$

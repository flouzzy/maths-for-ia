# Exercice 6: Bidual d'un espace vectoriel
## Énoncé
Pour tout $x \in E$, on définit l'application d'évaluation $\text{ev}_x : E^* \to \mathbb{K}$ par $\text{ev}_x(\phi) = \phi(x)$. Montrer que l'application $\Psi : x \mapsto \text{ev}_x$ est linéaire et injective.

## Correction détaillée
1. **Étape 1:** $\text{ev}_x$ est bien une forme linéaire sur $E^*$ car $\text{ev}_x(\phi_1 + \lambda \phi_2) = (\phi_1 + \lambda \phi_2)(x) = \phi_1(x) + \lambda \phi_2(x) = \text{ev}_x(\phi_1) + \lambda \text{ev}_x(\phi_2)$.
2. **Étape 2:** L'application $\Psi$ est linéaire. Soit $x, y \in E$ et $\lambda, \mu \in \mathbb{K}$. Évaluons $\Psi(\lambda x + \mu y)$ sur un élément quelconque $\phi \in E^*$ :
   $$\Psi(\lambda x + \mu y)(\phi) = \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y) = \lambda \Psi(x)(\phi) + \mu \Psi(y)(\phi)$$
   Ce qui démontre la linéarité.
3. **Étape 3:** Montrons que $\Psi$ est injective. Soit $x \in \ker \Psi$. Alors pour toute forme linéaire $\phi \in E^*$, on a $\phi(x) = 0$.
4. **Étape 4:** Si $x \neq 0$, on pourrait le compléter en une base $(x, e_2, \dots, e_n)$ et définir la forme coordonnée $\phi=x^*$ telle que $x^*(x)=1$, ce qui contredit $\phi(x)=0$.
5. **Conclusion:** Par conséquent $x=0$, d'où $\ker \Psi = \{0\}$. $\Psi$ est injective.

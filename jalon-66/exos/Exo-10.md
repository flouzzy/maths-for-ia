## Exercice 10 : Mesure à densité (Introduction) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :** Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $f \in \mathcal{M}_+$. On définit pour tout $A \in \mathcal{F}$ : $\nu(A) = \int_X f \cdot \mathbf{1}_A \, d\mu$.
Montrer que pour toute fonction simple positive $s$, on a $\int_X s \, d\nu = \int_X s \cdot f \, d\mu$.

**Correction Détaillée :**
1. Soit $s \in \mathcal{S}_+$ une fonction simple positive. Par définition, elle peut s'écrire sous forme canonique :
   $$s = \sum_{i=1}^n c_i \mathbf{1}_{A_i}$$
   où les $c_i \ge 0$ sont les valeurs distinctes prises par $s$, et les $A_i$ sont les préimages disjointes $s^{-1}(\{c_i\})$.
2. Calculons l'intégrale de $s$ par rapport à la "nouvelle" fonction d'ensemble $\nu$ :
   $$\int_X s \, d\nu = \sum_{i=1}^n c_i \nu(A_i)$$
3. Remplaçons $\nu(A_i)$ par sa définition :
   $$\nu(A_i) = \int_X f \cdot \mathbf{1}_{A_i} \, d\mu$$
4. On a donc :
   $$\int_X s \, d\nu = \sum_{i=1}^n c_i \left( \int_X f \cdot \mathbf{1}_{A_i} \, d\mu \right)$$
5. Par la propriété d'homogénéité (mise en évidence d'une constante hors de l'intégrale) :
   $$\int_X s \, d\nu = \sum_{i=1}^n \int_X c_i \cdot f \cdot \mathbf{1}_{A_i} \, d\mu$$
6. En utilisant la linéarité de l'intégrale pour les fonctions positives (somme finie) :
   $$\int_X s \, d\nu = \int_X \left( \sum_{i=1}^n c_i \cdot f \cdot \mathbf{1}_{A_i} \right) \, d\mu$$
7. Factorisons $f$ à l'intérieur de l'intégrale :
   $$\sum_{i=1}^n c_i \cdot f \cdot \mathbf{1}_{A_i} = f \cdot \left( \sum_{i=1}^n c_i \mathbf{1}_{A_i} \right) = f \cdot s$$
8. On conclut que :
   $$\int_X s \, d\nu = \int_X s \cdot f \, d\mu$$
   Ce résultat fondamental permet de montrer que $\nu$ est bien une mesure (mesure à densité) et de généraliser cette égalité à toute fonction mesurable positive (formule de changement de mesure).

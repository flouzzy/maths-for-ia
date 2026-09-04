# Exercice 09 : Continuité de la mesure sur une union dénombrable ($\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$)

## Énoncé

Soit $(A_n)$ une suite d'ensembles mesurables disjoints. Démontrer l'additivité dénombrable $\mu(\bigcup_{n=1}^\infty A_n) = \sum_{n=1}^\infty \mu(A_n)$ en utilisant l'intégrale de Lebesgue et Beppo Levi.

## Correction Détaillée

1. **Indicatrices :** Soit $E = \bigcup_{n=1}^\infty A_n$. Puisque les ensembles $(A_n)$ sont deux à deux disjoints, l'indicatrice de leur union est la somme de leurs indicatrices :
   $$ \mathbf{1}_E(x) = \sum_{n=1}^\infty \mathbf{1}_{A_n}(x) $$
2. **Mesure par intégrale :** Par définition de l'intégrale d'une fonction étagée (et indicatrice), la mesure d'un ensemble est l'intégrale de son indicatrice :
   $$ \mu(E) = \int_X \mathbf{1}_E \,d\mu $$
3. **Application de Beppo Levi :** La suite de fonctions $u_n(x) = \mathbf{1}_{A_n}(x)$ est une suite de fonctions mesurables positives. Le corollaire de Beppo Levi stipule que l'intégrale d'une somme de fonctions positives est la somme de leurs intégrales.
4. **Interversion :**
   $$ \mu(E) = \int_X \left( \sum_{n=1}^\infty \mathbf{1}_{A_n} \right) \,d\mu = \sum_{n=1}^\infty \int_X \mathbf{1}_{A_n} \,d\mu $$
5. **Conclusion finale :** Comme $\int_X \mathbf{1}_{A_n} \,d\mu = \mu(A_n)$, on en déduit :
   $$ \mu\left(\bigcup_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty \mu(A_n) $$
   L'additivité dénombrable des mesures est donc structurellement encodée dans le théorème de convergence monotone.

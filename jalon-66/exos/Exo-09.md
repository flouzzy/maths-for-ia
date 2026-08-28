# Exercice 9 : Changement de mesure \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $g \in \mathcal{M}_+$. On définit $\nu(A) = \int_X g \mathbf{1}_A \, d\mu$ pour tout $A \in \mathcal{F}$.
Prouver que pour toute fonction simple positive $s$, $\int_X s \, d\nu = \int_X s g \, d\mu$.

**Correction :**
Soit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ une fonction simple positive sous sa forme canonique.

Par définition de l'intégrale d'une fonction simple par rapport à $\nu$ :
$\int_X s \, d\nu = \sum_{i=1}^n a_i \nu(A_i)$.

Par définition de $\nu(A_i)$ :
$\nu(A_i) = \int_X g \mathbf{1}_{A_i} \, d\mu$.

En substituant :
$\int_X s \, d\nu = \sum_{i=1}^n a_i \left( \int_X g \mathbf{1}_{A_i} \, d\mu \right)$.

Par propriété de linéarité (multiplication par un scalaire et somme finie) de l'intégrale des fonctions mesurables positives :
$\int_X s \, d\nu = \int_X \left( \sum_{i=1}^n a_i g \mathbf{1}_{A_i} \right) \, d\mu$.

Or, $\sum_{i=1}^n a_i g(x) \mathbf{1}_{A_i}(x) = g(x) \sum_{i=1}^n a_i \mathbf{1}_{A_i}(x) = g(x) s(x)$.

Donc $\int_X s \, d\nu = \int_X s g \, d\mu$.

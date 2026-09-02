# Exo 05 : Mesure d'une union dénombrable ($\bigstar$\bigstar$\bigstar\star\star$)

## Énoncé
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $(A_n)_{n \ge 0}$ une suite d'ensembles mesurables, deux à deux disjoints. On pose $A = \bigcup_{n=0}^\infty A_n$.
En utilisant les fonctions indicatrices et le théorème de convergence monotone, démontrer la $\sigma$-additivité de la mesure :
$\mu(A) = \sum_{n=0}^\infty \mu(A_n)$.

## Correction Détaillée
**Étape 1 : Expression par des fonctions indicatrices**
Puisque les ensembles $A_n$ sont disjoints, l'indicatrice de la réunion s'écrit comme la somme infinie des indicatrices :
$$ \mathbf{1}_A = \sum_{n=0}^\infty \mathbf{1}_{A_n} $$

**Étape 2 : Application du théorème de sommation**
On sait que l'intégrale d'une fonction indicatrice d'un ensemble mesurable donne la mesure de cet ensemble :
$$ \int_X \mathbf{1}_E \, d\mu = \mu(E) $$
Les fonctions $u_n = \mathbf{1}_{A_n}$ sont mesurables et positives. Par le corollaire du TCM (intégration terme à terme d'une série à termes positifs) :
$$ \int_X \left( \sum_{n=0}^\infty \mathbf{1}_{A_n} \right) d\mu = \sum_{n=0}^\infty \int_X \mathbf{1}_{A_n} \, d\mu $$
On substitue les intégrales par les mesures :
$$ \int_X \mathbf{1}_A \, d\mu = \sum_{n=0}^\infty \mu(A_n) $$
D'où finalement :
$$ \mu(A) = \sum_{n=0}^\infty \mu(A_n) $$
Cela démontre que la construction de l'intégrale de Lebesgue via Beppo Levi est en parfaite cohérence avec les axiomes fondamentaux de la théorie de la mesure.

# Exercice 10 : Mesure à densité et TCM $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $f : X \to [0, \infty]$ une fonction mesurable.
On définit $\nu(A) = \int_A f d\mu$ pour tout $A \in \mathcal{F}$.
Montrer que $\nu$ est une mesure (la $\sigma$-additivité repose sur le TCM).

## Correction Détaillée
1. Par définition, $f$ est à valeurs positives, donc $\nu(A) \in [0, \infty]$. De plus, $\nu(\emptyset) = \int_{\emptyset} f d\mu = 0$.
2. Il reste à prouver la $\sigma$-additivité. Soit $(A_n)_{n \ge 1}$ une suite d'ensembles mesurables disjoints. Soit $A = \bigcup_{n=1}^\infty A_n$.
3. La fonction indicatrice de $A$ s'écrit comme la série des indicatrices des $A_n$ :
   $\mathbf{1}_A(x) = \sum_{n=1}^\infty \mathbf{1}_{A_n}(x)$.
4. L'intégrale de $f$ sur $A$ s'écrit :
   $$ \nu(A) = \int_X f \cdot \mathbf{1}_A d\mu = \int_X f \cdot \left( \sum_{n=1}^\infty \mathbf{1}_{A_n} \right) d\mu = \int_X \left( \sum_{n=1}^\infty f \cdot \mathbf{1}_{A_n} \right) d\mu $$
5. Les fonctions $u_n = f \cdot \mathbf{1}_{A_n}$ sont mesurables et positives.
6. Le corollaire de Beppo Levi pour les séries (sommation terme à terme) donne le droit d'intervertir la somme infinie et l'intégrale :
   $$ \int_X \left( \sum_{n=1}^\infty u_n \right) d\mu = \sum_{n=1}^\infty \int_X u_n d\mu $$
7. On reconnait les intégrales sur les $A_n$ :
   $$ \nu(A) = \sum_{n=1}^\infty \int_{A_n} f d\mu = \sum_{n=1}^\infty \nu(A_n) $$
8. La fonction d'ensemble $\nu$ est donc bien une mesure, on l'appelle mesure de densité $f$ par rapport à $\mu$.

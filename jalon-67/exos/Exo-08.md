# Exercice 8 : Produit scalaire fonctionnel infini \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f(x) = \sum_{k=1}^\infty \frac{\sin^2(kx)}{k^2}$ pour $x \in [0, \pi]$. Calculer $\int_{0}^{\pi} f(x) dx$.

**Solution Détaillée :**
1. Posons $u_k(x) = \frac{\sin^2(kx)}{k^2}$. Ces fonctions sont mesurables et **positives** (le carré garantit la positivité).
2. Nous sommes exactement dans le cadre du corollaire du TCM pour l'intégration des séries de fonctions positives.
3. On peut intervertir somme et intégrale :
   $$ \int_{0}^{\pi} \left( \sum_{k=1}^\infty \frac{\sin^2(kx)}{k^2} \right) dx = \sum_{k=1}^\infty \int_{0}^{\pi} \frac{\sin^2(kx)}{k^2} dx $$
4. Calculons l'intégrale de $\sin^2(kx)$.
   $\sin^2(kx) = \frac{1 - \cos(2kx)}{2}$.
   $$ \int_{0}^{\pi} \sin^2(kx) dx = \int_{0}^{\pi} \frac{1 - \cos(2kx)}{2} dx = \left[ \frac{x}{2} - \frac{\sin(2kx)}{4k} \right]_0^\pi = \frac{\pi}{2} $$
5. Remplaçons dans la somme :
   $$ \sum_{k=1}^\infty \frac{1}{k^2} \left( \frac{\pi}{2} \right) = \frac{\pi}{2} \sum_{k=1}^\infty \frac{1}{k^2} $$
6. On utilise la valeur classique (problème de Bâle) : $\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$.
7. L'intégrale vaut donc $\frac{\pi}{2} \times \frac{\pi^2}{6} = \frac{\pi^3}{12}$.

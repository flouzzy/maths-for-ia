## Exercice 3 : Mesure de densité $\quad \bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $f \in \mathcal{M}_+$.
Pour tout $A \in \mathcal{F}$, on pose $\nu(A) = \int_A f d\mu = \int_X f \mathbf{1}_A d\mu$.
Montrer que $\nu$ est une mesure sur $\mathcal{F}$.

**Correction :**
1. $\nu(\emptyset) = \int f \mathbf{1}_{\emptyset} d\mu = \int 0 d\mu = 0$.
2. Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles mesurables deux à deux disjoints. Posons $A = \bigcup_{n=0}^\infty A_n$.
On a $\mathbf{1}_A = \sum_{n=0}^\infty \mathbf{1}_{A_n}$.
Considérons les sommes partielles $g_k = \sum_{n=0}^k f \mathbf{1}_{A_n}$.
La suite $(g_k)$ est une suite croissante de fonctions mesurables positives, et elle converge simplement vers $g = f \mathbf{1}_A$.
D'après le théorème de convergence monotone, $\int g d\mu = \lim_{k \to \infty} \int g_k d\mu$.
Or, par linéarité, $\int g_k d\mu = \sum_{n=0}^k \int f \mathbf{1}_{A_n} d\mu = \sum_{n=0}^k \nu(A_n)$.
Donc $\nu(A) = \lim_{k \to \infty} \sum_{n=0}^k \nu(A_n) = \sum_{n=0}^\infty \nu(A_n)$.
Ainsi, $\nu$ est bien une mesure (sigma-additive).

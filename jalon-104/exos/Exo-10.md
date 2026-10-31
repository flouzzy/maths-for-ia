# Exercice 10 : Convergence faible vs Convergence forte $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $H$ un espace de Hilbert de dimension infinie et $(e_n)_{n \in \mathbb{N}}$ une base hilbertienne de $H$.
1. Montrer que la suite $(e_n)$ converge faiblement vers $0$, c'est-à-dire que pour tout $x \in H$, $\lim_{n \to \infty} \langle e_n, x \rangle = 0$.
2. Montrer que la suite $(e_n)$ ne converge pas fortement dans $H$ (i.e., elle ne converge pas pour la norme $\| \cdot \|$).

**Correction détaillée :**
1. Soit $x \in H$. Puisque $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne, l'identité de Parseval s'applique à $x$ :
   $\|x\|^2 = \sum_{n=0}^\infty |\langle x, e_n \rangle|^2 < \infty$.
   La série numérique à termes positifs $\sum |\langle x, e_n \rangle|^2$ est convergente.
   Une condition nécessaire de convergence d'une série numérique est que le terme général tende vers zéro.
   Par conséquent, $\lim_{n \to \infty} |\langle x, e_n \rangle|^2 = 0$.
   Cela implique que $\lim_{n \to \infty} \langle x, e_n \rangle = 0$.
   Par symétrie hermitienne du produit scalaire, $\langle e_n, x \rangle = \overline{\langle x, e_n \rangle}$, donc :
   $\lim_{n \to \infty} \langle e_n, x \rangle = 0$.
   La définition de la convergence faible de $e_n$ vers $0$ est satisfaite.

2. Montrons que la suite $(e_n)$ n'est pas de Cauchy pour la norme forte.
   Pour tout $n, m \in \mathbb{N}$ avec $n \neq m$, calculons la norme de la différence :
   $\|e_n - e_m\|^2 = \langle e_n - e_m, e_n - e_m \rangle = \|e_n\|^2 - 2 \text{Re}(\langle e_n, e_m \rangle) + \|e_m\|^2$
   Puisque la famille est orthonormée, $\|e_n\| = \|e_m\| = 1$ et $\langle e_n, e_m \rangle = 0$.
   Donc $\|e_n - e_m\|^2 = 1 - 0 + 1 = 2$.
   On en déduit que $\|e_n - e_m\| = \sqrt{2}$ pour tout $n \neq m$.
   La distance entre deux termes distincts quelconques de la suite est constante et vaut $\sqrt{2}$. La suite ne peut donc pas vérifier le critère de Cauchy (pour lequel les termes doivent se rapprocher arbitrairement près les uns des autres à partir d'un certain rang).
   Puisque l'espace $H$ est complet, une suite converge fortement si et seulement si elle est de Cauchy. La suite $(e_n)$ ne converge donc pas fortement.
   *(Note géométrique : la suite correspond aux points d'une sphère unité de dimension infinie, chaque point étant situé sur un axe orthogonal différent, la distance entre eux est toujours la diagonale d'un carré unité).*

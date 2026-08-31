## Exercice 1 : Application directe du théorème \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $A_n$ une suite croissante d'ensembles mesurables, c'est-à-dire $A_n \subset A_{n+1}$. Soit $A = \bigcup_{n=1}^\infty A_n$. En utilisant le théorème de convergence monotone appliqué aux fonctions indicatrices, démontrer que $\mu(A) = \lim_{n \to \infty} \mu(A_n)$.

**Correction Détaillée :**
1. Considérons la suite de fonctions indicatrices $f_n = \chi_{A_n}$.
2. Puisque $A_n \subset A_{n+1}$, pour tout $x \in X$, on a $f_n(x) \le f_{n+1}(x)$. La suite $(f_n)$ est donc croissante et composée de fonctions mesurables positives.
3. Pour tout $x \in A$, il existe un entier $N$ tel que $x \in A_N$, donc pour tout $n \ge N$, $x \in A_n$ et $f_n(x) = 1$. Ainsi $\lim f_n(x) = 1 = \chi_A(x)$.
   Si $x \notin A$, alors $x \notin A_n$ pour tout $n$, donc $\lim f_n(x) = 0 = \chi_A(x)$.
   On a bien $\lim f_n = \chi_A$.
4. D'après le théorème de convergence monotone, $\int_X \chi_A d\mu = \lim_{n \to \infty} \int_X \chi_{A_n} d\mu$.
5. Or, par définition, $\int_X \chi_{A} d\mu = \mu(A)$ et $\int_X \chi_{A_n} d\mu = \mu(A_n)$.
6. On conclut donc que $\mu(A) = \lim_{n \to \infty} \mu(A_n)$.

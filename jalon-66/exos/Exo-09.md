## Exercice 9 : Fonction de mesure de niveau \quad $$\bigstar\bigstar\bigstar\star$$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré fini. Soit $f \in \mathcal{M}_+$.
On définit $A_n = \{x \in X \mid f(x) \ge n\}$ pour $n \in \mathbb{N}^*$.
Montrer que si $\sum_{n=1}^\infty \mu(A_n) = +\infty$, alors $f$ n'est pas intégrable.

**Correction :**
1. Pour tout entier $N \ge 1$, on peut définir la fonction étagée :
   $$s_N = \sum_{n=1}^N \mathbf{1}_{A_n}$$
2. Remarquons que si $x$ est tel que $k \le f(x) < k+1$, alors $x \in A_n$ pour $n \le k$ et $x \notin A_n$ pour $n > k$.
   Ainsi, $s_N(x) = \min(k, N) \le f(x)$.
3. Donc, pour tout $N$, $s_N \le f$ sur tout $X$, et $s_N \in \mathcal{E}_+$.
4. L'intégrale de $s_N$ est :
   $$\int_X s_N \, d\mu = \sum_{n=1}^N \int_X \mathbf{1}_{A_n} \, d\mu = \sum_{n=1}^N \mu(A_n)$$
5. Par croissance de l'intégrale de Lebesgue, on a :
   $$\int_X f \, d\mu \ge \int_X s_N \, d\mu = \sum_{n=1}^N \mu(A_n)$$
6. Si la série $\sum \mu(A_n)$ diverge, la limite quand $N \to \infty$ du membre de droite est $+\infty$.
7. Par conséquent, $\int_X f \, d\mu = +\infty$, ce qui signifie par définition que $f$ n'est pas intégrable.

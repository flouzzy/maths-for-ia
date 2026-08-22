# Exercice 4 : Intégrale de la fonction partie entière $\bigstar\bigstar\star\star\star$

**Énoncé :**
Calculer l'intégrale de Lebesgue de la fonction $f(x) = \lfloor x \rfloor$ sur le segment $[0, n]$ où $n \in \mathbb{N}^*$, par rapport à la mesure de Lebesgue $\lambda$.

**Correction Détaillée :**
1. La fonction $f(x) = \lfloor x \rfloor$ sur $[0, n]$ prend des valeurs entières constantes sur des intervalles.
2. Décomposons le segment $[0, n]$ en union disjointe d'intervalles :
   $[0, n] = \bigcup_{k=0}^{n-1} [k, k+1[ \cup \{n\}$
3. Sur chaque intervalle $[k, k+1[$, on a $f(x) = k$. Sur $\{n\}$, on a $f(n) = n$.
4. $f$ s'écrit donc comme une fonction étagée positive :
   $f = \sum_{k=0}^{n-1} k \cdot \mathbf{1}_{[k, k+1[} + n \cdot \mathbf{1}_{\{n\}}$
5. Calculons son intégrale :
   $$\int_{[0, n]} f \, d\lambda = \sum_{k=0}^{n-1} k \cdot \lambda([k, k+1[) + n \cdot \lambda(\{n\})$$
6. On a $\lambda([k, k+1[) = (k+1) - k = 1$. L'ensemble $\{n\}$ est un singleton, donc sa mesure de Lebesgue est $\lambda(\{n\}) = 0$.
7. L'intégrale devient :
   $$\int_{[0, n]} f \, d\lambda = \sum_{k=0}^{n-1} k \times 1 + n \times 0 = \sum_{k=0}^{n-1} k$$
8. C'est la somme des premiers entiers :
   $$\sum_{k=0}^{n-1} k = \frac{(n-1)n}{2}$$

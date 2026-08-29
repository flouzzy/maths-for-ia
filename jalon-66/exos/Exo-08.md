## Exercice 8 : Intégrale d'une fonction discrète \quad $$\bigstar\bigstar\bigstar\star$$

**Énoncé :**
Soit $\mathbb{N}$ muni de la mesure de comptage $\mu$ (i.e. $\mu(\{n\}) = 1$).
Considérons la fonction mesurable positive $f(n) = \frac{1}{2^n}$.
Calculer $\int_{\mathbb{N}} f \, d\mu$ en approchant $f$ par des fonctions étagées.

**Correction :**
1. Soit la suite de fonctions étagées $s_N(n) = f(n) \mathbf{1}_{\{0, 1, \dots, N\}}(n)$.
2. Pour chaque $N$, $s_N \in \mathcal{E}_+$ et $0 \le s_N \le f$.
3. L'intégrale de $s_N$ par rapport à la mesure de comptage est :
   $$\int_{\mathbb{N}} s_N \, d\mu = \sum_{n=0}^N \frac{1}{2^n} \mu(\{n\}) = \sum_{n=0}^N \frac{1}{2^n}$$
4. C'est la somme partielle d'une série géométrique de raison $1/2$.
   $$\sum_{n=0}^N \left(\frac{1}{2}\right)^n = \frac{1 - (1/2)^{N+1}}{1 - 1/2} = 2 \left(1 - \frac{1}{2^{N+1}}\right)$$
5. Puisque $s_N \le f$, on a $\int_{\mathbb{N}} s_N \, d\mu \le \int_{\mathbb{N}} f \, d\mu$.
6. En prenant la limite $N \to \infty$, on obtient $2 \le \int_{\mathbb{N}} f \, d\mu$.
7. D'autre part, toute fonction étagée $s \le f$ ne possède qu'un nombre fini de valeurs non nulles, et est donc dominée par un certain $s_M$. Le supremum coïncide donc avec la limite.
8. Ainsi, $\int_{\mathbb{N}} f \, d\mu = 2$.

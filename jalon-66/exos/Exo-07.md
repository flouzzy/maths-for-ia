## Exercice 7 : Approximation par le bas \quad $$\bigstar\bigstar\bigstar$$

**Énoncé :**
Soit $f(x) = x$ sur $[0, 1]$ muni de la mesure de Lebesgue $\lambda$.
On définit les fonctions étagées $s_n(x) = \sum_{k=0}^{n-1} \frac{k}{n} \mathbf{1}_{[\frac{k}{n}, \frac{k+1}{n})}(x)$.
Calculer $\int_{[0, 1]} s_n \, d\lambda$ et trouver sa limite quand $n \to \infty$.

**Correction :**
1. $s_n$ est une fonction étagée, ses valeurs sont $\frac{k}{n}$ pour $0 \le k \le n-1$.
2. La mesure de chaque intervalle $[\frac{k}{n}, \frac{k+1}{n})$ est $\frac{1}{n}$.
3. Ainsi, l'intégrale de $s_n$ est la somme :
   $$\int_{[0, 1]} s_n \, d\lambda = \sum_{k=0}^{n-1} \frac{k}{n} \lambda\left(\left[\frac{k}{n}, \frac{k+1}{n}\right)\right) = \sum_{k=0}^{n-1} \frac{k}{n} \cdot \frac{1}{n} = \frac{1}{n^2} \sum_{k=0}^{n-1} k$$
4. On sait que $\sum_{k=0}^{n-1} k = \frac{(n-1)n}{2}$.
5. L'intégrale vaut donc $\frac{(n-1)n}{2n^2} = \frac{n-1}{2n} = \frac{1}{2} - \frac{1}{2n}$.
6. Quand $n \to \infty$, $\lim_{n \to \infty} \left( \frac{1}{2} - \frac{1}{2n} \right) = \frac{1}{2}$.
7. Ceci prouve rigoureusement que l'intégrale de Lebesgue de $x \mapsto x$ sur $[0, 1]$ est supérieure ou égale à $1/2$. (Elle est exactement de $1/2$ par le théorème de convergence monotone).

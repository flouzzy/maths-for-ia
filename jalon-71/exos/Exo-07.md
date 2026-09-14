## Exercice 7 : Fubini-Tonelli pour des séries doubles \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Les séries doubles sont des intégrales par rapport à la mesure de comptage.
Calculer $S = \sum_{n=1}^\infty \sum_{m=1}^\infty \frac{1}{(n+m)^3}$.

**Correction :**
1. Les termes $u_{n,m} = \frac{1}{(n+m)^3}$ sont strictement positifs. Tonelli assure que la sommation peut se faire dans n'importe quel ordre, y compris par "diagonales".
2. Posons $k = n + m$. Puisque $n \ge 1$ et $m \ge 1$, $k$ varie de $2$ à l'infini.
3. Pour un $k$ donné, combien y a-t-il de paires $(n, m)$ telles que $n+m = k$ ?
   On a $m = k - n$. Comme $m \ge 1$, on a $k - n \ge 1$, soit $n \le k - 1$.
   Puisque $n \ge 1$, $n$ prend les valeurs entières de $1$ à $k-1$.
   Il y a donc $k - 1$ paires possibles pour chaque somme $k$.
4. Réécrivons la double somme (ce qui correspond à un changement de variable garanti par Tonelli) :
   $$ S = \sum_{k=2}^\infty \sum_{(n,m) | n+m=k} \frac{1}{k^3} = \sum_{k=2}^\infty \frac{\text{nombre de paires}}{k^3} = \sum_{k=2}^\infty \frac{k-1}{k^3} $$
5. Séparons la fraction :
   $$ S = \sum_{k=2}^\infty \left( \frac{k}{k^3} - \frac{1}{k^3} \right) = \sum_{k=2}^\infty \frac{1}{k^2} - \sum_{k=2}^\infty \frac{1}{k^3} $$
6. Or, on connaît la fonction zêta de Riemann : $\zeta(s) = \sum_{k=1}^\infty \frac{1}{k^s}$.
   $$ \sum_{k=2}^\infty \frac{1}{k^2} = \zeta(2) - 1 = \frac{\pi^2}{6} - 1 $$
   $$ \sum_{k=2}^\infty \frac{1}{k^3} = \zeta(3) - 1 $$
7. Finalement, $S = \zeta(2) - 1 - (\zeta(3) - 1) = \frac{\pi^2}{6} - \zeta(3)$.

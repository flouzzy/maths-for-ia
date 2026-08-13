### Exercice 3 : Test de Weierstrass (Convergence Normale) \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Étudier la convergence (simple, absolue, uniforme) de la série de fonctions $\sum_{n=1}^\infty \frac{\cos(nx)}{n^2 + x^2}$ sur $\mathbb{R}$.

**Correction :**
On cherche à majorer uniformément le terme général en valeur absolue par le terme d'une série convergente indépendante de $x$.
Pour tout $x \in \mathbb{R}$ et $n \ge 1$,
$$ \left| \frac{\cos(nx)}{n^2 + x^2} \right| \le \frac{1}{n^2 + x^2} \le \frac{1}{n^2} $$
La série numérique $\sum_{n \ge 1} \frac{1}{n^2}$ est une série de Riemann convergente.
Par conséquent, par le critère de Weierstrass, la série de fonctions converge normalement sur $\mathbb{R}$.
Comme toute convergence normale implique la convergence uniforme, la série converge uniformément (et absolument, car la majoration porte sur la valeur absolue) sur $\mathbb{R}$.

## Exercice 4 : Fonctions bornées sur mesure finie $\quad \bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $\mu(X) < \infty$. Montrer que si $f \in \mathcal{M}_+$ est bornée, alors $\int f d\mu < \infty$.

**Correction :**
Supposons que $f$ est bornée par une constante $M > 0$. Ainsi, pour tout $x \in X$, $0 \le f(x) \le M$.
On a donc $f \le M \mathbf{1}_X$.
Par la propriété de croissance de l'intégrale (démontrée pour les fonctions simples puis étendue) :
$\int f d\mu \le \int M \mathbf{1}_X d\mu = M \mu(X)$.
Comme $\mu(X) < \infty$, l'intégrale de $f$ est majorée par une valeur finie.
Donc $\int f d\mu < \infty$.

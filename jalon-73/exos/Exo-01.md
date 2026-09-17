# Exercice 1 : Comparaison des normes $L^p$ sur un espace de mesure finie \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré tel que $\mu(X) < +\infty$.
Montrer que si $1 \le p \le q < +\infty$, alors $L^q(\mu) \subset L^p(\mu)$.

**Correction :**
Soit $f \in L^q(\mu)$. On doit montrer que $\int_X |f|^p d\mu < +\infty$.
On décompose l'intégrale sur deux sous-ensembles :
$A = \{x \in X \mid |f(x)| \le 1\}$ et $B = \{x \in X \mid |f(x)| > 1\}$.

Sur $A$, on a $|f(x)|^p \le 1$, donc $\int_A |f|^p d\mu \le \int_A 1 d\mu = \mu(A) \le \mu(X) < +\infty$.

Sur $B$, comme $q \ge p$ et $|f(x)| > 1$, on a $|f(x)|^p \le |f(x)|^q$.
Donc $\int_B |f|^p d\mu \le \int_B |f|^q d\mu$.
Or, comme $f \in L^q(\mu)$, $\int_X |f|^q d\mu < +\infty$, donc $\int_B |f|^q d\mu \le \int_X |f|^q d\mu < +\infty$.

En sommant, $\int_X |f|^p d\mu = \int_A |f|^p d\mu + \int_B |f|^p d\mu \le \mu(X) + \int_X |f|^q d\mu < +\infty$.
Ainsi, $f \in L^p(\mu)$. L'inclusion $L^q(\mu) \subset L^p(\mu)$ est démontrée.

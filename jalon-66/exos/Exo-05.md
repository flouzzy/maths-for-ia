## Exercice 5 : Inégalité de Markov $\quad \bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+$. Montrer que pour tout $t > 0$, $\mu(\{x \in X \mid f(x) \ge t\}) \le \frac{1}{t} \int f d\mu$.

**Correction :**
Soit $A_t = \{x \in X \mid f(x) \ge t\}$. L'ensemble $A_t$ est mesurable car $f$ l'est.
Remarquons que $f \ge t \mathbf{1}_{A_t}$ partout sur $X$.
En effet, si $x \in A_t$, $f(x) \ge t = t \cdot 1$. Si $x \notin A_t$, $f(x) \ge 0 = t \cdot 0$.
Par croissance de l'intégrale :
$\int f d\mu \ge \int t \mathbf{1}_{A_t} d\mu = t \mu(A_t)$.
En divisant par $t > 0$, on obtient bien l'inégalité de Markov : $\mu(A_t) \le \frac{1}{t} \int f d\mu$.

## Exercice 1 : Intégrabilité et mesure nulle $\quad \bigstar\star\star\star\star$

**Énoncé :**
Montrer que si $f, g \in \mathcal{M}_+$ et $f \le g$ presque partout, alors $\int f d\mu \le \int g d\mu$.

**Correction :**
Soit $N = \{x \in X \mid f(x) > g(x)\}$. Par hypothèse, $\mu(N) = 0$.
Soit $s \in \mathcal{S}_+$ telle que $s \le f$.
Définissons $s' = s \mathbf{1}_{X \setminus N}$. Puisque $\mu(N) = 0$, on a $\int s d\mu = \int s' d\mu$.
Sur $X \setminus N$, $s' \le f \le g$. Donc $s'$ est une fonction simple minorant $g$ presque partout.
On peut construire une fonction simple $\tilde{s} \le g$ partout telle que $\int \tilde{s} d\mu = \int s d\mu$.
Par définition du supremum, $\int s d\mu \le \int g d\mu$.
En prenant le supremum sur toutes les fonctions simples $s \le f$, on obtient $\int f d\mu \le \int g d\mu$.
